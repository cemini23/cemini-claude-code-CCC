---
title: Skill_Seekers — docs/repos/PDF to Claude skill converter (Phase-0 pending)
type: entity
tags: [tool, skills, adopt-candidate, k88]
keywords: [skill-seekers, yusufkaraaslan, doc-to-skill, pdf-to-skill, mcp]
related:
  - entities/tools/book-to-skill.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - "@osint-wiki/entities/tools/skill-seekers.md"
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/entities/tools/skill-seekers.md"
---

## Relations

- `@entities/tools/book-to-skill.md` — sibling book-corpus pipeline
- `@concepts/skill-vetting.md` — Phase-0 on generated skills
- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md spec compliance
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 Adopt

## Raw Concept

K88 **Adopt** — `github.com/yusufkaraaslan/Skill_Seekers`. MIT. Converts documentation sites, GitHub repos, PDFs into Claude skills with conflict detection.

## Narrative

**Steal-from use:** accelerate wiki→skill exports (`briefs/` → `.claude/skills/`). **Risk:** license inheritance from source corpora; generated skill quality vs hand-authored `@entities/skills/tech-debt-audit.md`.

**Verdict:** **CONDITIONAL-GO** — isolated Phase-0 on one CCC wiki chapter export before prod skills dir.

## Snippets

> doc→skill pipeline; compare output to wiki export workflow.
> — [Source: @osint-wiki/entities/tools/skill-seekers.md]
