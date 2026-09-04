---
title: "Natural Language Interaction Protocol (NLIP) — agent interop envelope (CCC K344)"
type: concept
tags: [concept, nlip, protocol, interoperability, ecma, k344]
keywords: [2609.04135, NLIP, semantic envelope, HTTP, WebSocket, AMQP, Ecma standard]
related:
  - sources/arxiv-nlip-natural-language-interaction-protocol-2609.04135.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-04_ccc-k342-k345-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-04
updated: 2026-09-04
---

## Relations

- `@sources/arxiv-nlip-natural-language-interaction-protocol-2609.04135.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-04_ccc-k342-k345-sip-ready.md`

## Raw Concept

K344: NLIP standardizes a **semantic message envelope** for NL-first agent interaction across heterogeneous stacks — transport-agnostic (HTTP/WS/AMQP).

## Narrative

**Awareness, not MCP replacement.** NLIP sits above transports; CCC keeps MCP/tool harness as primary execution surface. Use as interop vocabulary when routing multi-org agent messages (pairs K271 gateway). CC0 Ecma draft = digest pointer only; no catalog mirror. Runtime **`wont_wire`**.

## Snippets

> "NLIP envelope ≠ MCP tool schema — complementary layers." [Source: CCC K344 policy]
