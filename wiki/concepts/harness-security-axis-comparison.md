---
title: "EvoRiskBench — a security metric for the harness (CCC k282 route)"
type: concept
tags: [concept, k282, cross-wiki]
keywords: [2610.03153, k282]
related:
  - sources/arxiv-evoriskbench-harness-security-axis-2610.03153.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-05_k282-ccc-agent-eval-route.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@sources/arxiv-evoriskbench-harness-security-axis-2610.03153.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-05_k282-ccc-agent-eval-route.md`

## Raw Concept

Routed from `@osint-wiki` via `@briefs/2026-10-05_k282-ccc-agent-eval-route.md` (arXiv 2610.03153). Canon stays on OSINT.

## Narrative

**Nine model × harness configurations, scored on inbound injection through the surfaces the harness itself exposes — MCP tools, skills, and subagents.** Aggregate attack success **37.46%**; worst configuration **68.44%** (DeepSeek-V4-Pro-0813 × Codex). The headline number is the decomposition: **model spread is 54.37 pp; harness spread is 5.41 pp.** **CCC reading:** the harness is a *second-order* factor in absolute terms — but 5.41 pp is still real, and it is the factor **we control**. Model choice is mostly fixed for a given operator; harness configuration is not. This gives CCC a way to compare harness variants on a **security axis** rather than only a capability axis, which the existing benchmark set does not offer. Pairs K402 MCP error surfaces / `@concepts/schema-bound-mcp-tool-surface.md` / K421 tool-boundary mediation / `@concepts/measurement-integrity-mcp-security-eval.md`. **Routing:** the full brief goes to the cybersec lane; CCC keeps the harness-comparison framing. **No clone, no install.**

## Snippets

> "See source page for arXiv 2610.03153 locators." [Source: CCC k282 synthesis]
