---
title: DeepSearch-World — self-distillation for deep search agents (2607.07820)
type: source
tags: [source, arxiv, search, verifiable-environment, self-distillation, k156]
keywords: [2607.07820, deepsearch-world, deepsearch-evolve, verifiable, 420k, browsecomp, gaia]
related:
  - concepts/verifiable-search-agent-environment.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/multilingual-long-horizon-agent-eval.md
  - sources/brief-k156-deepsearch-world-verifiable-search-2026-07-13.md
maturity: draft
read_status: read
created: 2026-07-13
updated: 2026-07-13
phase_0_verdict: "WATCH 2026-07-13 — paper promises env+420K pool+code release; no public GitHub at Phase-0; steal verifiable offline search env for eval"
---

## Relations

- `@concepts/verifiable-search-agent-environment.md` — synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment |
| **Authors** | Xinyu Geng et al. |
| **arXiv** | 2607.07820v1 [cs.CL] |
| **Code** | **Not released** at Phase-0 — abstract: "We will release the environment, 420K training pool, validation set, model, and code" |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.07820-2607-07820v1-deepsearch-world-self-distillation.pdf` |
| **Retrieved** | 2026-07-13 |

## Narrative

**DeepSearch-World** — deterministic, **verifiable** offline Wikipedia search environment (reproducible search + page-reading tools). **420K** multi-hop QA from entity random walks.

**Agentic behaviors supported:** progress verification, grounded reflection, failure recovery.

**DeepSearch-Evolve** — self-distillation loop: trajectory generation → filtering → data mixing → fine-tuning (no stronger teacher model).

**DeepSearch-World-9B results:** BrowseComp 31.2%, GAIA 61.5%, HotpotQA 93.4%.

| Verdict | **WATCH/REFERENCE** — re-Phase-0 when repo drops; adopt verifiable env pattern for harness eval now |

## Snippets

> "DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools."
> — [Source: arxiv-2607.07820 abstract, retrieved 2026-07-13]
