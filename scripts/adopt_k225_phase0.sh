#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K225 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Do not curl|sh shard-demo install.sh — clone only"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/distributed-harness-security-controls.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-shard-harness-security-distribution-2607.25890.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-30_k225-shard-harness-security-distribution-prod.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/shard-secure-harness-distribution.md"
check "clone-lab" test -d "${REPO_ROOT}/.local/adopts/agent-security-lab/.git"
check "clone-demo" test -d "${REPO_ROOT}/.local/adopts/shard-demo/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
