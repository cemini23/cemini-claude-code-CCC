#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="${REPO_ROOT}/.local/adopts/StarHarness"
echo "K313 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/stratified-harness-evolution.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/starharness.md"
check "policy K313" grep -q "K313" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K313" grep -q "K313" "${REPO_ROOT}/.cursor/rules/ccc-k310-k314-phase1-wires.mdc"
if [ -d "${ADOPT}" ]; then
  check "clone exists" test -d "${ADOPT}"
  check "LICENSE on disk" grep -qi "MIT License" "${ADOPT}/LICENSE"
  sz="$(du -sm "${ADOPT}" | cut -f1)"; if [ "${sz}" -lt 500 ]; then echo "  PASS  clone size ${sz}MB <500MB"; pass=$((pass+1)); else echo "  FAIL  clone size ${sz}MB >=500MB"; fail=$((fail+1)); fi
else
  warn_note "StarHarness clone absent — expected MIT GO REFERENCE at .local/adopts/StarHarness"
fi
warn_note "K313 trainer/runtime wont_wire — REFERENCE only; do NOT auto-evolve .cursor/skills; no closed rewrite of '## Verify'."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
