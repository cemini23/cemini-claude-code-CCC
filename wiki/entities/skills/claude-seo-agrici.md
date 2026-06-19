---
title: claude-seo (AgriciDaniel) — local-SEO Claude Code skill
type: entity
tags: [skill, claude-code, seo, local-seo, gbp, NAP, claude-code-agent-skill, cc-by]
keywords: [claude-seo, AgriciDaniel, /seo local, /seo nap, /seo grid, /seo competitors, local pack, GBP, NAP consistency, doorway page safeguard]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
  - entities/skills/geo-seo-claude.md
  - concepts/agent-first-web-framework.md
maturity: validated
created: 2026-05-13
updated: 2026-06-19
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/anthropic-skills.md` — the SKILL.md spec this skill follows
- `@entities/commands/plugin.md` — install path

Cross-wiki: `@seo-wiki/entities/tools/claude-seo-agrici.md` is the operator-facing canonical write-up (full slash-command catalog + use cases). `@seo-wiki/sources/github-repo-audit-2026-05-07.md` is the Phase-0 GO verdict.

## Narrative

`github.com/AgriciDaniel/claude-seo` — CC-BY, ~3.5K stars, last commit 2026-04-30. A Claude Code Agent Skill bundle focused **specifically on brick-and-mortar local SEO**: GBP audit, NAP consistency, geo-grid local-pack rank tracking, competitor radius mapping.

CCC documents this skill (rather than the upstream tool, which lives in the SEO wiki) because it's a concrete real-world example of Cemini's `@entities/mcp-servers/anthropic-skills.md` adoption pattern — Phase-0 audited, installed, used, and SKILL.md-spec-compliant.

### Slash commands (representative; verify against current repo)

- `/seo local <url>` — audit a local-business website's on-page + schema + NAP
- `/seo maps` — analyze GBP listing fundamentals
- `/seo nap <business-name>` — sweep top citation directories for NAP consistency
- `/seo grid <listing-url>` — geo-grid rank-track for the listing's primary queries
- `/seo competitors <city>` — discover local-pack competitors

### Install

```
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install seo
```

### Built-in policy safeguards (worth noting)

The repo specifically implements **doorway-page prevention** — programmatic warning at 30 generated location pages, hard stop at 50. This is unusually disciplined for an open-source SEO tool and aligns with hard-policy boundaries Cemini cares about (no doorway pages, no thin city-clone content).

### Why CCC tracks this skill (not just the SEO wiki)

- **Concrete adoption record** — proves Cemini operationally depends on at least one third-party SKILL.md skill
- **Cross-wiki link target** — Cemini sessions starting in CCC need a path to the SEO-side operator documentation
- **Spec-compliance evidence** — the skill is one of the cleanest examples of the SKILL.md frontmatter pattern Cemini pins to

### Cemini-relevant failure modes

- **`/seo` command-namespace collision** — if both `claude-seo-agrici` and the GEO-focused `geo-seo-claude` (`@entities/skills/geo-seo-claude.md`) are installed, both expose `/seo:*` commands. Verify install order or rename if conflicts surface.
- **External-API rate limits** — depending on how `/seo` skills fetch SERP data, costs may apply. Cap with `numResults` parameters where exposed.

## Dead Ends

- **Treating the slash commands as exhaustive** — verify against the current repo README; the skill ships updates that change the command surface.
- **Running `/seo grid` from inside a target shop** — the geo-grid still works (the tool emulates multiple lat/longs) but conceptually misrepresents customer-perspective reality.
