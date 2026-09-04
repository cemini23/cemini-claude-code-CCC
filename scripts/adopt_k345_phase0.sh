#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K345 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-research-swarm-cheating-whistleblowing-2609.04170.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/knowledge-commons-governance-multi-agent.md"
check "policy K345" grep -q "K345" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K345" grep -q "K345" "${REPO_ROOT}/.cursor/rules/ccc-k342-k345-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/research-swarm-cheating"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/knowledge-commons-governance-multi-agent.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-research-swarm-cheating-whistleblowing-2609.04170.md' '${REPO_ROOT}/wiki/concepts/knowledge-commons-governance-multi-agent.md'"
warn_note "K345 Cybersec-primary — commons governance + measurement integrity; no PoCs; no public repo."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
