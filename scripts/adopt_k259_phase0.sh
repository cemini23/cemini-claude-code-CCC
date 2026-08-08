#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K259 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-cascade-agentic-regulatory-network-2608.05359.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-claim-validation-and-parameter-grounding.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/cascade-mcp.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-08_k259-cascade-mcp-claim-validation-prod.md"
check "CASCADE clone" test -d "${REPO_ROOT}/.local/adopts/CASCADE"
check "CASCADE LICENSE" test -f "${REPO_ROOT}/.local/adopts/CASCADE/LICENSE"
check "CASCADE MIT text" grep -q "MIT License" "${REPO_ROOT}/.local/adopts/CASCADE/LICENSE"
if du -sm "${REPO_ROOT}/.local/adopts/CASCADE" | awk '{exit !($1<500)}'; then
  echo "  PASS  CASCADE size <500MB"; pass=$((pass+1))
else
  echo "  FAIL  CASCADE size >=500MB"; fail=$((fail+1))
fi
warn_note "Cancer genomics OOD — runtime wont_wire; do not download DepMap (~413MB) or model into adopt"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
