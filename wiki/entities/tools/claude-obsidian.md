---
title: "claude-obsidian — markdown-vault autoresearch loop (DO NOT ADOPT — parallel-impl with claude-mem)"
type: entity
tags: [tool, claude-code, obsidian, markdown-vault, autoresearch, do-not-adopt, parallel-impl, dead-end, cross-wiki-stub]
keywords: [claude-obsidian, obsidian, markdown-vault, autoresearch, contradiction-flag, claude-mem-collision, sessionstart-hook]
related:
  - entities/tools/claude-mem.md
  - entities/patterns/autoresearch-loop.md
  - concepts/hooks-for-automation.md
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/obsidian-trading-journal-workflow.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/obsidian-vellum-second-brain-stack.md
maturity: draft
created: 2026-05-17
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/entities/tools/claude-obsidian.md"
---

## Relations

- @entities/tools/claude-mem.md — the adopted tool that claude-obsidian collides with; SessionStart-hook owner
- @entities/patterns/autoresearch-loop.md — the architectural pattern claude-obsidian implements (3-round autoresearch); the pattern is interesting even when this specific tool isn't
- @concepts/hooks-for-automation.md — hook-collision is the operational rejection reason, documented here
- @concepts/obsidian-agent-maintenance-workflow.md — K67 vault-hygiene pattern (do not install this tool to get it)
- @concepts/obsidian-trading-journal-workflow.md — K67 morning research + journal pattern (pattern-only)
- @osint-wiki/entities/tools/claude-obsidian.md — cross-wiki primary page; full Phase-0 audit table + Dead Ends lives there

## Raw Concept

CCC-side stub cross-routed from the OSINT primary. claude-obsidian is `github.com/AgriciDaniel/claude-obsidian` (MIT) — a Claude Code skill suite that wraps an Obsidian vault with `/autoresearch`, `/wiki`, `/save` slash commands. OSINT's Phase-0 audit verdict is **DO NOT ADOPT** for Cemini's laptop. This stub records the verdict and the load-bearing rejection reasons; full audit table is in the OSINT primary.

## Narrative

### Why catalogued here

The CCC-relevant slice is the operational lesson, not the tool. Three reasons CCC keeps a page on a NO-GO tool:

1. **Parallel-impl pattern is a recurring failure mode** — claude-obsidian was rejected because @entities/tools/claude-mem.md already owns the session-memory + observation-indexing surface. The shape of that rejection (overlapping problem domain + hook collision) is reusable.
2. **Hook-collision class** — claude-obsidian's `SessionStart` hook would collide with claude-mem v13.0.1's. Future adoption decisions face the same question; this page is the case study.
3. **`[!contradiction]` syntax conflict** — claude-obsidian uses `[!contradiction]` for cross-document contradictions. CCC uses `[NEEDS VERIFICATION YYYY-MM-DD]` (see @CLAUDE.md). Adopting claude-obsidian would force a 200+ file migration across the federation.

### Rejection summary (full table in OSINT)

| Question | Verdict |
|----------|---------|
| License | MIT — verified |
| Vault scope | Obsidian-Desktop-required; does not work on plain markdown trees |
| 3-round autoresearch cost | Unbounded per query; no cost cap |
| `[!contradiction]` syntax | **Conflicts** with `[NEEDS VERIFICATION]` |
| SessionStart hook | **Collides** with claude-mem v13.0.1 |

### What CCC steals from the page (not the tool)

- **The autoresearch loop pattern** — captured in @entities/patterns/autoresearch-loop.md.
- **The hook-collision check** as a Phase-0 audit step for any tool that registers `SessionStart` / `Stop` / `UserPromptSubmit`.

## Dead Ends

- **Adopting alongside claude-mem** — non-trivial. The SessionStart-hook surface is single-owner in practice; coexistence would require building a hook-routing layer that's out of scope for laptop-only operation. Recorded in the OSINT primary's Dead Ends section.

## Snippets

> Root cause of rejection: parallel-implementation with claude-mem v13.0.1 (already in production laptop-side as of K38, Phase-2 PASS 2026-05-12). The two tools target overlapping problem surfaces.
[Source: @osint-wiki/entities/tools/claude-obsidian.md]
