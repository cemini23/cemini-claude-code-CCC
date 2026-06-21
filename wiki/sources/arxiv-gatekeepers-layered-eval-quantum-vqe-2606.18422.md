---
title: Gatekeepers and hallucinations — layered VQE eval framework (arXiv 2606.18422)
type: source
tags: [source, arxiv, gatekeeper, layered-eval, k121]
keywords: [2606.18422, design-entropy, harness-failure, quantum-vqe]
related:
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/agent-completion-verification-gates.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-rubrics-self-correction.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- `@concepts/gatekeeper-layered-agent-evaluation.md` — harness generalization
- `@concepts/agent-completion-verification-gates.md` — gatekeeper screening peer
- `@concepts/failed-trajectory-harness-repair.md` — harness-as-failure-source

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Gatekeepers and Hallucinations: A Layered Evaluation Framework for LLM-Driven Quantum Circuit Generation |
| **Authors** | Coleman, Marfatia (UBC Quantum Matter Institute) |
| **arXiv** | 2606.18422 |
| **Location** | `raw-sources/arxiv-2606.18422-gatekeepers-and-hallucinations-a-layered-evaluat.pdf` |
| **Retrieved** | 2026-06-21 |
| **Read status** | skimmed (framework + failure taxonomy) |

## Narrative

**Layered eval for materials-informed VQE pipelines:**

1. **Gatekeeper rubric** — seven physical/framework screening criteria
2. **Circuit fidelity** — compare to analytical/reference implementations
3. **Design entropy** — run-to-run behavioral consistency

**Five LLM failure modes:** geometry hallucination, nonexistent API usage, runtime integration failures, constraint violations, plausible-but-unverifiable output.

**Harness lesson:** forensic audit found **evaluation platform** introduced failures via silent fallback-template substitution — eval infra inside same trust boundary as models.

**CCC relevance:** steal gatekeeper + design-entropy layers for harness eval — **REFERENCE** only (quantum domain niche).

## Snippets

> "Evaluation infrastructure belongs inside the same trust boundary as the models it tests."
