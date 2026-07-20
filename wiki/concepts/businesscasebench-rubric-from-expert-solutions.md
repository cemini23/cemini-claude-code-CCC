---
title: BusinessCaseBench — expert-solution rubrics for subjective knowledge work
type: concept
tags: [concept, evaluation, rubric, llm-as-judge, knowledge-work, k193]
keywords: [2607.16057, BusinessCaseBench, Standard scoring, Complete Answer, case method]
related:
  - sources/arxiv-businesscasebench-knowledge-work-2607.16057.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@sources/arxiv-businesscasebench-knowledge-work-2607.16057.md` — provenance
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — eval discipline
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — LLM judges advisory
- `@concepts/multi-agent-evidence-artifact-layers.md` — typed intermediates before narrative
- `@concepts/gatekeeper-layered-agent-evaluation.md` — layered eval peer

## Raw Concept

K193 BusinessCaseBench: convert expert instructor solutions into **equally-weighted checklist rubrics**; LLM-as-judge with human validation; report Standard (partial credit) vs Complete Answer (all criteria).

## Narrative

### Steal (ADOPT methodology)

1. For subjective agent outputs, write the **expert reference first**, then explode into checklist criteria — do not invent rubrics from vibes.
2. Report two scores: partial-credit vs all-criteria — Complete Answer is the harsh bar for "ship it".
3. Keep LLM-judge below execution tests on the K162 hierarchy; spot-check with humans when stakes are money/LIVE.
4. Benchmark artifact itself: **NO-GO** (no public package at Phase-0).

### Cemini map

| Use | Example |
|-----|---------|
| CCC briefs | Rubric from prior accepted brief before judging new ones |
| Poker | Strategy writeup vs solver/expert checklist |
| TipDrop | Operator playbook criteria for Discord posts |

| Verdict | **ADOPT** rubric-from-expert-solution pattern; **NO-GO** install |

## Snippets

> "reference solutions are transformed into equally-weighted checklist rubrics"
> — [Source: arxiv-2607.16057 Fig.1 pipeline]
