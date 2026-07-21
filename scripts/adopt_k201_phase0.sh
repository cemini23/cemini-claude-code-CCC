#!/usr/bin/env bash
# K201 Phase-0 — SWE-Pruner Pro internal prune (2607.18213)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K201 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "swe-pruner-pro has no SPDX — NO-GO; closed models keep K115 N/W"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/backbone-internal-tool-output-pruning.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-swe-pruner-pro-internal-prune-2607.18213.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-21_k201-swe-pruner-internal-prune-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
