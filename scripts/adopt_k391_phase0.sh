#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K391 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-xrr-curves-x-ray-calc-agent-2609.28926.md"
check "policy K391" grep -q "K391" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K391" grep -q "K391" "${REPO_ROOT}/.cursor/rules/ccc-k390-k394-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/x-ray-calc-xrr"
warn_note "K391 OOD materials stub"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
