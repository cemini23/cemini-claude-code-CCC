---
title: "AutoDesign — meta-harness optimization for long-horizon agentic design"
type: source
tags: [source, arxiv, meta-harness, self-improving, poster, k281]
keywords: [2608.13560, AutoDesign, DesignHarness, PosterBench, meta-harness-optimizer, rollout-feedback, HITL, meituan, mbzuai]
related:
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - entities/tools/autodesign.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/brief-k162-rsi-verification-hierarchy-2026-07-14.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@entities/tools/autodesign.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design |
| **arXiv** | 2608.13560 |
| **Authors** | Yaxin Luo, Haobin Jiang, et al. (Meituan / MBZUAI / HUST / PKU / Tsinghua / CUHK / SJTU) |
| **Code** | `github.com/Yaxin9Luo/AutoDesign` — **MIT** LICENSE file on disk (gh API NOASSERTION — verify the file) |
| **Retrieved** | 2026-08-14 |

## Narrative

Meta-harness framework where a **meta-harness optimizer guides a code agent to recursively improve the harness based on rollout feedback**, aligned with human design priors. Instantiated on paper-to-poster generation with **PosterBench** (100-paper Main Track, five disciplines) + PosterBench-mini (shared 10-paper subset for controlled eval).

Results: AutoDesign **78.32** on Main Track, +7.45 over closed-source Claude Design; integrating the learned **DesignHarness** improves avg PosterBench Score **54.99 → 67.39 (+12.4%)** across seven code agent×model configs. Fully autonomous loop: **253 tool calls, 11 editing turns, 40 min, <$3**, reaching average conference-poster quality. System-blind human study: highest preference among evaluated systems.

**Harness-security angle (pairs K162):** the self-improve loop must hold an **external eval contract / HITL** — pass criteria must not be closed self-rewritten by the optimizer. Evaluate the harness+optimizer jointly; keep human design priors and external scoring authoritative.

| Verdict | **Steal** meta-harness loop **with HITL / external eval contract** (pairs K162 — no closed self-rewrite of pass criteria). Clone to `.local/adopts/AutoDesign` if LICENSE MIT on disk and repo <500MB. Poster/Image-gen runtime **`wont_wire`**. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.13560-autodesign-meta-harness-optimization-for-long-ho.pdf`
