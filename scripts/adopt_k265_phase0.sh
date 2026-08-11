#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K265 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-she-safety-harness-evolution-2608.09885.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/trajectory-driven-safety-harness-evolution.md"
check "policy K265" grep -q "K265" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "SHE clone" test -d "${REPO_ROOT}/.local/adopts/SHE"
check "SHE LICENSE" test -f "${REPO_ROOT}/.local/adopts/SHE/LICENSE"
check "SHE Apache" grep -q "Apache License" "${REPO_ROOT}/.local/adopts/SHE/LICENSE"
if du -sm "${REPO_ROOT}/.local/adopts/SHE" | awk '{exit !($1<500)}'; then echo "  PASS  SHE size <500MB"; pass=$((pass+1)); else echo "  FAIL  SHE size"; fail=$((fail+1)); fi
warn_note "HITL only — do not auto-mutate prod harness"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
