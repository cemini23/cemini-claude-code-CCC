#!/usr/bin/env python3
"""Keep one claude-mem worker on the latest plugin version.

Stops the 13.15.x vs 13.16.x fight that lock every Cursor/Claude Code
workspace after CLAUDE_MEM_HOOK_FAIL_LOUD_THRESHOLD consecutive misses.

Subcommands:
  run    unify cache, then exec the latest worker in the foreground (launchd)
  watch  health-check, reset the hook lock, kick the worker if needed
  unify  cache/settings only (no exec)
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
CACHE = HOME / ".claude/plugins/cache/thedotmack/claude-mem"
INSTALLED = HOME / ".claude/plugins/installed_plugins.json"
DATA = HOME / ".claude-mem"
SETTINGS = DATA / "settings.json"
HOOK_FAILURES = DATA / "state/hook-failures.json"
BUN_CANDIDATES = (
    HOME / ".bun/bin/bun",
    Path("/opt/homebrew/bin/bun"),
    Path("/usr/local/bin/bun"),
)
WORKER_LABEL = "gui/{uid}/com.cemini.claude-mem-worker"
FAIL_LOUD_THRESHOLD = "10000"
CHROMA_MAX = 8
TRAMPOLINE_MARK = "cemini-claude-mem-trampoline"

TRAMPOLINE = '''#!/usr/bin/env bun
"use strict";
// {mark} — old plugin versions must not bind the worker port
const {{ spawn }} = require("child_process");
const path = require("path");
const os = require("os");
const target = {target!r};
const pluginRoot = {root!r};
const bun = process.execPath;
const env = {{ ...process.env, CLAUDE_PLUGIN_ROOT: pluginRoot }};
const args = [target, ...process.argv.slice(2)];
const daemonish = process.argv.includes("--daemon") || process.argv[2] === "start";
if (daemonish) {{
  const child = spawn(bun, args, {{ stdio: "inherit", detached: true, env, windowsHide: true }});
  child.unref();
  process.exit(0);
}}
const child = spawn(bun, args, {{ stdio: "inherit", env, windowsHide: true }});
child.on("exit", (c, s) => process.exit(c == null ? (s ? 1 : 0) : c));
child.on("error", (e) => {{ console.error(e); process.exit(1); }});
'''


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def version_key(name: str) -> tuple:
    core = name.split("-")[0]
    parts = core.split(".")
    nums = []
    for p in parts[:3]:
        try:
            nums.append(int(p))
        except ValueError:
            nums.append(0)
    while len(nums) < 3:
        nums.append(0)
    # Prefer release dirs over prerelease (name with hyphen after version)
    return (nums[0], nums[1], nums[2], 0 if "-" in name else 1)


def plugin_dirs() -> list[Path]:
    if not CACHE.is_dir():
        return []
    out = []
    for p in CACHE.iterdir():
        if p.is_dir() and p.name[:1].isdigit() and not (p / ".orphaned_at").exists():
            out.append(p)
    # include orphaned when listing "all" for trampoline; this helper is live-only
    return sorted(out, key=lambda p: version_key(p.name))


def all_plugin_dirs() -> list[Path]:
    if not CACHE.is_dir():
        return []
    return sorted(
        [p for p in CACHE.iterdir() if p.is_dir() and p.name[:1].isdigit()],
        key=lambda p: version_key(p.name),
    )


def latest_plugin() -> Path:
    live = plugin_dirs()
    if live:
        return live[-1]
    all_dirs = all_plugin_dirs()
    if not all_dirs:
        raise SystemExit(f"no claude-mem plugin cache under {CACHE}")
    return all_dirs[-1]


def bun_bin() -> Path:
    which = shutil.which("bun")
    if which:
        return Path(which)
    for p in BUN_CANDIDATES:
        if p.is_file() and os.access(p, os.X_OK):
            return p
    raise SystemExit("bun not found")


def worker_port() -> int:
    settings = load_json(SETTINGS, {})
    raw = settings.get("CLAUDE_MEM_WORKER_PORT")
    if raw:
        try:
            return int(raw)
        except (TypeError, ValueError):
            pass
    return 37700 + (os.getuid() % 100)


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return default


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    os.replace(tmp, path)


def health(timeout: float = 2.0) -> dict | None:
    url = f"http://127.0.0.1:{worker_port()}/api/health"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError, ValueError):
        return None


def merge_settings() -> None:
    data = load_json(SETTINGS, {})
    if not isinstance(data, dict):
        data = {}
    data["CLAUDE_MEM_RUNTIME"] = data.get("CLAUDE_MEM_RUNTIME") or "worker"
    data["CLAUDE_MEM_HOOK_FAIL_LOUD_THRESHOLD"] = FAIL_LOUD_THRESHOLD
    write_json(SETTINGS, data)


def orphan_older(latest: Path) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for p in all_plugin_dirs():
        if p == latest:
            marker = p / ".orphaned_at"
            if marker.exists():
                marker.unlink()
            continue
        marker = p / ".orphaned_at"
        if not marker.exists():
            marker.write_text(stamp + "\n")
            log(f"orphaned {p.name}")


def trampoline_older(latest: Path) -> None:
    target = str(latest / "scripts/worker-service.cjs")
    root = str(latest)
    body = TRAMPOLINE.format(mark=TRAMPOLINE_MARK, target=target, root=root)
    for p in all_plugin_dirs():
        if p == latest:
            continue
        script = p / "scripts/worker-service.cjs"
        if not script.parent.is_dir():
            continue
        existing = script.read_text() if script.exists() else ""
        if TRAMPOLINE_MARK in existing:
            continue
        bak = script.with_suffix(".cjs.pre-trampoline")
        if script.exists() and not bak.exists():
            shutil.copy2(script, bak)
        script.write_text(body)
        script.chmod(0o755)
        log(f"trampolined {p.name} -> {latest.name}")


def ensure_node_modules(latest: Path) -> None:
    nm = latest / "node_modules"
    entries = []
    if nm.is_dir():
        entries = [x for x in nm.iterdir() if x.name != ".bin"]
    if entries:
        return
    bun = bun_bin()
    log(f"bun install in {latest}")
    subprocess.run(
        [str(bun), "install", "--frozen-lockfile"],
        cwd=str(latest),
        check=False,
        timeout=180,
    )


def pin_installed_plugins(latest: Path) -> None:
    data = load_json(INSTALLED, {})
    plugins = data.setdefault("plugins", {})
    key = "claude-mem@thedotmack"
    entries = plugins.get(key) or [{}]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    first = entries[0] if isinstance(entries[0], dict) else {}
    first["scope"] = first.get("scope") or "user"
    first["installPath"] = str(latest)
    first["version"] = latest.name
    first["installedAt"] = first.get("installedAt") or now
    first["lastUpdated"] = now
    plugins[key] = [first]
    write_json(INSTALLED, data)


def reset_hook_failures() -> None:
    current = load_json(HOOK_FAILURES, {})
    n = current.get("consecutiveFailures") if isinstance(current, dict) else 0
    if n:
        log(f"reset hook-failures {n} -> 0")
    write_json(HOOK_FAILURES, {"consecutiveFailures": 0, "lastFailureAt": None})


def kill_workers() -> None:
    subprocess.run(
        ["pkill", "-f", "/claude-mem/.*/scripts/worker-service"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(0.4)
    subprocess.run(
        ["pkill", "-9", "-f", "/claude-mem/.*/scripts/worker-service"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def cull_chroma() -> None:
    try:
        out = subprocess.check_output(["pgrep", "-f", "chroma-mcp --client-type persistent --data-dir"], text=True)
        pids = [p for p in out.split() if p.strip()]
    except subprocess.CalledProcessError:
        return
    if len(pids) <= CHROMA_MAX:
        return
    log(f"culling chroma-mcp swarm ({len(pids)} procs)")
    subprocess.run(
        ["pkill", "-f", "chroma-mcp --client-type persistent --data-dir"],
        check=False,
    )


def unify() -> Path:
    DATA.mkdir(parents=True, exist_ok=True)
    latest = latest_plugin()
    merge_settings()
    orphan_older(latest)
    trampoline_older(latest)
    ensure_node_modules(latest)
    pin_installed_plugins(latest)
    return latest


def cmd_unify() -> int:
    latest = unify()
    log(f"unified latest={latest.name}")
    return 0


def cmd_run() -> int:
    latest = unify()
    worker = latest / "scripts/worker-service.cjs"
    if not worker.is_file():
        raise SystemExit(f"missing {worker}")
    kill_workers()
    time.sleep(0.6)
    bun = bun_bin()
    env = os.environ.copy()
    env["CLAUDE_PLUGIN_ROOT"] = str(latest)
    env["PATH"] = f"{bun.parent}:{env.get('PATH', '')}"
    env["CLAUDE_MEM_INTERNAL"] = "1"
    log(f"exec {bun} {worker} --daemon ({latest.name})")
    os.execve(str(bun), [str(bun), str(worker), "--daemon"], env)
    return 1


def kick_worker() -> None:
    label = WORKER_LABEL.format(uid=os.getuid())
    subprocess.run(["launchctl", "kickstart", "-k", label], check=False)


def cmd_watch() -> int:
    latest = unify()
    wanted = latest.name
    info = health()
    if info and info.get("status") == "ok" and str(info.get("version")) == wanted:
        reset_hook_failures()
        cull_chroma()
        log(f"ok version={wanted} pid={info.get('pid')}")
        return 0
    # Do not pkill here: launchd KeepAlive owns the worker. A RunAtLoad
    # race would otherwise kill a worker that is still booting.
    got = (info or {}).get("version")
    log(f"unhealthy want={wanted} got={got!r}; waiting")
    time.sleep(8)
    info = health()
    if info and info.get("status") == "ok" and str(info.get("version")) == wanted:
        reset_hook_failures()
        log(f"ok after wait version={wanted} pid={info.get('pid')}")
        return 0
    log("kickstarting worker job")
    reset_hook_failures()
    kick_worker()
    for _ in range(20):
        time.sleep(0.5)
        info = health()
        if info and str(info.get("version")) == wanted:
            log(f"recovered version={wanted} pid={info.get('pid')}")
            return 0
    log("worker did not recover within 10s")
    return 1


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "watch"
    if cmd == "run":
        return cmd_run()
    if cmd == "watch":
        return cmd_watch()
    if cmd == "unify":
        return cmd_unify()
    print("usage: claude_mem_keepalive.py run|watch|unify", file=sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        log(f"error: {exc}")
        raise SystemExit(1)
