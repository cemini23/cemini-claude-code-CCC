#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K246 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-multiglobeqa-geospatial-reasoning-2608.03882.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/geospatial-computation-vs-parametric-knowledge.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/multiglobeqa.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/MultiGlobeQA" || warn_note "clone dir missing — git clone pending"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-05_k246-multiglobeqa-geospatial-computation-prod.md" || warn_note "prod brief pending — parent handoff"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
