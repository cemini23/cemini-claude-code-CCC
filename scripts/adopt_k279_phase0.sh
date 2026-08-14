#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K279 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/marc-clinical-multi-agent-coordination.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/marc-v1.md"
check "policy K279" grep -q "K279" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/MARC-v1"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/MARC-v1/LICENSE"
warn_note "K279 MARC-v1 MIT GO REFERENCE (clone present); clinical wont_wire — decomposer/stage-wise attribution steal only."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
