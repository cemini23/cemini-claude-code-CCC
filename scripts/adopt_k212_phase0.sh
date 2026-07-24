#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K212 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "CLS-Data/ns_core NO-GO — no SPDX LICENSE"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/local-open-weight-agentic-coding-eval.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentic-coding-without-cloud-2607.21482.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/rrbench.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-24_k212-local-open-weight-agentic-coding-prod.md"
check "RRBench" test -d "${REPO_ROOT}/.local/adopts/RRBench/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
