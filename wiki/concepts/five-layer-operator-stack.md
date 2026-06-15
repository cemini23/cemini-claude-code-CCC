---
title: Five-layer operator stack — Claude / Obsidian / Hermes / Kimi / Cursor
type: concept
tags: [concept, operator-stack, obsidian, claude-code, hermes, kimi, cursor, k78]
keywords: [damidefi, five-tool-stack, reasoning, memory, automation, long-horizon, execution]
related:
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/obsidian-contribution-rate-workflow.md
  - concepts/cursor-ide-workspace.md
  - entities/tools/claude-code.md
  - entities/tools/hermes-agent.md
  - entities/tools/kimi-agent-swarm.md
  - entities/people/damidefi.md
  - sources/trading-posts-compilation-6-2026-05-29.md
  - concepts/obsidian-vellum-second-brain-stack.md
  - concepts/claude-cowork-automation-vs-hooks.md
maturity: draft
created: 2026-05-30
updated: 2026-06-13
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md"
---

## Relations

- `@concepts/claude-obsidian-notebooklm-bridge.md` — Obsidian layer in Cemini's vault-thinking path (K69 + K78)
- `@concepts/obsidian-contribution-rate-workflow.md` — cyrilXBT vault metric paired with this stack map (K78 Post 6)
- `@concepts/cursor-ide-workspace.md` — Cursor 3 execution layer on the laptop
- `@entities/tools/claude-code.md` — reasoning + long-context harness (primary for hooks/skills/MCP)
- `@entities/tools/hermes-agent.md` — scheduled automation reference; prod uses conductor instead
- `@entities/tools/kimi-agent-swarm.md` — long-horizon / swarm coding reference (not prod adopt)
- `@entities/people/damidefi.md` — Post 4 author stub
- `@sources/trading-posts-compilation-6-2026-05-29.md` — provenance (K78 Post 4)

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md` (canon).

## Raw Concept

K78 Post 4 (@DamiDefi): a **five-layer operator stack** where each tool owns a non-overlapping capability — reasoning, durable memory, scheduled automation, long-horizon coding, and live codebase execution. CCC maps this to Cemini's existing harness choices rather than adopting every named product.

## Narrative

| Layer | Vendor framing | Cemini mapping | Posture |
|-------|----------------|----------------|---------|
| Reasoning | Claude (200K context) | `@entities/tools/claude-code.md` + Anthropic API | **Adopt** — primary harness |
| Memory | Obsidian vault | Git-backed markdown wikis + `@entities/tools/claude-mem.md` + `hot.md` | **Adopt pattern** — no `@entities/tools/claude-obsidian.md` plugin |
| Automation | Hermes scheduled agents | Hermes on **librarian** (cron + Telegram) + `@entities/tools/conductor-mcp.md` on prod | **Adopt (operator)** — Hermes not prod trading |
| Long-horizon coding | Kimi K2.6 / Agent Swarm | `@entities/tools/kimi-agent-swarm.md` external UI only | **Reference** — no Moonshot MCP |
| Execution | Cursor 3 (Agents Window, cloud handoff) | `@concepts/cursor-ide-workspace.md` | **Adopt** — primary IDE |

**Key claim:** five distinct capabilities, none redundant **`[TENTATIVE]`** — useful as a **role-separation checklist** when adding tools (avoid two memory owners, two orchestrators).

### CCC guardrails

1. **Do not stack parallel memory systems** — claude-mem + Obsidian graph + Hermes `MEMORY.md` without boundaries → pick owners per layer.
2. **Hermes ≠ conductor** — Hermes owns operator cron/phone on librarian; conductor owns prod MCP. Cursor + Claude Code own wiki ingest — not Hermes.
3. **Kimi for batch research only** — not a substitute for Claude Code Agent Teams on repo edits.

## Snippets

> "Five layers. Five distinct capabilities. None of them redundant."
> — [Source: Posts.docx K78 Post 4, @DamiDefi; @osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md]
