#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K282 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentrewind-recoverable-execution-2608.14380.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/recoverable-agent-execution-checkpoints.md"
check "entity agentrewind" test -f "${REPO_ROOT}/wiki/entities/tools/agentrewind.md"
check "entity mettlebench" test -f "${REPO_ROOT}/wiki/entities/tools/mettlebench.md"
check "policy K282" grep -q "K282" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone recorder" test -d "${REPO_ROOT}/.local/adopts/replay-agent-recorder"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/replay-agent-recorder/LICENSE"
check "clone mettlebench" test -d "${REPO_ROOT}/.local/adopts/MettleBench"
check "apache-license" grep -qi "Apache License" "${REPO_ROOT}/.local/adopts/MettleBench/LICENSE"
warn_note "K282 AgentRewind MIT + MettleBench Apache-2.0 GO REFERENCE; framework runtime wont_wire (no CCC harness integration)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
