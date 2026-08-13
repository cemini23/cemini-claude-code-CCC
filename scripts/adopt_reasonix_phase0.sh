#!/usr/bin/env bash
# Phase-0 checks for esengine/DeepSeek-Reasonix (community, not first-party DeepSeek).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIT="${REASONIX_AUDIT:-/tmp/reasonix-audit}"
echo "Reasonix Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/reasonix.md"
check "not first-party" grep -q "Not first-party" "${REPO_ROOT}/wiki/entities/tools/reasonix.md"
if [[ -d "${AUDIT}/.git" ]]; then
  check "LICENSE MIT" grep -q "MIT License" "${AUDIT}/LICENSE"
  if du -sm "${AUDIT}" | awk '{exit !($1<200)}'; then echo "  PASS  clone <200MB"; pass=$((pass+1)); else echo "  FAIL  clone size"; fail=$((fail+1)); fi
else
  warn_note "no ${AUDIT} — re-clone --depth 1 https://github.com/esengine/DeepSeek-Reasonix.git"
fi
warn_note "NO-GO PATH and /route swap — keep claude-ds; do not npm i -g reasonix"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
