---
title: "skillkit — universal translation/management bridge for AI-agent skills across 46 agents"
type: entity
tags: [entity, tool, skill-management, skill-translation, mcp-server, marketplace, session-memory, p2p-mesh, adopt, ccc-primary-fit, cross-wiki-route-2026-05-16]
keywords: [skillkit, skill-format-translation, claude-skill-md, cursor-mdc, skillkit-mcp, runtime-skill-discovery, claude-skills-directory, session-memory, p2p-mesh-distribution, apache-2-license, rohitg00]
related:
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
  - entities/tools/claude-mem.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/npxskillui.md
maturity: draft
created: 2026-05-16
updated: 2026-05-31
phase_0_verdict: CONDITIONAL-GO
cross-wiki-source: "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — skillkit governs the same `.claude/skills/` surface the SKILL.md spec defines; it is a management/translation layer on top of that spec
- @entities/commands/plugin.md — alternative skill-acquisition path: where `/plugin` installs from a marketplace, skillkit's MCP server fetches capabilities at runtime
- @entities/tools/claude-mem.md — skillkit's session memory captures transient architectural insights, conceptually adjacent to claude-mem's passive observation layer
- @concepts/claude-desktop-vs-claude-code.md — format translation (SKILL.md ↔ .mdc) spans the Claude-Code vs other-agent surface split
- @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — cross-wiki source (tool-eval ingest verdict)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. `skillkit` is a universal translation and management bridge for AI-agent skills, spanning 46 agents (Claude Code, Cursor, Devin, and others). Apache-2.0; ~1,100 stars / last commit 2026-04-21 / 12 open issues. Stack: TypeScript / Node.js. K-cycle tool-eval verdict: **ADOPT**, CCC primary fit — skillkit operates directly on the `.claude/skills/` directory Cemini already uses, and its MCP server is a clean runtime-discovery layer.

URL: https://github.com/rohitg00/skillkit

## Narrative

skillkit sits one layer above the SKILL.md spec (`@entities/mcp-servers/anthropic-skills.md`): where that spec defines what a skill *is*, skillkit manages how skills are *acquired, translated, and discovered* across agents.

### Capabilities

1. **Cross-agent skill translation** — auto-translates skill formats between agents: Claude's `SKILL.md` ↔ Cursor's `.mdc`, and across the 46-agent set. A skill authored once is usable everywhere. For CCC this is the bridge that lets a Cemini-authored skill leave the Claude Code surface without a rewrite.

2. **Skill marketplace (400,000+ skills)** — indexes a marketplace of 400k+ skills sourced from GitHub repos and Gists. Note Cemini's standing stance per `@entities/mcp-servers/anthropic-skills.md`: adopt the spec, do not depend on catalog content. The same caution applies to skillkit's marketplace — it is a discovery surface, not a source of truth, and a 400k-skill catalog carries proportionally large supply-chain surface. Phase-0 audit any skill before install.

3. **MCP server for runtime skill discovery** — ships `npx @skillkit/mcp`, an MCP server that lets agents fetch capabilities (e.g. PDF processing) at runtime without pre-installation. This is the most CCC-relevant piece: it converts skill acquisition from an install-time step into a runtime fetch, adjacent in spirit to the lazy-tool MCP-discovery-proxy pattern (`@entities/tools/lazy-tool.md`).

4. **Session memory + P2P mesh distribution** — captures transient architectural insights during a session (conceptually parallel to claude-mem's passive observation, `@entities/tools/claude-mem.md`), and distributes learned patterns across teammates over a peer-to-peer mesh.

5. **Governs `.claude/skills/`** — operates directly on the directory Cemini already uses for project- and user-scoped skills.

### Verdict

ADOPT for CCC. The MCP runtime-discovery server (`npx @skillkit/mcp`) and the cross-agent translation layer are the high-value pieces; Apache-2.0, ~1,100 stars, and a recent commit (2026-04-21) clear the maturity bar. Treat the 400k-skill marketplace as discovery-only — never auto-install. The session-memory + P2P-mesh feature should be evaluated separately and is **not** part of the adopt recommendation pending the security question below; CCC is a laptop-only workspace with no team-distribution requirement, so the P2P mesh has no current use case here.

### Open questions

- P2P mesh in firewalled / zero-trust subnets — whether the peer-to-peer pattern-distribution mesh can operate (or should be disabled) inside a firewalled zero-trust subnet is unverified. Since CCC is laptop-only with no team mesh need, default to disabling P2P distribution; resolve the security question before any networked deployment. *(Partially de-risked by Phase-0: `@skillkit/mesh` is a fully isolatable workspace package — not adopting it sidesteps the question entirely.)*

## Phase-0 Audit (2026-05-16)

Clone: `git clone --depth 50 https://github.com/rohitg00/skillkit /tmp/skillkit-audit/`. INSPECT-only — tools not executed.

**License — CONFIRMED Apache-2.0.** Root `LICENSE` is the verbatim Apache License 2.0 text. Root `package.json` declares `"license": "Apache-2.0"` (valid SPDX identifier in the manifest; no per-file SPDX headers, which is normal for a JS monorepo). GitHub `licenseInfo.key` = `apache-2.0`. Eval claim verified.

**Maturity — observed vs claimed:**
- Stars: **1,074** (eval claimed ~1,100 — accurate).
- Last commit: **2026-04-28** (eval claimed 2026-04-21 — close; the 04-21 date matches a large commit cluster, 04-28 is the true HEAD; GitHub `pushedAt` 2026-05-11 is a non-default-branch/tag push, not new mainline work).
- Open issues: **12** (eval claimed ~12 — accurate).
- Stack: TypeScript-dominant monorepo (pnpm + turbo), ~3.9 MB TS — matches "TypeScript/Node.js".
- Repo created 2026-01-20: ~3 months old. **Single-author-dominant** — of the last 50 commits, 40 are Rohit Ghumare, 10 RUFFY-369. Effectively a one-maintainer project (the owner is a *personal* GitHub account, `isInOrganization: false`), so bus-factor risk is real.

**Dependency license scan — clean, no copyleft.** Workspace deps are all permissive-ecosystem (MIT/Apache/ISC class): `zod`, `yaml`, `minimatch`, `turndown`, `@mozilla/readability`, `better-sqlite3` types, `@modelcontextprotocol/sdk`, the `@noble/*` crypto suite, `jose`, `ws`, `got`, React/Next/Tailwind/fumadocs for docs. No GPL/AGPL/LGPL pulled in. `@google/genai` appears only in the `docs/` apps, not in `packages/core` or `packages/mcp`.

**Failure-mode probe — skill-library domain-fit MISMATCH (the headline finding):**
- The CLAUDE.md tool-class failure mode for skill libraries is *domain-fit mismatch*, and SkillKit largely is one. Its core value propositions are **cross-agent** features: format translation (`SKILL.md` ↔ Cursor `.mdc` ↔ 46 agents) and a multi-machine P2P mesh. **Cemini's CCC workspace is Claude-Code-only** — there is no Cursor/Devin/Codex surface to translate *to*, and no team/multi-machine deployment that needs a mesh. The translation bridge and `@skillkit/mesh` solve problems Cemini does not have.
- The genuinely CCC-relevant slice is narrow: the `npx`-able MCP server (`@skillkit/mcp`, bin `skillkit-mcp`) for runtime skill discovery, and basic `.claude/skills/` management. That is a real but modest fit — adjacent to the lazy-tool discovery-proxy pattern already catalogued.
- **"400,000-skill marketplace" claim — NOT substantiated; inflated marketing.** The README badges and prose say "400K+ skills". The actual shipped catalog, `marketplace/skills.json`, declares `totalSkills: 15120` and physically contains a `skills` array of **15,120 entries** across 33 curated collections (`updatedAt: 2026-02-28`). The 400K figure is a marketing number (a claimed upper bound of GitHub-discoverable skills), not the curated index the tool actually ships. Treat the marketplace as a ~15k-entry discovery surface at best, and per the existing anchor stance: Phase-0 every skill, never auto-install.
- "P2P mesh" — this one *does* exist in the tree: `packages/mesh/` is a real implementation (encrypted transport via `@noble/*` + `jose`, peer discovery, identity). It is not vapor, but it is also irrelevant to a laptop-only shop and is cleanly isolatable (separate workspace package, separate `@skillkit/mesh` install).

**Decision — CONDITIONAL-GO** (downgraded from the eval's ADOPT). License is clean and the MCP runtime-discovery server is a legitimate, low-surface-area fit. But ADOPT overstates it: the marquee cross-agent translation and mesh features are domain mismatches for a Claude-Code-only workspace, the marketplace size is inflated ~26x in marketing, and the project is a ~3-month-old single-maintainer personal repo. **Conditions for any adoption:** (1) adopt *only* `@skillkit/mcp` for runtime discovery — do not adopt the translation layer or `@skillkit/mesh`; (2) pin the dependency and treat the marketplace strictly as discovery, never auto-install; (3) accept the bus-factor risk explicitly or vendor the MCP package. If those conditions cannot hold, this is a NO-GO.

## Snippets

> skillkit ships an MCP server (`npx @skillkit/mcp`) for runtime skill discovery — agents fetch capabilities like PDF processing without pre-installation. It auto-translates skill formats (Claude SKILL.md ↔ Cursor .mdc) across 46 agents and indexes a marketplace of 400,000+ skills from GitHub and Gists.
[Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md]
