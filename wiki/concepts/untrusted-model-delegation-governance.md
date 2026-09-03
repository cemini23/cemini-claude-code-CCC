---
title: "Untrusted-model delegation governance — external authorization broker (CCC K333)"
type: concept
tags: [concept, delegation, authorization, untrusted-model, governance, cybersec, policy, k333]
keywords: [2609.00267, untrusted model property, authorization broker, scoped delegation, confused deputy, token replay, prompt injection escalation, compromised sub-agents, LangGraph, MCP]
related:
  - sources/arxiv-delegation-without-trust-2609.00267.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/output-attestation-and-delegation-ancestry.md
  - concepts/attested-capability-leases-execution-time-trust.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
  - entities/patterns/external-reference-monitor.md
  - sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-02
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-delegation-without-trust-2609.00267.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@concepts/attested-capability-leases-execution-time-trust.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

The question: how do you delegate work to sub-agents and tools when the orchestrating LLM may be fully prompt-injected? Answer from K333 [Source: wiki/sources/arxiv-delegation-without-trust-2609.00267.md]: adopt the **untrusted-model property** — security must not depend on model reasoning — and enforce **scoped delegation through an external authorization broker** outside the model loop.

## Narrative

**Untrusted-model property.** Design every multi-agent and MCP workflow as if the LLM is adversarially controlled. Authorization, scope narrowing, and audit must be **external** to model inference. Prompt-layer defenses and "the model should refuse" are not architectural boundaries (pairs `@concepts/recognition-vs-enforcement-instruction-arbitration.md` K326).

**External authorization broker.** A runtime decision point evaluates each candidate delegation or tool effect against policy **before** execution. The model proposes; the broker permits or denies. Sub-agents receive **scoped delegation artifacts** (task, tools, TTL, principal binding) — not replayable bearer credentials sitting in context where injection can exfiltrate or widen them.

**Four threat classes to design against (names only — no PoCs):**

| Threat | Design failure |
|--------|------------------|
| Confused deputy | Sub-agent executes for wrong principal — identity not bound at broker |
| Token theft / replay | Long-lived bearer token reused outside intended window |
| PI privilege escalation | Injected instructions widen tool scope the operator never approved |
| Compromised sub-agents | Over-broad sub-agent authority amplifies one breach |

**Framework gap.** LangGraph, CrewAI, AutoGen, and raw MCP wiring expose orchestration and tools but typically **lack a non-bypassable broker** at the delegation boundary. MCP is transport + schema; it is not, alone, scoped delegation under an untrusted model (pairs `@concepts/signed-mandate-mcp-protocol-enforcement.md` K285: signed mandates at proxy; `@concepts/mandate-signature-vs-preauth-intent.md` K310: unsigned shaping inputs; `@concepts/output-attestation-and-delegation-ancestry.md` K328: post-incident edge evidence).

**CCC policy lines (wire `policy_wired`):**

- **Treat the model as untrusted** in every threat model for delegated agents and MCP tools.
- **Never gate authority inside model reasoning** — broker outside the LLM loop; fail-closed on missing/expired scope.
- Prefer **scoped sub-agent delegation** over bearer credentials the model can hold, replay, or pass downstream.
- **Cybersec-primary steal** — authorization broker pattern only; **no attack templates, PoCs, or exploit text** anywhere in wiki/briefs.
- VotalAI LLM Shield = production reference narrative only; **no public SPDX repo** → no clone; runtime `wont_wire`.

| Confidence | `[CONFIRMED]` — threat taxonomy from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Bearer credentials + model-gated actions fail all four delegation threats under the untrusted-model property." [Source: wiki/sources/arxiv-delegation-without-trust-2609.00267.md — K333 policy line]

> "Authorization must live in an external broker — not in model reasoning." [Source: wiki/sources/arxiv-delegation-without-trust-2609.00267.md — K333 policy line]
