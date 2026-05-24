#!/usr/bin/env bash
# Exa MCP (stdio) — loads API key from env or ~/.cemini/exa-api-key (never commit keys).
set -euo pipefail

if [[ -z "${EXA_API_KEY:-}" ]] && [[ -f "${HOME}/.cemini/exa-api-key" ]]; then
  EXA_API_KEY="$(tr -d '[:space:]' < "${HOME}/.cemini/exa-api-key")"
  export EXA_API_KEY
fi

if [[ -z "${EXA_API_KEY:-}" ]]; then
  echo "mcp_exa: set EXA_API_KEY or write key to ~/.cemini/exa-api-key" >&2
  exit 1
fi

exec npx -y exa-mcp-server
