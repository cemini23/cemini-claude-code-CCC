#!/usr/bin/env bash
# Phase-0 checks for sst/opencode (coding agent) — NOT lidge-jun/opencodex.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIT="${OPENCODE_AUDIT:-/tmp/opencode-audit}"
echo "OpenCode Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/opencode.md"
check "name collision note" grep -q "opencodex" "${REPO_ROOT}/wiki/entities/tools/opencode.md"
if [[ -d "${AUDIT}/.git" ]]; then
  check "LICENSE MIT" grep -q "MIT License" "${AUDIT}/LICENSE"
  if du -sm "${AUDIT}" | awk '{exit !($1<500)}'; then echo "  PASS  clone <500MB"; pass=$((pass+1)); else echo "  FAIL  clone size"; fail=$((fail+1)); fi
else
  warn_note "no ${AUDIT} — re-clone --depth 1 --filter=blob:none https://github.com/sst/opencode.git"
fi
warn_note "NO-GO PATH and /route swap — keep claude-ds; curl|sh install forbidden"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
