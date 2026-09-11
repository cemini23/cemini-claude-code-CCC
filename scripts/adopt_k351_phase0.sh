#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K351 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-edge-slm-mcp-tool-reliability-2609.07370.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/edge-slm-mcp-tool-reliability.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/edge-slm-mcp-tool-reliability.md"
check "policy K351" grep -q "K351" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K351" grep -q "K351" "${REPO_ROOT}/.cursor/rules/ccc-k346-k357-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/edge-slm-mcp-tool-reliability"
warn_note "K351 ADOPT eval axis"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
