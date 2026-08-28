---
title: "TAU-Agent — traffic anomaly video RAG (CCC K317, OOD stub)"
type: source
tags: [source, arxiv, rag, video, traffic, ood, k317]
keywords: [2608.25935, TAU-Agent, traffic anomaly, retrieval-augmented, VLM, video captioning, tracking]
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
| **Title** | TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding |
| **arXiv** | 2608.25935 (cs.CV, 2026-08-26) |
| **Authors** | Yuqiang Lin, Yan Shi, Sam Lockyer, Harish Tayyar Madabushi, Adrian Evans, Wenbin Li, Yinhai Wang, Nic Zhang (Bath + UW) |
| **Code** | `github.com/siri-rouser/TAU-Agent` — **MIT** (gh API verified 2026-08-28) — **skip clone** (OOD) |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: OOD** — video/traffic domain, **short stub**. `wont_wire`. No clone (Image-gen skip).

Agentic RAG for traffic anomaly understanding in videos: a central **retrieval agent** orchestrates two visual perception tools — a **Video Captioning Tool** and an **Open-Vocabulary Tracking Tool** — to retrieve and select query-relevant evidence (captions, temporal intervals, object trajectories). The selected evidence, plus sampled frames, goes to an SFT VLM for final reasoning.

AI City Challenge 2026: 0.6779 Track 3 (2nd), 0.3998 Track 7 (12th), 67.9275 Track 8 (5th).

The steal: **retrieval agent picks evidence first, then VLM** — lazy, not dump. Same evidence-selection principle as K311 SCOUT and K316's "incomplete evidence acquisition" lesson.

| Confidence | `[TENTATIVE]` — competition scores as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "A central retrieval agent orchestrates two visual perception tools … to retrieve and select query-relevant evidence, including captions, temporal intervals, and object trajectories." [Source: arXiv 2608.25935 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.25935-tau-agent-an-agentic-retrieval-augmented-framewo.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
