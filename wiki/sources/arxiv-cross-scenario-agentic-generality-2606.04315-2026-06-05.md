---
title: Cross-scenario generality of agentic memory systems (arXiv 2606.04315)
type: source
tags: [source, arxiv, agent-memory, automem, k100]
keywords: [2606.04315, automem, cross-scenario, memory-systems]
related:
  - concepts/agentic-memory-cross-scenario-generality.md
  - sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md
  - "@osint-wiki/sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md"
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- `@concepts/agentic-memory-cross-scenario-generality.md` — CCC stub; OSINT owns depth
- `@osint-wiki/sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md` — OSINT mirror (when ingested)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline |
| **Authors** | Chen, Gu, Yin, Long, Zeng, Liu, Guo, Zhou, Tang (MSU / GMU / Purdue) |
| **arXiv** | 2606.04315 |
| **PDF** | `raw-sources/arxiv-2606.04315-exploring-cross-scenario-generality-of-agentic-m.pdf` |
| **Retrieved** | 2026-06-05 |
| **Read status** | read |

## Narrative

Evaluates eight memory architectures + search harness baseline across five task families. **AutoMEM** — agentic memory harness with self-managed tool interface — achieves best cross-scenario ranking. Key diagnostic: passive stores fail on agentic trajectories via representation + retrieval failures.

**K100 routing fix:** this is a **memory** paper, not tool-calling generalization (was mis-bundled with MAVEN).

## Snippets

> "AutoMEM, an agentic memory harness with a self-managed tool interface, achieving the best cross-scenario generality among the systems we evaluate."
> — [Source: arxiv-2606.04315 abstract, retrieved 2026-06-05]

> "Existing memory systems struggle on agentic trajectories through two failure modes… a representation-level failure… and a retrieval-level failure."
> — [Source: arxiv-2606.04315 abstract, retrieved 2026-06-05]
