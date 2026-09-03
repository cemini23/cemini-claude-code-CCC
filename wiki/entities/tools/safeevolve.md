---
title: "SafeEvolve — harness-policy safety co-evolution (REFERENCE clone, runtime not wired)"
type: entity
tags: [entity, tool, safety, harness-evolution, mit, reference, k340]
keywords: [2609.02786, SafeEvolve, MaoPopovich, MIT, safety alignment, skill bank]
related:
  - sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md
  - concepts/harness-policy-co-evolution-safety.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
  - concepts/skill-misevolution.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/ccc-k337-k341-phase1-wires.mdc"
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md`
- `@concepts/harness-policy-co-evolution-safety.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K340 — SafeEvolve harness–policy co-evolution for agent safety; MIT REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| SafeEvolve | `MaoPopovich/SafeEvolve` | **MIT** → **GO REFERENCE** `.local/adopts/SafeEvolve` (~841KB) |

**Phase-0:** `scripts/adopt_k340_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

Co-evolves safety harness artifacts (prompt + hierarchical skill bank) with policy via SFT-RL from on-policy trajectories. **Runtime `wont_wire`** — trainer/SFT-RL not wired into CCC harness. **Never auto-evolve `.cursor/skills`** from SafeEvolve loops (pairs K237/K268/K162).

## Snippets

> "GO REFERENCE only — safety co-evolution pattern study; no CCC runtime wiring." [Source: wiki/entities/tools/safeevolve.md]
