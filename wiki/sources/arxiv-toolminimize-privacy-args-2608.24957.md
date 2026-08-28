---
title: "ToolMinimize — rewrite tool args to minimum necessary PSD (CCC K315)"
type: source
tags: [source, arxiv, privacy, tool-calls, middleware, mcp, k315]
keywords: [2608.24957, ToolMinimize, PSD, data minimization, privacy cost, argument rewriting, allow/block, MCP]
related:
  - concepts/tool-argument-privacy-minimization.md
  - concepts/step-level-tool-guardrails.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/tool-argument-privacy-minimization.md`
- `@concepts/step-level-tool-guardrails.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure |
| **arXiv** | 2608.24957 (cs.CR, 2026-08-25) |
| **Authors** | Wenbiao Li, Yuqiao Xu (Case Western Reserve University) |
| **Venue** | PST 2026 (IEEE) |
| **Code** | No public repo (Phase-0 SPDX hunt: no hit) |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: ADOPT policy — allow/block is not enough; rewrite the argument values.** Middleware sits between agent and tool (no LLM/framework/tool changes), classifies PSD in arguments, computes a quantitative privacy cost, and rewrites to the minimum necessary data using four operations: **removal, generalization, substitution, truncation** (1.77 ms median latency).

Key numbers:

- 81–88% of tool calls include unnecessary PSD under default prompts across GPT-4o, Claude 3.5 Sonnet, Llama-3.3-70B.
- Explicit privacy prompts still leave 36–76% over-sharing (Llama barely responds: 81%→76%).
- Live validation on 307 calls: privacy cost down 81.2–92.0% at **100% argument-level task validity** (TOST equivalence p<0.001 at Δ=1.0); on 25 unannotated MCP schemas, 79.0% reduction with no `minimum_necessary` metadata.
- Optional LLM content-necessity layer strips task-irrelevant PSD from free-text fields: live-LLM reduction 85.1–95.6%; author-schema 71.1%→90.9%.
- PII detectors miss **implicit PSD** (a hospital name that implies a diagnosis is not a PII pattern); schema-aware rewriting catches it.

Pairs K259/K239 (allow/block gates can't rewrite). Cybersec steal (no PII/PoC dumps). **Dual-ID: CCC K285 Mandato ≠ this — do not merge ToolMinimize with Mandato.**

| Confidence | `[CONFIRMED]` — controlled measurement + live validation reported in paper; not yet reproduced in CCC |
|------------|------------|

## Snippets

> "81–88% of tool calls include unnecessary PSD under default prompts; explicit privacy instructions still leave 36–76% over-sharing." [Source: arXiv 2608.24957 abstract]

> "TOOLMINIMIZE … combines schema-aware necessity analysis with four operations: removal, generalization, substitution, and truncation." [Source: arXiv 2608.24957 abstract]

> "Live validation on 307 tool calls … reduces privacy cost by 81.2–92.0% at 100% argument-level task validity (TOST equivalence p<0.001 at Δ=1.0)." [Source: arXiv 2608.24957 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.24957-toolminimize-auditing-and-rewriting-llm-agent-to.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
