---
title: Federated daily research digest — CCC automated discovery loop
type: concept
tags: [concept, meta, automation, federation, k93]
keywords: [federated-digest, daily-research, exa, inbox, launchagent]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/cross-wiki-routing.md
  - entities/tools/exa-mcp.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - concepts/autosci-memory-centric-research-agents.md
  - sources/arxiv-system-scaling-harness-2605.26112.md
  - sources/arxiv-autosci-2605.31468.md
  - sweeps/2026-06-01-daily.md
  - sweeps/2026-06-02-daily.md
  - concepts/adaptive-auto-harness-open-ended-streams.md
  - sweeps/2026-06-03-daily.md
  - concepts/interaction-native-knowledge-harness.md
maturity: core
created: 2026-06-01
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/concepts/federated-daily-research-digest.md"
---

## Relations

- `@meta/daily-research-digest-cadence.md` — CCC-local cadence stub
- `@concepts/monokern-compounding-research-pipeline.md` — weekly overlay
- `@concepts/cross-wiki-routing.md` — federation read paths
- `@entities/tools/exa-mcp.md` — external research MCP
- `@osint-wiki/concepts/federated-daily-research-digest.md` — OSINT canon

## Raw Concept

K93 structural install: replicate OSINT morning digest on **ccc-wiki** repo — Exa/news fetch → `research to be indexed/` → `wiki/sweeps/` report; Cursor session does full ingest with human gates.

## Narrative

| Piece | CCC path |
|-------|----------|
| Config | `scripts/daily_research_config.yaml` |
| Runner | `scripts/daily_research_digest_run.py` |
| Wrapper | `~/bin/cemini-daily-research-digest-ccc` |
| LaunchAgent | `com.cemini.daily-research-digest.ccc` @ 08:15 |
| Install | `OSINT WORKSPACE/scripts/federation/daily_digest/install_federated_daily_digest.sh` |

**Tier-3 auto-ingest remains NO-GO** — digest discovers; operator ingests.

## Snippets

> Installed 2026-06-01 via K93 brief `2026-06-01_k93-ccc-digest-monokern-harness-from-osint.md`.
