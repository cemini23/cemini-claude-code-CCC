---
title: "EverOS — long-term-memory OS for self-evolving agents (Apache-2.0)"
type: entity
tags: [tool, memory, context-offload, token-economics, self-evolving-agents, cross-wiki-route]
keywords: [everos, evermind-ai, long-term-memory, context-offload, disk-backed-memory, token-savings, agent-memory]
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/context-engineering.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md"
---

## Relations

- @concepts/token-economics-and-prompt-caching.md — EverOS's context-offload-to-disk pattern is a fourth lever beyond the three cache layers
- @concepts/context-engineering.md — offloading context to disk is a context-engineering primitive not currently in Cemini's toolkit
- @entities/patterns/cpr-context-compression.md — CPR compresses; EverOS offloads. Complementary primitives for the same problem
- @entities/tools/claude-mem.md — claude-mem captures observations passively; EverOS offloads active context to disk. Adjacent layers in the memory stack
- @entities/mcp-servers/stash.md — stash persists episodic memory; EverOS persists working context. Different memory tier, same direction
- @osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from OSINT K54 (26-URL eval, May 2026). `EverMind-AI/EverOS` (Apache-2.0, 4,968★) is a long-term-memory operating system for self-evolving agents that offloads context to disk to save tokens. The K54 eval initially rejected it on a fabricated "no license" finding; GitHub API verification confirmed Apache-2.0 — clean for adoption. Directly relevant to CCC token-economics and context-compaction research.

## Narrative

### What EverOS does

A memory OS layer for AI agents that persists working context to disk, reducing the token cost of re-loading context on every session:

- **Context offload to disk** — instead of keeping full context in the model's attention window, EverOS persists it to disk and reloads on demand
- **Self-evolving agent memory** — agents accumulate knowledge across sessions; the memory OS manages retrieval and staleness
- **Token savings** — by offloading context that doesn't need to be in the active window, EverOS claims significant token-cost reduction

### Why CCC cares

EverOS fills a gap in Cemini's current memory stack:

| Layer | Cemini's current tool | EverOS's role |
|-------|----------------------|---------------|
| Session state | `hot.md` | — |
| Passive observation | `claude-mem` | — |
| Episodic memory | `stash` MCP | — |
| **Working context persistence** | *(missing)* | EverOS |

The context-offload-to-disk pattern is a fourth context-engineering lever beyond Cemini's current three (prompt caching, subagent dispatch, MCP context optimisation). It's complementary to CPR (compress/preserve/resume) — CPR compresses context for re-injection; EverOS offloads it entirely and reloads on demand.

### Adoption posture

Apache-2.0 (verified via GitHub API — the K54 eval's "NO LICENSE FOUND" was wrong). 4,968★, actively maintained. Worth a Phase-0 audit for the context-offload pattern specifically. The self-evolving-agent architecture is secondary; the disk-backed context persistence is the primary CCC-relevant primitive.

[CONFIRMED] — Apache-2.0 verified via GitHub API (K54 cross-wiki source).
