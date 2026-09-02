#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K334 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-as-eval-artifact.md"
check "policy K334" grep -q "K334" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K334" grep -q "K334" "${REPO_ROOT}/.cursor/rules/ccc-k333-k336-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/HarnessDev"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/harness-as-eval-artifact.md"
warn_note "K334 ADOPT eval — unit of eval = runnable harness; Creation+Evolution; unstable/partial transfer; state often never fires. Project page only — no SPDX → policy only. Never auto-evolve .cursor/skills."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
