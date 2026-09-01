#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K329 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/domain-grounded-tool-orchestration.md"
check "policy K329" grep -q "K329" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K329" grep -q "K329" "${REPO_ROOT}/.cursor/rules/ccc-k328-k332-phase1-wires.mdc"
check "no ParaView clone" test ! -d "${REPO_ROOT}/.local/adopts/ParaView"
check "no TTK clone" test ! -d "${REPO_ROOT}/.local/adopts/TTK"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/domain-grounded-tool-orchestration.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md' '${REPO_ROOT}/wiki/concepts/domain-grounded-tool-orchestration.md'"
warn_note "K329 ADOPT pattern — separate intent (LLM) / execution (deterministic domain tools) / explanation (LLM) over MCP; domain ontology constrains planning. Ontology does not change tool selection (already reliable) but raises result interpretation 0.41→0.91 when facts are scoped not bulk. Pairs K259/K272/K316. ParaView/TTK OOD wont_wire runtime. No clone."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
