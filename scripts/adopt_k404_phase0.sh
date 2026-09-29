#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K404 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harness-learning-test-time-adaptation-2609.35738.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-learning-test-time-adaptation.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/harness-learning-test-time-adaptation.md"
check "policy K404" grep -q "K404" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K404" grep -q "K404" "${REPO_ROOT}/.cursor/rules/ccc-k401-k405-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/harness-learning"
warn_note "K404 ADOPT eval-first"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
