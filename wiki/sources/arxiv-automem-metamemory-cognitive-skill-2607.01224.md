---
title: AutoMem — automated metamemory as cognitive skill (arXiv 2607.01224)
type: source
tags: [source, arxiv, memory, metamemory, automem, k137]
keywords: [2607.01224, automem, metamemory, scaffold, memory-proficiency, balrog]
related:
  - concepts/metamemory-scaffold-proficiency-training.md
  - entities/tools/automem-stanford-cognitive-skill.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/agentic-memory-cross-scenario-generality.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/long-thread-context-decay.md
  - sources/brief-k137-automem-metamemory-cognitive-skill-2026-07-02.md
  - entities/tools/claude-mem.md
maturity: draft
read_status: read
created: 2026-07-02
updated: 2026-07-02
---

## Relations

- `@concepts/metamemory-scaffold-proficiency-training.md` — synthesis
- `@entities/tools/automem-stanford-cognitive-skill.md` — reference repo (not verygoodplugins/automem)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AutoMem: Automated Learning of Memory as a Cognitive Skill |
| **Authors** | Wu et al. (Stanford) |
| **arXiv** | 2607.01224v1 [cs.AI] |
| **Project** | https://autolearnmem.github.io/ |
| **Code** | https://github.com/autoLearnMem/AutoMem |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.01224-automem-automated-learning-of-memory-as-a-cognit.pdf` |
| **Retrieved** | 2026-07-02 |
| **Read status** | read (framework, results, scaffold evolution) |

## Narrative

**AutoMem** (Stanford, 2607.01224) treats **memory management as a trainable cognitive skill** (metamemory): file-system operations (READ, WRITE, SEARCH, APPEND, UPSERT_MAP) are **first-class actions** alongside task actions in a unified action space.

Two automated outer loops optimize a shared inner-loop agent:

| Loop | Optimizes | Mechanism |
|------|-----------|-----------|
| **#1 Structure** | Prompts, file schema, validation, action vocabulary | Meta-LLM (Claude Opus 4.6) reviews full trajectories → revises scaffold |
| **#2 Proficiency** | Memory specialist LoRA weights | Meta-LLM (Opus 4.7) curates SFT from agent traces; gameplay model frozen |

Evaluated on BALROG games (Crafter, MiniHack, NetHack). Qwen2.5-32B + memory optimization alone → **~2×–4×** progression gains without training task-action weights; competitive with Claude Opus 4.5 / Gemini 3.1 Pro Thinking.

**Name collision:** distinct from arXiv **2606.04315** AutoMEM (cross-scenario eval) and from **verygoodplugins/automem** (MIT graph-vector MCP memory service).

**CCC relevance:** steal scaffold/proficiency split, meta-LLM trajectory review for `hot.md`/claude-mem schema, engine logging over agent self-log, search-before-write discipline. **REFERENCE** — no LICENSE on repo at Phase-0.

## Snippets

> "Memory expertise is a learned skill: knowing what to encode, when to retrieve, and how to organize knowledge—a capacity known in cognitive science as metamemory."
> — [Source: arxiv-2607.01224-automem-automated-learning-of-memory-as-a-cognit.pdf abstract, retrieved 2026-07-02]

> "Optimizing memory alone—without modifying the model's task-action behavior—improved the base agent's performance ∼2×–4×."
> — [Source: arxiv-2607.01224-automem-automated-learning-of-memory-as-a-cognit.pdf abstract, retrieved 2026-07-02]
