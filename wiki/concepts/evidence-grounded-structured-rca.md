---
title: "Evidence-grounded structured RCA — diagnose with evidence, gate fixes (CCC K341)"
type: concept
tags: [concept, rca, diagnostics, evidence-tree, telecom, policy, k341]
keywords: [2609.02805, telecom RCA, structured reasoning, evidence-grounded, human-gated remediation, ARGUS]
related:
  - sources/arxiv-llms-telecom-rca-structured-reasoning-2609.02805.md
  - sources/arxiv-argus-mcp-k8s-rca-2608.23084.md
  - entities/tools/argus-agentic-runtime.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-llms-telecom-rca-structured-reasoning-2609.02805.md`
- `@sources/arxiv-argus-mcp-k8s-rca-2608.23084.md`
- `@entities/tools/argus-agentic-runtime.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

K341: telecom RCA with LLMs requires **structured, evidence-grounded reasoning** — not vanilla free-form diagnosis. Pairs K306 ARGUS asymmetry.

## Narrative

**Evidence tree, not scalar.** Root-cause work spans cross-layer 5G/6G dependencies; vanilla LLM answers hallucinate without structured retrieval, orchestration, and verifiable checks against network evidence.

**Diagnostic/prescriptive split (K306).** Agents may **draft** diagnoses with cited evidence; **remediations stay human-gated** — never auto-apply fixes from agent RCA output. Runtime **`wont_wire`**. `policy_wired`.

## Snippets

> "Diagnose with evidence; remediate with human gate — same pattern as K306 ARGUS." [Source: CCC K341 synthesis]
