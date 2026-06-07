---
title: Agent backpressure loop — throttle agent output (K103)
type: concept
tags: [concept, harness, subagents, k103]
keywords: [bibryam, backpressure, flow-control, coding-agents]
related:
  - concepts/subagent-orchestration.md
  - concepts/context-engineering.md
  - concepts/claude-code-large-codebase-workflow.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-19-2026-06-07.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-19-2026-06-07.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — parent orchestration discipline
- `@concepts/context-engineering.md` — backpressure limits context flood
- `@concepts/claude-code-large-codebase-workflow.md` — prior @bibryam large-codebase post (K69)
- `@entities/tools/claude-code.md` — Stop hook + permission gates as harness backpressure
- `@sources/trading-posts-compilation-19-2026-06-07.md` — K103 Post 6 (@bibryam)

## Raw Concept

K103 Post 6 (@bibryam): **backpressure loop** for coding agents — explicit flow control so fast model/tool output does not overrun human review, context budget, or downstream verification.

## Narrative

### Pattern sketch [TENTATIVE — single X post, not Cemini-tested]

| Stage | Backpressure mechanism |
|-------|------------------------|
| Tool burst | Cap parallel subagents; queue Task tool invocations |
| Edit flood | Scoped diffs; OpenSpec acceptance criteria before wide refactors |
| Context growth | `@concepts/long-thread-context-decay.md` mitigations; compaction / new session |
| Verification | Rubrics or lint gate before merge (`@concepts/agent-rubrics-self-correction.md`) |

### Cemini harness anchors [CONFIRMED existing stack]

- `Stop` hook — prevents runaway session completion loops
- Permission allowlists — throttle destructive tools
- `/goal` + Ralph — single acceptance envelope reduces unbounded iteration
- Subagent isolation — explore agent readonly; shell agent scoped

**Verdict:** **REFERENCE** — complements `@concepts/subagent-orchestration.md`; no new tool install.

## Snippets

> Backpressure loop for coding agents — flow control over unbounded agent output. [TENTATIVE — @bibryam, Posts.docx K103 Post 6]
