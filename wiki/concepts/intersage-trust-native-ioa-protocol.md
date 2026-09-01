---
title: "InterSAGE — trust-native Internet-of-Agents protocol (K278)"
type: concept
tags: [concept, ioa, identity, discovery, trust-negotiation, accountability, k278]
keywords: [2608.13030, InterSAGE, AIC, Agent-Identity-Card, DID-bound-VC, capability-attenuation, kernel-audit, internet-of-agents]
related:
  - sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md
  - entities/tools/intersage.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@cybersecurity-wiki/concepts/intersage-trust-native-ioa-protocol.md"
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md
  - concepts/output-attestation-and-delegation-ancestry.md
  - sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-14
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md`
- `@entities/tools/intersage.md`
- `@concepts/mcp-claim-validation-and-parameter-grounding.md`
- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md`

## Raw Concept

Communication protocols (MCP, A2A, ANP, AG-UI) standardize how agents *exchange messages*, but not how an agent **proves what it is, what it is authorized to do, whether advertised capabilities are genuine, or how actions stay accountable after delegation**. InterSAGE supplies that missing trust substrate.

## Narrative

InterSAGE is a **positioning paper** (design rationale for later specs/formalization, no production system). Four layers → nine security aspects: **Persistent Identity (L0)** / **Discovery (L1)** / **Trust Negotiation (L2)** / **Accountability (L3)**.

### Steal (ADOPT)

1. **Agent Identity Card (AIC) — four-dimensional identity binding.** Bind developer × code package × operator × deployment context, each with an independent signature. One compromised dimension cannot impersonate the others. (SPIFFE, OAuth client creds, DID, OIDC-A each bind a *single* dimension.)
2. **Capability-aware discovery via DID-bound Verifiable Credential manifests.** Skill/tool advertisements become VCs verified for **issuer provenance, subject binding, permission alignment, freshness** before interaction begins. Discovery results are claims to check, not facts.
3. **Monotonic capability attenuation + two-tier access control.** Delegation chains only ever *shrink* capability; least privilege is a signed structural invariant, while application-level policy stays independent.
4. **Kernel-mediated cryptographic audit trails.** Usage / delegation / execution traces bound to identity **without a consensus ledger** — viable in resource-constrained or fully decentralized environments.
5. **Positioning discipline.** Defines trust primitives *alongside* (not replacing) MCP/A2A/ANP/AG-UI — communication protocols evolve independently while trust semantics stay explicit, portable, verifiable.

### Atto angle (operator note)

InterSAGE is the priority steal for Atto: extract solvers need **AIC-style identity** (which agent/version produced which artifact), **capability-bound discovery** (only call solvers whose advertised capability is verified and permission-aligned), and **kernel-mediated audit trails** (per-extract provenance for downstream review). No public SPDX clone → policy wire only; implement the *pattern*, not a dependency.

| Verdict | **ADOPT** AIC 4-D identity, DID-bound capability VCs, monotonic attenuation, kernel-mediated audit. Policy_wired; runtime `wont_wire` (no artifact). |

## Snippets

> "An attacker who compromises the operator's deployment cannot impersonate a different developer or substitute a different code package, because each dimension carries its own independently verifiable signature." — [Source: arXiv 2608.13030 p.3]

> "InterSAGE does not replace existing agent protocols such as MCP, A2A, ANP, or AG-UI; it defines the missing trust-relevant primitives that those protocols need." — [Source: arXiv 2608.13030 p.1]
