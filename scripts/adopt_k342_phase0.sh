#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K342 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-hierarchical-spm-agentic-orchestration-2609.04015.md"
check "no concept" test ! -f "${REPO_ROOT}/wiki/concepts/hierarchical-spm-automation.md"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/SPM-automation"
warn_note "K342 OOD microscopy lab automation — source stub; wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
