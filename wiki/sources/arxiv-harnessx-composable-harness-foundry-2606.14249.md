---
title: HarnessX — composable evolvable agent harness foundry (arXiv 2606.14249)
type: source
tags: [source, arxiv, harnessx, aegis, harness-evolution, k116]
keywords: [2606.14249, harnessx, nine-dimensions, co-evolution, grpo]
related:
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/code-as-agent-harness.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/etclovg-harness-layers.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- `@concepts/harnessx-composable-evolution-foundry.md` — CCC synthesis
- `@concepts/code-as-agent-harness.md` — harness as first-class object
- `@concepts/continual-harness-online-self-improvement.md` — online harness refinement peer
- `@concepts/etclovg-harness-layers.md` — ETCLOVG layer mapping for nine dimensions

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry |
| **Authors** | Darwin Agent Team |
| **arXiv** | 2606.14249v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.14249-harnessx-a-composable-adaptive-and-evolvable-age.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (nine dimensions, AEGIS, benchmarks) |

## Narrative

**HarnessX** — foundry for composable, adaptive, evolvable harnesses. Typed **processor** bundles on eight hook points; **nine behavioral dimensions** (c₁…c₉):

| Dim | Domain |
|-----|--------|
| D1 | Model selection |
| D2 | Context assembly |
| D3 | Memory management |
| D4 | Tool ecosystem |
| D5 | Execution environment |
| D6 | Evaluation and reward |
| D7 | Control and safety |
| D8 | Observability |
| D9 | Training bridge |

**AEGIS** — trace-driven evolution: Digester → Planner → Evolver → Critic + deterministic acceptance gate (seesaw: no regression on solved tasks). **Operational mirror** maps harness edits to RL in symbolic space. **Ensemble routing** forks harness variants per task cluster when edits help subset but regress others.

**Harness–model co-evolution:** shared replay buffer; cross-harness GRPO trains model while harness evolves.

**Benchmarks:** ALFWorld, GAIA, WebShop, τ³-Bench, SWE-bench Verified — average **+14.5%** (up to **+44.0%**); largest gains on weakest baselines.

**Code:** "will be open-sourced in a future release" — **no public repo** 2026-06-16.

## Snippets

> "Harness configurations are states, typed edits are actions, and execution traces plus verifier scores constitute feedback."

> "LLM subagents explore, hypothesize, and propose; typed structure and deterministic gates determine what ships."
