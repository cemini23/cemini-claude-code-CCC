---
title: Obsidian trading journal workflow — morning research + thesis log
type: concept
tags: [concept, obsidian, trading, claude-code, discretionary, k67]
keywords: [trading-journal, morning-agent, watchlist, thesis, post-mortem, cyrilXBT]
related:
  - concepts/obsidian-agent-maintenance-workflow.md
  - entities/tools/conductor-mcp.md
  - concepts/cross-wiki-routing.md
  - entities/tools/claude-obsidian.md
  - entities/mcp-servers/stash.md
  - concepts/claude-code-personal-os-scope.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/claude-code-finance-research-setup.md
  - concepts/obsidian-vellum-second-brain-stack.md
maturity: draft
created: 2026-05-26
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
---

## Relations

- `@concepts/obsidian-agent-maintenance-workflow.md` — vault structure/hygiene complements journal templates
- `@entities/tools/conductor-mcp.md` — morning **brief** pattern may route through conductor, not vault-only
- `@concepts/cross-wiki-routing.md` — macro/discretionary curriculum lives on `@osint-wiki`
- `@entities/tools/claude-obsidian.md` — rejected tool; journal workflow is pattern-only
- `@entities/mcp-servers/stash.md` — episodic trade hypotheses vs Obsidian long-form narrative

Cross-wiki: `@osint-wiki/concepts/koroushak-discretionary-trading-curriculum.md`; K67 Posts 20, 30 (@cyrilXBT).

## Raw Concept

K67 — Obsidian as **system of record** for discretionary trading: scheduled morning research pass (news, macro, watchlist) → structured vault notes; separate templates for thesis, entries, post-mortems. **No Polymarket execution** detail in CCC scope.

## Narrative

### Two-agent split [TENTATIVE]

| Agent | Output |
|-------|--------|
| **Morning research** | Daily brief note (macro, catalysts, watchlist deltas) |
| **Journal** | Per-trade thesis, sizing rationale, post-mortem |

### CCC / Cemini boundaries

- **CCC:** document harness patterns (`/goal`, scheduled wakeup, episodic capture) — not alpha claims.
- **OSINT:** discretionary curriculum + market content.
- **Prod:** execution stays on CeminiSuite stack; vault is operator laptop optional layer.

### Optional wiring

- Hook or cron → Claude morning pass → markdown drop folder → Obsidian sync.
- Link completed briefs to `@entities/mcp-servers/stash.md` for **hypothesis** tracking without duplicating full journal text.

## Snippets

> "Morning agent: scheduled Claude research pass with structured output into vault — pattern for conductor morning brief hook, not trading alpha."
> — [Source: briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md, Post 20]
