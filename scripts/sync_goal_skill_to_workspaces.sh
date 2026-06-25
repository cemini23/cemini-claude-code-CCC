#!/usr/bin/env bash
# Sync /goal Cursor skill + rule to all Cemini federation workspaces.
# Delegates to sync_federation_cursor_skills.sh (goal + mattpocock skills).
set -euo pipefail
exec "$(cd "$(dirname "$0")" && pwd)/sync_federation_cursor_skills.sh" "$@"
