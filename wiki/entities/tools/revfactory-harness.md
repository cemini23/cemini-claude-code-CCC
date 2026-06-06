---
title: revfactory/harness — dynamic Claude Code agent-team generator
type: entity
tags: [tool, agent-harness, adopt-candidate, k93]
keywords: [revfactory, harness, meta-skill, agent-teams, apache-2.0]
related:
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/subagent-orchestration.md
  - entities/tools/claude-code.md
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
  - "@osint-wiki/entities/tools/revfactory-harness.md"
  - concepts/cross-wiki-tool-adoption-routing.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - entities/tools/typst.md
  - entities/tools/flowforge-skill.md
maturity: draft
created: 2026-06-01
updated: 2026-06-06
---

## Relations

- `@concepts/thin-harness-fat-skills-garrytan.md` — garrytan thin-harness thesis (Posts K93)
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — arXiv 2605.30621 design rules
- `@concepts/subagent-orchestration.md` — scatter/gather complement
- `@entities/tools/claude-code.md` — host harness
- `@sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` — K93 v5 Adopt
- `@osint-wiki/entities/tools/revfactory-harness.md` — OSINT canon

## Raw Concept

`revfactory/harness` — meta-skill that **generates domain-specific Claude Code agent teams** on demand. Apache-2.0 `[CONFIRMED 2026-06-01]` (~5.1k★). K93 v5 **Adopt**.

## Narrative

| Check | Verdict |
|-------|---------|
| Overlap with `.cursor/rules/` + conductor | Compare before wiring — may duplicate orchestration |
| Phase-0 | **DONE** 2026-06-04 — see `## Phase-0 Audit` |
| vs ECC / SuperClaude | Parallel harness bundles — pick one after hook audit |

**Verdict:** **CONDITIONAL-GO** — isolated profile trial only; map output to `@concepts/claude-code-subagent-templates.md`.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README skim. No plugin install.

| Check | Result |
|-------|--------|
| License | **Apache-2.0** — API verified [CONFIRMED] |
| Maturity | **5,843★**; v1.2.0; last push **2026-05-29** |
| Behavior | Claude Code plugin — domain sentence → `.claude/agents/` + `.claude/skills/` via 6 team-architecture patterns |
| Failure mode | **Orchestration duplication** vs `.cursor/rules/` + conductor; **write blast radius** to project `.claude/` tree |

**Decision — CONDITIONAL-GO.** License clean; real adoption value for greenfield team scaffolding. **Conditions:** (1) trial in throwaway git worktree, not main CCC wiki tree; (2) diff generated agents against existing `@concepts/subagent-orchestration.md` templates before merge; (3) pick **one** meta-harness bundle (Harness vs ECC vs SuperClaude) — do not stack. **NO-GO** for librarian/prod deploy.

## Adoption trial (2026-06-04)

| Step | Result |
|------|--------|
| `claude plugin marketplace add revfactory/harness` | **PASS** |
| `claude plugin install harness@harness-marketplace` | **PASS** — user scope |
| Agent Teams flag | **Not set** — requires `export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` before first harness generation |

**Posture:** **ADOPTED (Claude Code plugin, user scope)** — invoke via Claude Code CLI on this laptop; do not generate into main CCC wiki tree without worktree isolation.

## Adoption trial (2026-06-04) — full run

| Step | Result |
|------|--------|
| `claude plugin list` | **PASS** — `harness@harness-marketplace` enabled |
| Worktree probe | **PASS** — branch `trial/harness-20260604` created then removed |
| Generation trial | **BLOCKED** — `claude -p` requires Anthropic API key (org subscription disabled for Claude Code) |
| AGENT_TEAMS flag | Required before generation — `export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` |

## Snippets

> "Generates domain-specific agent teams on the fly." — K93 v5 eval URL 3.
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md]
