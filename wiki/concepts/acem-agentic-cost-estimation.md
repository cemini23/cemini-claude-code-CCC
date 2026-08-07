---
title: ACEM — agentic cost estimation vocabulary (K243)
type: concept
tags: [concept, cost, estimation, planning, hitl, k243]
keywords: [2608.02582, ACEM, RF, CF, HIS, UCP, Story points, function points]
related:
  - sources/arxiv-acem-agentic-cost-estimation-2608.02582.md
  - concepts/token-economics-and-prompt-caching.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
  - concepts/anytime-valid-agent-eval-stopping.md
  - entities/tools/av-aivat.md
  - sources/arxiv-av-aivat-anytime-valid-agent-eval-2608.06362.md
maturity: draft
created: 2026-08-04
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-acem-agentic-cost-estimation-2608.02582.md` — K243 provenance
- `@concepts/token-economics-and-prompt-caching.md` — token/cost discipline peer

## Raw Concept

How should agent project planners estimate total cost beyond raw LLM tokens?

## Narrative

K243 **ACEM** (arXiv **2608.02582**, Mohammad El-Ramly): conceptual cost model.

**Total cost = LLM + HITL + infrastructure**

### Constructs (ADOPT vocabulary)

| Construct | Meaning |
|-----------|---------|
| **Revision Factor (RF)** | Iteration / rework multiplier on base estimate |
| **Context Factor (CF)** | Context growth cost driver |
| **HITL Intensity Score (HIS-1..4)** | Human-in-loop burden tiers |

Maps traditional sizing (UCP / Story / FP) → token estimates. Constants symbolic — pending operator calibration.

Pairs `@concepts/token-economics-and-prompt-caching.md` for runtime token discipline; ACEM adds **planning-phase** vocabulary for agent projects with HITL and infra.

| Verdict | **ADOPT** RF/CF/HIS vocabulary for planning. **NO-GO** install (conceptual; no code artifact). |

## Dead Ends

- **Claiming Zenodo CC-BY book as ACEM code** — different artifact; do not conflate
- **Using uncalibrated constants as budgets** — symbolic until operator calibration
