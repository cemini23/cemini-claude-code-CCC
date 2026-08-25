---
title: "Utility Under Attack — agent memory poisoning and the limits of content screening and provenance ranking"
type: source
tags: [source, arxiv, security, memory, poisoning, provenance, retrieval, k304]
keywords: [2608.21230, longmemeval, content screening boundary, bounded occupancy, write-time screening, quantify labs]
related:
  - concepts/memory-poisoning-content-screening-bound.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/memory-poisoning-content-screening-bound.md`
- `@concepts/reconstructive-agent-memory-vs-verbatim-replay.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking |
| **arXiv** | 2608.21230 |
| **Authors** | Arulnidhi Karunanidhi (Quantify Labs) |
| **Artifacts** | harnesses + corpora + aggregate run reports released with paper; no poison PoCs reproduced here |
| **Retrieved** | 2026-08-25 |

## Narrative

Measures the cost of the **weakest** memory-poisoning attack constructible: plainly-worded false assertions generated in one pass — no instructions, no triggers, no retriever optimization. Findings:

| Result | Number |
|--------|--------|
| Corpus poisoned at | **1.2%** |
| LongMemEval accuracy | **0.850 → 0.300** (two-thirds of memory value gone) |
| Write-time content screening recall on indirect injection | 0.832 (1.5% flag rate on trigger-laden benign text) |
| Poisoned memories refused by that same pipeline | **0 / 360** |
| Shipped additive provenance weight vs none | indistinguishable (**p=0.80**) |
| Raising the weight works by | **exclusion** (absolute penalty on untrusted > half the semantic-similarity range) |
| Untrusted-but-benign corpus | 0.3167 → 0.7000 (defense helps) |
| Answer-bearing evidence itself untrusted | retrieval collapses to zero; accuracy 0.0417 (120 questions) |

Thesis: this is a **boundary of content-only screening**, not a detector deficiency — separating a false assertion from a true one requires **external grounding beyond the screened text**. Additive provenance ranking has **no usable weight** in the measured similarity regime: any weight strong enough against a content-shaping attacker also excludes untrusted content categorically. Recommendation: treat provenance as a **bounded occupancy constraint** in retrieval, and require external grounding on the write path.

Pairs K230 reconstructive memory (memory architecture) and Cybersec K304 dual-ID. **No poison PoCs stored or reproduced in this wiki.**

| Verdict | **ADOPT policy** — bounded occupancy for untrusted memories; external grounding required before persistent writes; do not rely on content screening or additive provenance scores. |
|---------|---------|

## Snippets

> "At 1.2% of the corpus, this removes two-thirds of an agent memory's value on LongMemEval (accuracy 0.850 to 0.300), and a four-stage write-time content screening pipeline … refuses 0 of 360 poisoned memories." [Source: arXiv 2608.21230 abstract]

> "We argue provenance belongs in retrieval as a bounded occupancy constraint instead" [Source: arXiv 2608.21230 §1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.21230-utility-under-attack-agent-memory-poisoning-and.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
