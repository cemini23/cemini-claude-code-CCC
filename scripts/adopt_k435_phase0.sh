#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K435 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-verifine-judge-policy-co-evolution-2610.08761.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/judge-policy-co-evolution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/judge-policy-co-evolution.md"
check "policy K435" grep -q "K435" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K435" grep -q "K435" "${REPO_ROOT}/.cursor/rules/ccc-k431-k435-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/verifine"
warn_note "K435 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
