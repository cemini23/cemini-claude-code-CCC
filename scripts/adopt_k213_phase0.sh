#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K213 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "ACM paper — checklist only; no product install"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/agentic-context-management-lifecycle.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentic-context-management-2607.21503.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-24_k213-agentic-context-management-lifecycle-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
