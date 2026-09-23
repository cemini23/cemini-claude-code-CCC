---
title: "MCP-GRANITE: Benchmarking Granularity of the MCP Tool Interface for LLM Agents (CCC K376)"
type: source
tags: [source, arxiv, k376]
keywords: [2609.24161, k376]
related:
  - concepts/mcp-tool-interface-granularity-eval.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@concepts/mcp-tool-interface-granularity-eval.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MCP-GRANITE: Benchmarking Granularity of the MCP Tool Interface for LLM Agents |
| **arXiv** | 2609.24161 (2026-09) |
| **Retrieved** | 2026-09-23 |

## Narrative

**Verdict: ADOPT eval-first.**

MCP tool **interface granularity** — how many tools, how fine-grained schemas — is a controlled variable for agent eval, not an afterthought. **MCP-GRANITE** sweeps granularity and reports a **~4-tool sweet spot** on their benchmark suite: too few tools overload single-call semantics; too many inflate selection error and context cost. Treat granularity as a harness axis when comparing MCP stacks or ablating tool design (pairs K272 agent4binary packaging / K351 edge SLM JSON reliability). No public SPDX product requirement for CCC — eval vocabulary only. No clone. Runtime **`wont_wire`**.

## Snippets

> "MCP-GRANITE: Benchmarking Granularity of the MCP Tool Interface for LLM Agents — CCC K376 synthesis." [Source: arXiv 2609.24161 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.24161-mcp-granite-benchmark-granularity-interface-test.pdf` |
