---
title: "Diagnostic/prescriptive asymmetry in MCP-grounded RCA"
type: concept
tags: [concept, mcp, rca, sre, trust, remediation, k306]
keywords: [argus, root cause analysis, prometheus, loki, slack, auto-remediation ban, 2608.23084]
related:
  - sources/arxiv-argus-mcp-k8s-rca-2608.23084.md
  - entities/tools/argus-agentic-runtime.md
  - concepts/verification-gated-persist-pivot-runtime.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-argus-mcp-k8s-rca-2608.23084.md`
- `@entities/tools/argus-agentic-runtime.md` (dual-ID: CCC K253 Argus persist/pivot — different product)
- `@concepts/verification-gated-persist-pivot-runtime.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: when an agent is good at saying what broke, can it be trusted to say what to do? Source: arXiv 2608.23084 (CCC K306).

## Narrative

ARGUS (K8s RCA over standard MCP servers: cluster state, Prometheus, Loki, NATS; output into Slack) named the correct root cause in **10/10** injected faults with MCP success ratio **0.91** — yet the six interviewed on-call engineers consistently distrusted its recommended fixes. The asymmetry held across fault injection, rubric scoring, and interviews:

- **Diagnosis** = evidence correlation over observed state → MCP-grounded agents excel.
- **Prescription** = change under uncertainty with blast radius → humans rightly demand control.

Policy consequence: wire agents as **diagnostic engines**, keep remediation human-gated. This generalizes ARGUS's finding to every "agent suggests fix" surface (prod alerts, lint autofixes, harness self-repair): present diagnosis + evidence + proposed action separately, and never let the same loop that diagnosed also execute the fix unattended (pairs K253 verification-gated persist/pivot).

Dual-ID: CCC K306 ≠ CCC K253 (`lbx154/Argus` runtime). Cybersec K306 (LLM-compliance) unaffected.

## Snippets

> "Our central finding is a diagnostic/prescriptive asymmetry: ARGUS reliably identifies what went wrong, but is perceived as less reliable or trustworthy at specifying what to do next." [Source: arXiv 2608.23084 abstract]
