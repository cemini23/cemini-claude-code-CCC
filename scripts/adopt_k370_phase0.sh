#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K370 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harness-design-coding-agents-empirical-2609.20804.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/coding-agent-harness-component-design.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/coding-agent-harness-component-design.md"
check "policy K370" grep -q "K370" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K370" grep -q "K370" "${REPO_ROOT}/.cursor/rules/ccc-k369-k372-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/coding-agent-harness-component-design"
warn_note "K370 ADOPT eval-first"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
