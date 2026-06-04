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
updated: 2026-06-04
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

**Verdict:** **CONDITIONAL-GO** — isolated trial on one CCC wiki chapter export before prod skills dir.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README skim. No install / no MCP wire-up.

| Check | Result |
|-------|--------|
| License | **MIT** — API verified [CONFIRMED] |
| Maturity | **13,934★**; v3.7.0; **3,445+** tests; PyPI `skill-seekers`; last push **2026-05-31** |
| Surface | CLI + optional **40-tool MCP** integration — large blast radius if enabled blindly |
| Failure mode | **License inheritance** from scraped corpora; generated SKILL.md quality vs hand-authored wiki exports |

**Decision — CONDITIONAL-GO.** Mature OSS with real test coverage. **Conditions:** (1) one-shot CLI export of a single CCC wiki chapter into temp dir; (2) run full `@concepts/skill-vetting.md` on output before copying to `~/.claude/skills/`; (3) do **not** enable MCP server in prod until tool list audited. Compare output to manual brief→skill workflow first.

## Adoption trial (2026-06-04)

| Step | Result |
|------|--------|
| `pip install skill-seekers` (v3.7.0) | **PASS** |
| `skill-seekers create ./wiki/concepts --name ccc-skill-vetting` | **PARTIAL** — SKILL.md + references generated; auto-enhance failed (no headless Claude in trial shell) |
| `skill-seekers package … --target markdown` | **PASS** — `/tmp/ccc-adopt-trials-20260604/skill-seekers-out-markdown.zip` (249 KB) |
| `skill-scanner scan` on output | **SAFE** (1 LOW) |

**Posture:** **ADOPTED (CLI workflow)** — use for wiki→skill exports with `--skip-enhance` or manual vetting; do not enable 40-tool MCP until audited.

## Snippets

> doc→skill pipeline; compare output to wiki export workflow.
> — [Source: @osint-wiki/entities/tools/skill-seekers.md]
