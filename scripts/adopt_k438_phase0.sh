#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K438 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-decisive-step-base-model-probe-2610.10478.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/decisive-step-base-model-probe.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/decisive-step-base-model-probe.md"
check "policy K438" grep -q "K438" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K438" grep -q "K438" "${REPO_ROOT}/.cursor/rules/ccc-k436-k440-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/decisive-step"
warn_note "K438 ADOPT eval-methodology"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
