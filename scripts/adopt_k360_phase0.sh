#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K360 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-emergence-world-multi-agent-stress-test-2609.17320.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/long-horizon-multi-agent-adversarial-eval.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/long-horizon-multi-agent-adversarial-eval.md"
check "policy K360" grep -q "K360" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K360" grep -q "K360" "${REPO_ROOT}/.cursor/rules/ccc-k358-k362-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/long-horizon-multi-agent-adversarial-eval"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-emergence-world-multi-agent-stress-test-2609.17320.md' '${REPO_ROOT}/wiki/concepts/long-horizon-multi-agent-adversarial-eval.md'"
warn_note "K360 Cybersec-primary + ADOPT eval"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
