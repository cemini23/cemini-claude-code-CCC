---
title: Ralph loop — file-based memory for autonomous Claude Code iterations
type: entity
tags: [pattern, ralph, loop, autonomous-agent, file-based-memory, claude-code, prd-json]
keywords: [ralph, awesome-ralph, prd.json, progress.txt, PROMPT_plan.md, PROMPT_build.md, fresh-context iteration, agent loop]
related:
  - entities/tools/claude-code.md
  - entities/tools/openspec.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/tools/spec-kit.md
  - entities/patterns/cpr-context-compression.md
  - entities/patterns/autoresearch-loop.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — the harness Ralph runs on
- `@entities/tools/openspec.md` — structurally similar (spec-driven), different execution model
- `@entities/patterns/full-prompt-goal-template.md` — sibling pattern; single-shot vs loop
- `@concepts/context-engineering.md` — Ralph's fresh-context-per-iteration is the core context-engineering trick
- `@concepts/token-economics-and-prompt-caching.md` — Ralph's many fresh contexts trade prompt-cache amortization against context-degradation avoidance
- `@entities/tools/spec-kit.md`, `@entities/tools/openspec.md` — sibling spec-driven workflow tools (different execution model)
- `@entities/patterns/cpr-context-compression.md` — Ralph's file-based memory is exactly the CPR preserve leg in different terminology
- `@entities/patterns/autoresearch-loop.md` — Ralph is the simpler sibling (no explicit objective function); autoresearch adds the scoring + mutation legs

Cross-wiki: `@osint-wiki/concepts/ralph-autonomous-agent-pattern.md` carries the original audit + Steal-from verdict; this page is the CCC-side adoption brief.

## Raw Concept

Distilled from `github.com/snwfdhmp/awesome-ralph` (K-series audit, MIT, Steal-from verdict). The OSINT side did the audit; CCC carries the pattern as a reusable workflow primitive that Claude Code sessions might invoke.

## Narrative

Ralph is an autonomous-AI-coding pattern that runs Claude Code in continuous loops until requirements are demonstrably fulfilled. The critical design choice: **isolate each iteration with a fresh context window**, manage state via persistent file structures rather than relying on degrading long-context coherence.

### Why fresh-context-per-iteration

Long Claude Code sessions degrade as context fills:
- Earlier instructions get forgotten / overridden
- File-state snapshots from earlier in the session conflict with current disk state
- Hallucinations compound once the model "remembers" something inaccurate from earlier in the same turn

Ralph's answer: **don't extend context — checkpoint to disk and restart**. Each loop iteration is a fresh agent with the same persistent-file state. The agent re-reads `prd.json` + `progress.txt` + recent git log + relevant code, decides next step, executes, commits, exits. Next loop iteration: fresh context, same persistent state.

### Three persistent artifacts

1. **`prd.json`** — Product Requirements Document. Structured task list: user stories, acceptance criteria, completion status per task. Source of truth for "what done looks like."
2. **`progress.txt`** — append-only ledger of what the agent did each iteration. Survives across restarts.
3. **Git history** — the actual code state. Each loop iteration commits its work.

### Two-mode workflow

**Plan mode** — gap analysis without implementation:
- Read `prd.json`, identify next incomplete task
- Read existing code, identify the gap between current state and target state
- Output a `PROMPT_build.md` describing the implementation plan
- **Does not write code.**

**Build mode** — execute the plan:
- Read `PROMPT_build.md`
- Implement the change
- Run tests
- Commit
- Update `progress.txt`

Loop: plan → build → verify → plan → build → verify… until `prd.json` reports all tasks complete.

### Cemini-side adoption

Cemini has not yet wired Ralph into a Cemini workflow. The pattern is documented because:

1. **K-series ingest workflow** is loop-shaped (preingest_check → read → discuss → write pages → lint → commit) and a `K-series-prd.json` template could formalize what's currently informal.
2. **Brief-staging workflow** is plan-then-build (draft brief → review → ship) and could split into segregated `PROMPT_plan.md` + `PROMPT_build.md`.
3. **The `/loop` slash command** is Claude Code's native Ralph-equivalent — a thinner, harness-level version of the same idea.

What Cemini does NOT take from Ralph: the shell-script orchestration loops (operational hazard on the production trading server) and bash-driven autonomous git operations (force-overwrites from hallucinating agents are unacceptable risk).

### Comparison to `/goal` single-shot

| Dimension | Ralph (loop-based) | `/goal` template (single-shot) |
|---|---|---|
| Iteration model | Fresh context per loop iteration | One context window, end-to-end |
| State management | `prd.json` + `progress.txt` files | Inline `PROGRESS LOG` rule + final deliverable summary |
| Failure handling | Loop continues until prd.json all complete | Self-verify + debug-yourself, don't hand back |
| Best for | Long-running multi-task projects | Single complex task with clear success criteria |
| Cost profile | Many fresh-context loops = many startup tokens | One long context, may degrade past 100K tokens |

Both are reference templates; pick by task shape.

## Dead Ends

- **Trying to make Ralph the *primary* orchestrator** — eval Reject grade on production-stack fit. Steal-from-only.
- **Wiring shell-scripted git autonomy into the workspace laptop** — operational hazard for the curated wiki repository.
