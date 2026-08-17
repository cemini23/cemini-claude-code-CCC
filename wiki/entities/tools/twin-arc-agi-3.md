---
title: "TWIN-ARC-AGI-3 — test-time digital twin (Stanford / Cornell / USC / Yeshiva)"
type: entity
tags: [entity, tool, world-model, arc-agi, mit, k283]
keywords: [k283, Twin, TWIN-ARC-AGI-3, ARC-AGI-3, MIT, replay-validation]
related:
  - sources/arxiv-twin-test-time-digital-twin-2608.14490.md
  - concepts/test-time-world-model-validate-before-act.md
  - concepts/active-abstraction-programmatic-world-models.md
  - entities/tools/tycho-arc-agi.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@game-dev-wiki/concepts/twin-test-time-world-model-stub.md"
maturity: draft
wire_status: wont_wire
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-twin-test-time-digital-twin-2608.14490.md`
- `@concepts/test-time-world-model-validate-before-act.md`
- `@concepts/active-abstraction-programmatic-world-models.md`
- `@entities/tools/tycho-arc-agi.md`

## Raw Concept

Phase-0 entity for CCC K283 — Twin (test-time digital twin for ARC-AGI-3).

## Narrative

Repo `github.com/Alexyskoutnev/TWIN-ARC-AGI-3` — LICENSE **MIT** (verified on disk; `Copyright (c) 2026 Alexy Skoutnev`). ~7.1MB → cloned to `.local/adopts/TWIN-ARC-AGI-3` as **GO REFERENCE**.

Steal: harness-enforced validate-before-act (no scored action until the twin replays every logged transition) + goal-before-reward + execute-checked (halt-on-mismatch) + counterexample-driven repair. Pairs K231 Tycho — build/use/bypass; Twin is the mandatory replay gate. ARC bench runtime **`wont_wire`**.

**Phase-0:** `scripts/adopt_k283_phase0.sh`
