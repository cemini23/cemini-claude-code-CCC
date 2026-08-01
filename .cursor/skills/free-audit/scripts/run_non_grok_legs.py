#!/usr/bin/env python3
"""Run claude-ds (DeepSeek V4 Flash) + free OpenRouter auditor legs.

HTTP legs have NO tools. Pack artifacts are inlined into the prompt so models
cannot stall on Read/tool-call stubs (DeepSeek DSML / Nemotron tool JSON).

Usage:
  python3 run_non_grok_legs.py --pack reports/audit/pack-free-foo --out reports/audit/free-foo
  python3 run_non_grok_legs.py --pack … --out … --models-json free_models.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _env import env, load_routing_env  # noqa: E402
from select_free_or_models import fetch_models, pick_diverse, rank_candidates  # noqa: E402

SYSTEM = """You are a readonly auditor in a multi-model free audit.

HARD RULES:
- You have NO tools, NO function calling, NO file Read, NO shell.
- Do NOT emit tool calls, XML tool markup, DSML, or JSON like {"tool":...}.
- All evidence is already pasted in the user message under ## Inlined pack artifacts.
- Reply with the required markdown audit format ONLY (Verdict / Findings / …).
- Do not invent secrets. Do not edit files.
"""

RETRY_SYSTEM = (
    SYSTEM
    + "\nYour previous reply was INVALID because it tried to call tools. "
    "Answer now using only the inlined pack artifacts. Start with '### Verdict'."
)

TOOL_STUB_RE = re.compile(
    r"(?is)"
    r"(tool_calls|DSML|</?\|?DSML|"
    r"<\|?tool|"
    r"\"tool\"\s*:\s*\"read\""
    r"|\"name\"\s*:\s*\"Read\""
    r"|invoke\s+name=\"Read\""
    r"|functions?\.[A-Za-z_]+\()"
)

VERDICT_RE = re.compile(r"(?im)^###\s*Verdict\b")

SKIP_PACK_NAMES = {
    "audit_prompt.md",
    "meta.json",
    "PACK_INDEX.md",
}


def _chat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    system: str,
    title: str,
    max_tokens: int = 8_000,
) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
        # Disable tools when the provider honors OpenAI-compatible tool_choice.
        "tool_choice": "none",
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = env("OPENROUTER_HTTP_REFERER", "https://github.com/cemini23")
        headers["X-Title"] = env("OPENROUTER_APP_TITLE", title)
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Some providers reject tool_choice when no tools are declared — retry bare.
        err_body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        if e.code in (400, 422) and "tool" in err_body.lower():
            body.pop("tool_choice", None)
            data = json.dumps(body).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=600) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        else:
            raise
    msg = payload["choices"][0]["message"]
    content = (msg.get("content") or "").strip()
    # Some models put stubs in reasoning / tool_calls fields with empty content.
    if not content:
        tool_calls = msg.get("tool_calls") or msg.get("function_call")
        if tool_calls:
            return json.dumps(tool_calls)[:2000]
    return content


def _safe_label(model_id: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", model_id).strip("-")
    return f"auditor-or-{slug}"[:120]


def _looks_degraded(text: str) -> bool:
    if not text or len(text.strip()) < 40:
        return True
    if TOOL_STUB_RE.search(text):
        return True
    if not VERDICT_RE.search(text) and "### Verdict" not in text:
        # Allow "Verdict" without hashes as weak pass only if substantial prose
        if not re.search(r"(?im)^Verdict\b", text):
            return True
    return False


def _inline_pack_bundle(pack: Path, *, max_total: int = 100_000) -> str:
    """Concatenate pack artifacts (already truncated by build_audit_pack)."""
    parts: list[str] = []
    used = 0
    # Prefer PACK_INDEX read order when present
    order: list[str] = []
    index = pack / "PACK_INDEX.md"
    if index.is_file():
        for line in index.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line.startswith("- `") and line.endswith("`"):
                path_s = line[3:-1]
                name = Path(path_s).name
                if name and name not in order:
                    order.append(name)
    # Fallback: all files in pack
    names = order or sorted(p.name for p in pack.iterdir() if p.is_file())
    for name in names:
        if name in SKIP_PACK_NAMES:
            continue
        path = pack / name
        if not path.is_file():
            continue
        body = path.read_text(encoding="utf-8", errors="replace")
        chunk = f"\n### FILE: {name}\n```\n{body}\n```\n"
        if used + len(chunk) > max_total:
            remain = max_total - used
            if remain < 500:
                parts.append(f"\n… omitted remaining pack files (budget {max_total} chars) …\n")
                break
            chunk = chunk[:remain] + "\n… truncated …\n"
            parts.append(chunk)
            break
        parts.append(chunk)
        used += len(chunk)
    return "".join(parts) if parts else "(no pack artifacts found)"


def _api_user_prompt(base: str, slot: str, model: str, mode: str, bundle: str) -> str:
    text = base
    text = text.replace("{{MODEL_SLOT}}", f"{slot} ({model})")
    text = text.replace("{{MODE}}", mode or "code-debug")
    # Rewrite path-read language that triggers agentic tool calls.
    text = text.replace(
        "## Data pack files (READ these paths)",
        "## Data pack file index (contents inlined below — do NOT call tools)",
    )
    text = text.replace(
        "READ these paths",
        "listed below; full contents are inlined — do NOT call tools",
    )
    text += (
        "\n\n---\n\n## Inlined pack artifacts\n\n"
        "The following files are already loaded. Cite them by filename. "
        "Do not emit Read/tool calls.\n"
        f"{bundle}\n"
        "\n---\n\n"
        "Remember: respond with ### Verdict and the Findings table only. No tools.\n"
    )
    return text


def _write_report(dest: Path, *, model: str, channel: str, ts: str, content: str, note: str = "") -> None:
    header = f"<!-- model={model} channel={channel} ts={ts} -->\n"
    if note:
        header += f"<!-- {note} -->\n"
    dest.write_text(header + "\n" + content.rstrip() + "\n", encoding="utf-8")


def _call_with_retry(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    title: str,
) -> tuple[str, bool, str]:
    """Return (content, ok, note)."""
    content = _chat(
        base_url=base_url,
        api_key=api_key,
        model=model,
        prompt=prompt,
        system=SYSTEM,
        title=title,
    )
    if not _looks_degraded(content):
        return content, True, ""
    # Retry once with stricter system + nudge
    retry_prompt = (
        prompt
        + "\n\nIMPORTANT: Your first attempt must have been a tool call. "
        "Do not call tools. Start your reply with exactly: ### Verdict\n"
    )
    content2 = _chat(
        base_url=base_url,
        api_key=api_key,
        model=model,
        prompt=retry_prompt,
        system=RETRY_SYSTEM,
        title=title,
    )
    if not _looks_degraded(content2):
        return content2, True, "retry-after-tool-stub"
    return content2 or content, False, "degraded-tool-stub"


def _alternate_free_models(primary: list[str], pool: list[dict], *, need: int = 2) -> list[str]:
    """Extra free models from ranked pool not already in primary."""
    used = set(primary)
    alts: list[str] = []
    for c in pool:
        mid = c["id"]
        if mid in used or mid == "openrouter/free":
            continue
        alts.append(mid)
        if len(alts) >= need:
            break
    return alts


def main() -> int:
    ap = argparse.ArgumentParser(description="Run free-audit non-Grok legs")
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--models-json", type=Path, default=None)
    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--mode", default="code-debug")
    ap.add_argument("--skip-deepseek", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-bundle-chars", type=int, default=100_000)
    args = ap.parse_args()

    load_routing_env()
    pack = args.pack.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    prompt_path = pack / "audit_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path}", file=sys.stderr)
        return 1
    base_prompt = prompt_path.read_text(encoding="utf-8")
    bundle = _inline_pack_bundle(pack, max_total=args.max_bundle_chars)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    or_key = env("OPENROUTER_API_KEY")
    or_base = env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    ranked_pool: list[dict] = []

    if args.models_json and args.models_json.is_file():
        models_data = json.loads(args.models_json.read_text(encoding="utf-8"))
        free_models = [
            m["id"] if isinstance(m, dict) else str(m) for m in models_data.get("models", [])
        ]
    else:
        if not or_key:
            print("OPENROUTER_API_KEY required for free OR legs", file=sys.stderr)
            return 1
        try:
            ranked_pool = rank_candidates(fetch_models(or_base, or_key))
            picked = pick_diverse(ranked_pool, max(2, args.count))
        except Exception as e:
            print(f"Free model select failed: {e}", file=sys.stderr)
            return 1
        free_models = [p["id"] for p in picked]
        (out / "free_models.json").write_text(
            json.dumps({"models": picked, "count": len(picked)}, indent=2) + "\n",
            encoding="utf-8",
        )

    if len(free_models) < 2:
        print("Need ≥2 free OpenRouter models", file=sys.stderr)
        return 1

    if or_key and not ranked_pool:
        try:
            ranked_pool = rank_candidates(fetch_models(or_base, or_key))
        except Exception:
            ranked_pool = []

    plan = {
        "deepseek": None if args.skip_deepseek else env("DEEPSEEK_MODEL", "deepseek-v4-flash"),
        "free_or": free_models,
        "bundle_chars": len(bundle),
    }
    print(json.dumps({"plan": plan}, indent=2))
    if args.dry_run:
        return 0

    written: list[str] = []
    errors: list[str] = []
    degraded: list[str] = []

    # Slot 2 — DeepSeek / claude-ds
    if not args.skip_deepseek:
        ds_key = env("DEEPSEEK_API_KEY")
        ds_base = env("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        ds_model = env("DEEPSEEK_MODEL", "deepseek-v4-flash")
        label = "auditor-claude-ds"
        dest = out / f"{label}.md"
        if not ds_key:
            msg = "DEEPSEEK_API_KEY missing — skipped claude-ds slot"
            errors.append(msg)
            dest.write_text(f"### Verdict\nFAIL — {msg}\n", encoding="utf-8")
            print(f"  SKIP {msg}", file=sys.stderr)
        else:
            try:
                prompt = _api_user_prompt(base_prompt, "claude-ds", ds_model, args.mode, bundle)
                content, ok, note = _call_with_retry(
                    base_url=ds_base,
                    api_key=ds_key,
                    model=ds_model,
                    prompt=prompt,
                    title="free-audit-claude-ds",
                )
                _write_report(dest, model=ds_model, channel="deepseek-api", ts=ts, content=content, note=note)
                written.append(str(dest))
                if ok:
                    print(f"  OK {label} → {dest}" + (f" ({note})" if note else ""))
                else:
                    degraded.append(label)
                    errors.append(f"{label}: degraded tool-stub response")
                    print(f"  DEGRADED {label} → {dest}", file=sys.stderr)
            except (urllib.error.URLError, urllib.error.HTTPError, KeyError, TimeoutError, json.JSONDecodeError) as e:
                err = f"{label}: {e}"
                errors.append(err)
                dest.write_text(f"### Verdict\nFAIL — API error: {e}\n", encoding="utf-8")
                print(f"  ERR {err}", file=sys.stderr)

    # Slots 3+ — free OpenRouter (with alternate fallback on degraded)
    if not or_key:
        print("OPENROUTER_API_KEY missing", file=sys.stderr)
        return 1

    alts = _alternate_free_models(free_models, ranked_pool, need=4)
    alt_i = 0
    ok_or = 0
    for mid in free_models:
        label = _safe_label(mid)
        dest = out / f"{label}.md"
        try_models = [mid]
        # One alternate if primary degrades
        if alt_i < len(alts):
            try_models.append(alts[alt_i])
        success = False
        last_content = ""
        used_model = mid
        note = ""
        for attempt_i, attempt_model in enumerate(try_models):
            try:
                prompt = _api_user_prompt(
                    base_prompt, "openrouter-free", attempt_model, args.mode, bundle
                )
                content, ok, note = _call_with_retry(
                    base_url=or_base,
                    api_key=or_key,
                    model=attempt_model,
                    prompt=prompt,
                    title="free-audit",
                )
                last_content = content
                used_model = attempt_model
                if ok:
                    success = True
                    if attempt_i > 0:
                        note = (note + "+" if note else "") + f"fallback-from-{mid}"
                        alt_i += 1
                    break
                print(
                    f"  DEGRADED {attempt_model} — trying fallback…"
                    if attempt_i + 1 < len(try_models)
                    else f"  DEGRADED {attempt_model}",
                    file=sys.stderr,
                )
                if attempt_i > 0:
                    alt_i += 1
            except (urllib.error.URLError, urllib.error.HTTPError, KeyError, TimeoutError, json.JSONDecodeError) as e:
                err = f"{label}/{attempt_model}: {e}"
                errors.append(err)
                print(f"  ERR {err}", file=sys.stderr)
                if attempt_i > 0:
                    alt_i += 1

        if last_content:
            # If fallback succeeded under a different model, keep primary filename
            # but record actual model in header.
            _write_report(
                dest,
                model=used_model,
                channel="openrouter-free",
                ts=ts,
                content=last_content,
                note=note or ("degraded-tool-stub" if not success else ""),
            )
            written.append(str(dest))
            if success:
                ok_or += 1
                print(f"  OK {label} model={used_model} → {dest}" + (f" ({note})" if note else ""))
            else:
                degraded.append(label)
                errors.append(f"{label}: degraded tool-stub response")
        elif not last_content:
            dest.write_text("### Verdict\nFAIL — empty response\n", encoding="utf-8")

    # If we still have <2 good OR reports, try more alts into extra files
    while ok_or < 2 and alt_i < len(alts):
        mid = alts[alt_i]
        alt_i += 1
        label = _safe_label(mid)
        dest = out / f"{label}.md"
        try:
            prompt = _api_user_prompt(base_prompt, "openrouter-free", mid, args.mode, bundle)
            content, ok, note = _call_with_retry(
                base_url=or_base,
                api_key=or_key,
                model=mid,
                prompt=prompt,
                title="free-audit",
            )
            _write_report(dest, model=mid, channel="openrouter-free", ts=ts, content=content, note=note or "")
            written.append(str(dest))
            if ok:
                ok_or += 1
                print(f"  OK extra {label} → {dest}")
            else:
                degraded.append(label)
                print(f"  DEGRADED extra {label}", file=sys.stderr)
        except Exception as e:
            print(f"  ERR extra {mid}: {e}", file=sys.stderr)

    meta = {
        "ts": ts,
        "written": written,
        "errors": errors,
        "degraded": degraded,
        "free_models": free_models,
        "bundle_chars": len(bundle),
        "ok_or_count": ok_or,
    }
    (out / f"non_grok_legs_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    # Success if DeepSeek ok (or skipped) and ≥1 OR ok — prefer ≥2 OR
    return 0 if written and ok_or >= 1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
