#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K371 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-overclaiming-propensity-frontier-agents-2609.20812.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/overclaiming-propensity-agent-measurement.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/overclaiming-propensity-agent-measurement.md"
check "policy K371" grep -q "K371" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K371" grep -q "K371" "${REPO_ROOT}/.cursor/rules/ccc-k369-k372-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/overclaiming-propensity-agent-measurement"
check "ocp helper" test -f "${REPO_ROOT}/scripts/ocp_claim_check.py"
check "ocp selftest" python3 "${REPO_ROOT}/scripts/ocp_claim_check.py" selftest
warn_note "K371 ADOPT eval + policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
