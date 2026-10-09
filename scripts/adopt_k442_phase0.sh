#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K442 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-epistemic-humility-knowledge-conflict-2610.12360.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/epistemic-humility-identify-solve-escalate.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/epistemic-humility-identify-solve-escalate.md"
check "policy K442" grep -q "K442" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K442" grep -q "K442" "${REPO_ROOT}/.cursor/rules/ccc-k441-k444-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/EpistemicHumilityLLMAgents"
warn_note "K442 ADOPT eval-methodology (Claude Code harness eval)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
