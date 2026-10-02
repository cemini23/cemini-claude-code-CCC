#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K419 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-vista-lossless-visual-memory-harness-2610.02200.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/lossless-visual-memory-harness.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/lossless-visual-memory-harness.md"
check "policy K419" grep -q "K419" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K419" grep -q "K419" "${REPO_ROOT}/.cursor/rules/ccc-k416-k420-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/VISTA"
warn_note "K419 ADOPT pattern (MIT)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
