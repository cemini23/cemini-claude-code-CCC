#!/usr/bin/env bash
# K154 Phase-0 — Ensemble QSP hierarchical memory (2607.07666).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K154 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.07666 — REFERENCE; AstraZeneca QSP domain off prod"
warn_note "Steal: short/mid/long hierarchical memory with explicit caps"
warn_note "Steal: evict completed work to bound mid-term state (~301 token median)"
warn_note "No David adopt — pharma modeling off-domain"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/hierarchical-bounded-agent-memory.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-ensemble-qsp-hierarchical-memory-2607.07666.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-13_k154-hierarchical-bounded-agent-memory-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
