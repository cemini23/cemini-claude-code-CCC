---
title: Interpretable agentic document ops (READ / Beyond Top-K) (K255)
type: concept
tags: [concept, rag, mcp, retrieval, embedding-free, k255]
keywords: [2608.06305, READ, memory_grep, memory_outline, BM25]
related:
  - sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md
  - entities/tools/read-agentic-document-search.md
  - concepts/claim-centered-retrieval-with-provenance.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - briefs/2026-08-07_phase1-wire-status-closeout-k254-k258.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md`
- `@entities/tools/read-agentic-document-search.md`
- `@concepts/claim-centered-retrieval-with-provenance.md`

## Raw Concept

When is black-box top-k RAG the wrong interface for long structured documents?

## Narrative

K255 READ (arXiv **2608.06305**): for financial/audit-style docs, chunk boundaries routinely separate figures from units/fiscal-year headers. Prefer deterministic ops — normalized lexical search, structural outline, bounded span reads — over opaque similarity scores. Trajectories become replayable line citations (pairs Traceable Scholarship / claim-units).

### Caveats (paper-honest)

- BM25 ≈ READ statistically — win is **embedding-free vs dense**, not “agent beats lexical.”
- Tuned dense still trails but gap shrinks; report honest baselines.
- Small n=51 author-built bench — large effects only.

### Cemini steal (ADOPT)

1. For long table-heavy docs in wiki/finance ingest: prefer grep/outline/read loops (or BM25) before dense RAG.
2. Require citable line/locator ranges in answers (`@concepts/claim-centered-retrieval-with-provenance.md`).
3. Do not default-install READ MCP into prod allowlist — REFERENCE study first.

| Verdict | **ADOPT** interface pattern. **GO** `.local/adopts/READ` MIT. Entity `policy_wired` / `wont_wire` runtime. |
