#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K321 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-asil-structured-state-semantic-actions-2608.26991.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/structured-state-semantic-actions.md"
check "policy K321" grep -q "K321" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K321" grep -q "K321" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no ASIL clone" test ! -d "${REPO_ROOT}/.local/adopts/ASIL"
warn_note "K321 ADOPT policy — JSON observations + semantic actions over screenshot-click; no SPDX hit → policy; GUI runtime wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
