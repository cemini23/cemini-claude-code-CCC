#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K361 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-sciencebuddy-recursive-self-improvement-2609.17523.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/recursive-in-recursive-harness-improvement.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/recursive-in-recursive-harness-improvement.md"
check "policy K361" grep -q "K361" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K361" grep -q "K361" "${REPO_ROOT}/.cursor/rules/ccc-k358-k362-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/recursive-in-recursive-harness-improvement"
warn_note "K361 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
