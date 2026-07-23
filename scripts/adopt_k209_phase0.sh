#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K209 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Public kit is benchmark-only; retrieval engine not included"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/multi-stage-rag-architect-reviewer-triad.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-iterasim-rag-multistage-2607.20346.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/iterasim-rag-public.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-23_k209-iterasim-multistage-rag-triad-prod.md"
check "local clone" test -d "${REPO_ROOT}/.local/adopts/iterasim-rag-public/.git"
check "MIT LICENSE" test -f "${REPO_ROOT}/.local/adopts/iterasim-rag-public/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
