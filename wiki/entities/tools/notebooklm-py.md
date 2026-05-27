---
title: notebooklm-py — reverse-engineered NotebookLM SDK + CLI
type: entity
tags: [tool, notebooklm, google, cli, cross-wiki-route, k69]
keywords: [notebooklm-py, notebooklm, audio-overview, agents-skill-dir]
related:
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-20-2026-05-27.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @concepts/claude-obsidian-notebooklm-bridge.md — K69 Post 18 workflow
- @concepts/cross-wiki-tool-eval-inventory.md — K68 row (MIT, Adopt catalog)
- @entities/tools/claude-code.md — harness that would invoke CLI/skill
- @sources/trading-posts-compilation-20-2026-05-27.md — Post 18 (@DamiDefi)

## Raw Concept

K69 Post 18 + K68 tool-eval inventory: **notebooklm-py** — MIT, ~13.7k★ claimed [TENTATIVE], reverse-engineered NotebookLM API with CLI and `.agents` skill directory. **Adopt-eligible** for doc/audio synthesis workflows; **not** Cemini prod core.

## Narrative

### Phase-0 posture [TENTATIVE — pending deep audit]

| Check | Status |
|-------|--------|
| License | MIT per inventory row |
| Data boundary | Google NotebookLM — **no prod secrets** in uploads |
| Overlap | Distinct from librarian RAG — consumer podcast/Q&A use case |
| CCC fit | Optional bridge from Obsidian exports / briefs → audio review |

### Guardrails

- Redact credentials, SSH configs, `.env` before any NotebookLM upload.
- Treat as **operator convenience**, not federation layer.

## Snippets

> Reverse-engineered NotebookLM SDK; ships `.agents` skill dir. [Source: @concepts/cross-wiki-tool-eval-inventory.md K68 row]
