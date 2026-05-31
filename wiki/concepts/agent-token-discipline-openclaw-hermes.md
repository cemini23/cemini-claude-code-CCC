---
title: Agent token discipline — OpenClaw / Hermes waste patterns
type: concept
tags: [concept, token-economics, openclaw, hermes, k69]
keywords: [voxyz, openclaw, hermes, token-waste, always-on-agent]
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/three-cache-architecture.md
  - concepts/context-engineering.md
  - entities/tools/hermes-agent.md
  - entities/tools/claude-mem.md
  - entities/tools/claude-code.md
  - entities/tools/ai-token-monitor.md
  - entities/tools/codexbar.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - entities/tools/build-your-own-openclaw.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/karpathy-token-efficiency-patterns.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - concepts/agent-personality-file-hermes-openclaw.md
  - sources/trading-posts-compilation-16-2026-05-31.md
  - concepts/remote-hermes-access-pattern.md
maturity: draft
created: 2026-05-27
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @concepts/token-economics-and-prompt-caching.md — API-side economics
- @concepts/three-cache-architecture.md — cache discipline vs unbounded always-on loops
- @concepts/context-engineering.md — compaction and subagent offload
- @entities/tools/hermes-agent.md — reference runtime cited in post (not Cemini adopt)
- @entities/tools/claude-mem.md — bounded observation vs always-on chat gateways
- @entities/tools/claude-code.md — primary harness with explicit session boundaries
- @entities/tools/ai-token-monitor.md — monitoring steal-from
- @entities/tools/codexbar.md — macOS limit tracking
- @sources/trading-posts-compilation-20-2026-05-27.md — Post 13 (@Voxyz_ai)

## Raw Concept

K69 Post 13 (@Voxyz_ai): **token waste** in always-on **OpenClaw / Hermes** setups — messaging gateways, redundant tool loops, unbounded memory reloads. Warning pattern for personal-agent stacks; Cemini already uses different architecture.

## Narrative

### Failure modes cited [TENTATIVE]

| Pattern | Risk |
|---------|------|
| 24/7 gateway polling | Background turns burn API quota without operator intent |
| Full memory snapshot every turn | Ignores prefix caching / hot.md pin discipline |
| Skill auto-write loops | Multi-step tasks spawn unreviewed skill files + re-read cost |
| Parallel OpenClaw + Claude Code | Duplicate harnesses without shared token budget |

### Cemini countermeasures [CONFIRMED via existing stack]

- Session-scoped Claude Code + `@concepts/three-cache-architecture.md`
- `@entities/tools/lazy-tool.md` for MCP catalog cost
- `@entities/mcp-servers/stash.md` for episodic memory without full vault re-index
- Hermes/OpenClaw **reference only** — `@entities/tools/hermes-agent.md`

### Posture

Do **not** add always-on Hermes gateway beside conductor without token budget + kill switch. Post is anti-pattern catalog, not adoption pitch.

## Snippets

> OpenClaw/Hermes token waste — always-on agent discipline warning. [TENTATIVE — @Voxyz_ai, Posts.docx K69 Post 13]
