#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K322 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-more-mixture-of-roles-2608.27338.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/query-aware-role-fusion.md"
check "policy K322" grep -q "K322" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K322" grep -q "K322" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no MoRe clone" test ! -d "${REPO_ROOT}/.local/adopts/MoRe"
check "no GRPO wired" grep -q "GRPO.*wont_wire" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
warn_note "K322 WATCH — query-aware steering-vector fusion; GRPO wont_wire; no clone; steal: don't auto-spawn MAS."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
