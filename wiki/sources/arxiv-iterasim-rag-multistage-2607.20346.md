---
title: "IteraSim RAG — multi-stage retrieval + Architect/Writer/Reviewer"
type: source
tags: [source, arxiv, rag, multi-agent, retrieval, openfoam, k209]
keywords: [2607.20346, IteraSim, RRF, MMR, keyword router, Reviewer]
related:
  - concepts/multi-stage-rag-architect-reviewer-triad.md
  - concepts/domain-mcp-skills-fresh-subagent-orchestration.md
  - entities/tools/iterasim-rag-public.md
  - sources/brief-k206-k209-mcp-slm-rag-ethics-2026-07-23.md
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- `@concepts/multi-stage-rag-architect-reviewer-triad.md` — synthesized steal
- `@entities/tools/iterasim-rag-public.md` — MIT benchmark kit
- `@concepts/domain-mcp-skills-fresh-subagent-orchestration.md` — multi-agent peer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | IteraSim RAG: A Multi-Stage Retrieval-Augmented Agentic Back-End for OpenFOAM-Based Computational Fluid Dynamics |
| **Author** | Pratyush Kumar (ETH Zürich) |
| **arXiv** | 2607.20346 |
| **Pages** | 40 |
| **Retrieved** | 2026-07-23 |
| **Code** | `iterasim/iterasim-rag-public` — **MIT** benchmark kit (engine not included) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.20346-iterasim-rag-a-multi-stage-retrieval-augmented-a.pdf` |

## Narrative

Fixes flat single-query RAG + self-review entanglement: (1) multi-variant query expand → RRF → MMR; (2) deterministic router for tool-vs-corpus paths; (3) Architect / InputWriter / Reviewer triad + static canonical knowledge. CFD domain OOD — steal retrieval + separation-of-roles pattern.
