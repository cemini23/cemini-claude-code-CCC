---
title: "MixedComplementarityProblems.jl — batched MCP solver"
type: source
tags: [source, arxiv, robotics, mcp, julia, k240]
keywords: [2608.00959, David Fridovich-Keil, CLeARoboticsLab, PATH, lane-change]
related:
  - concepts/batched-open-mcp-solver-robotics.md
  - entities/tools/mixed-complementarity-problems-jl.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@concepts/batched-open-mcp-solver-robotics.md`
- `@entities/tools/mixed-complementarity-problems-jl.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MixedComplementarityProblems.jl |
| **Author** | David Fridovich-Keil (UT Austin) |
| **arXiv** | 2608.00959 |
| **Repo** | `CLeARoboticsLab/MixedComplementarityProblems.jl` |
| **License** | BSD-3-Clause |
| **Local clone** | `.local/adopts/MixedComplementarityProblems.jl` (~2.6MB) |
| **Retrieved** | 2026-08-04 |

## Narrative

Open-source Julia interior-point MCP solver; batched CPU/GPU; automatic differentiation w.r.t. parameters. ~100× vs sequential PATH on lane-change game benchmark.

Robotics / multi-agent trajectory domain — **OOD for CCC harness day-to-day**. Cross-wiki note for `@game-dev-wiki`.

| Verdict | **GO** REFERENCE clone. **wont_wire** CCC runtime (robotics). |
