---
title: "HAM-VLN — hierarchical agentic memory for zero-shot VLN"
type: source
tags: [source, arxiv, memory, vln, embodied, k236]
keywords: [2607.29600, HAM-VLN, decision-coupled, world graph, VLN-CE]
related:
  - concepts/decision-coupled-hierarchical-agentic-memory.md
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

- `@concepts/decision-coupled-hierarchical-agentic-memory.md`
- `@entities/tools/ham-vln.md`
- `@concepts/hierarchical-bounded-agent-memory.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation |
| **Author** | (arXiv metadata) |
| **arXiv** | 2607.29600 |
| **Pages** | 9 |
| **Retrieved** | 2026-08-03 |
| **Code/Availability** | No public HAM-VLN repo found (Phase-0) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.29600-ham-vln-harnessing-hierarchical-agentic-memory-f.pdf` |

## Narrative

Decision-coupled hierarchical agentic memory for zero-shot VLN. The same MLLM call that picks the next action also writes semantics (room/objects/progress/failures) into a depth-grounded world graph. Recent waypoints verbatim in a bounded window; older entries via retrieval (relevance, recency, salience) + one-hop topology — no extra LLM calls.

**Results:** >65% context length reduction; SR 61.0% VLN-CE R2R, 52.7% RxR, 79.7% HM3D-v2 ObjectNav — no training.

| Verdict | **ADOPT** decision-coupled write + hierarchical retrieve pattern (pairs K154/K230). **NO-GO** code. Embodied/VLN specifics → game-dev brief/stub later if needed |
