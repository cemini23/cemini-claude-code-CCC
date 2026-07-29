---
title: OpenAI Codex CLI — implementer lane
type: entity
tags: [entity, tool, codex, cli, openai, orchestration, k207]
keywords: [codex exec, @openai/codex, ChatGPT login, gpt-5.6-terra, darwin-arm64]
related:
  - concepts/subagent-orchestration.md
  - concepts/operator-model-selection.md
maturity: validated
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @concepts/subagent-orchestration.md — Cursor Task `codex-implementer` lane
- @concepts/operator-model-selection.md — when to pick Codex vs Grok/Fable

## Raw Concept

User-global OpenAI Codex CLI used as the cross-vendor implementer for Cemini (Cursor Task + Claude Code orchestration).

## Narrative

| Field | Value |
|-------|--------|
| Package | `@openai/codex` (npm) |
| Version (2026-07-29) | **0.145.0** |
| Binary | `~/.local/bin/codex` → package; vendor at `…/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex` |
| Auth | ChatGPT login (`codex login`) — `~/.codex/auth.json` |
| Smoke | `codex exec --skip-git-repo-check 'Reply with exactly the single token: CODEX_OK'` |
| Adopt script | `scripts/adopt_codex_cli.sh` (mirrored OSINT ↔ CCC) |

**2026-07-29 repair:** old vendor path `…/codex/codex` was ENOENT (stale 0.129 install). Reinstall fixed layout to `…/bin/codex`. ChatGPT plan does **not** support all API model slugs (e.g. `o4-mini`) — use Codex default / plan models.

## Dead Ends

- Pinning `o4-mini` under ChatGPT auth.
- Assuming per-workspace `node_modules` — CLI is user-global via PATH.
