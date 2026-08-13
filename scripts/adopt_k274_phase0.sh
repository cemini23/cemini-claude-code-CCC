#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K274 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-convergent-detour-hijacking-cdh-2608.12273.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/convergent-detour-hijacking-progressive-disclosure.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/patterns/convergent-detour-hijacking.md"
check "policy K274" grep -q "K274" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K274 attack pattern — no code/SPDX; policy_wired, runtime wont_wire"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
