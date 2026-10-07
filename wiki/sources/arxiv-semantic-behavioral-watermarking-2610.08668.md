---
title: "Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents (CCC K433)"
type: source
tags: [source, arxiv, k433]
keywords: [2610.08668, k433]
related:
  - concepts/semantic-action-cluster-watermarking.md
  - briefs/2026-10-07_ccc-k431-k435-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@concepts/semantic-action-cluster-watermarking.md`
- `@briefs/2026-10-07_ccc-k431-k435-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents |
| **arXiv** | 2610.08668 (2026-10) |
| **Retrieved** | 2026-10-07 |

## Narrative

**Verdict: ADOPT pattern.**

**Watermark the action, not the string — and check for forgery, not only removal.** Behavioural watermarking embeds an owner identifier in an agent's **high-level action choices**, so provenance survives without touching output tokens. Prior schemes bind the signal to **raw strings** and break three ways, all measured here rather than asserted: (1) **AgentMark's own robustness test paraphrases only the observation** and bit-recovery collapses to **16.8%** — and its released script holds the per-step key fixed, so that experiment measures **distribution drift, not the key desynchronisation its own context-hash design admits**. (2) **Renaming a tool desynchronises decoding** even when the observation is untouched — the axis this paper measures and closes. (3) **Every prior agent watermark studies only removal; none asks whether an adversary can forge a trajectory that verifies as someone else's** — a question already answered *affirmatively* for text watermarks. SBW's answer: watermark over **semantic action clusters** under history conditioning, and replace the public-cluster bin with **keyed collision-resistant binning** whose fresh-bucket assignment is provably unpredictable in the random-oracle model. Results across five models (3B–14B, four vendors) and three encoders: on ToolBench detection under rewriting is **0.49–0.66 cluster-level vs 0.05–0.17 exact-symbol** at 1% FPR; on ALFWorld **0.92–0.97 vs 0.00–0.01**. Keyed binning takes **adaptive forgery from 100% to the false-positive floor**. And the authors mark the boundary their guarantee does not cover: **chained replay remains 0.76–0.98 across all five models, reported as open**. **CCC relevance:** this lands on the audit-integrity line — **an agent-writable trace is not evidence** (K394), and here the *positive* construction is given: bind provenance to something paraphrase-stable, and **test forgery, not just removal**. Pairs `@concepts/agent-trace-tampering-audit-gap.md` / K403 Tracekit / K406 Assay / K427 trajectory audit. **No repo.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "every prior agent watermark studies only removal: none asks whether an adversary can forge a trajectory that verifies as someone else's." [Source: arXiv 2610.08668 (retrieved 2026-10-07)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.08668-semantic-behavioral-watermarking-paraphrase-robu.pdf` |
