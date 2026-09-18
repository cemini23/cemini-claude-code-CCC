#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K369 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-closed-world-resolution-tool-hallucination-2609.19425.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/closed-world-tool-hallucination-resolution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/closed-world-tool-hallucination-resolution.md"
check "policy K369" grep -q "K369" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K369" grep -q "K369" "${REPO_ROOT}/.cursor/rules/ccc-k369-k372-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/closed-world-tool-hallucination-resolution"
warn_note "K369 ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
