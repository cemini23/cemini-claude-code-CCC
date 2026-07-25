#!/usr/bin/env bash
# Sync federation Cursor skills + /goal rule to all Cemini workspaces.
# Canon lives in CCC repo: .cursor/skills/{goal,to-issues,grill-with-docs,cursor-audit,super-audit}
# + cemini-goal-skill.mdc
#
# Domain skills (canon outside CCC):
#   adopted-geo-tools ← SEO wiki .cursor/skills/adopted-geo-tools (absolute SEO_ROOT paths)
#
# User-global ~/.cursor/skills + ~/.cursor/rules cover Home / empty windows.
# Per-workspace copies cover Open Folder sessions (project skills discovery).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Core operator skills (mattpocock + Cemini audits + task router)
CANON_SKILLS=(goal to-issues grill-with-docs cursor-audit super-audit route)
SRC_RULE="${REPO_ROOT}/.cursor/rules/cemini-goal-skill.mdc"
SRC_SEC_RULE="${REPO_ROOT}/.cursor/rules/cemini-cursor-security-preflight.mdc"
SRC_ROUTE_RULE="${REPO_ROOT}/.cursor/rules/cemini-route-outsource.mdc"
USER_RULE="${HOME}/.cursor/rules/cemini-goal-skill.mdc"
USER_SEC_RULE="${HOME}/.cursor/rules/cemini-cursor-security-preflight.mdc"
USER_ROUTE_RULE="${HOME}/.cursor/rules/cemini-route-outsource.mdc"

# Domain skills: name|absolute path to skill directory (must contain SKILL.md)
SEO_ROOT="/Users/claudiobarone/Projects/SEO:GEO B&M Business"
OSINT_ROOT="/Users/claudiobarone/Projects/OSINT WORKSPACE"
DOMAIN_SKILL_DIRS=(
  "adopted-geo-tools|${SEO_ROOT}/.cursor/skills/adopted-geo-tools"
  # K174 Extract — action-first ADHD output shaping (MIT); canon in OSINT
  "i-have-adhd|${OSINT_ROOT}/.cursor/skills/i-have-adhd"
)

# Prefer Projects/ canon paths; include Desktop aliases when present.
# tipdrop-* and pm-lp live under Desktop/projects or Projects.
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
  # Priority product + other live Open Folder roots
  "/Users/claudiobarone/Projects/atto"
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

# Copy entire skill directory (SKILL.md + reference/examples/scripts).
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
  # Prefer rsync when available (deletes stale extras); else recursive cp.
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

# Sync a domain skill whose canon lives outside CCC (e.g. SEO wiki).
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
    # Historical filename still present in some agent contexts
    copy_file "${SRC_ROUTE_RULE}" "${rules_dir}/tipdrop-route-outsource.mdc"
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
  local entry name
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
  # multi-file skills must carry companions
  [[ -f "${dest}/.cursor/skills/cursor-audit/reference.md" ]] || ok=1
  [[ -f "${dest}/.cursor/skills/super-audit/prompt-template.md" ]] || ok=1
  return "${ok}"
}

echo "Sync federation Cursor skills from ${REPO_ROOT}"
echo "  CCC skills: ${CANON_SKILLS[*]}"
echo "  Domain skills: adopted-geo-tools (SEO) + i-have-adhd (OSINT K174)"

# User-global copies (Cursor discovers ~/.cursor/skills/* in any window, including Home)
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
echo "Synced ${count} workspace(s) + user-global (${#CANON_SKILLS[@]} CCC + ${#DOMAIN_SKILL_DIRS[@]} domain + goal/security rules); ${skip} path(s) skipped (missing)."
echo "Optional: cursor-security-preflight --quick   # scan all .cursor trees after sync"
