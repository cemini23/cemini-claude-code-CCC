#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K305 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mcp-universe-rl-2608.22167.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/mcp-universe-rl.md"
check "policy K305" grep -q "K305" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K305" grep -q "K305" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/MCP-Universe"
check "apache-license-on-disk" grep -qi "Apache License" "${REPO_ROOT}/.local/adopts/MCP-Universe/LICENSE.txt"
warn_note "K305 MCP-Universe RL Apache-2.0 GO REFERENCE clone; trainer runtime wont_wire; no GRPO wired harness; no HF weights."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
