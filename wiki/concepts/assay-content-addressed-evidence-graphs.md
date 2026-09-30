---
title: "Assay: Claims That Decay With the Code. Content-Addressed Evidence Graphs for Accountable AI-Assisted Software Delivery (CCC K406)"
type: concept
tags: [concept, k406]
keywords: [2609.36170, k406]
related:
  - sources/arxiv-assay-content-addressed-evidence-graphs-2609.36170.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@sources/arxiv-assay-content-addressed-evidence-graphs-2609.36170.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

K406: CONDITIONAL-GO (Apache-2.0) — arXiv 2609.36170.

## Narrative

**Assay — claims decay with the code.** Every agent claim (tests pass, no secrets, behavior preserved) is bound to the **Merkle hash of the dependency cone** of the code it covers. Staleness becomes a hash comparison, not a judgment. **Blast radius == staleness frontier** (Prop. 3): the reach an agent wants before editing and the evidence a gate wants voided after are the same set, from one traversal. Adds a **merge gate that consults no model** — eight mechanical checks: coverage, freshness, signatures, exit codes, plausibility, **evidence monotonicity** (the mechanical form of "do not delete the failing test"), and review status. Blocks 9/9 scripted adversarial behaviors (self-approval, forged ledger, deleted failing test, stale evidence). A **600-token brief costs 14×–114× less** than an exploration proxy. Ships a **dependency-free Python CLI, git hooks, and an MCP server**. Pairs K403 Tracekit (tamper-evident audit) / K394 trace tampering / K402 MCP error surfaces / K405 TokenCast + K320 context cost / reward-tampering literature. **Phase-0: Apache-2.0**, 0 stars, pushed 2026-09-27, no community vetting yet. Runtime **`wont_wire`** — MCP server transport/auth needs its own audit before wiring. Concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.36170 locators." [Source: CCC K406 synthesis]
