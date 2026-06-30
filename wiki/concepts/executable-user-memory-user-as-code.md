---
title: Executable user memory — User as Code paradigm
type: concept
tags: [concept, memory, executable, user-as-code, k120]
keywords: [2606.16707, checkpoint-pipeline, active-service, aggregate-queries]
related:
  - sources/arxiv-user-as-code-executable-memory-2606.16707.md
  - entities/tools/user-as-code.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/code-as-agent-harness.md
  - concepts/selective-experience-memory-harness.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - entities/tools/claude-mem.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/subagent-orchestration.md
  - sources/brief-k120-user-as-code-dynamo-prod-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-user-as-code-executable-memory-2606.16707.md` — Pine AI paper
- `@entities/tools/user-as-code.md` — Apache-2.0 reference repo
- `@concepts/agent-memory-stack-comparison.md` — vs claude-mem / mem0
- `@concepts/llm-as-code-agentic-programming.md` — code-owned control flow peer
- `@concepts/code-as-agent-harness.md` — executable substrate layer
- `@concepts/selective-experience-memory-harness.md` — τ-gated retrieval contrast
- `@concepts/multi-factor-agentic-memory-value-model.md` — forgetting/value peer
- `@entities/tools/claude-mem.md` — adopted observation memory (different tier)
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — delivery vs representation

## Raw Concept

Should user memory be retrieved facts, or executable state + rules?

## Narrative

**User as Code** [TENTATIVE — 2606.16707]: personalized agent memory as **typed Python state** + **deterministic rules** — not a bag-of-facts store consulted via similarity search.

### vs retrieval memory

| Capability | Retrieval (vector/KG) | Executable (UaC) |
|------------|----------------------|------------------|
| Single fact recall | Strong | Competitive |
| Aggregate over history | Collapses (6–43% in paper) | One-line compute on typed state |
| Contradiction resolution | Needs manual versioning | Interpreter + checkpoint merge |
| Proactive alerts | Query-driven only | Rules fire on state change |

### Two-phase pipeline (steal-for CCC)

1. **Append-only log** — raw observations never discarded (`wiki/log.md`, claude-mem observations)
2. **Periodic checkpoint** — structured artifact (`hot.md`, wiki pages, typed frontmatter)

Novelty is **automated checkpointing** from dialogue into code-readable representation — not "Python can sum a list."

### CCC posture

| Question | Answer |
|----------|--------|
| Replace claude-mem? | **No** — different layer; claude-mem = passive index; UaC = user model for personal agents |
| Install `user-as-code` on prod? | **NO-GO** — laptop personal-agent experiments only |
| Steal | Checkpoint ritual + proactive rule hooks (allergy-style guardrails in skills) |

## Snippets

> "The initiation asymmetry central to active service: the system must generate alerts without being asked."

> — [Source: arxiv-2606.16707-user-as-code-executable-memory-for-personalized.pdf]
