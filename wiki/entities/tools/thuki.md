---
title: "thuki — quiet-node/thuki Tauri+Rust macOS Ollama overlay (NOT a Claude Code persistence tool)"
type: entity
category: tool
tags: [entity, tool, tauri-app, rust, sqlite, ollama, local-first, macos-desktop, k44, skip-phase-0-2026-05-14, k44-purpose-misstated, single-author-74-percent]
keywords: [thuki, quiet-node-thuki, tauri-v2, rust-backend, react-19, sqlite-conversation-history, ollama-local-inference, NOT-claude-code-state, apache-2-license, no-notice-file]
related:
  - entities/tools/claude-mem.md
  - concepts/local-llm-mechanics-primer.md
  - concepts/obsidian-agent-maintenance-workflow.md
maturity: validated
created: 2026-05-14
updated: 2026-05-26
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @entities/tools/claude-mem.md — K44 mis-framed thuki as a CC persistence layer; claude-mem is the genuine local-memory tool that contrast clarifies
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Rust+Tauri v2 macOS desktop overlay app with React 19 frontend, local SQLite for **conversation history**, Ollama local inference, Bun build. Vietnamese name *thư kí* ("secretary"). **Apache-2.0, 486 stars verified (claim 485), repo `quiet-node/thuki` (NOT `thukilabs/thuki` as K44 implied), 74% single-author (Logan Nguyen), 7 weeks old**. K44 doc-level eval is **materially wrong about purpose** — see verdict.

## Narrative

### Phase-0 audit verdict (2026-05-14): SKIP

**Critical correction (G9): K44 mis-stated thuki's purpose.** thuki is **NOT a Claude Code agent persistence layer**. It is a macOS Tauri 2 + React 19 + Rust desktop overlay that runs Ollama locally for an on-screen "AI secretary" experience. SQLite is used internally for *conversation history* of the Ollama overlay, not for Claude Code state management. The repo contains its own local `CLAUDE.md` (its contributor guide), which likely triggered the K44 doc-eval misread.

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo resolves | **CONDITIONAL** | `thukilabs/thuki` does NOT exist; correct slug is `quiet-node/thuki`. K44 cited wrong org |
| G1 | License = Apache-2.0 | **PASS** | Apache-2.0 verbatim |
| G2 | NOTICE file (Apache-2.0 §4.4) | **FAIL** | **No NOTICE file** — if any code were lifted, Cemini IP-sale buyer would need a generated NOTICE entry |
| G3 | Stars match claim | **PASS** | 486 verified (claim 485) — minor drift |
| G4 | Maturity (≥3mo + active) | **FAIL** | Only ~7 weeks old (created 2026-03-20); tagged v0.9.x WIP/beta |
| G5 | Bus factor (<70% one author) | **FLAG** | 74% single-author (Logan Nguyen: 134/180 commits) |
| G6 | Not abandoned-after-pump | **PASS** | Active commits (last 2026-05-13) |
| G7 | SQLite backend real | **PASS** | `rusqlite 0.39 bundled`, WAL mode, FK ON, `~/.thuki/thuki.db` confirmed |
| G8 | Stack compat with Cemini (Python/Postgres) | **FAIL** | Rust/TS/Tauri/macOS native; no runtime portability |
| G9 | "Claude Code state management" claim | **FAIL — UNSUPPORTED** | **Demonstrably false.** SQLite stores Ollama-overlay conversation history; no Claude Code integration exists in the repo |

**Verdict: SKIP.** K44 doc-level claim is materially wrong about thuki's purpose. There is no extraction target relevant to Cemini's stack.

### Why SKIP (not Steal-from)

1. **K44 claim "Claude Code persistence" is false** — thuki is a desktop Ollama overlay, not a Claude Code companion
2. **Cemini uses Postgres, not SQLite** — downgrading to SQLite for "local-first" is a step backward
3. **Generic SQLite patterns** (`PRAGMA table_info` migrations, WAL mode, FK ON) are already covered by Alembic + standard SQLite idioms; thuki adds nothing novel
4. **No NOTICE file** + 7-week age + 74% single-author = poor extraction-source signals

### Ranked extractable patterns (negligible value)

If any extraction is attempted, the only patterns of even marginal interest:

1. **`ensure_column()` idempotent additive migrations** (`database.rs:152-189`) — `PRAGMA table_info` → conditional `ALTER TABLE ADD COLUMN`. **Low value**; Alembic+autogenerate already covers this for Cemini's Postgres stack.
2. **WAL + FK-ON + bundled-driver init** (`open_database`) — three-line idempotent open. **Negligible value**; trivially reproducible.
3. **Legacy-path one-time migration shim** (`migrate_legacy_db`) — moves DB file on first launch. Not Cemini-relevant.

### Lessons recorded

This audit confirms the **two-gate evaluation pattern** (doc-level vs Phase-0). K44's doc-level "Steal-from" verdict was based on a paragraph that mis-read thuki's purpose. Without Phase-0 source verification, Cemini would have spent engineering time porting "Claude Code persistence patterns" from a tool that has no such patterns. **K44 doc-level claims must be source-verified before any extraction budget is spent.**

## Snippets

> "Thuki operates as a context-aware floating AI secretary, leveraging a Rust backend and localized SQLite databases to maintain continuous conversation history alongside local Ollama inference."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶97 — Phase-0 audit confirms the Ollama-overlay framing but flags the K44 "Claude Code state" framing as unsupported by source.]
