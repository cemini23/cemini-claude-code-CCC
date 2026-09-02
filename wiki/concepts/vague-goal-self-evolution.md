---
title: "Vague-goal self-evolution — goal interpretation is the missing search axis (CCC K332)"
type: concept
tags: [concept, self-evolution, vague-goal, goal-operationalization, hidden-eval, harness-self-edit, misevolution, policy, k332]
keywords: [Aspire, vague-goal-driven self-evolution, goal interpretation, proxy self-eval, retained improvement, harness evolution, high-blast HITL, 2608.31111]
related:
  - sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md
  - concepts/skill-misevolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/stratified-harness-evolution.md
  - concepts/validation-ratchet-skill-evolution.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
  - concepts/harness-as-eval-artifact.md
  - sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-01
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md`
- `@concepts/skill-misevolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@concepts/seagym-self-evolving-harness-evaluation.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/validation-ratchet-skill-evolution.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

The question: with only a vague capability goal ("improve at research") and no agent-visible task, metric, or decomposable reward, can an agent decide *what* to learn, build its own learning signals, and retain real capability growth? Answer from Aspire (K332) [Source: wiki/sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md]: agents close the train/edit loops, but **goal interpretation is the missing search axis** — weight gains are sparse and unstable, proxies fail hidden eval, and continued search erases earlier gains.

## Narrative

Explicit-task self-evolution (PostTrainBench, LaMDAgent, SEAL) begins after a human has operationalized a broad capability into a fixed task-level objective: the agent searches over *how*, not *what*. **Vague-goal self-evolution** expands the decision space: the agent must also operationalize the goal — diagnose gaps, decompose sub-goals, build training/validation signals. "Vague" = a broad capability direction not yet operationalized, not ambiguity. Evaluation items must stay **hidden**; gains on an agent-built proxy are not transferable growth.

**Evidence (30-cell adaptive-feedback protocol + RQ3):**

- **Producing a trained checkpoint is common; producing an above-base score is rare.** 30 → 28 evaluated → 21 eligible → **1 retained improvement**. Local gains can stay below base; a positive within-lineage slope can be recovery from training-induced regression (math 0.79 → 1.75 → 2.38, base 17.86).
- **More search ≠ better search; continued search can erase earlier gains** (Terra math 20.10 → 2.78 → 18.17). Checkpoint selection and rollback are necessary; blind continuation yields near-zero finals (0.159 / 2.540 / 0).
- **Proxy self-eval fails hidden eval.** Luna specialized a harness to an 8-item self-built checklist (8/8) that recast mechanism/formula questions as study-design problems — hidden-eval task macro 19.32 vs 28.64 reference. **Local training success ≠ transferable capability.**
- **Strongest evolved harness < engineered reference.** All three valid successor harnesses (frozen Qwen3.5-4B weights) stay below Qwen-Agent (27.22 / 20.76 / 19.32 vs 28.64). One-step harness generation; not recursive self-improvement.
- **Vague goals redirect search toward goal interpretation** and yield lower outcomes than explicit-task references (RQ1).

**CCC policy lines (wire `policy_wired`):**

- **Goal interpretation is the missing search axis** — for any vague-goal work, define what/how/verify before search; judge progress against the **base model**, not only the previous checkpoint (pairs `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` K162, `@concepts/seagym-self-evolving-harness-evaluation.md` K117/K162 eval environment).
- **Treat harness self-edit as high-blast HITL (misevolution)** — never auto-evolve `.cursor/skills`; keep retention checks on held-out packs before trusting learned state (pairs `@concepts/skill-misevolution.md` K237, `@concepts/validation-ratchet-skill-evolution.md` K324 ratchet, `@concepts/stratified-harness-evolution.md` K313 hidden selection + frozen weights).
- No public SPDX → **no clone**; runtime `wont_wire` (project page only).

| Confidence | `[CONFIRMED]` — results reported in the paper; policy is CCC synthesis |
|------------|------------|
