---
title: "MCP-GRANITE: Benchmarking Granularity of the MCP Tool Interface for LLM Agents (CCC K376)"
type: concept
tags: [concept, k376]
keywords: [2609.24161, k376]
related:
  - sources/arxiv-mcp-granite-tool-interface-granularity-2609.24161.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@sources/arxiv-mcp-granite-tool-interface-granularity-2609.24161.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

K376: ADOPT eval-first — arXiv 2609.24161.

## Narrative

MCP tool **interface granularity** — how many tools, how fine-grained schemas — is a controlled variable for agent eval, not an afterthought. **MCP-GRANITE** sweeps granularity and reports a **~4-tool sweet spot** on their benchmark suite: too few tools overload single-call semantics; too many inflate selection error and context cost. Treat granularity as a harness axis when comparing MCP stacks or ablating tool design (pairs K272 agent4binary packaging / K351 edge SLM JSON reliability). No public SPDX product requirement for CCC — eval vocabulary only. No clone. Runtime **`wont_wire`**.

## Snippets

> "See source page for arXiv 2609.24161 locators." [Source: CCC K376 synthesis]
