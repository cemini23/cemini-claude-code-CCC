#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K318 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-progrouter-progress-orchestration-2608.25992.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/progress-guided-step-routing.md"
check "policy K318" grep -q "K318" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K318" grep -q "K318" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no ProgRouter clone" test ! -d "${REPO_ROOT}/.local/adopts/ProgRouter"
warn_note "K318 ADOPT step-wise routing — progress + remaining difficulty + cost; no public SPDX → policy."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
