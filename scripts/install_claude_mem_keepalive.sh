#!/usr/bin/env bash
# Install LaunchAgents that keep one claude-mem worker on the latest plugin
# version and reset the hook lockout before it can block every workspace.
#
# Usage:
#   bash scripts/install_claude_mem_keepalive.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/scripts/claude_mem_keepalive.py"
BIN="$HOME/.claude-mem/bin/claude-mem-keepalive.py"
AGENT_DIR="$HOME/Library/LaunchAgents"
WORKER_PLIST="$AGENT_DIR/com.cemini.claude-mem-worker.plist"
WATCH_PLIST="$AGENT_DIR/com.cemini.claude-mem-watchdog.plist"
PYTHON="/usr/bin/python3"
LOG_DIR="$HOME/Library/Logs"

if [[ ! -f "$SRC" ]]; then
  echo "ERROR: missing $SRC" >&2
  exit 1
fi

mkdir -p "$HOME/.claude-mem/bin" "$AGENT_DIR" "$LOG_DIR" "$HOME/.claude-mem/state"
cp "$SRC" "$BIN"
chmod 755 "$BIN" "$SRC"

cat > "$WORKER_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cemini.claude-mem-worker</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PYTHON}</string>
    <string>${BIN}</string>
    <string>run</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>ThrottleInterval</key>
  <integer>15</integer>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>${HOME}/.bun/bin:${HOME}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>${HOME}</string>
  </dict>
  <key>StandardOutPath</key>
  <string>${LOG_DIR}/cemini-claude-mem-worker.log</string>
  <key>StandardErrorPath</key>
  <string>${LOG_DIR}/cemini-claude-mem-worker.log</string>
</dict>
</plist>
EOF

cat > "$WATCH_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cemini.claude-mem-watchdog</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PYTHON}</string>
    <string>${BIN}</string>
    <string>watch</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>StartInterval</key>
  <integer>30</integer>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>${HOME}/.bun/bin:${HOME}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>${HOME}</string>
  </dict>
  <key>StandardOutPath</key>
  <string>${LOG_DIR}/cemini-claude-mem-watchdog.log</string>
  <key>StandardErrorPath</key>
  <string>${LOG_DIR}/cemini-claude-mem-watchdog.log</string>
</dict>
</plist>
EOF

chmod 644 "$WORKER_PLIST" "$WATCH_PLIST"

for label in com.cemini.claude-mem-worker com.cemini.claude-mem-watchdog; do
  launchctl unload "$AGENT_DIR/${label}.plist" 2>/dev/null || true
done

# Drop any leftover ad-hoc daemon so launchd can bind 37702.
pkill -f '/claude-mem/.*/scripts/worker-service' 2>/dev/null || true
sleep 1

launchctl load "$WORKER_PLIST"
launchctl load "$WATCH_PLIST"

echo "installed:"
echo "  $BIN"
echo "  $WORKER_PLIST"
echo "  $WATCH_PLIST"

ok=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  if curl -fsS -m 2 "http://127.0.0.1:37702/api/health" >/tmp/cm-ka-health.json 2>/dev/null; then
    echo "health: $(cat /tmp/cm-ka-health.json)"
    ok=1
    break
  fi
  sleep 1
done
if [[ "$ok" -ne 1 ]]; then
  echo "WARN: worker not healthy yet; check $LOG_DIR/cemini-claude-mem-worker.log" >&2
  exit 1
fi
