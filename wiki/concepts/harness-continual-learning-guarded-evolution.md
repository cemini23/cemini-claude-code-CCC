---
title: Harness continual learning with guarded evolution
type: concept
tags: [concept, continual-learning, harness, meta-harness, k292]
keywords: [2608.19013, HCL, harness-level forgetting, Continual Evaluator]
related:
  - sources/arxiv-prime-agent-rlm-harness-2608.23552.md
  - concepts/rlm-continual-harness.md
  - sources/arxiv-harness-continual-learning-2608.19013.md
  - entities/tools/harness-continual-learning-hcl.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/versioned-model-harness-continual-adaptation.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - entities/tools/task-coevolve.md
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
  - entities/tools/prime-agent.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-20
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-harness-continual-learning-2608.19013.md`
- `@entities/tools/harness-continual-learning-hcl.md`
- `@sources/arxiv-prime-agent-rlm-harness-2608.23552.md`
- `@concepts/rlm-continual-harness.md`

## Raw Concept

How does an agent improve harness state (prompts, memory, skills, routing) across sessions without breaking earlier reliable behavior?

## Narrative

**HCL** treats harness components as versioned coupled state around a **frozen** foundation model. **Harness-level forgetting:** memory/skill/routing edits can break prior correct trajectories without weight changes.

**Guarded evolution:** Optimizer proposes; Evaluator commits only if current gain + historical retention budget + validity pass (pairs K162 — external eval contract, not closed self-rewrite).

**Cemini steal:** Version harness baselines (K273 ACM); measure retention sweeps when mutating `.cursor/rules`, skills, or MCP allowlists; no unattended auto-evolve of pass criteria.

| Verdict | **ADOPT** guarded harness evolution + retention budgets. **Policy only**. |
