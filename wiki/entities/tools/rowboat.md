---
title: rowboatlabs/rowboat — multi-agent orchestration (Apache-2.0 steal-from)
type: entity
tags: [tool, orchestration, steal-from, k68, cross-wiki-route]
keywords: [rowboat, rowboatlabs, multi-agent, orchestration, apache-2]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/scatter-gather.md
  - entities/tools/osmedeus-acp-orchestration.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — primary consumer of orchestration diagrams
- `@entities/tools/conductor-mcp.md` — compare fan-out/merge vs rowboat topology
- `@entities/patterns/scatter-gather.md` — bounded parallel pattern contrast
- `@entities/tools/osmedeus-acp-orchestration.md` — adjacent YAML/subprocess orchestration reference

Cross-wiki: K68 `@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md`.

## Raw Concept

`rowboatlabs/rowboat` — open-source **multi-agent orchestration** framework. K68 **Steal-from** — extract role/routing patterns for CCC wiki; no wholesale stack adoption without Phase-0 clone.

## Narrative

### Steal-from targets [TENTATIVE — eval summary]

- Agent role assignment and handoff contracts
- Coordinator vs worker separation
- State passing between parallel legs

### Adoption posture

| Check | Status |
|-------|--------|
| License | Apache-2.0 [CONFIRMED K68] |
| Phase-0 | **Required** before any code import |
| Verdict | **STEAL-FROM (K68)** |

## Snippets

> "Orchestration patterns."
> — [Source: briefs/2026-05-26_k68-ccc-tooling-from-osint.md]
