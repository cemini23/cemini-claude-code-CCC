---
title: "MetaCaster — meta-harness few-shot TSF via intermediary-engineer agents (REFERENCE)"
type: entity
tags: [entity, tool, time-series, meta-harness, mit, reference, k308]
keywords: [2608.23473, metacaster, D2I-Group, MIT, tsf, guruwatcher]
related:
  - sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md
  - concepts/agent-as-intermediary-engineer.md
  - entities/tools/autodesign.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md`
- `@concepts/agent-as-intermediary-engineer.md`
- `@entities/tools/autodesign.md` (K281 meta-harness pair)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K308 — MetaCaster meta-harness multi-agent TSF framework; MIT REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| MetaCaster framework | `D2I-Group/metacaster` | **MIT** → **GO REFERENCE** clone `.local/adopts/metacaster` (~5MB) |

**Phase-0:** `scripts/adopt_k308_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

Agents as intermediary engineers training lightweight forecasters from few examples + text; meta-harness loop with external eval; harness transfers across LLM providers. 18 datasets / 23 forecasters / 14 baselines.

## Phase-1

TSF runtime **`wont_wire`** on CCC. GuruWatcher/time-series steal: intermediary-engineer pattern, alert-only — no forecaster runtime swap (see `briefs/2026-08-25_k300-k309-harness-wave-prod.md`). Pairs K281.
