---
title: npxskillui — skill UI / marketplace CLI (Phase-0 pending)
type: entity
tags: [tool, skills, ui, adopt-candidate, k90]
keywords: [npxskillui, skill-ui, npm, claude-skills]
related:
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/tools/skillkit.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- `@concepts/skill-vetting.md` — Phase-0 before any catalog install
- `@entities/mcp-servers/anthropic-skills.md` — spec-only policy
- `@entities/tools/skillkit.md` — sibling skill-management tooling
- `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — K90 v6 Adopt

## Raw Concept

K90 v6 **Adopt** — `npxskillui` skill UI / discovery CLI (exact GitHub org/repo — verify on Phase-0 **`[NEEDS VERIFICATION 2026-05-31]`**). Gemini tier Adopt; run `gh api` before install.

## Narrative

Potential accelerator for browsing/installing skills — **conflicts with LESSONS.md catalog-mirror policy** if it pulls remote skill bodies into `~/.claude/skills/` without audit.

**Verdict:** **CONDITIONAL-GO** — Phase-0: license SPDX + sample skill audit + hook collision check with claude-mem.

## Snippets

> K90 v6 Adopt — npxskillui; verify repo + license before install.
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]
