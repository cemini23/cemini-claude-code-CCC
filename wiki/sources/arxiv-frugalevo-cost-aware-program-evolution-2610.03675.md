---
title: "FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution (CCC K425)"
type: source
tags: [source, arxiv, k425]
keywords: [2610.03675, k425]
related:
  - concepts/cost-aware-program-evolution.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- `@concepts/cost-aware-program-evolution.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution |
| **arXiv** | 2610.03675 (2026-10) |
| **Repo** | `chchenhui/frugalevo` |
| **Retrieved** | 2026-10-05 |

## Narrative

**Verdict: ADOPT pattern (Apache-2.0).**

**FrugalEvo — optimize gain per dollar, not gain per iteration.** LLM-guided evolutionary search (AlphaEvolve and successors) usually reports performance after a fixed number of iterations, which **conflates capability with spend** — more iterations means more money, and test-time scaling means a better number may just be a larger bill. The paper's first contribution is a **metric**: **Budget-Aware AUC**, the area under the best-so-far score curve plotted against **cumulative LLM cost** up to a budget. The second is the architecture, and it is the CCC-relevant part: **split generation across two models.** A strong, expensive LLM proposes **design strategies**; a cheap LLM **implements them as code and refines it**. The strong model never writes the bulk of the tokens. On top of that the harness and prompts are **designed to maximize prefix sharing across evolution steps**, so **prompt caching actually fires** and cost per iteration drops to **$0.0097 against $0.0210–$0.0435 for the baselines**. Results: it matches or beats OpenEvolve, ShinkaEvolve, AdaEvolve, and EvoX on final quality and **wins BA-AUC on 9 of 10** tasks; on circle packing it sets a new SOTA for **$0.55** (GLM-5.3 + Flash) where comparable multi-agent methods averaged **~$50**. **CCC relevance is high and it composes with several earlier pages:** the expensive-planner/cheap-implementer split is K409's Builder/Target and K411's frontier-designs-for-smaller-models, and the cache-aware harness is the practical version of `@concepts/token-economics-and-prompt-caching.md` — **structure the prompt so the cache can hit.** Pairs K405 TokenCast / K320 / K415 instance-adaptive harness / `@concepts/three-cache-architecture.md`. **Phase-0: `chchenhui/frugalevo` Apache-2.0**, 3★, pushed 2026-10-04. **CLONED 2026-10-05** → `.local/adopts/frugalevo` (shallow, commit `1db9af27b`). The working tree was **5.5 GB**, of which **5.1 GB was `runs/` — the paper's experiment output, not code**; that was trimmed per operator decision, leaving **408 MB**. What remains is the harness: `skydiscover/` 1.8 MB, `configs/` 1.4 MB, `scripts/` 4 KB, `benchmarks/` 72 MB of datasets. The API's `size=305717KB` was packed git data and understated the checkout by ~18x. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "we design our harness and prompts to maximize the sharing of prefixes across different evolution steps, improving cache reuse." [Source: arXiv 2610.03675 (retrieved 2026-10-05)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.03675-frugalevo-towards-cost-aware-llm-guided-program.pdf` |
