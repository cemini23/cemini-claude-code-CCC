---
title: "StepGuard — step-level guardrails with scalable supervision (CCC K312)"
type: source
tags: [source, arxiv, guardrails, agent-safety, step-level, grpo, k312]
keywords: [2608.24777, StepGuard, StepGen, Balance-GRPO, AgentDojo, ASR, pre-execution check]
related:
  - concepts/step-level-tool-guardrails.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@concepts/step-level-tool-guardrails.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety–Utility Balancing |
| **arXiv** | 2608.24777 [cs.AI] |
| **Authors** | Zhijie Zheng, Yu Li, Chen Qian, Yuqian Fu, Yanwei Fu, Lu Sheng, Jing Shao, Dongrui Liu (Shanghai AI Laboratory AgentDoG Team + Beihang/Fudan/RUC/KAUST) |
| **Code** | `github.com/zheng977/StepGuard` exists but **no LICENSE file** (`license: null` via API 2026-08-26) → **NO-GO clone** |
| **Retrieved** | 2026-08-26 |

## Narrative

StepGuard is a step-level guard model that does two jobs most guardrails split: it checks a candidate tool action **before execution**, and it audits completed trajectories. Training solves the two classic blockers:

1. **StepGen data engine** — synthesizes multi-step trajectories where safe and unsafe variants share the same context prefix and diverge only at the designated risky step; benign look-alike trajectories reuse similar tools so the guard cannot cheat on tool identity.
2. **Balance-GRPO** — reweights normalized advantages by the observed accuracy gap between safe and unsafe actions, directly attacking over-defense (utility loss) and under-defense (missed attacks).

Results: highest average accuracy among open-weight guard models, comparable to GPT-5.4; as a runtime guard on AgentDojo and AgentDyn it cuts mean attack success rate by **77.3%** while mean utility drops only **2.8 points**.

For CCC this is the runtime shape of "gate the step, not just the final answer": pairs K239 preview-before-effect (`@concepts/execution-fidelity-irreversible-agent-invariants.md`) and K264 accept/reject/escalate. The safety–utility dial is the honest part — guards are tuned, not free.

| Verdict | **ADOPT policy**: check candidate tool actions before execute + audit trajectories; keep an explicit safety–utility balance. No SPDX clone → no repo adopted. Runtime trainer `wire_status: wont_wire`; policy `policy_wired`. Cybersec steal brief written. |
|---------|---------|

## Snippets

> "We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed." [Source: arXiv 2608.24777 abstract]

> "StepGen constructs matched safe and unsafe trajectories that share the same execution prefix and diverge at a designated risky step." [Source: arXiv 2608.24777 §1]

> "StepGuard reduces mean ASR by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 points." [Source: arXiv 2608.24777 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.24777-stepguard-learning-step-level-guardrails-with-sc.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
