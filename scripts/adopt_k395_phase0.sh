#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K395 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-approval-laundering-2609.28586.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/agent-approval-laundering-transitive-effects.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/agent-approval-laundering-transitive-effects.md"
check "policy K395" grep -q "K395" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K395" grep -q "K395" "${REPO_ROOT}/.cursor/rules/ccc-k395-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/agent-approval-laundering-transitive-effects"
warn_note "K395 Cybersec-primary ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
