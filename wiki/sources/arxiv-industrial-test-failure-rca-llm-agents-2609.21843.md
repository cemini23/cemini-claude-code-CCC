---
title: "Supporting Industrial Test-Failure Analysis with LLM-Based Systems: An Experience Report (CCC K374)"
type: source
tags: [source, arxiv, k374]
keywords: [2609.21843, k374]
related:
  - concepts/industrial-test-failure-rca-agents.md
  - briefs/2026-09-21_ccc-k373-k375-sip-ready.md
  - concepts/evidence-grounded-structured-rca.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-21
---

## Relations

- `@concepts/industrial-test-failure-rca-agents.md`
- `@briefs/2026-09-21_ccc-k373-k375-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Supporting Industrial Test-Failure Analysis with LLM-Based Systems: An Experience Report |
| **arXiv** | 2609.21843 (2026-09) |
| **Retrieved** | 2026-09-21 |

## Narrative

**Verdict: ADOPT pattern.**

Industrial nightly regression failures require **multi-source RCA** across controller and device logs. Westermo case study: tool-augmented LLM workflows in **single-agent** vs **orchestrated multi-agent** configurations on two real failure scenarios; six practitioners + 120 repeated runs. Neither configuration showed consistent practitioner-perceived quality advantage — **single-agent was faster and cheaper**, making it the practical baseline; multi-agent benefits need harder scenarios. Eval axes: perceived correctness, reasoning quality, fix realism, clarity, usefulness, trust, cost, duration, consistency. Pairs K341 evidence-grounded RCA / K306 ARGUS diagnose-not-auto-remediate. Industrial domain OOD for CCC runtime; pattern **`policy_wired`**. No clone.

## Snippets

> "Supporting Industrial Test-Failure Analysis with LLM-Based Systems: An Experience Report — CCC K374 synthesis." [Source: arXiv 2609.21843 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.21843-supporting-industrial-test-failure-analysis-with.pdf` |
