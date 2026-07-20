#!/usr/bin/env bash
# K193 Phase-0 — BusinessCaseBench rubrics (2607.16057)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K193 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "No public BusinessCaseBench package — methodology ADOPT only"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/businesscasebench-rubric-from-expert-solutions.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-businesscasebench-knowledge-work-2607.16057.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-20_k193-businesscasebench-rubric-eval-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
