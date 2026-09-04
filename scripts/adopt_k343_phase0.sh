#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K343 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-environment-evolution-terminal-agents-2609.04128.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/environment-evolution-terminal-agents.md"
check "policy K343" grep -q "K343" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K343" grep -q "K343" "${REPO_ROOT}/.cursor/rules/ccc-k342-k345-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/Terminal-X"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/environment-evolution-terminal-agents.md"
warn_note "K343 ADOPT eval — off-policy environment evolution for terminal agents. Terminal-X null SPDX → no clone."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
