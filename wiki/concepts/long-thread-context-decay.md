---
title: Long-thread context decay — agent quality degradation (K103)
type: concept
tags: [concept, context-engineering, k103]
keywords: [hooeem, context-decay, long-conversation, compaction]
related:
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/subagent-orchestration.md
  - concepts/full-stack-ai-engineer-agent-path.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/claude-mem.md
  - sources/trading-posts-compilation-19-2026-06-07.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-19-2026-06-07.md"
---

## Relations

- `@concepts/context-engineering.md` — parent discipline
- `@concepts/token-economics-and-prompt-caching.md` — cache burn on long threads
- `@concepts/subagent-orchestration.md` — fork fresh subagent vs decaying parent
- `@concepts/full-stack-ai-engineer-agent-path.md` — prior @hooeem posts (K72)
- `@entities/patterns/cpr-context-compression.md` — compression pattern
- `@entities/tools/claude-mem.md` — offload to durable memory vs window bloat
- `@sources/trading-posts-compilation-19-2026-06-07.md` — K103 Post 12 (@hooeem)

## Raw Concept

K103 Post 12 (@hooeem): **long conversations degrade agent quality** — model attention dilutes, tool-call discipline slips, and earlier constraints are "forgotten" despite technically remaining in context.

## Narrative

### Mitigations [TENTATIVE post + CONFIRMED Cemini practice]

| Symptom | Mitigation |
|---------|------------|
| Instruction drift | Rewrite `hot.md` + restate acceptance criteria mid-task |
| Tool spam | `@concepts/agent-backpressure-loop.md` |
| Stale project state | SessionStart read `CLAUDE.md`; file answers to wiki |
| Unbounded history | New chat; Task subagent with clean context; CPR compression |
| Lost cross-session work | `@entities/tools/claude-mem.md` + `wiki/log.md` |

**Verdict:** **REFERENCE** — reinforces existing context-engineering stack; pair with `@concepts/agent-backpressure-loop.md` for output-side throttling.

## Snippets

> Long conversations degrade agent quality — context decay mitigations. [TENTATIVE — @hooeem, Posts.docx K103 Post 12]
