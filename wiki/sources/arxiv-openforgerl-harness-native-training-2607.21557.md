---
title: "OpenForgeRL — train harness-native agents in any environment"
type: source
tags: [source, arxiv, harness, rl, training, k214]
keywords: [2607.21557, OpenForgeRL, harness-native, veRL, Claude Code, Codex]
related:
  - concepts/harness-native-agent-rl-training.md
  - concepts/code-as-agent-harness.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/measurement-gated-agent-harness-optimization.md
  - sources/brief-k210-k214-traceable-euclid-acm-openforge-2026-07-24.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- `@concepts/harness-native-agent-rl-training.md`
- `@concepts/code-as-agent-harness.md`
- `@concepts/agentic-online-rl-self-evolving-systems.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | OpenForgeRL: Train Harness-native Agents in Any Environment |
| **Author** | Xiao Yu, Baolin Peng, et al. (Columbia / Dartmouth / MSR) |
| **arXiv** | 2607.21557 |
| **Pages** | 25 |
| **Retrieved** | 2026-07-24 |
| **Code** | no official OpenForgeRL repo at Phase-0; cites `THUDM/slime` Apache (~328MB) — **NO-GO** clone this batch (prefer pattern; slime optional later) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.21557-openforgerl-train-harness-native-agents-in-any-e.pdf` |

## Narrative

Inference harnesses (Claude Code, Codex, OpenClaw) aren't natively expressible in standard SFT/RL stacks. OpenForgeRL: proxy records harness model calls as RL data + K8s per-rollout containers. Train in the real harness. **ADOPT** harness-native training idea; **NO-GO** install until SPDX'd official artifact.
