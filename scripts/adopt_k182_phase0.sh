#!/usr/bin/env bash
# K182 Phase-0 — ACP three-layer (2607.14919)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K182 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "ACP three-layer (2607.14919)"
check "$(basename wiki/concepts/acp-mcp-three-layer-human-agent-execution.md)" test -e "${REPO_ROOT}/wiki/concepts/acp-mcp-three-layer-human-agent-execution.md"
check "$(basename wiki/entities/tools/sancho-acp-clients.md)" test -e "${REPO_ROOT}/wiki/entities/tools/sancho-acp-clients.md"
check "$(basename briefs/2026-07-17_k182-acp-mcp-three-layer-prod.md)" test -e "${REPO_ROOT}/briefs/2026-07-17_k182-acp-mcp-three-layer-prod.md"
check "$(basename .local/adopts/sancho-acp-clients/LICENSE)" test -e "${REPO_ROOT}/.local/adopts/sancho-acp-clients/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
