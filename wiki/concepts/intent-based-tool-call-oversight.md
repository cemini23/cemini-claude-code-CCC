---
title: "Toward SLM-based agentic task-tool intent matching (CCC K422)"
type: concept
tags: [concept, k422]
keywords: [2610.03213, k422]
related:
  - sources/arxiv-slm-task-tool-intent-matching-2610.03213.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
  - concepts/streaming-trajectory-monitor-pre-execution-gate.md
  - sources/arxiv-ontrack-streaming-monitor-2610.12375.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-05
updated: 2026-10-09
---

## Relations

- `@sources/arxiv-slm-task-tool-intent-matching-2610.03213.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

K422: ADOPT pattern (no repo — 404) — arXiv 2610.03213.

## Narrative

**Cisco — authorize the intent, not just the call.** Conventional authorization asks whether an agent *may* invoke a tool. It cannot ask whether calling that tool is a **logical step toward the task's intent**. An allowed call can still be irrelevant, and a rogue agent can steer a combination of individually-permitted calls away from the task. The paper extends **Task-Based Access Control** to **intent-based TBAC** and puts a **small language model in the per-call path**: an SLM scores each selected tool against the assigned task and emits a relevance signal for downstream enforcement. That framing is the contribution — **a per-call cognitive check, not a permission check**, positioned for low latency and on-prem deployment where frontier models are ruled out by privacy, cost, or policy. Results: a **Gemma-3-4B**, specialized through `GEPA → SFT → GRPO`, reaches **96.13% end-to-end accuracy / 96.90 F1** against a 95% operational bar, with FPR 5.42 / FNR 2.94 — from 87.48% base. The 1B model reaches 89.60% and does not clear the bar, so **4B is the floor**. The staged pipeline matters independently: GEPA, SFT, and GRPO move **false positives and false negatives differently** — GEPA bought recall at a selectivity cost, SFT restored selectivity, GRPO balanced both. Pairs K395 approval laundering / K402 MCP error surfaces / K421 tool-boundary mediation / `@concepts/step-level-tool-guardrails.md`. **Phase-0: the paper's stated repo `outshift-open/outshift-casa-slm` returns 404** — not published under that name → **no repo to clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.03213 locators." [Source: CCC K422 synthesis]
