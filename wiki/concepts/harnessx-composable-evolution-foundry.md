---
title: HarnessX — composable harness evolution foundry
type: concept
tags: [concept, harnessx, harness-evolution, aegis, k116]
keywords: [2606.14249, nine-dimensions, processor-hooks, seesaw-constraint]
related:
  - sources/arxiv-harnessx-composable-harness-foundry-2606.14249.md
  - concepts/code-as-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-harness-operational-definition.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md
  - sources/brief-k116-orchrm-harnessx-llm-as-code-prod-2026-06-16.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md
maturity: draft
created: 2026-06-16
updated: 2026-07-07
---

## Relations

- `@sources/arxiv-harnessx-composable-harness-foundry-2606.14249.md` — Darwin Agent Team paper
- `@concepts/code-as-agent-harness.md` — harness as serializable first-class object
- `@concepts/etclovg-harness-layers.md` — map D1–D9 to ETCLOVG layers
- `@concepts/continual-harness-online-self-improvement.md` — online refinement peer
- `@concepts/self-harness-model-specific-improvement-loop.md` — harness self-improvement
- `@concepts/failed-trajectory-harness-repair.md` — scoped harness edits
- `@concepts/agent-harness-operational-definition.md` — T1–T4 membership test

## Raw Concept

Can harnesses evolve composably from traces without entangled hand-edits?

## Narrative

**HarnessX** [TENTATIVE — no public code]: harness = typed configuration **H = (c₁…c₉)** over nine dimensions (model, context, memory, tools, sandbox, eval/reward, control/safety, observability, training bridge). **Processors** plug into eight hook points with singleton-group and ordering metadata.

**AEGIS evolution loop:** trace → Digester/Planner/Evolver (LLM proposes) → Critic → **deterministic gate** (seesaw: no regression on solved tasks). **Ensemble routing** forks variants per task cluster when global edit would regress subset.

**Operational mirror:** harness edits = RL actions in symbolic space; defenses against reward hacking, catastrophic forgetting, under-exploration.

**Results:** +14.5% avg across five benchmarks (up to +44%); co-evolution with cross-harness GRPO breaks scaffolding ceiling for weak models.

**CCC mapping (REFERENCE):**

| HarnessX dim | CCC surface |
|--------------|-------------|
| D2 context | `@concepts/tool-response-context-pruning-summarization.md` |
| D3 memory | claude-mem + wiki |
| D6 eval | `wiki_lint.py`, OpenSpec, verification gates |
| D7 control | hooks, permissions, Tier1/Tier2 |
| D8 observability | `wiki/log.md`, harness flaw records |

**Verdict:** REFERENCE taxonomy for harness flaw records + OpenSpec scoped edits; no install until open-source release.

## Snippets

> "Typed structure and deterministic gates determine what ships."

> "A candidate must not regress any previously solved task recorded in the trace store."
