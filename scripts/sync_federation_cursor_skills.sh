#!/usr/bin/env bash
# Sync federation Cursor skills + /goal rule to all Cemini workspaces.
# Canon lives in CCC repo: .cursor/skills/{goal,to-issues,grill-with-docs} + cemini-goal-skill.mdc
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CANON_SKILLS=(goal to-issues grill-with-docs)
SRC_RULE="${REPO_ROOT}/.cursor/rules/cemini-goal-skill.mdc"
USER_RULE="${HOME}/.cursor/rules/cemini-goal-skill.mdc"

WORKSPACES=(
  "${REPO_ROOT}"
  "/Users/claudiobarone/Projects/OSINT WORKSPACE"
  "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
  "/Users/claudiobarone/Projects/Gambling wiki"
  "/Users/claudiobarone/Projects/Game Dev wiki"
  "/Users/claudiobarone/Desktop/projects/Game Dev wiki"
  "/Users/claudiobarone/Projects/Cybersecurity wiki"
  "/Users/claudiobarone/Projects/Image gen"
  "/Users/claudiobarone/Projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Projects/3D printing"
  "/Users/claudiobarone/Projects/CeminiSuite"
  "/Users/claudiobarone/Projects/cemini-federation-hub"
  "/Users/claudiobarone/Projects/castle-sim"
  "/Users/claudiobarone/Projects/CeminiDFS"
  "/Users/claudiobarone/Projects/world-cup-bot"
  "/Users/claudiobarone/Projects/wc-ticket-monitor"
  "/Users/claudiobarone/Projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Projects/agent-toolkit-demo"
)

copy_file() {
  local src="$1"
  local dest="$2"
  if [[ "${src}" -ef "${dest}" ]]; then
    return 0
  fi
  cp -f "${src}" "${dest}"
}

install_workspace() {
  local dest="$1"
  local rules_dir="${dest}/.cursor/rules"
  mkdir -p "${rules_dir}"
  copy_file "${SRC_RULE}" "${rules_dir}/cemini-goal-skill.mdc"
  for skill in "${CANON_SKILLS[@]}"; do
    local src_skill="${REPO_ROOT}/.cursor/skills/${skill}/SKILL.md"
    if [[ ! -f "${src_skill}" ]]; then
      echo "  FAIL missing canon ${src_skill}" >&2
      return 1
    fi
    local skill_dir="${dest}/.cursor/skills/${skill}"
    mkdir -p "${skill_dir}"
    copy_file "${src_skill}" "${skill_dir}/SKILL.md"
  done
}

verify_workspace() {
  local dest="$1"
  local ok=0
  for skill in "${CANON_SKILLS[@]}"; do
    [[ -f "${dest}/.cursor/skills/${skill}/SKILL.md" ]] || ok=1
  done
  [[ -f "${dest}/.cursor/rules/cemini-goal-skill.mdc" ]] || ok=1
  return "${ok}"
}

echo "Sync federation Cursor skills from ${REPO_ROOT}"
echo "  skills: ${CANON_SKILLS[*]}"

# User-global copies (Cursor discovers ~/.cursor/skills/* in any window)
for skill in "${CANON_SKILLS[@]}"; do
  src_skill="${REPO_ROOT}/.cursor/skills/${skill}/SKILL.md"
  user_skill="${HOME}/.cursor/skills/${skill}/SKILL.md"
  mkdir -p "$(dirname "${user_skill}")"
  copy_file "${src_skill}" "${user_skill}"
  echo "  OK  user-global ${user_skill}"
done
mkdir -p "$(dirname "${USER_RULE}")"
copy_file "${SRC_RULE}" "${USER_RULE}"
echo "  OK  user-global ${USER_RULE}"

count=0
fail=0
for ws in "${WORKSPACES[@]}"; do
  if [[ ! -d "${ws}" ]]; then
    echo "  SKIP missing ${ws}"
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
  echo "Synced ${count} workspace(s); ${fail} verify failure(s)." >&2
  exit 1
fi
echo "Synced ${count} workspace(s) + user-global (${#CANON_SKILLS[@]} skills + goal rule)."
