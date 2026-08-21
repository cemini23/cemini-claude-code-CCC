#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K298 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/adaptive-validation-task-selection-harness-optimization.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/task-coevolve.md"
check "policy K298" grep -q "K298" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" test ! -d "${REPO_ROOT}/.local/adopts/Task-CoEvolve"
warn_note "K298 Task-CoEvolve no LICENSE -> NO-GO clone; policy_wired (pairs K281/K292/K162)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
