---
title: tech-debt-skill — codebase audit skill for Claude Code
type: entity
tags: [tool, skill, code-review, tech-debt, claude-code, audit]
keywords: [tech-debt-skill, ksimback, TECH_DEBT_AUDIT.md, code quality audit, tech debt audit, looks bad but is fine]
related:
  - entities/tools/claude-code.md
  - entities/skills/tech-debt-audit.md
  - entities/commands/plugin.md
  - entities/mcp-servers/anthropic-skills.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/skills/tech-debt-audit.md` — the actual installed skill page (sibling, deeper detail)
- `@entities/commands/plugin.md` — install via `/plugin install`
- `@entities/mcp-servers/anthropic-skills.md` — example of a SKILL.md-spec-compliant adoption

## Raw Concept

`github.com/ksimback/tech-debt-skill`. Cemini's first installed third-party skill (per CCC `LESSONS.md` 2026-05-13: "Cemini's existing `~/.claude/skills/tech-debt-audit.md` was already 80% compliant; 3-field frontmatter upgrade brought it to 100%"). License + maturity: confirm via `gh api repos/ksimback/tech-debt-skill --jq '.license.spdx_id'` per `@entities/tools/claude-code.md` § Phase-0.

## Narrative

A Claude Code Agent Skill that audits a codebase end-to-end and produces a `TECH_DEBT_AUDIT.md` deliverable with file:line-cited findings, severity ratings, and effort estimates. Distinct from generic lint output in three ways:

1. **File:line citations** — every finding points to a specific span, not a category
2. **Severity ratings** — explicit (high/medium/low) rather than implicit
3. **Required "looks bad but is actually fine" section** — forces shallow analysis to be flagged. A skill that returns 50 findings without this section is suspect.

### Install + invocation

```
# in Claude Code:
/plugin marketplace add ksimback/tech-debt-skill
/plugin install tech-debt-audit
# then in any repo:
/tech-debt-audit
```

After install, the skill lives at `~/.claude/skills/tech-debt-audit.md` (user-scoped). Cemini retrofitted the SKILL.md frontmatter to the 2026-05-13-pinned spec — this was the example case in the LESSONS entry.

### Cemini's usage pattern

Run before:
- Showing code to anyone (client, investor, collaborator, recruiter)
- Major refactor decisions
- Pull-request review handoffs

Don't run:
- Continuously — whole-repo audits consume significant tokens (20-100K typical)
- On unfinished features — the audit will spam findings on incomplete code

### Token economics

A whole-repo audit on a moderately-sized repo (10-50 files, 5-20K LOC) typically uses:

- Input tokens: 30-100K (the model reads the codebase via `Read`/`Grep`)
- Output tokens: 5-20K (the audit findings)

This is non-trivial. Pair with `@entities/tools/ttok.md` to preview large repos before running, and with subagent dispatch (`@concepts/subagent-orchestration.md`) for very-large repos where the parent context shouldn't carry every file.

### What "looks bad but is fine" looks like

The skill's required section catches things like:
- Long functions that have valid reason to be long (parsers, state machines)
- "Magic numbers" that are well-named constants in domain context
- Repeated patterns that look like duplication but are intentional copy-for-evolution

A 50-finding audit with zero entries here is almost always a shallow pass — the skill itself is biased to find issues, and a real codebase always has at least some intentional-but-suspect-looking code.

## Dead Ends

- **Running tech-debt-audit on every commit** — burns tokens with diminishing return. Use on milestones.
- **Acting on every finding** — the audit's job is to surface; the human's job is to triage. Most "high" findings are work-worth-doing; many "medium" findings are intentional.
- **Using tech-debt-audit as a substitute for human review** — it's a complement. Different failure modes; both useful.
