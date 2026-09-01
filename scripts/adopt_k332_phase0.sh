#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K332 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/vague-goal-self-evolution.md"
check "policy K332" grep -q "K332" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K332" grep -q "K332" "${REPO_ROOT}/.cursor/rules/ccc-k328-k332-phase1-wires.mdc"
check "no Aspire clone" test ! -d "${REPO_ROOT}/.local/adopts/Aspire"
check "no weights dir" bash -c "! test -d '${REPO_ROOT}/.local/adopts/Aspire-weights'"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/vague-goal-self-evolution.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md' '${REPO_ROOT}/wiki/concepts/vague-goal-self-evolution.md'"
warn_note "K332 ADOPT policy — vague-goal self-evolution ≠ explicit-task optimization. Agents complete train/harness-edit loops, but weight gains are sparse; strongest evolved harness stays below an engineered reference; proxy self-eval fails hidden eval; continued search can erase earlier gains. Pairs K162/K237/K292/K313. Never auto-evolve .cursor/skills. Project page only; no public SPDX → no clone. Runtime wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
