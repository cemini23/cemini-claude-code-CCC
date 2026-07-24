---
title: Harness-native agent RL training (OpenForgeRL pattern)
type: concept
tags: [concept, harness, rl, training, k214]
keywords: [2607.21557, OpenForgeRL, proxy recording, K8s rollouts]
related:
  - sources/arxiv-openforgerl-harness-native-training-2607.21557.md
  - concepts/code-as-agent-harness.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/measurement-gated-agent-harness-optimization.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k210-k214-traceable-euclid-acm-openforge-2026-07-24.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-openforgerl-harness-native-training-2607.21557.md`
- `@concepts/code-as-agent-harness.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`

## Raw Concept

K214: train agents **inside** real inference harnesses via call-recording proxy + isolated rollouts — don't simplify the harness away for RL.

## Narrative

### Steal (ADOPT)

1. When improving Claude Code/Cursor agents with RL/SFT: preserve harness semantics (tools, multi-process state).
2. Prefer measurement-gated evals in the real harness (pairs K200/K169).
3. No official OpenForgeRL SPDX artifact — **NO-GO** install; slime optional later under size budget.

| Verdict | **ADOPT** harness-native training checklist; **NO-GO** install |
