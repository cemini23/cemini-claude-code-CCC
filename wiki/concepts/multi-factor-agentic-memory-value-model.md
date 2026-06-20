---
title: Multi-factor agentic memory value model — blind vs oracle forgetting
type: concept
tags: [concept, agentic-memory, forgetting, evaluation, k115]
keywords: [2606.12945, blind-forgetting, longmemeval, borgeagent]
related:
  - sources/arxiv-multi-factor-agentic-memory-2606.12945.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/claude-mem.md
  - concepts/three-cache-architecture.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md
  - concepts/executable-user-memory-user-as-code.md
maturity: draft
created: 2026-06-15
updated: 2026-06-20
---

## Relations

- `@sources/arxiv-multi-factor-agentic-memory-2606.12945.md` — arXiv provenance
- `@concepts/agent-memory-stack-comparison.md` — mem0/Hermes/claude-mem peers
- `@entities/tools/claude-mem.md` — compaction target for blind-forgetting eval
- `@concepts/three-cache-architecture.md` — stash / claude-mem / wiki tiers
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — delivery vs retention axis

## Raw Concept

How should agents decide what to forget at consolidation when the future query is unknown?

## Narrative

**Seven-factor value function** V(m) drives encode depth, forget risk, and retrieval with **learned weights** (CMA-ES on retention objective) [2606.12945].

**Critical eval discipline — blind vs oracle:**

| Mistake | Oracle regime | Realistic blind regime |
|---------|---------------|------------------------|
| Score goal relevance using **held-out eval question** at consolidation | Similarity wins (≈98% gold) | **Invalid** — peeks at future |
| Score using **session topic only** at consolidation | — | Multi-factor wins (0.770 vs 0.657) |

**Steal-from:** when benchmarking claude-mem compaction or wiki hot.md rotation, use **blind** consolidation signals — never tune forgetting with query leakage.

**BorgeAgent** cited as open substrate (`zhibao-dev/BorgeAgent`) — **404 on GitHub 2026-06-15** → REFERENCE only.

**Verdict:** **REFERENCE** — eval methodology + multi-factor framing; no install until repo + license verified.

## Snippets

> "Oracle forgetting measures retrieval, not retention — a real agent has not seen the evaluation question at consolidation time."

> "Reliability, emotional intensity, and self/user relevance dominate learned weights; query-time goal similarity is correctly down-weighted for forgetting."
