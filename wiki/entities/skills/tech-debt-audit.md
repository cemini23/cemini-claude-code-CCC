---
title: tech-debt-audit (skill) — Cemini's installed code-audit skill
type: entity
tags: [skill, claude-code, tech-debt, audit, installed, SKILL.md, cemini]
keywords: [tech-debt-audit, ksimback, ~/.claude/skills, SKILL.md compliant, 100% compliant, retrofit, K42 example]
related:
  - entities/tools/tech-debt-skill.md
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
  - entities/tools/cc-thinking-skills.md
  - entities/tools/jezweb-claude-skills.md
  - entities/skills/cursor-audit.md
  - entities/skills/super-audit.md
maturity: validated
created: 2026-05-13
updated: 2026-06-09
---

## Relations

- `@entities/tools/tech-debt-skill.md` — the upstream repo this skill came from
- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/anthropic-skills.md` — the SKILL.md spec this skill is 100% compliant with
- `@entities/commands/plugin.md` — install path
- `@entities/skills/cursor-audit.md` — targeted multi-model debug/review; run cursor-audit on stuck bugs; tech-debt-audit for whole-repo sweeps
- `@entities/skills/super-audit.md` — pre-ship five-model council; complementary to whole-repo tech-debt pass

## Raw Concept

Lives at `~/.claude/skills/tech-debt-audit.md`. Cemini's first installed third-party Claude Code skill. The skill that motivated CCC's `LESSONS.md` 2026-05-13 entry on adopting the SKILL.md frontmatter spec internally.

## Narrative

CCC's `LESSONS.md` (2026-05-13 entry) records: *"Cemini's existing `~/.claude/skills/tech-debt-audit.md` was already 80% compliant; 3-field frontmatter upgrade (license + metadata.author + metadata.version) brought it to 100%. No body changes; backwards-compatible."*

This page is the canonical documentation of the installed skill — distinct from `@entities/tools/tech-debt-skill.md` (the upstream repo) because:

- The installed skill carries Cemini's frontmatter retrofit
- The installed skill is what the harness actually loads
- Future spec drift will be tracked here, not at the upstream repo page

### Current frontmatter (after 2026-05-13 retrofit)

```yaml
---
name: tech-debt-audit
description: Whole-codebase tech-debt audit producing TECH_DEBT_AUDIT.md with file:line cited findings, severity, effort estimates, and a required "looks bad but is actually fine" section.
license: MIT
metadata:
  author: ksimback
  version: 0.1.0
disable-model-invocation: false
---
```

The frontmatter matches the SKILL.md spec snapshot pinned in CCC `LESSONS.md`. Future skill-spec changes (instructa drift, Anthropic updates) will land here as version bumps.

### Invocation

The skill responds to:
- Slash command: `/tech-debt-audit` in any repo
- Natural-language match against the `description:` field (e.g., "audit this codebase for tech debt")

Either path triggers the same body protocol — the harness reads the SKILL.md, the LLM follows the protocol's instructions to traverse the repo and emit the audit deliverable.

### Cemini's audit cadence

- **Pre-handoff** — before any code shown to a third party
- **Pre-major-refactor** — to baseline the surface area
- **Quarterly** — on the CCC wiki itself (audit `wiki/` and `scripts/` for accumulated drift; not standard for prose wikis but useful for the script side)
- **Never per-commit** — token-economics doesn't justify continuous use

### Linkage to skill-vetting hygiene

The retrofit demonstrated CCC's posture from `@entities/mcp-servers/anthropic-skills.md`: adopt the *spec*, control the *content*. By rewriting the frontmatter locally, Cemini gains versioning and license tracking without depending on upstream catalog churn (per `LESSONS.md` 2026-05-13: catalog content is too short-lived to mirror).

## Dead Ends

- **Editing this skill's body without versioning** — body changes should bump `metadata.version` and append a one-line changelog comment.
- **Treating the upstream repo as the source-of-truth for what's installed** — the installed copy is the source-of-truth for what *Cemini's* skill does. Drift is intentional once retrofitted.
