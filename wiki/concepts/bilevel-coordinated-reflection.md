---
title: "Bilevel coordinated reflection — orchestrator–worker game + verification (CCC K339)"
type: concept
tags: [concept, multi-agent, reflection, game-theory, orchestrator, k339]
keywords: [2609.02750, bilevel coordination, decomposition quality, reflection bounds, external verification]
related:
  - sources/arxiv-bilevel-coordinated-reflection-2609.02750.md
  - concepts/stratified-harness-evolution.md
  - concepts/experiential-working-memory-coupling.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-bilevel-coordinated-reflection-2609.02750.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/experiential-working-memory-coupling.md`
- `@concepts/role-specialization-model-multi-tool-coordination.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

K339 formalizes orchestrator–worker coordination as a bilevel game and reflection as bounded memory updates — with explicit role for **external verification**.

## Narrative

**Decomposition quality controls coordination slack.** Poor task decomposition widens the gap between orchestrator intent and worker equilibrium; treat decomposition as a harness artifact to evaluate, not an invisible prompt detail.

**Reflection ≠ proof.** Free-form reflection has finite-time upper bounds with tight worst-case behavior — pair reflection loops with **external verification** (execution checks, held-out eval) per K162 hierarchy. Pairs K313 stratified evolution and K314 EM–WM memory coupling.

**Wire:** `policy_wired`; no clone. Runtime `wont_wire`.

## Snippets

> "Prefer external verification in the reflection loop — textual self-critique alone is not a reliability boundary." [Source: CCC K339 synthesis]
