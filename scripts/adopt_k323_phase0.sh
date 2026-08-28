#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="${REPO_ROOT}/.local/adopts/intent-as-a-tool"
echo "K323 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/intent-as-a-tool-misalignment-signal.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/intent-as-a-tool.md"
check "policy K323" grep -q "K323" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K323" grep -q "K323" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
if [ -d "${ADOPT}" ]; then
  check "clone exists" test -d "${ADOPT}"
  check "LICENSE on disk" grep -qi "MIT License" "${ADOPT}/LICENSE"
  sz="$(du -sm "${ADOPT}" | cut -f1)"; if [ "${sz}" -lt 500 ]; then echo "  PASS  clone size ${sz}MB <500MB"; pass=$((pass+1)); else echo "  FAIL  clone size ${sz}MB >=500MB"; fail=$((fail+1)); fi
else
  warn_note "intent-as-a-tool clone absent — expected MIT GO REFERENCE at .local/adopts/intent-as-a-tool"
fi
check "no attack/PoC text" bash -c "! grep -rEi 'blackmail|jailbreak' '${REPO_ROOT}/wiki/sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md' '${REPO_ROOT}/wiki/concepts/intent-as-a-tool-misalignment-signal.md'"
warn_note "K323 ADOPT policy — intent-targeted tools = judge-free commitment signal; runtime wont_wire; no attack writeups."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
