---
title: "Mandate signature vs pre-authorization intent (CCC K310)"
type: concept
tags: [concept, security, payments, mandates, ap2, context-binding, k310]
keywords: [signed mandate, user intent, pre-authorization context, A2A, MCP tool results, AIVSS, MAESTRO]
related:
  - sources/arxiv-ap2-beyond-the-mandate-2608.23858.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - sources/arxiv-recognition-without-enforcement-2608.28502.md
maturity: draft
created: 2026-08-26
updated: 2026-08-31
---

## Relations

- `@sources/arxiv-ap2-beyond-the-mandate-2608.23858.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`

## Raw Concept

The question: does a validly signed mandate prove the user wanted what it encodes? Answer from AP2 v0.2's systematic security analysis [Source: wiki/sources/arxiv-ap2-beyond-the-mandate-2608.23858.md]: **no** — signatures cover transaction data *after* shaping; the A2A messages and MCP tool results that shaped it stay unsigned.

## Narrative

A signature is an integrity proof for bytes, not an intent proof for decisions. In agent-mediated transactions the decision content is assembled upstream of signing — catalog reads, tool results, agent-to-agent messages, prompt-injectable surfaces. Manipulate that pre-authorization context and a mandate gets signed over action the user never intended; every downstream cryptographic check then passes.

Policy for CCC (ADOPT):

1. **Never treat a signed artifact as proof of intent.** Signature validity answers "was this altered after signing", not "did the principal want this".
2. **Bind pre-commit context.** The exact approved request + the state it was approved against must be revalidated at effect time — same shape as AID-Guard K302 revalidate-at-commit (`@concepts/execution-fidelity-irreversible-agent-invariants.md`).
3. **Treat unsigned shaping inputs as attacker-controllable** in any threat model: A2A messages, MCP tool results, catalog data.
4. **No PoCs in wiki or briefs** — the paper's five demonstrations stay in the paper.

Dual-ID: CCC K285 (`@concepts/signed-mandate-mcp-protocol-enforcement.md`) = in-protocol signed-mandate enforcement; CCC K310 = everything outside the signature. Complementary, do not merge.

| Confidence | `[CONFIRMED]` — paper testbed across all five deployment architectures; 48 threats / 8 High by AIVSS |
|------------|------------|

## Snippets

> "valid mandate signatures alone do not ensure that an agent-mediated transaction reflects the user's intent when its pre-authorization context is manipulated" [Source: arXiv 2608.23858 abstract]
