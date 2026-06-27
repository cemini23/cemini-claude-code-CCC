---
title: ToolBench-X
type: entity
tags: [entity, tool, benchmark, tool-use, k129]
keywords: [2606.25819, toolbench-x, foreverskyou, reliability-hazards]
related:
  - sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md
  - concepts/recoverable-tool-reliability-hazards.md
  - sources/brief-k129-tool-reliability-orchestration-2026-06-27.md
maturity: draft
created: 2026-06-27
updated: 2026-06-27
---

## Relations

- `@sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md`
- `@concepts/recoverable-tool-reliability-hazards.md`

## Raw Concept

ToolBench-X — benchmark for tool-using agents under recoverable tool-environment unreliability. K129 ingest (2606.25819).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/Foreverskyou/ToolBench-X |
| **License** | **Unverified** — null SPDX on GitHub at Phase-0 2026-06-27 |
| **Verdict** | **REFERENCE**; **CONDITIONAL-GO** laptop eval after LICENSE confirmed |
| **Overlap** | SafeClawBench (security endpoints), ToolForge (validation-carrying tools) |

**Phase-0:** `scripts/adopt_k129_phase0.sh`

## Dead Ends

- No SPDX license via `gh api` at ingest — do not treat as Adopt until LICENSE file lands.

## Snippets

> "ToolBench-X injects five structured hazard types … each instance remains solvable through at least one valid recovery path."
> — [Source: arxiv-2606.25819-2606-25819v1-beyond-function-calling-benchmarkin.pdf, retrieved 2026-06-27]
