#!/usr/bin/env bash
# K172 Phase-0 — MCP contract validation gate (2607.12220)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K172 Phase-0 (CCC) — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "NO-GO local paper-repo clone (license and/or no public code) — pattern ADOPT only"
check "mcp-contract-grounded-synthesis-and-validation-gate.md" test -f "${REPO_ROOT}/wiki/concepts/mcp-contract-grounded-synthesis-and-validation-gate.md"
check "arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md" test -f "${REPO_ROOT}/wiki/sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md"
check "jsalfity-agentic-bt-mcp-artifacts.md" test -f "${REPO_ROOT}/wiki/entities/tools/jsalfity-agentic-bt-mcp-artifacts.md"
check "2026-07-16_k172-mcp-contract-validation-gate-prod.md" test -f "${REPO_ROOT}/briefs/2026-07-16_k172-mcp-contract-validation-gate-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
