#!/usr/bin/env python3
"""Cross-vendor behavior assay gate — K392 leftover.

Check frozen vendor/release/harness pins and cheap assay results before comparing models.
Usage:
  python3 scripts/cross_vendor_behavior_assay.py checklist
  python3 scripts/cross_vendor_behavior_assay.py json --json run.json
  python3 scripts/cross_vendor_behavior_assay.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = REPO_ROOT / "config" / "cross_vendor_behavior_assay.example.json"

PIN_KEYS = ("vendor", "model_id", "release", "harness_version")


def checklist_text() -> str:
    return "\n".join(
        [
            "K392 cross-vendor behavior assay checklist",
            "",
            "Before comparing vendors or releases:",
            "  [pins] vendor, model_id, release, harness_version frozen",
            "  [assays] non-empty list of cheap probes with pass/fail",
            "  [threshold] min_pass_ratio default 0.8 on assays",
            "",
            "Verdict: PASS | CONDITIONAL | REJECT",
        ]
    )


def classify(data: dict) -> tuple[str, list[str], float]:
    if not isinstance(data, dict):
        return "REJECT", ["input must be a JSON object"], 0.0

    pins = data.get("pins")
    if not isinstance(pins, dict):
        return "REJECT", ["pins must be an object"], 0.0
    missing = [k for k in PIN_KEYS if not str(pins.get(k) or "").strip()]
    if missing:
        return "REJECT", [f"pins missing: {', '.join(missing)}"], 0.0

    assays = data.get("assays")
    if not isinstance(assays, list) or not assays:
        return "REJECT", ["assays must be a non-empty list"], 0.0

    passed = 0
    for i, a in enumerate(assays):
        if not isinstance(a, dict):
            return "REJECT", [f"assays[{i}] must be an object"], 0.0
        if "pass" not in a:
            return "REJECT", [f"assays[{i}] missing pass boolean"], 0.0
        if bool(a["pass"]):
            passed += 1

    ratio = passed / len(assays)
    threshold = float(data.get("min_pass_ratio") or 0.8)
    if ratio < threshold:
        return "CONDITIONAL", [f"pass ratio {ratio:.2f} below min_pass_ratio {threshold}"], ratio
    return "PASS", [], ratio


def cmd_json(args: argparse.Namespace) -> int:
    path = Path(args.json)
    data = json.loads(path.read_text(encoding="utf-8"))
    verdict, reasons, ratio = classify(data)
    print(json.dumps({"verdict": verdict, "pass_ratio": ratio, "reasons": reasons}, indent=2))
    if verdict == "REJECT":
        return 1
    if verdict == "CONDITIONAL":
        return 2
    return 0


def selftest() -> int:
    if not EXAMPLE.is_file():
        print(f"missing {EXAMPLE}", file=sys.stderr)
        return 1
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    v, _, _ = classify(data)
    if v != "PASS":
        print(f"example failed: {v}", file=sys.stderr)
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
