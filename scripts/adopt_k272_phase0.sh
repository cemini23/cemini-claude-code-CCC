#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K272 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-callable-spectroscopic-binary-2608.10866.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/domain-solvers-as-agent-callable-mcp-skills.md"
check "policy K272" grep -q "K272" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/agent4binary"
check "MIT" grep -q "MIT License" "${REPO_ROOT}/.local/adopts/agent4binary/LICENSE"
if du -sm "${REPO_ROOT}/.local/adopts/agent4binary" | awk '{exit !($1<500)}'; then echo "  PASS  size <500MB"; pass=$((pass+1)); else echo "  FAIL  size"; fail=$((fail+1)); fi
warn_note "astronomy OOD — REFERENCE only; wont_wire runtime"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
