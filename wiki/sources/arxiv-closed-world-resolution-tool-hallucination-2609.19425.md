---
title: "Closed-World Resolution Against Tool Hallucination in LLM Agents (CCC K369)"
type: source
tags: [source, arxiv, k369]
keywords: [2609.19425, k369]
related:
  - concepts/closed-world-tool-hallucination-resolution.md
  - briefs/2026-09-18_ccc-k369-k372-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-18
updated: 2026-09-18
---

## Relations

- `@concepts/closed-world-tool-hallucination-resolution.md`
- `@briefs/2026-09-18_ccc-k369-k372-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Closed-World Resolution Against Tool Hallucination in LLM Agents |
| **arXiv** | 2609.19425 (2026-09) |
| **Retrieved** | 2026-09-18 |

## Narrative

**Verdict: ADOPT policy.**

Tool-selection and tool-gating presuppose the emitted call refers to a **real tool** — **hallucinated tools/arguments** bypass both (not a gate decision at all). Closed-world resolution validates calls against an explicit tool registry/schema before execution. Pairs K259 tool affordances / K368 implicit trust / K274 CDH. Runtime **`wont_wire`** — schema validation belongs in broker/harness.

## Snippets

> "Closed-World Resolution Against Tool Hallucination in LLM Agents — CCC K369 synthesis." [Source: arXiv 2609.19425 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.19425-closed-world-resolution-against-tool-hallucinati.pdf` |
