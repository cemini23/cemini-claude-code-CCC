---
title: "Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean (CCC K411)"
type: source
tags: [source, arxiv, k411]
keywords: [2609.39544, k411]
related:
  - concepts/evolutionary-mcp-tool-interface-design.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@concepts/evolutionary-mcp-tool-interface-design.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean |
| **arXiv** | 2609.39544 (2026-09) |
| **Repo** | `LLM4Rocq/rocq-mcp-experiment` |
| **Retrieved** | 2026-10-01 |

## Narrative

**Verdict: ADOPT pattern (Apache-2.0).**

**ROCQ-MCP-EVOLVE — grow the tool interface, do not design it by hand.** Agents reach proof assistants through an MCP server, and that interface sets what the agent receives and what each interaction costs. Today those interfaces are inherited from tools built for humans. This paper **evolves** one instead: a frontier model (Claude Fable 5) acts as **orchestrator**, proposing one new feature at a time; each mutation is evaluated by **smaller** models (Haiku 4.5, Sonnet 5 as testers) on a curated set and kept **only if it improves all three objectives** — accuracy, **cost per solve**, and wall time per solve. Starting from a server that exposes one tool (compile a file), the loop grows a full interface. On the miniF2F-Rocq held-out split it beats both the minimal baseline and an established MCP server across four models from two families. Sonnet: baseline .50 acc / $0.24 / 94 s → established .73 / $0.16 / 44 s → evolved **.82 / $0.11 / 36 s**. The evolved server is **ported to Lean** and improves cost and wall time there too, though it loses on solve rate to a Lean-specific server. Two things make this CCC-relevant: the **interface is the optimization target**, and the thing being optimized is **cost per solve**, not accuracy alone. The frontier model is not the solver — it is the tool designer for the weaker models that actually run. Pairs K402 MCP error surfaces / K311 lazy MCP / K409 meta-skills (Builder-Target) / K405 TokenCast + K320 cost accounting. **Phase-0: `LLM4Rocq/rocq-mcp-experiment` Apache-2.0**, 0★, 0 forks, pushed 2026-10-01 — brand new, no community vetting. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "We propose an evolutionary method where a frontier model incrementally proposes new features and only keeps the ones that improve the overall performance of smaller models." [Source: arXiv 2609.39544 (retrieved 2026-10-01)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.39544-growing-an-agent-prover-interface-evolutionary-t.pdf` |
 **Clone decision 2026-10-01: NO CLONE.** CCC runs no theorem-proving workstream. The reusable result is the *evolutionary method* (mutate one feature, keep it only if accuracy AND cost/solve AND wall time all improve), which the concept page records. The Rocq MCP server itself is domain-specific. Revisit only if a CCC workstream evolves an MCP interface, in which case the method transfers without the code.
