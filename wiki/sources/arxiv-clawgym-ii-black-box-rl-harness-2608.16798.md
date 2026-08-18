---
title: "ClawGym II — black-box RL on agent harness"
type: source
tags: [source, arxiv, agent-harness, reinforcement-learning, black-box-rl, serving-proxy, k287]
keywords: [2608.16798, ClawGym II, black-box RL, serving proxy, prefix tree, PPO, GRPO, mix-harness, OpenClaw, Claude Code]
related:
  - concepts/black-box-rl-opaque-harness-optimization.md
  - entities/tools/clawgym-ii.md
  - concepts/scaffold-over-tool-interface.md
  - concepts/versioned-model-harness-continual-adaptation.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@concepts/black-box-rl-opaque-harness-optimization.md`
- `@entities/tools/clawgym-ii.md`
- `@concepts/scaffold-over-tool-interface.md` — K262 scaffold > interface
- `@concepts/versioned-model-harness-continual-adaptation.md` — K263 versioned model-harness pairs

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ClawGym II: Exploring Black-Box RL on Agent Harness |
| **arXiv** | 2608.16798 |
| **Authors** | Huatong Song, Fei Bai, Ming Yang, Renyuan Li, Jia Deng, Jujie He, Zhange Zhang, Daixuan Cheng, Yan Xing, Qi Yun, Xuxing Chen, Danyang Li, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Mingjie Tang, Ji-Rong Wen (Renmin University of China + IQuest Research) |
| **Code** | none public (no ClawGym II SPDX repo) |
| **Retrieved** | 2026-08-18 |

## Narrative

A unified **black-box RL framework** for stable, scalable policy optimization of general agents through complex harnesses. It addresses three challenges: (1) scalable/stable execution infrastructure, (2) efficient policy optimization from fragmented black-box traces, (3) extensibility across heterogeneous harnesses.

**Core techniques:**

1. **Sandbox-based execution infrastructure** — each task environment + harness is encapsulated in a temporary sandbox provisioned on demand and destroyed on completion, isolating every rollout and enabling large-scale concurrency.
2. **Serving proxy at the model boundary** — policy optimization is decoupled from opaque harness execution; a proxy intercepts every model call while the harness retains its native execution logic.
3. **Prefix trees** — captured calls are organized into a prefix tree to recover reliable multi-turn trajectories from fragmented, forked, redundant traces, and both critic-based PPO and critic-free GRPO are adapted to optimize over the recovered tree structure.
4. **Training–inference consistency** — black-box token-in-token-out + token-level importance-sampling rollout correction mitigate biases between inference and training engines.
5. **Mix-harness training** — each task–harness pair is a training instance; rollouts from heterogeneous harnesses (OpenClaw + Claude Code) jointly optimize one model.

**Results.** From Qwen3-30A3B, black-box RL produces ClawII-OC-30A3B (OpenClaw) and ClawII-CC-30A3B (Claude Code), improving Pass@1 on PinchBench by +11.71/+17.28 and ClawGym-Bench by +9.98/+14.81 respectively, stable over 200–400 optimization steps. Mix-harness training matches or surpasses single-harness counterparts; consistent gains also on JobBench and OfficeQA.

| Verdict | **ADOPT** decouple policy optimization from opaque harness via serving proxy; rebuild prefix trees from captured model calls; PPO/GRPO over trees; mix-harness joint training; sandbox per rollout. No public ClawGym II SPDX repo → **policy only**. Pairs K281 AutoDesign, K262 scaffold>interface, K263 versioned model-harness pairs. |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.16798-clawgym-ii-exploring-black-box-rl-on-agent-harne.pdf` |
