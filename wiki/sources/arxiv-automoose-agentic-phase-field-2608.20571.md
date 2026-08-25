---
title: "AutoMOOSE — agentic phase-field simulation software (materials/HPC OOD)"
type: source
tags: [source, arxiv, ood, materials, hpc, moose, falsification, k300]
keywords: [2608.20571, AutoMOOSE, MOOSE, phase-field, skeptic, six-agent pipeline, argonne]
related:
  - concepts/verification-gated-persist-pivot-runtime.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/verification-gated-persist-pivot-runtime.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AutoMOOSE: Use Case and Logical Views of Agentic Phase-Field Simulation Software |
| **arXiv** | 2608.20571 [cond-mat.mtrl-sci] |
| **Authors** | Sukriti Manna, Henry Chan, Subramanian Sankaranarayanan (UIC + Argonne CNM) |
| **Code** | `github.com/sukritimanna/AutoMOOSE` — **MIT**, but requires a compiled MOOSE `phase_field-opt` binary + SLURM HPC → **skip clone** |
| **Retrieved** | 2026-08-25 |

## Narrative

OOD for CCC (computational materials / HPC) — **stub only**, no concept depth, **`wont_wire`**.

AutoMOOSE converts a natural-language request into an executed, screened, and interpreted MOOSE phase-field simulation. Documented through the 1+5 architectural-views model: user roles, component structure, **six-agent pipeline**, physics plugin layer, **Model Context Protocol interface**, and screening/falsification/recovery loop.

The one transferable line: **separation of physical falsification from automatic repair** — corrected simulations remain inspectable and must be **re-admitted before acceptance**. The Skeptic agent falsifies but never repairs; a separate closed-loop module acts on its verdict. This is the same verification-gated admission shape as CCC K253 persist/pivot, arrived at independently in a physics domain.

| Verdict | **OOD** — source stub. MIT license noted, **no clone** (needs MOOSE binary). Steal: Skeptic falsifies, never repairs; re-admit after repair. `wont_wire`. |
|---------|---------|

## Snippets

> "our architecture separates physical falsification from automatic repair, so corrected simulations remain inspectable and must be re-admitted before acceptance." [Source: arXiv 2608.20571 abstract]

> "the Skeptic agent falsifies but never repairs, and a separate closed-loop module acts on its verdict." [Source: arXiv 2608.20571 §architecture]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.20571-automoose-use-case-and-logical-views-of-agentic.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
