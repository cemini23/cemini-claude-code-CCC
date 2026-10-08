#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K440 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-embodiedrsi-value-of-information-experiments-2610.10498.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/value-of-information-experiment-selection.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/value-of-information-experiment-selection.md"
check "policy K440" grep -q "K440" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K440" grep -q "K440" "${REPO_ROOT}/.cursor/rules/ccc-k436-k440-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/agentic_robotics"
warn_note "K440 REFERENCE (cross-domain; pattern transfers)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
