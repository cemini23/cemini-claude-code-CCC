# CCC Wiki — Operations Log

Append-only chronological record of wiki operations: bootstraps, ingests, sweeps, retractions. Newest entries on top.

---

## [2026-05-13] deep-dive sweep | mined OSINT/Cybersec/SEO/3D-printing/Image-gen for Claude Code material

Cross-wiki inventory pass dispatched two parallel Explore agents to scan the four sibling wikis (OSINT was the largest pool; SEO + Cybersec produced the densest finds). 48 OSINT entries + ~20 sibling entries surfaced. Decisions:

**16 NEW pages added**:
- `entities/tools/`: lazy-tool, claude-code-router, spec-kit, ttok, tech-debt-skill, cua, claude-code-ultimate-guide
- `entities/mcp-servers/`: (none new this round)
- `entities/skills/` (new subdir): tech-debt-audit, claude-seo-agrici, marketingskills, geo-seo-claude
- `entities/commands/` (new subdir): plugin
- `entities/patterns/`: tier1-tier2-agent-model
- `concepts/`: claude-desktop-vs-claude-code, three-cache-architecture, mcp-context-optimization

**8 existing pages deepened** (added Relations + new sections):
- claude-code (now hub-flagged), claude-mem, anthropic-skills, token-economics-and-prompt-caching, subagent-orchestration, hooks-for-automation, ralph-loop, context-engineering

**Cross-wiki backlinks added** (10 sibling pages):
- SEO: claude-code-tool-stack, claude-platforms, claude-seo-agrici, geo-seo-claude, marketingskills, github-repo-audit-2026-05-07
- Cybersec: llm-pentest-automation, pentest-ai-agents, cua, claude-code-ultimate-guide
- Plus `ccc-wiki` row added to SEO and Cybersec wikis' `Related Wikis` tables (the OSINT row was added at bootstrap)

**Lint**: clean. 32 pages indexed (up from 16), 179 outbound edges (up from 58), 36/36 cross-wiki refs resolve (up from 8/8). 0 orphans, 0 bidirectional gaps, 0 dangling refs, 0 frontmatter issues.

**Source-wiki page-count by category** (post-sweep):
- entities/tools: 13 (up from 6)
- entities/mcp-servers: 3
- entities/skills: 4 (new)
- entities/commands: 1 (new)
- entities/patterns: 3 (up from 2)
- concepts: 8 (up from 5)
- TOTAL seed pages: 32 (up from 16)

Backlogged in ROADMAP for follow-up depth: structured-findings-schema pattern, cpr-context-compression pattern, agent-vm-sandboxing concept, skill-vetting concept, twelve-rule-claude-md-template concept, plus per-skill audit pages for any future skill adoption.

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

## [2026-05-13] cross-wiki route | Nested Learning (Behrouz et al, NeurIPS 2025)

Cross-wiki stub routed from `@osint-wiki/sources/nl-nested-learning-behrouz-neurips2025.md`.
- Created wiki/concepts/nested-learning.md (stub)

## [2026-05-14] cross-wiki route | visual-explainer — Agent Skill for Rich HTML Diagram Generation

Cross-wiki stub routed from `@osint-wiki/entities/tools/visual-explainer.md`.
- Created wiki/entities/visual-explainer.md (stub)

## [2026-05-14] cross-wiki route | openusage — Local Token Economics Dashboard

Cross-wiki stub routed from `@osint-wiki/entities/tools/openusage.md`.
- Created wiki/entities/openusage.md (stub)

## [2026-05-14] cross-wiki route | claude_code_agent_farm — Parallel Claude Code Orchestration via tmux

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-code-agent-farm.md`.
- Created wiki/entities/claude-code-agent-farm.md (stub)

## [2026-05-14] cross-wiki route | Fusion — Multi-Node Agent Orchestrator with Worktree Isolation

Cross-wiki stub routed from `@osint-wiki/entities/tools/fusion.md`.
- Created wiki/entities/fusion.md (stub)
