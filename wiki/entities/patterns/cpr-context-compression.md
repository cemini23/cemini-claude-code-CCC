---
title: "CPR — Compress / Preserve / Resume pattern for long-running Claude Code sessions"
type: entity
tags: [pattern, claude-code, context-compression, state-resumption, long-running-agents, hot-md, cross-wiki-stub]
keywords: [cpr, compress-preserve-resume, context-death, state-serialization, hot-md, claude-mem, session-checkpoint, eliaalberti-cpr, rohitg00-cpr-impl]
related:
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/tools/claude-mem.md
  - entities/patterns/ralph-loop.md
  - entities/mcp-servers/stash.md
  - entities/patterns/scatter-gather.md
  - entities/tools/everos.md
  - concepts/long-thread-context-decay.md
  - concepts/self-compacting-adaptive-context.md
  - sources/arxiv-self-compacting-agents-2606.23525.md
  - entities/patterns/full-prompt-goal-template.md
maturity: draft
created: 2026-05-17
updated: 2026-06-24
cross-wiki-source: "@osint-wiki/concepts/context-compression-resume-pattern.md"
---

## Relations

- @concepts/context-engineering.md — CPR is one of the four context-engineering levers (the "compaction" lever) operationalised as a pattern
- @concepts/token-economics-and-prompt-caching.md — CPR's compress step deliberately trades cache hit for context survival; the trade-off lives in token economics
- @entities/tools/claude-mem.md — CCC's reference implementation of the preserve/resume legs; the compress leg is Claude Code's native compaction
- @entities/patterns/ralph-loop.md — CPR's preserve step is exactly what Ralph's file-based memory does between iterations; same pattern, different terminology
- @entities/mcp-servers/stash.md — durable-storage MCP whose 8-stage consolidation implements the CPR compress leg at the persistence layer
- @entities/patterns/scatter-gather.md — fan-out topology where each branch independently runs CPR before its results are merged back upstream
- @osint-wiki/concepts/context-compression-resume-pattern.md — cross-wiki primary; full lineage, K8 source, agentmemory reference implementation, and architectural detail live there

## Raw Concept

CCC-side stub cross-routed from the OSINT primary. CPR ("Compress / Preserve / Resume") is a library-agnostic architectural pattern for long-running LLM agents that risk **context death** between sessions or in the face of process crashes. The pattern's canonical CCC manifestation is `hot.md` + claude-mem; the OSINT primary covers the LangGraph / pgvector / SHA-256-dedup reference implementation (`agentmemory/rohitg00-cpr-impl`).

## Narrative

### The pattern (three legs)

1. **Compress** — when the working context approaches the model's window, summarise the trajectory into a dense string before persisting. Cemini's manifestation: Claude Code's native compaction event (when the harness compresses prior messages), plus the `hot.md` ritual which is a hand-written compression.

**Rubric-gated compact (K124)** [TENTATIVE — arxiv-2606.23525]: prefer compress **after** a sub-task checkpoint, not mid-derivation. Before `/compact` or new chat, set in `hot.md`:

| Field | Values |
|-------|--------|
| `Checkpoint` | last completed sub-task name |
| `Compact OK` | `yes` / `no — mid-derivation` / `no — stuck loop` |

If `Compact OK` is not `yes`, use Task subagent with clean context instead of compacting the parent thread. See `@concepts/self-compacting-adaptive-context.md`.

2. **Preserve** — write compressed state to durable storage outside the LLM context. Cemini's manifestation: `hot.md` (gitignored session-state cache) plus claude-mem's observation index.
3. **Resume** — on next session start, read preserved state back in. Cemini's manifestation: the `## Session-start ritual` section of @CLAUDE.md reads `hot.md` first.

### Why catalogued in CCC

CCC operates the pattern, doesn't theorise about it. The pattern lives here because:

- **`hot.md` is the preserve leg.** Re-read on every session start. Rewritten at session end with updated position, open decisions, pending actions.
- **claude-mem is the dual preserve leg.** Semantic injection on SessionStart; the search/timeline tools surface preserved observations on demand.
- **Compression is opportunistic.** Cemini doesn't run a continuous compress loop; the harness compacts when it must, and the operator periodically refreshes `hot.md`.

The OSINT primary documents a deeper variant (LangGraph PostgresSaver + summarisation-before-serialization + RRF fusion via `agentmemory`). That's prescribed-not-built for OSINT; CCC's lighter `hot.md` + claude-mem stack is what actually runs.

### Failure modes the pattern guards against

- **Context death** — the agent's working memory exceeds the window and useful state evaporates. CPR's compress leg keeps the trajectory addressable.
- **Process crash** — the agent dies mid-task. CPR's preserve leg means the next session resumes from the last checkpoint, not from zero.
- **Cross-session amnesia** — the agent forgets prior decisions and re-litigates them. CPR's resume leg loads preserved state back in.

## Snippets

> The pattern is library-agnostic — the concrete reference implementation is `EliaAlberti/cpr-compress-preserve-resume`, but the underlying architectural shape applies to any long-running LLM agent that risks context death.
[Source: @osint-wiki/concepts/context-compression-resume-pattern.md]
