# CCC — Cemini Claude Code Wiki — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for **how Cemini operates Claude Code** — scoped to:

1. **Claude Code workflow** (CLI harness, IDE extension, fast/slow modes, settings, permissions) — the day-to-day driver of the OSINT / Cybersecurity / 3D-printing / Image-gen / SEO wikis.
2. **Agent orchestration** (subagents, conductor, Task tool, Plan agent, Explore agent, agent isolation) — who does what when a single Claude session would blow its context budget.
3. **Context + token economics** (prompt caching 5-minute TTL, lazy injection, context windows, sub-300s vs 1200s wake intervals, what burns cache and what doesn't).
4. **MCP servers** (Exa, Brave, librarian-kb-server, conductor, stash, claude-mem, playwright, Anthropic skills marketplace) — discovery, audit, install, settings hygiene.
5. **Hooks · Skills · Slash commands · Settings** (`SessionStart`, `Stop`, `UserPromptSubmit`; SKILL.md frontmatter spec; user vs project commands; `.claude/settings.json` patterns).
6. **Prompting patterns** (`/goal` single-shot meta-prompt, Ralph loop pattern, OpenSpec spec-driven workflow, /loop dynamic mode, ScheduleWakeup discipline).

Audience: **future Cemini sessions reading this back as their reference manual**, plus any LLM librarian asked "how does this human run Claude Code?" Written for LLM consumption — terse, sourced, cross-linked. Not marketing.

This is a **laptop-only** workspace. Raw sources archive to **`cemini-egress-fi:/opt/cemini-bulk/research/ccc/`** via OSINT `archive_raw_to_egress.sh`. No wiki rsync to librarian (decommissioned 2026-06).

## Architecture — three layers

1. **Raw sources** — immutable. Canonical archive: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/` via OSINT `archive_raw_to_egress.sh`.
   - Anthropic docs (`docs.claude.com/en/docs/claude-code/...`) saved as `.md`
   - Repo snapshots of third-party Claude-Code tooling (`claude-mem`, `openspec`, `awesome-ralph`, etc.)
   - Conference / podcast transcripts on Claude Code workflow (`.md`)
   - Screenshots of `.claude/settings.json`, hook configurations, MCP wiring (`.png`)
   - **Drop pattern**: `research to be indexed/` → ingest → archive to egress-fi (local copy removed on success)

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`. Structured pages on tools, MCP servers, hooks, skills, slash commands, patterns, people, and concepts.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): adoption recommendations for new MCP servers, hook templates ready to paste into `settings.json`, slash-command drafts, prompt envelopes for specific workflows
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
Cemini claude code CCC/             # repo root
  CLAUDE.md                         # this file — the schema
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active workstreams + decisions + done log
  hot.md                            # session-state cache (gitignored)
  README.md                         # human-facing entry point
  research to be indexed/           # transient drop zone (gitignored)
  raw-sources/                      # archived raw source corpus (gitignored)
  briefs/                           # staging for distribution → claude.ai or hands-on (gitignored)
  wiki/                             # canonical wiki
    index.md                        # content-oriented catalog of all wiki pages
    log.md                          # append-only chronological operations log
    sources/                        # one page per ingested source
    entities/
      tools/                        # claude-code, claude-mem, openspec, exa-mcp, conductor-mcp, syncthing, ...
      skills/                       # per-skill catalog (SKILL.md-compliant pages)
      mcp-servers/                  # exa, brave-search, anthropic-skills, librarian-kb-server, ...
      hooks/                        # SessionStart, Stop, UserPromptSubmit hook recipes
      commands/                     # slash command pages (/goal, /loop, /schedule, /review, ...)
      patterns/                     # ralph-loop, full-prompt-goal-template, /goal-Ralph-OpenSpec hybrid
      people/                       # authors of patterns / tools we lean on
    concepts/                       # context-engineering, token-economics-and-prompt-caching, etc.
  scripts/                          # wiki_lint.py, preingest_check.py
  prompts/                          # reusable prompt templates
  .claude/                          # Claude Code per-project state (gitignored)
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/tools/claude-code.md`, `entities/mcp-servers/exa.md`, `entities/commands/goal.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
maturity: draft | validated | core
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + tested in real workflow) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, examples. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / commands / config blocks / screenshots-as-text with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned (e.g. an MCP server that looked promising but failed Phase-0; a hook pattern that introduced an unfixable loop)

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — categories: tools, skills, mcp-servers, hooks, commands, patterns, people. Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — examples: context-engineering, token-economics-and-prompt-caching, subagent-orchestration, cross-wiki-routing, hooks-for-automation. Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable. Body sections: `## Target` (claude.ai | hands-on | settings.json patch) / `## Summary` / `## Body` / `## Sources`.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub

**Citation tags**:
- Source page: `[Source: filename.md p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- GitHub repo: `[Source: github.com/owner/repo @ <sha>]`
- Anthropic docs: `[Source: docs.claude.com/en/docs/claude-code/<page> (retrieved YYYY-MM-DD)]`
- Multiple: `[Sources: filename.md p.5, docs.claude.com/...]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources, OR personally tested in a Claude Code session
- `[TENTATIVE]` — single source or untested
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so staleness can be flagged. Especially important for harness behavior — Claude Code ships rapidly and behavior pinned today may be wrong in two weeks.
- `[RETRACTED]` — previously believed, now disproven (e.g. a hook event that was renamed in a Claude Code release). Keep in place with a note; don't delete

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Visibility | Description |
|-------|------|------------|-------------|
| `ccc-wiki` | `wiki/` | **Public** | Cursor + Claude Code meta-wiki — workflow, agents, MCP, hooks, skills, slash commands, /goal·Ralph·OpenSpec |
| `osint-wiki` | `../../OSINT WORKSPACE/wiki/` | **Private** | Financial research, quant finance, prediction markets, CeminiSuite. Shared: conductor/librarian, skill audits |
| `gambling-wiki` | `../Gambling wiki/wiki/` | **Public** | Sports betting, casino, poker, DFS, best ball. Shared: Kelly/FLB theory; osint owns PM bots |
| `game-dev-wiki` | `../Game Dev wiki/wiki/` | **Public** | Hobby game dev — castle/RTS research, Godot evals, agent harness. Shared: role graphs — ccc owns generic orchestration |
| `cybersecurity-wiki` | `../Cybersecurity wiki/wiki/` | Public | Cybersecurity research — offensive/defensive, certifications. Shared: permission-scoping hooks |
| `image-gen-wiki` | `../Image gen/wiki/` | Public | Uncensored image generation, ComfyUI, LoRA, persona ops |
| `seo-wiki` | `../SEO:GEO B&M Business/wiki/` | Public | Local SEO, GBP, GEO/AEO, creator marketing skills |
| `3d-printing-wiki` | `../3D printing/wiki/` | Public | FDM/FFF, Bambu, slicers, print farms |

**Private:** `osint-wiki`, Cemini Financial Suite (`../CeminiSuite`). **Public:** this wiki (`ccc-wiki`) + six domain wikis (including `gambling-wiki`, `game-dev-wiki`). Federation table: `README.md`. Eval prompt: `prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md`.

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references (e.g., `@osint-wiki/concepts/ralph-autonomous-agent-pattern.md`)
- Bidirectional: if this wiki's page A references another wiki's page B, add a matching `@ccc-wiki/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/`
2. **Run `python3 scripts/preingest_check.py`** — detects duplicates by sha256 / arXiv ID / DOI / URL / filename / title. Verdicts: `DUPLICATE` (do not ingest without deciding), `LIKELY` (human review), `NEW` (proceed)
3. Read the source (or relevant sections for long PDFs / repo READMEs / multi-part articles)
4. **Discuss key takeaways with the user before writing**
4b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki (most often `osint-wiki` for finance-specific, or `cybersecurity-wiki` for hardening / permissions). If so, route via a stub or brief. **When in doubt, prefer a brief over a stub.**
5. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative
6. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub. Real content accumulates over subsequent ingests
7. Update `wiki/index.md` — add rows for new pages
8. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
9. **Archive raw to egress-fi**: `bash "../../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id ccc "research to be indexed/<filename>"` — update source page `Location`
10. Update `ROADMAP.md` if the ingest opens new follow-ups; stage briefs in `briefs/` if the ingest produced something actionable
11. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Mechanical checks via `scripts/wiki_lint.py` (8 checks):

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)
- **@path body mentions** that reference non-existent pages
- **Cross-wiki @wiki-alias/path** links that don't resolve

Human/LLM judgment still needed for:
- **Contradictions** — two pages making incompatible claims (e.g. one says `Stop` hook fires before final message, another says after). Flag with `[NEEDS VERIFICATION]` and note on both pages
- **Stale claims** — superseded by a Claude Code release. Move to `[RETRACTED]` with pointer to the new behavior

## External research — MCP tools

When the wiki + raw sources can't answer, or when verifying an unverified URL:

| Tool | When to use |
|------|-------------|
| `mcp__brave-search__brave_web_search` | Quick targeted lookup — Claude Code release note, hook event name, settings.json key |
| `mcp__brave-search__brave_news_search` | Recent Anthropic announcements, breaking model releases |
| `mcp__exa__web_search_exa` | Higher-signal web search for Claude Code workflow content (Anthropic blog, conference talks) |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for evaluating new Claude Code tooling. |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research — comparing competing agent-orchestration frameworks |
| `WebFetch` | Quick read of a public docs page when MCP unavailable |
| `mcp__playwright__browser_navigate` | Inspect Anthropic console, settings UI, IDE-extension surfaces when search isn't enough |

**Workflow integration**:
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa` or Brave. If results converge, ingest the best 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` + Phase-0 audit pattern (below)

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai** — copy the relevant brief body into a Claude conversation for prompt drafting, hook design, or architecture discussion
- **→ Hands-on** — paste briefs into `.claude/settings.json` patches, new skill scaffolds, or `/goal` invocations. Manual transfer; no automation
- **→ Sibling wikis** — when a CCC concept applies to OSINT/Cybersecurity/3D-printing/Image-gen/SEO, write the cross-wiki link as `@<alias>/...` and add a backlink stub on the target

No remote server, no scp, no team distribution. Everything stays on this laptop.

## Working method

- Search the wiki first. Raw sources second. External sources last (via MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim about Claude Code behavior, actively look for the opposing failure mode — every "this hook fires X" claim should be paired with the test that disproves "it sometimes fires Y"
- Flag single-source claims explicitly. Especially common with Claude Code internals — Anthropic docs are the only source for many of them
- File insights into wiki pages or briefs before they disappear from chat
- For real-world changes (editing `~/.claude/settings.json`, adopting a new MCP server, wiring a `Stop` hook), be extra rigorous about provenance — wrong calls have real-world session-cost / context-pollution consequences

## Phase-0 audit pattern (before adopting an external tool)

Before adopting any third-party Claude-Code tool into the workflow, run a Phase-0 source audit (~30 min):

1. Read the README + LICENSE + last-N-commits (or for SaaS: pricing page + terms-of-service + recent changelog)
2. **Verify license via API** — `gh api repos/<owner>/<repo> --jq '.license.spdx_id'`. README claims are not enough — see `@osint-wiki/LESSONS.md` 2026-05-11 entry on the no-LICENSE-file pattern (5 occurrences in 4 K-cycles).
3. Verify maturity — stars/commits/last-push/issue-responsiveness
4. **Audit for the most-likely failure mode for this tool class:**
   - **MCP servers**: stdio vs HTTP transport; auth model; what credentials it reads; rate limits
   - **Skills**: SKILL.md frontmatter compliance; catalog churn risk (don't depend on remote catalog content)
   - **Hooks**: blast radius (Stop hook misfires loop you forever); reversibility
   - **Prompts/patterns**: do they assume tools you don't have? do they leak credentials?
5. Compare against existing wiki coverage (don't adopt parallel implementations)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page

Pattern carried over from `@osint-wiki/concepts/tool-evaluation-framework.md` — 7+ catches of eval-brief mischaracterization since K28.

## Session-start ritual

On every new session, **before any other work**:

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from <last position>. Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 2. (Future ritual hooks land here.)

Keep each check under 60 seconds.

## Related — environment + secrets

- **Brave Search API** / **Exa API**: optional but recommended for external research. Keys live in `~/.env` or `.env` (gitignored).
- **Claude Code settings**: project-scoped state lives in `.claude/settings.json` (gitignored) and `.claude/settings.local.json` (gitignored). User-scoped state lives in `~/.claude/`. Hooks and permission allowlists go in those files — never commit them.

If you fork/clone this workspace to another machine: never reuse anyone else's keys. Set up your own Anthropic credentials, your own Brave/Exa keys.
