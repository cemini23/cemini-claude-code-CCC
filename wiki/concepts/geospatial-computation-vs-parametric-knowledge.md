---
title: Geospatial computation vs parametric knowledge (K246)
type: concept
tags: [concept, geospatial, computation, solver, k246]
keywords: [2608.03882, MultiGlobeQA, grid-indexing, gold-facts, k199, k241]
related:
  - sources/arxiv-multiglobeqa-geospatial-reasoning-2608.03882.md
  - entities/tools/multiglobeqa.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/llm-tabular-prediction-dimensionality-failure.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@sources/arxiv-multiglobeqa-geospatial-reasoning-2608.03882.md` — K246 provenance
- `@concepts/solver-grounded-agent-numerics.md` — K199 solver-grounded peer
- `@concepts/llm-tabular-prediction-dimensionality-failure.md` — K241 computation-not-knowledge peer

## Raw Concept

When geospatial QA fails, is the bottleneck missing world knowledge or inability to compute over spatial structure?

## Narrative

K246 MultiGlobeQA (arXiv **2608.03882**): 46,060 QA pairs, 14 spatial-function families, 15 answer formats, 201 countries, EN + 16 languages; execution-based GT over 3 KGs.

### Findings

- LLMs collapse on **grid indexing + shape computation**; topology/directions strongest
- Retrieval/tools help but plateau **<2/3** even with **gold facts** → bottleneck is **computation, not knowledge**
- Low-income region gap **widens** with gold facts (computation burden dominates)

Pairs K199 solver-grounded numerics and K241 tabular dimensionality failure: LLM-as-interface, solver-as-truth for spatial computation.

### Cemini policy (ADOPT)

- Route grid/shape/area tasks through geospatial solvers or tool-grounded pipelines
- Do not expect RAG alone to fix geospatial QA ceilings
- MIT REFERENCE bench `@entities/tools/multiglobeqa.md` — `wont_wire` CCC runtime; optional SEO/OSINT geo eval note

| Verdict | **ADOPT** solver/tool-grounded geospatial computation. **GO** MIT REFERENCE clone. |
