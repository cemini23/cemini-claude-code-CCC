#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K324 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-redevoagent-redteam-skill-evo-2608.27439.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/validation-ratchet-skill-evolution.md"
check "policy K324" grep -q "K324" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K324" grep -q "K324" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no RedEvoAgent clone" test ! -d "${REPO_ROOT}/.local/adopts/RedEvoAgent"
check "no attack/PoC text" bash -c "! grep -rEi 'jailbreak|exploit' '${REPO_ROOT}/wiki/sources/arxiv-redevoagent-redteam-skill-evo-2608.27439.md' '${REPO_ROOT}/wiki/concepts/validation-ratchet-skill-evolution.md'"
warn_note "K324 Cybersec-primary — CCC steal is validation ratchet only; no attack-skill clone; wont_wire runtime; dual-ID same-day Cybersec PDF."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
