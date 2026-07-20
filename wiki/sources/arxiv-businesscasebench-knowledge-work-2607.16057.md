---
title: "BusinessCaseBench — frontier AI on business-case knowledge work"
type: source
tags: [source, arxiv, benchmark, knowledge-work, llm-as-judge, rubric, k193]
keywords: [2607.16057, BusinessCaseBench, Wharton, HBS, case method, Standard scoring, Complete Answer]
related:
  - concepts/businesscasebench-rubric-from-expert-solutions.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@concepts/businesscasebench-rubric-from-expert-solutions.md` — synthesized steal
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — eval-rigor peer (K169)
- `@concepts/multi-agent-evidence-artifact-layers.md` — evidence → synthesis → interface
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — LLM-judge sits below execution on verification hierarchy

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Frontier AI performance across the business disciplines: a case-grounded benchmark of knowledge work and analytical reasoning |
| **Author** | Ajay Patel, Kartik Hosanagar, Ramayya Krishnan, Chris Callison-Burch, Karim Lakhani, Mitch Weiss (Wharton / CMU / UPenn / HBS) |
| **arXiv** | 2607.16057 |
| **Pages** | 33 |
| **Retrieved** | 2026-07-20 |
| **Code** | none public at Phase-0 — **NO-GO** install |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.16057-frontier-ai-performance-across-the-business-disc.pdf` |

## Narrative

### Thesis

Coding/math/tool-use benchmarks miss white-collar analytical work: synthesis under uncertainty, trade-offs, multi-stakeholder judgment. Business-school case method + instructor solutions → rubric checklists → LLM-as-judge with human validation.

### Headline scores [TENTATIVE — paper figures]

Frontier models already high on Standard (partial-credit) scoring across 18 disciplines; e.g. Claude Sonnet 4.6 ~**88.4%**, GPT-5.4 ~**87.2%**, Gemini 3 Flash Preview ~**81.6%**. ~**23 pp** gain within one model family over two years.

### CCC / federation steal

When grading subjective agent outputs (briefs, poker strategy writeups, TipDrop operator notes): build **equally-weighted checklist rubrics from an expert reference**, score Standard vs Complete Answer separately, and treat LLM-judge as advisory (K162). Cross-wiki: OSINT may deepen for finance/case pedagogy — CCC keeps harness/eval-method slice only.

## Snippets

> "We construct BusinessCaseBench, a benchmark spanning hundreds of questions drawn from business cases across eighteen disciplines, each paired with a grading rubric derived from the expert-written instructor case solution."
> — Abstract

> "A longitudinal comparison within one model family documents roughly a 23-percentage-point gain over two years."
> — Significance statement
