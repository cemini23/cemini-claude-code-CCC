---
title: "Step-level tool guardrails (CCC K312)"
type: concept
tags: [concept, guardrails, agent-safety, pre-execution, safety-utility, k312]
keywords: [StepGuard, StepGen, Balance-GRPO, pre-execution check, trajectory audit, ASR, over-defense]
related:
  - sources/arxiv-stepguard-step-level-guardrails-2608.24777.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@sources/arxiv-stepguard-step-level-guardrails-2608.24777.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`

## Raw Concept

The question: where should an agent guardrail look? Answer from StepGuard [Source: wiki/sources/arxiv-stepguard-step-level-guardrails-2608.24777.md]: at **each candidate tool action before execution**, plus post-hoc trajectory audits — not only at the final answer.

## Narrative

Trajectory-level guards see damage after it happens; final-answer checks miss harmful intermediate steps entirely. StepGuard's contributions CCC adopts as policy:

1. **Gate the step, not only the run.** Check the exact tool call against its context before it executes; audit full trajectories afterwards.
2. **Context-matched supervision.** Safe and unsafe training variants share a prefix and diverge only at the risky step — so the guard learns decision boundaries, not surface patterns. Benign tool-look-alikes stop it from keying on tool identity.
3. **The safety–utility dial is explicit.** Balance-GRPO reweights advantages by the observed safe/unsafe accuracy gap; guards are *tuned* between over-defense and under-defense, and that tuning is a real cost (ASR −77.3% for ~2.8 utility points).

Pairs K239 preview-before-effect (`@concepts/execution-fidelity-irreversible-agent-invariants.md`): preview is the human-facing form of the same gate; StepGuard is the automated form.

Leftover implementation (propose-only): a StepGuard-style PreToolUse hook policy for CCC — HITL later; no trainer runtime (`wont_wire`). Cybersec steal brief written.

| Confidence | `[CONFIRMED]` — AgentDojo + AgentDyn evals vs no-guard baseline |
|------------|------------|

## Snippets

> "a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed" [Source: arXiv 2608.24777 abstract]

> "reduces mean ASR by 77.3% … while mean utility drops by only 2.8 points" [Source: arXiv 2608.24777 abstract]
