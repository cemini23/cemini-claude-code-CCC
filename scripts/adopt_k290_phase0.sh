#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K290 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-task-conditioned-least-privilege-learning-2608.18351.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/task-conditioned-least-privilege-agent-learning.md"
check "pattern" test -f "${REPO_ROOT}/wiki/entities/patterns/task-conditioned-least-privilege-envelope.md"
check "policy K290" grep -q "K290" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "phase1 rule" test -f "${REPO_ROOT}/.cursor/rules/ccc-k290-k294-phase1-wires.mdc"
warn_note "K290 least-privilege learning — no public SPDX clone; policy only. Atto-priority (pairs K285 Mandato)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
