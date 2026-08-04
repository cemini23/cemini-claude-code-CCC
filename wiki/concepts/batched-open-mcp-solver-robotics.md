---
title: Batched open MCP solver for robotics (K240)
type: concept
tags: [concept, robotics, mcp, julia, solver, k240]
keywords: [2608.00959, MixedComplementarityProblems.jl, PATH, lane-change, batched GPU]
related:
  - sources/arxiv-mixed-complementarity-problems-jl-2608.00959.md
  - entities/tools/mixed-complementarity-problems-jl.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@sources/arxiv-mixed-complementarity-problems-jl-2608.00959.md` — K240 provenance
- `@entities/tools/mixed-complementarity-problems-jl.md` — BSD-3 REFERENCE clone

## Raw Concept

Open-source batched mixed-complementarity solvers for multi-agent trajectory games — robotics OOD for CCC harness.

## Narrative

K240 **MixedComplementarityProblems.jl** (arXiv **2608.00959**, David Fridovich-Keil, UT Austin): Julia interior-point MCP solver with batched CPU/GPU execution and AD w.r.t. parameters. ~100× vs sequential PATH on lane-change game.

**OOD for CCC harness day-to-day** — robotics / multi-agent trajectory domain. Cross-wiki routing: `@game-dev-wiki` for trajectory/game applications.

| Verdict | **GO** REFERENCE clone at `.local/adopts/MixedComplementarityProblems.jl`. **wont_wire** CCC runtime. |

## Dead Ends

- **Wiring into Cursor MCP** — no agent-harness fit; keep as `.local/adopts/` study clone only
