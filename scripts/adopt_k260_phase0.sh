#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K260 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/adversarial-curriculum-structured-reward-doc-fidelity.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/residencyrl.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-08-10_k260-residencyrl-adversarial-curriculum-prod.md"
check "hands-on" test -f "${REPO_ROOT}/briefs/2026-08-10_k260-harness-policy-hands-on.md"
check "handoff" test -f "${REPO_ROOT}/wiki/briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md"
check "policy rule mentions K260" grep -q "K260" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
# Explicitly expect NO local adopt
if [[ -d "${REPO_ROOT}/.local/adopts/ResidencyRL" ]] || [[ -d "${REPO_ROOT}/.local/adopts/residencyrl" ]]; then
  echo "  FAIL  unexpected ResidencyRL adopt dir (code is closed)"
  fail=$((fail+1))
else
  echo "  PASS  no ResidencyRL local adopt (NO-GO closed code)"
  pass=$((pass+1))
fi
warn_note "Clinical OOD — pattern ADOPT only; no Gemini medical agent runtime"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
