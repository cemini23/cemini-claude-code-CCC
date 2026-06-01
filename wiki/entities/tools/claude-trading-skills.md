---
title: claude-trading-skills — trading skill pack (Phase-0 pending)
type: entity
tags: [tool, skills, trading, adopt-candidate, k92]
keywords: [claude-trading-skills, trading, skills, k92-eval]
related:
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/claude-code-finance-research-setup.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- `@concepts/skill-vetting.md` — mandatory Phase-0 before install
- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md surface
- `@concepts/claude-code-finance-research-setup.md` — finance harness context (OSINT-primary)
- `@sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md` — K92 v7 Adopt tier

## Raw Concept

K92 v7 eval lists **claude-trading-skills** as **Adopt → CCC**. Exact `owner/repo` slug **`[NEEDS VERIFICATION 2026-06-01]`** — run `gh api` + README audit before any `~/.claude/skills/` install.

## Narrative

Likely a **curated trading-analysis skill bundle** for Claude Code. CCC financial execution stays on OSINT / CeminiSuite — treat skills as **research prompts only**, not execution authority.

**Verdict:** **CONDITIONAL-GO** — Phase-0: SPDX license, skill count, credential leakage scan, catalog-mirror policy.

## Snippets

> K92 v7 Adopt — claude-trading-skills routed to CCC; verify repo URL on Phase-0.
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
