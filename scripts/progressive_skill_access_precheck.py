#!/usr/bin/env python3
"""Progressive skill access precheck — K390 leftover.

Validate a staged skill/tool disclosure plan (no flat catalog dump at turn 0).
Usage:
  python3 scripts/progressive_skill_access_precheck.py checklist
  python3 scripts/progressive_skill_access_precheck.py json --json plan.json
  python3 scripts/progressive_skill_access_precheck.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = REPO_ROOT / "config" / "progressive_skill_access.example.json"


def checklist_text() -> str:
    return "\n".join(
        [
            "K390 progressive skill access precheck",
            "",
            "Before exposing skills/tools to the model:",
            "  [stages] ordered disclosure stages (not full catalog at turn 0)",
            "  [max_tools_per_stage] cap tools visible per stage",
            "  [flat_dump] must be false — no dump_all_tools_at_start",
            "  [unlock] each stage lists explicit unlock criteria",
            "",
            "Verdict: PASS | REVIEW | REJECT",
        ]
    )


def classify(data: dict) -> tuple[str, list[str]]:
    if not isinstance(data, dict):
        return "REJECT", ["input must be a JSON object"]

    reasons: list[str] = []
    if data.get("flat_dump") or data.get("dump_all_tools_at_start"):
        reasons.append("flat catalog dump forbidden at start")

    stages = data.get("stages")
    if not isinstance(stages, list) or len(stages) < 1:
        return "REJECT", ["stages must be a non-empty list"]

    max_default = int(data.get("max_tools_per_stage") or 8)
    for i, st in enumerate(stages):
        if not isinstance(st, dict):
            return "REJECT", [f"stages[{i}] must be an object"]
        tools = st.get("tools")
        if not isinstance(tools, list):
            return "REJECT", [f"stages[{i}].tools must be a list"]
        cap = int(st.get("max_tools") or max_default)
        if len(tools) > cap:
            reasons.append(f"stage {i} exposes {len(tools)} tools > cap {cap}")
        if not str(st.get("unlock_criteria") or "").strip():
            reasons.append(f"stage {i} missing unlock_criteria")

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
    v, _ = classify(data)
    if v != "PASS":
        print(f"example failed: {v}", file=sys.stderr)
        return 1
    bad = {"flat_dump": True, "stages": [{"tools": ["a"], "unlock_criteria": "x"}]}
    v2, _ = classify(bad)
    if v2 not in ("REVIEW", "REJECT"):
        print(f"flat_dump check failed: {v2}", file=sys.stderr)
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
