---
title: "ClawGym II — black-box RL on agent harness (RUC / IQuest)"
type: entity
tags: [entity, tool, agent-harness, reinforcement-learning, black-box-rl, policy-only, k287]
keywords: [k287, ClawGym II, serving proxy, prefix tree, PPO, GRPO, mix-harness]
related:
  - sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md
  - concepts/black-box-rl-opaque-harness-optimization.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md`
- `@concepts/black-box-rl-opaque-harness-optimization.md`

## Raw Concept

Phase-0 entity for CCC K287 — ClawGym II (black-box RL framework).

## Narrative

Authors: Renmin University of China + IQuest Research. A unified black-box RL framework for optimizing general agents through opaque harnesses. **No public ClawGym II SPDX repo → policy only** (no clone). Core: sandbox-per-rollout execution infrastructure, a **serving proxy** at the model boundary, **prefix-tree** trajectory recovery, PPO/GRPO over the tree, training–inference consistency, and **mix-harness** joint training. Validated on OpenClaw + Claude Code (Qwen3-30A3B → +9.98/+14.81 Pass@1 on ClawGym-Bench).

Steal: decouple policy optimization from opaque harness execution; intercept model calls at a serving proxy; rebuild prefix trees; mix-harness joint training. **`policy_wired`** — pattern only, no runtime wiring.

**Phase-0:** `scripts/adopt_k287_phase0.sh`
