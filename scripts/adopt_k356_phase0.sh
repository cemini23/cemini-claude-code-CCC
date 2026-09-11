#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K356 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-cobra-skills-bandit-evolution-2609.11682.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/bandit-guided-skill-evolution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/bandit-guided-skill-evolution.md"
check "policy K356" grep -q "K356" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K356" grep -q "K356" "${REPO_ROOT}/.cursor/rules/ccc-k346-k357-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/bandit-guided-skill-evolution"
warn_note "K356 ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
