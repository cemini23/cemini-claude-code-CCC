#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K330 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-castclaw-hitl-forecasting-agent-2608.30976.md"
check "policy K330" grep -q "K330" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K330" grep -q "K330" "${REPO_ROOT}/.cursor/rules/ccc-k328-k332-phase1-wires.mdc"
check "no CastClaw clone" test ! -d "${REPO_ROOT}/.local/adopts/CastClaw"
check "no GW rule invented" bash -c "! test -f '${REPO_ROOT}/.cursor/rules/guruwatcher-k330-castclaw-phase1-wires.mdc'"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-castclaw-hitl-forecasting-agent-2608.30976.md'"
warn_note "K330 OOD — TSF demo (4 pages). Steal: leave numerics to specialist forecasters; revision replaces the active forecast only after validation + hard constraints; HITL cannot bypass those gates; versioned execution record. GuruWatcher alert-only — no TSF runtime. Short source stub. wont_wire. No clone."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
