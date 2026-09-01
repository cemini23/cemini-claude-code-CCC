---
title: "AutoSciRub — evaluation-first automatic rubric induction (MIT REFERENCE clone, runtime not wired)"
type: entity
tags: [entity, tool, rubric-induction, evaluation-first, mit, reference, k331]
keywords: [2608.31076, AutoSciRub, zjunlp, rubric induction, criterion-level verification, executable rubric, ResearchClawBench, AstaBench]
related:
  - sources/arxiv-autoscirub-rubric-induction-2608.31076.md
  - concepts/evaluation-first-rubric-induction.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".local/adopts/AutoSciRub (REFERENCE clone; policy on concepts/evaluation-first-rubric-induction.md)"
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-autoscirub-rubric-induction-2608.31076.md`
- `@concepts/evaluation-first-rubric-induction.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K331 — AutoSciRub automatic rubric induction; MIT REFERENCE clone; runtime `wont_wire`.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| AutoSciRub framework | `zjunlp/AutoSciRub` | **MIT** (gh API SPDX 2026-09-01; 20 stars, pushed 2026-08-21) → **GO REFERENCE** clone `.local/adopts/AutoSciRub` (~2.5MB shallow, <500MB; LICENSE on disk) |

**Phase-0:** `scripts/adopt_k331_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

AutoSciRub induces a task-specific **executable rubric before** research execution and uses it to guide execution, criterion-level verification, and iterative revision. Gains transfer across harnesses with a frozen backbone (+2.08 pts across three backbone LLMs under fixed Codex; +2.95 pts across three agent harnesses under fixed DeepSeek-V4-Flash on ResearchClawBench; +16.8 pts on AstaBench E2E Discovery). See `@concepts/evaluation-first-rubric-induction.md`.

**Wire:** runtime **`wont_wire`** — no rubric-induction loop in the live CCC harness; policy is wired on the concept (evaluation-first rubric = control surface; **keep the external eval contract — do not rewrite `## Verify`**). Clone is REFERENCE only — reading reference for the rubric-induction + criterion-level-verification protocol.

| Wire | Target | Status |
|------|--------|--------|
| AutoSciRub runtime | none | `wont_wire` |
| Evaluation-first rubric policy | `.cursor/rules/ccc-k328-k332-phase1-wires.mdc` + shared policy §K331 | policy |
