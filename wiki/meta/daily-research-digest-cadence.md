---
title: Daily research digest cadence (CCC)
type: concept
tags: [meta, automation, k93]
keywords: [daily-digest, sweeps, launchagent, ccc]
related:
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - sweeps/2026-06-01-daily.md
maturity: core
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- `@concepts/federated-daily-research-digest.md` — federation pattern
- `@concepts/monokern-compounding-research-pipeline.md` — weekly overlay

## Raw Concept

CCC-local cadence for automated discovery installed 2026-06-01 (K93).

## Narrative

| Step | When | Output |
|------|------|--------|
| LaunchAgent | Daily ~08:15 | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| Inbox drops | Same run | `research to be indexed/` |
| Cursor ingest | Operator session | 3–15 wiki pages + `wiki/log.md` |

Load agent: `launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.ccc.plist`

Config topics: `scripts/daily_research_config.yaml`.

## Snippets

> Federated install from @osint-wiki/concepts/federated-daily-research-digest.md
