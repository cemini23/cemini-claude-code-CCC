#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K362 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentic-societies-social-harness-2609.17527.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/social-harness-multi-agent-trust.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/social-harness-multi-agent-trust.md"
check "policy K362" grep -q "K362" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K362" grep -q "K362" "${REPO_ROOT}/.cursor/rules/ccc-k358-k362-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/social-harness-multi-agent-trust"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-agentic-societies-social-harness-2609.17527.md' '${REPO_ROOT}/wiki/concepts/social-harness-multi-agent-trust.md'"
warn_note "K362 Cybersec-primary + ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
