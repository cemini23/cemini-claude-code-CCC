---
title: Claude Cowork day automation vs Claude Code hooks (K97)
type: concept
tags: [concept, claude-cowork, hooks, automation, k97]
keywords: [eng-khairallah1, cowork, hooks, full-day-automation]
related:
  - concepts/hooks-for-automation.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/claude-code.md
  - concepts/five-layer-operator-stack.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
---

## Relations

- `@concepts/hooks-for-automation.md` — Cemini's automation surface on Claude Code
- `@concepts/claude-desktop-vs-claude-code.md` — Cowork lives on Desktop/web; hooks on Code
- `@entities/tools/claude-code.md` — primary Cemini harness
- `@concepts/five-layer-operator-stack.md` — multi-tool day stack context
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 13 (@eng_khairallah1)

## Raw Concept

K97 Post 13 (@eng_khairallah1): **Claude Cowork** "full-day automation course" — consumer-facing workflow for chaining Desktop/Cowork tasks across a workday. CCC compares to **Claude Code hooks + slash commands** rather than adopting Cowork as prod harness.

## Narrative

| Cowork pattern (post) | Cemini analog |
|----------------------|---------------|
| Scheduled morning research brief | `@concepts/federated-daily-research-digest.md` + LaunchAgent |
| Recurring status summaries | `/loop` or `/schedule` + `@entities/tools/claude-mem.md` |
| Handoff between task types | Subagent dispatch (`@concepts/subagent-orchestration.md`) |
| Persistent project context | `CLAUDE.md`, `.cursor/rules/`, wiki ingest |
| GUI-first automation | Claude Desktop MCP — **secondary** to CLI harness |

### Posture

- **Do not** duplicate Cowork flows on Desktop if Claude Code hooks already cover the same trigger.
- **Steal-from:** day-structure templates (morning triage → deep work → ingest) for briefs, not product dependency.
- Cowork course content is `[TENTATIVE]` — verify feature names against current Anthropic Cowork docs `[NEEDS VERIFICATION 2026-06-03]`.

**Verdict:** **REFERENCE** — workflow vocabulary only; Cemini prod stays Claude Code + Cursor.

## Snippets

> Claude Cowork full-day automation course — compare vs Claude Code hooks. [TENTATIVE — @eng_khairallah1, Posts.docx K97 Post 13]
