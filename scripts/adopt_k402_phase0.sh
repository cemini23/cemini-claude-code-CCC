#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K402 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mcp-developer-error-messages-hurt-agents-2609.35381.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-developer-error-messages-agent-recovery.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/mcp-developer-error-messages-agent-recovery.md"
check "policy K402" grep -q "K402" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K402" grep -q "K402" "${REPO_ROOT}/.cursor/rules/ccc-k401-k405-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/mcp-dev-errors"
warn_note "K402 ADOPT policy + eval"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
