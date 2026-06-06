#!/usr/bin/env bash
# K102 Phase-0 laptop adoptions — typst binary + harness/flowforge checks.
# Does not write to wiki/ or ~/.claude/ without explicit COPY_FLOWFORGE=1.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K102 Phase-0 adoption checks"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"
  shift
  if "$@"; then
    echo "  PASS  ${label}"
    pass=$((pass + 1))
  else
    echo "  FAIL  ${label}"
    fail=$((fail + 1))
  fi
}

warn_check() {
  local label="$1"
  shift
  if "$@"; then
    echo "  PASS  ${label}"
    pass=$((pass + 1))
  else
    echo "  WARN  ${label}"
    warn=$((warn + 1))
  fi
}

# 1. typst — optional PDF pipeline
if command -v typst >/dev/null 2>&1; then
  check "typst on PATH" typst --version
else
  echo "  INFO  typst not installed — run: brew install typst"
  warn=$((warn + 1))
fi

# 2. revfactory/harness — user-scope plugin (2026-06-04 trial)
if command -v claude >/dev/null 2>&1; then
  if claude plugin list 2>/dev/null | grep -qi harness; then
    check "harness plugin listed" true
  else
    echo "  INFO  harness plugin not listed — run: claude plugin install harness@harness-marketplace"
    warn=$((warn + 1))
  fi
else
  echo "  WARN  claude CLI not on PATH — skip harness plugin check"
  warn=$((warn + 1))
fi

if [[ -z "${CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS:-}" ]]; then
  echo "  INFO  export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 before first harness generation"
  warn=$((warn + 1))
else
  check "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS set" true
fi

# 3. flowforge-skill — optional copy
FLOWFORGE_REPO="${FLOWFORGE_REPO:-https://github.com/wentong2022-arch/flowforge-skill.git}"
FLOWFORGE_TMP="${FLOWFORGE_TMP:-/tmp/flowforge-skill-k102}"
if [[ "${COPY_FLOWFORGE:-}" == "1" ]]; then
  rm -rf "${FLOWFORGE_TMP}"
  git clone --depth 1 "${FLOWFORGE_REPO}" "${FLOWFORGE_TMP}"
  if command -v skill-scanner >/dev/null 2>&1; then
    skill-scanner scan "${FLOWFORGE_TMP}/" || true
  fi
  echo "  INFO  cloned to ${FLOWFORGE_TMP} — copy SKILL.md to ~/.claude/skills/ manually after review"
  pass=$((pass + 1))
else
  echo "  SKIP  flowforge clone (set COPY_FLOWFORGE=1 to clone + scan)"
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn/info"
if [[ "${fail}" -gt 0 ]]; then
  exit 1
fi
