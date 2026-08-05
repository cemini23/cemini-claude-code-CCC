---
title: "MultiGlobeQA — geospatial reasoning benchmark"
type: source
tags: [source, arxiv, geospatial, qa, benchmark, k246]
keywords: [2608.03882, MultiGlobeQA, andreeaiana, aiana94, spatial-function]
related:
  - concepts/geospatial-computation-vs-parametric-knowledge.md
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

- `@concepts/geospatial-computation-vs-parametric-knowledge.md`
- `@entities/tools/multiglobeqa.md`
- `@concepts/solver-grounded-agent-numerics.md`
- `@concepts/llm-tabular-prediction-dimensionality-failure.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MultiGlobeQA |
| **arXiv** | 2608.03882 |
| **Repo** | `andreeaiana/MultiGlobeQA` — MIT |
| **Dataset** | HF `aiana94/MultiGlobeQA` |
| **Local clone** | `.local/adopts/MultiGlobeQA` |
| **Retrieved** | 2026-08-05 |

## Narrative

46,060 QA pairs, 14 spatial-function families, 15 answer formats, 201 countries, EN + 16 languages. Execution-based ground truth over 3 knowledge graphs.

**Findings:**

- LLMs collapse on grid indexing + shape computation; topology/directions best
- Retrieval/tools help but plateau <2/3 even with gold facts → **computation not knowledge** is bottleneck
- Low-income region gap **widens** with gold facts

| Verdict | **ADOPT** solver/tool-grounded geospatial computation (pairs K199/K241). **GO** MIT REFERENCE. `wont_wire` CCC runtime (eval bench). Optional SEO/OSINT geo note. |
