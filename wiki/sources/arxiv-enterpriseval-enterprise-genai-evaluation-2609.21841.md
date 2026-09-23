---
title: "EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise (CCC K373)"
type: source
tags: [source, arxiv, k373]
keywords: [2609.21841, k373]
related:
  - concepts/enterprise-use-case-genai-evaluation.md
  - briefs/2026-09-21_ccc-k373-k375-sip-ready.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/evaluation-first-rubric-induction.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-23
---

## Relations

- `@concepts/enterprise-use-case-genai-evaluation.md`
- `@briefs/2026-09-21_ccc-k373-k375-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise |
| **arXiv** | 2609.21841 (2026-09) |
| **Retrieved** | 2026-09-21 |

## Narrative

**Verdict: ADOPT eval-first.**

Public benchmarks answer “what can the model do?” — enterprise deployment needs “is this workflow fit, reliable, safe and worth scaling on our data under our controls?”. **EnterpriseVal** freezes the **socio-technical configuration** (model, prompts, retrieval, tools, guardrails, human oversight) and scores a metric catalogue spanning fidelity, utility, efficiency, reliability, assurance, and oversight. A two-tier **REJECT / CONDITIONAL / SCALE** gate maps metric vectors with confidence bounds to deployment decisions; reviewer catch rate is a measured parameter. Pilot: credit-memo drafting 88% citation precision / 1.6% hallucination vs gates 70% / 5%; procedure transformation analyst effort 27.4→2.9 h/doc. Pairs K331 rubric-before-run / K289 evidence-tree eval / K277 measurement integrity / K151 CAGE-1 governance. No public product repo → no clone. Runtime **`wont_wire`**.

## Snippets

> "EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise — CCC K373 synthesis." [Source: arXiv 2609.21841 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.21841-enterpriseval-quantifying-the-efficacy-reliabili.pdf` |
