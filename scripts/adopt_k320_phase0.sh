#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K320 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-claude-code-complete-user-handbook-2608.26742.md"
check "entity delta" grep -q "Handbook delta (K320" "${REPO_ROOT}/wiki/entities/tools/claude-code.md"
check "policy K320" grep -q "K320" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K320" grep -q "K320" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no handbook clone" test ! -d "${REPO_ROOT}/.local/adopts/claude-code-handbook"
warn_note "K320 ADOPT practitioner reference — delta only, not 208-page dump; [TENTATIVE] flags vs Anthropic docs."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
