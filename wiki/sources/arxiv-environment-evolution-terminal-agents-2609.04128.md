---
title: "Environment evolution for terminal agents — off-policy difficulty scheduling (CCC K343)"
type: source
tags: [source, arxiv, terminal-agents, environment-evolution, eval, training, k343]
keywords: [2609.04128, environment evolution, terminal agents, off-policy, co-evolution, difficulty scheduling]
related:
  - concepts/environment-evolution-terminal-agents.md
  - concepts/harness-as-eval-artifact.md
  - briefs/2026-09-04_ccc-k342-k345-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-04
updated: 2026-09-04
---

## Relations

- `@concepts/environment-evolution-terminal-agents.md`
- `@concepts/harness-as-eval-artifact.md`
- `@briefs/2026-09-04_ccc-k342-k345-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Environment Evolution for Terminal Agents |
| **arXiv** | 2609.04128 (2026-09-03) |
| **Code** | `UniPat-AI/Terminal-X` cited — **null SPDX** ~60MB → no clone |
| **Retrieved** | 2026-09-04 |

## Narrative

**Verdict: ADOPT eval-first — off-policy environment evolution beats on-policy co-evolution for terminal-agent training.**

On-policy co-evolution synthesizes environments near the learnable frontier from rollout weaknesses but limits generalization as models strengthen. **Environment evolution** incrementally increases difficulty **off-policy** and schedules evolved environments generation-by-generation for continuous learning signals. Three evolution directions derived from the multi-turn learning objective.

CCC policy: evaluate **environment curriculum** as harness artifact (pairs K334 HarnessDev, K294 SPADE executable envs). Trainer/runtime **`wont_wire`**. No Terminal-X clone (null SPDX).

## Snippets

> "Off-policy difficulty evolution + generational scheduling provides continuous learning signals as terminal agents scale." [Source: arXiv 2609.04128 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.04128-environment-evolution-for-terminal-agents.pdf` |
