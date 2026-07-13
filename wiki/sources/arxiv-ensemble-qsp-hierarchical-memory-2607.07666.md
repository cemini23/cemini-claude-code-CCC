---
title: Ensemble QSP — hierarchical memory for long-horizon multi-agent modeling (2607.07666)
type: source
tags: [source, arxiv, memory, multi-agent, long-horizon, k154]
keywords: [2607.07666, ensemble qsp, hierarchical memory, astra zeneca, qsp, bounded context, eviction]
related:
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/subagent-orchestration.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - sources/brief-k154-hierarchical-bounded-agent-memory-2026-07-13.md
maturity: draft
read_status: read
created: 2026-07-13
updated: 2026-07-13
phase_0_verdict: "REFERENCE 2026-07-13 — AstraZeneca QSP domain off prod; steal three-layer capped memory + eviction for long-horizon harness"
---

## Relations

- `@concepts/hierarchical-bounded-agent-memory.md` — harness synthesis (domain-agnostic)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling |
| **Authors** | Shivendra G. Tewari, Holly Kimko — AstraZeneca Systems Medicine |
| **arXiv** | 2607.07666 |
| **Domain** | Quantitative systems pharmacology (QSP) — **clinical/pharma off-domain** for Cemini prod bots |
| **Code** | **None** at Phase-0 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.07666-2607-07666v1-a-hierarchical-memory-architecture.pdf` |
| **Retrieved** | 2026-07-13 |

## Narrative

**Ensemble QSP** — PI agent + five specialist sub-agents for autonomous QSP workflows.

### Three-layer hierarchical memory

| Layer | Contents | Bound |
|-------|----------|-------|
| **Short-term** | Recent turns + capped scratchpad (facts, file structure) | 4–20 turns; scratchpad ≤20k chars (specialists), ≤8k (PI) |
| **Mid-term** | Structured JSON project state | Median **301 tokens**, max 4,050 across 104 runs |
| **Long-term** | Domain handbook, checklists, source-paper retrieval | On demand |

**Eviction:** completed work evicted → injected context stays bounded across sessions.

| Verdict | **REFERENCE** — steal bounded three-layer memory for long-horizon agent harness; QSP domain not adopted |

## Snippets

> "Because every layer is explicitly capped and completed work is evicted, the injected mid-term state stays bounded as a project runs across sessions."
> — [Source: arxiv-2607.07666, retrieved 2026-07-13]
