---
title: Deterministic PRM guidance in discrete diffusion (cross-route stub)
type: source
tags: [source, arxiv, cross-wiki, reward-modeling]
keywords: [2609.35472, PRM, process reward model, discrete diffusion, grader calibration, image-gen cross-route]
related:
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/conformal-self-verification-certified-bank.md
maturity: draft
read_status: skimmed
cross-wiki-source: "@image-gen-wiki/sources/arxiv-2609-35472-prm-discrete-diffusion-routed.md"
created: 2026-09-29
updated: 2026-10-07
---

## Relations

- `@concepts/orchestration-reward-modeling-orch-rm.md`
- `@image-gen-wiki/sources/arxiv-2609-35472-prm-discrete-diffusion-routed.md` — cross-wiki primary

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Deterministic PRM guidance in discrete diffusion |
| **arXiv** | 2609.35472 |
| **Type** | Cross-wiki stub (routed inbound from `image-gen-wiki`) |
| **URL** | https://arxiv.org/abs/2609.35472 |
| **Retrieved** | 2026-09-30 (stub); primary ingest 2026-09-29 |
| **Read-status** | skimmed — CCC-relevant part only |

## Narrative

arXiv:2609.35472 asks why **deterministic process-reward-model (PRM) guidance** underperforms in
discrete diffusion reasoning. The subject matter is image generation, so the primary page lives in
`image-gen-wiki`. This CCC stub exists only for the part that transfers.

**CCC-relevant claim `[TENTATIVE]`:** a PRM applied deterministically as a guidance signal degrades
results. The failure is not that the reward model is wrong. A fixed, non-adaptive application of its
scores at every step removes the model's ability to trade the reward against other constraints.
Pairs with `@concepts/orchestration-reward-modeling-orch-rm.md` and with the eval-reliability line
(K392 low-cost behavioral assays, K407 judge variance).

**CCC transfer `[CONFIRMED 2026-10-07]` — corroborated by a second independent source.** Do not wire
a reward model or grader as an **unconditional per-step control signal** in an agent harness. Gate
it, bound its influence, or use it only at selection boundaries.

The upgrade, and its basis: this claim sat under a dated needs-verification tag (2026-09-30) until
it crossed the 7-day lint threshold on 2026-10-07. The K428 ingest that same day supplied the second
source from an **unrelated domain**. CLIFT blends its verifier signal into per-step rewards
**asymmetrically — it can only add evidence on top of the judge baseline, never subtract** — and
states plainly that this is **what prevents the reward-collapse failure of earlier linear blends**.
Two independent settings — diffusion guidance, and web-agent RL — converge on the same prescription:
**bound the grader's influence; never apply it unconditionally.**

Confidence note, kept explicit: this is `[CONFIRMED]` by *two independent sources*, not by CCC
testing. Neither source is a Claude Code harness, so the claim is well-supported as a principle and
still **personally untested here**. If CCC ever wires a grader into a loop, the load-bearing test is
whether a bounded/asymmetric blend beats an unconditional one on the same task.

## Snippets

> "Relevant to harness eval design and grader calibration, not image-gen build track." [Source: CCC
> routing note, image-gen ingest 2026-09-29]

## Dead Ends

- **Not a runtime wire.** No CCC tool, hook, or policy derives from this page. The stub prevents the
  cross-wiki link from dangling; it does not propose adoption.
