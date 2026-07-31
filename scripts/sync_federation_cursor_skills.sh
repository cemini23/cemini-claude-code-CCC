#!/usr/bin/env bash
# Sync federation Cursor skills + shared rules to all Cemini workspaces.
#
# Canon: CCC `.cursor/skills/<name>/SKILL.md` with frontmatter `federation: true`
# Domain skills (canon outside CCC): DOMAIN_SKILL_DIRS below.
#
# Auto-discovers federation skills — add a new cross-project skill by putting
# `federation: true` in its SKILL.md frontmatter (no hard-coded list edit required).
#
# User-global ~/.cursor/skills + ~/.cursor/rules cover Home / empty windows.
# Per-workspace copies cover Open Folder sessions.
#
# Autosync: CCC `scripts/post-commit.sh` runs this when skills/rules change.
# Manual: bash scripts/sync_federation_cursor_skills.sh
#         ~/bin/sync-federation-cursor-skills
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_RULE="${REPO_ROOT}/.cursor/rules/cemini-goal-skill.mdc"
SRC_SEC_RULE="${REPO_ROOT}/.cursor/rules/cemini-cursor-security-preflight.mdc"
SRC_ROUTE_RULE="${REPO_ROOT}/.cursor/rules/cemini-route-outsource.mdc"
SRC_PHASE1_RULE="${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
USER_RULE="${HOME}/.cursor/rules/cemini-goal-skill.mdc"
USER_SEC_RULE="${HOME}/.cursor/rules/cemini-cursor-security-preflight.mdc"
USER_ROUTE_RULE="${HOME}/.cursor/rules/cemini-route-outsource.mdc"
USER_PHASE1_RULE="${HOME}/.cursor/rules/cemini-phase1-policy-wires.mdc"

# Discover CCC skills marked federation: true (YAML frontmatter).
discover_federation_skills() {
  local skill_md name
  CANON_SKILLS=()
  shopt -s nullglob
  for skill_md in "${REPO_ROOT}/.cursor/skills"/*/SKILL.md; do
    if awk '
      BEGIN { in_fm=0; found=0 }
      /^---[[:space:]]*$/ {
        if (in_fm==0) { in_fm=1; next }
        else { exit }
      }
      in_fm && /^federation:[[:space:]]*true[[:space:]]*$/ { found=1; exit }
      END { exit found ? 0 : 1 }
    ' "${skill_md}"; then
      name="$(basename "$(dirname "${skill_md}")")"
      # Domain skills synced separately — skip if listed in DOMAIN_SKILL_DIRS
      case "${name}" in
        adopted-geo-tools|i-have-adhd) continue ;;
      esac
      CANON_SKILLS+=("${name}")
    fi
  done
  shopt -u nullglob
  if [[ ${#CANON_SKILLS[@]} -eq 0 ]]; then
    echo "FAIL: no skills with federation: true under ${REPO_ROOT}/.cursor/skills" >&2
    exit 1
  fi
  # Stable order
  IFS=$'\n' CANON_SKILLS=($(printf '%s\n' "${CANON_SKILLS[@]}" | sort -u))
  unset IFS
}

# Domain skills: name|absolute path to skill directory (must contain SKILL.md)
SEO_ROOT="/Users/claudiobarone/Projects/SEO:GEO B&M Business"
OSINT_ROOT="/Users/claudiobarone/Projects/OSINT WORKSPACE"
DOMAIN_SKILL_DIRS=(
  "adopted-geo-tools|${SEO_ROOT}/.cursor/skills/adopted-geo-tools"
  "i-have-adhd|${OSINT_ROOT}/.cursor/skills/i-have-adhd"
)

WORKSPACES=(
  "${REPO_ROOT}"
  "/Users/claudiobarone/Projects/OSINT WORKSPACE"
  "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
  "/Users/claudiobarone/Projects/Gambling wiki"
  "/Users/claudiobarone/Desktop/projects/Gambling wiki"
  "/Users/claudiobarone/Projects/Game Dev wiki"
  "/Users/claudiobarone/Desktop/projects/Game Dev wiki"
  "/Users/claudiobarone/Projects/Cybersecurity wiki"
  "/Users/claudiobarone/Desktop/projects/Cybersecurity wiki"
  "/Users/claudiobarone/Projects/Image gen"
  "/Users/claudiobarone/Desktop/projects/Image gen"
  "/Users/claudiobarone/Projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Projects/3D printing"
  "/Users/claudiobarone/Desktop/projects/3D printing"
  "/Users/claudiobarone/Projects/CeminiSuite"
  "/Users/claudiobarone/Desktop/projects/CeminiSuite"
  "/Users/claudiobarone/Projects/cemini-federation-hub"
  "/Users/claudiobarone/Desktop/projects/cemini-federation-hub"
  "/Users/claudiobarone/Projects/castle-sim"
  "/Users/claudiobarone/Desktop/projects/castle-sim"
  "/Users/claudiobarone/Projects/CeminiDFS"
  "/Users/claudiobarone/Desktop/projects/CeminiDFS"
  "/Users/claudiobarone/Projects/world-cup-bot"
  "/Users/claudiobarone/Desktop/projects/world-cup-bot"
  "/Users/claudiobarone/Projects/wc-ticket-monitor"
  "/Users/claudiobarone/Desktop/projects/wc-ticket-monitor"
  "/Users/claudiobarone/Projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Desktop/projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Projects/agent-toolkit-demo"
  "/Users/claudiobarone/Desktop/projects/agent-toolkit-demo"
  "/Users/claudiobarone/Desktop/projects/tipdrop-workspace-kit"
  "/Users/claudiobarone/Projects/tipdrop-workspace-kit"
  "/Users/claudiobarone/Desktop/projects/tipdrop-scanner"
  "/Users/claudiobarone/Projects/tipdrop-scanner"
  "/Users/claudiobarone/Desktop/tipdrop-scanner"
  "/Users/claudiobarone/Projects/pm-lp-canary-wiki"
  "/Users/claudiobarone/Desktop/projects/pm-lp-canary-wiki"
  "/Users/claudiobarone/Projects/atto"
  "/Users/claudiobarone/Projects/GuruWatcher"
  "/Users/claudiobarone/Projects/easy review"
  "/Users/claudiobarone/Projects/ARIS"
  "/Users/claudiobarone/Projects/QuantOS_Private"
  "/Users/claudiobarone/Projects/ara-schema"
  "/Users/claudiobarone/Projects/wikilint"
  "/Users/claudiobarone/Projects/vet"
)

copy_file() {
  local src="$1"
  local dest="$2"
  if [[ "${src}" -ef "${dest}" ]]; then
    return 0
  fi
  mkdir -p "$(dirname "${dest}")"
  cp -f "${src}" "${dest}"
}

sync_skill_tree() {
  local skill="$1"
  local dest_root="$2"
  local src_dir="${REPO_ROOT}/.cursor/skills/${skill}"
  local dest_dir="${dest_root}/.cursor/skills/${skill}"
  if [[ ! -f "${src_dir}/SKILL.md" ]]; then
    echo "  FAIL missing canon ${src_dir}/SKILL.md" >&2
    return 1
  fi
  mkdir -p "${dest_dir}"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete \
      --exclude '.DS_Store' \
      --exclude 'upstream' \
      "${src_dir}/" "${dest_dir}/"
  else
    rm -rf "${dest_dir}"
    mkdir -p "${dest_dir}"
    cp -R "${src_dir}/." "${dest_dir}/"
    rm -rf "${dest_dir}/upstream"
  fi
}

sync_domain_skill_tree() {
  local skill="$1"
  local src_dir="$2"
  local dest_root="$3"
  local dest_dir="${dest_root}/.cursor/skills/${skill}"
  if [[ ! -f "${src_dir}/SKILL.md" ]]; then
    echo "  FAIL missing domain canon ${src_dir}/SKILL.md" >&2
    return 1
  fi
  mkdir -p "${dest_dir}"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete \
      --exclude '.DS_Store' \
      --exclude 'upstream' \
      "${src_dir}/" "${dest_dir}/"
  else
    rm -rf "${dest_dir}"
    mkdir -p "${dest_dir}"
    cp -R "${src_dir}/." "${dest_dir}/"
    rm -rf "${dest_dir}/upstream"
  fi
}

install_workspace() {
  local dest="$1"
  local rules_dir="${dest}/.cursor/rules"
  local entry name src_dir
  mkdir -p "${rules_dir}"
  copy_file "${SRC_RULE}" "${rules_dir}/cemini-goal-skill.mdc"
  if [[ -f "${SRC_SEC_RULE}" ]]; then
    copy_file "${SRC_SEC_RULE}" "${rules_dir}/cemini-cursor-security-preflight.mdc"
  fi
  if [[ -f "${SRC_ROUTE_RULE}" ]]; then
    copy_file "${SRC_ROUTE_RULE}" "${rules_dir}/cemini-route-outsource.mdc"
    copy_file "${SRC_ROUTE_RULE}" "${rules_dir}/tipdrop-route-outsource.mdc"
  fi
  if [[ -f "${SRC_PHASE1_RULE}" ]]; then
    copy_file "${SRC_PHASE1_RULE}" "${rules_dir}/cemini-phase1-policy-wires.mdc"
  fi
  for skill in "${CANON_SKILLS[@]}"; do
    sync_skill_tree "${skill}" "${dest}"
  done
  for entry in "${DOMAIN_SKILL_DIRS[@]}"; do
    name="${entry%%|*}"
    src_dir="${entry#*|}"
    sync_domain_skill_tree "${name}" "${src_dir}" "${dest}"
  done
}

verify_workspace() {
  local dest="$1"
  local ok=0
  local entry name skill
  for skill in "${CANON_SKILLS[@]}"; do
    [[ -f "${dest}/.cursor/skills/${skill}/SKILL.md" ]] || ok=1
  done
  for entry in "${DOMAIN_SKILL_DIRS[@]}"; do
    name="${entry%%|*}"
    [[ -f "${dest}/.cursor/skills/${name}/SKILL.md" ]] || ok=1
  done
  [[ -f "${dest}/.cursor/rules/cemini-goal-skill.mdc" ]] || ok=1
  [[ -f "${dest}/.cursor/rules/cemini-cursor-security-preflight.mdc" ]] || ok=1
  [[ -f "${dest}/.cursor/rules/cemini-route-outsource.mdc" ]] || ok=1
  [[ -f "${dest}/.cursor/skills/route/SKILL.md" ]] || ok=1
  [[ -f "${dest}/.cursor/skills/phase1-wire/SKILL.md" ]] || ok=1
  if [[ -f "${SRC_PHASE1_RULE}" ]]; then
    [[ -f "${dest}/.cursor/rules/cemini-phase1-policy-wires.mdc" ]] || ok=1
  fi
  if [[ -f "${dest}/.cursor/skills/cursor-audit/SKILL.md" ]]; then
    [[ -f "${dest}/.cursor/skills/cursor-audit/reference.md" ]] || ok=1
  fi
  if [[ -f "${dest}/.cursor/skills/super-audit/SKILL.md" ]]; then
    [[ -f "${dest}/.cursor/skills/super-audit/prompt-template.md" ]] || ok=1
  fi
  return "${ok}"
}

discover_federation_skills

echo "Sync federation Cursor skills from ${REPO_ROOT}"
echo "  Federation skills (auto): ${CANON_SKILLS[*]}"
echo "  Domain skills: adopted-geo-tools (SEO) + i-have-adhd (OSINT K174)"

for skill in "${CANON_SKILLS[@]}"; do
  sync_skill_tree "${skill}" "${HOME}"
  echo "  OK  user-global ~/.cursor/skills/${skill}/"
done
for entry in "${DOMAIN_SKILL_DIRS[@]}"; do
  name="${entry%%|*}"
  src_dir="${entry#*|}"
  sync_domain_skill_tree "${name}" "${src_dir}" "${HOME}"
  echo "  OK  user-global ~/.cursor/skills/${name}/"
done
mkdir -p "$(dirname "${USER_RULE}")"
copy_file "${SRC_RULE}" "${USER_RULE}"
echo "  OK  user-global ${USER_RULE}"
if [[ -f "${SRC_SEC_RULE}" ]]; then
  copy_file "${SRC_SEC_RULE}" "${USER_SEC_RULE}"
  echo "  OK  user-global ${USER_SEC_RULE}"
fi
if [[ -f "${SRC_ROUTE_RULE}" ]]; then
  copy_file "${SRC_ROUTE_RULE}" "${USER_ROUTE_RULE}"
  copy_file "${SRC_ROUTE_RULE}" "${HOME}/.cursor/rules/tipdrop-route-outsource.mdc"
  echo "  OK  user-global ${USER_ROUTE_RULE}"
fi
if [[ -f "${SRC_PHASE1_RULE}" ]]; then
  copy_file "${SRC_PHASE1_RULE}" "${USER_PHASE1_RULE}"
  echo "  OK  user-global ${USER_PHASE1_RULE}"
fi

count=0
fail=0
skip=0
for ws in "${WORKSPACES[@]}"; do
  if [[ ! -d "${ws}" ]]; then
    echo "  SKIP missing ${ws}"
    skip=$((skip + 1))
    continue
  fi
  install_workspace "${ws}"
  if verify_workspace "${ws}"; then
    echo "  OK  ${ws}"
    count=$((count + 1))
  else
    echo "  FAIL verify ${ws}" >&2
    fail=$((fail + 1))
  fi
done

echo ""
if [[ "${fail}" -gt 0 ]]; then
  echo "Synced ${count} workspace(s); ${fail} verify failure(s); ${skip} skipped." >&2
  exit 1
fi
echo "Synced ${count} workspace(s) + user-global (${#CANON_SKILLS[@]} federation + ${#DOMAIN_SKILL_DIRS[@]} domain + shared rules); ${skip} path(s) skipped (missing)."
echo "Optional: cursor-security-preflight --quick"
