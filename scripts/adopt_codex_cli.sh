#!/usr/bin/env bash
# adopt_codex_cli.sh — ensure OpenAI Codex CLI works on this Mac for all Cemini workspaces
#
# Codex is user-global (~/.local/bin/codex → npm @openai/codex). Cursor Task
# codex-implementer + Claude Code orchestration lanes resolve it from PATH.
# Re-run after ENOENT on darwin-arm64 vendor binary or ChatGPT auth drift.
#
# Usage:
#   bash scripts/adopt_codex_cli.sh
#   bash scripts/adopt_codex_cli.sh --reinstall
#   bash scripts/adopt_codex_cli.sh --smoke
set -euo pipefail

REINSTALL=0
SMOKE=0
for arg in "$@"; do
  case "$arg" in
    --reinstall) REINSTALL=1 ;;
    --smoke) SMOKE=1 ;;
    -h|--help)
      sed -n '1,20p' "$0"
      exit 0
      ;;
  esac
done

REPORT_DIR="${HOME}/.cemini/reports"
mkdir -p "$REPORT_DIR"
REPORT="${REPORT_DIR}/codex-cli-adopt-$(date -u +%Y-%m-%d).md"
NPM_PREFIX="${NPM_CONFIG_PREFIX:-${HOME}/.local}"
export PATH="${NPM_PREFIX}/bin:${HOME}/.local/bin:${PATH}"

echo "Codex CLI adopt"
echo "==============="

if [[ "$REINSTALL" -eq 1 ]] || ! command -v codex >/dev/null 2>&1; then
  echo "Installing/reinstalling @openai/codex@latest into ${NPM_PREFIX}…"
  npm install -g @openai/codex@latest
fi

if ! command -v codex >/dev/null 2>&1; then
  echo "ERROR: codex not on PATH after install. Ensure ${NPM_PREFIX}/bin is in PATH." >&2
  exit 1
fi

VER="$(codex --version 2>&1 | head -1 || true)"
echo "Version: $VER"

# New package layout uses …/bin/codex; old broken layout used …/codex/codex
PKG="${NPM_PREFIX}/lib/node_modules/@openai/codex"
BIN_NEW="${PKG}/node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex"
BIN_OLD="${PKG}/node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/codex/codex"
if [[ -x "$BIN_NEW" ]]; then
  echo "Vendor binary: OK ($BIN_NEW)"
elif [[ -x "$BIN_OLD" ]]; then
  echo "Vendor binary: OK legacy ($BIN_OLD)"
else
  echo "WARN: vendor binary path missing — re-run with --reinstall" >&2
fi

STATUS="$(codex login status 2>&1 || true)"
echo "Auth: $STATUS"
if ! echo "$STATUS" | grep -qi 'Logged in'; then
  echo ""
  echo "Not logged in. Run ONE of:"
  echo "  codex login                 # ChatGPT device/browser auth"
  echo "  printenv OPENAI_API_KEY | codex login --with-api-key"
  echo ""
  echo "Then re-run: bash $0 --smoke"
fi

# Ensure common shells see ~/.local/bin (idempotent)
ensure_path_line() {
  local rc="$1"
  local line='export PATH="$HOME/.local/bin:$PATH"'
  [[ -f "$rc" ]] || touch "$rc"
  if ! grep -qF '.local/bin' "$rc" 2>/dev/null; then
    printf '\n# Cemini — Codex / Claude / npm user globals\n%s\n' "$line" >>"$rc"
    echo "PATH: appended ~/.local/bin to $rc"
  else
    echo "PATH: $rc already references .local/bin"
  fi
}
ensure_path_line "${HOME}/.zshrc"
ensure_path_line "${HOME}/.zprofile"

SMOKE_RESULT="skipped"
if [[ "$SMOKE" -eq 1 ]] && echo "$STATUS" | grep -qi 'Logged in'; then
  echo "Smoke: codex exec (default ChatGPT model)…"
  OUT="$(cd /tmp && codex exec --skip-git-repo-check 'Reply with exactly the single token: CODEX_OK' 2>&1 || true)"
  if echo "$OUT" | grep -q 'CODEX_OK'; then
    SMOKE_RESULT="PASS"
    echo "Smoke: PASS"
  else
    SMOKE_RESULT="FAIL"
    echo "Smoke: FAIL — see tail of output"
    echo "$OUT" | tail -20
  fi
fi

# Mirror script into CCC + OSINT if we are running from either
SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
for DEST_ROOT in \
  "/Users/claudiobarone/Projects/Cemini claude code CCC" \
  "/Users/claudiobarone/Projects/OSINT WORKSPACE" \
  "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
do
  if [[ -d "$DEST_ROOT/scripts" ]]; then
    DEST="$DEST_ROOT/scripts/adopt_codex_cli.sh"
    if [[ "$(realpath "$SELF" 2>/dev/null || echo "$SELF")" != "$(realpath "$DEST" 2>/dev/null || echo "$DEST")" ]]; then
      cp "$SELF" "$DEST"
      chmod +x "$DEST"
      echo "Synced script → $DEST"
    fi
  fi
done

{
  echo "# Codex CLI adopt"
  echo ""
  echo "- **Date (UTC):** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- **Version:** $VER"
  echo "- **Auth:** $STATUS"
  echo "- **Smoke:** $SMOKE_RESULT"
  echo "- **PATH prefix:** ${NPM_PREFIX}/bin + ~/.local/bin"
  echo "- **Note:** ChatGPT login does not support all API model slugs (e.g. o4-mini). Use Codex default / ChatGPT-plan models."
  echo ""
  echo "## Workspaces"
  echo ""
  echo "CLI is user-global — any Open Folder that inherits login-shell PATH gets \`codex\`."
  echo "Cursor Task \`codex-implementer\` and CCC orchestration expect \`codex\` on PATH."
  echo ""
  echo "## Re-auth"
  echo ""
  echo '```bash'
  echo "codex login"
  echo "bash scripts/adopt_codex_cli.sh --smoke"
  echo '```'
} >"$REPORT"

echo ""
echo "Report: $REPORT"
echo "Done."
