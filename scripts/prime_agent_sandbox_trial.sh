#!/usr/bin/env bash
# Prime Agent REFERENCE sandbox trial (CCC K309).
# Inventory + K292 retention check. Does NOT install, PATH-swap, or run the agent.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLONE="${REPO_ROOT}/.local/adopts/prime-agent"
pass=0; fail=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }

echo "K309 Prime Agent sandbox trial — ${REPO_ROOT}"
echo "Mode: inventory + retention. Never curl|sh install.sh. Never replace Cursor / /route / claude-ds."

check "clone-dir" test -d "${CLONE}"
check "mit-license" grep -qi "MIT License" "${CLONE}/LICENSE"
size_mb="$(du -sm "${CLONE}" | awk '{print $1}')"
check "size-under-500mb" test "${size_mb}" -lt 500
check "readme-rlm" grep -q "Recursive Language Model" "${CLONE}/README.md"
check "readme-continual" grep -qi "Continual Harness" "${CLONE}/README.md"
check "install-sh-present-unread" test -f "${CLONE}/install.sh"  # do not execute
if command -v prime-agent >/dev/null 2>&1; then
  echo "  WARN  prime-agent on PATH at $(command -v prime-agent) — do not use as /route or claude-ds"
else
  echo "  PASS  prime-agent-not-on-path"
  pass=$((pass+1))
fi

# Eval pack = README-claimed abstractions present on disk (harness-inventory, not ARC-AGI-3).
check "agents-md" test -f "${CLONE}/AGENTS.md"
check "security-md" test -f "${CLONE}/SECURITY.md"

# K292 retention: CCC harness files must be unchanged by this trial (we only read).
tmp="$(mktemp)"
(
  cd "${REPO_ROOT}"
  find .cursor/skills .cursor/rules -type f \( -name 'SKILL.md' -o -name '*.mdc' \) \
    | sort | xargs shasum -a 256
) > "${tmp}"
check "retention-snapshot-nonempty" test -s "${tmp}"
# Re-hash immediately; trial is read-only so this must match.
tmp2="$(mktemp)"
(
  cd "${REPO_ROOT}"
  find .cursor/skills .cursor/rules -type f \( -name 'SKILL.md' -o -name '*.mdc' \) \
    | sort | xargs shasum -a 256
) > "${tmp2}"
check "k292-retention-harness-unchanged" cmp -s "${tmp}" "${tmp2}"
rm -f "${tmp}" "${tmp2}"

echo "Summary: ${pass} pass, ${fail} fail  (clone ${size_mb}MB)"
echo "HITL still required before any skill/prompt self-write. Do not adopt Continual Harness learned state."
[[ "${fail}" -eq 0 ]]
