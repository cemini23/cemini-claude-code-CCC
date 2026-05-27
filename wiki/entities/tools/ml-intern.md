---
title: huggingface/ml-intern — research-agent workflow reference (Apache-2.0)
type: entity
tags: [tool, reference, research-agent, huggingface, k68, cross-wiki-route]
keywords: [ml-intern, huggingface, research-agent, workflow, apache-2]
related:
  - concepts/subagent-orchestration.md
  - concepts/code-as-agent-harness.md
  - entities/patterns/autoresearch-loop.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/ai-infra-engineer-learning.md
maturity: draft
created: 2026-05-26
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — multi-step research delegation patterns
- `@concepts/code-as-agent-harness.md` — practical agent loop for ML/research tasks
- `@entities/patterns/autoresearch-loop.md` — proposal → eval → iterate kinship
- `@entities/tools/claude-code.md` — CCC harness for comparable workflows on laptop

Cross-wiki: K68 `@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md`.

## Raw Concept

`huggingface/ml-intern` — Hugging Face **research-agent workflow** examples. K68 **Reference** for CCC orchestration docs (how to structure literature/experiment agents), not prod install.

## Narrative

### What to steal (patterns only)

- Task decomposition for paper/experiment pipelines
- Checkpointing intermediate artifacts
- Human review gates before “publish” outputs

### Adoption posture

| Check | Status |
|-------|--------|
| License | Apache-2.0 [CONFIRMED K68] |
| Cemini prod | **No** — OSINT/CCC laptop reference |
| Verdict | **REFERENCE (K68)** |

## Snippets

> "Practical research-agent workflows."
> — [Source: briefs/2026-05-26_k68-ccc-tooling-from-osint.md]
