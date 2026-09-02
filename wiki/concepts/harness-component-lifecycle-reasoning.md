---
title: "Harness component lifecycle reasoning — teardown order + execution verify (CCC K336)"
type: concept
tags: [concept, harness-lifecycle, component-teardown, dependency-graph, eval-axis, execution-verify, policy, k336]
keywords: [2609.01600, CordisBench, component lifecycle, teardown order, scale degradation, deterministic semantics, dependency propagation, plugin harness]
related:
  - sources/arxiv-cordisbench-component-lifecycle-2609.01600.md
  - concepts/cross-process-plugin-agent-harness.md
  - concepts/harness-as-eval-artifact.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-cordisbench-component-lifecycle-2609.01600.md`
- `@concepts/cross-process-plugin-agent-harness.md`
- `@concepts/harness-as-eval-artifact.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

The question: when a dynamic agent harness installs, reconfigures, and removes plugins, does the model predict the correct final state? Answer from CordisBench (K336) [Source: wiki/sources/arxiv-cordisbench-component-lifecycle-2609.01600.md]: **teardown order matters**, LLM reasoning **does not scale**, and **deterministic execution verify** beats model anticipation when a formal lifecycle spec exists.

## Narrative

**Lifecycle = dependency + order.** Dynamic harnesses are not static tool lists. Components have install/configure/interact/teardown phases; **dependencies propagate state**; **teardown order** can change the final configuration even when the same set of components is removed. Agents that only track "what is installed" miss ordering effects.

**Scale degradation.** CordisBench (1,200 questions; 528 executable against Cordis reference semantics) shows models succeed on **small** systems (≈2 components) but **degrade as interactions scale** (toward ≈32 components). Lifecycle reasoning is a combinatorial dependency problem — not parametric common sense.

**Execution verify > LLM anticipation.** When Cordis provides **deterministic reference semantics**, execution matches on all 528 executable questions. Policy: if dependencies are formalized, **compute or execute-verify** teardown outcomes — do not trust the model to verbally predict final state at scale.

**Pairs K327 Logos:** isolate plugins as processes; durable state in append-only transcript; resume with **no repeated effect** at tool-call-cycle boundaries — lifecycle eval complements process-isolation policy (plugin fault domains vs dependency teardown correctness).

**CCC policy lines (wire `policy_wired`):**

- Add **component lifecycle + teardown order** as an eval axis for dynamic harness/plugin changes.
- Prefer **deterministic semantics + execution verify** over LLM lifecycle reasoning when a formal spec exists.
- Paper cites GitHub/HF artifacts — **no public SPDX found at Phase-0** → **WATCH** until license verified; **no clone this wave**; eval runtime `wont_wire`.

| Confidence | `[CONFIRMED]` — benchmark results from the paper; SPDX watch `[NEEDS VERIFICATION 2026-09-02]` |
|------------|------------|

## Snippets

> "Teardown order changes final state — lifecycle reasoning is an ordering problem." [Source: wiki/sources/arxiv-cordisbench-component-lifecycle-2609.01600.md — K336 policy line]

> "When dependencies are formal, compute or execute-verify instead of trusting model lifecycle anticipation at scale." [Source: wiki/sources/arxiv-cordisbench-component-lifecycle-2609.01600.md — K336 policy line]
