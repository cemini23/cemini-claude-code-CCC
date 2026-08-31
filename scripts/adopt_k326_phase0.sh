#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K326 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-recognition-without-enforcement-2608.28502.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/recognition-vs-enforcement-instruction-arbitration.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/patterns/external-reference-monitor.md"
check "policy K326" grep -q "K326" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K326" grep -q "K326" "${REPO_ROOT}/.cursor/rules/ccc-k325-k327-phase1-wires.mdc"
check "no InstructionArbitrationBench clone" test ! -d "${REPO_ROOT}/.local/adopts/InstructionArbitrationBench"
check "entity wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/entities/patterns/external-reference-monitor.md"
check "no attack prompts/PoCs" bash -c "! grep -rEi 'system override|fabricated priority|delete all files|ignore previous instructions|jailbreak suffix|\[SYSTEM' '${REPO_ROOT}/wiki/sources/arxiv-recognition-without-enforcement-2608.28502.md' '${REPO_ROOT}/wiki/concepts/recognition-vs-enforcement-instruction-arbitration.md' '${REPO_ROOT}/wiki/entities/patterns/external-reference-monitor.md'"
warn_note "K326 ADOPT policy — recognition ≠ enforcement; external reference monitor (authenticated source routing + capability-gated tools). Zero attack text. Do not clone forthcoming bench until SPDX. Cybersec steal. Pairs K285/K310/K312."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
