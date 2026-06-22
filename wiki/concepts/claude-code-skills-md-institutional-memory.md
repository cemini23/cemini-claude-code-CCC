---
title: Claude Code Skills.md — institutional memory vs stateless prompting
type: concept
tags: [concept, claude-code, skills, institutional-memory, k76]
keywords: [skills-md, behavioral-infrastructure, compound-effect, stateless-prompting, hermes-contrast]
related:
  - concepts/skill-vetting.md
  - concepts/claude-md-five-section-template.md
  - concepts/twelve-rule-claude-md-template.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/tools/hermes-agent.md
  - concepts/context-engineering.md
  - sources/trading-posts-macro-charts-skills-md-2026-05-28.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - entities/tools/nvidia-skills.md
  - entities/tools/mattpocock-skills.md
maturity: draft
created: 2026-05-28
updated: 2026-06-22
cross-wiki-source: "@osint-wiki/concepts/claude-code-skills-md-workflow.md"
---

## Relations

- `@concepts/skill-vetting.md` — Phase-0 gate before installing third-party skills
- `@concepts/claude-md-five-section-template.md` — CLAUDE.md hierarchy paired with Skills.md layer
- `@concepts/twelve-rule-claude-md-template.md` — complementary discipline template (rules vs five-section scaffold)
- `@entities/mcp-servers/anthropic-skills.md` — marketplace + SKILL.md spec surface
- `@entities/tools/nvidia-skills.md` — K126 signed skill distribution stub (OSINT canonical)
- `@entities/tools/mattpocock-skills.md` — K126 Adopt composable skill library stub
- `@entities/tools/hermes-agent.md` — runtime memory product contrast (not file-based Skills.md)
- `@concepts/context-engineering.md` — persistent files as context lever

Cross-wiki: `@osint-wiki/concepts/claude-code-skills-md-workflow.md`, `@osint-wiki/concepts/curator-skills.md`, `@osint-wiki/concepts/cemini-repository-topology.md`.

## Raw Concept

K76 Post 2 (@NainsiDwiv50980) — **Skills.md as lightweight behavioral infrastructure**: reusable markdown skills (standards, deploy flows, test gates, security rules) loaded persistently in Claude Code, compounding quality over weeks vs stateless per-session prompting.

## Narrative

### Skills.md vs stateless prompting

| Mode | Failure mode | Skills.md fix |
|------|--------------|---------------|
| Stateless prompting | Team conventions forgotten each session | Version-controlled skill files persist |
| Ad-hoc instructions | Inconsistent enforcement | Reusable intelligence layers |

### Compound effect [TENTATIVE]

File-based rules beat repeated natural-language reminders when the same conventions apply across many sessions. Treat productivity claims as pattern notes until benchmarked in Cemini workflows.

### vs Hermes / runtime memory

| Layer | Mechanism | CCC use |
|-------|-----------|---------|
| Skills.md / SKILL.md | Repo artifacts, git-reviewed | `~/.claude/skills/`, project skills |
| Hermes / claude-mem | Runtime/episodic memory products | Reference only; different trust model |

Skills.md is **institutional memory you commit**; Hermes is **session/runtime memory you don't necessarily version the same way**.

### CCC fit

- Adopt the **pattern** (persistent skill files + vetting), not viral skill packs without Phase-0.
- Pair with `@concepts/claude-md-five-section-template.md` for schema-level harness setup.
- Subsystem CLAUDE.md per repo folder aligns with `@osint-wiki/concepts/cemini-repository-topology.md`.

## Snippets

> "Skills.md is essentially lightweight behavioral infrastructure."
> — [Source: briefs/2026-05-28_k76-claude-skills-claude-md-workflows-from-osint.md]

> "The future belongs to AI systems that remember how you work, how your team builds, what your product architecture looks like."
> — [Source: @osint-wiki/sources/trading-posts-macro-charts-skills-md-2026-05-28.md, Post 2]
