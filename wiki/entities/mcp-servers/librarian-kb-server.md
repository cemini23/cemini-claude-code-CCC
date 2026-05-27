---
title: librarian-kb-server — REST API serving the OSINT wiki
type: entity
tags: [mcp-server, librarian, kb-server, hetzner, rest-api, wiki-serving]
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
maturity: validated
created: 2026-05-13
updated: 2026-05-26
---

## Relations

- `@entities/tools/conductor-mcp.md` — the conductor's primary retrieval backend
- `@concepts/cross-wiki-routing.md` — librarian's role in the cross-wiki query pipeline
- `@entities/mcp-servers/stash.md` — durable-storage MCP layer sharing the librarian deployment surface
- `@entities/mcp-servers/llm-wiki-compiler.md` — candidate upstream compiler that would feed the librarian's index

Cross-wiki: `@osint-wiki/concepts/librarian-server-architecture.md` carries the canonical architecture write-up.

## Raw Concept

The librarian is the **federation serving layer**, hosted on `cemini-librarian` (Hetzner). It serves `/opt/cemini-wiki/<wiki-alias>/wiki/` over a REST API. Public wikis plus `ccc-wiki` sync from the maintainer laptop via `@osint-wiki` `scripts/sync_wiki_to_librarian.sh` (hourly cron + post-commit hook). **`osint-wiki` itself is private** and syncs from the same script but is not a public GitHub deliverable.

## Narrative

The librarian-kb-server runs on the Hetzner box `cemini-librarian` (connection details in `.local/server.md` of the OSINT workspace, gitignored). It:

- Serves wiki content over HTTP (read-only)
- Provides a `/search` endpoint backed by embeddings + keyword
- Provides a `/page/<slug>` endpoint for direct retrieval
- Refreshes its index via `kb ingest` (a server-side cron-driven sync from `/opt/cemini-wiki/<alias>/wiki/`)

**Synced wikis** (hourly + post-commit via `@osint-wiki` `scripts/sync_wiki_to_librarian.sh` → `cemini-librarian:/opt/cemini-wiki/<alias>/wiki/`):

| Alias | Remote path | Notes |
|-------|-------------|-------|
| `osint-wiki` | `wiki/` | Private repo; primary financial canon |
| `ccc-wiki` | `ccc-wiki/wiki/` | **This wiki** — public; synced since 2026-05-21 |
| `image-gen-wiki` | `image-gen-wiki/wiki/` | Public |
| `seo-wiki` | `seo-geo-wiki/wiki/` | Public |
| `3d-printing-wiki` | `3d-printing-wiki/wiki/` | Public |
| `cybersecurity-wiki` | `cybersecurity-wiki/wiki/` | Public |

**Conductor fallback**: when kb-server is unreachable, the conductor can still read each wiki's local `wiki/` directory on the maintainer laptop (per `wiki-alias`).

**Operational note** (2026-05-21): `ccc-wiki` and all public federation wikis are on the hourly rsync path. Reindex runs only when rsync reports file changes. SSH host aliases (`cemini-librarian`) are maintainer-local — not published in this public repo.

**Phase-0 verdict** (OSINT side, K28-K30): GO with caveats — see SwarmVault/PageIndex NO-GO history. The librarian's value is precisely the graph-preserving fan-out those competitors lacked.

## Dead Ends

- **Treating the librarian as a write path** — it's read-only. Writes happen on the laptop via the per-wiki ingest workflow; the librarian re-reads on `kb ingest`.
- **Querying the librarian before sync completes** — stale or empty until the laptop rsync + `kb vault reindex` run. Conductor falls back to local `wiki/` directories.
