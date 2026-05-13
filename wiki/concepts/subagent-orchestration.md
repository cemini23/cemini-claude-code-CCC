---
title: Subagent orchestration — when and how to delegate
type: concept
tags: [concept, subagent, agent, delegation, claude-code, parallelism, explore-agent, plan-agent]
keywords: [subagent, Agent tool, Explore agent, Plan agent, code-reviewer, general-purpose, isolation, worktree, parallel agents]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/cross-wiki-routing.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — the harness providing the `Agent` tool
- `@concepts/context-engineering.md` — subagent dispatch is one of the four levers
- `@concepts/token-economics-and-prompt-caching.md` — the cost trade-off behind subagent dispatch
- `@concepts/cross-wiki-routing.md` — multi-wiki queries are a canonical multi-subagent fan-out

Cross-wiki: `@osint-wiki/concepts/conductor-orchestrator.md` carries the OSINT-side conductor history (parallel subagent dispatch for cross-wiki queries).

## Raw Concept

Question this page answers: **when does Cemini delegate to a subagent rather than do the work in the parent session?**

## Narrative

Claude Code's `Agent` tool spawns an isolated subagent that gets its own context window, its own tool surface, and returns a single message to the parent. Several agent types are pre-defined:

| Type | When to use |
|------|-------------|
| `general-purpose` | Default; broad research / multi-step tasks |
| `Explore` | Read-only code search. Fast pattern-finding ("where is X defined / which files reference Y") |
| `Plan` | Architect-style implementation planning |
| `code-reviewer` | Independent second-opinion review |
| `statusline-setup` | Configures the harness status line |
| `claude-code-guide` | Q&A about Claude Code / Agent SDK / Anthropic API |

User-authored agents inherit a similar surface unless explicitly restricted.

### When to dispatch

The dispatch decision reduces to: **does the subagent save the parent more tokens than its own setup costs?**

- **Heavy reads (>10K of raw content)** — yes. The parent ingests the subagent's brief reply; the bulk of the read stays in the subagent's window.
- **Independent second opinions** — yes. Independence is the deliverable; the parent's context can't provide it.
- **Genuinely parallel work** — yes. Multiple subagents in a single message run concurrently. The parent waits for all replies.
- **Trivial lookups, single file reads** — no. Direct `Read`/`Grep` is cheaper.
- **Tasks requiring the parent's working state** — no. Subagents don't share the parent's context.

### Parallelism rules

When dispatching multiple independent subagents, **send them in a single message with multiple `Agent` tool uses**. They run concurrently. Sequential `Agent` calls run serially. Cemini's typical multi-subagent fan-out: 2-4 parallel agents for a Phase-0 audit (license check + entry-point read + dependency audit + maturity-signal check).

### Foreground vs background

- **Foreground** — block on the result. Use when the next action depends on the subagent's findings.
- **Background (`run_in_background: true`)** — fire-and-forget; you get notified when complete. Use for genuinely-independent work you can do alongside.

### Isolation

`isolation: "worktree"` puts the subagent in a temporary git worktree. Use when the subagent is going to edit files and you want the changes contained. Worktree auto-cleans on no-changes; on changes you get the path back.

### Prompt brief discipline

The subagent doesn't see the parent conversation. The prompt must be **self-contained**: state the goal, what's been ruled out, what the constraint is, what form the answer should take. Bad: "fix the bug." Good: "investigate why test_X.py fails on Python 3.11+; expected fix is in src/foo.py; report findings only — don't edit." Under-briefed subagents do shallow generic work.

### Cross-wiki orchestration

The `conductor` MCP server (`@entities/tools/conductor-mcp.md`) is a subagent-orchestration primitive for the federation: it fans a query across multiple wikis and returns one synthesis. The same pattern is reusable for any "search across N independent corpora and merge" problem — see `@concepts/cross-wiki-routing.md` for the routing layer that decides which wikis to fan to.

### What not to outsource

- **Synthesis and judgment.** "Based on the findings, fix it" pushes synthesis onto the subagent. The parent should integrate.
- **Per-session state writes.** Subagents don't share the parent's `hot.md` view. The parent updates `hot.md` after merging subagent results.
- **Anything requiring authorization the subagent doesn't have.** Subagents inherit permission allowlists; locked-down subagents can't run the tools the work needs.

## Dead Ends

- **Subagent for a 1-file read** — pays setup, saves nothing. Direct `Read`.
- **Serial subagent calls when they could be parallel** — wastes wall-clock time.
- **Trusting the subagent's summary as a description of what it did** — verify by checking the actual changes / outputs. The harness tracks file state separately.
