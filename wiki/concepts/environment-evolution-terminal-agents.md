---
title: "Environment evolution for terminal agents — off-policy curriculum (CCC K343)"
type: concept
tags: [concept, terminal-agents, environment-evolution, eval, curriculum, k343]
keywords: [2609.04128, off-policy evolution, difficulty scheduling, terminal bench, co-evolution limits]
related:
  - sources/arxiv-environment-evolution-terminal-agents-2609.04128.md
  - concepts/harness-as-eval-artifact.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-04_ccc-k342-k345-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-04
updated: 2026-09-04
---

## Relations

- `@sources/arxiv-environment-evolution-terminal-agents-2609.04128.md`
- `@concepts/harness-as-eval-artifact.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-04_ccc-k342-k345-sip-ready.md`

## Raw Concept

K343: terminal-agent training needs **environment curricula** that stay challenging as models improve — on-policy co-evolution alone stalls.

## Narrative

**Off-policy environment evolution** increases difficulty without requiring fresh on-policy rollouts each step; **generational scheduling** keeps learning signals alive as capability scales. Contrast with co-evolution that synthesizes near-frontier envs from weaknesses but generalizes poorly at scale.

CCC eval steal: treat environment difficulty schedules as harness artifacts to measure (pairs K334). Trainer **`wont_wire`**. No Terminal-X clone (null SPDX).

## Snippets

> "Evaluate the environment curriculum, not only terminal task pass rate." [Source: CCC K343 synthesis]
