---
title: Robust-TO — confidence-aware tool orchestration (arXiv 2606.26904)
type: source
tags: [source, arxiv, tool-orchestration, video, robust-to, k129]
keywords: [2606.26904, robust-to, blind-trust, confidence-aware]
related:
  - concepts/confidence-aware-tool-orchestration.md
  - sources/brief-k129-robust-to-imagegen-handoff-2026-06-27.md
  - concepts/recoverable-tool-reliability-hazards.md
  - concepts/subagent-orchestration.md
maturity: draft
read_status: read
created: 2026-06-27
updated: 2026-06-27
cross-wiki-primary: "@image-gen-wiki/concepts/confidence-aware-tool-orchestration.md"
---

## Relations

- `@concepts/confidence-aware-tool-orchestration.md` — CCC orchestration steal
- `@sources/brief-k129-robust-to-imagegen-handoff-2026-06-27.md` — image-gen handoff stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Confidence-Aware Tool Orchestration for Robust Video Understanding |
| **Authors** | He, Choi, Yoon (NTU Singapore et al.) |
| **arXiv** | 2606.26904v1 [cs.CV] |
| **Project** | https://rova-v2.github.io/ |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.26904-2606-26904v1-confidence-aware-tool-orchestration.pdf` |
| **Retrieved** | 2026-06-27 |
| **Read status** | read (Blind Trust Problem + three-stage pipeline) |

## Narrative

**Robust-TO** addresses the **Blind Trust Problem** — treating all frames/tool outputs as equally reliable. Pipeline: (1) frame quality profiling + reliability-relevance scoring, (2) confidence-guided tool routing with `(result, confidence)` pairs, (3) three-tier evidence synthesis (high/medium/low).

**Cross-wiki:** video corruption domain is **image-gen-primary**; CCC keeps generic **confidence-aware tool orchestration** pattern for MCP/subagent routing.

**Verdict:** **REFERENCE** — no public harness repo at Phase-0; steal tiered evidence weighting for conductor/lazy-tool.

## Snippets

> "Every frame is treated as equally informative, every perception output as equally reliable, and the model's confidence in its answer is decoupled from the visual conditions that produced it."
> — [Source: arxiv-2606.26904-2606-26904v1-confidence-aware-tool-orchestration.pdf, retrieved 2026-06-27]
