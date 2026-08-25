---
title: "Prime Agent — self-improving RLM harness by Prime Intellect (REFERENCE, not a Cursor//route replacement)"
type: entity
tags: [entity, tool, rlm, harness, mit, reference, k309]
keywords: [2608.23552, prime-agent, PrimeIntellect-ai, MIT, arc-agi-3, continual harness]
related:
  - sources/arxiv-prime-agent-rlm-harness-2608.23552.md
  - concepts/rlm-continual-harness.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-prime-agent-rlm-harness-2608.23552.md`
- `@concepts/rlm-continual-harness.md`
- `@concepts/harness-continual-learning-guarded-evolution.md` (K292 retention discipline)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K309 — Prime Agent RLM harness; MIT REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Prime Agent harness | `PrimeIntellect-ai/prime-agent` | **MIT** → **GO REFERENCE** clone `.local/adopts/prime-agent` (~31MB, <500MB) |

**Phase-0:** `scripts/adopt_k309_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

Persistent IPython REPL (RLM), Continual Harness across trajectories, recursive subagents, Agents View. ARC-AGI-3 RHAE Best@1 30% → 95.5% (paper). Standardized execution/recovery/verification so harness failures ≠ model failures.

## Phase-1

Runtime **`wont_wire`**: **do not replace Cursor / `/route` / claude-ds with Prime Agent.** HITL required before any skill/prompt self-write (K162/K237); any future trial must include K292-style retention checks on held-out packs. Atto steal brief written (`briefs/2026-08-25_k300-k309-atto-prime-agent-aid-guard-steal.md`).
