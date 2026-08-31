---
title: CCC SIP-ready — PreToolUse step-gate + BM25 SCOUT leftovers (operator OK)
type: brief
tags: [brief, handoff, k311, k312, leftover]
keywords: [pretooluse, step-gate, scout, bm25, sip]
related:
  - concepts/hooks-for-automation.md
  - concepts/step-level-tool-guardrails.md
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
  - entities/skills/scout-tool-search.md
  - entities/skills/step-gate.md
maturity: draft
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@concepts/hooks-for-automation.md`
- `@concepts/step-level-tool-guardrails.md`
- `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md`

## Target

Operator **2026-08-31** gave full permissions to ship the two HITL leftovers from K311/K312:

1. **Dense SCOUT** — BM25 (corpus IDF) on local SKILL.md, no HF/vector DB, no extra pip.
2. **Real Claude Code PreToolUse hook** — deterministic `command` hook that **denies only HOLD** from `step_gate.classify`. Wire into **`~/.claude/settings.local.json`** (machine-local; wiki iterating-safely). Do **not** commit `~/.claude/settings.json`.

Then parent will audit with **GPT-5.6 Sol** and **Kimi**, then lint, commit, push, federation-sync.

Executor: live OpenCode Zen → **claude-ds Flash**. **Do not commit or push** — parent audits first.

## Plan

### A. BM25 SCOUT (`scripts/scout_tool_search.py`)

Keep CLI: `query` / `read` / `selftest`. Replace term-overlap scorer with **BM25-lite** (k1=1.5, b=0.75) over the local skill corpus (name + description + first heading). IDF from that corpus. Small substring bonus OK. **No** rank-bm25 pip, **no** sentence-transformers, **no** HF.

Selftest must still: ≥3 federation skills; query `route` returns `route`; nonsense query empty. Add: query `step` ranks `step-gate` in top-k.

Update `.cursor/skills/scout-tool-search/SKILL.md` (still `federation: true`, `disable-model-invocation: true`). Update wiki concept `hybrid-mcp-tool-discovery-lazy-catalog.md`. No `curl|bash` install recipes.

### B. PreToolUse step-gate hook

New `scripts/claude_pretooluse_step_gate.py`:

- Read Claude Code PreToolUse JSON from stdin (`tool_name` + `tool_input`).
- Flatten `tool_input` to an args summary string; call existing `step_gate.classify`.
- **HOLD** → stdout:
  ```json
  {"hookSpecificOutput":{"permissionDecision":"deny"},"systemMessage":"step-gate HOLD: <why>. Operator OK required."}
  ```
- **PROCEED** and **ESCALATE** → `permissionDecision: allow` (do **not** deny unknown tools — that would freeze the session; pairs K312 safety–utility).
- Env `STEP_GATE_HOOK=0` disables (always allow).
- `selftest` with synthetic payloads: force-push HOLD→deny; wiki_lint PROCEED→allow; unknown ESCALATE→allow.
- Timeout-friendly (no network). Exit 0 with JSON (not exit 2 on deny).

New `scripts/install_pretooluse_step_gate.sh` (idempotent):

- Backup `~/.claude/settings.local.json` if present.
- Merge `hooks.PreToolUse` matcher `Bash|Write|Edit` with command `python3 "<CCC>/scripts/claude_pretooluse_step_gate.py"` timeout 5s.
- Do **not** rewrite unrelated hooks (claude-mem SessionStart stays).
- Do **not** write secrets to stdout.
- **Run the installer** on this machine (operator OK).

Update `step_gate.py` docstring: hook exists; CLI remains. Update `.cursor/skills/step-gate/SKILL.md`: operator CLI **and** optional Claude Code hook; still no Stop-hook; still no `curl|bash`.

Wiki: `hooks-for-automation.md` — Cemini now has **one** PreToolUse: deny-on-HOLD only, settings.local.json. `step-level-tool-guardrails.md` leftover = shipped. Entities for both skills. `wiki/log.md`. Policy leftover lines already say shipped skills; add hook + BM25 note in `ccc-k310-k314-phase1-wires.mdc` / shared policy K311/K312 bullets.

### C. Out of scope

- Osmani label state machine, BrowseComp-Plus_CM, InstructionArbitrationBench clone, `/route` rewrite, dense MCP catalog, Stop hooks, `permissions.deny` duplicates.

## Success criteria (executor)

1. `python3 scripts/scout_tool_search.py selftest` PASS (BM25 path).
2. `python3 scripts/step_gate.py selftest` PASS.
3. `python3 scripts/claude_pretooluse_step_gate.py selftest` PASS.
4. `bash scripts/install_pretooluse_step_gate.sh` exit 0; `~/.claude/settings.local.json` contains PreToolUse + script path; no secrets printed.
5. `python3 scripts/wiki_lint.py` exit 0 (0 bidirectional gaps).
6. **No git commit, no push.** Dirty CLAUDE.md / LESSONS.md / keepalive **uncommitted**.
7. Final reply: file list + selftest evidence + whether installer ran.

## NEVER

- No secrets in git or chat. Do not commit `~/.claude/settings.json` or `.local.json`.
- No Stop hook. No deny-on-ESCALATE. No HF/vector DB. No `curl|bash` in SKILL.md.
- Do not rewrite `route-task.ps1`. Do not federation-sync CCC-only k310/k315/k325 rules.
- Do not auto-evolve other skills. Do not rewrite `## Verify`.
