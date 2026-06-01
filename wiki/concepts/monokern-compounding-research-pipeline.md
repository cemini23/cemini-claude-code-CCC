---
title: Monokern compounding research pipeline — weekly deep-research overlay
type: concept
tags: [concept, workflow, notebooklm, obsidian, k93]
keywords: [monokern, notebooklm, compounding, weekly-pipeline]
related:
  - concepts/federated-daily-research-digest.md
  - entities/tools/notebooklm-py.md
  - concepts/obsidian-vellum-second-brain-stack.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - meta/daily-research-digest-cadence.md
  - concepts/autosci-memory-centric-research-agents.md
  - sources/arxiv-autosci-2605.31468.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/concepts/monokern-compounding-research-pipeline.md"
---

## Relations

- `@concepts/federated-daily-research-digest.md` — daily Exa/inbox layer
- `@entities/tools/notebooklm-py.md` — NotebookLM SDK (K69)
- `@concepts/obsidian-vellum-second-brain-stack.md` — vault memory patterns
- `@sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md` — OSINT source
- `@osint-wiki/concepts/monokern-compounding-research-pipeline.md` — canon

## Raw Concept

K93 operator request: weekly **Monokern-style** pipeline on one ROADMAP harness topic — harvest sources → NotebookLM → markdown into wiki/Obsidian. Config: `scripts/daily_research_config.yaml` → `monokern_pipeline`.

## Narrative

| Cadence | CCC behavior |
|---------|----------------|
| Daily | `scripts/daily_research_digest_run.py` → `wiki/sweeps/YYYY-MM-DD-daily.md` |
| Weekly | One Monokern session on `monokern_pipeline.active_topic` |
| Ingest | Human-gated wiki writes (no Tier-3 auto-ingest) |

**Verdict:** **REFERENCE** — enabled in CCC config 2026-06-01; laptop-only NotebookLM auth.

## Snippets

> "Obsidian is what turns it into something that compounds." — Monokern source.
> — [Source: @osint-wiki/sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md]
