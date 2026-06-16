#!/usr/bin/env bash
# K116 Phase-0 — OrchRM, HarnessX, LLM-as-Code cluster (2026-06-16 ingest).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K116 Phase-0 adoption checks (CCC)"
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

echo ""
echo "=== 2606.13598 Orch-RM (Wang-ML-Lab/OrchRM) ==="
if command -v gh >/dev/null 2>&1; then
  if gh api repos/Wang-ML-Lab/OrchRM --jq '.name' >/dev/null 2>&1; then
    lic="$(gh api repos/Wang-ML-Lab/OrchRM --jq '.license.spdx_id' 2>/dev/null || echo "")"
    check "OrchRM repo exists" true
    echo "  INFO  license: ${lic:-none}"
  else
    warn_note "Wang-ML-Lab/OrchRM — 404 (paper: code will be available)"
  fi
else
  warn_note "gh not available"
fi

echo ""
echo "=== 2606.14249 HarnessX (Darwin Agent Team) ==="
warn_note "no public repo — paper promises future open-source (REFERENCE)"

echo ""
echo "=== 2606.15874 LLM-as-Code (CityU / Tencent Jarvis) ==="
warn_note "KDD 2026 workshop paper — no framework repo found (REFERENCE)"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
echo "Verdict: pattern steals only — BoN orchestration RM, HarnessX D1–D9 taxonomy, program-owned control flow"
exit 0
