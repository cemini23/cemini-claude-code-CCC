---
title: Decision-coupled hierarchical agentic memory
type: concept
tags: [concept, memory, hierarchical, vln, k236, k154, k230]
keywords: [2607.29600, HAM-VLN, world graph, decision-coupled write, retrieval]
related:
  - sources/arxiv-ham-vln-hierarchical-agentic-memory-2607.29600.md
  - entities/tools/ham-vln.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - concepts/agentic-context-management-lifecycle.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- `@sources/arxiv-ham-vln-hierarchical-agentic-memory-2607.29600.md` — K236 HAM-VLN
- `@concepts/hierarchical-bounded-agent-memory.md` — K154 three-layer peer
- `@concepts/reconstructive-agent-memory-vs-verbatim-replay.md` — K230 reconstruct peer
- `@concepts/agentic-context-management-lifecycle.md` — lifecycle compaction peer

## Raw Concept

Can the same model call that decides the next action also write structured memory — without extra LLM round-trips?

## Narrative

K236 HAM-VLN (arXiv **2607.29600**): the MLLM call selecting the next navigation action **also writes** semantics (rooms, objects, progress, failures) into a depth-grounded world graph. Recent waypoints stay verbatim in a bounded window; older entries retrieved by relevance, recency, salience + one-hop topology. **No extra LLM calls** for memory maintenance. >65% context reduction; strong zero-shot VLN/ObjectNav without training.

### Cemini steal (ADOPT)

Pairs K154 hierarchical bounded memory and K230 reconstruct-before-inject:

| Mechanism | CCC mapping |
|-----------|-------------|
| Decision-coupled write | Subagent return payloads + hot.md updates on same turn as action |
| Bounded verbatim window | Short-term layer in `@concepts/hierarchical-bounded-agent-memory.md` |
| Retrieval + topology | claude-mem / wiki retrieval; one-hop `@relations` |
| No extra memory LLM calls | Avoid separate "summarize memory" passes unless advantage-gated (K231) |

Embodied/VLN domain is OOD — **pattern only**. No public code.

| Verdict | **ADOPT** decision-coupled write + hierarchical retrieve. **NO-GO** HAM-VLN runtime |

## Snippets

> Same MLLM call that picks next action also writes semantics into depth-grounded world graph.
> — [Source: arxiv-2607.29600, retrieved 2026-08-03]
