#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K365 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-asleval-privacy-exposure-displacement-2609.18864.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/privacy-exposure-displacement-eval.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/privacy-exposure-displacement-eval.md"
check "policy K365" grep -q "K365" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K365" grep -q "K365" "${REPO_ROOT}/.cursor/rules/ccc-k363-k367-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/privacy-exposure-displacement-eval"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-asleval-privacy-exposure-displacement-2609.18864.md' '${REPO_ROOT}/wiki/concepts/privacy-exposure-displacement-eval.md'"
warn_note "K365 Cybersec-primary + ADOPT eval"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
