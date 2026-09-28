#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K398 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-muslim-arabic-voice-ai-platform-2609.31511.md"
check "policy K398" grep -q "K398" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K398" grep -q "K398" "${REPO_ROOT}/.cursor/rules/ccc-k396-k400-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/muslim-voice"
warn_note "K398 OOD voice domain stub"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
