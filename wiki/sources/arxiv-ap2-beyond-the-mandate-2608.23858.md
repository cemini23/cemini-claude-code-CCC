---
title: "Beyond the Mandate — systematic security analysis of AP2 v0.2 (CCC K310)"
type: source
tags: [source, arxiv, security, payments, ap2, a2a, mcp, threat-model, k310]
keywords: [2608.23858, AP2, Agent Payments Protocol, MAESTRO, AIVSS, mandate, pre-authorization, prompt injection]
related:
  - concepts/mandate-signature-vs-preauth-intent.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2) |
| **arXiv** | 2608.23858 [cs.CR] |
| **Authors** | Avital Aviv, Parth A. Gandhi, Ron Bitton, Asaf Shabtai (Ben-Gurion University + Intuit) |
| **Code** | None adopted — paper testbed + scanner are **not** cloned as the artifact (policy only; no PoCs in wiki) |
| **Retrieved** | 2026-08-26 |

## Narrative

First threat model spanning AP2 v0.2's transaction lifecycle, trust boundaries, and deployment architectures. The core finding for CCC: **valid mandate signatures do not prove user intent** when the pre-authorization context is manipulated. AP2 signs Checkout/Payment mandates after context shaping; A2A messages and MCP tool results that *determine* what gets signed stay unsigned.

Method: five lifecycle phases × five deployment architectures; MAESTRO model with four threat actors, eleven attack surfaces, eighteen adversary capabilities, six attacker goals → **48 threats in five attack families**, AIVSS-scored, **8 reach High band in at least one architecture**. The authors built a testbed across all five architectures and demonstrated five PoC attacks covering all eight High threats plus mitigations, and ship a deployment-aware scanner (static, cross-role consistency, adversarial checks).

AP2 v0.1 had replay + prompt-injection findings; v0.2 adds Human-Not-Present flows that widen the surface. Dual-ID vs **CCC K285** (`@concepts/signed-mandate-mcp-protocol-enforcement.md`): K285 covers signed-mandate enforcement inside the protocol; **K310 covers everything the signature does not see** — do not merge.

| Verdict | **ADOPT policy**: never treat a signed mandate as proof of intent; bind pre-commit/pre-auth context. No PoCs, no exploit text, no scanner clone. `wire_status: policy_wired`. Cybersec steal brief written. |
|---------|---------|

## Snippets

> "Our analysis shows that valid mandate signatures alone do not ensure that an agent-mediated transaction reflects the user's intent when its pre-authorization context is manipulated." [Source: arXiv 2608.23858 abstract]

> "an attacker may not need to forge a mandate or receipt to cause harm; instead, the attacker may manipulate the agent's context, tools or communications so that a validly signed mandate encodes an unsafe or unintended action." [Source: arXiv 2608.23858 §1]

> "The resulting catalog contains 48 threats spanning five attack families … identifying eight that reach the High band in at least one architecture." [Source: arXiv 2608.23858 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.23858-beyond-the-mandate-a-systematic-security-analysi.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
