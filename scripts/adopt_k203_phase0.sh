#!/usr/bin/env bash
# K203 Phase-0 — BioSecBench verifiable eval
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K203 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/verifiable-deterministic-agent-benchmarking.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-biosecbench-surveillance-2607.19262.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-22_k203-verifiable-agent-benchmark-prod.md"
warn_note "Biosec domain → cybersec; CCC keeps eval methodology only"
check "biosecbench clone" test -d "${REPO_ROOT}/.local/adopts/biosecbench-surveillance/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
