#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K241 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-llms-fail-tabular-prediction-2608.02412.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/llm-tabular-prediction-dimensionality-failure.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-04_k241-llm-tabular-prediction-failure-prod.md" || warn_note "prod brief pending — parent handoff"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
