---
title: User as Code — executable memory for personalized agents (arXiv 2606.16707)
type: source
tags: [source, arxiv, memory, user-as-code, k120]
keywords: [2606.16707, executable-memory, pine-ai, locomo]
related:
  - concepts/executable-user-memory-user-as-code.md
  - entities/tools/user-as-code.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/subagent-orchestration.md
  - entities/tools/claude-mem.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- `@concepts/executable-user-memory-user-as-code.md` — CCC synthesis
- `@entities/tools/user-as-code.md` — 19PINE-AI reference implementation
- `@concepts/agent-memory-stack-comparison.md` — memory stack positioning

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | User as Code: Executable Memory for Personalized Agents |
| **Authors** | Bojie Li (Pine AI) |
| **arXiv** | 2606.16707v1 [cs.AI] |
| **Repo** | `github.com/19PINE-AI/user-as-code` (Apache-2.0) |
| **Location** | `raw-sources/arxiv-2606.16707-user-as-code-executable-memory-for-personalized.pdf` |
| **Retrieved** | 2026-06-20 |
| **Read status** | read (UaC paradigm, two-phase pipeline, benchmarks) |

## Narrative

**Problem:** Retrieval-based user memory (vectors, KG, flat facts) separates **representation** from **verification** — poor at contradictions, aggregates, and proactive rules.

**User as Code (UaC):** user model = living Python project — typed objects hold state; functions encode rules the interpreter runs. Memory **representation and reasoning share one executable medium**.

**Two-phase pipeline:** append-only conversation log (never discard) → periodic checkpoint into structured typed Python code (database-style WAL + checkpoint applied to LLM memory).

**Task tiers:** (1) basic recall, (2) multi-session retrieval, (3) **active service** — unsolicited alerts on state change (e.g. drug–allergy conflict).

**Results [TENTATIVE — paper claims]:** LOCOMO factual recall 78.8% (competitive with strong baselines); aggregate queries ~99% vs retrieval 6–43%; proactive alerts unique to executable rules.

**CCC relevance:** steal checkpoint pipeline for `hot.md` + wiki state; **CONDITIONAL-GO** on Pine repo for personal-agent experiments — not prod Cemini stack (claude-mem owner).

## Snippets

> "Representing the user and reasoning about the user happen in one medium an interpreter can run."

> "Append-only log that never discards a fact, periodically checkpointed into structured, typed code."
