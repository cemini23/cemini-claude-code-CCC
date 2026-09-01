---
title: "Evaluation-first rubric induction — induce the rubric before execution (CCC K331)"
type: concept
tags: [concept, rubric-induction, evaluation-first, research-agents, external-eval-contract, criterion-level-verification, k331]
keywords: [AutoSciRub, executable rubric, rubric skeleton, criterion-level verification, intermediate scientific specification, external eval contract, do not rewrite verify, 2608.31076]
related:
  - sources/arxiv-autoscirub-rubric-induction-2608.31076.md
  - entities/tools/autoscirub.md
  - concepts/validation-ratchet-skill-evolution.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/stratified-harness-evolution.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/evidence-tree-rubric-supervision.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-autoscirub-rubric-induction-2608.31076.md`
- `@entities/tools/autoscirub.md`
- `@concepts/validation-ratchet-skill-evolution.md`
- `@concepts/seagym-self-evolving-harness-evaluation.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/agent-rubrics-self-correction.md`
- `@concepts/evidence-tree-rubric-supervision.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

The question: autonomous research agents revise outputs without an explicit specification of the scientific requirements the task entails. How do we make implicit success criteria explicit *before* execution, and keep the pass criteria out of the agent's control? Answer from AutoSciRub (K331) [Source: wiki/sources/arxiv-autoscirub-rubric-induction-2608.31076.md]: **evaluation-first** — induce a task-specific **executable rubric** before research execution, then use it to guide, verify criterion-by-criterion, and revise.

## Narrative

Open-ended research tasks hide objectives, methods, evidence, and success conditions. The result: plausible-looking reports that omit essential analyses, use inappropriate procedures, or make unsupported claims. Rubrics in existing benchmarks are **post-hoc evaluation instruments**; AutoSciRub makes the rubric an **intermediate scientific specification** that connects task interpretation → execution → verification → iterative revision. **A reliable research agent learns to evaluate before improving.**

**Two stages:**

1. **Automatic Rubric Induction** — decompose the instruction into atomic scientific goals (skeleton); ground each goal in relevant literature + task-visible data; synthesize a task-specific executable rubric: each criterion links to goals and specifies data sources, required experiments/analyses, metrics/comparisons, expected evidence artifacts, and a satisfaction condition.
2. **Rubric-Guided Iterative Revision** — a verifier checks each criterion (satisfied / remaining evidence gap) and returns targeted feedback (missing experiment, incomplete comparison, unsupported claim); revise; stop when all criteria pass or the budget is reached. 35/40 tasks pass within three revisions; one revision is a strong default cost/performance trade-off.

**Evidence it works (transferable with frozen backbone):** +2.08 pts (3 backbones, fixed Codex harness) and +2.95 pts (3 harnesses, fixed DeepSeek-V4-Flash) on ResearchClawBench; +16.8 pts on AstaBench E2E Discovery. Rubric-guided revision ≈ **2.7×** cumulative improvement of rubric-free self-refinement (2.05 vs 0.77) — repeated rewriting alone does not explain the gain. Limitation: it operationalizes an identified direction; it does **not** fix a missing scientific framing (scientific-core coverage 3.35 → 3.07).

**CCC policy lines (wire `policy_wired`):**

- **Open-ended research hides success criteria. The evaluation-first rubric is the control surface** — induce it before execution, and use it to guide, verify, and revise (pairs `@concepts/validation-ratchet-skill-evolution.md` K324: keep updates only when validation improves).
- **Keep the external eval contract; do not let the agent rewrite pass criteria** — **do not rewrite `## Verify`** (pairs `@concepts/seagym-self-evolving-harness-evaluation.md` K162 verification hierarchy, `@concepts/stratified-harness-evolution.md` K281/K313 hidden selection eval, `@concepts/evidence-tree-rubric-supervision.md` K289 evidence-tree eval, `@concepts/agent-rubrics-self-correction.md` K97 rubric loops).
- Criterion-level verification identifies **specific omissions** instead of a holistic score — the diagnostic granularity CCC wants for report/artifact revision.

Entity `entities/tools/autoscirub.md`: runtime `wont_wire`, REFERENCE clone only (MIT).

| Confidence | `[CONFIRMED]` — results reported in the paper; policy is CCC synthesis |
|------------|------------|
