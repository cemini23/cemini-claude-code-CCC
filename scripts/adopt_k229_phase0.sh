#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K229 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/cost-aware-tool-acquisition-stopping.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-cam-df-cost-aware-tool-stopping-2607.27083.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-30_k229-cam-df-tool-acquisition-stopping-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
