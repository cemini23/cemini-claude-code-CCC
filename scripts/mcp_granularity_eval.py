#!/usr/bin/env python3
"""MCP tool interface granularity eval helper — K376 leftover (MCP-GRANITE steal).

Counts tools in a local catalog JSON and labels granularity band for harness eval.
Not a live MCP broker. Pairs scout-tool-search (lazy load) and harness-component-eval.

Usage:
  python3 scripts/mcp_granularity_eval.py checklist
  python3 scripts/mcp_granularity_eval.py json --json catalog.json
  python3 scripts/mcp_granularity_eval.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = REPO_ROOT / "config" / "mcp_granularity_eval.example.json"

# MCP-GRANITE sweep narrative: ~4-tool sweet spot on their benchmark (CCC steal, not a law).
SWEET_MIN = 3
SWEET_MAX = 6
WARN_HIGH = 12


def checklist_text() -> str:
    lines = [
        "K376 MCP tool interface granularity checklist",
        "",
        "Before comparing MCP harness runs, pin:",
        "  [catalog] frozen tool list + schema version for the eval window",
        "  [count] number of tools exposed to the model at selection time",
        "  [lazy] SCOUT-style top-k vs full catalog dump (pairs K311)",
        "  [band] UNDER (<3) | SWEET (3–6) | ELEVATED (7–12) | HIGH (>12)",
        "",
        "Record granularity alongside pass rate — do not swap tool count mid ablation.",
    ]
    return "\n".join(lines)


def band_for_count(n: int) -> str:
    if n < SWEET_MIN:
        return "UNDER"
    if n <= SWEET_MAX:
        return "SWEET"
    if n <= WARN_HIGH:
        return "ELEVATED"
    return "HIGH"


def classify_catalog(data: dict) -> tuple[str, dict]:
    if not isinstance(data, dict):
        return "REJECT", {"error": "input must be a JSON object"}

    tools = data.get("tools")
    if not isinstance(tools, list):
        return "REJECT", {"error": "tools must be a list"}

    names: list[str] = []
    for i, t in enumerate(tools):
        if not isinstance(t, dict):
            return "REJECT", {"error": f"tools[{i}] must be an object"}
        name = str(t.get("name") or "").strip()
        if not name:
            return "REJECT", {"error": f"tools[{i}] missing name"}
        names.append(name)

    n = len(names)
    dupes = len(names) - len(set(names))
    band = band_for_count(n)
    notes: list[str] = []
    if dupes:
        notes.append(f"duplicate tool names: {dupes}")
    if band == "HIGH":
        notes.append("consider lazy catalog / SCOUT top-k before adding tools")
    if band == "UNDER":
        notes.append("single tools may overload semantics — document composite args")

    verdict = "OK" if band in ("SWEET", "ELEVATED") else "REVIEW"
    if band == "HIGH" or dupes:
        verdict = "REVIEW"

    return verdict, {
        "tool_count": n,
        "granularity_band": band,
        "duplicate_names": dupes,
        "notes": notes,
    }


def cmd_json(args: argparse.Namespace) -> int:
    path = Path(args.json)
    if not path.is_file():
        print(f"missing file: {path}", file=sys.stderr)
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    verdict, detail = classify_catalog(data)
    out = {"verdict": verdict, **detail}
    print(json.dumps(out, indent=2))
    return 0 if verdict == "OK" else 2


def selftest() -> int:
    if not EXAMPLE.is_file():
        print(f"selftest FAIL: missing {EXAMPLE}", file=sys.stderr)
        return 1

    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    v1, d1 = classify_catalog(data)
    if v1 != "OK" or d1.get("granularity_band") != "SWEET":
        print(f"selftest FAIL: example catalog {v1} {d1}", file=sys.stderr)
        return 1

    over = {"tools": [{"name": f"t{i}"} for i in range(15)]}
    v2, d2 = classify_catalog(over)
    if d2.get("granularity_band") != "HIGH" or v2 != "REVIEW":
        print(f"selftest FAIL: high count {v2} {d2}", file=sys.stderr)
        return 1

    under = {"tools": [{"name": "only_one"}]}
    v3, d3 = classify_catalog(under)
    if d3.get("granularity_band") != "UNDER":
        print(f"selftest FAIL: under band {d3}", file=sys.stderr)
        return 1

    print("selftest PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="K376 MCP granularity eval helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("checklist")
    p_json = sub.add_parser("json")
    p_json.add_argument("--json", required=True, help="catalog JSON path")
    sub.add_parser("selftest")

    args = parser.parse_args()
    if args.cmd == "checklist":
        print(checklist_text())
        return 0
    if args.cmd == "json":
        return cmd_json(args)
    if args.cmd == "selftest":
        return selftest()
    return 1


if __name__ == "__main__":
    sys.exit(main())
