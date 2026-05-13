---
title: spec-kit — GitHub's CLI for spec-driven development
type: entity
tags: [tool, spec-driven, sdd, github, cli, workflow, claude-code]
keywords: [spec-kit, specify, specify-cli, github spec kit, spec-driven development, scaffold from spec]
related:
  - entities/tools/claude-code.md
  - entities/tools/openspec.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/patterns/ralph-loop.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness that consumes spec-kit specs
- `@entities/tools/openspec.md` — sibling spec-driven workflow tool; structurally similar
- `@entities/patterns/full-prompt-goal-template.md` — `/goal` is a single-shot goal-pinning equivalent
- `@entities/patterns/ralph-loop.md` — Ralph's `prd.json` plays the same role spec-kit's spec plays

Cross-wiki: `@seo-wiki/entities/tools/claude-code-tool-stack.md` (Tool 6 of the SEO-side reference stack).

## Raw Concept

`github.com/github/spec-kit` — GitHub's CLI for **Spec-Driven Development**. The tool ships as `specify-cli`, installable via `uv tool install specify-cli` (auto-installs Python 3.11+ if needed). The flow: write a spec, validate it, generate scaffold code, iterate. The spec becomes documentation — useful when handing off to contractors or other devs.

## Narrative

spec-kit is the third member of CCC's spec-driven-workflow trio (alongside `@entities/tools/openspec.md` and Ralph's `prd.json`). All three encode "what done looks like" before the agent writes code. They differ in execution model and authoring overhead:

| Tool | Authored by | Execution model | Cemini posture |
|------|-------------|-----------------|----------------|
| spec-kit | GitHub | CLI-driven; `specify init` → spec → validate → scaffold | Documented, not adopted |
| OpenSpec | Fission-AI | Slash-command-driven inside Claude Code (`/opsx`) | Documented, not adopted |
| Ralph `prd.json` | snwfdhmp | Loop-shaped with fresh-context-per-iteration | Documented, not adopted |

The shared discipline is **stop vibe-coding**. Instead of "build me a landing page," you define the spec, validate it, then generate. The spec ships with the codebase as documentation.

### Install + use

```bash
uv tool install specify-cli
specify init my-project
# write spec.md inside the project
specify validate
specify generate
```

### Why CCC documents it without adopting it

For Cemini's solo-dev cadence the `/goal` template (`@entities/patterns/full-prompt-goal-template.md`) covers the same goal-pinning function with less authoring overhead. spec-kit / OpenSpec earn their slot when:

- Scope outgrows a single `/goal` invocation (multi-feature project)
- The spec needs to live as project documentation independently of the agent session
- A team handoff is expected (contractor, reviewer)

None of those is a Cemini-active workstream today.

### Comparison to the `/goal` template

`/goal` is single-shot, optimized for one task with clear acceptance criteria. spec-kit is multi-step, optimized for a project with stable scope across many sessions. Use `/goal` when the work fits in one prompt envelope; use spec-kit when it doesn't.

## Dead Ends

- **Adopting spec-kit without an active multi-feature project** — premature; would create dead spec docs that drift from reality.
- **Treating spec-kit and OpenSpec as interchangeable** — they share a goal-pinning function but differ in execution model and tooling integration. Pick one and stick.
