---
title: repomix — pack entire repo into one LLM-optimized file (MIT)
type: entity
tags: [tool, context, repo-packing, cross-wiki-route]
keywords: [repomix, yamadashy, repo-packing, context-window, llm-optimized]
related:
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/three-cache-architecture.md
  - entities/tools/claude-code.md
  - entities/tools/ttok.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
---

## Relations

- `@concepts/context-engineering.md` — single-file packing is a blunt instrument for window budgeting
- `@concepts/token-economics-and-prompt-caching.md` — large packs burn tokens/cache lines on every turn if re-injected
- `@concepts/three-cache-architecture.md` — packing does not replace KV-cache discipline
- `@entities/tools/claude-code.md` — used ahead of or inside Claude Code sessions
- `@entities/tools/ttok.md` — preview token count before pasting a pack

Cross-wiki: already referenced in `@osint-wiki` ridark-eth / eval sources; license **MIT CONFIRMED** 2026-05-22 (~25.4k★).

## Raw Concept

Routed from `briefs/2026-05-21_k55-2-ridark-eth-ccc-relevant-repos.md` (high-priority #20). Packs a repository tree into one LLM-friendly artifact — alternative to naive multi-file `Read` spam.

## Narrative

`yamadashy/repomix` is a **repo-to-single-file** packer tuned for LLM consumption (structure preservation, ignore rules, token-aware output). CCC use case: one-shot audits, onboarding subagents, or handing a snapshot to claude.ai — **not** a substitute for `@concepts/subagent-orchestration.md` Explore agent on active codebases (packs go stale immediately after edits).

### Adoption posture

| Check | Status |
|-------|--------|
| License | MIT [CONFIRMED 2026-05-22] |
| Phase-0 | **Light** — CLI UX + ignore-file behavior only |
| Verdict | **GO (utility)** — keep in toolbox; pair with `ttok` before paste |

## Dead Ends

- **Re-packing every turn** — defeats caching; pack once per stable snapshot.
