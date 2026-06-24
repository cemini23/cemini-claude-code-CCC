#!/usr/bin/env bash
# Sync /goal Cursor skill + rule to all Cemini federation workspaces.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_SKILL="${REPO_ROOT}/.cursor/skills/goal/SKILL.md"
SRC_RULE="${REPO_ROOT}/.cursor/rules/cemini-goal-skill.mdc"
USER_SKILL="${HOME}/.cursor/skills/goal/SKILL.md"
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

echo "Sync /goal skill from ${REPO_ROOT}"

copy_file() {
  local src="$1"
  local dest="$2"
  if [[ "${src}" -ef "${dest}" ]]; then
    return 0
  fi
  cp -f "${src}" "${dest}"
}

install_pair() {
  local dest="$1"
  local skill_dir="${dest}/.cursor/skills/goal"
  local rules_dir="${dest}/.cursor/rules"
  mkdir -p "${skill_dir}" "${rules_dir}"
  copy_file "${SRC_SKILL}" "${skill_dir}/SKILL.md"
  copy_file "${SRC_RULE}" "${rules_dir}/cemini-goal-skill.mdc"
}

mkdir -p "$(dirname "${USER_SKILL}")" "$(dirname "${USER_RULE}")"
cp "${SRC_SKILL}" "${USER_SKILL}"
cp "${SRC_RULE}" "${USER_RULE}"
echo "  OK  user-global ${USER_SKILL}"

count=0
for ws in "${WORKSPACES[@]}"; do
  if [[ ! -d "${ws}" ]]; then
    echo "  SKIP missing ${ws}"
    continue
  fi
  install_pair "${ws}"
  echo "  OK  ${ws}"
  count=$((count + 1))
done

echo ""
echo "Synced ${count} workspace(s) + user-global copy."
