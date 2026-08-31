#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K327 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-logos-cross-process-agent-harness-2608.28553.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/cross-process-plugin-agent-harness.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/logos-agent-harness.md"
check "policy K327" grep -q "K327" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K327" grep -q "K327" "${REPO_ROOT}/.cursor/rules/ccc-k325-k327-phase1-wires.mdc"
check "no Logos clone" test ! -d "${REPO_ROOT}/.local/adopts/Logos"
check "entity wired" grep -q "wire_status: wont_wire" "${REPO_ROOT}/wiki/entities/tools/logos-agent-harness.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-logos-cross-process-agent-harness-2608.28553.md' '${REPO_ROOT}/wiki/concepts/cross-process-plugin-agent-harness.md' '${REPO_ROOT}/wiki/entities/tools/logos-agent-harness.md'"
warn_note "K327 ADOPT policy — plugin=process, append-only transcript, resume without repeated effect at 4 tool-call boundaries. No public SPDX → policy only, no clone. Runtime wont_wire (do not replace Cursor//route). Pairs K282."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
