#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K425 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-frugalevo-cost-aware-program-evolution-2610.03675.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/cost-aware-program-evolution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/cost-aware-program-evolution.md"
check "policy K425" grep -q "K425" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K425" grep -q "K425" "${REPO_ROOT}/.cursor/rules/ccc-k421-k425-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/frugalevo"
warn_note "K425 ADOPT pattern (Apache-2.0)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
