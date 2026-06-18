---
title: Agents All the Way Down — custom agent build methodology
type: concept
tags: [concept, custom-agents, methodology, turtle-pattern, k115]
keywords: [2606.11869, p1-p5, turtle-pattern, agent-tests-agent]
related:
  - sources/arxiv-agents-all-the-way-down-2606.11869.md
  - concepts/code-as-agent-harness.md
  - entities/tools/claude-code.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/skill-vetting.md
  - concepts/claude-honesty-critic-agent.md
  - concepts/specification-driven-scientific-workflow-management.md
maturity: draft
created: 2026-06-15
updated: 2026-06-18
---

## Relations

- `@sources/arxiv-agents-all-the-way-down-2606.11869.md` — UPC methodology paper
- `@concepts/code-as-agent-harness.md` — harness substrate (P1)
- `@entities/tools/claude-code.md` — P3 general-purpose prototype tier
- `@concepts/ship-subagent-writer-reviewer-tester.md` — P5 behavioral eval pattern
- `@concepts/skill-vetting.md` — P2 security allow-lists
- `@concepts/claude-honesty-critic-agent.md` — P5 critic variant

## Raw Concept

What is the published practice for building a custom in-app agent when Claude Code is the bench saw?

## Narrative

**Agents All the Way Down** [TENTATIVE — single methodology paper]: five-phase practice with **two one-time preconditions** (substrate + building blocks) and **three repeating practices** (prototype → harvest CLI → agent-tests-agent).

| CCC mapping | Phase |
|-------------|-------|
| `CLAUDE.md` + prompt cache discipline | P1 Substrate |
| MCP, skills, hooks, slash commands | P2 Building blocks |
| Cursor/Claude Code on real repo | P3 Prototype |
| `briefs/` → `settings.json` / skills / CLI | P4 Turtle harvest |
| `/ship`, honesty critic, eval prompts | P5 Agent-tests-agent |

**When to build custom** (need ≥1 axis): embedded domain prompt, private tools, in-app deployment, tight allow-list, model routing, brand/audit.

**When not to:** general Claude Code + conductor already covers the job — aligns with CCC posture on Hermes/OpenClaw as reference-only.

**Verdict:** **REFERENCE** — methodology catalog; no framework install.

## Snippets

> "P4 — Harvest, fold, ship as CLI — the Turtle pattern."

> "An agent that needs none of the six axes should not be built — the general-purpose tier handles it."
