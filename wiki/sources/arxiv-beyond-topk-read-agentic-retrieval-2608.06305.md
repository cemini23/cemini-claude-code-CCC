---
title: "Beyond Top-K — READ interpretable agentic document ops"
type: source
tags: [source, arxiv, rag, mcp, retrieval, k255]
keywords: [2608.06305, READ, twospoon, memory_grep, embedding-free]
related:
  - concepts/interpretable-agentic-document-ops.md
  - entities/tools/read-agentic-document-search.md
  - concepts/claim-centered-retrieval-with-provenance.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@concepts/interpretable-agentic-document-ops.md`
- `@entities/tools/read-agentic-document-search.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations |
| **arXiv** | 2608.06305 |
| **Authors** | Sagar Tamang, Ayush Vyas, Tabarakul Hazarika (TwoSpoon / IIT Patna) |
| **Repo** | `twospoon/READ` — MIT SPDX confirmed |
| **Retrieved** | 2026-08-07 |

## Narrative

On long financial/regulatory docs, chunk+embed+top-k is structurally unsound (units separated from figures). READ exposes deterministic MCP ops (`memory_grep` / `memory_outline` / `memory_read` / `memory_list`) over raw Markdown — trajectories are citable line ranges. 51 verified Qs: READ 58.8% vs dense 15.7% (tuned dense 35.3%, still −23.5pp). BM25 statistically indistinguishable from READ → separates embedding-based from embedding-free, not agentic from lexical.

| Verdict | **ADOPT** interpretable agentic document ops. **GO** MIT REFERENCE clone `.local/adopts/READ` (~8.4MB). **wont_wire** as default CCC MCP. |

**Location (2026-08-07):** local `raw-sources/<file>` — egress-fi SCP timed out (banner exchange); re-archive when jump is up → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`.
