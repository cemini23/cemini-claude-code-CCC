#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="${REPO_ROOT}/.local/adopts/Recuris"
echo "K314 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-recuris-em-wm-memory-evolution-2608.24876.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/experiential-working-memory-coupling.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/recuris.md"
check "policy K314" grep -q "K314" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K314" grep -q "K314" "${REPO_ROOT}/.cursor/rules/ccc-k310-k314-phase1-wires.mdc"
if [ -d "${ADOPT}" ]; then
  check "clone exists" test -d "${ADOPT}"
  check "LICENSE on disk" grep -qi "Apache License" "${ADOPT}/LICENSE"
  sz="$(du -sm "${ADOPT}" | cut -f1)"; if [ "${sz}" -lt 500 ]; then echo "  PASS  clone size ${sz}MB <500MB"; pass=$((pass+1)); else echo "  FAIL  clone size ${sz}MB >=500MB"; fail=$((fail+1)); fi
else
  warn_note "Recuris clone absent — expected Apache-2.0 GO REFERENCE at .local/adopts/Recuris"
fi
warn_note "K314 runtime wont_wire — HITL before any skill self-write; validation-gated patch admission only."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
