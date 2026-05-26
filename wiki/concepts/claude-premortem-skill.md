---
title: Claude pre-mortem skill — ship-gate before agent harness changes
type: concept
tags: [concept, skills, claude-code, phase-0, safety, k67]
keywords: [pre-mortem, skill-md, itsolelehmann, harness-changes, failure-modes, skill-audit]
related:
  - concepts/skill-vetting.md
  - concepts/hooks-for-automation.md
  - concepts/code-as-agent-harness.md
  - entities/tools/claude-code.md
  - entities/tools/openspec.md
  - concepts/agent-vm-sandboxing.md
  - concepts/claude-code-personal-os-scope.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
---

## Relations

- `@concepts/skill-vetting.md` — pre-mortem runs **before** Phase-0 GO on new third-party skills
- `@concepts/hooks-for-automation.md` — hook/skill changes share blast-radius review
- `@concepts/code-as-agent-harness.md` — harness edits are in scope for pre-mortem
- `@entities/tools/claude-code.md` — host for custom `SKILL.md` install
- `@entities/tools/openspec.md` — spec-first changes pair with pre-mortem on agent behavior
- `@concepts/agent-vm-sandboxing.md` — isolate first run after pre-mortem passes

Cross-wiki: K67 Post 29 (@itsolelehmann) via `@osint-wiki/briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md`.

## Raw Concept

K67 brief — **pre-mortem SKILL.md** pattern: before shipping Claude Code agent/skill/hook changes, run a structured failure-mode review. CCC adoption as **pattern** (author skill not vendored wholesale).

## Narrative

### What it is [TENTATIVE — X long-form only]

A project-local skill that forces the agent (or human operator) to enumerate **what could go wrong** before merging harness changes: hook loops, permission broadening, credential leakage, context pollution, irreversible `Stop` hooks, parallel subagent cost explosions.

### CCC fit

| Gate | When |
|------|------|
| `@concepts/skill-vetting.md` | Third-party skill **install** |
| Pre-mortem (this page) | **Authoring** CCC-internal skills, hooks, conductor routing tweaks |
| OpenSpec / brief | Multi-step harness refactors |

**Adopt posture:** **GO (pattern)** — implement as `~/.claude/skills/` or project skill after human review of upstream template; do not auto-install from X link without Phase-0.

### Explicit non-actions

- Not a substitute for `@concepts/skill-vetting.md` on external skills.
- Not required for wiki-only markdown edits (no harness blast radius).

## Snippets

> "Pre-mortem SKILL.md before shipping agent changes — aligns with skill_audit + Phase-0 audit gates."
> — [Source: briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md, Post 29]
