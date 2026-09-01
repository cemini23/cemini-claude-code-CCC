---
title: "Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems (CCC K328)"
type: source
tags: [source, arxiv, attestation, delegation, ancestry, co-signed-dag, multi-agent, policy, k328]
keywords: [2608.30387, output attestation, delegation ancestry, co-signed DAG, child-key compromise, edge authorization, A2A, MCP, deployer-side binding]
related:
  - concepts/output-attestation-and-delegation-ancestry.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/intersage-trust-native-ioa-protocol.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems |
| **arXiv** | 2608.30387 (cs.CR, 2026-08-31) |
| **Authors** | Lifei Liu, Haoran Yu (Independent Researcher, Seattle, WA) |
| **Venue** | arXiv preprint, 9 pages |
| **Code** | Anonymous artifact package (`anonymous.4open.science/r/cscloud-artifacts-6342`); no public repo / no SPDX found → **policy only, no clone** |
| **Retrieved** | 2026-09-01 |

## Narrative

**Verdict: ADOPT policy.** Two post-incident evidence questions: (1) which deployer released these exact bytes, and (2) was each cross-deployer edge authorized? Credentials establish who may act at issuance time; they need **not** bind later output bytes or prove both deployers authorized a dynamically created edge.

Two-layer design without a shared authority, public log, or precommitted workflow:

- **Layer 1 — output attestation:** a trusted **deployer runtime** (not the LLM agent) hashes each released output and signs the complete record (deployer + validity metadata). This records released bytes; it does **not** prevent prompt injection. **Output attestation ≠ behavioral safety.**
- **Layer 2 — ancestry evidence (edge authorization):** each delegation record binds a parent; for cross-deployer edges a **co-signed DAG** requires both endpoint deployers to sign the edge manifest.

The key comparative result: after **child-key compromise**, a signed linked list and a Merkle-chain variant accept an unauthorized parent binding (only the child signs), whereas the **co-signed DAG rejects it** because the parent must authorize the edge (Theorem 2, edge-authorization game; negligible win probability under SUF-CMA + collision resistance).

Measurements: ancestry-only checks 24.3 (LINKED-LIST) / 72.7 (MERKLE) / 499.2 µs (SIGNED-DAG) per hop at depth 5; live local MCP/A2A/LLM workflow (E12) — 30/30 tasks pass complete verification per condition, Signed-DAG mean 813.1 ms vs 770.8 ms no-evidence (+5.5%); three-zone AWS (E11) — 1,000/1,000 co-signed-DAG paths verified, issuance 3.651 ms, verification 5.015 ms (excluding TLS/KMS/model latency). In E12, the controlled child-key-only claim is **rejected** only under SIGNED-DAG.

Bounded scope (Table II/III): trust = deployer runtime, signing key, admission-controlled registry, verifier. Out of scope: prompt-injection prevention, endpoint collusion, cross-verifier replay, streaming-order semantics, open self-enrollment. Signatures support **post-incident audit and attribution**, not prevention.

CCC policy lines: sign released output bytes at the runtime; require parent co-signature for cross-deployer edges; audit before revocation. Pairs K278 InterSAGE (edge trust), K285 Mandato (signed mandates), K310 AP2 (pre-auth intent — unsigned shaping inputs stay attacker-controllable). **Cybersec steal** (two-layer attestation; zero exploit text). `policy_wired`.

| Confidence | `[CONFIRMED]` — protocol design + measurements reported in the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Credentials establish who may act, but need not bind them to later output bytes or prove both deployers authorized a dynamically created edge." [Source: arXiv 2608.30387 abstract]

> "After child-key compromise, the single-signer designs permit an unauthorized parent binding, whereas the co-signed DAG rejects it because the parent must authorize the edge." [Source: arXiv 2608.30387 abstract]

> "We do not claim that the construction prevents agent compromise; it makes the resulting outputs and delegation path auditable." [Source: arXiv 2608.30387 §I]

> "Every attested task passed complete verification … all 1,000 valid co-signed-DAG paths verified; issuance averaged 3.651 ms and complete verification 5.015 ms." [Source: arXiv 2608.30387 §VI-D]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.30387-attesting-outputs-and-delegation-ancestry-in-mul.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
