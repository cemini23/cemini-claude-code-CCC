---
title: "CastClaw — HITL autonomous agent for industry time-series forecasting (CCC K330, OOD stub)"
type: source
tags: [source, arxiv, forecasting, hitl, harness-engineering, versioned-execution-record, ood, k330]
keywords: [2608.30976, CastClaw, time-series forecasting, validation-gated revision, stopping rules, execution report, electricity price]
related:
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/anytime-valid-agent-eval-stopping.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@concepts/anytime-valid-agent-eval-stopping.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting |
| **arXiv** | 2608.30976 (cs.LG, 2026-08-31) |
| **Authors** | Xiaoyu Tao, Mingyue Cheng, Ze Guo, Bokai Pan, Qi Liu, Shijin Wang, Enhong Chen (USTC State Key Lab of Cognitive Intelligence) |
| **Venue** | arXiv preprint, 4 pages |
| **Code** | `npm install -g castclaw` demo — **OOD** (TSF demo) → no clone |
| **Retrieved** | 2026-09-01 |

## Narrative

**Verdict: OOD** — forecasting-system demo, **short source stub**. `wont_wire`. No clone.

CastClaw is a human-in-the-loop autonomous forecasting system built through **harness engineering**: one runtime connects registered forecasting models, analysis/retrieval tools, natural-language user input, and a **versioned execution record**. It leaves numerical prediction to specialized forecasters; it invokes retrieval, analysis, another model, or the user only when a check identifies missing support.

Steal (harness discipline, not TSF runtime):

- **Ask for missing essentials — no silent defaults.** CastClaw distinguishes hard requirements from hypotheses to test and timestamps corrections; a superseded request marks its forecasts stale but retains compatible evidence.
- **A revision replaces the active forecast only after validation + hard constraints.** The Nord Pool case: a candidate adjustment performed worse on the validation period, so it was **rejected and the supplied forecast retained** — the rejection is recorded. HITL cannot bypass those gates; user input is part of the recorded decision process, not post-hoc feedback.
- **Versioned execution record** — inputs, data/model versions, tool outputs, user input, forecast versions, stopping decision; every call and affected forecast version recorded; an action repeats only when evidence changes.
- **Explicit stopping conditions** — stop when the forecast is supported, another action has little expected value, the budget is exhausted, or expert judgment is required.

Results: lowest point-estimate MSE/MAE in all ten dataset–metric cells across five electricity-price datasets vs 16 baselines (mean reductions 14.9% MSE / 18.6% MAE); point estimates only, no significance/causality claims. GuruWatcher: **alert-only pointer** — no new TSF runtime, no GW rule file unless a one-liner in shared policy suffices.

| Confidence | `[CONFIRMED]` — measurements reported in the paper; not reproduced in CCC |
|------------|------------|

## Snippets

> "CastClaw leaves numerical prediction to specialized forecasters. It invokes retrieval, analysis, another model, or the user only when a check identifies missing support; a candidate replaces the current forecast only after validation and constraint checks." [Source: arXiv 2608.30976 §I]

> "CastClaw asks for missing essentials rather than choosing hidden defaults … The run stops when the forecast is supported, another action has little expected value, the budget is exhausted, or expert judgment is required." [Source: arXiv 2608.30976 §II-A/C]

> "The example therefore demonstrates selective tool use and an auditable decision to retain the supplied forecast." [Source: arXiv 2608.30976 §III-A]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.30976-a-human-in-the-loop-autonomous-agent-for-industr.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
