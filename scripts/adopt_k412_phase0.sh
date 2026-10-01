#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K412 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-skill-based-agents-power-system-studies-2609.40272.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/claude-code-vs-agents-sdk-engineering-harness.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/claude-code-vs-agents-sdk-engineering-harness.md"
check "policy K412" grep -q "K412" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K412" grep -q "K412" "${REPO_ROOT}/.cursor/rules/ccc-k411-k415-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/pnnl-power-agents"
warn_note "K412 ADOPT pattern (Claude Code harness eval)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
