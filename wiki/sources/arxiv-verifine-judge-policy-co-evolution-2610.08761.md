---
title: "VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning (CCC K435)"
type: source
tags: [source, arxiv, k435]
keywords: [2610.08761, k435]
related:
  - concepts/judge-policy-co-evolution.md
  - briefs/2026-10-07_ccc-k431-k435-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@concepts/judge-policy-co-evolution.md`
- `@briefs/2026-10-07_ccc-k431-k435-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning |
| **arXiv** | 2610.08761 (2026-10) |
| **Retrieved** | 2026-10-07 |

## Narrative

**Verdict: ADOPT pattern.**

**VeriFine — the judge is not fixed infrastructure; it is a co-evolving component.** NVIDIA. The premise is precise: **self-improving policies continually expose new failure patterns, which changes what their judges must be able to verify.** A **static judge becomes the bottleneck** as the policy improves — once the policy approaches the judge's effective verification boundary, feedback degrades into **reward hacking, distribution shift, and outright performance loss**. Meanwhile the training data goes stale: as earlier scenarios get solved, the distribution fills with well-solved samples and the learning signal thins. VeriFine answers with **two coupled loops**: a **Policy Improvement Loop** uses a **reference-free rubric judge** to diagnose recurring failures, build an **adaptive curriculum**, and optimise the policy; when progress plateaus, a **Judge Improvement Loop** activates and **selectively queries human guidance on informative failure cases**, refining the judge through **coactive calibration** — humans and agents resolve disagreements and converge, **human as participant rather than infallible oracle**. The revised judge then drives the next round of data selection and policy optimisation. Concrete protocol: boundary checks every 150 steps; rubric revision **keeps the dimensions and changes sub-rubrics and examples**; revisions accepted on Pearson/MAE; human review requested when average correlation improvement stays under 0.2 for 10+ iterations. Demonstrated on driving and robot navigation under RL and SFT. **CCC relevance:** this is the strongest answer yet to the *who grades the grader* problem, and it is the **constructive counterpart to K428 CLIFT** — CLIFT makes the verifier cheap and transferable and *frozen*; VeriFine says a frozen judge eventually throttles the system and **the verifier must co-evolve, with a small, targeted human channel** rather than a broad one. It is the *selective* human channel that makes this affordable. Pairs K424 (no LLM judge) / K423 (representation) / `@concepts/validation-ratchet-skill-evolution.md` / `@concepts/agent-rubrics-self-correction.md` / K416 YouRA. **No repo.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify." [Source: arXiv 2610.08761 (retrieved 2026-10-07)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.08761-verifine-scaling-verification-for-self-improveme.pdf` |
