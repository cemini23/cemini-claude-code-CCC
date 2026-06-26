---
title: MEMPROBE — hidden user-state recovery audit (arXiv 2606.24595)
type: source
tags: [source, arxiv, memory, evaluation, memprobe, k128]
keywords: [2606.24595, memprobe, recovery, hidden-user-state, dump-all, top-k]
related:
  - concepts/hidden-user-state-recovery-audit.md
  - entities/tools/memprobe.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - entities/tools/claude-mem.md
  - sources/brief-k128-memprobe-memory-recovery-2026-06-26.md
  - concepts/multi-factor-agentic-memory-value-model.md
maturity: draft
read_status: read
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- `@concepts/hidden-user-state-recovery-audit.md` — recovery vs task-success synthesis
- `@entities/tools/memprobe.md` — benchmark repo entity

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery |
| **Authors** | Ma et al. (UIC, KU Leuven, UCSD) |
| **arXiv** | 2606.24595v1 [cs.CL] |
| **Repo** | https://github.com/sora1998/MemProbe (CC-BY-4.0) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.24595-2606-24595v1-memprobe-probing-long-term-agent-me.pdf` |
| **Retrieved** | 2026-06-26 |
| **Read status** | read (benchmark design + three findings) |

## Narrative

**MEMPROBE** evaluates long-term agent memory as an **auditable post-interaction artifact**: after leak-controlled assistance tasks, reconstruct a hidden taxonomy-anchored user-state bank from the agent's memory store. Scores **recovery** (full-store `dump_all` vs system's top-k retrieve) against ground truth — not downstream task success.

**Scale:** 50 simulated users × 31 hidden dimensions = 1,550 recovery targets; tests 5 SOTA memory systems.

**Key findings [TENTATIVE — paper eval]:**

1. **Task success ≠ memory** — memoryless baseline nearly saturates task completion; recovery stays ~0.6 category-balanced and drops under top-k.
2. **Write–read split** — stored evidence ≠ retrievable user state; consolidation/write policy is the bottleneck.
3. **Episodic frontier** — stable preferences recover better than one-off relational episodes.

**CCC relevance:** steal recovery audit for claude-mem + `hot.md` eval; pairs with channel-fracture inverse verification and WorldMemArena stage rubric. **REFERENCE** benchmark; **CONDITIONAL-GO** laptop clone for methodology study (CC-BY-4.0 attribution).

## Snippets

> "Task success and recoverable memory behave as distinct capabilities."
> — [Source: arxiv-2606.24595-2606-24595v1-memprobe-probing-long-term-agent-me.pdf abstract, retrieved 2026-06-26]

> "We probe what the memory retains, reconstructing each hidden target under two access modes: a full-store dump_all probe and the system's own top-k retrieve interface."
> — [Source: arxiv-2606.24595-2606-24595v1-memprobe-probing-long-term-agent-me.pdf, retrieved 2026-06-26]
