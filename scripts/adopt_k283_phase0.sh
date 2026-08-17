#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K283 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-twin-test-time-digital-twin-2608.14490.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/test-time-world-model-validate-before-act.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/twin-arc-agi-3.md"
check "policy K283" grep -q "K283" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/TWIN-ARC-AGI-3"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/TWIN-ARC-AGI-3/LICENSE"
warn_note "K283 Twin MIT GO REFERENCE (clone present); ARC bench runtime wont_wire — harness-enforced validate-before-act steal only (pairs K231 Tycho)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
