#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K441 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-security-by-design-point-of-execution-2610.10659.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/specification-versus-capability-failure-attribution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/specification-versus-capability-failure-attribution.md"
check "policy K441" grep -q "K441" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K441" grep -q "K441" "${REPO_ROOT}/.cursor/rules/ccc-k441-k444-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/sbd-toe-mcp"
warn_note "K441 ADOPT pattern (MCP-delivered governed requirements)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
