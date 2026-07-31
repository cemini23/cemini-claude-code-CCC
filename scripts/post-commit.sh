#!/usr/bin/env bash
# CCC post-commit: autosync federation Cursor skills when canon changes.
# Installed via scripts/install-hooks.sh → .git/hooks/post-commit
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SYNC="${REPO_ROOT}/scripts/sync_federation_cursor_skills.sh"

# Only sync when this commit touched federation skill/rule surfaces
changed="$(git -C "${REPO_ROOT}" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null || true)"
if [[ -z "${changed}" ]]; then
  exit 0
fi

need_sync=0
while IFS= read -r path; do
  case "${path}" in
    .cursor/skills/*/SKILL.md|.cursor/skills/*/*|.cursor/rules/cemini-goal-skill.mdc|.cursor/rules/cemini-route-outsource.mdc|.cursor/rules/cemini-cursor-security-preflight.mdc|.cursor/rules/cemini-phase1-policy-wires.mdc|scripts/sync_federation_cursor_skills.sh)
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

echo "[post-commit] federation skill/rule change detected — syncing workspaces..."
if bash "${SYNC}"; then
  echo "[post-commit] federation sync OK"
else
  echo "[post-commit] federation sync FAILED (commit already recorded; fix + re-run sync)" >&2
  exit 0
fi
