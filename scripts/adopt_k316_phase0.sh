#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K316 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-lifeplanner-geospatial-agents-2608.25039.md"
check "policy K316" grep -q "K316" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K316" grep -q "K316" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no LifePlanner clone" test ! -d "${REPO_ROOT}/.local/adopts/LifePlanner"
warn_note "K316 OOD trip-planning bench — short stub; wont_wire. Steal: fail from incomplete evidence + imprecise tools, not model size."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
