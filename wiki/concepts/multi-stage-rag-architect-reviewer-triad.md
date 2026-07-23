---
title: Multi-stage RAG + Architect/Writer/Reviewer triad
type: concept
tags: [concept, rag, multi-agent, retrieval, reviewer, k209]
keywords: [2607.20346, IteraSim, RRF, MMR, query expansion, role separation]
related:
  - sources/arxiv-iterasim-rag-multistage-2607.20346.md
  - entities/tools/iterasim-rag-public.md
  - concepts/domain-mcp-skills-fresh-subagent-orchestration.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - sources/brief-k206-k209-mcp-slm-rag-ethics-2026-07-23.md
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- `@sources/arxiv-iterasim-rag-multistage-2607.20346.md`
- `@entities/tools/iterasim-rag-public.md`
- `@concepts/multi-agent-evidence-artifact-layers.md` — evidence→synthesis→interface

## Raw Concept

K209 IteraSim: don't flat-query RAG; expand→fuse→re-rank; route tool vs corpus queries differently; separate draft from review agents.

## Narrative

### Steal (ADOPT)

1. Wiki/conductor retrieval: multi-variant expand + RRF/MMR-style diversity, not one embedding hit.
2. Separate **Architect** (plan) / **Writer** (artifact) / **Reviewer** (critique) — never self-grade alone (K162).
3. Keep a static canonical-knowledge layer for defaults (like CLAUDE.md / wiki core pages).
4. CFD OpenFOAM body OOD; MIT public kit is benchmark-only.

| Verdict | **ADOPT** retrieval + role-triad checklist; **GO** MIT benchmark clone REFERENCE |
