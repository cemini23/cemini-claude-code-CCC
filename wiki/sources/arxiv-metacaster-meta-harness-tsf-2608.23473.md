---
title: "MetaCaster — meta-harness-optimized agent for end-to-end few-shot learning of lightweight time series forecasters"
type: source
tags: [source, arxiv, time-series, forecasting, meta-harness, multi-agent, k308]
keywords: [2608.23473, metacaster, tsf, intermediary engineers, few-shot, nec labs, d2i-group]
related:
  - concepts/agent-as-intermediary-engineer.md
  - entities/tools/metacaster.md
  - entities/tools/autodesign.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/agent-as-intermediary-engineer.md`
- `@entities/tools/metacaster.md`
- `@entities/tools/autodesign.md` (K281 meta-harness pair)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | METACASTER: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters |
| **arXiv** | 2608.23473 |
| **Authors** | ChengAo Shen et al. (U Houston, NEC Labs, Waterloo, UConn, UIUC, SMU) |
| **Code** | `D2I-Group/metacaster` — **MIT** (gh API SPDX verified 2026-08-25), ~5MB → **GO REFERENCE** `.local/adopts/metacaster` |
| **Retrieved** | 2026-08-25 |

## Narrative

Foundation models are uneconomical for resource-constrained TSF; lightweight forecasters need data that scarce/slow/privacy-sensitive domains don't have. MetaCaster resolves this with **agentic data generation**: a meta-harness `H_AGENT` optimizes the working agent's harness (prompts, skills, tools) so the agent can train a specialized lightweight forecaster from only a few examples plus textual context. The optimized harness is **transferable across LLMs** (API switching downstream).

Paradigm claim: agents act **not as forecasters but as intermediary engineers** that prepare efficient task-specific forecasters for deployment — the LLM never predicts the series itself. Evaluated on 18 datasets × 23 SOTA lightweight forecasters × 14 baselines with data- and compute-efficiency wins.

Pairs K281 AutoDesign (meta-harness optimizing harness rather than model). GuruWatcher steal: intermediary-engineer pattern for alert-only time-series work; no TSF runtime on CCC.

| Verdict | **ADOPT** agent-as-intermediary-engineer + external-eval meta-harness loop (do not rewrite pass criteria mid-loop). Clone REFERENCE; TSF runtime **`wont_wire`**. |
|---------|---------|

## Snippets

> "Our work highlights a new TSF paradigm in which agents act not as forecasters but as intermediary engineers that prepare efficient, task-specific forecasters for deployment." [Source: arXiv 2608.23473 abstract]

> "we optimize MGAGENT's Harness using a meta-harness H_AGENT … which is more efficient than fine-tuning LLMs. The optimized Harness is also transferable across different LLMs" [Source: arXiv 2608.23473 §1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.23473-metacaster-meta-harness-optimized-agent-for-end.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
