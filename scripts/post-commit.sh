#!/usr/bin/env bash
# CCC post-commit: autosync federation Cursor skills when canon changes.
# Installed via scripts/install-hooks.sh → .git/hooks/post-commit
#
# IMPORTANT: resolve via git toplevel — $0 under .git/hooks is a symlink and
# dirname("$0")/.. points at .git/, not the repo root.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "${REPO_ROOT}" ]]; then
  # Fallback: follow symlink to scripts/post-commit.sh → repo root
  self="${BASH_SOURCE[0]:-$0}"
  while [[ -L "${self}" ]]; do
    dir="$(cd -P "$(dirname "${self}")" && pwd)"
    self="$(readlink "${self}")"
    [[ "${self}" != /* ]] && self="${dir}/${self}"
  done
  REPO_ROOT="$(cd "$(dirname "${self}")/.." && pwd)"
fi

SYNC="${REPO_ROOT}/scripts/sync_federation_cursor_skills.sh"

# Only sync when this commit touched federation skill/rule surfaces
changed="$(git -C "${REPO_ROOT}" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null || true)"
if [[ -z "${changed}" ]]; then
  exit 0
fi

need_sync=0
while IFS= read -r path; do
  case "${path}" in
    .cursor/skills/*/SKILL.md|.cursor/skills/*/*|.cursor/rules/cemini-goal-skill.mdc|.cursor/rules/cemini-route-outsource.mdc|.cursor/rules/cemini-cursor-security-preflight.mdc|.cursor/rules/cemini-phase1-policy-wires.mdc|.cursor/rules/cemini-federation-skill-sync.mdc|scripts/sync_federation_cursor_skills.sh|scripts/post-commit.sh)
      need_sync=1
      break
      ;;
  esac
done <<< "${changed}"

if [[ "${need_sync}" -eq 0 ]]; then
  exit 0
fi

if [[ ! -x "${SYNC}" ]]; then
  chmod +x "${SYNC}" 2>/dev/null || true
fi

if [[ ! -f "${SYNC}" ]]; then
  echo "[post-commit] missing ${SYNC}" >&2
  exit 0
fi

echo "[post-commit] federation skill/rule change detected — syncing workspaces..."
if bash "${SYNC}"; then
  echo "[post-commit] federation sync OK"
else
  echo "[post-commit] federation sync FAILED (commit already recorded; fix + re-run sync)" >&2
  exit 0
fi
