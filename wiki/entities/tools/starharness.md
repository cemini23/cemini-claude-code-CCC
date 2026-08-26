---
title: "StarHarness — stratified harness evolution by ServiceNow (REFERENCE clone, trainer not wired)"
type: entity
tags: [entity, tool, harness-evolution, mit, reference, k313]
keywords: [2608.24804, StarHarness, ServiceNow, MIT, ITBench, EnterpriseOps-Gym, AutomationBench]
related:
  - sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md
  - concepts/stratified-harness-evolution.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/ccc-k310-k314-phase1-wires.mdc"
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@sources/arxiv-starharness-stratified-harness-evolution-2608.24804.md`
- `@concepts/stratified-harness-evolution.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K313 — StarHarness stratified harness evolution; MIT REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| StarHarness framework | `ServiceNow/StarHarness` | **MIT** (gh API SPDX 2026-08-26) → **GO REFERENCE** clone `.local/adopts/StarHarness` (24MB shallow, <500MB; LICENSE on disk) |

**Phase-0:** `scripts/adopt_k313_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

Evolves environment-specific harnesses with frozen weights: prompt/task framing, tool interfaces, skills, MCP providers, subagents, loop config. Stratified pool by baseline failure behavior; proposer-visible search vs proposer-hidden selection vs held-out. +20–35 pp on three enterprise benchmarks after 4–12 accepted changes; transfers across GPT/Qwen without re-evolution.

**Wire:** trainer/runtime `wont_wire` — no auto-evolution loop in CCC, and **do not** evolve `.cursor/skills` unattended (pairs K237/K298/K307). The repo is a reading reference for the stratified protocol (`@concepts/stratified-harness-evolution.md`).
