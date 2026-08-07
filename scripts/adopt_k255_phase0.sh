#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K255 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/interpretable-agentic-document-ops.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/read-agentic-document-search.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-07_k255-read-agentic-document-ops-prod.md" || warn_note "prod brief pending"
check "READ clone" test -d "${REPO_ROOT}/.local/adopts/READ"
check "READ LICENSE" test -f "${REPO_ROOT}/.local/adopts/READ/LICENSE"
check "READ LICENSE text MIT" grep -q "MIT License" "${REPO_ROOT}/.local/adopts/READ/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
