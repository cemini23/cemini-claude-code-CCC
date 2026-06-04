---
title: "Scatter-gather topology — parallel subagent fan-out pattern (LangGraph origin)"
type: entity
tags: [pattern, claude-code, scatter-gather, langgraph, subagent-orchestration, parallel-execution, cross-wiki-stub]
keywords: [scatter-gather, langgraph-topology, parallel-fan-out, gather-aggregation, subagent-orchestration, conductor-routing]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/patterns/cpr-context-compression.md
  - entities/patterns/citadel-agent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/tools/cc-wf-studio.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - entities/tools/claude-code-game-studios.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - entities/tools/kimi-agent-swarm.md
  - concepts/claude-code-software-factory.md
  - entities/tools/rowboat.md
  - concepts/claude-code-subagent-templates.md
  - concepts/agent-five-gate-org-chart.md
maturity: draft
created: 2026-05-17
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/concepts/scatter-gather-topology.md"
---

## Relations

- @concepts/subagent-orchestration.md — scatter-gather is the topology Claude Code implements via parallel `Agent` tool calls; this pattern is the formal pattern name
- @entities/tools/conductor-mcp.md — the cross-wiki query router uses scatter-gather to fan out a single query across multiple wiki aliases and merge results
- @entities/patterns/tier1-tier2-agent-model.md — Tier-2 subagents are the natural scatter-leg workers; the Tier-1 caller is the gather node
- @entities/patterns/cpr-context-compression.md — scatter-gather state serialisation is a CPR concern when the gather step needs to persist intermediate scatter results
- @osint-wiki/concepts/scatter-gather-topology.md — cross-wiki primary; full LangGraph topology, conductor architecture history, and ~30 cross-references live there
- @concepts/kimi-agent-swarm-vs-claude-agent-teams.md — Kimi Swarm is unbounded hub fan-out; scatter-gather stays cost-bounded on CCC

## Raw Concept

CCC-side stub cross-routed from the OSINT primary. Scatter-gather is a LangGraph-canonical topology where a single state branches into N parallel paths (scatter) and the branches re-merge at an aggregation node (gather). The OSINT primary is the load-bearing write-up — extensive history, ~40 source links, LangGraph code references. This stub documents the Claude-Code-side manifestation.

## Narrative

### The pattern

```
       ┌─── worker A ───┐
input → ── worker B ───  → gather → output
       └─── worker C ───┘
```

- **Scatter** — a single task is decomposed into N independent subtasks dispatched to N workers in parallel.
- **Workers** — each operates with its own context; no inter-worker communication during the scatter phase.
- **Gather** — a single aggregation node merges the N outputs into a single result.

### CCC-side manifestations

1. **Parallel `Agent` tool calls.** When a Claude Code session emits multiple `Agent` invocations in a single message, the harness runs them in parallel. This is scatter-gather at the harness level — the parent agent is the gather node, the dispatched subagents are the workers.
2. **`Explore` agent for codebase-wide questions.** When a question spans many files, a single `Explore` agent often dispatches several internal sub-investigations and merges; scatter-gather at the agent level.
3. **Conductor cross-wiki routing.** A query against the federation (`@osint-wiki`, `@cybersecurity-wiki`, `@seo-wiki`, …) scatters per-wiki-alias and gathers into a single merged answer. The conductor's architecture is a scatter-gather application.

### Where it matters operationally

- **Context isolation.** Each scatter-leg has its own context window. The parent's context only sees the gathered output, not the scatter-leg trajectories. This is the load-bearing reason to scatter-gather a wide search rather than running it inline — it preserves the parent's working memory.
- **Cost.** N parallel scatter-legs means N times the per-leg input tokens. Worth it when the legs are independent and the gather is cheap; not worth it when the legs are dependent (would need sequential execution anyway).
- **Failure handling.** If one scatter-leg fails, the gather step needs an explicit strategy (drop the leg, retry, return partial). Default to drop + flag in the gathered output.

### When NOT to use it

- **Sequential dependencies.** If leg B needs leg A's output, scatter-gather is the wrong topology — use a pipeline.
- **Tiny tasks.** Spawning a subagent has overhead; for single-file reads, inline is faster.
- **State-sharing requirements.** If legs need to coordinate during execution, you're really doing a multi-agent conversation, not scatter-gather. Different pattern.

## Snippets

> Scatter-gather is the LangGraph-canonical topology where a single state branches into N parallel paths (scatter) and the branches re-merge at an aggregation node (gather).
[Source: @osint-wiki/concepts/scatter-gather-topology.md]
