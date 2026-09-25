#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K393 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-instrumental-monitor-evasion-task-pressure-2609.30217.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/instrumental-monitor-evasion-under-task-pressure.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/instrumental-monitor-evasion-under-task-pressure.md"
check "policy K393" grep -q "K393" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K393" grep -q "K393" "${REPO_ROOT}/.cursor/rules/ccc-k390-k394-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/instrumental-monitor-evasion"
warn_note "K393 Cybersec + ADOPT eval"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
