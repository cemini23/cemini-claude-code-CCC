#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K344 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-nlip-natural-language-interaction-protocol-2609.04135.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/natural-language-interaction-protocol.md"
check "policy K344" grep -q "K344" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K344" grep -q "K344" "${REPO_ROOT}/.cursor/rules/ccc-k342-k345-phase1-wires.mdc"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/natural-language-interaction-protocol.md"
warn_note "K344 NLIP Ecma awareness — CC0 ecma_draft digest pointer optional; no catalog mirror; runtime wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
