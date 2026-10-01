---
title: "Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean (CCC K411)"
type: concept
tags: [concept, k411]
keywords: [2609.39544, k411]
related:
  - sources/arxiv-rocq-mcp-evolve-tool-interface-evolution-2609.39544.md
  - concepts/mcp-tool-interface-granularity-eval.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@sources/arxiv-rocq-mcp-evolve-tool-interface-evolution-2609.39544.md`
- `@concepts/mcp-tool-interface-granularity-eval.md` — prior CCC page this evolves from static design to a search loop
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

K411: ADOPT pattern (Apache-2.0) — arXiv 2609.39544.

## Narrative

**ROCQ-MCP-EVOLVE — grow the tool interface, do not design it by hand.** Agents reach proof assistants through an MCP server, and that interface sets what the agent receives and what each interaction costs. Today those interfaces are inherited from tools built for humans. This paper **evolves** one instead: a frontier model (Claude Fable 5) acts as **orchestrator**, proposing one new feature at a time; each mutation is evaluated by **smaller** models (Haiku 4.5, Sonnet 5 as testers) on a curated set and kept **only if it improves all three objectives** — accuracy, **cost per solve**, and wall time per solve. Starting from a server that exposes one tool (compile a file), the loop grows a full interface. On the miniF2F-Rocq held-out split it beats both the minimal baseline and an established MCP server across four models from two families. Sonnet: baseline .50 acc / $0.24 / 94 s → established .73 / $0.16 / 44 s → evolved **.82 / $0.11 / 36 s**. The evolved server is **ported to Lean** and improves cost and wall time there too, though it loses on solve rate to a Lean-specific server. Two things make this CCC-relevant: the **interface is the optimization target**, and the thing being optimized is **cost per solve**, not accuracy alone. The frontier model is not the solver — it is the tool designer for the weaker models that actually run. Pairs K402 MCP error surfaces / K311 lazy MCP / K409 meta-skills (Builder-Target) / K405 TokenCast + K320 cost accounting. **Phase-0: `LLM4Rocq/rocq-mcp-experiment` Apache-2.0**, 0★, 0 forks, pushed 2026-10-01 — brand new, no community vetting. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.39544 locators." [Source: CCC K411 synthesis]
