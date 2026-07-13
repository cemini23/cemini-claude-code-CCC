#!/usr/bin/env bash
# K153 Phase-0 — MILES modular instruction memory (2607.06974).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K153 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.06974 — REFERENCE; no public GitHub at Phase-0"
warn_note "Steal: modular sub-goal + sub-instruction memory units"
warn_note "Steal: coarse-to-fine learnable selection for final-answer correctness"
warn_note "No David adopt — sequential reasoning memory not TipDrop-primary"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/modular-instruction-memory-learnable-selection.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-miles-modular-instruction-memory-2607.06974.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-13_k153-miles-modular-instruction-memory-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
