---
title: CodexBar — macOS menu-bar API-usage tracker
type: entity
tags: [tool, telemetry, token-economics, claude-code, codex, macos, menu-bar, swift, mit, adopt]
keywords: [codexbar, steipete, menu bar, macos, api usage, daily limit, weekly limit, desktop notifications, swift, claude code, openai codex, budget overrun]
related:
  - concepts/token-economics-and-prompt-caching.md
  - entities/openusage.md
  - entities/tools/ai-token-monitor.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
---

# CodexBar — macOS menu-bar API-usage tracker

## Relations

- `@concepts/token-economics-and-prompt-caching.md` — the cost-discipline concept CodexBar enforces by surfacing live spend + limit-tracking against budget policy
- `@entities/openusage.md` — sibling local token-telemetry tool (Go daemon + dashboard); CodexBar is the glanceable menu-bar form of the same job
- `@entities/tools/ai-token-monitor.md` — sibling cross-platform desktop token monitor; ai-token-monitor is the full-app cross-platform version, CodexBar is the lightweight macOS-native one
- `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` — cross-wiki tool-eval source

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17 (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). The eval flagged CodexBar as a CCC-primary-fit tool: a lightweight instrument for enforcing token-economic policy and preventing budget overruns.

Repo: `github.com/steipete/CodexBar` · License: MIT · Stack: Swift · Tier: **Adopt** (CCC primary fit).

## Narrative

CodexBar is a lightweight macOS **menu-bar app** that shows live API usage statistics for **Claude Code** and **OpenAI Codex**. It tracks daily and weekly limit consumption and fires **desktop notifications** as those limits are approached — making it the alerting layer for token-economic policy rather than just a passive dashboard.

Written in Swift as a native macOS menu-bar utility, it occupies the lightest-touch slot of the token-telemetry tool class: always glanceable in the menu bar, no window to manage, no daemon to configure.

### Fit for CCC

CCC's token-economics mandate (`@concepts/token-economics-and-prompt-caching.md`) currently *reasons about* cost — 5-minute cache TTL, `ScheduleWakeup` pacing, MCP catalog overhead — but does not *enforce* it. CodexBar adds the missing enforcement primitive: a **notification trigger** when daily/weekly usage trends toward an overrun. That converts a documented rule of thumb into an active guardrail.

Of the three candidate token instruments, CodexBar is the **most operator-friendly for a single macOS laptop**:

| Tool | Form | Best when |
|------|------|-----------|
| CodexBar | macOS menu-bar app + notifications | Single-laptop macOS operator wants glanceable spend + overrun alerts |
| `@entities/openusage.md` | Go daemon + themed dashboard | Zero-config passive multi-environment logging |
| `@entities/tools/ai-token-monitor.md` | Cross-platform Tauri app | Non-macOS machines or a dedicated dashboard window |

CodexBar's differentiator over `openusage` is the **active limit-tracking + notification** behavior — `openusage` records, CodexBar warns. Its constraint is macOS-only; `ai-token-monitor` is the cross-platform fallback if the workflow leaves macOS.

### Adoption posture

MIT license — no IP-sale or redistribution constraint; the eval cleared it as Adopt. Phase-0 audit (clone + license verify via `gh api` + maintainer/maturity signals) still pending before operational install — see `@concepts/skill-vetting.md` Phase-0 pattern.

## Snippets

> Tier: Adopt — CCC primary fit. Lightweight macOS menu-bar app showing live API usage stats, daily/weekly limit tracking, and desktop notifications for Claude Code and OpenAI Codex — for enforcing token-economic policy / preventing budget overruns. MIT.
[Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
