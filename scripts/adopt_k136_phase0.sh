#!/usr/bin/env bash
# K136 Phase-0 — Agentic orchestration options ABPM (2606.31518).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K136 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"
  shift
  if "$@"; then
    echo "  PASS  ${label}"
    pass=$((pass + 1))
  else
    echo "  FAIL  ${label}"
    fail=$((fail + 1))
  fi
}

warn_note() {
  echo "  WARN  $1"
  warn=$((warn + 1))
}

if command -v gh >/dev/null 2>&1; then
  license="$(gh api repos/JohannesLbck/SimpleAgenticScenario --jq '.license.spdx_id // empty' 2>/dev/null || true)"
  if [[ -n "${license}" ]]; then
    check "SimpleAgenticScenario license (${license})" true
  else
    warn_note "SimpleAgenticScenario — no SPDX license (REFERENCE only, NO-GO install)"
  fi
else
  warn_note "gh unavailable — skip GitHub license check"
fi

warn_note "2606.31518 — REFERENCE taxonomy; steal OO1–OO4 selection table + metrics"
warn_note "cpee.org / autobpmn.ai — external demo platforms; no Cemini prod install"
warn_note "Harness steals: OO3/OO4 for regulated flows; engine logging over agent self-log"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
