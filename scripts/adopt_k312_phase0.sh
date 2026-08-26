#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K312 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-stepguard-step-level-guardrails-2608.24777.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/step-level-tool-guardrails.md"
check "policy K312" grep -q "K312" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K312" grep -q "K312" "${REPO_ROOT}/.cursor/rules/ccc-k310-k314-phase1-wires.mdc"
check "no StepGuard clone" test ! -d "${REPO_ROOT}/.local/adopts/StepGuard"
warn_note "K312 github.com/zheng977/StepGuard exists but license:null (gh API 2026-08-26) -> NO-GO clone. Policy: gate candidate tool actions before execute; trainer wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
