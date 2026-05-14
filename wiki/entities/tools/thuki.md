---
title: "thuki — Rust+Tauri macOS overlay AI secretary with local-first SQLite + Ollama"
type: entity
category: tool
tags: [entity, tool, tauri-app, rust, sqlite, ollama, local-first, on-screen-context, k44, steal-from-doc-level-pending-phase-0]
keywords: [thuki, tauri-v2, rust-backend, react-19, sqlite-state, ollama-inference, local-first-storage, context-aware-overlay, apache-2-license]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Rust+Tauri v2 macOS overlay app with React 19 frontend, local SQLite state, Ollama local inference, Bun build. Functions as a context-aware AI secretary capturing on-screen context and surfacing contextual hints. **Apache-2.0, claimed 485 stars, v0.9.1 release**. K44 verdict: **Steal-from** — extract SQLite state-management patterns; do not adopt the Tauri overlay runtime (out-of-scope for Cemini).

## Narrative

**Steal-from rationale**: Cemini doesn't ship a desktop overlay; the value here is the SQLite local-first state-management pattern (continuous conversation history, conversation-context indexing) which translates to CCC-wiki's local-first knowledge-storage initiative.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/quiet-node/thuki`)
- G2: License (Apache-2.0 confirmed)
- G3: Read SQLite schema + state-management module; confirm it's portable to a non-Tauri context
- G4: Docker sandbox mechanism (K44 NEEDS VERIFICATION) — irrelevant for extraction but a maturity signal

**Extraction target**: the SQLite + conversation-context indexing module only. Strict isolation from Tauri/React frontend.

## Snippets

> "Thuki operates as a context-aware floating AI secretary, leveraging a Rust backend and localized SQLite databases to maintain continuous conversation history alongside local Ollama inference."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶97]
