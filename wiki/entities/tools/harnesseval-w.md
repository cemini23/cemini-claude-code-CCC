---
title: "HarnessEval-W — agentified visual-world evaluation (mirros-lab)"
type: entity
tags: [entity, tool, evaluation, world-model, agentified-benchmark, no-license, k289]
keywords: [k289, HarnessEval-W, agentified eval, evidence tree, null-SPDX, NO-GO, sub-agent routing]
related:
  - sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md
  - concepts/agentified-eval-evidence-tree-harness.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md`
- `@concepts/agentified-eval-evidence-tree-harness.md`

## Raw Concept

Phase-0 entity for CCC K289 — HarnessEval-W (agentified evaluation of visual worlds).

## Narrative

Repo `github.com/mirros-lab/harnesseval-w` — **NO-GO clone** (null SPDX, no LICENSE in pyproject). An agentified evaluation pipeline for world models: per case, interpret context → route to skills → decompose into subproblems → spawn specialized sub-agents with diagnostic tools → parent validates evidence → final verdict as a **transparent evidence tree**. 330 cases / 18 world models.

Steal: eval as an evidence tree (not scalar-only rubric); route case → skills → tool-equipped sub-agents; parent validates before verdict; agentic case construction with validation. **`policy_wired`** — pattern only, no runtime clone.

**Phase-0:** `scripts/adopt_k289_phase0.sh` (no clone — null SPDX)
