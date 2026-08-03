---
title: Agentic Context Management — five-primitive lifecycle
type: concept
tags: [concept, context, memory, cost, lifecycle, k213]
keywords: [2607.21503, ACM, architecting, ingesting, scoping, anticipating, compacting]
related:
  - sources/arxiv-agentic-context-management-2607.21503.md
  - concepts/mcp-context-optimization.md
  - concepts/self-compacting-adaptive-context.md
  - concepts/tool-response-context-pruning-summarization.md
  - concepts/hierarchical-bounded-agent-memory.md
  - sources/brief-k210-k214-traceable-euclid-acm-openforge-2026-07-24.md
  - concepts/decision-coupled-hierarchical-agentic-memory.md
  - concepts/exact-stateful-tokenization-agentic-serving.md
  - sources/arxiv-ham-vln-hierarchical-agentic-memory-2607.29600.md
  - sources/arxiv-toktier-exact-stateful-tokenization-2607.29678.md
maturity: draft
created: 2026-07-24
updated: 2026-08-03
---

## Relations

- `@sources/arxiv-agentic-context-management-2607.21503.md`
- `@concepts/mcp-context-optimization.md`
- `@concepts/self-compacting-adaptive-context.md`
- `@concepts/exact-stateful-tokenization-agentic-serving.md` — K238 TokTier TTFT under high cache hits

## Raw Concept

K213 ACM: manage context as lifecycle — architect / ingest / scope / anticipate / compact+consolidate — across org scopes. Not "just add a vector store."

## Narrative

### Steal (ADOPT)

1. Map CCC stack: architect (CLAUDE.md/lazy-tool) · ingest (claude-mem/hot.md) · scope (project domains) · anticipate (session ritual) · compact (K124 rubric).
2. Prefer managed lifecycle over unbounded history dumps.
3. No product install — checklist only.

| Verdict | **ADOPT** ACM five-primitive checklist |

### K236 / K238 additions (2026-08-03)

- **Compact+consolidate:** K236 decision-coupled writes avoid separate memory passes; K238 flags append-heavy continuations where tokenization dominates TTFT under high cache hits.
- See `@concepts/decision-coupled-hierarchical-agentic-memory.md`, `@concepts/exact-stateful-tokenization-agentic-serving.md`.
