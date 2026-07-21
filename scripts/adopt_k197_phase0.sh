#!/usr/bin/env bash
# K197 Phase-0 — DataFlow-Harness NL2Pipeline (2607.16617)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K197 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "DataFlow-WebUI has no SPDX — NO-GO; DataFlow Apache is REFERENCE only"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/nl2pipeline-platform-grounded-mutations.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-dataflow-harness-nl2pipeline-2607.16617.md"
check "entity DataFlow" test -f "${REPO_ROOT}/wiki/entities/tools/dataflow-opendcai.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-21_k197-nl2pipeline-dataflow-harness-prod.md"
check "local DataFlow clone" test -d "${REPO_ROOT}/.local/adopts/DataFlow/.git"
check "DataFlow LICENSE" test -f "${REPO_ROOT}/.local/adopts/DataFlow/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
