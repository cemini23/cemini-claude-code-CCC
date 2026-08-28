---
title: "AsymSpec — context-asymmetric speculative decoding (CCC K319, WATCH)"
type: source
tags: [source, arxiv, serving, speculative-decoding, huawei, watch, k319]
keywords: [2608.26004, AsymSpec, speculative decoding, context compression, drafter, verifier, serving]
related:
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs |
| **arXiv** | 2608.26004 (2026-08-26) |
| **Authors** | Sheng Liang, Yongyue Zhang, Nathanael Brian, Hang Lv, Hao Wang, Chen Zhang, Yong Liu (Huawei + USTC) |
| **Code** | None (Huawei — no clone) |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: WATCH — serving only.** `wont_wire`. No clone.

Speculative decoding (SD) assumes drafter and verifier share **identical context**; AsymSpec breaks that symmetry: a lightweight **drafter reads the full input** while the large **verifier operates on the compressed view**. The drafter steers the verifier via contrastive **δ-fusion of logits**, modulated by a divergence-aware acceptance gate.

Results: ≈90% of full-context accuracy on average; **1.3–1.7× throughput speedups at 0.2–0.3× compute** on isolated text capabilities across four agentic capabilities + two end-to-end agent benchmarks.

CCC relevance: it is a serving-side trick for compressed-context agent pipelines; nothing to wire into Cemini's harness (we run API calls, not our own SD verifier). The general lesson — compression discards critical reasoning signals, so asymmetric context access recovers them — is already covered by context-engineering pages.

| Confidence | `[TENTATIVE]` — vendor results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "A lightweight drafter reads the full input while the large verifier operates on the compressed view." [Source: arXiv 2608.26004 abstract]

> "ASYMSPEC reaches ≈90% of full-context accuracy on average, delivering 1.3–1.7× throughput speedups at 0.2–0.3× the compute cost." [Source: arXiv 2608.26004 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.26004-asymspec-context-asymmetric-speculative-decoding.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
