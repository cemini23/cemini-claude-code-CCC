---
title: "Stratified harness evolution (CCC K313)"
type: concept
tags: [concept, harness-evolution, evaluation, stratification, held-out, k313]
keywords: [StarHarness, failure-mode stratification, proposer-hidden selection, generalization, frozen weights, interface repair]
related:
  - sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md
  - entities/tools/starharness.md
  - concepts/validation-ratchet-skill-evolution.md
  - concepts/evaluation-first-rubric-induction.md
  - concepts/vague-goal-self-evolution.md
  - sources/arxiv-autoscirub-rubric-induction-2608.31076.md
  - sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md
  - concepts/harness-as-eval-artifact.md
  - concepts/meta-harness-continual-improvement.md
  - sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md
  - sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md
  - concepts/bilevel-coordinated-reflection.md
  - sources/arxiv-bilevel-coordinated-reflection-2609.02750.md
maturity: draft
created: 2026-08-26
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md`
- `@entities/tools/starharness.md`
- `@concepts/evaluation-first-rubric-induction.md`
- `@concepts/vague-goal-self-evolution.md`
- `@sources/arxiv-autoscirub-rubric-induction-2608.31076.md`
- `@sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md`

## Raw Concept

The question: can you evolve a harness from a small task subset without overfitting it? Answer from StarHarness [Source: wiki/sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md]: yes — if search, selection, and evaluation are separated by construction.

## Narrative

Protocol (ADOPT):

1. **Freeze the model.** Evolve only prompt/task framing, tool interfaces, skills, MCP providers, subagents, loop config — never weights.
2. **Stratify by baseline failure mode.** Build a compact evolution pool that covers each distinct failure behavior, not a random sample.
3. **Separate the three task sets.** Proposer-*visible* search tasks; proposer-*hidden* selection tasks; held-out tasks for generalization. This is the eval-discipline answer to K162's external-eval contract and K281/K292/K298's "never optimize the pass criteria": a proposer that cannot see the selection set cannot game it.
4. **Accept few changes.** 4–12 accepted edits per environment produced 20–35 pp full-benchmark gains that persist on excluded tasks and transfer across GPT/Qwen without re-evolution.

What evolves is diagnostic too: the three recurring change classes — interface repair, environment conventions, operational knowledge — tell you *why* an agent fails in a new environment.

Guardrail for CCC: this pattern stays REFERENCE. Do not auto-evolve `.cursor/skills` (pairs K237/K298/K307); no closed rewrite of `## Verify`.

| Confidence | `[CONFIRMED]` — three enterprise benchmarks + cross-family transfer |
|------------|------------|

## Snippets

> "separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization" [Source: arXiv 2608.24804 abstract]

> "improves full-benchmark performance by 20–35 percentage points over the default harness, after 4–12 accepted changes per environment" [Source: arXiv 2608.24804 abstract]
