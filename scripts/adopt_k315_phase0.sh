#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K315 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-toolminimize-privacy-args-2608.24957.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/tool-argument-privacy-minimization.md"
check "policy K315" grep -q "K315" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K315" grep -q "K315" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no ToolMinimize clone" test ! -d "${REPO_ROOT}/.local/adopts/ToolMinimize"
check "no PII/PoC text" bash -c "! grep -rEi 'sloan kettering|alcoholics anonymous' '${REPO_ROOT}/wiki/sources/arxiv-toolminimize-privacy-args-2608.24957.md' '${REPO_ROOT}/wiki/concepts/tool-argument-privacy-minimization.md'"
warn_note "K315 ADOPT policy — rewrite args (remove/generalize/substitute/truncate), not only allow/block. No public SPDX. Cybersec steal. No PII/PoC dumps."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
