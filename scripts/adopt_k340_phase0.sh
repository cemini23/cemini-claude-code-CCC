#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K340 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-policy-co-evolution-safety.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/safeevolve.md"
check "policy K340" grep -q "K340" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K340" grep -q "K340" "${REPO_ROOT}/.cursor/rules/ccc-k337-k341-phase1-wires.mdc"
check "clone dir" test -d "${REPO_ROOT}/.local/adopts/SafeEvolve"
check "MIT license" grep -qi "MIT" "${REPO_ROOT}/.local/adopts/SafeEvolve/LICENSE" 2>/dev/null || grep -qi "MIT" "${REPO_ROOT}/.local/adopts/SafeEvolve/LICENSE.md" 2>/dev/null
check "clone size" bash -c "test \$(du -sm \"${REPO_ROOT}/.local/adopts/SafeEvolve\" | cut -f1) -lt 500"
check "entity wont_wire" grep -q "wire_status: wont_wire" "${REPO_ROOT}/wiki/entities/tools/safeevolve.md"
warn_note "K340 ADOPT policy — harness–policy co-evolution; REFERENCE clone only; trainer wont_wire; never auto-evolve .cursor/skills."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
