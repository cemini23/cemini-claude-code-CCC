#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K275 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/multi-hop-api-retrieval-eval-tool-policies.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/vakra.md"
check "policy K275" grep -q "K275" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" test ! -d "${REPO_ROOT}/.local/adopts/vakra"
warn_note "K275 VAKRA CC-BY-NC-SA 4.0 — NO-GO clone; eval axes ADOPT, HF dataset WATCH only"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
