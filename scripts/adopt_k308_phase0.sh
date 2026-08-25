#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K308 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/agent-as-intermediary-engineer.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/metacaster.md"
check "policy K308" grep -q "K308" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K308" grep -q "K308" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/metacaster"
check "mit-license-on-disk" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/metacaster/LICENSE"
check "skill" test -f "${REPO_ROOT}/.cursor/skills/intermediary-engineer/SKILL.md"
warn_note "K308 MetaCaster MIT GO REFERENCE clone; TSF runtime wont_wire; GuruWatcher intermediary-engineer pointer only (pairs K281)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
