---
title: "Mandato — protocol-level enforcement of digitally signed mandates on MCP agent actions"
type: source
tags: [source, arxiv, mcp, authorization, governance, audit, k285]
keywords: [2608.14074, Mandato, signed-mandate, hash-chained-audit, MCP-proxy, PDP-PEP, EU-AI-Act, eIDAS]
related:
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - entities/tools/mandato.md
  - entities/patterns/signed-mandate-mcp-proxy.md
  - concepts/enterprise-mcp-auth-gateway.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@entities/tools/mandato.md`
- `@entities/patterns/signed-mandate-mcp-proxy.md`
- `@concepts/enterprise-mcp-auth-gateway.md` — K271 MCP auth gateway: Mandato adds signed-artifact authority + evidentiary log
- `@concepts/intersage-trust-native-ioa-protocol.md` — K278 InterSAGE identity/VC trust protocol

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails |
| **arXiv** | 2608.14074 |
| **Author** | Giovanni Racioppi (Hyperlabs, Italy) |
| **Code** | none public — specification-driven, no SPDX clone |
| **Retrieved** | 2026-08-18 |

## Narrative

MANDATO reifies agent authorization as a first-class, digitally signed artifact — the **mandate** — and enforces it at an MCP-transparent proxy that the agent cannot route around. A mandate is a tuple `M = (id, P, A, Σ, Γ, V, D, σ_P)` binding a principal, an agent workload identity, a scope of tool grants, contextual conditions, a validity window, and a delegation policy, signed by the principal (JAdES/JWS). Each grant `g = (τ, Π, κ, q)` names a tool, a set of parameter constraints drawn from a deliberately **non-Turing-complete** constraint language (equality, enumerated sets, numeric ranges, string prefixes, presence/absence), an oversight class `κ ∈ {auto, confirm, forbid}`, and an optional quota.

**Decision semantics** are deterministic and LLM-free: a call is PERMIT (admissible + `auto`), ESCALATE (admissible + `confirm`), or DENY otherwise. Deny-by-default is structural — absence of a mandate, an expired chain, an unverifiable signature, an unknown tool, or an out-of-language constraint all collapse to DENY. Delegation enforces **monotone attenuation** (a sub-mandate can only narrow scope, widen conditions, shrink validity, never weaken oversight). Revocation and ratification are signed acts appended to the log; history is corrected by appending, never editing.

**Reference architecture** splits PDP/PEP (XACML pattern): the in-line interceptor is minimal and fail-closed; the decision point evaluates `δ` against the mandate store, revocation view, and quota counters. Upstream MCP servers accept sessions only from the proxy's mTLS workload identity, so enforcement is non-bypassable. Every decision produces a record `r_i = (t_i, c_i↓, ℳ_i^ref, δ_i, π_i, h_i)` with hash-chained head `h_i = H(h_{i−1} ∥ r_i)`, selective hash commitments of sensitive argument values (GDPR minimization), and periodic Merkle checkpoints anchored via RFC 3161 (baseline) → qualified timestamps/seals (target).

**Compliance mapping** is explicit: EU AI Act Arts. 12 (record-keeping — completeness + integrity demonstrable by a third party) and 14 (human oversight — `κ` makes oversight a property of the authorization artifact, not a UX choice), GDPR accountability/minimization, NIS2, eIDAS 2 (QTSP roadmap). **Status is a system under construction**: spec v0.6 with 170+ numbered requirements, 22+ relational tables, 22 use cases, milestones M0–M8.5; empirical results are a falsifiable evaluation plan (p95 enforcement overhead ≤ 5% of median tool time; 100% audit completeness; verification cost on 10⁶ records), not reported numbers.

**Limitations (stated):** bounds authority not competence; legal reading as delegation is an alignment claim not settled doctrine; anchoring is tamper-evident not tamper-proof within a checkpoint interval; multi-proxy/federated composition unsolved for the single-authority case.

| Verdict | **ADOPT** digitally signed mandate artifacts evaluated at an MCP proxy + append-only hash-chained audit. No public SPDX clone → **policy only**. **Atto-priority** (pairs K278 InterSAGE, K271 MCP auth gateway, K239 execution fidelity). |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.14074-mandato-protocol-level-enforcement-of-digitally.pdf` |
