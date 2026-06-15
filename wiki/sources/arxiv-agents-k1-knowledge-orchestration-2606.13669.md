---
title: Agents-K1 — agent-native knowledge orchestration (arXiv 2606.13669)
type: source
tags: [source, arxiv, agents-k1, knowledge-graph, librarian, cross-wiki-route, k114]
keywords: [2606.13669, agents-k1, scholar-kg, graphanything, knowledge-orchestration]
related:
  - concepts/agents-k1-agent-native-knowledge-orchestration.md
  - concepts/interaction-native-knowledge-harness.md
  - entities/mcp-servers/librarian-kb-server.md
  - entities/tools/conductor-mcp.md
  - concepts/cross-wiki-routing.md
  - osint-wiki/concepts/librarian-server-architecture.md
maturity: draft
read_status: skimmed
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@concepts/agents-k1-agent-native-knowledge-orchestration.md` — CCC REFERENCE synthesis
- `@concepts/interaction-native-knowledge-harness.md` — wiki-as-audit vs graph-for-retrieval parallel
- `@entities/mcp-servers/librarian-kb-server.md` — Cemini federation serving layer
- `@entities/tools/conductor-mcp.md` — cross-wiki query router over librarian
- `@concepts/cross-wiki-routing.md` — federation ingest vs KG construction boundary
- `@osint-wiki/concepts/librarian-server-architecture.md` — OSINT serving-layer canon

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agents-K1: Towards Agent-native Knowledge Orchestration |
| **Authors** | Shanghai AI Lab et al. (Zongsheng Cao, Bo Zhang, Lei Bai, …) |
| **arXiv** | 2606.13669v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.13669-agents-k1-towards-agent-native-knowledge-orchest.pdf` |
| **Retrieved** | 2026-06-13 |
| **Read status** | skimmed — pipeline architecture, Scholar-KG scale claims, GraphAnything CLI |

## Narrative

Argues research agents need **knowledge orchestration** (what knowledge, how organized, traceable evidence) not just **agent orchestration** (plan/act loops). Flat citation graphs and abstract-only RAG lose claims, mechanisms, multimodal evidence, and citation intent.

**Agents-K1 pipeline:**

| Stage | Component |
|-------|-----------|
| Parse + schema | MinerU multimodal parser; five-module schema (meta, explicit mentions, implicit abstractions, citation intent, inter-entity relations) |
| Extract | 4B GRPO-trained IE backbone (rule-based reward) |
| Agent interface | **GraphAnything CLI** — tri-source fusion: web search + multimodal graph retrieval + cross-document traversal (CLI/MCP/API) |

Built **Scholar-KG** from **2.46M** papers (six disciplines); **1M-paper subset released**. **General-KG** extension: schema-adaptive multi-view modes (binary, nary, temporal, event, diy YAML) for non-academic corpora.

Benchmark lifts cited on FrontierScience-Research and multi-hop QA vs graph-RAG baselines.

**Cross-wiki routing:** KG construction + librarian scaling debates → `@osint-wiki` (serving layer owner). CCC extracts **agent-native KG** requirements and GraphAnything tri-source pattern as REFERENCE vs existing `wiki/` + kb-server — do not duplicate Scholar-KG on laptop.

## Snippets

> "A research agent needs more than a list of relevant papers. It needs structured knowledge that preserves what each paper claims, what evidence supports the claim, how the claim relates to prior work, and where the evidence can be checked."

> "The graph should serve online retrieval, while structured provenance links each node back to exact evidence spans."

> — [Source: arxiv-2606.13669-agents-k1-towards-agent-native-knowledge-orchest.pdf §1,3, retrieved 2026-06-13]
