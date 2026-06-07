#!/usr/bin/env bash
# K103 Phase-0 laptop adoptions — pydantic-ai (GO) + asm reference (CONDITIONAL-GO).
# Polymarket_data / pmxt live on OSINT scripts/adopt_k103_phase0.sh — not duplicated here.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k103-phase0-ccc}"
mkdir -p "${PHASE0}"

echo "K103 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"
echo "  phase0 dir: ${PHASE0}"

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

# 1. pydantic-ai — GO (MIT core)
if command -v pip3 >/dev/null 2>&1; then
  if python3 -c "import pydantic_ai" 2>/dev/null; then
    check "pydantic_ai import" true
  else
    echo "  INFO  installing pydantic-ai..."
    pip3 install --user -q "pydantic-ai" 2>/dev/null || pip3 install -q "pydantic-ai"
    if python3 -c "import pydantic_ai" 2>/dev/null; then
      check "pydantic_ai import after install" true
    else
      echo "  WARN  pydantic_ai import failed — check venv"
      warn=$((warn + 1))
    fi
  fi
else
  echo "  WARN  pip3 not on PATH"
  warn=$((warn + 1))
fi

if python3 -c "import pydantic_ai_gateway" 2>/dev/null; then
  echo "  WARN  pydantic_ai_gateway detected — AGPL companion; uninstall for prod hygiene"
  warn=$((warn + 1))
fi

# 2. asm — CONDITIONAL-GO (reference clone only)
ASM_DIR="${PHASE0}/asm"
if [[ ! -d "${ASM_DIR}/.git" ]]; then
  git clone --depth 1 https://github.com/luongnv89/asm.git "${ASM_DIR}"
fi
if [[ -f "${ASM_DIR}/package.json" || -f "${ASM_DIR}/README.md" ]]; then
  check "asm reference clone" true
else
  echo "  FAIL  asm clone incomplete"
  fail=$((fail + 1))
fi
echo "  INFO  asm at ${ASM_DIR} — do NOT symlink into ~/.claude/skills without isolated test dir"

# 3. skill-scanner optional
if command -v skill-scanner >/dev/null 2>&1 && [[ -d "${ASM_DIR}" ]]; then
  skill-scanner scan "${ASM_DIR}/" 2>/dev/null || true
  echo "  INFO  skill-scanner scan attempted on asm clone"
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn/info"
echo "OSINT full K103 script: OSINT WORKSPACE/scripts/adopt_k103_phase0.sh"
if [[ "${fail}" -gt 0 ]]; then
  exit 1
fi
