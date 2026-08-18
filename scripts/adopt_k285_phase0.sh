#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K285 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/signed-mandate-mcp-protocol-enforcement.md"
check "entity mandato" test -f "${REPO_ROOT}/wiki/entities/tools/mandato.md"
check "pattern signed-mandate" test -f "${REPO_ROOT}/wiki/entities/patterns/signed-mandate-mcp-proxy.md"
check "policy K285" grep -q "K285" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" bash -c '! test -d "${REPO_ROOT}/.local/adopts/mandato"'
warn_note "K285 Mandato signed-mandate MCP proxy — no public SPDX clone; policy only. Atto-priority (pairs K278 InterSAGE, K271 auth gateway)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
