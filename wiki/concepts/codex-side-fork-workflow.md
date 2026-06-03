---
title: Codex /side and /fork — branch exploration without polluting main thread
type: concept
tags: [concept, codex, harness, side, fork, goal, k84]
keywords: [ziwenxu, openai-codex, branch-exploration, cursor-fork, git-worktree, parallel-ide]
related:
  - concepts/2026-05-13_multi-codex-codex-home-isolation.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/cursor-ide-workspace.md
  - concepts/code-as-agent-harness.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - entities/tools/claude-code.md
maturity: draft
created: 2026-05-30
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md"
---

## Relations

- `@concepts/2026-05-13_multi-codex-codex-home-isolation.md` — parallel Codex CLI instances via `CODEX_HOME`
- `@entities/patterns/full-prompt-goal-template.md` — Codex `/goal` maps to Cemini `/goal` + OpenSpec lane
- `@concepts/cursor-ide-workspace.md` — Cursor multi-chat / Agent fork as local analog
- `@concepts/code-as-agent-harness.md` — harness-level thread isolation
- `@concepts/claude-desktop-vs-claude-code.md` — Codex as parallel OpenAI harness, not CCC primary
- `@entities/tools/lazy-tool.md` — OSINT-side MCP proxy; same federation, different IDE
- `@entities/tools/conductor-mcp.md` — prod orchestration; Codex is reference parallel IDE
- `@sources/trading-posts-compilation-k84-2026-05-30.md` — provenance (K84 Posts 3–8)

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md` (canon).

## Raw Concept

K84 Posts 3–8 (@ziwenxu_ / OpenAI): **Codex harness** features for long-horizon agent work — especially `/side` (branch exploration) and `/fork` (preserve good path before risky work). CCC documents as **steal-from patterns** mapped to Cursor + Claude Code, not as confirmed Cemini Codex adoption **`[NEEDS VERIFICATION 2026-05-30]`** until verified on operator Codex build.

## Narrative

| Codex feature | Intent | Cemini analog |
|---------------|--------|---------------|
| `/side` | Explore alternate approach without polluting main agent thread | New Cursor chat; Claude Code subagent; git branch |
| `/fork` | Snapshot good state before risky refactor | Git commit/checkpoint; Cursor fork; worktree |
| `/goal` | Long-horizon task decomposition | `@entities/patterns/full-prompt-goal-template.md` + OpenSpec |
| `/pet` | Low-priority novelty | Skip unless mobile Codex stabilizes |
| Skills + project rules | Persistent harness instructions | `.cursor/rules/`, `.claude/settings.json`, SKILL.md |

### Parallel IDE, not replacement

Codex + Claude Code + Cursor coexist in the federation:

- **Cursor** — primary laptop IDE (`@concepts/cursor-ide-workspace.md`)
- **Claude Code** — hooks, claude-mem, plugin marketplace
- **Codex** — OpenAI CLI harness; compare isolation to `@concepts/2026-05-13_multi-codex-codex-home-isolation.md`

**Do not** treat X-thread product claims as `[CONFIRMED]` without local verification on the installed Codex version.

### K97 Post 10 — Codex 30-min course [TENTATIVE]

@0xCodez beginner course on **OpenAI Codex CLI** — onboarding path for parallel IDE. CCC operators already on Claude Code: skim for `/side`, `/fork`, skills parity only; full course is `[NEEDS VERIFICATION 2026-06-03]` against installed Codex build. Cross-link: [OpenAI Codex docs](https://developers.openai.com/codex) (retrieved 2026-06-03).

### Do not port (K84 brief)

Crypto Polymarket bot stack from @0xPhilanthrop stays on `@osint-wiki` — harness patterns only on CCC.

## Snippets

> Codex hidden features: `/side`, `/fork`, `/goal`, skills, mobile preview — route harness patterns to CCC, trading content to OSINT.
> — [Source: briefs/2026-05-30_k84-codex-harness-from-osint-posts.md; @osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md]
