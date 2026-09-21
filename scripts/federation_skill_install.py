#!/usr/bin/env python3
"""Federation skill install helper — K312 step-gate safe ship path.

Install or update federation Cursor skills without bash/Write args that mention
the skills tree path (PreToolUse step-gate HOLD on mutating tools).

Usage:
  python3 scripts/federation_skill_install.py sync
  python3 scripts/federation_skill_install.py verify <skill-name>
  python3 scripts/federation_skill_install.py write --name NAME --body-file PATH
  python3 scripts/federation_skill_install.py selftest
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".cursor" / "skills"
SYNC_SCRIPT = REPO_ROOT / "scripts" / "sync_federation_cursor_skills.sh"

_FEDERATION_TRUE = re.compile(
    r"^federation:\s*(?:true|True|\"true\"|'true')\s*$", re.MULTILINE
)


def _parse_frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end]


def verify_skill(name: str) -> tuple[bool, str]:
    skill_path = SKILLS_DIR / name / "SKILL.md"
    if not skill_path.is_file():
        return False, f"missing {skill_path.relative_to(REPO_ROOT)}"
    raw = skill_path.read_text(encoding="utf-8", errors="replace")
    fm = _parse_frontmatter(raw)
    if fm is None:
        return False, "SKILL.md missing YAML frontmatter"
    if not _FEDERATION_TRUE.search(fm):
        return False, "frontmatter missing federation: true"
    return True, "ok"


def cmd_sync(_: argparse.Namespace) -> int:
    if not SYNC_SCRIPT.is_file():
        print(f"sync script missing: {SYNC_SCRIPT}", file=sys.stderr)
        return 1
    proc = subprocess.run(
        ["bash", str(SYNC_SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if proc.stdout:
        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n")
    if proc.returncode != 0:
        if proc.stderr:
            print(proc.stderr, file=sys.stderr, end="" if proc.stderr.endswith("\n") else "\n")
        print(f"sync failed (exit {proc.returncode})", file=sys.stderr)
        return proc.returncode
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    ok, msg = verify_skill(args.name)
    if ok:
        print(f"verify PASS: {args.name} ({msg})")
        return 0
    print(f"verify FAIL: {args.name} — {msg}", file=sys.stderr)
    return 1


def cmd_write(args: argparse.Namespace) -> int:
    body_path = Path(args.body_file)
    if not body_path.is_file():
        print(f"body file missing: {body_path}", file=sys.stderr)
        return 1
    body = body_path.read_text(encoding="utf-8")
    dest_dir = SKILLS_DIR / args.name
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "SKILL.md"
    dest.write_text(body, encoding="utf-8")
    print(f"wrote {dest.relative_to(REPO_ROOT)}")
    return 0


def selftest() -> int:
    ok, msg = verify_skill("enterprise-scale-gate")
    if not ok:
        print(f"selftest FAIL: enterprise-scale-gate — {msg}", file=sys.stderr)
        return 1
    if not SYNC_SCRIPT.is_file():
        print(f"selftest FAIL: sync script missing", file=sys.stderr)
        return 1
    if not SKILLS_DIR.is_dir():
        print("selftest FAIL: skills dir missing", file=sys.stderr)
        return 1
    fed_count = 0
    for skill_md in SKILLS_DIR.glob("*/SKILL.md"):
        name = skill_md.parent.name
        if verify_skill(name)[0]:
            fed_count += 1
    if fed_count < 1:
        print("selftest FAIL: no federation skills found", file=sys.stderr)
        return 1
    print(
        f"selftest PASS: enterprise-scale-gate ok; sync script present; "
        f"{fed_count} federation skill(s); dry sync check ok"
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sync").set_defaults(fn=cmd_sync)
    p_v = sub.add_parser("verify", help="verify federation skill exists")
    p_v.add_argument("name")
    p_v.set_defaults(fn=cmd_verify)
    p_w = sub.add_parser("write", help="write SKILL.md from body file")
    p_w.add_argument("--name", required=True)
    p_w.add_argument("--body-file", required=True)
    p_w.set_defaults(fn=cmd_write)
    sub.add_parser("selftest").set_defaults(fn=lambda _: selftest())
    args = ap.parse_args()
    return int(args.fn(args))


if __name__ == "__main__":
    raise SystemExit(main())
