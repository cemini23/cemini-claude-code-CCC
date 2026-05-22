---
title: /goal — full-prompt single-shot meta-template
type: entity
tags: [pattern, prompt, goal, meta-prompt, claude-code, single-shot, template]
keywords: [the full prompt, /goal, success criteria, operating rules, plan first, work autonomously, no placeholders]
related:
  - entities/tools/claude-code.md
  - entities/tools/openspec.md
  - entities/patterns/ralph-loop.md
  - concepts/context-engineering.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/spec-kit.md
  - entities/tools/claude-for-legal.md
  - concepts/twelve-rule-claude-md-template.md
  - entities/patterns/autoresearch-loop.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - entities/tools/the-architect.md
maturity: validated
created: 2026-05-13
updated: 2026-05-22
---

## Relations

- `@entities/tools/claude-code.md` — the harness this template targets
- `@entities/tools/openspec.md` — structurally similar (goal-pinning), different execution model
- `@entities/patterns/ralph-loop.md` — sibling pattern; loop-based vs this single-shot
- `@concepts/context-engineering.md` — `/goal` is one of Cemini's primary context-engineering tools
- `@entities/tools/claude-for-legal.md` — "cold-start interviews" pattern: learn the institutional playbook before executing, same shape as `/goal`
- `@concepts/twelve-rule-claude-md-template.md` — the persistent-context analog; `/goal` is single-shot, 12-rule template is durable CLAUDE.md
- `@entities/patterns/autoresearch-loop.md` — `/goal` is a single-shot version of autoresearch's proposal stage
- `@concepts/code-as-agent-harness.md` — durable goal pinning via Stop-hook feedback control
- `@concepts/self-healing-agent-sessions.md` — Stop-hook must not create infinite self-heal loops

Cross-wiki: `@osint-wiki/sources/autonomous-agent-meta-prompt-2026-05.md` is the original source page with the verbatim template.

## Raw Concept

Single-shot meta-prompt template circulated on X in May 2026 (file `THE FULL PROMPT _goal.docx`, sha256 b9f610e3..., archived at `cemini-librarian:/opt/cemini-bulk/research/`). Cemini adopted the template as its modal way of starting non-trivial Claude Code sessions. The CCC bootstrap (this session) used a `/goal` invocation; the same envelope drives most Cemini workflows.

## Narrative

`/goal` is a slash command Cemini uses to seed a session with a long-form goal-condition. The harness's `Stop` hook blocks session termination until the condition holds — the goal stays active across model turns, hooks, and subagent calls until criteria are met. This makes the pattern *durable* in a way that putting goal text into the first user message is not (that text gets summarized away as context fills).

### Template structure

5 numbered sections + 10 operating rules:

1. **`/goal`** — one-line statement of what "done" looks like.
2. **`── CONTEXT ──`** — Project / Stack / Current state / Working dir / Constraints / Audience.
3. **`── SUCCESS CRITERIA (ALL MUST BE TRUE) ──`** — numbered list, each specific and measurable; ends with "runs without errors" + "you can show proof."
4. **`── OPERATING RULES — NON-NEGOTIABLE ──`** — 10 rules: PLAN FIRST · WORK AUTONOMOUSLY · SELF-VERIFY · DEBUG YOURSELF · USE EVERY TOOL · NO PLACEHOLDERS · PROGRESS LOG · STAY ON GOAL · IF BLOCKED · CHECK SUCCESS BEFORE STOPPING.
5. **`── QUALITY BAR ──`** + **`── FINAL DELIVERABLE ──`** — code clean/typed, docs every new pattern; deliverable = confirmation per criterion + every file modified + run/test/deploy instructions + proof + decisions + known limitations.

### Where this fits in Cemini's workflow

Modal use for non-trivial single-shot tasks. Concrete adoption sites today:

1. **Wiki bootstraps** — this CCC bootstrap is the case-in-point. 8 success criteria, ~16 pages written, lint clean, git initialized. The template's "CHECK SUCCESS BEFORE STOPPING" rule is exactly what gates the session-end.
2. **Phase-0 audits** — when auditing a new MCP server or skill, the `/goal` envelope formalizes "produce a GO/CONDITIONAL/NO-GO verdict, with evidence, against the per-tool-class failure-mode bullets."
3. **Brief-staging** — turning research insight into a `briefs/<date>_<slug>.md` deliverable. The 5-section structure (goal / context / success / rules / quality bar) maps cleanly to the brief's body sections.

### When NOT to use the full template

- Routine tasks (status, lint, single-file edit). The 10-rule operating envelope is heavy for short tasks; default to a lighter prompt.
- Ambiguous tasks. "WORK AUTONOMOUSLY" + "Don't ask clarifying Qs unless genuinely blocked" pushes the agent to guess rather than ask, which is wrong for tasks where Cemini's intent isn't clear from the goal-condition. For ambiguous tasks, drop AUTONOMOUSLY and replace with "ASK CLARIFYING QUESTIONS FIRST."

### Cemini-specific adaptations

- **Goal-condition character limit**: the harness enforces a 4000-char limit on the goal field. The CCC bootstrap goal had to be compressed from 8794 chars to fit. The result was lower readability but tighter focus — Cemini now drafts the long version first, then prunes to fit.
- **CROSS-WIKI BACKLINKS**: when the goal touches multiple wikis, the template gets a "bidirectional cross-wiki links" criterion. Easy to forget; build it into the SC list.
- **LOCAL-ONLY CONSTRAINT**: laptop-only wikis (CCC, Cybersecurity, 3D-printing, Image-gen, SEO) need an explicit "NO REMOTE, NO PUSH" in the constraints block, otherwise the agent helpfully offers to push.

## Snippets

Operating rules (verbatim from source):

> 1. PLAN FIRST. Output a numbered task list before writing any code.
> 2. WORK AUTONOMOUSLY. Don't ask clarifying Qs unless genuinely blocked.
> 3. SELF-VERIFY. After every step: run tests, inspect output, confirm it worked.
> 4. DEBUG YOURSELF. If it fails, diagnose + fix. Don't hand it back.
> 5. USE EVERY TOOL. MCPs · terminal · web · code exec · pull real data.
> 6. NO PLACEHOLDERS. No TODOs · no stubs · real components + real states.
> 7. PROGRESS LOG. Track completed · in-flight · decisions · blockers.
> 8. STAY ON GOAL. Discoveries off-spec? Note + keep moving.
> 9. IF BLOCKED. Log the wall · continue everything parallelizable.
> 10. CHECK SUCCESS BEFORE STOPPING. Re-read criteria · confirm each is met.

## Dead Ends

- **"USE EVERY TOOL" without constraint** — in Cemini contexts this could include unsafe tools (e.g., trading-server writes). Always pair with explicit deny-listing in `.claude/settings.json`.
- **Goal field as a dumping ground** — over-long goals get summarized away. Pin the 5-10 most-load-bearing sentences; off-spec context goes in `hot.md` / `ROADMAP.md`.
