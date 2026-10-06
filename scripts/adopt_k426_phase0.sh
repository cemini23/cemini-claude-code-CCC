#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K426 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mcpacific-mcp-tool-taxonomy-2610.05319.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-tool-taxonomy-navigation.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/mcp-tool-taxonomy-navigation.md"
check "policy K426" grep -q "K426" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K426" grep -q "K426" "${REPO_ROOT}/.cursor/rules/ccc-k426-k430-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/mcpacific"
warn_note "K426 ADOPT pattern (no repo)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
