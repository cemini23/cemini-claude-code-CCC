#!/usr/bin/env bash
# K126 Phase-0 — mattpocock/skills (MIT) transplant; nvidia/skills reference only.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k126-phase0-ccc}"
MP="${PHASE0}/mattpocock-skills"
CCC_SKILLS="${REPO_ROOT}/.cursor/skills"

echo "K126 Phase-0 adoption checks (CCC)"
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

warn_note() {
  echo "  WARN  $1"
  warn=$((warn + 1))
}

if [[ ! -d "${MP}/.git" ]]; then
  git clone --depth 1 https://github.com/mattpocock/skills.git "${MP}"
fi

check "mattpocock/skills clone" test -d "${MP}/.git"

if command -v gh >/dev/null 2>&1; then
  mp_lic="$(gh api repos/mattpocock/skills --jq '.license.spdx_id' 2>/dev/null || echo "")"
  [[ "${mp_lic}" == "MIT" ]] && check "mattpocock/skills MIT license" true || warn_note "mattpocock license: ${mp_lic:-none}"

  nv_lic="$(gh api repos/NVIDIA/skills --jq '.license.spdx_id' 2>/dev/null || echo "")"
  warn_note "NVIDIA/skills license field: ${nv_lic:-none} — dual Apache-2.0 + CC-BY-4.0 per OSINT eval; SkillSpector gate only"
fi

for sk in to-issues grill-with-docs; do
  if [[ -f "${CCC_SKILLS}/${sk}/SKILL.md" ]]; then
    check "${sk} installed in .cursor/skills" true
  else
    warn_note "${sk} missing — run: cp -R ${MP}/skills/engineering/${sk} ${CCC_SKILLS}/${sk}"
  fi
done

warn_note "grill-me in briefs maps to grill-with-docs in mattpocock repo (2026-06-22)"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
