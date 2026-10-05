---
title: "Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes (CCC K421)"
type: source
tags: [source, arxiv, k421]
keywords: [2610.02861, k421]
related:
  - concepts/model-is-not-a-security-boundary.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- `@concepts/model-is-not-a-security-boundary.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes |
| **arXiv** | 2610.02861 (2026-10) |
| **Retrieved** | 2026-10-05 |

## Narrative

**Verdict: ADOPT principle; cybersec-primary.**

**Containing the Autonomous Operator — agent safety as an infrastructure problem.** The thesis is one sentence and everything follows from it: **the model is not a security boundary.** Alignment, system prompts, and input classifiers lower the probability of misbehavior but guarantee nothing, and their failure modes are adversarially discoverable. So an agent that operates a Kubernetes cluster must be secured the way multi-tenant platform security is secured — **assume the workload is hostile and constrain what it can reach, do, and exfiltrate.** The paper names what breaks: agents **collapse the data/control separation** that cloud-native security rests on, because content the agent merely *reads* — a log line, a ticket field, an annotation, a third-party MCP tool description — can redirect what it *does*. Its central design rule is to **break the combination of untrusted input, sensitive access, and external egress**; each alone is survivable, the three together are not. The framework is seven layers mapped onto native Kubernetes controls: workload identity, RBAC plus `ValidatingAdmissionPolicy`, gVisor/Kata sandboxing, **FQDN-aware egress policy**, an **agent/MCP gateway applying policy-as-code over tool arguments**, and eBPF runtime enforcement. **CCC relevance:** this is the infrastructure-side statement of the same principle CCC holds at the harness level — *gate the tool step, enforcement is external and fail-closed, model self-arbitration is not a boundary* (`cemini-invariants.mdc`). Pairs K402 MCP error surfaces / K403 Tracekit / K395 approval laundering / `@concepts/schema-bound-mcp-tool-surface.md` / `@concepts/untrusted-model-delegation-governance.md`. **Routing: cybersec-primary** — brief written to `@cybersecurity-wiki/`; CCC keeps the tool-boundary-mediation principle. No repo, no measured results (the paper reports a threat–control matrix and four attack walkthroughs, explicitly no attack-success or overhead figures). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Content that an agent merely reads—a log line, a ticket, a tool description—can redirect what it does. This paper argues that the model must not be treated as a security boundary." [Source: arXiv 2610.02861 (retrieved 2026-10-05)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.02861-containing-the-autonomous-operator-a-defense-in.pdf` |
