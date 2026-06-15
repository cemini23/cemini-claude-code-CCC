---
title: Learning What to Remember — multi-factor agentic memory (arXiv 2606.12945)
type: source
tags: [source, arxiv, agentic-memory, forgetting, longmemeval, k115]
keywords: [2606.12945, multi-factor-memory, blind-forgetting, borgeagent]
related:
  - concepts/multi-factor-agentic-memory-value-model.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/claude-mem.md
  - concepts/three-cache-architecture.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- `@concepts/multi-factor-agentic-memory-value-model.md` — CCC synthesis
- `@concepts/agent-memory-stack-comparison.md` — memory stack peers
- `@entities/tools/claude-mem.md` — adopted session memory
- `@concepts/three-cache-architecture.md` — wiki vs claude-mem vs stash layering

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory |
| **Authors** | Chen et al. |
| **arXiv** | 2606.12945v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.12945-learning-what-to-remember-a-cognitively-grounded.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (value function, blind vs oracle, LongMemEval-S) |

## Narrative

**Multi-factor memory value** V(m) = Σ wᵢ fᵢ(m) with seven factors: emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, usage history. Single scalar drives **encoding depth**, **forget risk**, and **retrieval rank**. Weights learned via gradient-free optimizer (CMA-ES) on downstream objective — here gold-evidence retention under fixed budget (API-free proxy).

**Methodological pitfall — oracle vs blind forgetting:**

| Regime | Goal relevance signal | Similarity-only retention | Multi-factor learned |
|--------|----------------------|---------------------------|----------------------|
| **Oracle** (peeks at eval question at consolidation) | query-defined | ≈0.98 gold | no advantage possible |
| **Blind** (session topic only at consolidation) | query-agnostic | near-chance | **0.770±0.011** vs 0.657 uni-factor |

479 usable **LongMemEval-S** cases; CPU-only experiments, no API calls. Cites open-source **BorgeAgent** substrate (`github.com/zhibao-dev/BorgeAgent`, 2026) — **repo 404 on GitHub 2026-06-15** [NEEDS VERIFICATION 2026-06-15].

**CCC relevance:** blind-forgetting eval discipline for claude-mem compaction; multi-factor value vs pure similarity/recency. REFERENCE until BorgeAgent repo verified.

## Snippets

> "Similarity-to-query is only defined at retrieval time — but the forgetting decision is made earlier, at consolidation, when the future query is unknown."

> "In the blind regime … learned multi-factor value retains 0.770±0.011 of gold evidence versus 0.657 (uni-factor)."
