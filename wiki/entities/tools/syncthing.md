---
title: Syncthing — peer-to-peer file sync for Claude Code projects
type: entity
tags: [tool, sync, syncthing, file-sync, p2p, claude-code]
keywords: [syncthing, file sync, peer-to-peer, laptop sync, project sync, .stignore, dev hygiene]
related:
  - entities/tools/claude-code.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — Syncthing is workflow infrastructure under Claude Code, not part of the harness

## Narrative

Syncthing is the peer-to-peer file synchronization tool Cemini uses to keep `~/Desktop/` (and selectively the wiki repos) in sync across the macOS laptop and the Hetzner librarian where applicable. It runs as a local daemon with a web UI on `localhost:8384`. Each shared folder has a `.stignore` file controlling exclusions, and folders are paired by device IDs — no cloud account, no third-party server.

**Why Syncthing instead of iCloud / Dropbox / git remote**:

- **Privacy**: end-to-end encrypted P2P. No vendor sees the wiki contents.
- **No bandwidth cap**: handles the multi-GB `raw-sources/` corpora that gitignore + cloud-sync flag as too-large.
- **Conflict policy**: Syncthing's `.stversions/` archives are explicit, scoped to the folder, and easier to triage than Dropbox's silent conflicts.
- **Cemini cost discipline**: zero recurring fee; runs on hardware Cemini already pays for.

**`.stignore` patterns Cemini reuses across wikis** — exclude the same paths that `.gitignore` excludes, plus a few sync-specific traps:

```
# Match .gitignore
.claude/
.env
hot.md
research to be indexed/
briefs/

# Sync-only exclusions
.DS_Store
*.swp
.stversions/
```

**Interaction with Claude Code**: Syncthing is **not part of the Claude Code harness**. It runs alongside as workflow infrastructure. Claude Code reads/writes the wiki files; Syncthing replicates them to peers. The two never communicate directly. A pitfall worth flagging: a Stop hook that writes to a synced folder (e.g., `hot.md` rewrite at session end) triggers a sync round-trip. For files Cemini wants fast-replicating, this is desirable; for files the policy excludes (`.claude/`), `.stignore` blocks the replication entirely.

**Adoption status**: in active use; not heavily documented in any wiki. This page exists as a placeholder for the next time Cemini debugs a sync conflict and wants a reference.

## Dead Ends

- **Putting `.claude/settings.json` under Syncthing** — leaks per-machine paths and personal allowlists; keep `.claude/` in `.stignore` always.
- **Syncing `raw-sources/` to a low-disk peer** — the corpus is multi-GB. Sync only to peers with the headroom.
