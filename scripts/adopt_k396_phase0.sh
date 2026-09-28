#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K396 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-rectoolbench-fuzzy-intent-tool-orchestration-2609.30717.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/recommendation-tool-orchestration-fuzzy-intent-eval.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/recommendation-tool-orchestration-fuzzy-intent-eval.md"
check "policy K396" grep -q "K396" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K396" grep -q "K396" "${REPO_ROOT}/.cursor/rules/ccc-k396-k400-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/rectoolbench"
warn_note "K396 ADOPT eval-first"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
