---
title: "Harness-of-Harness — meta-harness for multi-day SWE (REFERENCE clone, runtime not wired)"
type: entity
tags: [entity, tool, meta-harness, swe, mit, reference, k335]
keywords: [2609.01481, Harness-of-Harness, HoH, Flesymeb, MIT, continual improvement, multi-day SWE]
related:
  - sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md
  - concepts/meta-harness-continual-improvement.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/ccc-k333-k336-phase1-wires.mdc"
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md`
- `@concepts/meta-harness-continual-improvement.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K335 — Harness-of-Harness meta-harness for multi-day autonomous SWE with continual harness improvement; MIT REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Harness-of-Harness | `Flesymeb/HarnessOfHarness` | **MIT** → **GO REFERENCE** clone `.local/adopts/HarnessOfHarness` (~312MB shallow, <500MB cap) |

**Phase-0:** `scripts/adopt_k335_phase0.sh` — gh API SPDX `MIT`, LICENSE on disk, `du -sm` <500.

HoH wraps existing coding-agent harnesses (Claude Code, OpenHands, etc.) with an outer meta-loop: plan–code–test iterations, small verifiable increments, independent eval gate, versioned project history, progressive tool exposure. Reports +52.25% avg relative gain (max 82.86%) after three iterations across three harness–model pairs.

**Wire:** runtime **`wont_wire`** — do **not** replace Cursor / `/route` / claude-ds. The repo is a reading reference for the meta-harness continual-improvement pattern (`@concepts/meta-harness-continual-improvement.md`). **Do not** auto-evolve `.cursor/skills` from HoH trajectories (pairs K237/K313).

## Snippets

> "GO REFERENCE only — meta-harness pattern study; no CCC runtime wiring." [Source: wiki/entities/tools/harness-of-harness.md — wire note]
