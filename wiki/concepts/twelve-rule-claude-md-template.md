---
title: "12-rule CLAUDE.md template (Karpathy → Forrest Chang → Mnilax)"
type: concept
tags: [concept, claude-md, prompting-discipline, agent-orchestration, karpathy-derivative, cross-wiki-stub]
keywords: [claude-md-12-rules, mnilax-extension, forrest-chang-4-rules, karpathy-jan-2026, checkpoint-discipline, fail-loud, token-budget, surface-conflicts]
related:
  - entities/tools/claude-code.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/context-engineering.md
  - concepts/subagent-orchestration.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/open-design.md
  - entities/tools/claude-code-tips.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/google-eng-practices.md
  - entities/tools/andrej-karpathy-skills-multica.md
  - entities/tools/three-man-team.md
  - concepts/claude-prompt-engineering-techniques.md
  - concepts/karpathy-token-efficiency-patterns.md
  - concepts/harness-de-bloat-4x4-pattern.md
  - concepts/claude-md-five-section-template.md
  - concepts/claude-code-skills-md-institutional-memory.md
  - concepts/karpathy-agent-infrastructure-basics.md
maturity: draft
created: 2026-05-17
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/concepts/claude-md-12-rule-template.md"
---

## Relations

- @entities/tools/claude-code.md — the harness that reads CLAUDE.md on every session start
- @entities/patterns/full-prompt-goal-template.md — `/goal` template is the single-shot analog; the 12-rule template is the persistent-context analog
- @concepts/context-engineering.md — the 12 rules are concrete operationalisations of the four context-engineering levers
- @concepts/subagent-orchestration.md — rule 11 (One In-Progress at a Time) is the concurrency-discipline foundation for subagent fan-out
- @concepts/cross-wiki-tool-eval-inventory.md — Karpathy's CLAUDE.md hit #1 on GitHub with 82k stars (K56 Posts.docx); the 12-rule template's lineage continues to evolve
- @osint-wiki/concepts/claude-md-12-rule-template.md — cross-wiki primary page (full lineage, empirical claims, and per-rule sourcing live there)
- @entities/tools/open-design.md — modular skill Markdown patterns applicable to CLAUDE.md sections
- @entities/tools/claude-code-tips.md — community tips (license unverified) — cherry-pick only after manual LICENSE read

## Raw Concept

CCC-side stub cross-routed from the OSINT-side primary. The 12 rules are a CLAUDE.md prompting-discipline template; their canonical write-up — including the Karpathy / Forrest Chang / Mnilax lineage, the empirical 3%-vs-41%-mistake-rate claim, and the full per-rule sourcing — lives in OSINT. This stub catalogues the rules and explains their Claude-Code-side relevance.

## Narrative

### Lineage (three-step)

1. **Andrej Karpathy (late Jan 2026, X thread)** — diagnosed silent assumptions, over-engineering, and unverified completions in Claude code work.
2. **Forrest Chang (`forrestchang/andrej-karpathy-skills`, created 2026-01-27)** — distilled Karpathy's diagnosis into a 4-rule prescriptive template.
3. **@Mnilax (X article, ~Apr 2026)** — added 8 rules covering May 2026 agent-orchestration failure modes.

### The 4 Forrest Chang rules

1. **Think Before Coding** — no silent assumptions; surface tradeoffs.
2. **Simplicity First** — minimum code that solves the problem.
3. **Surgical Changes** — touch only what you must.
4. **Goal-Driven Execution** — define success criteria; loop until verified.

### The 8 Mnilax additions

5. **Token Budget** — keep CLAUDE.md under 200 lines.
6. **Fail Loud** — no silent fallbacks; errors surface immediately.
7. **Checkpoint Discipline** — after every meaningful step, restate goal + state + next action.
8. **Surface Conflicts** — flag contradictions between user instructions or earlier decisions.
9. **No Mid-Stream Refactor** — finish requested task first; defer cleanup.
10. **Verify Before Claim** — never say "done" without running the actual verification.
11. **One In-Progress at a Time** — concurrency discipline for multi-step work.
12. **State Resumption Recipe** — every CLAUDE.md should explain how to resume after compaction/context-loss.

### CCC-side observations

- **Rule 5 vs CCC reality** — CCC's `CLAUDE.md` runs ~190 lines (within budget). The OSINT one runs longer (lineage-heavy historical detail); Cemini accepts that trade for that wiki and not for this one.
- **Rule 7 (checkpoint discipline)** is operationalised here via `hot.md` — the resume-from-hot.md ritual at session start is the same shape as rule 7's restate-goal-state-next-action loop.
- **Rule 12 (state resumption recipe)** is operationalised here via the `## Session-start ritual` section of CCC's CLAUDE.md (read `hot.md` first, then inbox check).

### Empirical claim (deferred to OSINT primary)

Mnilax cites a 3%-vs-41% mistake-rate delta between a 12-rule CLAUDE.md and a no-CLAUDE.md baseline. `[NEEDS VERIFICATION 2026-05-17]` — the methodology behind that number isn't published; OSINT's primary page flags this as author-asserted, not externally verified.

## Snippets

> Rule 5 — Token Budget: keep CLAUDE.md under 200 lines; budget context allocation.
[Source: @osint-wiki/concepts/claude-md-12-rule-template.md]

> Rule 12 — State Resumption Recipe: every CLAUDE.md should explain how to resume after compaction/context-loss.
[Source: @osint-wiki/concepts/claude-md-12-rule-template.md]
