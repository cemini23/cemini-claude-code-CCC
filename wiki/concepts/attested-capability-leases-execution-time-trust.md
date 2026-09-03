---
title: "Attested capability leases — execution-time trust for remote MCP (CCC K337)"
type: concept
tags: [concept, mcp, capability-lease, execution-trust, cybersec, policy, k337]
keywords: [2609.02690, ACLE-MCP, post-authorization execution trust gap, Execution Gate, workload appraisal, OAuth]
related:
  - sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md
  - concepts/untrusted-model-delegation-governance.md
  - concepts/output-attestation-and-delegation-ancestry.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
  - entities/patterns/external-reference-monitor.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md`
- `@concepts/untrusted-model-delegation-governance.md`
- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

K337 (arXiv 2609.02690): OAuth proves delegated access, not that the **current provider workload** executing a protected MCP call matches the relying party's trust assumptions.

## Narrative

**Post-authorization execution trust gap.** After OAuth succeeds, execution may shift to a substituted workload, stale attestation, copied authority, or undeclared proxy — while authorization remains valid.

**Capability lease + Execution Gate.** Issue a short-lived, sender-constrained lease binding workload appraisal, op/object/param bounds, freshness, downstream constraints; consume at the **Execution Gate** immediately before protected tool logic. Complements K328 output attestation (bytes released) and K333 scoped delegation (who may act) — focus here is **who executes** at invocation time.

**Wire:** `policy_wired` — no public SPDX clone; no PoCs. Pairs K285/K326/K328/K333. Cybersec-primary steal.

## Snippets

> "Invocation-time binding between call authority and current workload state is a practical complement to OAuth-protected remote tool use." [Source: arXiv 2609.02690 — paraphrase]
