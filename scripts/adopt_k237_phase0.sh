#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K237 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-educating-agentic-engineer-accel-2607.29610.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/accel-agentic-engineer-competencies.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-03_k237-accel-agentic-engineer-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
