#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K382 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-a2m-mcp-metadata-hijacking-2609.26761.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-tool-metadata-supply-chain-risk.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/mcp-tool-metadata-supply-chain-risk.md"
check "policy K382" grep -q "K382" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K382" grep -q "K382" "${REPO_ROOT}/.cursor/rules/ccc-k376-k384-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/mcp-tool-metadata-supply-chain-risk"
warn_note "K382 Cybersec-primary ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
