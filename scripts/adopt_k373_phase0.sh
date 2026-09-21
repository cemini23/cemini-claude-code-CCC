#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K373 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-enterpriseval-enterprise-genai-evaluation-2609.21841.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/enterprise-use-case-genai-evaluation.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/enterprise-use-case-genai-evaluation.md"
check "policy K373" grep -q "K373" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K373" grep -q "K373" "${REPO_ROOT}/.cursor/rules/ccc-k373-k375-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/enterprise-use-case-genai-evaluation"
check "scale-gate skill" test -f "${REPO_ROOT}/.cursor/skills/enterprise-scale-gate/SKILL.md"
check "scale-gate helper" test -f "${REPO_ROOT}/scripts/enterprise_scale_gate.py"
check "scale-gate selftest" python3 "${REPO_ROOT}/scripts/enterprise_scale_gate.py" selftest
warn_note "K373 ADOPT eval-first"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
