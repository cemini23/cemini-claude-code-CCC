---
title: "Addy Osmani — human judgment and the software factory (Substack RSS)"
type: source
tags: [source, substack, rss, osmani, labels, queue, k244]
keywords: [addyo.substack.com, label state machine, ready-to-implement, verification budget, trajectory-vs-comprehension]
related:
  - concepts/skill-set-selection-under-budget.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/skill-set-selection-under-budget.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Human judgment doesn't leave the software factory |
| **Source** | Addy Osmani — `https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software` |
| **Retrieved** | 2026-08-21 |

## Narrative

**Source stub** (fills missing citation in `briefs/2026-08-21_k244-harness-skill-wayfinder.md`). Osmani's **label state machine** for agentic work queues: **Warp** labels `ready-to-implement` / `ready-to-spec` / `needs-info` / `wait-to-implement` as a queue+lock; **Vercel** labels `success` / `flawed` / `blocked` / `manual` — **only `success` ships**. Core discipline:

- A **verification budget** gates promotion between labels; worker ≠ verifier.
- **Persist the trajectory vs comprehension debt** — keeping the full trace is cheaper than rebuilding understanding later.

| Verdict | **Steal-from** — labeling state machine for task queues; propose-only. |
