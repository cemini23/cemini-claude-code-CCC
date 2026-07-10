---
title: Multilingual long-horizon agent evaluation
type: concept
tags: [concept, benchmark, multilingual, long-horizon, evaluation, harness, k152]
keywords: [polyworkbench, multilingual compounding, hybrid eval, structural executable semantic, 2607.06008]
related:
  - sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/orchestration-option-quantitative-metrics.md
  - concepts/recoverable-tool-reliability-hazards.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k152-polyworkbench-multilingual-agent-eval-2026-07-10.md
  - briefs/2026-07-10_ccc-handoff-cage-polyworkbench-ingest.md
  - "@cybersecurity-wiki/concepts/multilingual-long-horizon-agent-evaluation.md"
  - "@cybersecurity-wiki/sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md"
maturity: draft
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- `@sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md` — K152 PolyWorkBench
- `@concepts/client-as-first-order-harness-factor.md` — client harness affects long-horizon scores

## Raw Concept

K152 arXiv **2607.06008** — PolyWorkBench introduces multilingual long-horizon eval discipline. Question: do agents survive **language switches** across **many steps**?

## Narrative

### Multilingual compounding degradation

Monolingual success does not predict multilingual long-horizon success. Each language boundary and each step can amplify prior errors — analogous to **recoverable tool reliability** compounding (K129) but on **locale/context** axis.

### Hybrid eval rubric (steal for CCC eval design)

| Layer | What it checks | CCC analogue |
|-------|----------------|--------------|
| **Structural** | Files, state, artifacts exist | `wiki_lint.py`, pytest, git diff |
| **Executable** | Code runs, tests pass | CI, Phase-0 smoke scripts |
| **LLM semantic** | Rubric on intent/quality | super-audit, gatekeeper layers |

### Client sensitivity

PolyWorkBench reports different scores across **Claude Code**, **OpenClaw**, etc. — reinforces that benchmark numbers are **harness-specific**, not model-only.

### Cemini applicability

- **CCC:** adopt hybrid rubric when scoring agent options; note multilingual gap in English-primary workflows
- **David/TipDrop:** adopt only if multilingual Discord/content pipelines become primary — otherwise REFERENCE

| Verdict | **REFERENCE** — eval methodology steal; no benchmark install at Phase-0 |

## Snippets

> "Long-horizon multilingual evaluation requires hybrid scoring — structural, executable, and semantic — because any single metric misses compounding failure modes."
> — [Source: arxiv-2607.06008 synthesis, retrieved 2026-07-10]
