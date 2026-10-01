#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K415 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-turbo-harness-instance-adaptive-2609.40330.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/instance-adaptive-harness-optimization.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/instance-adaptive-harness-optimization.md"
check "policy K415" grep -q "K415" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K415" grep -q "K415" "${REPO_ROOT}/.cursor/rules/ccc-k411-k415-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/turbo-harness"
warn_note "K415 CONDITIONAL-GO (MIT)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
