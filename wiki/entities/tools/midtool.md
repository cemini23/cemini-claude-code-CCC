---
title: "MidTool — mid-training data synthesis for agentic tool use (UW / Snowflake / UNC)"
type: entity
tags: [entity, tool, mid-training, tool-use, mcp, k299]
keywords: [2608.20314, MidTool, MidTool-Mix, wont_wire, HF skip]
related:
  - sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md
  - concepts/mid-training-tool-use-affordance-grounding.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
wire_target: "model-choice awareness only — no HF download, no runtime wire"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md`
- `@concepts/mid-training-tool-use-affordance-grounding.md`

## Raw Concept

Phase-0 entity for CCC K299 — MidTool 20.3B-token mid-training tool-use corpus; HF `MidTool/midtool-release` **skipped**.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| MidTool-Mix corpus / models | `hf.co/collections/MidTool/midtool-release` | **WATCH — no download** |

**Phase-0:** `scripts/adopt_k299_phase0.sh` — no clone, no HF fetch.

Model-choice awareness: dedicated tool-use mid-training (affordance recognition, argument grounding, workflow composition, incomplete-info recovery) beats leaving tool use to post-training. **`wont_wire`** runtime.

## Phase-1

`wont_wire` → awareness only (`.cursor/rules/cemini-phase1-policy-wires.mdc` §K299). Pairs K259 (CASCADE parameter grounding).
