#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K292 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harness-continual-learning-2608.19013.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/harness-continual-learning-guarded-evolution.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/harness-continual-learning-hcl.md"
check "policy K292" grep -q "K292" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K292 HCL — no public code; policy only (pairs K281/K162/K263)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
