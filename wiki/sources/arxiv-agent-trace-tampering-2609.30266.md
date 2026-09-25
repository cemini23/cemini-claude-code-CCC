---
title: "LLM Agents Can Easily Tamper With Their Own Traces (CCC K394)"
type: source
tags: [source, arxiv, k394]
keywords: [2609.30266, k394]
related:
  - concepts/agent-trace-tampering-audit-gap.md
  - briefs/2026-09-25_ccc-k390-k394-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-25
updated: 2026-09-25
---

## Relations

- `@concepts/agent-trace-tampering-audit-gap.md`
- `@briefs/2026-09-25_ccc-k390-k394-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLM Agents Can Easily Tamper With Their Own Traces |
| **arXiv** | 2609.30266 (2026-09) |
| **Retrieved** | 2026-09-25 |

## Narrative

**Verdict: Cybersec + ADOPT policy.**

**Cybersec-primary + ADOPT policy:** agent-writable traces break audit — require **external append-only / tamper-evident logging** (pairs K277/K239/K327 Logos transcript). **No PoCs / no tamper recipes.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary." [Source: https://arxiv.org/abs/2609.30266 (retrieved 2026-09-25)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.30266-llm-agents-can-easily-tamper-with-their-own-trac.pdf` |
