#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K357 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-artificial-id-persistent-alignment-2609.11911.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/artificial-id-persistent-agent-drive.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/artificial-id-persistent-agent-drive.md"
check "policy K357" grep -q "K357" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K357" grep -q "K357" "${REPO_ROOT}/.cursor/rules/ccc-k346-k357-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/artificial-id-persistent-agent-drive"
warn_note "K357 ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
