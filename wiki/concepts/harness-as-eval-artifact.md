---
title: "Harness as eval artifact — Creation + Evolution stages (CCC K334)"
type: concept
tags: [concept, harness-evolution, evaluation, creation, evolution, integration-verify, policy, k334]
keywords: [2609.01437, HarnessDev, harness creation, harness evolution, eval artifact, held-out transfer, state never fires, integration verify]
related:
  - sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/stratified-harness-evolution.md
  - concepts/vague-goal-self-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
  - concepts/harness-component-lifecycle-reasoning.md
  - concepts/meta-harness-continual-improvement.md
  - concepts/environment-evolution-terminal-agents.md
  - sources/arxiv-environment-evolution-terminal-agents-2609.04128.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-02
updated: 2026-09-04
---

## Relations

- `@sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/vague-goal-self-evolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

The question: when agents "improve themselves," should we score task answers or the harness that produces them? Answer from HarnessDev (K334) [Source: wiki/sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md]: score the **runnable harness** as the eval artifact — Creation and Evolution are distinct, unstable, and require integration verify.

## Narrative

**Shift the eval unit.** Traditional agent benchmarks grade terminal outputs. HarnessDev grades **harness infrastructure**: orchestration loops, tool interfaces, memory/state hooks, and whether the harness **actually runs** the intended control flow. A pretty harness on paper that never triggers its state machine is a failure mode, not a partial success.

**Two stages (distinct skills):**

| Stage | Agent task | Failure mode |
|-------|------------|--------------|
| **Creation** | Build a runnable harness from a task spec | Scaffolds exist but lag human references on code/search |
| **Evolution** | Iterate harness from behavioral feedback | Visible gains unstable; partial held-out transfer; model-dependent |

**Evidence lines:**

- **Visible feedback ≠ held-out transfer** — evolution loops show improvement on the feedback channel that does not fully survive held-out evaluation.
- **Executor swap negates gains** — harness evolution tied to one model may not transfer when the executor changes.
- **State defined ≠ state fired** — memory and state components appear in generated code but **never execute** at runtime; static review misses this; **integration verify required** (execution traces, required-hook coverage).

**CCC policy lines (wire `policy_wired`):**

- **Evaluate harness infrastructure, not only answers** — pairs `@concepts/meta-harness-optimization-hitl-eval-contract.md` K281 (external eval contract), `@concepts/stratified-harness-evolution.md` K313 (hidden selection tasks), `@concepts/vague-goal-self-evolution.md` K332 (proxy self-eval failure).
- **Creation and Evolution are separate capabilities** — do not assume one-shot harness generation implies stable evolution.
- **Never auto-evolve `.cursor/skills`** — harness self-edit remains high-blast HITL (pairs K162 bounded self-refinement, K237 misevolution).
- Project page only — **no public SPDX** → no clone; runtime `wont_wire`.

| Confidence | `[CONFIRMED]` — benchmark results from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Evaluate the runnable harness — not the terminal task output alone." [Source: wiki/sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md — K334 policy line]

> "State components defined in code often never fire at runtime — integration verify is mandatory." [Source: wiki/sources/arxiv-harnessdev-harness-creation-evolution-2609.01437.md — K334 policy line]
