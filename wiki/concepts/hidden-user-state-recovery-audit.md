---
title: Hidden user-state recovery audit (MemProbe pattern)
type: concept
tags: [concept, memory, evaluation, recovery, memprobe, k128]
keywords: [2606.24595, memprobe, dump-all, top-k, task-success, user-state-bank]
related:
  - sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md
  - entities/tools/memprobe.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - entities/tools/claude-mem.md
  - entities/patterns/cpr-context-compression.md
  - sources/brief-k128-memprobe-memory-recovery-2026-06-26.md
maturity: draft
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- `@sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md` — MemProbe paper
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — stored ≠ delivered; dump_all vs top-k analogue
- `@concepts/worldmemarena-multimodal-agent-memory-eval.md` — complementary stage-based eval

## Raw Concept

Question: how do you audit agent memory quality when task success alone cannot distinguish good memory from none?

## Narrative

**Hidden user-state recovery audit** [TENTATIVE — MemProbe 2606.24595]: after ordinary assistance, reconstruct structured user state (preferences, skills, episodic events, self-model) from the memory artifact and score against hidden ground truth — **not** downstream answer correctness.

**Steal-from for Cemini harness:**

| MemProbe axis | CCC analogue |
|---------------|--------------|
| Hidden user-state bank | Taxonomy for what `hot.md` + claude-mem should retain (prefs, open decisions, session checkpoints) |
| Leak-controlled tasks | Ingest/discuss-before-write — evidence emerges without naming targets |
| `dump_all` probe | Full claude-mem export / wiki read-back — was fact ever written? |
| Top-k retrieve | conductor/stash recall under token budget — is fact still reachable? |
| Recovery score | Post-session audit: reconstruct operator state from artifacts vs what user believes was saved |
| Task success trap | Do not equate "session completed" with "memory formed" |

**Findings to encode in eval rubrics:**

1. Behavioral benchmarks (LongMemEval, personalization QA) **insufficient** alone.
2. **Consolidation write policy** matters more than raw capacity — fleeting chat ≠ durable claims.
3. **Episodic relational memory** remains hard — prefer explicit event+consequence entries in `wiki/log.md` over implicit chat recall.

**Verdict:** MemProbe repo **REFERENCE** + **CONDITIONAL-GO** laptop eval (CC-BY-4.0). No prod memory stack replacement.

## Snippets

> "Assessing memory thus calls for a different yardstick… how much of a user's hidden state can be reconstructed."
> — [Source: arxiv-2606.24595-2606-24595v1-memprobe-probing-long-term-agent-me.pdf, retrieved 2026-06-26]
