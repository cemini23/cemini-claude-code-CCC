#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K397 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-safety-bounded-sdc-mcp-gateway-medical-2609.31358.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/safety-bounded-sdc-mcp-gateway.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/safety-bounded-sdc-mcp-gateway.md"
check "policy K397" grep -q "K397" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K397" grep -q "K397" "${REPO_ROOT}/.cursor/rules/ccc-k396-k400-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/sdc-mcp-gateway"
warn_note "K397 ADOPT policy awareness"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
