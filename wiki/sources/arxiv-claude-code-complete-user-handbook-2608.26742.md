---
title: "Claude Code Complete User Handbook — Soldani (CCC K320)"
type: source
tags: [source, arxiv, claude-code, handbook, practitioner, k320]
keywords: [2608.26742, Soldani, Claude Code handbook, control stack, plan contract, evidence-gated delivery, superseded guidance]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@entities/tools/claude-code.md` — delta applied here, not a 208-page dump
- `@concepts/context-engineering.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Claude Code Complete User Handbook — A verified practitioner's reference for agentic work |
| **arXiv** | 2608.26742 (cs.NI, 2026-08-27) |
| **Author** | David Soldani — Version 1.0, 26 August 2026, 208 pages |
| **Code** | None — practitioner reference, no clone |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: ADOPT as practitioner reference.** Source page + **delta** vs `@entities/tools/claude-code.md` — do **not** paste 208 pages. Claims that contradict Anthropic docs are flagged `[TENTATIVE]`.

The handbook is organized as a verified reference with nine parts: Foundations; Safe working method; Project knowledge and context; Extending Claude Code; Browser use, autonomy and orchestration; Distributed and cloud operation; Operating at scale; Governance, assurance and compliance; Capstone. Part 0 consolidates **21 superseded/misconceived claims** (M01–M21) with the verified position at 23 August 2026 and an evidence ledger (Appendix J).

Deltas CCC did not already have (applied to the entity page):

1. **The agentic control stack** — four layers, only 2–4 constrain: (1) advisory instruction (CLAUDE.md/rules/skills/prompt — shapes intent, not enforced); (2) permission deny→ask→allow (product-enforced); (3) sandbox (OS-enforced, not on native Windows); (4) isolation (container/VM — contains failures of 2–3). Hooks cut across 1–2 but **no hook decision can bypass a matching deny rule**.
2. **Plan-as-contract** — an 8-point minimum complete plan (outcome+exclusions, inputs, every changed file, ordered steps, open human decisions, tests/evidence, external side effects, rollback). Approve the plan, not "any method"; keep the permission mode you intended. Auto mode is classifier-assisted, not a sandbox.
3. **Measure usage and context separately** — `/usage` (allocation, cost) vs `/context` (occupancy) are different quantities; usage climbs superlinearly (every request carries accumulated history); a CLAUDE.md edit does not take effect mid-session.
4. **Completion report discipline** — distinguish checks that ran from checks that were described; "do not describe a check that did not run"; inspect the evidence yourself (`/diff`, `git diff`).
5. **Evidence-Gated Delivery** — eight-stage method with named gates ending in a human release gate (Chapter 34).
6. **Misconception corrections (M01–M21)** — e.g. `/loop` ≠ cron (session-scoped, 50-task cap, 7-day expiry); M03 subagent "independent second opinion" only if you make it one (fork inherits parent conversation; parent's acceptEdits/bypass overrides subagent mode); M15 workflow agents always run in acceptEdits whatever the session mode; M10 not every MCP tool definition consumes context (Tool Search defers); M20 green routine status ≠ task success.

| Confidence | `[TENTATIVE]` — single-source practitioner reference; several claims (M13 /agents, M17 /loop caps, M15 workflow-agent modes) not yet cross-checked against current Anthropic docs `[NEEDS VERIFICATION 2026-09-04]` |
|------------|------------|

## Snippets

> "Claude Code is a fast operator with variable judgement, broad tool access, no inherent knowledge of your unstated intent, and a strong disposition to report success." [Source: arXiv 2608.26742 p.8]

> "An instruction that must hold belongs at layer 2 or below. An instruction that merely should hold belongs at layer 1, where it costs context and buys a tendency." [Source: arXiv 2608.26742 §1.2]

> "M20 — A green status on a routine run means the session started and exited without an infrastructure error. Blocked requests, missing connector tools and task failures appear only in the transcript." [Source: arXiv 2608.26742 Table 1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.26742-claude-code-complete-user-handbook.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
