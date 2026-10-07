---
title: "Leveraging a four-quadrant approach for evaluating Redpine Science (CCC K432)"
type: concept
tags: [concept, k432]
keywords: [2610.07937, k432]
related:
  - sources/arxiv-four-quadrant-rag-eval-2610.07937.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-07_ccc-k431-k435-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@sources/arxiv-four-quadrant-rag-eval-2610.07937.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-07_ccc-k431-k435-sip-ready.md`

## Raw Concept

K432: ADOPT eval-methodology (vendor report) — arXiv 2610.07937.

## Narrative

**Evaluate retrieval and generation separately, or the score tells you nothing.** A vendor report (Redpine) on a literature-access MCP, and the methodological point transfers even though the product does not. A RAG pipeline **conflates two effects** — whether the right passage surfaced, and whether the model turned it into a grounded answer — and most evaluations report **one blended number**. A win on that number can come from better retrieval, better generation over similar evidence, or both, and the score alone does not say which. The report's structure is the contribution: **four evaluations across two levels** (retrieval vs generation) × **two benchmark provenances** (public vs expert-validated). The provenance axis exists because **public benchmarks risk saturation and memorisation** — a model can score well by having seen the answers. Headline: 94.4% correct claims with the tool vs 87.6% with no retrieval; 83.1% Recall@10 placing the gold paper in the top ten *stripped of any model reasoning* (the retrieval-only cell); blinded expert panel puts Precision@5 at 75.2% vs 39.8% for the incumbent. **CCC relevance is the separation discipline, not the product:** when CCC measures a retrieval-ish surface, **report the retrieval cell and the generation cell separately** and **state the benchmark's provenance**. This is the same lesson as K423 (representation) and K407 (judge variance) applied to RAG. **Caveat: this is a vendor report about the vendor's own product** — read the numbers as a company's own measurements, and note the release includes the expert-validated question set and reproduction instructions. **Phase-0: `redpine-ai/benchmarks` MIT**, 0★, 2.7 MB — the released benchmarks. Pairs `@concepts/deep-research-evaluation-prompt.md` / `@concepts/claim-centered-retrieval-with-provenance.md` / K426 MCP tool taxonomy. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.07937 locators." [Source: CCC K432 synthesis]
