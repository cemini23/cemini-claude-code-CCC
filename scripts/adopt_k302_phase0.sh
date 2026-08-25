#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K302 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-aid-guard-stateful-authorization-2608.21159.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/authorization-to-effect-closure.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/aid-guard.md"
check "policy K302" grep -q "K302" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K302" grep -q "K302" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
check "skill" test -f "${REPO_ROOT}/.cursor/skills/aid-guard-commit/SKILL.md"
check "helper-selftest" python3 "${REPO_ROOT}/scripts/aid_guard_commit.py" selftest
warn_note "K302 AID-Guard no public SPDX repo — policy_wired + commit helper; pairs K239/K285. Not a LIVE proxy."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
