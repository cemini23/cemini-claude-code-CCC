---
title: "InterSAGE — trust-native Internet-of-Agents protocol (DeepKernel Lab)"
type: entity
tags: [entity, tool, ioa, protocol, identity, k278]
keywords: [k278, InterSAGE, AIC, DID, verifiable-credential, capability-attenuation, internet-of-agents, deepkernel, tsinghua]
related:
  - sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md`
- `@concepts/intersage-trust-native-ioa-protocol.md`

## Raw Concept

Phase-0 entity for CCC K278 — InterSAGE protocol suite.

## Narrative

**No public SPDX clone found** — positioning paper, no released repo. **ADOPT** as policy/pattern: AIC four-dimensional identity (developer × code package × operator × deployment context), DID-bound capability VC manifests, monotonic capability attenuation + two-tier access control, kernel-mediated cryptographic audit trails. **Atto-priority** steal (identity + capability-bound discovery + audit trails for extract solvers). Runtime **`wont_wire`** — implement the pattern, no dependency.

**Phase-0:** `scripts/adopt_k278_phase0.sh`
