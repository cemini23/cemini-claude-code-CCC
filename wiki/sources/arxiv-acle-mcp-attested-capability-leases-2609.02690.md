---
title: "ACLE-MCP — attested capability leases for execution-time trust (CCC K337)"
type: source
tags: [source, arxiv, mcp, capability-lease, execution-trust, cybersec, policy, k337]
keywords: [2609.02690, ACLE-MCP, post-authorization execution trust gap, capability lease, Execution Gate, OAuth, remote MCP, workload appraisal]
related:
  - concepts/attested-capability-leases-execution-time-trust.md
  - concepts/untrusted-model-delegation-governance.md
  - concepts/output-attestation-and-delegation-ancestry.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@concepts/attested-capability-leases-execution-time-trust.md`
- `@concepts/untrusted-model-delegation-governance.md`
- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use |
| **arXiv** | 2609.02690 (2026-09-02) |
| **Authors** | Peking University (Ding, Luo, Chen, Shen, Wu) |
| **Code** | Runnable prototype (Keycloak/OIDC, MCP Python SDK, optional vTPM) — **no public SPDX repo** → no clone |
| **Retrieved** | 2026-09-03 |

## Narrative

**Verdict: Cybersec-primary + CCC ADOPT policy — OAuth authorizes access, not the workload that executes.**

Remote MCP lets agents invoke provider-side tools after OAuth, but valid authorization does not prove the **current provider-side workload** is the one the relying party intended to trust. The **post-authorization execution trust gap** covers substituted workloads, stale attestation, authority transferred from another sender, and undeclared downstream components.

**ACLE-MCP** couples delegated authorization, workload appraisal, and resource-side **Execution Gate** admission. For protected calls it issues a short-lived, **sender-constrained capability lease** binding expected workload, freshness, operation/object/param bounds, downstream constraints, and receipt obligations. The gate consumes the lease immediately before protected tool logic.

Evaluation: weaker modes leave distinct post-authorization attack families open; full ACLE-MCP blocks evaluated families while preserving benign tasks (+25.7% pooled p95 latency vs OAuth-only in local agent extension). **No public repo → policy only.** **Zero PoC / attack recipe text in wiki.** Pairs K285 Mandato, K328 output attestation, K326 external monitor, K333 untrusted-model delegation.

| Confidence | `[CONFIRMED]` — problem statement and architecture from paper; policy is CCC synthesis |

## Snippets

> "OAuth answers whether a client may access a resource — not whether the concrete provider-side workload executing a later invocation is still the execution unit the relying party intended to trust." [Source: arXiv 2609.02690]

> "For protected calls, ACLE-MCP issues a short-lived, sender-constrained capability lease … consumed at the Execution Gate immediately before protected tool logic begins." [Source: arXiv 2609.02690 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.02690-acle-mcp-attested-capability-leases-for-executio.pdf` |
