---
title: "Output attestation + delegation ancestry — two-layer post-incident evidence (CCC K328)"
type: concept
tags: [concept, attestation, delegation, ancestry, co-signed-dag, output-binding, edge-authorization, policy, k328]
keywords: [output attestation, delegation ancestry, co-signed DAG, child-key compromise, deployer-side binding, edge authorization, post-incident evidence, 2608.30387]
related:
  - sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/intersage-trust-native-ioa-protocol.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

The question: after an incident in a multi-agent system, how do we answer (1) which deployer released these exact bytes and (2) was each cross-deployer edge authorized — when there is no shared authority, public log, or precommitted workflow? Answer from K328 [Source: wiki/sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md]: **two independently verifiable evidence layers** — deployer-runtime output-hash signatures + edge-authorization ancestry — instead of a stronger credential.

## Narrative

**Credentials ≠ later output bytes.** A credential records a principal and a permission at issuance time; it does not bind the bytes a runtime later releases, and it does not prove both deployers authorized a dynamically created edge. Two gaps remain for dynamic paths:

- **G1 (output binding):** a credential does not attest bytes later released by a runtime.
- **G2 (edge consent):** under child-key compromise, a child-only signature on a new parent reference does not demonstrate that the named parent approved the relationship.

**The two-layer design (ADOPT policy):**

1. **Output attestation (Layer 1).** A trusted **deployer runtime** (never the LLM agent) hashes each released output and signs the complete record with deployer + validity metadata. This records what was released under a trusted-runtime assumption. **It does not detect or prevent prompt injection — output attestation ≠ behavioral safety.** Signatures provide tamper-evident evidence of released bytes and the delegation path for investigation and targeted revocation.
2. **Ancestry evidence (Layer 2).** Each delegation record binds issuer, child instance, proposed parent, depth, expiry, nonce, evidence construction. For cross-deployer edges, a **co-signed DAG** requires **both endpoint deployers** to sign the complete edge manifest (construction id, co-signer set, child nonce).

**The key result (child-key compromise):** a signed linked list and a Merkle-chain variant use only the child's authorization for an edge → the compromised child forges a parent binding (win probability 1). The co-signed DAG additionally requires the **parent's signature on the edge transcript** → forgery requires breaking SUF-CMA signatures (negligible). **Signed list / Merkle-chain do not reject unauthorized parent binding; co-signed DAG does.**

Trust boundary (bounded by construction): deployer runtime, signing key, admission-controlled registry, verifier. Out of scope: prompt-injection prevention, endpoint collusion, cross-verifier replay, streaming-order semantics, open self-enrollment, semantic safety of output.

**CCC policy lines (wire `policy_wired`):**

- Sign released output bytes at the **runtime**, with a trusted-runtime assumption — the agent neither holds the signing key nor populates the signed fields.
- For cross-deployer edges, **require parent co-signature** (co-signed DAG), not child-only chains — especially after any key-compromise suspicion.
- Treat attestation as **post-incident audit/attribution evidence**, never as a behavioral-safety control (pairs `@concepts/mandate-signature-vs-preauth-intent.md` K310: unsigned shaping inputs remain attacker-controllable; `@concepts/signed-mandate-mcp-protocol-enforcement.md` K285: signed mandates prove integrity of bytes, not intent; `@concepts/intersage-trust-native-ioa-protocol.md` K278: edge-level trust).
- **Cybersec steal** — two-layer attestation only (zero exploit text, no attack templates).

Cost is measured and small: ancestry checks 24.3–499.2 µs/hop; Signed-DAG adds 42.3 ms (5.5%) end-to-end over a no-evidence path in a live MCP/A2A/LLM workflow; 1,000/1,000 AWS paths verified (issuance 3.651 ms, verification 5.015 ms, excluding TLS/KMS/model latency).

| Confidence | `[CONFIRMED]` — protocol + measurements from the paper; policy is CCC synthesis |
|------------|------------|
