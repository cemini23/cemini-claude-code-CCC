---
title: "Signed mandate MCP protocol enforcement (K285)"
type: concept
tags: [concept, mcp, authorization, governance, signed-mandate, audit, k285]
keywords: [2608.14074, Mandato, signed-mandate, hash-chained-audit, PDP-PEP, deny-by-default, monotone-attenuation, EU-AI-Act]
related:
  - sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md
  - entities/tools/mandato.md
  - entities/patterns/signed-mandate-mcp-proxy.md
  - concepts/enterprise-mcp-auth-gateway.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md`
- `@entities/tools/mandato.md`
- `@entities/patterns/signed-mandate-mcp-proxy.md`
- `@concepts/enterprise-mcp-auth-gateway.md` — K271 MCP auth gateway: transport/auth; Mandato adds signed-artifact authority + evidentiary log
- `@concepts/intersage-trust-native-ioa-protocol.md` — K278 InterSAGE identity + capability-bound discovery
- `@concepts/execution-fidelity-irreversible-agent-invariants.md` — K239: Mandato's deny-by-default + oversight class is the authorization-side counterpart to irreversible-execution invariants

## Raw Concept

Authorization for agent actions lives in application code, is unsigned, non-auditable, and enforced by the same code that executes. What if authority were a signed, machine-readable artifact enforced at a protocol chokepoint the agent cannot route around — with every decision chained into evidentiary log?

## Narrative

Mandato (arXiv 2608.14074) reifies authorization as a first-class **digitally signed mandate** and enforces it at an **MCP-transparent proxy**. The mandate binds a principal, an agent workload identity, a scope of tool grants (each with a non-Turing-complete parameter-constraint language), contextual conditions, a validity window, and a delegation policy. Decision semantics are **deterministic and LLM-free** — permit / escalate / deny, deny-by-default structurally.

### Steal (ADOPT)

1. **Authorization as a signed artifact, not application code.** A mandate is inspectable, versionable, signable, delegable, revocable independently of the code that implements the agent. Signing a mandate is a legal act (modeled on civil-law delegation), so auditors and lawyers can read it.
2. **Enforce at a protocol chokepoint the agent can't route around.** Deploy as an MCP-transparent proxy that terminates both sides; upstream servers accept only the proxy's mTLS workload identity. Completeness and non-bypassability become architectural, not contractual.
3. **Separate PDP from PEP.** The in-line enforcement point is minimal and fail-closed; the decision point evaluates against the mandate store + revocation view + quota counters. Escalations park the call via MCP task semantics and route to a human console that shows the *mandate clause* — oversight is against an authorization, not a raw JSON blob (AI Act Art. 14 "meaningful" oversight).
4. **Closed constraint language — decidability first.** Predicates over equality / enumerated sets / numeric ranges / string prefixes / presence-absence. An authorization decision must be explainable in one line per predicate and must not itself become an unauditable program.
5. **Monotone attenuation for delegation.** A sub-mandate can only narrow scope, widen conditions, shrink validity, and never weaken oversight (confirm cannot become auto downstream). The chain, not the leaf, is the unit of authority.
6. **Append-only, hash-chained audit log with external anchoring.** Every decision → a record with hash-chained head; sensitive argument values committed as hashes (GDPR minimization); periodic Merkle checkpoints under RFC 3161 → qualified timestamps (eIDAS). Ratification corrects history by appending, never editing. An auditor verifies integrity/completeness without trusting the operator.
7. **Deny-by-default is structural.** No mandate, expired chain, unverifiable signature, unknown tool, or out-of-language constraint all collapse to DENY.

### Why this pairs K278 (InterSAGE) and K271 (MCP auth gateway)

K271's enterprise MCP auth gateway adds transport-level auth and identity; Mandato adds the **authority artifact** on top — what the identified caller is *allowed* to do, signed and evidenced. K278 InterSAGE binds identity via DID + capability VCs and monotonic capability attenuation; Mandato's mandate is the enforcement-plane complement to InterSAGE's trust-plane identity. K239 execution-fidelity invariants gate irreversible transitions; Mandato gates *authorization* with the same deny-by-default discipline.

### Local adopt

- **No clone** — specification-driven (v0.6), no public SPDX repo. **Policy only.** Atto-priority: the signed-mandate proxy pattern maps directly onto extract-solver tool authorization.

| Verdict | **ADOPT** signed mandate chain at MCP proxy; parameter constraints + TTL + principal binding; hash-chained permit/deny audit; separated decision/enforcement points. `policy_wired`; no runtime clone. |
