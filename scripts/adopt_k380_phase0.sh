#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K380 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-onpanda-on-policy-token-alignment-2609.24983.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/on-policy-token-alignment-annotation.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/on-policy-token-alignment-annotation.md"
check "policy K380" grep -q "K380" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K380" grep -q "K380" "${REPO_ROOT}/.cursor/rules/ccc-k376-k384-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/on-policy-token-alignment-annotation"
warn_note "K380 ADOPT eval axis"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
