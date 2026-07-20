#!/usr/bin/env bash
# K190 Phase-0 — MCP cloud gateway hybrid recommend (2607.15593)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K190 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Alibaba gateway proprietary — NO-GO install"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-scalable-mcp-cloud-gateway-2607.15593.md"
check "entity agentgateway" test -f "${REPO_ROOT}/wiki/entities/tools/agentgateway.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-20_k190-mcp-cloud-gateway-hybrid-recommend-prod.md"
check "local agentgateway clone" test -d "${REPO_ROOT}/.local/adopts/agentgateway/.git"
check "agentgateway LICENSE" test -f "${REPO_ROOT}/.local/adopts/agentgateway/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
