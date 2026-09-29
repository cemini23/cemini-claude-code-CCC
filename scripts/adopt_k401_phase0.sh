#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K401 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-htn-planning-mcp-multi-server-coordination-2609.33731.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/htn-planning-mcp-multi-server-coordination.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/htn-planning-mcp-multi-server-coordination.md"
check "policy K401" grep -q "K401" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K401" grep -q "K401" "${REPO_ROOT}/.cursor/rules/ccc-k401-k405-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/hplan26-artifact"
warn_note "K401 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
