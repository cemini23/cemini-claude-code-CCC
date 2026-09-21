#!/usr/bin/env python3
"""Enterprise use-case scale gate — K373 leftover (EnterpriseVal steal).

Check frozen socio-technical config + metric thresholds before SCALE.
Outputs REJECT | CONDITIONAL | SCALE. Never promotes CONDITIONAL to SCALE
without human_review_confirmed on medium/high consequence tiers.

Usage:
  python3 scripts/enterprise_scale_gate.py checklist
  python3 scripts/enterprise_scale_gate.py json --json eval.json
  python3 scripts/enterprise_scale_gate.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = REPO_ROOT / "config" / "enterprise_scale_gate.example.json"

FROZEN_KEYS = ("model", "prompts", "retrieval", "tools", "guardrails", "oversight")
TIERS = {"low", "medium", "high"}


def checklist_text() -> str:
    lines = [
        "K373 enterprise scale gate checklist",
        "",
        "Before SCALE, confirm:",
        "  [frozen_config] model, prompts, retrieval, tools, guardrails, oversight pinned",
        "  [metrics] each metric has value + threshold_min and/or threshold_max",
        "  [bounds] optional confidence_lower / confidence_upper on metrics",
        "  [consequence_tier] low | medium | high sets review intensity",
        "  [human_review_confirmed] required true to SCALE when tier is medium/high",
        "",
        "Verdicts: REJECT (fail thresholds / incomplete config) |",
        "          CONDITIONAL (pass metrics but needs human review) |",
        "          SCALE (cleared to expand)",
    ]
    return "\n".join(lines)


def _nonempty(v: object) -> bool:
    return bool(str(v or "").strip())


def _metric_fails(m: dict) -> list[str]:
    reasons: list[str] = []
    name = str(m.get("name") or "unnamed")
    if "value" not in m:
        return [f"{name}: missing value"]
    try:
        value = float(m["value"])
    except (TypeError, ValueError):
        return [f"{name}: value must be numeric"]

    tmin = m.get("threshold_min")
    tmax = m.get("threshold_max")
    if tmin is None and tmax is None:
        return [f"{name}: need threshold_min and/or threshold_max"]

    if tmin is not None and value < float(tmin):
        reasons.append(f"{name}: value {value} below threshold_min {tmin}")
    if tmax is not None and value > float(tmax):
        reasons.append(f"{name}: value {value} above threshold_max {tmax}")

    lower = m.get("confidence_lower")
    upper = m.get("confidence_upper")
    if lower is not None and value < float(lower):
        reasons.append(f"{name}: value below confidence_lower {lower}")
    if upper is not None and value > float(upper):
        reasons.append(f"{name}: value above confidence_upper {upper}")

    return reasons


def classify(data: dict) -> tuple[str, list[str]]:
    if not isinstance(data, dict):
        return "REJECT", ["input must be a JSON object"]

    frozen = data.get("frozen_config")
    if not isinstance(frozen, dict):
        return "REJECT", ["frozen_config must be an object"]

    missing = [k for k in FROZEN_KEYS if not _nonempty(frozen.get(k))]
    if missing:
        return "REJECT", [f"frozen_config missing or empty: {k}" for k in missing]

    tier = str(data.get("consequence_tier") or "medium").strip().lower()
    if tier not in TIERS:
        return "REJECT", [f"invalid consequence_tier: {tier!r}"]

    metrics = data.get("metrics")
    if not isinstance(metrics, list) or not metrics:
        return "REJECT", ["metrics must be a non-empty list"]

    fails: list[str] = []
    for m in metrics:
        if not isinstance(m, dict):
            fails.append("metric entry must be an object")
            continue
        fails.extend(_metric_fails(m))

    if fails:
        return "REJECT", fails

    human_ok = bool(data.get("human_review_confirmed"))
    if tier in {"medium", "high"} and not human_ok:
        return "CONDITIONAL", [
            f"metrics pass but human_review_confirmed required for {tier} consequence tier"
        ]

    return "SCALE", ["frozen config + metrics pass; cleared to scale"]


def selftest() -> int:
    good = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    got, _ = classify(good)
    if got != "SCALE":
        print(f"FAIL example expected SCALE, got {got}", file=sys.stderr)
        return 1

    bad_frozen = dict(good)
    bad_frozen["frozen_config"] = {"model": "x"}
    if classify(bad_frozen)[0] != "REJECT":
        print("FAIL incomplete frozen_config", file=sys.stderr)
        return 1

    bad_metric = json.loads(json.dumps(good))
    bad_metric["metrics"] = [
        {
            "name": "citation_precision",
            "value": 0.50,
            "threshold_min": 0.70,
        }
    ]
    if classify(bad_metric)[0] != "REJECT":
        print("FAIL sub-threshold metric", file=sys.stderr)
        return 1

    conditional = json.loads(json.dumps(good))
    conditional["human_review_confirmed"] = False
    conditional["consequence_tier"] = "high"
    if classify(conditional)[0] != "CONDITIONAL":
        print("FAIL expected CONDITIONAL without human review", file=sys.stderr)
        return 1

    low_auto = json.loads(json.dumps(good))
    low_auto["consequence_tier"] = "low"
    low_auto["human_review_confirmed"] = False
    if classify(low_auto)[0] != "SCALE":
        print("FAIL low tier should SCALE without human review", file=sys.stderr)
        return 1

    print("enterprise_scale_gate selftest: 5 pass, 0 fail")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("checklist")
    p_json = sub.add_parser("json")
    p_json.add_argument("--json", required=True)
    sub.add_parser("selftest")
    args = ap.parse_args()

    if args.cmd == "checklist":
        print(checklist_text())
        return 0

    if args.cmd == "selftest":
        return selftest()

    data = json.loads(Path(args.json).read_text(encoding="utf-8"))
    verdict, reasons = classify(data)
    print(json.dumps({"verdict": verdict, "reasons": reasons}, indent=2))
    return 0 if verdict == "SCALE" else 1 if verdict == "CONDITIONAL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
