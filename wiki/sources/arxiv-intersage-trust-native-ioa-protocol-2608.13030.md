---
title: "InterSAGE — the secure and verifiable interoperability protocol for an Internet of Agents"
type: source
tags: [source, arxiv, ioa, identity, discovery, trust-negotiation, accountability, k278]
keywords: [2608.13030, InterSAGE, AIC, Agent-Identity-Card, DID, verifiable-credential, capability-attenuation, audit-trail, DeepKernel]
related:
  - concepts/intersage-trust-native-ioa-protocol.md
  - entities/tools/intersage.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - "@cybersecurity-wiki/sources/arxiv-2608-13030-intersage.md"
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@concepts/intersage-trust-native-ioa-protocol.md`
- `@entities/tools/intersage.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents |
| **arXiv** | 2608.13030 |
| **Authors** | Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu (DeepKernel Lab, Tsinghua) |
| **Code** | None public — positioning paper; no public SPDX clone found → **policy only** |
| **Retrieved** | 2026-08-14 |

## Narrative

Trust-native protocol suite supplying the **trust substrate** that communication-level agent protocols (MCP, A2A, ANP, AG-UI) leave unspecified. Organized as **four layers**: Persistent Identity (L0), Discovery (L1), Trust Negotiation (L2), Accountability (L3), covering **nine security aspects** across the agent lifecycle.

Four layer-aligned design primitives:

1. **Agent Identity Card (AIC)** — persistent identity with **four-dimensional binding**: developer, code package, operator, deployment context. Each dimension carries an independently verifiable signature, so compromising one dimension can't impersonate another.
2. **Capability-aware discovery** — skill/tool advertisements become **DID-bound Verifiable Credential manifests**, verified for issuer provenance, subject binding, permission alignment, freshness *before* interaction begins.
3. **Trust negotiation** — **monotonic capability attenuation** chains + two-tier access control (A2A-aligned); least privilege becomes a **signed structural invariant** while preserving application-level policy independence.
4. **Kernel-mediated cryptographic audit trails** — usage, delegation, and execution traces bound to agent identity **without a consensus ledger**, viable in resource-constrained / decentralized environments.

Positioning: explicitly does **not** replace MCP/A2A/ANP/AG-UI; defines the missing trust-relevant primitives those protocols need. Compared against **50+ related efforts** (SPIFFE/SPIRE, OAuth 2.0 client creds, W3C DIDs, OIDC-A, AgentMesh, etc.).

| Verdict | **ADOPT** AIC four-dimensional identity, DID-bound capability VCs, monotonic attenuation, kernel-mediated audit. **Atto-priority** (extract-solver identity + capability-bound discovery + audit trails). No public SPDX clone → policy only. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.13030-intersage-the-secure-and-verifiable-interoperabi.pdf`
