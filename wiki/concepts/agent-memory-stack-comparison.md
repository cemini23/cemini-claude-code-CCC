---
title: Agent memory stack comparison — mem0, OpenClaw, Hermes, claude-mem
type: concept
tags: [concept, memory, openclaw, hermes, mem0, k72]
keywords: [mem0ai, openclaw, hermes-agent, claude-mem, memory-comparison]
related:
  - entities/tools/claude-mem.md
  - entities/tools/hermes-agent.md
  - entities/tools/claude-subconscious.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/three-cache-architecture.md
  - entities/mcp-servers/stash.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - sources/trading-posts-compilation-25-2026-05-27.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@entities/tools/claude-mem.md` — **adopted** CCC session memory
- `@entities/tools/hermes-agent.md` — reference runtime (not prod)
- `@entities/tools/claude-subconscious.md` — Letta layer (K71); parallel-impl check
- `@concepts/agent-token-discipline-openclaw-hermes.md` — cost of always-on memory agents
- `@concepts/three-cache-architecture.md` — stash vs claude-mem vs wiki layering
- `@entities/mcp-servers/stash.md` — episodic goals/hypotheses

Cross-wiki: K72 Post 1 (@mem0ai); OSINT `@entities/tools/hermes-agent.md`.

## Raw Concept

K72 Post 1 — marketing comparison of **mem0**, **OpenClaw**, and **Hermes** persistent-memory approaches for always-on agents. CCC documents **selection matrix**, not multi-install.

## Narrative

| Layer | Product | CCC posture |
|-------|---------|-------------|
| Session + observation index | claude-mem | **In use** |
| Episodic federation | stash | **Global MCP** |
| Personal-agent runtime | Hermes / OpenClaw | **Reference** — see token discipline page |
| Vector user memory API | mem0 | **Evaluate** — overlap risk with claude-mem |

**Rule:** one **SessionStart** memory owner — see `@entities/tools/claude-obsidian.md` rejection case study.

| Verdict | **REFERENCE** |

## Snippets

> "mem0 + OpenClaw + Hermes memory comparison."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 1]
