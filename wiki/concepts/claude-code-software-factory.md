---
title: Claude Code software factory — multi-repo codegen orchestration metaphor
type: concept
tags: [concept, claude-code, orchestration, multi-repo, k67]
keywords: [software-factory, sairahul1, multi-surface, shared-skills, subagent]
related:
  - concepts/subagent-orchestration.md
  - concepts/code-as-agent-harness.md
  - entities/tools/openspec.md
  - entities/patterns/scatter-gather.md
  - entities/tools/claude-code-game-studios.md
  - concepts/claude-code-personal-os-scope.md
  - sources/k67-explorax-100-repos-reference.md
  - entities/tools/purple-cli.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — factory = parallel subagents + shared skill library
- `@concepts/code-as-agent-harness.md` — harness layers for multi-repo fan-out
- `@entities/tools/openspec.md` — spec-driven factory leg before codegen
- `@entities/patterns/scatter-gather.md` — scatter work across repos; gather in integration agent
- `@entities/tools/claude-code-game-studios.md` — role-graph steal-from; factory adds multi-repo surface
- `@concepts/claude-code-personal-os-scope.md` — contrast: factory is **engineering** scope, not life-ops

Cross-wiki: K67 Post 24 (@sairahul1).

## Raw Concept

K67 — **software factory** metaphor: one Claude Code workspace driving multiple repos/surfaces with **shared skills** and coordinated subagents. CCC documents orchestration alignment only — **no OSINT prod port**.

## Narrative

### Factory components [TENTATIVE]

| Layer | CCC mapping |
|-------|-------------|
| Shared skills | `~/.claude/skills/` + project skills; `@concepts/skill-vetting.md` |
| Work partitioning | `@concepts/subagent-orchestration.md` Task/Agent fan-out |
| Integration | Parent session or conductor synthesis |
| Spec gate | `@entities/tools/openspec.md` before cross-repo changes |

### vs Cemini prod

CeminiSuite uses LangGraph/conductor for **trading** — factory pattern applies to **CeminiSuite + wiki repos** on laptop, not market execution paths.

### Verdict

**REFERENCE** — vocabulary for CCC orchestration docs and `/goal` envelopes spanning multiple git roots.

## Snippets

> "Multi-repo / multi-surface codegen with shared skills — factory metaphor for CCC orchestration docs."
> — [Source: briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md, Post 24]
