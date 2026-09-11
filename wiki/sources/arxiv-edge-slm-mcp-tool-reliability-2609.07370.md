---
title: "CPU Reliability Benchmark for MCP-Style Tool Calling in Sub-2B SLMs (CCC K351)"
type: source
tags: [source, arxiv, k351]
keywords: [2609.07370, k351]
related:
  - concepts/edge-slm-mcp-tool-reliability.md
  - briefs/2026-09-11_ccc-k346-k357-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
---

## Relations

- `@concepts/edge-slm-mcp-tool-reliability.md`
- `@briefs/2026-09-11_ccc-k346-k357-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CPU Reliability Benchmark for MCP-Style Tool Calling in Sub-2B SLMs |
| **arXiv** | 2609.07370 (2026-09) |
| **Retrieved** | 2026-09-11 |

## Narrative

**Verdict: ADOPT eval axis.**

Edge SLM agents on SBCs need **machine-readable JSON tool calls**, not fluent text alone. Reliability benchmark for MCP-style invocation on sub-2B models. Eval axis `policy_wired`; runtime `wont_wire`. Pairs K259 tool affordances / K296 terminal-state eval.

## Snippets

> "CPU Reliability Benchmark for MCP-Style Tool Calling in Sub-2B SLMs — CCC K351 synthesis." [Source: arXiv 2609.07370 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.07370-beyond-fluent-generation-a-cpu-reliability-bench.pdf` |
