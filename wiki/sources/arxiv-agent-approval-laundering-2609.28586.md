---
title: "Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation (CCC K395)"
type: source
tags: [source, k395, cybersec]
keywords: [2609.28586, k395, approval-laundering]
related:
  - concepts/agent-approval-laundering-transitive-effects.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-25_ccc-k395-agent-approval-laundering-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-09-25
updated: 2026-09-25
---

## Relations

- `@concepts/agent-approval-laundering-transitive-effects.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-25_ccc-k395-agent-approval-laundering-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation |
| **arXiv** | 2609.28586 (2026-09) |
| **Retrieved** | 2026-09-25 |

## Narrative

**Verdict: Cybersec-primary ADOPT policy.**

**Agent approval laundering** — a user- or policy-**approved** tool invocation can still cause **transitive** effects outside the approved action envelope (follow-on tools, side channels, delegated sub-agents). Authorization at the **first hop** is not **effect closure** (pairs K310 pre-auth intent / K302 AID-Guard / K333 untrusted-model delegation). **Cybersec-primary**; **No PoCs / no exploit recipes.** No clone. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation — CCC K395 synthesis." [Source: arXiv 2609.28586 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.28586-agent-approval-laundering-transitive-effects.pdf` |
