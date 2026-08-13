#!/usr/bin/env bash
# Federation Cursor security preflight — scan .cursor (and skills) across all
# Cemini Cursor workspaces + user-global ~/.cursor.
#
# Canon: Cemini claude code CCC/scripts/cursor_security_preflight_federation.sh
# Install: ln -sf … ~/.local/bin/cursor-security-preflight
#
# Usage:
#   cursor-security-preflight              # all workspaces (default)
#   cursor-security-preflight --local      # only $PWD (or --root PATH)
#   cursor-security-preflight --root DIR   # single workspace root
#   cursor-security-preflight --quick      # skip skill-scanner; agentshield+skillspector only
#
# Requires on PATH: agentshield, skillspector (skill-scanner optional).
set -euo pipefail

CCC_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_ROOT="${HOME}/.cursor/security-preflight"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
MODE="all"   # all | local
QUICK=0
SINGLE_ROOT=""
FAIL=0
SCANNED=0

# Same federation roots as sync_federation_cursor_skills.sh (+ tipdrop Desktop canon).
WORKSPACES=(
  "${CCC_ROOT}"
  "/Users/claudiobarone/Projects/OSINT WORKSPACE"
  "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
  "/Users/claudiobarone/Projects/Gambling wiki"
  "/Users/claudiobarone/Desktop/projects/Gambling wiki"
  "/Users/claudiobarone/Projects/Game Dev wiki"
  "/Users/claudiobarone/Desktop/projects/Game Dev wiki"
  "/Users/claudiobarone/Projects/Cybersecurity wiki"
  "/Users/claudiobarone/Desktop/projects/Cybersecurity wiki"
  "/Users/claudiobarone/Projects/Image gen"
  "/Users/claudiobarone/Desktop/projects/Image gen"
  "/Users/claudiobarone/Projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Projects/3D printing"
  "/Users/claudiobarone/Desktop/projects/3D printing"
  "/Users/claudiobarone/Projects/CeminiSuite"
  "/Users/claudiobarone/Desktop/projects/CeminiSuite"
  "/Users/claudiobarone/Projects/cemini-federation-hub"
  "/Users/claudiobarone/Desktop/projects/cemini-federation-hub"
  "/Users/claudiobarone/Projects/castle-sim"
  "/Users/claudiobarone/Desktop/projects/castle-sim"
  "/Users/claudiobarone/Projects/CeminiDFS"
  "/Users/claudiobarone/Desktop/projects/CeminiDFS"
  "/Users/claudiobarone/Projects/world-cup-bot"
  "/Users/claudiobarone/Desktop/projects/world-cup-bot"
  "/Users/claudiobarone/Projects/wc-ticket-monitor"
  "/Users/claudiobarone/Desktop/projects/wc-ticket-monitor"
  "/Users/claudiobarone/Projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Desktop/projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Projects/agent-toolkit-demo"
  "/Users/claudiobarone/Desktop/projects/agent-toolkit-demo"
  "/Users/claudiobarone/Desktop/projects/tipdrop-workspace-kit"
  "/Users/claudiobarone/Projects/tipdrop-workspace-kit"
  "/Users/claudiobarone/Desktop/projects/tipdrop-scanner"
  "/Users/claudiobarone/Projects/tipdrop-scanner"
  "/Users/claudiobarone/Projects/pm-lp-canary-wiki"
  "/Users/claudiobarone/Desktop/projects/pm-lp-canary-wiki"
)

usage() {
  cat <<'EOF'
Federation Cursor security preflight — all Cemini Cursor workspaces + ~/.cursor

  cursor-security-preflight              # all workspaces (default)
  cursor-security-preflight --local      # only $PWD
  cursor-security-preflight --root DIR   # single workspace root
  cursor-security-preflight --quick      # skip skill-scanner

Requires: agentshield, skillspector on PATH (skill-scanner optional).
Reports: ~/.cursor/security-preflight/<stamp>/  (symlink: latest)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --all) MODE="all"; shift ;;
    --local) MODE="local"; shift ;;
    --root) SINGLE_ROOT="$2"; MODE="local"; shift 2 ;;
    --quick) QUICK=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "MISSING: $1 not on PATH"
    FAIL=1
    return 1
  fi
}

slugify() {
  # Path → filesystem-safe label
  echo "$1" | sed 's|^/Users/[^/]*/||; s|/|-|g; s| |-|g; s|:|-|g'
}

dedupe_existing_dirs() {
  # stdin: paths; stdout: unique realpaths that exist
  local -a seen=()
  local p rp
  while IFS= read -r p; do
    [[ -z "$p" || ! -d "$p" ]] && continue
    rp="$(cd "$p" && pwd -P)"
    local s
    for s in "${seen[@]+"${seen[@]}"}"; do
      [[ "$s" == "$rp" ]] && continue 2
    done
    seen+=("$rp")
    echo "$rp"
  done
}

collect_roots() {
  if [[ "$MODE" == "local" ]]; then
    if [[ -n "$SINGLE_ROOT" ]]; then
      echo "$SINGLE_ROOT"
    else
      echo "$(pwd -P)"
    fi
    return
  fi
  # Global Cursor Home first, then federation workspaces
  echo "${HOME}/.cursor"
  local w
  for w in "${WORKSPACES[@]}"; do
    echo "$w"
  done
}

scan_agentshield() {
  local path="$1"
  local label="$2"
  local out_md="${REPORT_DIR}/agentshield-${label}.md"
  local out_log="${REPORT_DIR}/agentshield-${label}.ndjson"
  echo ""
  echo "-- agentshield: ${path} --"
  if agentshield scan -p "$path" -f markdown \
    --min-severity medium \
    --supply-chain \
    --log "$out_log" \
    >"$out_md" 2>"${REPORT_DIR}/agentshield-${label}.err"; then
    echo "  wrote ${out_md}"
  else
    echo "  WARN agentshield non-zero (see ${out_md} / .err)"
    FAIL=1
  fi
  SCANNED=$((SCANNED + 1))
}

scan_skillspector_tree() {
  local skills_dir="$1"
  local label="$2"
  [[ -d "$skills_dir" ]] || return 0
  echo ""
  echo "-- skillspector --no-llm: ${skills_dir} --"
  # ~/.cursor/skills mixes Cemini federation skills with Cursor plugin vendor
  # dumps (Cloudflare). Vendor skills are scored in plugin cache, not here —
  # turnstile-spin CRITICAL was vitest/wrangler CVEs + secret-fetch scripts.
  local scan_root="$skills_dir"
  local tmp=""
  if [[ "$skills_dir" == "${HOME}/.cursor/skills" ]]; then
    tmp="$(mktemp -d "${TMPDIR:-/tmp}/preflight-cemini-skills.XXXXXX")"
    local skill_dir name
    shopt -s nullglob
    for skill_dir in "${skills_dir}"/*/; do
      name="$(basename "$skill_dir")"
      case "$name" in
        turnstile-spin|cloudflare|cloudflare-one|cloudflare-one-migrations|cloudflare-email-service|wrangler|workers-best-practices|durable-objects|sandbox-sdk|web-perf|agents-sdk)
          echo "  SKIP vendor plugin skill: ${name}"
          continue
          ;;
      esac
      ln -s "$skill_dir" "${tmp}/${name}"
    done
    shopt -u nullglob
    scan_root="$tmp"
  fi
  if skillspector scan "$scan_root" --no-llm --recursive \
    --format markdown \
    --output "${REPORT_DIR}/skillspector-${label}.md" 2>&1 \
    | tee "${REPORT_DIR}/skillspector-${label}.log"; then
    :
  else
    echo "  WARN skillspector non-zero"
    FAIL=1
  fi
  [[ -n "$tmp" && -d "$tmp" ]] && rm -rf "$tmp"
  SCANNED=$((SCANNED + 1))
}

scan_skill_scanner_each() {
  local skills_dir="$1"
  local label="$2"
  [[ -d "$skills_dir" ]] || return 0
  command -v skill-scanner >/dev/null 2>&1 || return 0
  echo ""
  echo "-- skill-scanner: ${skills_dir}/* --"
  local skill_dir name
  shopt -s nullglob
  for skill_dir in "${skills_dir}"/*/; do
    name="$(basename "$skill_dir")"
    [[ -f "${skill_dir}/SKILL.md" ]] || continue
    case "$name" in
      turnstile-spin|cloudflare|cloudflare-one|cloudflare-one-migrations|cloudflare-email-service|wrangler|workers-best-practices|durable-objects|sandbox-sdk|web-perf|agents-sdk)
        echo "  SKIP vendor plugin skill: ${name}"
        continue
        ;;
    esac
    if skill-scanner scan "$skill_dir" --format summary \
      --fail-on-severity critical \
      >"${REPORT_DIR}/skill-scanner-${label}-${name}.log" 2>&1; then
      echo "  OK ${name}"
    else
      echo "  FAIL ${name} (critical+ — see log)"
      FAIL=1
    fi
  done
  shopt -u nullglob
}

REPORT_DIR="${REPORT_ROOT}/${STAMP}"
mkdir -p "${REPORT_DIR}"
ln -sfn "${REPORT_DIR}" "${REPORT_ROOT}/latest"

echo "== cursor security preflight federation (${STAMP}) =="
echo "mode=${MODE} quick=${QUICK}"
echo "reports → ${REPORT_DIR}"

need agentshield || true
need skillspector || true
if [[ "$QUICK" -eq 0 ]]; then
  need skill-scanner || true
fi

# Always scan Claude Code global config once (not Cursor, but same laptop agents)
if command -v agentshield >/dev/null 2>&1 && [[ -d "${HOME}/.claude" ]]; then
  scan_agentshield "${HOME}/.claude" "global-claude"
fi

while IFS= read -r root; do
  [[ -z "$root" ]] && continue
  label="$(slugify "$root")"
  cursor_dir="${root}/.cursor"
  # User-global ~/.cursor IS the cursor dir
  if [[ "$root" == "${HOME}/.cursor" ]]; then
    cursor_dir="$root"
  fi
  if [[ ! -d "$cursor_dir" ]]; then
    echo "SKIP no .cursor: ${root}"
    continue
  fi
  echo ""
  echo "======== ${root} ========"
  if command -v agentshield >/dev/null 2>&1; then
    scan_agentshield "$cursor_dir" "cursor-${label}"
  fi
  skills_dir="${cursor_dir}/skills"
  if command -v skillspector >/dev/null 2>&1; then
    scan_skillspector_tree "$skills_dir" "skills-${label}"
  fi
  if [[ "$QUICK" -eq 0 ]]; then
    scan_skill_scanner_each "$skills_dir" "${label}"
  fi
done < <(collect_roots | dedupe_existing_dirs)

# Summary index
{
  echo "# Cursor security preflight — ${STAMP}"
  echo
  echo "- mode: \`${MODE}\`"
  echo "- scanned units: ${SCANNED}"
  echo "- fail flag: ${FAIL}"
  echo "- report dir: \`${REPORT_DIR}\`"
  echo
  echo "## Artifacts"
  ls -1 "${REPORT_DIR}" | sed 's/^/- /'
} >"${REPORT_DIR}/INDEX.md"

echo ""
echo "INDEX → ${REPORT_DIR}/INDEX.md"
if [[ "${FAIL}" -ne 0 ]]; then
  echo "PREFLIGHT finished with failures"
  exit 1
fi
echo "PREFLIGHT OK (${SCANNED} scan units)"
exit 0
