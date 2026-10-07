#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K431 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-one-step-at-a-time-step-level-sop-2610.07817.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/step-level-process-delivery.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/step-level-process-delivery.md"
check "policy K431" grep -q "K431" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K431" grep -q "K431" "${REPO_ROOT}/.cursor/rules/ccc-k431-k435-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/sop-mcp"
warn_note "K431 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
