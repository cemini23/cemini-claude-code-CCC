---
title: Agentic online-RL systems for self-evolving agents — the three-pillar stack
type: concept
tags: [concept, agentic-rl, self-evolving, online-rl, harness, k139]
keywords: [ATDP, agent trajectory data protocol, data proxy, evolution control plane, self-evolving agents, AReaL, 2607.01120]
related:
  - sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md
  - entities/tools/areal.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k139-agentic-online-rl-self-evolving-2026-07-07.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - sources/arxiv-large-cancer-assistant-lca-2607.06531.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/toolverse-gust-turn-aware-agentic-rl.md
  - sources/arxiv-toolverse-long-horizon-mcp-rl-2607.15660.md
  - concepts/harness-native-agent-rl-training.md
  - sources/arxiv-openforgerl-harness-native-training-2607.21557.md
maturity: draft
created: 2026-07-07
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md` — K139 provenance (Ant Group position paper)
- `@entities/tools/areal.md` — AREAL2.0 scoped instantiation
- `@concepts/continual-harness-online-self-improvement.md` — harness-only sibling; this page adds the **weight-update** loop
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix consumes trajectory data; ATDP is the missing protocol

## Raw Concept

K139 arXiv **2607.01120**: self-evolving agents at enterprise scale are bottlenecked by **agentic online RL systems**, not RL algorithms. Three co-designed pillars required.

## Narrative

### The three pillars

| Pillar | What it fixes | CCC analogue (today) |
|--------|---------------|----------------------|
| **ATDP** — Agent Trajectory Data Protocol | Logs are *observable* but not *learnable*; no step-granular RL signal across heterogeneous paradigms | `wiki/log.md`, claude-mem traces — debug-grade, **not** step-signal-grade |
| **Data proxy** | No governed path from real workloads → training substrate | egress-fi raw archive + ingest ritual (governance layer; no training) |
| **Evolution control plane** | No auto-decision on *when* to update weights vs evolve harness | Manual HarnessFix + skill-promotion gates (`@concepts/skill-vetting.md`) |

### Two evolution axes

The control plane must choose between **updating policy weights** (RL fine-tune) and **evolving the in-context harness** (prompts, tools, memory). CCC deliberately runs **only the harness axis** on laptop/prod — no local RL. This page marks the weight axis as **WATCH**.

### What CCC steals now [TENTATIVE]

1. **ATDP discipline** — even without training, log trajectories with **step-level outcome signals** (which tool call advanced the goal), not just prompt/completion dumps. Sharpens HarnessFix root-cause and completion-gate diagnosis.
2. **Trigger from statistics** — decide harness edits from **trajectory statistics** (repeated failure signatures), not vibes — pairs with `@concepts/failed-trajectory-harness-repair.md`.
3. **Governed substrate** — keep the egress-fi archive + ingest provenance as the "data proxy" governance layer if a weight-side loop is ever built on `cemini-prod`.

4. **Impermeable routing (K150)** — evolution control plane must keep **orchestration routing invariant** when policy weights swap — pairs with `@concepts/algorithmic-impermeability-model-agnostic-orchestration.md`.

### Where it sits in ETCLOVG

Spans **Observability** (ATDP), **Lifecycle** (evolution control plane), and **Governance** (data proxy) — see `@concepts/etclovg-harness-layers.md`.

| Verdict | **REFERENCE / WATCH** — architecture target; laptop stance = harness axis only, no local RL |

## Snippets

> "There is no unified agent evolution control plane with automatic triggering that decides … when to update policy model weights or evolve the in-context harness."
> — [Source: arxiv-2607.01120 abstract, retrieved 2026-07-07]
