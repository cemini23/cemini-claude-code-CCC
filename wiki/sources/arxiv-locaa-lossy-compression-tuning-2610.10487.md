---
title: "LOCAA: An Agentic System for Automated Lossy Compressor Tuning (CCC K439)"
type: source
tags: [source, arxiv, k439]
keywords: [2610.10487, k439]
related:
  - concepts/compression-in-the-loop-tuning.md
  - briefs/2026-10-08_ccc-k436-k440-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/compression-in-the-loop-tuning.md`
- `@briefs/2026-10-08_ccc-k436-k440-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LOCAA: An Agentic System for Automated Lossy Compressor Tuning |
| **arXiv** | 2610.10487 (2026-10) |
| **Repo** | `DIR-LAB/pocket-agent` |
| **Retrieved** | 2026-10-08 |

## Narrative

**Verdict: ADOPT pattern (MIT framework).**

**Search a black-box knob the conventional methods cannot search.** Scientific lossy compression is configured by an **error bound (EB)**, but users care about quality metrics (PSNR, SSIM) and runtime, and **the EB→quality mapping is nonlinear, non-monotonic, and staircase-shaped** depending on dataset and compressor — so binary search is unreliable and derivative-free methods are expensive. LOCAA is a **single agent** doing **compression-in-the-loop search** over MCP-exposed tools with persistent memory and **compressor-aware guidance**. Results: **1.98× fewer trials than binary search** and 5.03× fewer than FRaZ on fixed-ratio search; **61.5 → 17 trials (−72.4%)** under joint PSNR+SSIM constraints; **persistent memory cuts trials another 27.9%** across timesteps of the same field. Two ablations worth keeping: **compressor knowledge beats chain-of-thought** (ZFP 8.67 → 4.00 trials, 53.8%, because ZFP's staircase response breaks generic reasoning), and **the two are not additive** — CoT on top of knowledge helps SZ and *hurts* SZ3, ZFP, SPERR. Also: **88.4% of input tokens were served from prompt cache** (215.9K tokens/run, 181.5K cached). **CCC reading:** this is a clean instance of a pattern CCC keeps collecting — an agent is *better than a fixed algorithm when the response surface is unknown* — and the efficiency came from **domain knowledge plus cache-friendly prompting**, not from reasoning alone. It pairs K425 (cost-aware evolution) and K429 (memory budgeting), and its 88.4% cache hit is the practical case for structuring prompts so the cache fires. **Phase-0: framework `DIR-LAB/pocket-agent` MIT**, 5★. No clone this wave. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "By combining agentic large language models with compression-in-the-loop evaluation, LOCAA efficiently searches compressor and error-bound configurations" [Source: arXiv 2610.10487 (retrieved 2026-10-08)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.10487-locaa-an-agentic-system-for-automated-lossy-comp.pdf` |
