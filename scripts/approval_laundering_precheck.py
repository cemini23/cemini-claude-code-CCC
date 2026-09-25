#!/usr/bin/env python3
"""Approval laundering precheck — K395 leftover (pairs K310/K302/K333).

Checklist + JSON gate: entry approval documented vs transitive effect review.
Policy helper only — not a runtime broker.

Usage:
  python3 scripts/approval_laundering_precheck.py checklist
  python3 scripts/approval_laundering_precheck.py json --json review.json
  python3 scripts/approval_laundering_precheck.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = REPO_ROOT / "config" / "approval_laundering_precheck.example.json"


def checklist_text() -> str:
    return "\n".join(
        [
            "K395 approval laundering precheck (pairs K310 / K302 / K333)",
            "",
            "Before treating an action as fully authorized:",
            "  [entry] approved_tool / approved_command recorded",
            "  [transitive] list follow-on effects (hooks, network, sub-agents, writes)",
            "  [closure] human or broker confirmed effect envelope — not prompt-only",
            "  [audit] log covers transitive effects or documents known gaps",
            "",
            "Verdict: PASS | REVIEW | REJECT",
        ]
    )


def classify(data: dict) -> tuple[str, list[str]]:
    if not isinstance(data, dict):
        return "REJECT", ["input must be a JSON object"]

    entry = str(data.get("approved_entry") or "").strip()
    if not entry:
        return "REJECT", ["approved_entry required"]

    transitive = data.get("transitive_effects")
    if not isinstance(transitive, list):
        return "REJECT", ["transitive_effects must be a list"]

    reviewed = bool(data.get("effect_closure_reviewed"))
    audit_ok = bool(data.get("audit_covers_transitive"))

    reasons: list[str] = []
    if not transitive:
        reasons.append("empty transitive_effects — enumerate hooks/network/delegation")
    if not reviewed:
        reasons.append("effect_closure_reviewed is false")
    if not audit_ok:
        reasons.append("audit_covers_transitive is false")

    if reasons:
        return "REVIEW", reasons
    return "PASS", []


def cmd_json(args: argparse.Namespace) -> int:
    path = Path(args.json)
    data = json.loads(path.read_text(encoding="utf-8"))
    verdict, reasons = classify(data)
    print(json.dumps({"verdict": verdict, "reasons": reasons}, indent=2))
    if verdict == "REJECT":
        return 1
    if verdict == "REVIEW":
        return 2
    return 0


def selftest() -> int:
    if not EXAMPLE.is_file():
        print(f"missing {EXAMPLE}", file=sys.stderr)
        return 1
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    if classify(data)[0] != "PASS":
        print("example should PASS", file=sys.stderr)
        return 1
    bad = {"approved_entry": "npm install", "transitive_effects": [], "effect_closure_reviewed": False}
    if classify(bad)[0] != "REVIEW":
        print("bad case should REVIEW", file=sys.stderr)
        return 1
    print("selftest PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("checklist")
    p = sub.add_parser("json")
    p.add_argument("--json", required=True)
    sub.add_parser("selftest")
    args = parser.parse_args()
    if args.cmd == "checklist":
        print(checklist_text())
        return 0
    if args.cmd == "json":
        return cmd_json(args)
    return selftest()


if __name__ == "__main__":
    sys.exit(main())
