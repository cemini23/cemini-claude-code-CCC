---
title: marketingskills (coreyhaines31) — marketing-framework Claude Code skill bundle
type: entity
tags: [skill, claude-code, marketing, copywriting, claude-code-agent-skill, plugin]
keywords: [marketingskills, coreyhaines31, PAS copywriting, brand voice context, localized email drafting, marketing frameworks]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/anthropic-skills.md` — the SKILL.md spec this skill follows
- `@entities/commands/plugin.md` — install path

Cross-wiki: `@seo-wiki/entities/tools/marketingskills.md` carries the operator-facing write-up + Phase-0 GO verdict.

## Narrative

`github.com/coreyhaines31/marketingskills` — Claude Code Agent Skill bundle that provides **marketing-framework templates** instead of generic GPT wrapping. The bundle's distinguishing trait: it encodes specific marketing frameworks (PAS copywriting, brand-voice context capture, localized email/social drafting) as SKILL.md protocols rather than free-form prompts.

CCC tracks this skill as a concrete example of:

1. **Bundle-shaped skills** — one `/plugin install` exposes multiple skill files. Most installable Claude Code skills follow this shape.
2. **Framework-encoded skills** — vs. "be helpful with marketing" prompts. Framework-encoded skills produce more consistent output across sessions.

### Install

```
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

### Skill surfaces (representative)

The bundle includes skills for:
- **PAS copywriting** — Problem / Agitate / Solve copywriting framework
- **Brand-voice context** — capture a brand's voice from sample text, then apply consistently to new drafts
- **Localized drafting** — geo-aware email + social posts (overlap with `@entities/skills/claude-seo-agrici.md` for local SEO)
- **Campaign-stage templates** — awareness / consideration / conversion-stage copy

### Cemini-relevant adoption notes

- **Used by Cemini for SEO-wiki workflows** — when drafting client-facing marketing material in the SEO wiki, this skill bundle is the modal helper
- **Not used in OSINT / Cybersec / 3D-printing / Image-gen** — domain mismatch
- **No NSFW handling** — appropriate boundaries hard-coded; not a fit for image-gen wiki workflows that require explicit content

### Spec compliance

Per CCC `LESSONS.md` 2026-05-13: catalog skills with strong adoption are candidates for Cemini-side frontmatter retrofit. As of 2026-05-13, marketingskills is installed but not retrofitted — see `@entities/skills/tech-debt-audit.md` for the pattern when the time comes.

## Dead Ends

- **Treating PAS copywriting output as ship-ready** — it's first-draft. The "human-in-the-loop" rule from `@seo-wiki/concepts/ai-assistance-guardrails.md` applies: rewrite at least 30-50% in human voice before publishing.
- **Using marketingskills outside the marketing domain** — domain mismatch. The framework prompts assume marketing intent; misuse produces marketing-style output for inappropriate contexts.
