---
title: ai-token-monitor — cross-platform desktop token-usage monitor
type: entity
tags: [tool, telemetry, token-economics, claude-code, codex, desktop-app, tauri, mit, adopt]
keywords: [ai-token-monitor, soulduse, token usage, telemetry, tauri, typescript, rust, offline, leaderboard, claude code, openai codex, context economics]
related:
  - concepts/token-economics-and-prompt-caching.md
  - entities/openusage.md
  - entities/tools/codexbar.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/deepseek-coding-cost-routing.md
maturity: draft
created: 2026-05-17
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
---

# ai-token-monitor — cross-platform desktop token-usage monitor

## Relations

- `@concepts/token-economics-and-prompt-caching.md` — the cost-discipline concept ai-token-monitor instruments by tracking per-environment token spend over time
- `@entities/openusage.md` — sibling local token-telemetry tool (Go daemon + dashboard); ai-token-monitor is the desktop-app form of the same job
- `@entities/tools/codexbar.md` — sibling menu-bar token tracker; CodexBar is the lightweight macOS-only counterpart, ai-token-monitor is the cross-platform full-app version
- `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` — cross-wiki tool-eval source

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17 (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). The eval flagged ai-token-monitor as a CCC-primary-fit tool: telemetry for managing context + token economics across the laptop-side developer fleet.

Repo: `github.com/soulduse/ai-token-monitor` · License: MIT · Stack: TypeScript front-end + Rust (Tauri) shell · Tier: **Adopt** (CCC primary fit).

## Narrative

ai-token-monitor is a cross-platform desktop application that continuously monitors local API token usage for **Claude Code** and **OpenAI Codex**. It runs as a standalone Tauri app (TypeScript UI in a Rust-backed native shell) rather than a CLI or background daemon, so it gives an always-visible window onto consumption rather than a queryable log.

The operation is **fully offline except for an opt-in leaderboard feature** — by default no usage data leaves the machine. The leaderboard is a community comparison surface that the user explicitly enables; with it off, ai-token-monitor is a purely local instrument.

### Fit for CCC

CCC's mandate includes context + token economics (`@concepts/token-economics-and-prompt-caching.md`) — the discipline of keeping the 5-minute prompt-cache warm, pacing `ScheduleWakeup` delays, and not burning input tokens on MCP catalog bloat. That discipline is currently *reasoned about* but not *measured*. ai-token-monitor is one of three candidate instruments for closing that gap:

| Tool | Form | Scope | Notes |
|------|------|-------|-------|
| `@entities/openusage.md` | Go background daemon + themed dashboard | Multi-environment, intercepts API-key env vars | Zero-config, passive |
| `@entities/tools/codexbar.md` | macOS menu-bar app | Live stats, daily/weekly limit tracking, notifications | Lightweight, glanceable |
| ai-token-monitor | Cross-platform Tauri desktop app | Claude Code + Codex, offline + opt-in leaderboard | Full-window app; cross-platform reach |

ai-token-monitor's differentiator is **cross-platform reach** (not macOS-only like CodexBar) and a **full application surface** (richer than a menu-bar widget, more visible than a daemon). For a single-laptop operator the menu-bar form (CodexBar) is usually lighter-touch; ai-token-monitor earns its slot if the workflow ever spans non-macOS machines or wants a dedicated dashboard window.

### Adoption posture

MIT license — no IP-sale or redistribution constraint; the eval cleared it as Adopt. Phase-0 audit (clone + license verify via `gh api` + maturity signals) still pending before operational install — see `@concepts/skill-vetting.md` Phase-0 pattern. The opt-in leaderboard is the one item to confirm stays off by default in a Phase-0 pass.

## Snippets

> Tier: Adopt — CCC primary fit. Cross-platform desktop app, continuously monitors local API token usage for Claude Code and Codex; fully offline except opt-in leaderboards. Telemetry for managing context + token economics across the laptop-side developer fleet. MIT.
[Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
