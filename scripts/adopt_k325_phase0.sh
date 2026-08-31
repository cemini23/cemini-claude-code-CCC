#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K325 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/bounded-authority-auditable-trajectories.md"
check "policy K325" grep -q "K325" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K325" grep -q "K325" "${REPO_ROOT}/.cursor/rules/ccc-k325-k327-phase1-wires.mdc"
check "no survey clone" bash -c "! ls -d '${REPO_ROOT}/.local/adopts/'* 2>/dev/null | grep -qi 'software.*systems.*secur\|slr\|security-agent'"
check "no exploit/PoC text" bash -c "! grep -rEi 'proof of concept|exploit code|jailbreak prompt|attack template' '${REPO_ROOT}/wiki/sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md' '${REPO_ROOT}/wiki/concepts/bounded-authority-auditable-trajectories.md'"
warn_note "K325 Cybersec-primary SLR — CCC steal = bounded authority + auditable trajectories gap; HITL on irreversible tools; eval = evidence tree not scalar (K289). wont_wire runtime. No 72-page dump in wiki."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
