---
title: "Toward SLM-based agentic task-tool intent matching (CCC K422)"
type: source
tags: [source, arxiv, k422]
keywords: [2610.03213, k422]
related:
  - concepts/intent-based-tool-call-oversight.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- `@concepts/intent-based-tool-call-oversight.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Toward SLM-based agentic task-tool intent matching |
| **arXiv** | 2610.03213 (2026-10) |
| **Retrieved** | 2026-10-05 |

## Narrative

**Verdict: ADOPT pattern (no repo — 404).**

**Cisco — authorize the intent, not just the call.** Conventional authorization asks whether an agent *may* invoke a tool. It cannot ask whether calling that tool is a **logical step toward the task's intent**. An allowed call can still be irrelevant, and a rogue agent can steer a combination of individually-permitted calls away from the task. The paper extends **Task-Based Access Control** to **intent-based TBAC** and puts a **small language model in the per-call path**: an SLM scores each selected tool against the assigned task and emits a relevance signal for downstream enforcement. That framing is the contribution — **a per-call cognitive check, not a permission check**, positioned for low latency and on-prem deployment where frontier models are ruled out by privacy, cost, or policy. Results: a **Gemma-3-4B**, specialized through `GEPA → SFT → GRPO`, reaches **96.13% end-to-end accuracy / 96.90 F1** against a 95% operational bar, with FPR 5.42 / FNR 2.94 — from 87.48% base. The 1B model reaches 89.60% and does not clear the bar, so **4B is the floor**. The staged pipeline matters independently: GEPA, SFT, and GRPO move **false positives and false negatives differently** — GEPA bought recall at a selectivity cost, SFT restored selectivity, GRPO balanced both. Pairs K395 approval laundering / K402 MCP error surfaces / K421 tool-boundary mediation / `@concepts/step-level-tool-guardrails.md`. **Phase-0: the paper's stated repo `outshift-open/outshift-casa-slm` returns 404** — not published under that name → **no repo to clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Conventional authorization schemes can determine whether an agent is allowed to invoke a tool, but cannot assess the agent's underlying cognition, specifically, whether the tool selection represents a logical, relevant step toward satisfying the intent of the task." [Source: arXiv 2610.03213 (retrieved 2026-10-05)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.03213-toward-slm-based-agentic-task-tool-intent-matchi.pdf` |
