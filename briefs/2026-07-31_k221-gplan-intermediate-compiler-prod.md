---
title: K221 — G-plan intermediate + deterministic G-code compiler (prod harness steal)
type: brief
target: cemini-prod
created: 2026-07-31
tags: [k221, harness, intermediate-representation, deterministic-compiler, no-raw-gcode]
source: arXiv:2607.27729 PrintAnything
---

## Target

`cemini-prod:/opt/cemini/briefs/` — agent harness / tool-design lane (not equity MAPPO; not printer install).

## Summary

**Steal:** do not let a model emit machine-control strings (G-code, shell, firmware macros) as free text. Predict a **typed intermediate** (PrintAnything’s G-plan: occupancy / region / flow), then run a **deterministic compiler** to the executable artifact. Complements AgentsCAD MCP grounding (K171) and OVC claim predicates (K220).

## Steal for Cemini harness

1. **Intermediate representation first** — raster / schema / blackboard fields the agent fills; compiler owns syntax.
2. **Deterministic lowering** — perimeter/infill (or equivalent) from maps with audited formulas; no LLM in the last mile.
3. **Benchmark against “convert then legacy tool”** — mesh→slicer baselines show staged error amplification; same lesson for agent pipelines that mesh then hope.
4. **Hardware / misuse caveat** — authors note unauthorized-object risk; treat raw executables as gated outputs.

## Anti-steals

- Do **not** adopt PrintAnything weights or run model G-code on prod printers.
- Do **not** tipdrop/David, atto, or poker-route.
- Do **not** weaken the 3D-wiki hallucinated-G-code red line for friend readers.

## Sources

- https://arxiv.org/abs/2607.27729
- `@3d-printing-wiki/sources/2026-hong-printanything-gplan.md`
- `@3d-printing-wiki/briefs/2026-07-31_printanything-phase0.md`
- Related: K171 AgentsCAD MCP grounding; K220 optimistic claim adjudication
