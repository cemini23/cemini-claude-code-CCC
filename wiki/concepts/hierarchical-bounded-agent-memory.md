---
title: Hierarchical bounded agent memory — short / mid / long with eviction
type: concept
tags: [concept, memory, context, multi-agent, long-horizon, harness, k154]
keywords: [2607.07666, ensemble qsp, scratchpad, mid-term state, eviction, bounded context, three-layer]
related:
  - sources/arxiv-ensemble-qsp-hierarchical-memory-2607.07666.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/dual-representation-agent-memory.md
  - concepts/mcp-context-optimization.md
  - entities/patterns/cpr-context-compression.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - sources/brief-k154-hierarchical-bounded-agent-memory-2026-07-13.md
  - briefs/2026-07-13_ccc-handoff-memory-search-trustx-ingest.md
  - concepts/agentic-context-management-lifecycle.md
  - concepts/memory-poisoning-write-execute-forget-lifecycle.md
  - sources/arxiv-memsecbench-memory-poisoning-lifecycle-2607.27080.md
  - concepts/decision-coupled-hierarchical-agentic-memory.md
  - sources/arxiv-ham-vln-hierarchical-agentic-memory-2607.29600.md
  - entities/tools/ham-vln.md
  - concepts/experiential-working-memory-coupling.md
maturity: draft
created: 2026-07-13
updated: 2026-08-26
---

## Relations

- `@sources/arxiv-ensemble-qsp-hierarchical-memory-2607.07666.md` — K154 Ensemble QSP (AstraZeneca)
- `@concepts/decision-coupled-hierarchical-agentic-memory.md` — K236 HAM-VLN decision-coupled write

## Raw Concept

K154 arXiv **2607.07666** — long-horizon multi-agent runs fail when context grows unbounded. **Three explicit layers + eviction** keep injected state ~constant while preserving continuity.

## Narrative

### Three layers → Cemini mapping [TENTATIVE]

| Layer | QSP implementation | CCC surface |
|-------|-------------------|-------------|
| **Short-term** | Turn window + scratchpad for exact facts | `hot.md`, in-thread working notes, subagent return payloads |
| **Mid-term** | Capped JSON project state (301 token median) | ROADMAP open decisions, OpenSpec state, git branch metadata |
| **Long-term** | Handbook + retrieval on demand | `wiki/`, claude-mem, egress-fi archives |

### Eviction discipline

Completed subtasks **evicted** from mid-term state — do not accumulate stale checklist items across weeks. Pairs with `@entities/patterns/cpr-context-compression.md` and `@concepts/channel-fracture-cross-agent-memory-delivery.md` (prove delivery at receiver).

### Domain note

QSP/pharma workflow is **off-domain** for prod trading bots — adopt **memory architecture only**.

| Verdict | **REFERENCE** — bounded hierarchical memory pattern for multi-session agent projects |

### K236 complement (2026-08-03)

HAM-VLN adds **decision-coupled writes**: the same turn that acts also updates the world graph — no separate memory LLM call. Pairs short/mid/long layers here with `@concepts/decision-coupled-hierarchical-agentic-memory.md`.

## Snippets

> "Mid-term project state: median 301 tokens, max 4,050, across 104 runs."
> — [Source: arxiv-2607.07666 abstract, retrieved 2026-07-13]
