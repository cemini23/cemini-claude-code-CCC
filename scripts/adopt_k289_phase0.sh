#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K289 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/agentified-eval-evidence-tree-harness.md"
check "entity harnesseval-w" test -f "${REPO_ROOT}/wiki/entities/tools/harnesseval-w.md"
check "policy K289" grep -q "K289" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" bash -c '! test -d "${REPO_ROOT}/.local/adopts/harnesseval-w"'
warn_note "K289 HarnessEval-W agentified eval — null SPDX (no LICENSE in pyproject) NO-GO clone; policy_wired. Pairs K162 verification hierarchy, K277 measurement integrity."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
