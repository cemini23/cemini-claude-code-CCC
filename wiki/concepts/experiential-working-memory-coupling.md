---
title: "Experiential–Working Memory coupling (CCC K314)"
type: concept
tags: [concept, memory, rsi, skill-selection, validation-gated, long-horizon, k314]
keywords: [Recuris, experiential memory, working memory, Meta-Agent, skill patch, failure localization, bounded evolution]
related:
  - sources/arxiv-recuris-em-wm-memory-evolution-2608.24876.md
  - entities/tools/recuris.md
  - concepts/hierarchical-bounded-agent-memory.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@sources/arxiv-recuris-em-wm-memory-evolution-2608.24876.md`
- `@entities/tools/recuris.md`
- `@concepts/hierarchical-bounded-agent-memory.md`

## Raw Concept

The question: how should an agent use accumulated experience without drowning current decisions in history? Answer from Recuris [Source: wiki/sources/arxiv-recuris-em-wm-memory-evolution-2608.24876.md]: split the memory — Working Memory holds structured task state and *picks* skills from Experiential Memory.

## Narrative

Three moves CCC adopts as pattern:

1. **EM–WM split.** EM stores procedures/skills; WM tracks live task progress. Skill invocation is grounded in WM state, not in full-history similarity — this fixes misaligned skill picks and keeps context bounded.
2. **Execution as evidence.** The coupling produces structured traces that localize a failure to a specific memory component (wrong pick vs stale skill vs missing skill). Diagnosis stops being vibes.
3. **Validation-gated Skill Memory patches.** A fixed Meta-Agent proposes localized patches; admission requires passing validation; the loop stays bounded. Gains: +17.8 pp on τ²-Bench for GPT-5.6 Sol, +32.2 pp on longest-horizon tasks, six failure modes cut 20–86%.

Guardrails (pairs K237/K298/K307 and K309): **HITL before any skill self-write**; validation gate before patch admission; runtime `wont_wire`. Bounded memory shape also pairs `@concepts/hierarchical-bounded-agent-memory.md`.

| Confidence | `[CONFIRMED]` — 35/37 model–benchmark pairs improved across ten models |
|------------|------------|

## Snippets

> "Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history" [Source: arXiv 2608.24876 abstract]

> "localized, validation-gated updates to Skill Memory that reshape execution and yield new evidence, forming a bounded recursive memory-evolution loop" [Source: arXiv 2608.24876 abstract]
