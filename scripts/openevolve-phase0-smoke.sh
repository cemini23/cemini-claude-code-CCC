#!/usr/bin/env bash
# Phase-0 smoke for openevolve — isolated temp venv; does not touch wiki or ~/.claude/
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORKDIR="${OPENEVOLVE_SMOKE_DIR:-$(mktemp -d /tmp/openevolve-smoke.XXXXXX)}"
VENV="${WORKDIR}/.venv"

echo "openevolve Phase-0 smoke"
echo "  workdir: ${WORKDIR}"
echo "  repo:    ${REPO_ROOT} (read-only; no writes here)"

cleanup() {
  if [[ "${KEEP_SMOKE_DIR:-}" != "1" ]] && [[ "${WORKDIR}" == /tmp/openevolve-smoke.* ]]; then
    rm -rf "${WORKDIR}"
    echo "removed ${WORKDIR}"
  else
    echo "kept ${WORKDIR} (KEEP_SMOKE_DIR=1 or custom OPENEVOLVE_SMOKE_DIR)"
  fi
}
trap cleanup EXIT

python3 -m venv "${VENV}"
# shellcheck source=/dev/null
source "${VENV}/bin/activate"
pip -q install --upgrade pip
pip -q install openevolve

if command -v openevolve >/dev/null 2>&1; then
  openevolve --help | head -n 20
elif python3 -c "import openevolve" 2>/dev/null; then
  python3 -m openevolve --help 2>/dev/null | head -n 20 || python3 -c "import openevolve; print('import ok:', openevolve.__file__)"
else
  echo "openevolve installed but CLI not on PATH — check package docs" >&2
  exit 1
fi

echo "Phase-0 smoke: PASS (isolated venv only)"
