---
title: "red-run — Claude Code agent-team orchestrator for distributed terminal pentest ops (Sliver C2)"
type: entity
category: tool
tags: [entity, tool, claude-code-agent-teams, tmux-orchestration, sliver-c2, sqlite-state, chromadb-rag, k44, steal-from-gpl-poison]
keywords: [red-run, blacklanternsecurity, agent-team-coordination, tmux-pane-routing, sliver-c2-backend, ctf-orchestrator, gpl-3-poison-pill]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python+Shell agent-team orchestrator that coordinates Claude Code operators across separate tmux panes via slash-commands like `/red-run-ctf`. Uses SQLite for state, ChromaDB for RAG-based skill retrieval, and Sliver C2 backend. **GPL-3.0, 160 stars**. K44 verdict: **Steal-from** (architectural patterns only). Primary fit: CCC. Cross-route: Cybersec-wiki (autonomous pentest agents).

## Narrative

The architectural value for CCC is the **subagent-orchestration-via-tmux pattern** — distinct from the existing conductor/librarian model in that it explicitly partitions the screen real estate to different agents simultaneously.

**License posture**: GPL-3.0 is an **absolute poison pill** for the impending Cemini IP sale. Static or dynamic linkage into the shipped Cemini suite triggers copyleft propagation. Strict laptop-side-only usage required. The architectural patterns (tmux routing, SQLite state, ChromaDB skill RAG) are concepts, not GPL'd artifacts — those can be re-implemented under MIT.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/blacklanternsecurity/red-run`)
- G2: License (GPL-3.0 confirmed, treat as poison-pill, never linked)
- G3: Persistent shell-server (SSE service on 127.0.0.1:8022, K44 NEEDS VERIFICATION) — audit reverse-shell mechanism for safe re-implementation pattern
- G4: ChromaDB skill RAG schema — can re-implement under MIT vector store

**Cross-route to Cybersec**: provides operational concept blueprint for "autonomous pentest agents coordinating via shared C2." Useful as cybersec-wiki reference; not deployed.

## Snippets

> "This repository offers a masterclass in subagent orchestration, utilizing Claude Code agent teams to coordinate operators across distinct tmux panes via orchestrator variants such as /red-run-ctf. The architecture relies on SQLite for state tracking and ChromaDB for RAG-based semantic skill retrieval."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶37]
