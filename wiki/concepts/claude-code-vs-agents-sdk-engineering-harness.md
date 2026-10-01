---
title: "Skill-Based AI Agents for Power-System Studies (CCC K412)"
type: concept
tags: [concept, k412]
keywords: [2609.40272, k412]
related:
  - sources/arxiv-skill-based-agents-power-system-studies-2609.40272.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@sources/arxiv-skill-based-agents-power-system-studies-2609.40272.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

K412: ADOPT pattern (Claude Code harness eval) — arXiv 2609.40272.

## Narrative

**PNNL runs a real engineering workflow on two agent harnesses and compares them.** The domain is power-system transmission planning; the tools are a **custom MCP server** exposing Siemens PSS®E functions (power flow, dynamic simulation, result extraction, model validation). Two implementation pathways were built on the same capability set: a **programmable OpenAI Agents SDK** harness, and the **Claude Code CLI** harness. Both use **reusable skills, subagents, MCP tools, data-repository connections, and local shell/Python execution** — the same four-part shape CCC ships. Both executed the representative study tasks successfully. Evaluation is by **task completion, output accuracy, and the need for human expert interventions** — that third metric is the one worth stealing: HITL burden measured as a first-class outcome, not as an afterthought. The paper's conclusion is a practice shift: agentic systems absorb routine simulation setup and result extraction, and engineers move to scenario design and interpretation. **This is the most directly CCC-relevant paper of the wave** — it is a head-to-head of Claude Code as a production engineering harness against a programmable SDK, in a domain with real correctness stakes. Pairs `@concepts/harness-as-eval-artifact.md` / K402 MCP error surfaces / `@concepts/subagent-orchestration.md` / `@concepts/skill-set-selection-under-budget.md`. **No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.40272 locators." [Source: CCC K412 synthesis]
