# CCC Wiki — Operations Log

Append-only chronological record of wiki operations: bootstraps, ingests, sweeps, retractions. Newest entries on top.

---

## [2026-05-13] bootstrap | CCC meta-wiki seeded from sibling-wiki schemas

Fifth sibling wiki in the Cemini federation initialized. Topic: meta — how Cemini operates Claude Code.

- Mirrored Cybersecurity wiki's `CLAUDE.md` schema (laptop-only flavor); adapted folder layout (entity categories: tools / skills / mcp-servers / hooks / commands / patterns / people), Related-Wikis table, Phase-0 audit failure-mode bullets.
- Ported `scripts/wiki_lint.py` and `scripts/preingest_check.py` from OSINT WORKSPACE/scripts. No code changes — the scripts are env-driven (`WIKI_DIR`) and locate the wiki by `Path(__file__).parent.parent / "wiki"`.
- Authored root files: `README.md`, `ROADMAP.md`, `LESSONS.md`, `hot.md`, `.gitignore`.
- Wrote 16 seed pages:
  - `entities/tools/`: claude-code, claude-mem, exa-mcp, conductor-mcp, openspec, syncthing
  - `entities/mcp-servers/`: anthropic-skills, exa, librarian-kb-server
  - `entities/patterns/`: ralph-loop, full-prompt-goal-template
  - `concepts/`: context-engineering, token-economics-and-prompt-caching, subagent-orchestration, cross-wiki-routing, hooks-for-automation
- Wired 7 cross-wiki body @-links from CCC into OSINT (ralph-loop, full-prompt-goal-template, openspec, conductor, librarian, subagent-orchestration, cross-wiki-routing).
- Added `ccc-wiki` row to OSINT's CLAUDE.md Related Wikis table (path: `../projects/Cemini claude code CCC/wiki/`) and added `@ccc-wiki/...` backlinks to the OSINT target pages.
- Initialized git repo. No remote configured. Initial commit covers the schema, scripts, seed corpus, and index/log.
- Lint result: clean (exit code 0). All `@path` body mentions resolve; all `related:` paths resolve; no orphans; no bidirectional gaps; no missing frontmatter.

Pages created: 16 + index.md + log.md. Outbound cross-wiki links: 7. Inbound backlinks added to OSINT: matches outbound count.
