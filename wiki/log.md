# CCC Wiki — Operations Log

Append-only chronological record of wiki operations: bootstraps, ingests, sweeps, retractions. Newest entries on top.

---

## [2026-05-17] parked-followup batch | 10 ROADMAP follow-ups stubbed from sibling-wiki primaries

Cleared 10 of the 11 parked follow-ups from `ROADMAP.md` § Follow-ups from the deep-dive. Each new page is a Claude-Code-side stub pointing at an existing OSINT or Cybersec primary; bodies focus on the CCC slice (Tier-2 gates, hook collisions, harness configuration, memory-stack composition).

**New pages (10)**:
- `concepts/agent-vm-sandboxing.md` — cross-wiki stub → `@cybersecurity-wiki/concepts/agent-vm-sandboxing.md`
- `concepts/skill-vetting.md` — internal extraction from `entities/mcp-servers/anthropic-skills.md` (5-step Phase-0 checklist; OSINT-side namesake is `[RETRACTED]`, intentionally different concept)
- `concepts/twelve-rule-claude-md-template.md` — cross-wiki stub → `@osint-wiki/concepts/claude-md-12-rule-template.md`
- `entities/tools/claude-obsidian.md` — cross-wiki stub → `@osint-wiki/entities/tools/claude-obsidian.md` (DO NOT ADOPT, recorded for the hook-collision case study)
- `entities/patterns/cpr-context-compression.md` — cross-wiki stub → `@osint-wiki/concepts/context-compression-resume-pattern.md`
- `entities/patterns/autoresearch-loop.md` — cross-wiki stub → `@osint-wiki/concepts/autoresearch-loop-pattern.md`
- `entities/patterns/scatter-gather.md` — cross-wiki stub → `@osint-wiki/concepts/scatter-gather-topology.md`
- `entities/mcp-servers/stash.md` — cross-wiki stub → `@osint-wiki/sources/alash3al-stash.md`
- `entities/mcp-servers/llm-wiki-compiler.md` — cross-wiki stub → `@osint-wiki/sources/atomicmemory-llm-wiki-compiler.md`
- `entities/mcp-servers/polymarket-mcp-server.md` — cross-wiki stub → `@osint-wiki/sources/caiovicentino-polymarket-mcp-server.md`

**Bidirectional backlinks added** to 17 existing CCC pages: cua, claude-mem, claude-code, claude-code-ultimate-guide, conductor-mcp, pmxt-mcp-pattern, plugin, full-prompt-goal-template, ralph-loop, tier1-tier2-agent-model, anthropic-skills, librarian-kb-server, context-engineering, token-economics-and-prompt-caching, subagent-orchestration, hooks-for-automation, cross-wiki-routing.

**`index.md` updated**: 1 tool row, 3 mcp-server rows, 3 pattern rows, 3 concept rows, 10 cross-wiki-link rows.

**Deferred from this batch**:
- `entities/patterns/structured-findings-schema.md` — no primary page found in OSINT/Cybersec; defer until either a primary surfaces or Cemini ships its own structured-findings shape.
- `entities/mcp-servers/kb-server.md` — covered by existing `entities/mcp-servers/librarian-kb-server.md`; would be duplicate. Closed from the parked list.

---

## [2026-05-16] cross-wiki ingest | Claude-Code/agent-orchestration tools from OSINT tool-eval (v3 iteration)

Five pages cross-routed into CCC from the OSINT-side tool-eval ingest `@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`.

**2 primary tool pages** (CCC primary fit):
- `entities/tools/claude-for-legal.md` — Anthropic's official legal-vertical Claude Code/MCP plugin suite (Apache-2.0, 6,100★/6 issues). Verdict STEAL-FROM: extract managed-agent cookbooks (cadence jobs), cold-start interviews (skill bootstrapping), the Trust Layer injection guardrail (subagent orchestration), and the MCP-connector reference architecture. `[NEEDS VERIFICATION 2026-05-16]` on the Trust Layer "license gates" mechanism.
- `entities/tools/skillkit.md` — universal cross-agent skill translation/management bridge (Apache-2.0, 1,100★, last commit 2026-04-21). Verdict ADOPT: the `npx @skillkit/mcp` runtime-discovery server + SKILL.md↔.mdc translation. Marketplace (400k+ skills) treated as discovery-only. `[NEEDS VERIFICATION 2026-05-16]` on P2P-mesh security in zero-trust subnets.

**3 cross-wiki pattern stubs** (primary home is a sibling wiki; CCC-relevant patterns only):
- `entities/mcp-servers/pmxt-mcp-pattern.md` — MCP-exposes-trading-execution pattern (`@pmxt/mcp`); primary `@osint-wiki/entities/tools/pmxt.md`
- `entities/tools/polyterm-tui-pattern.md` — terminal-native UI-design reference; primary `@osint-wiki/entities/tools/polyterm.md`
- `entities/tools/osmedeus-acp-orchestration.md` — ACP subprocess-agent orchestration pattern for the conductor; primary `@cybersecurity-wiki/entities/tools/osmedeus.md`

**Bidirectional backlinks added** to 11 existing CCC pages: subagent-orchestration, full-prompt-goal-template, anthropic-skills, plugin, claude-mem, claude-desktop-vs-claude-code, context-engineering, conductor-mcp, tier1-tier2-agent-model, claude-code, exa. `index.md` updated (4 tool rows, 1 mcp-server row, 6 cross-wiki-link rows). No pre-existing near-equivalent pages found — all 5 are new.

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

## [2026-05-15] cross-wiki route | multi-codex — CODEX_HOME env-var isolation pattern

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_multi-codex-codex-home-isolation.md (stub)

## [2026-05-15] cross-wiki route | tolaria — refactoring-workflow patterns (STEAL-FROM, AGPL-3.0)

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_tolaria-steal-from-patterns.md (stub)

## [2026-05-16] phase-0 | K49 tool audits (SkillKit, claude-for-legal)

Phase-0 clone audits of the 2 CCC-wiki K49 tools. Verdicts in each entity page's `## Phase-0 Audit` section.

- **SkillKit → CONDITIONAL-GO** (downgraded from the eval's ADOPT). Apache-2.0 confirmed; deps clean. Domain-fit mismatch: SkillKit's headline value is cross-agent skill translation (Cursor/Devin) + a multi-machine P2P mesh — Cemini's CCC is Claude-Code-only with no multi-machine deployment, so those features solve problems Cemini doesn't have. The "400k-skill marketplace" claim is inflated ~26× (actual catalog: 15,120). Adopt only the `npx @skillkit/mcp` runtime-discovery server; skip the translation layer + mesh. Single-maintainer (personal account) — bus-factor risk.
- **claude-for-legal → STEAL-FROM-CONFIRMED.** Apache-2.0 confirmed; genuine `anthropics` org repo (Anthropic-staff commits). Pattern extraction into IP-sale surfaces is cleared. Extractable patterns confirmed present: managed-agent cookbooks (5 templates), cold-start interview SKILL.md, and the Trust Layer — actually a two-part guardrail (read-only-subagent injection check + admin allowlist), richer than the eval's "license gate" framing. Do not adopt the suite; extract the patterns for `subagent-orchestration`.
