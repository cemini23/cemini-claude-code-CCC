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
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/conductor-mcp.md` — the conductor's primary retrieval backend
- `@concepts/cross-wiki-routing.md` — librarian's role in the cross-wiki query pipeline
- `@entities/mcp-servers/stash.md` — durable-storage MCP layer sharing the librarian deployment surface
- `@entities/mcp-servers/llm-wiki-compiler.md` — candidate upstream compiler that would feed the librarian's index

Cross-wiki: `@osint-wiki/concepts/librarian-server-architecture.md` carries the canonical architecture write-up.

## Raw Concept

The librarian is the **OSINT wiki's serving layer**, hosted on `cemini-librarian` (Hetzner). It serves `/opt/cemini-wiki/<wiki-alias>/wiki/` over a REST API. CCC and the other laptop-only wikis (Cybersecurity / 3D-printing / Image-gen / SEO) are **not synced to the librarian** by default — they're laptop-only by design.

## Narrative

The librarian-kb-server runs on the Hetzner box `cemini-librarian` (connection details in `.local/server.md` of the OSINT workspace, gitignored). It:

- Serves wiki content over HTTP (read-only)
- Provides a `/search` endpoint backed by embeddings + keyword
- Provides a `/page/<slug>` endpoint for direct retrieval
- Refreshes its index via `kb ingest` (a server-side cron-driven sync from `/opt/cemini-wiki/<alias>/wiki/`)

**Synced wikis** (per OSINT's CLAUDE.md "Using the conductor/librarian for unified search" section):

- `osint-wiki` — primary; canonical home for the OSINT wiki
- `image-gen-wiki` — optional sync via rsync from laptop
- `seo-wiki` — optional sync via rsync from laptop
- `3d-printing-wiki` — optional sync via rsync from laptop
- `cybersecurity-wiki` — currently laptop-only; not synced
- `ccc-wiki` (this wiki) — currently laptop-only; not synced

**Why CCC is not synced**: by design. CCC content is meta-workflow — the audience is future Cemini sessions reading the wiki *on this laptop*. A future cross-wiki conductor query (e.g., "what does Cemini's hook policy look like?") that needs CCC content reads CCC's local `wiki/` directory directly via the conductor's per-wiki-alias resolution. No server round-trip required.

**When CCC would justify a sync**:

- Multi-machine Cemini development (more than one laptop)
- A team workflow (currently solo-dev)
- An external consumer (claude.ai web session that needs to query CCC over HTTP)

None of these are active today. If they become active, the sync is a one-line addition to the wiki-sync cron on the librarian, plus a `ccc-wiki` row in OSINT's libraries config. ROADMAP.md tracks this as a deferred follow-up.

**Phase-0 verdict** (OSINT side, K28-K30): GO with caveats — see SwarmVault/PageIndex NO-GO history. The librarian's value is precisely the graph-preserving fan-out those competitors lacked.

## Dead Ends

- **Treating the librarian as a write path** — it's read-only. Writes happen on the laptop via the per-wiki ingest workflow; the librarian re-reads on `kb ingest`.
- **Querying the librarian for laptop-only wikis** — won't find anything. Laptop-only wikis are read directly off the macOS filesystem by the conductor.
