---
title: PolyWorkBench — Benchmarking Multilingual Long-Horizon LLM Agents (2607.06008)
type: source
tags: [source, arxiv, benchmark, multilingual, long-horizon, evaluation, k152]
keywords: [2607.06008, polyworkbench, tencent, bjtu, multilingual agent, long horizon, claudecode, openclaw]
related:
  - concepts/multilingual-long-horizon-agent-eval.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/orchestration-option-quantitative-metrics.md
  - concepts/recoverable-tool-reliability-hazards.md
  - sources/brief-k152-polyworkbench-multilingual-agent-eval-2026-07-10.md
  - concepts/gatekeeper-layered-agent-evaluation.md
maturity: draft
read_status: read
created: 2026-07-10
updated: 2026-07-10
phase_0_verdict: "REFERENCE 2026-07-10 — benchmark paper; tests claudecode/openclaw among clients; no public GitHub at Phase-0; steal multilingual compounding + hybrid eval rubric only"
---

## Relations

- `@concepts/multilingual-long-horizon-agent-eval.md` — synthesis
- `@concepts/client-as-first-order-harness-factor.md` — client choice affects long-horizon scores

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents |
| **Authors** | Tencent / Beijing Jiaotong University (arXiv 2607.06008v1, Jul 2026) |
| **Code** | **Not found** at Phase-0 — paper claims benchmark release; no public repo located |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.06008-2607-06008v1-polyworkbench-benchmarking-multilin.pdf` |
| **Retrieved** | 2026-07-10 |
| **Read status** | read (67 tasks, 5 domains, hybrid eval, multilingual degradation) |

## Narrative

PolyWorkBench evaluates **multilingual long-horizon** agents across **67 tasks** in **5 domains** (coding, office, research, creative, life). Hybrid scoring: **structural** (file/state checks) + **executable** (run tests) + **LLM semantic** (rubric).

Key finding: **multilingual compounding degradation** — agents that succeed monolingually often fail when language switches mid-trajectory; error compounds over long horizons.

Evaluated clients include **Claude Code**, **OpenClaw**, and other agent harnesses — supports K140 thesis that **client is first-order** for long-horizon eval.

| Verdict | **REFERENCE** — no install; cite when designing multilingual or long-horizon eval; weak David adoption unless TipDrop multilingual workflows expand |

## Snippets

> "Multilingual long-horizon agents face compounding degradation: each language switch and each step amplifies prior errors."
> — [Source: arxiv-2607.06008 paraphrase from §1, retrieved 2026-07-10]

> Hybrid evaluation combines structural verification, executable checks, and LLM-based semantic assessment.
> — [Source: arxiv-2607.06008 methodology, retrieved 2026-07-10]
