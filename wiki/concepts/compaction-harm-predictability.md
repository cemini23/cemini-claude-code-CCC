---
title: "Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus (CCC K434)"
type: concept
tags: [concept, k434]
keywords: [2610.08722, k434]
related:
  - sources/arxiv-compaction-harm-predictability-2610.08722.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-07_ccc-k431-k435-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@sources/arxiv-compaction-harm-predictability-2610.08722.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-07_ccc-k431-k435-sip-ready.md`

## Raw Concept

K434: ADOPT eval-methodology (bounded null) — arXiv 2610.08722.

## Narrative

**Does an agent's history tell you when compaction will hurt? Mostly no — and that is the finding.** Salesforce. Long-horizon harnesses compact on a **global rule, usually a token budget, blind to what the agent is doing**. The natural next step is to defer compaction where recent history says it is about to hurt. This paper tests that on TRACE's public corpus of **590 harness-triggered compaction boundaries**, where each boundary is **replayed from a re-executed prefix** under both the pre-compaction context and the summary, and the **burden of the next actions** (calls that error, or repeat a call already made) is recorded. That paired-replay design is what makes a per-boundary counterfactual possible at all — task success cannot say whether a given compaction hurt. **The result is a carefully-reported null with a real ceiling.** Pre-boundary history predicts post-compaction harm **only weakly**: the prespecified placement contrast is a **wide null** (−0.062 [−0.209, +0.079]), and the naive `has-written` label behind it turns out to measure **trajectory phase** — of 494 "write-prefixed" boundaries, **368 have no write beyond login or session calls**. The best trigger reaches **held-out AUROC 0.66 against a 0.72 same-boundary replicate**; the best frozen interpretable trigger **avoids 21% of harmful boundaries while keeping 84% of opportunities**, and **beats the random-rule expectation on count but not on burden mass** (a post hoc comparison). And the question you would actually want answered — **does any trigger beat a token-budget rule at matched retention? — cannot be evaluated on this release**, because token counts were not published. The paper says what corpora should ship to answer it. **CCC relevance is high and the direction is useful:** CCC holds a whole compaction line (`@concepts/truncate-only-long-horizon-compaction.md`, `context-engineering`, K387 KV working-set, K410 bounded controller state, K429 memory budgeting, K419 lossless memory) — and this is the **measurement that line has been missing**. The honest reading is *we do not yet know that history-based compaction timing beats a token budget*, and **a trajectory-phase proxy will look like signal if you do not control for it**. Pairs the full compaction cluster. **No repo** (TRACE is the source corpus). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.08722 locators." [Source: CCC K434 synthesis]
