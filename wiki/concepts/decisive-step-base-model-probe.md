---
title: "Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models (CCC K438)"
type: concept
tags: [concept, k438]
keywords: [2610.10478, k438]
related:
  - sources/arxiv-decisive-step-base-model-probe-2610.10478.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-08_ccc-k436-k440-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@sources/arxiv-decisive-step-base-model-probe-2610.10478.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-08_ccc-k436-k440-sip-ready.md`

## Raw Concept

K438: ADOPT eval-methodology — arXiv 2610.10478.

## Narrative

**Find the step where the repository flips, and probe the base model there.** NVIDIA. The problem: choosing which base checkpoint deserves an expensive agentic post-training round, before its agentic ability exists. End-to-end pass@K is unusable — untuned base models cannot drive a tool-use harness at all, so it reads near zero. Non-agentic coding benchmarks are worse: across ten base/post-trained pairs, **Spearman correlation with post-trained SWE-bench Verified pass@1 ranges from 0.830 (RepoBench XFirst) to −0.394 (HumanEval)** — a *negative* correlation, so the cheap proxy can rank backwards. The method: take a frontier model's **successful trajectory**, replay it, run the task's own tests after every code-changing step, and locate the **decisive step** — the first step whose cumulative patch flips the repo from failing to passing. That action is certified by the task's verifier, so it is a real action, not a gold patch. Three probes at that step: **Decisive-Action BPB** (probability mass on the certified action; ρ=0.964), **Patch MCQ** (distinguish it from verifier-rejected alternatives; ρ=0.903), and **prefix-conditioned pass@K** (sample continuations, accept any the tests pass; ρ=0.988 at K=16). **Two CCC-relevant pieces beyond the method.** (1) **A generic recipe**: any agentic benchmark with successful trajectories and a verifier can be converted into a base-model evaluation. (2) **A benchmark-validity finding**: the authors' **independent audit of 1,682 APTBench MCQs found questions whose designated correct option is incorrect or not uniquely correct** — a third instance of the K423 lesson, this time with the defect *inside the answer key*. Pairs K423 / K428 / `verifiable-deterministic-agent-benchmarking` / K424. **No repo.** Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.10478 locators." [Source: CCC K438 synthesis]
