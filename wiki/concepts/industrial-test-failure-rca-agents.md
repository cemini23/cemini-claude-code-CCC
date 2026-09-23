---
title: "Supporting Industrial Test-Failure Analysis with LLM-Based Systems: An Experience Report (CCC K374)"
type: concept
tags: [concept, k374]
keywords: [2609.21843, k374]
related:
  - sources/arxiv-industrial-test-failure-rca-llm-agents-2609.21843.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-21_ccc-k373-k375-sip-ready.md
  - concepts/evidence-grounded-structured-rca.md
  - sources/arxiv-argus-mcp-k8s-rca-2608.23084.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-21
updated: 2026-09-23
---

## Relations

- `@sources/arxiv-industrial-test-failure-rca-llm-agents-2609.21843.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-21_ccc-k373-k375-sip-ready.md`

## Raw Concept

K374: ADOPT pattern — arXiv 2609.21843.

## Narrative

Industrial nightly regression failures require **multi-source RCA** across controller and device logs. Westermo case study: tool-augmented LLM workflows in **single-agent** vs **orchestrated multi-agent** configurations on two real failure scenarios; six practitioners + 120 repeated runs. Neither configuration showed consistent practitioner-perceived quality advantage — **single-agent was faster and cheaper**, making it the practical baseline; multi-agent benefits need harder scenarios. Eval axes: perceived correctness, reasoning quality, fix realism, clarity, usefulness, trust, cost, duration, consistency. Pairs K341 evidence-grounded RCA / K306 ARGUS diagnose-not-auto-remediate. Industrial domain OOD for CCC runtime; pattern **`policy_wired`**. No clone.

## Snippets

> "See source page for arXiv 2609.21843 locators." [Source: CCC K374 synthesis]
