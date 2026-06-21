---
title: LightMem2 — long-term memory with TokenPilot integration
type: entity
tags: [tool, memory, lightmem, tokenpilot, k121]
keywords: [zjunlp, lightmem2, mit, context-management]
related:
  - sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md
  - concepts/prompt-cache-aligned-context-management.md
  - concepts/skill-vetting.md
  - entities/tools/claude-mem.md
maturity: draft
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- `@sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md` — TokenPilot paper (integrated here)
- `@concepts/prompt-cache-aligned-context-management.md` — cache-aligned compaction pattern
- `@concepts/skill-vetting.md` — Phase-0 before install
- `@entities/tools/claude-mem.md` — adopted CCC memory (orthogonal layer)

## Raw Concept

`github.com/zjunlp/LightMem2` — long-term agent memory framework with integrated **TokenPilot** cache-efficient context management.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `zjunlp/LightMem2` |
| **License** | MIT (API verified 2026-06-21) |
| **Stars** | ~23 (2026-06-21) |
| **Upstream** | Zhejiang University NLP group |

### Phase-0 verdict

| Question | Answer |
|----------|--------|
| Replace claude-mem? | **NO-GO** — parallel memory owner collision |
| CONDITIONAL-GO | Laptop eval of TokenPilot compaction vs manual context discipline |
| Steal-from | Ingestion-aware compaction + lifecycle eviction without busting cache prefix |

## Snippets

> "TokenPilot has been integrated into LightMem2."

> — [Source: arxiv-2606.17016-tokenpilot-cache-efficient-context-management-fo.pdf]
