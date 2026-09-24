#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K388 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-shopping-algorithm-agent-heuristic-surrogate-2609.28372.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/agent-heuristic-surrogate-consumer-eval.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/agent-heuristic-surrogate-consumer-eval.md"
check "policy K388" grep -q "K388" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K388" grep -q "K388" "${REPO_ROOT}/.cursor/rules/ccc-k385-k389-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/agent-heuristic-surrogate-consumer-eval"
warn_note "K388 ADOPT eval + policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
