---
title: "Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation (CCC K395)"
type: concept
tags: [concept, k395, cybersec]
keywords: [2609.28586, k395]
related:
  - sources/arxiv-agent-approval-laundering-2609.28586.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-25_ccc-k395-agent-approval-laundering-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-25
updated: 2026-09-25
---

## Relations

- `@sources/arxiv-agent-approval-laundering-2609.28586.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-25_ccc-k395-agent-approval-laundering-sip-ready.md`

## Raw Concept

K395: Cybersec-primary ADOPT policy — arXiv 2609.28586.

## Narrative

**Agent approval laundering** — a user- or policy-**approved** tool invocation can still cause **transitive** effects outside the approved action envelope (follow-on tools, side channels, delegated sub-agents). Authorization at the **first hop** is not **effect closure** (pairs K310 pre-auth intent / K302 AID-Guard / K333 untrusted-model delegation). **Cybersec-primary**; **No PoCs / no exploit recipes.** No clone. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Coding-agent approval interfaces bind a human decision to a command or tool call, whereas developer tools execute the transitive workflow that invocation activates. We call the resulting structural record-coverage failure approval laundering: a durable record faithfully names the entry invocation yet omits effects exercised within its workflow." [Source: https://arxiv.org/abs/2609.28586 (retrieved 2026-09-25)]
