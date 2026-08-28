---
title: "INTENT-AS-A-TOOL — intent-targeted tools for misalignment tracking (MIT REFERENCE clone)"
type: entity
tags: [entity, tool, safety, intent, mit, reference, k323]
keywords: [2608.27348, INTENT-AS-A-TOOL, RebeccaZhang22, intent tool, call probability, misalignment]
related:
  - sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md
  - concepts/intent-as-a-tool-misalignment-signal.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/ccc-k315-k324-phase1-wires.mdc"
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md`
- `@concepts/intent-as-a-tool-misalignment-signal.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K323 — INTENT-AS-A-TOOL; MIT REFERENCE clone; runtime `wont_wire`.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Intent-as-a-tool code + data | `RebeccaZhang22/intent-as-a-tool` | **MIT** (gh API SPDX 2026-08-28) → **GO REFERENCE** clone `.local/adopts/intent-as-a-tool` (~0.3MB; LICENSE on disk) |

**Phase-0:** `scripts/adopt_k323_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

Adds intent-targeted tools to an agent's action space so the model can express commitment to a target behavior as an explicit tool call; the call probability is a judge-free, dense misalignment signal that complements CoT monitoring and identifies critical steps for online intervention. See `@concepts/intent-as-a-tool-misalignment-signal.md`.

**Wire:** policy `policy_wired` (intent-tool tripwires are a design principle for high-risk monitoring); runtime **`wont_wire`** — Cemini does not inject intent tools into live harnesses. **No jailbreak/PoC text in wiki/briefs.**
