---
title: MemProbe
type: entity
tags: [entity, tool, memory, benchmark, evaluation, k128]
keywords: [2606.24595, memprobe, sora1998, recovery-benchmark]
related:
  - sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md
  - concepts/hidden-user-state-recovery-audit.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - entities/tools/claude-mem.md
  - sources/brief-k128-memprobe-memory-recovery-2026-06-26.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/multi-factor-agentic-memory-value-model.md
maturity: draft
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- `@sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md`
- `@concepts/hidden-user-state-recovery-audit.md`

## Raw Concept

MemProbe — open benchmark + pipeline for probing long-term agent memory via hidden user-state recovery (github.com/sora1998/MemProbe). K128 ingest (2606.24595).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/sora1998/MemProbe |
| **License** | CC-BY-4.0 [CONFIRMED gh api 2026-06-26] |
| **Verdict** | **REFERENCE** eval rubric; **CONDITIONAL-GO** laptop benchmark run with attribution |
| **Overlap** | WorldMemArena (stage eval), LongMemEval (behavioral recall), claude-mem (operator memory) |

**Phase-0:** `scripts/adopt_k128_phase0.sh` — clone + CC-BY-4.0 verify.

**NO-GO:** replace claude-mem/conductor on prod; treat CC-BY benchmark data as attribution-required in IP-sale bundle.

## Snippets

> "Code and data are available at https://github.com/sora1998/MemProbe."
> — [Source: arxiv-2606.24595-2606-24595v1-memprobe-probing-long-term-agent-me.pdf, retrieved 2026-06-26]
