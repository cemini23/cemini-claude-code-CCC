---
title: FinAcumen — financial experience memory harness (arXiv 2606.17642)
type: source
tags: [source, arxiv, finacumen, cross-wiki-route, finance, k117]
keywords: [2606.17642, finacumen, selective-retrieval, experience-memory]
related:
  - concepts/selective-experience-memory-harness.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/skillhone-continual-skill-decision-history.md
maturity: draft
read_status: read
created: 2026-06-17
updated: 2026-06-17
cross-wiki-route: "@osint-wiki/concepts/finacumen-financial-experience-memory.md"
---

## Relations

- `@concepts/selective-experience-memory-harness.md` — harness-pattern synthesis (CCC)
- `@concepts/agent-memory-stack-comparison.md` — experience memory peer
- `@concepts/skillhone-continual-skill-decision-history.md` — strategy + guard-rule lineage

Cross-wiki: `@osint-wiki/concepts/finacumen-financial-experience-memory.md` — finance domain canon (stub 2026-06-17).

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness |
| **Authors** | Guo et al. (BUPT, Queen Mary) |
| **arXiv** | 2606.17642v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.17642-finacumen-financial-multimodal-reasoning-via-sel.pdf` |
| **Retrieved** | 2026-06-17 |
| **Read status** | read (harness loop, τ-gated retrieval, benchmarks) |

## Narrative

**FinAcumen** — financial multimodal agent with **self-evolving experience memory harness**:

- Rollouts distill **strategies** (success) + **guard rules** (failure-derived caution)
- **τ-gated selective retrieval** — inject experience only above relevance threshold; explicit fallback when irrelevant
- Deterministic financial tool environment (numerical engine, grounded retrieval, answer gate)

**Benchmarks:** FinMMR, BizBench (SEC-NUM), FinMME, FinTMMBench — improves frozen 8B VLM vs finance-specialized models; approaches proprietary general models.

**Code:** paper cites `anonymous.4open.science/r/FinAcumen`; `CamelliaLilium/FinAcumen` on GitHub (MIT, 0★) — **unverified match** [NEEDS VERIFICATION 2026-06-17].

**CCC routing:** harness steal (τ-gated experience, guard rules); finance benchmarks → **osint-wiki**.

## Snippets

> "Retrieved experiences condition reasoning only when semantic relevance exceeds a calibrated threshold, while irrelevant memory is explicitly suppressed through a fallback mechanism."

> "Distilling successful strategies and failure-derived cautionary rules into a persistent memory bank."
