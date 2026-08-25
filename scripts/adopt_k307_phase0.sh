#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K307 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mediskill-evo-process-constrained-2608.23397.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/process-constrained-self-evolution.md"
check "policy K307" grep -q "K307" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K307" grep -q "K307" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
warn_note "K307 MediSkill-Evo typed banks + frozen snapshot + process critic; clinical wont_wire; no unattended skill evolve (pairs K237/K162)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
