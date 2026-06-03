---
title: Claude Code cheat sheet — hidden shortcuts and command surface (K97)
type: concept
tags: [concept, claude-code, shortcuts, k97]
keywords: [0x-rody, shift-tab, escape, ctrl-s, cheat-sheet, cli-flags]
related:
  - entities/tools/claude-code.md
  - entities/tools/claude-code-tips.md
  - concepts/context-engineering.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
---

## Relations

- `@entities/tools/claude-code.md` — host harness; this page is operator-facing surface map
- `@entities/tools/claude-code-tips.md` — community tips repo (license-blocked); fold validated ideas here
- `@concepts/context-engineering.md` — mode switches affect context budget
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 2 (@0x_rody)

## Raw Concept

K97 Post 2 (@0x_rody): Claude Code exposes **70+ commands, 12 keyboard shortcuts, and 30+ CLI flags** — most operators use ~5. CCC catalogs the **load-bearing shortcuts** called out in the post plus pointers to official docs for the full surface.

## Narrative

### High-signal shortcuts [TENTATIVE — post summary, verify on installed build]

| Input | Effect | CCC use |
|-------|--------|---------|
| **Shift+Tab** | Cycle plan / auto-accept / normal modes | Plan-first for multi-file refactors; auto-accept only on scoped tasks |
| **Escape ×2** | Rewind / undo last agent turn | Recovery after bad edit without restarting session |
| **Ctrl+S** | Stash draft prompt | Compose long `/goal` envelopes before send; pairs with `@concepts/context-engineering.md` |

### Command surface discipline

- Prefer **slash commands + skills** over re-typing harness instructions each turn (`@entities/patterns/full-prompt-goal-template.md`).
- **CLI flags** (`--model`, `--resume`, permission modes) belong in project docs or `CLAUDE.md` — not chat.
- Cherry-pick from `@entities/tools/claude-code-tips.md` only after manual LICENSE review.

**Verdict:** **REFERENCE** — no new install; refresh operator cheat sheet when Anthropic ships keyboard changes `[NEEDS VERIFICATION 2026-06-03]`.

## Snippets

> "Claude Code has 70+ commands, 12 keyboard shortcuts, and 30+ CLI flags. Most people use about 5 of them."
> — [Source: Posts.docx K97 Post 2, @0x_rody; @osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md]
