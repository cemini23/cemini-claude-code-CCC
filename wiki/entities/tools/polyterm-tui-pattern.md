---
title: "PolyTerm — terminal-native UI-design reference for Claude Code tools"
type: entity
tags: [entity, tool, pattern, tui-design, terminal-native, ascii-visualization, cross-wiki-stub, cross-wiki-route-2026-05-16]
keywords: [polyterm, terminal-ui, ascii-depth-chart, tui-keyboard-shortcuts, c15-mw-shortcuts, terminal-native-claude-code-tools, mit-license, nytemodeonly]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/entities/tools/polyterm.md"
---

## Relations

- @entities/tools/claude-code.md — Claude Code is itself a terminal-native tool; PolyTerm is a UI-design reference for any TUI built alongside it
- @concepts/context-engineering.md — ASCII/text-native rendering keeps visualizations inside the model's text window; relevant to terminal-tool output design
- @osint-wiki/entities/tools/polyterm.md — cross-wiki primary page (full tool write-up + audit lives in OSINT)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. PolyTerm is terminal-native Polymarket analytics (MIT, https://github.com/NYTEMODEONLY/polyterm). The CCC-relevant slice is its TUI design, not its market analytics. Primary page: `@osint-wiki/entities/tools/polyterm.md` — the prediction-market detail belongs in OSINT; this stub documents only the UI-design reference.

## Narrative

**Pattern: terminal-native UI design reference for building Claude Code-adjacent TUI tools.**

PolyTerm renders market data as ASCII depth-chart visualizations and navigates via TUI keyboard shortcuts (e.g. `c15`, `mw`). Two reusable lessons for CCC:

1. **ASCII / text-native visualization** — depth charts rendered as plain text rather than as images or a GUI. Any tool a Cemini Claude Code session interacts with benefits from text-native output: it round-trips cleanly through the model's context window, is greppable, and needs no rendering surface. PolyTerm is a concrete reference for what a good text-native chart looks like.

2. **Compact keyboard-navigation shortcuts** — short, mnemonic chords (`c15`, `mw`) for fast TUI navigation. A reference for ergonomics when CCC builds or evaluates terminal-native tooling.

PolyTerm is **not** a tool CCC adopts — the analytics payload is OSINT's. It is catalogued here purely as a UI-design reference for the "terminal-native Claude Code tool" class. Full tool detail and any Phase-0 verdict are in the OSINT primary page.

## Snippets

> PolyTerm's ASCII depth-chart visualizations and TUI keyboard-navigation shortcuts (`c15`, `mw`) are a UI-design reference for building terminal-native Claude Code tools.
[Source: @osint-wiki/entities/tools/polyterm.md]
