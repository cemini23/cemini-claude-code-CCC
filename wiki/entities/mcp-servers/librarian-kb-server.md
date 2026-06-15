---
title: librarian-kb-server — REST API serving the OSINT wiki
type: entity
tags: [mcp-server, librarian, kb-server, hetzner, rest-api, wiki-serving, decommissioned]
keywords: [librarian, kb-server, cemini-librarian, hetzner, kb ingest, wiki serving, REST]
related:
  - entities/tools/conductor-mcp.md
  - concepts/cross-wiki-routing.md
  - entities/mcp-servers/stash.md
  - entities/mcp-servers/llm-wiki-compiler.md
  - concepts/deep-research-evaluation-prompt.md
  - entities/tools/anything-llm.md
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/rag-binary-quantization.md
  - concepts/agents-k1-agent-native-knowledge-orchestration.md
  - sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-internet-of-agentic-ai-2606.12835.md
maturity: retracted
created: 2026-05-13
updated: 2026-06-15
---

## Relations

- `@entities/tools/conductor-mcp.md` — the conductor's primary retrieval backend
- `@concepts/cross-wiki-routing.md` — librarian's role in the cross-wiki query pipeline
- `@entities/mcp-servers/stash.md` — durable-storage MCP layer sharing the librarian deployment surface
- `@osint-wiki/meta/librarian-decommission-2026-06-14.md` — **authoritative** decommission record

Cross-wiki: `@osint-wiki/concepts/librarian-server-architecture.md` — historical architecture.

## Raw Concept

`[RETRACTED 2026-06-14]` Hetzner host `cemini-librarian` **deleted**. kb-server REST API and `kb ingest` cron are **offline**. Wiki canon is laptop git per federation repo; query via Read/grep locally.

## Narrative

### Decommission (2026-06-14)

| Item | Status |
|------|--------|
| Host `cemini-librarian` | Deleted |
| Port 3838 kb-server | Gone |
| Hourly `sync_wiki_to_librarian.sh` | Deprecated (script exits 3) |
| lazy-tool `kb_search` | Fails — use local wiki files |
| Conductor fallback | **Default path:** read each wiki's local `wiki/` on laptop |

### Historical — federation serving layer (pre-decommission)

The librarian was the **federation serving layer**, hosted on `cemini-librarian` (Hetzner). It served `/opt/cemini-wiki/<wiki-alias>/wiki/` over a REST API. Public wikis plus `ccc-wiki` synced from the maintainer laptop via `@osint-wiki` `scripts/sync_wiki_to_librarian.sh` (hourly cron + post-commit hook).

The librarian-kb-server:

- Served wiki content over HTTP (read-only)
- Provided a `/search` endpoint backed by embeddings + keyword
- Provided a `/page/<slug>` endpoint for direct retrieval
- Refreshed its index via `kb ingest` (server-side cron from `/opt/cemini-wiki/<alias>/wiki/`)

**Synced wikis** (historical):

| Alias | Remote path | Notes |
|-------|-------------|-------|
| `osint-wiki` | `wiki/` | Private repo |
| `ccc-wiki` | `ccc-wiki/wiki/` | This wiki — public |
| `image-gen-wiki` | `image-gen-wiki/wiki/` | Public |
| `seo-wiki` | `seo-geo-wiki/wiki/` | Public |
| `3d-printing-wiki` | `3d-printing-wiki/wiki/` | Public |
| `cybersecurity-wiki` | `cybersecurity-wiki/wiki/` | Public |

## Dead Ends

- **Treating the librarian as a write path** — it was read-only; writes happened on the laptop.
- **Querying the librarian after 2026-06-14** — host deleted; restore from Hetzner snapshot only if operator re-provisions.
