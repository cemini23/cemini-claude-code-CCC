---
title: Selective experience memory harness — τ-gated strategy retrieval
type: concept
tags: [concept, experience-memory, harness, cross-wiki-route, k117]
keywords: [2606.17642, finacumen, tau-gated, guard-rules]
related:
  - sources/arxiv-finacumen-experience-memory-harness-2606.17642.md
  - concepts/skillhone-continual-skill-decision-history.md
  - concepts/skill-vetting.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/mcp-pre-trade-diligence-boundary.md
  - concepts/executable-user-memory-user-as-code.md
maturity: draft
created: 2026-06-17
updated: 2026-06-20
---

## Relations

- `@sources/arxiv-finacumen-experience-memory-harness-2606.17642.md` — FinAcumen paper (finance domain)
- `@concepts/skillhone-continual-skill-decision-history.md` — decision history + evidence
- `@concepts/skill-vetting.md` — suppress low-quality retrieved guidance
- `@concepts/agent-memory-stack-comparison.md` — experience vs reflection memory
- `@concepts/mcp-pre-trade-diligence-boundary.md` — finance harness boundary (osint peer)

Cross-wiki: `@osint-wiki/concepts/finacumen-financial-experience-memory.md`

## Raw Concept

When should prior episode experience condition the current agent run?

## Narrative

**Selective experience memory harness** [TENTATIVE — 2606.17642 FinAcumen]: accumulate **strategies** (success patterns) + **guard rules** (failure caution) from trajectories; at inference retrieve only if semantic relevance **> τ**; else explicit **fallback** (no memory injection).

Contrasts with undifferentiated reflection banks that retrieve weakly related guidance and amplify hallucination risk.

**CCC steal (domain-agnostic):**

- Wiki skill iteration: store guard rules from failed ingests separately from success templates
- τ-gate before injecting claude-mem observations into parent context on unrelated tasks
- Pair with `@concepts/skill-vetting.md` probe quality

**Finance benchmarks / FinAcumen install:** → `@osint-wiki/concepts/finacumen-financial-experience-memory.md`

**Verdict:** REFERENCE pattern; FinAcumen code unverified on GitHub.

## Snippets

> "Irrelevant memory is explicitly suppressed through a fallback mechanism."

> "Distilling successful strategies and failure-derived cautionary rules into a persistent memory bank."
