#!/usr/bin/env bash
# K205 Phase-0 — Agents in the Wild
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K205 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/production-agent-deployment-checklist.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agents-in-the-wild-deployment-2607.19336.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-22_k205-agents-in-the-wild-deploy-prod.md"
warn_note "Tutorial only — no product install"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
