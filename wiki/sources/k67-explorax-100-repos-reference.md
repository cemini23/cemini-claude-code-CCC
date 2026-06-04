---
title: K67 @exploraX_ — 100 OSS repos reference list (audit queue)
type: source
tags: [source, k67, github, catalog, reference-only]
keywords: [explorax, 100-repos, oss-list, phase-0-queue, posts-docx-k67]
related:
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/skill-vetting.md
  - concepts/claude-code-software-factory.md
  - concepts/mcp-server-catalog-curation.md
  - sources/trading-posts-compilation-18-2026-06-04.md
maturity: draft
created: 2026-05-26
updated: 2026-06-04
read_status: unread-stub
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
---

## Relations

- `@concepts/cross-wiki-tool-eval-inventory.md` — dedupe against existing catalog rows before any GO
- `@concepts/skill-vetting.md` — Phase-0 required per repo if promoted
- `@concepts/claude-code-software-factory.md` — list is input to factory eval, not truth
- `@concepts/mcp-server-catalog-curation.md` — K98 Post 10 (@exploraX_ 50 MCP) extends same queue discipline

Cross-wiki: K67 Post 36 (@exploraX_); K98 Post 10 in `@sources/trading-posts-compilation-18-2026-06-04.md`.

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Curated GitHub list (~34k chars) — agent harness, MCP, eval tools |
| Author | @exploraX_ (X) |
| Type | X long-form / link catalog |
| Location | Posts.docx K67 Post 36 |
| Retrieved | 2026-05-26 |
| read_status | unread-stub |

## Narrative

**Not ingest-as-truth.** CCC holds this stub so the list does not get re-discovered as net-new URLs each eval cycle.

### Operator workflow

1. For each candidate URL → `python3 scripts/preingest_check.py` if adding raw source.
2. `gh api` license + Phase-0 per `CLAUDE.md`.
3. Dedupe against `@concepts/cross-wiki-tool-eval-inventory.md` and OSINT `entities/tools/*`.
4. Promote only on **GO** — stub page or catalog row, not bulk entity creation.

## Snippets

> "Curated GitHub list — reference catalog, not ingest-as-truth."
> — [Source: briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md, Post 36]
