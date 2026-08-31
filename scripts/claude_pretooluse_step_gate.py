#!/usr/bin/env python3
"""Claude Code PreToolUse hook — step-gate deny-on-HOLD (CCC K312, shipped 2026-08-31).

Reads the Claude Code PreToolUse event JSON from stdin, flattens tool_input to
an args summary, and runs step_gate.classify. Emits a hook-specific output JSON:

  HOLD     -> {"hookSpecificOutput":{"permissionDecision":"deny"},
               "systemMessage":"step-gate HOLD: <why>. Operator OK required."}
  PROCEED  -> {"hookSpecificOutput":{"permissionDecision":"allow"}}
  ESCALATE -> {"hookSpecificOutput":{"permissionDecision":"allow"}}

Deny is ONLY ever produced for step-gate HOLD. PROCEED and ESCALATE always
allow — denying unknown tools would freeze the Claude Code session (pairs
K312 safety-utility). Env STEP_GATE_HOOK=0 disables the gate (always allow).

Exit code is always 0 when the hook ran (a deny is a decision, not a crash).
Timeout-friendly: no network, no imports beyond stdlib + sibling step_gate.py.

Usage:
  python3 scripts/claude_pretooluse_step_gate.py            # read stdin JSON
  python3 scripts/claude_pretooluse_step_gate.py selftest   # synthetic payloads
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Sibling module in scripts/ (repo root may not be on sys.path when Claude Code
# invokes this hook directly).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step_gate import classify  # noqa: E402


def flatten_tool_input(tool_input) -> str:
    """Flatten a PreToolUse tool_input object into an args summary string."""
    if tool_input is None:
        return ""
    if isinstance(tool_input, str):
        return tool_input
    if isinstance(tool_input, (int, float, bool)):
        return str(tool_input)
    if isinstance(tool_input, dict):
        parts = []
        for k, v in tool_input.items():
            if isinstance(v, (dict, list, tuple)):
                parts.append(flatten_tool_input(v))
            elif v is not None:
                parts.append(str(v))
        return " ".join(p for p in parts if p)
    if isinstance(tool_input, (list, tuple)):
        return " ".join(flatten_tool_input(v) for v in tool_input if v is not None)
    return str(tool_input)


def decide(tool_name: str, tool_input) -> tuple[str, str]:
    """Return (permission_decision, system_message). Never returns None."""
    if os.environ.get("STEP_GATE_HOOK", "1") == "0":
        return "allow", ""
    args_summary = flatten_tool_input(tool_input)
    verdict, why = classify(tool_name, args_summary)
    if verdict == "hold":
        return "deny", f"step-gate HOLD: {why}. Operator OK required."
    return "allow", ""


def run_from_stdin() -> str:
    """Read PreToolUse JSON from stdin and return the hook output JSON."""
    raw = sys.stdin.read()
    try:
        event = json.loads(raw)
    except json.JSONDecodeError:
        # Malformed payload — never deny on a parse failure (would freeze the
        # session). Allow and note it.
        return json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}})
    if not isinstance(event, dict):
        # Array / scalar JSON is valid JSON but not a PreToolUse event.
        return json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}})
    tool_name = event.get("tool_name") or event.get("toolName") or ""
    tool_input = event.get("tool_input") or event.get("toolInput") or {}
    decision, message = decide(tool_name, tool_input)
    out: dict = {"hookSpecificOutput": {"permissionDecision": decision}}
    if message:
        out["systemMessage"] = message
    return json.dumps(out)


def selftest() -> int:
    cases = [
        # (tool_name, tool_input, want_decision, why)
        (
            "Bash",
            {"command": "git push --force origin main", "description": "force push"},
            "deny",
            "force-push HOLD must deny",
        ),
        (
            "Bash",
            {"command": "python3 scripts/wiki_lint.py", "description": "lint"},
            "allow",
            "wiki_lint PROCEED must allow",
        ),
        (
            "Edit",
            {"file_path": ".env", "content": "SECRET=..."},
            "deny",
            ".env write HOLD must deny",
        ),
        (
            "Write",
            {"file_path": "wiki/concepts/context-engineering.md", "content": "x"},
            "allow",
            "unknown high-blast ESCALATE must allow",
        ),
        (
            "Bash",
            {"command": "git status"},
            "allow",
            "git status PROCEED must allow",
        ),
        (
            "Write",
            {"file_path": "watches.json", "content": "{}"},
            "deny",
            "watches.json write HOLD must deny",
        ),
        (
            "Bash",
            {"command": "grep -r token wiki/"},
            "allow",
            "read-only token mention must not HOLD",
        ),
    ]
    for tool, tool_input, want, why in cases:
        got, _msg = decide(tool, tool_input)
        if got != want:
            raise SystemExit(
                f"selftest FAIL: ({tool!r}, {tool_input!r}) -> {got}, expected {want} ({why})"
            )
    # STEP_GATE_HOOK=0 kill switch: even a HOLD must allow.
    os.environ["STEP_GATE_HOOK"] = "0"
    try:
        got, _msg = decide("Bash", {"command": "git push --force origin main"})
        if got != "allow":
            raise SystemExit(f"selftest FAIL: STEP_GATE_HOOK=0 did not force allow (got {got})")
    finally:
        os.environ.pop("STEP_GATE_HOOK", None)
    import io

    old_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("[]")
        out = json.loads(run_from_stdin())
        if out.get("hookSpecificOutput", {}).get("permissionDecision") != "allow":
            raise SystemExit("selftest FAIL: [] payload must allow")
        sys.stdin = io.StringIO("not-json")
        out = json.loads(run_from_stdin())
        if out.get("hookSpecificOutput", {}).get("permissionDecision") != "allow":
            raise SystemExit("selftest FAIL: malformed JSON must allow")
    finally:
        sys.stdin = old_stdin
    print(
        f"selftest PASS: {len(cases)} payloads + kill switch + malformed stdin classified correctly"
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "mode",
        nargs="?",
        default="run",
        choices=["run", "selftest"],
        help="'run' reads stdin (default); 'selftest' runs synthetic payloads",
    )
    args = ap.parse_args()
    if args.mode == "selftest":
        return selftest()
    try:
        print(run_from_stdin())
    except Exception:
        # Fail open on stdout so Claude Code sees a decision (stderr is ignored).
        print(json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}}))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
