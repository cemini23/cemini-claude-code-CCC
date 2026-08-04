---
title: "ACEM — Agentic Cost Estimation Model"
type: source
tags: [source, arxiv, cost, estimation, planning, k243]
keywords: [2608.02582, Mohammad El-Ramly, RF, CF, HIS, UCP]
related:
  - concepts/acem-agentic-cost-estimation.md
  - concepts/token-economics-and-prompt-caching.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@concepts/acem-agentic-cost-estimation.md`
- `@concepts/token-economics-and-prompt-caching.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ACEM — Agentic Cost Estimation Model |
| **Author** | Mohammad El-Ramly |
| **arXiv** | 2608.02582 |
| **Type** | Conceptual (no installable code artifact) |
| **Related Zenodo book** | Different 24MB CC-BY guide — **not** ACEM code clone |
| **Retrieved** | 2026-08-04 |

## Narrative

Cost = LLM + HITL + infrastructure. Constructs:

| Construct | Role |
|-----------|------|
| **Revision Factor (RF)** | Iteration / rework multiplier |
| **Context Factor (CF)** | Context growth cost |
| **HITL Intensity Score (HIS-1..4)** | Human-in-loop burden tiers |

Maps UCP / Story / FP → tokens. Constants symbolic pending calibration.

| Verdict | **ADOPT** RF/CF/HIS costing vocabulary for agent project planning. **NO-GO** install. Do not claim ACEM code clone from Zenodo book. |
