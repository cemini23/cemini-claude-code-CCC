#!/usr/bin/env bash
# Install the CCC step-gate PreToolUse hook into ~/.claude/settings.local.json.
#
# Idempotent merge:
#   - backs up ~/.claude/settings.local.json (timestamped copy) if present
#   - adds/updates hooks.PreToolUse matcher "Bash|Write|Edit" -> command
#     `python3 "<CCC>/scripts/claude_pretooluse_step_gate.py"` timeout 5
#   - leaves every other key and hook untouched (claude-mem SessionStart stays)
#   - prints no secrets (never echoes the settings file contents)
#
# The hook denies ONLY step-gate HOLD verdicts; PROCEED/ESCALATE always allow.
# Kill switch: STEP_GATE_HOOK=0 in the hook process env disables the gate.
#
# Usage:
#   bash scripts/install_pretooluse_step_gate.sh

set -euo pipefail

# Resolve repo root from script location (scripts/ -> repo root).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK_SCRIPT="$REPO_ROOT/scripts/claude_pretooluse_step_gate.py"
SETTINGS_FILE="$HOME/.claude/settings.local.json"
MATCHER="Bash|Write|Edit"

if [[ ! -f "$HOOK_SCRIPT" ]]; then
    echo "Error: $HOOK_SCRIPT not found — run from the repo or fix the path." >&2
    exit 1
fi

mkdir -p "$HOME/.claude"

# Backup (timestamped, keep a fresh copy per install; harmless if run twice).
if [[ -f "$SETTINGS_FILE" ]]; then
    BACKUP="$SETTINGS_FILE.bak.$(date +%Y%m%d%H%M%S)"
    cp "$SETTINGS_FILE" "$BACKUP"
    echo "backup: $BACKUP"
fi

python3 - "$SETTINGS_FILE" "$HOOK_SCRIPT" "$MATCHER" <<'PY'
import json
import sys

settings_file, hook_script, matcher = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    with open(settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {}
except json.JSONDecodeError as e:
    print(f"Error: {settings_file} is not valid JSON ({e}) — aborting, no changes made.", file=sys.stderr)
    sys.exit(1)

if not isinstance(settings, dict):
    print(f"Error: {settings_file} is not a JSON object — aborting, no changes made.", file=sys.stderr)
    sys.exit(1)

hooks = settings.setdefault("hooks", {})
pretooluse = hooks.setdefault("PreToolUse", [])
if not isinstance(pretooluse, list):
    print("Error: hooks.PreToolUse is not a list — aborting, no changes made.", file=sys.stderr)
    sys.exit(1)

command = f'python3 "{hook_script}"'
entry = {"type": "command", "command": command, "timeout": 5}

# Find the matcher block we own; keep every other block (SessionStart, etc.).
block = next((b for b in pretooluse if isinstance(b, dict) and b.get("matcher") == matcher), None)
if block is None:
    block = {"matcher": matcher, "hooks": []}
    pretooluse.append(block)

inner = block.setdefault("hooks", [])
if not isinstance(inner, list):
    print(f"Error: hooks.PreToolUse matcher '{matcher}' hooks is not a list — aborting.", file=sys.stderr)
    sys.exit(1)

# Replace an existing identical command entry, else append (idempotent).
for i, h in enumerate(inner):
    if isinstance(h, dict) and h.get("command") == command:
        inner[i] = entry
        break
else:
    inner.append(entry)

import os
import tempfile

fd, tmp_path = tempfile.mkstemp(prefix="settings.local.", suffix=".json", dir=os.path.dirname(settings_file) or ".")
try:
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")
    os.replace(tmp_path, settings_file)
except Exception:
    try:
        os.unlink(tmp_path)
    except OSError:
        pass
    raise

print(f"installed: PreToolUse matcher '{matcher}' in {settings_file}")
print(f"  command: {command}")
print("  timeout: 5s — denies ONLY step-gate HOLD; PROCEED/ESCALATE allow")
PY

echo "verify:"
echo "  grep -n claude_pretooluse_step_gate \"$SETTINGS_FILE\""
