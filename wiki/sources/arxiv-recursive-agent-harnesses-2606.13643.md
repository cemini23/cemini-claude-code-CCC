---
title: Recursive Agent Harnesses — harness recursion for long context (arXiv 2606.13643)
type: source
tags: [source, arxiv, recursive-agent-harness, oolong, k115]
keywords: [2606.13643, rah, harness-recursion, code-as-action, dynamic-workflows]
related:
  - concepts/recursive-agent-harness-harness-recursion.md
  - concepts/subagent-orchestration.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/code-as-agent-harness.md
  - entities/patterns/scatter-gather.md
  - concepts/claude-harness-dynamic-workflows-k88.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- `@concepts/recursive-agent-harness-harness-recursion.md` — CCC synthesis
- `@concepts/subagent-orchestration.md` — Task tool subagent spawning
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — code-first orchestration
- `@concepts/code-as-agent-harness.md` — harness vs model recursion axis
- `@entities/patterns/scatter-gather.md` — parallel subagent fan-out

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Recursive Agent Harnesses |
| **Authors** | Lumer, Sen, Paul, Subbiah (PwC U.S.) |
| **arXiv** | 2606.13643v1 [cs.CL] |
| **Location** | `raw-sources/arxiv-2606.13643-recursive-agent-harnesses.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (RAH definition, Oolong-Synthetic eval) |

## Narrative

Names **Recursive Agent Harness (RAH)** — **harness recursion**: recursive unit is a **full agent harness** (filesystem, tools, planning) not a bare model call (RLM model recursion). Parent writes executable script spawning **Task()-style subagent harnesses** in parallel per long-context entry; JSON tool calls for 1–5 entries.

**Oolong-Synthetic** (199 samples, 13 context buckets 1K–4M tokens), backbone **GPT-5** held fixed:

| System | Accuracy |
|--------|----------|
| Codex coding agent baseline | 71.75% |
| **RAH** (same backbone) | **81.36%** |
| RLM (model recursion, no tools) | 64.38% (cited) |
| RAH + Claude Sonnet 4.5 | 89.77% |

Relates to Anthropic **dynamic workflows** (code orchestrates subagents at scale). Mechanism = established primitives (CodeAct, Minions); contribution is naming + controlled harness-only ablation.

**Unverified repo:** `darkness22s/recursive-agent-harness` on GitHub — npm package passes tests but **no SPDX license**, 0★, product scope (autonomous successor runtime) **does not match** PwC paper eval — **not** paper implementation [NEEDS VERIFICATION 2026-06-15].

**CCC relevance:** Claude Code Task tool + scatter-gather already implements RAH pattern; steal explicit **harness recursion** vocabulary for long-context wiki/conductor jobs.

## Snippets

> "We frame it as harness recursion, the code-first extension to the model recursion of RLMs."

> "RAH improves the Codex result from 71.75% to 81.36% with GPT-5 held fixed — attributing the gain to the harness rather than the model."
