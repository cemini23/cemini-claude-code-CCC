---
title: Obsidian agent maintenance workflow — vault hygiene via Claude Code
type: concept
tags: [concept, obsidian, claude-code, second-brain, k67]
keywords: [obsidian, vault-hygiene, moc, para, tag-normalization, axel-bitblaze, cyrilXBT]
related:
  - concepts/obsidian-trading-journal-workflow.md
  - entities/tools/claude-obsidian.md
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
  - entities/tools/thuki.md
  - entities/mcp-servers/librarian-kb-server.md
  - concepts/cross-wiki-routing.md
  - concepts/claude-obsidian-notebooklm-bridge.md
maturity: draft
created: 2026-05-26
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
---

## Relations

- `@concepts/obsidian-trading-journal-workflow.md` — journal **content** vs this page's **hygiene** ops
- `@entities/tools/claude-obsidian.md` — **DO NOT ADOPT** tool; steal maintenance *ideas*, not install
- `@entities/tools/claude-mem.md` — session memory layer; does not replace vault indexing
- `@entities/mcp-servers/stash.md` — episodic goals/hypotheses; not Obsidian MOC refresh
- `@entities/tools/thuki.md` — local SQLite chat history; different problem than vault tags
- `@entities/mcp-servers/librarian-kb-server.md` — federation wiki RAG; **avoid** duplicating as Obsidian indexer

Cross-wiki: K67 Posts 21 (@Axel_bitblaze69), 33 (@cyrilXBT).

## Raw Concept

K67 — **maintenance agent** pattern: Claude Code runs periodic vault hygiene (tag normalization, orphan cleanup, MOC/PARA refresh) on an Obsidian vault. Distinct from research agents or trading journal capture.

## Narrative

### Workflow shape [TENTATIVE]

1. **Scope lock** — folders or tags in scope; no full-vault rewrite without human diff review.
2. **Hygiene passes** — broken links, duplicate titles, stale MOCs, inconsistent frontmatter.
3. **Human gate** — commit or sync only after operator approves batch (git-backed vault recommended).

### CCC stack mapping

| Need | Use | Avoid |
|------|-----|--------|
| Session continuity | `@entities/tools/claude-mem.md` | Re-indexing entire vault into kb-server |
| Cross-wiki facts | `@concepts/cross-wiki-routing.md` + librarian | Treating Obsidian as CCC wiki canonical |
| Parallel tool | `@entities/tools/claude-obsidian.md` install | SessionStart collision with claude-mem |

### Verdict

**REFERENCE** for laptop personal vaults; **not** Cemini prod or CCC wiki canonical store (CCC wiki stays in `wiki/` git).

## Snippets

> "Vault hygiene via Claude: tag normalization, orphan note cleanup, MOC refresh — maintenance agent not research agent."
> — [Source: briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md, Post 21]
