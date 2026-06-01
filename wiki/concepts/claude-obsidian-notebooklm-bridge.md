---
title: Claude + Obsidian vault thinking — NotebookLM CLI bridge
type: concept
tags: [concept, obsidian, claude-code, notebooklm, k69]
keywords: [damidefi, obsidian-vault, notebooklm-cli, second-brain, thinking-partner]
related:
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/obsidian-trading-journal-workflow.md
  - concepts/five-layer-operator-stack.md
  - concepts/obsidian-contribution-rate-workflow.md
  - entities/tools/claude-obsidian.md
  - entities/tools/notebooklm-py.md
  - entities/tools/claude-code.md
  - entities/tools/claude-mem.md
  - entities/people/damidefi.md
  - concepts/cross-wiki-routing.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - sources/trading-posts-compilation-6-2026-05-29.md
  - concepts/obsidian-vellum-second-brain-stack.md
  - concepts/monokern-compounding-research-pipeline.md
maturity: validated
created: 2026-05-27
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @concepts/obsidian-agent-maintenance-workflow.md — vault **hygiene** vs this page's **thinking partner** use
- @concepts/obsidian-trading-journal-workflow.md — journal capture pattern (K67)
- @entities/tools/claude-obsidian.md — **DO NOT ADOPT** plugin; steal workflow ideas only
- @entities/tools/notebooklm-py.md — Post 18 CLI bridge to NotebookLM
- @entities/tools/claude-code.md — primary harness for vault-adjacent automation
- @entities/tools/claude-mem.md — session memory; not a substitute for Obsidian graph
- @sources/trading-posts-compilation-20-2026-05-27.md — Posts 17–18 (@DamiDefi)
- @concepts/five-layer-operator-stack.md — K78 Post 4 five-tool stack (Obsidian layer)
- @concepts/obsidian-contribution-rate-workflow.md — K78 Post 6 output-oriented vault flows
- @entities/people/damidefi.md — author stub
- @sources/trading-posts-compilation-6-2026-05-29.md — K78 provenance

Cross-wiki: SEO wiki ingested Post 16 offline Obsidian stack separately (`@seo-wiki/concepts/obsidian-integration.md`).

## Raw Concept

K69 Posts 17–18 (@DamiDefi): use **Claude Code + Obsidian vault** as a thinking surface (linked notes, MOCs, iterative elaboration), plus **NotebookLM CLI** (`notebooklm-py`) to round-trip audio/podcast-style synthesis from vault exports.

## Narrative

### Post 17 — Vault thinking partner [TENTATIVE]

- Claude reads/writes markdown in git-backed Obsidian vault.
- Emphasis on **iterative note refinement** and cross-links — not full autonomous vault rewrite.
- **CCC guardrail:** same as K67 — no `@entities/tools/claude-obsidian.md` install (SessionStart collision with claude-mem).

### Post 18 — NotebookLM CLI bridge [CONFIRMED 2026-05-27]

- Export/select vault corpus → NotebookLM via `@entities/tools/notebooklm-py.md` for audio overview / Q&A surface.
- **Wired (laptop):** `notebooklm-py` 0.5.0, auth ok, skills installed (`notebooklm` + OSINT `notebooklm-osint-bridge`).
- **Separation:** NotebookLM is Google-hosted; do not treat as private infra — redact secrets before export (see OSINT bridge skill).

### Stack mapping

| Need | CCC tool | Avoid |
|------|----------|--------|
| Vault edits | Claude Code + git | claude-obsidian plugin |
| Cross-wiki facts | conductor + librarian | Re-indexing vault into kb-server |
| Session continuity | claude-mem + hot.md | Hermes 24/7 gateway |
| Audio synthesis | notebooklm-py (optional) | Pushing prod secrets into NotebookLM |

## Snippets

> Claude + Obsidian vault thinking; Claude Code → NotebookLM CLI. [TENTATIVE — @DamiDefi, Posts.docx K69 Posts 17–18]
