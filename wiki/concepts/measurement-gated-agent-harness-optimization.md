---
title: Measurement-gated agent harness optimization (FlashRT pattern)
type: concept
tags: [concept, harness, optimization, measurement, coding-agent, k200]
keywords: [2607.18171, FlashRT, chain-of-program, IR, bench gate]
related:
  - sources/arxiv-flashrt-agent-harness-realtime-2607.18171.md
  - concepts/code-as-agent-harness.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
  - concepts/harness-native-agent-rl-training.md
  - sources/arxiv-openforgerl-harness-native-training-2607.21557.md
maturity: draft
created: 2026-07-21
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-flashrt-agent-harness-realtime-2607.18171.md` — provenance
- `@concepts/code-as-agent-harness.md` — harness peer
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — measurement > self-score
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — eval discipline peer

## Raw Concept

K200 FlashRT: guide coding agents from a simple reference to optimized deploys via IR + validation + **measurement-gated** iterate. Repo 404 — pattern only.

## Narrative

### Steal (ADOPT)

1. Optimization tasks: require dependency IR before rewrite.
2. Sequential validate of IR before speculative transforms.
3. Accept a candidate only if **bench metrics** improve target (latency/throughput/cost).
4. Pair with K162 — no closed self-refine on pass criteria without human gate.
5. FlashRT code: **NO-GO** (GitHub 404 at Phase-0).

| Verdict | **ADOPT** measurement-gated harness checklist; **NO-GO** install |

## Snippets

> "iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop"
> — [Source: arxiv-2607.18171]
