---
title: "BioSecBench-Surveillance — verifiable agent benchmark (biosec route)"
type: source
tags: [source, arxiv, benchmark, verifiable-eval, biosecurity, harness, k203]
keywords: [2607.19262, BioSecBench, LatchBio, deterministic grading, model-harness pairs]
related:
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k202-k205-agents-langgraph-biosec-2026-07-22.md
  - "@cybersecurity-wiki/concepts/biosecbench-surveillance-verifiable-agent-eval.md"
  - "@cybersecurity-wiki/sources/arxiv-biosecbench-surveillance-2607.19262.md"
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- `@concepts/verifiable-deterministic-agent-benchmarking.md` — CCC harness steal
- Cybersec deepen: `@cybersecurity-wiki/concepts/biosecbench-surveillance-verifiable-agent-eval.md`
- `@cybersecurity-wiki/sources/arxiv-biosecbench-surveillance-2607.19262.md`
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — eval rigor peer
- Prefer brief over CCC biosec deepen

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance |
| **Author** | Harmon Bhasin, Kevin Flyangolts, et al. (LatchBio / Aclid) |
| **arXiv** | 2607.19262 |
| **Pages** | 8 |
| **Retrieved** | 2026-07-22 |
| **Code** | `latchbio/biosecbench-surveillance` — LICENSE file **Apache-2.0** (API NOASSERTION); tiny REFERENCE clone |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.19262-biosecbench-surveillance-a-verifiable-benchmark.pdf` |

## Narrative

100 evaluations; agent gets only data+context a human analyst would; structured answers graded **deterministically**. 3,962 attempts across 16 model–harness pairs; best ~**50.2%** (Opus 4.8/PI, GPT-5.5/Codex). Failures often in surrounding choices (refs, thresholds, filters) even when workflow correct.

**CCC:** steal verifiable-eval methodology + report harness×model. **Cybersec** owns pathogen-surveillance domain.

## Snippets

> "Each evaluation gives an agent only the data and context a human analyst would have, then grades its structured answer deterministically."
> — Abstract
