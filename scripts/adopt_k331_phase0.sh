#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K331 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-autoscirub-rubric-induction-2608.31076.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/evaluation-first-rubric-induction.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/autoscirub.md"
check "policy K331" grep -q "K331" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K331" grep -q "K331" "${REPO_ROOT}/.cursor/rules/ccc-k328-k332-phase1-wires.mdc"
check "clone LICENSE" test -f "${REPO_ROOT}/.local/adopts/AutoSciRub/LICENSE"
check "clone size" bash -c "du -sm '${REPO_ROOT}/.local/adopts/AutoSciRub' | awk '\$1 < 500'"
check "entity wired" grep -q "wire_status: wont_wire" "${REPO_ROOT}/wiki/entities/tools/autoscirub.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-autoscirub-rubric-induction-2608.31076.md' '${REPO_ROOT}/wiki/concepts/evaluation-first-rubric-induction.md' '${REPO_ROOT}/wiki/entities/tools/autoscirub.md'"
warn_note "K331 ADOPT eval-first — induce a task-specific executable rubric before research execution; use it to guide, verify, and revise. Gains transfer across harnesses with frozen backbone. Pairs K162/K281/K289/K298 — do not rewrite ## Verify. zjunlp/AutoSciRub MIT (gh SPDX) ~2.5MB → GO REFERENCE .local/adopts/AutoSciRub. Runtime wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
