---
title: agent-skill-manager (asm) — Claude/Codex skill registry CLI
type: entity
tags: [tool, skills, cursor, k103]
keywords: [asm, luongnv89, skill-registry, batch-ingest]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - entities/tools/claude-skill-registry.md
  - "@osint-wiki/entities/tools/agent-skill-manager.md"
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
phase_0_verdict: "CONDITIONAL-GO 2026-06-07 — MIT; isolated skill dirs only"
---

## Relations

- `@sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md` — K103 Adopt
- `@concepts/agent-skills-progressive-disclosure.md` — SKILL.md loading model
- `@concepts/skill-vetting.md` — Phase-0 before global symlink
- `@entities/tools/claude-skill-registry.md` — registry pattern peer (K88)
- `@osint-wiki/entities/tools/agent-skill-manager.md` — canonical Phase-0 audit

## Raw Concept

- **URL:** https://github.com/luongnv89/asm
- **Tier:** Adopt CONDITIONAL-GO (CCC-wiki primary)
- **License:** MIT [CONFIRMED 2026-06-07]
- **Stars / push:** ~350★ / 2026-06-03 [TENTATIVE]

## Narrative

TypeScript CLI for modular agent skill registries — batch ingest, `asm eval`, provider integrations for Claude Code and Codex. Complements `.cursor/mcp.json` lazy-tool routing without replacing conductor/kb-server.

**Phase-0 CONDITIONAL-GO:** laptop-only; pin version; **never** auto-symlink into prod `~/.claude/skills` paths. Failure mode: overwriting mixed-repo skill directories.

**Install:** `scripts/adopt_k103_phase0.sh` — reference clone under `/tmp/k103-phase0-ccc/asm`; copy skills manually after `skill-scanner` review.

## Snippets

> "Registry resolution + batch skill ingestion for Cursor IDE environments." [Source: Tool Evaluation and Wiki Fit.docx URL 1; K103]
