---
title: "Cross-wiki tool eval inventory — all CCC-routed items from OSINT tool evaluations"
type: concept
tags: [concept, cross-wiki-routing, tool-eval, inventory, catalog]
keywords: [tool-eval, cross-wiki-routing, osint-eval, ccc-catalog, tool-inventory, verdict-register]
related:
  - concepts/cross-wiki-routing.md
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - concepts/twelve-rule-claude-md-template.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- @concepts/cross-wiki-routing.md — the routing discipline that produced this inventory; every item below arrived via cross-wiki brief
- @concepts/subagent-orchestration.md — many items below are agent-orchestration tools/patterns
- @entities/tools/conductor-mcp.md — the conductor is the cross-wiki query router that fans to the wikis these tools were evaluated from

## Raw Concept

This page is the consolidated receipt for all CCC-routed items from OSINT-wiki tool evaluations (K45 through K56, May 2026). It serves as a searchable inventory — each item gets one line with tool name, license, eval verdict, CCC disposition, and primary wiki home. Items promoted to full CCC pages are noted with a link. This page replaces what would otherwise be ~35 individual stub pages.

## Narrative

### Routing pattern

OSINT-wiki runs a multi-wiki tool evaluation → CCC-relevant items (Claude Code workflow, agent orchestration, MCP servers, skills, patterns) are routed here as cross-wiki briefs → briefs are triaged: apex items get full entity pages, the rest are cataloged below.

### Apex items (promoted to full pages)

| Tool | CCC Page | Why promoted |
|------|----------|-------------|
| Citadel | @entities/patterns/citadel-agent-orchestration.md | Apex agent-orchestration OS layer |
| evilsocket/audit | @entities/patterns/glasswing-deliberate-disagreement.md | Glasswing deliberate-disagreement pattern |
| defenseclaw | @entities/tools/defenseclaw.md | Security governance for agentic AI |
| cc-wf-studio | @entities/tools/cc-wf-studio.md | Visual workflow editor for CC pipelines |
| DeLive | @entities/tools/delive.md | Desktop→MCP→agent-skill bridge pattern |
| EverOS | @entities/tools/everos.md | Context-offload-to-disk memory OS |
| src-hunter-skill | @entities/skills/src-hunter-skill.md | Largest SKILL.md design exemplar |

### Full inventory (all routed items)

#### From K45 (2026-05-15) — 52-URL eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| defenseclaw | Apache-2.0 | Adopt | **Promoted to page** | ccc-wiki |
| DeepZero | MIT | Adopt | Catalog — Jinja2 agent-orchestration template; reference | osint-wiki |
| LEANN | MIT | Adopt | Catalog — MCP-native local vector memory; already adopted in OSINT | osint-wiki |
| pm-claude-skills | MIT | Adopt | Catalog — 106 SKILL.md files; clone-and-symlink pattern | ccc-wiki |
| Arcforge | NOASSERTION | Defer | Catalog — architecture-design IDE; license unverified | osint-wiki |
| lytenyte | dual-license (unverified) | Defer | Catalog — pre-built CC "AI Skills" context files | ccc-wiki |
| OpenAgents | Apache-2.0 | Defer | Catalog — agent-orchestration reference; no commits since Oct 2023 | osint-wiki |
| deepeval | Apache-2.0 | Adopt | Catalog — Vibe-Coder auto-test-generation from failing LLM metrics | osint-wiki |
| Decepticon | Apache-2.0 | Steal-from | Catalog — model fallback chain (Anthropic→Gemini→Ollama); cybersec-primary | cybersec-wiki |
| T-Pot | GPL-3.0 | Steal-from | Catalog — honeypot-as-agent-sandbox; backlink to agent-vm-sandboxing | cybersec-wiki |
| open-generative-ai | MIT | Steal-from | Drop (image-gen-wiki domain) | image-gen-wiki |
| voicebox | MIT | Adopt | Drop (image-gen-wiki domain) | image-gen-wiki |
| multi-codex | unverified | Defer | **Promoted previously** → @concepts/2026-05-13_multi-codex-codex-home-isolation.md | ccc-wiki |
| tolaria | AGPL-3.0 | Steal-from | **Promoted previously** → @concepts/2026-05-13_tolaria-steal-from-patterns.md | ccc-wiki |
| EGGROLL | (research paper) | Reference | Drop (ML research; osint-wiki domain) | osint-wiki |

#### From K51 (2026-05-18) — 36-repo eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| Citadel | unverified | Steal-from | **Promoted to page** | ccc-wiki |
| openai/skills | unverified | Steal-from | Catalog — OpenAI Codex Skills catalog; Agent Skills open standard | ccc-wiki |
| mimeo | unverified | Steal-from | Catalog — generates SKILL.md/AGENTS.md artifacts; persona-cloning templates | ccc-wiki |
| playwright-computer-use | unverified | Steal-from | Catalog — MCP bridge for autonomous browser; self-healing selectors | ccc-wiki |
| Codeman | unverified | Steal-from | Catalog — parallel CC/Opencode in tmux sessions; zero-lag WebUI | ccc-wiki |
| md2html | unverified | Steal-from | Catalog — CC skill: Markdown→self-contained HTML with Mermaid/TOC | ccc-wiki |
| agent-toolkit | unverified | Steal-from | Catalog — curated skill collection; 1.8k★, 17.6k+ marketplace installs | ccc-wiki |
| awesome-cli-coding-agents | n/a (directory) | Reference | Catalog — curated directory of terminal-native AI coding agents | ccc-wiki |
| buddyme | NO LICENSE | Reject | Reject — multi-model agent framework; fully opaque IP | — |
| litellm-agent-platform | NO LICENSE | Reject | Reject — BerriAI sandboxed agent platform; sandboxing concept noted | — |

#### From K53 (2026-05-18) — 41-URL eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| cc-wf-studio | AGPL-3.0-or-later (claimed) | Adopt (with AGPL caveat) | **Promoted to page** | ccc-wiki |
| picoclaw | MIT | Adopt | Catalog — Go local-gateway; MCP-server architecture mirror; 29k★ | ccc-wiki |
| git-truck | MIT | Adopt | Catalog — local-first git viz via `npx -y git-truck`; 710★ | ccc-wiki |
| hermes-desktop | MIT | Adopt | Catalog — Tauri/React desktop GUI for Hermes Agent; 5.8k★ | osint-wiki |
| ai-engineer-roadmap | unverified | Reference | Catalog — non-executable Markdown roadmap; training reference | ccc-wiki |
| grex | Apache-2.0 | Reference | Catalog — regex-from-examples CLI; MCP-server wrapping exemplar | cybersec-wiki |
| gridex | Apache-2.0 | Reference | Catalog — native DB IDE; architecture template for unbloated dev tools | osint-wiki |

#### From K54 (2026-05-19) — 26-URL eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| DeLive | Apache-2.0 | Adopt | **Promoted to page** | ccc-wiki |
| EverOS | Apache-2.0 | Re-evaluate (license verified) | **Promoted to page** | ccc-wiki |
| notebooklm-py | MIT | Adopt | Catalog — reverse-engineered NotebookLM SDK; ships `.agents` skill dir; 13.7k★ | ccc-wiki |
| Windows-Use | MIT | Adopt | Catalog — AI agent driving Windows GUI; subagent-orchestration exemplar | ccc-wiki |
| LLMFeeder | MIT | Re-evaluate (license verified) | Catalog — browser extension; one-keystroke web→Markdown with token estimation | ccc-wiki |
| pro-workflow | NO LICENSE | Reject | Reject — self-correcting SQLite-FTS5 memory for CC; genuinely unlicensed | — |
| TruffleHog | AGPL-3.0 | Reference | Catalog — credential scanner; Git pre-commit-hook reference for CC scripts | ccc-wiki |
| Hackers-Arise tutorial | n/a (educational) | Reference | Catalog — MCP server log-analysis blueprint | ccc-wiki |
| free-programming-books | CC-BY-4.0 | Reference | Catalog — 388k★ text corpus; benchmark fodder for local retrieval latency testing | ccc-wiki |

#### From K55 (2026-05-20) — 19-URL eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| src-hunter-skill | MIT | Adopt | **Promoted to page** | ccc-wiki |
| OpenHuman v0.54 | GPL-3.0 | Steal-from (patterns) | Catalog — agentmemory bridge, Memory Tree, TokenJuice; codebase quarantined | osint-wiki |
| ai-polymarket-agent | MIT | Adopt | Catalog — Polymarket MCP server; Phase-0 pending on cemini-prod side | osint-wiki |
| awesome-claude | UNVERIFIED | Reference | Catalog — curated Claude-ecosystem registry; automated intake schema | ccc-wiki |
| the-book-of-secret-knowledge | GPL-3.0 | Reference | Catalog — 220k★ sysops/CLI reference; read-only, no verbatim fork | ccc-wiki |
| hackingtool-plugin | NO LICENSE | Defer | Drop — 1 star, no license, dead | — |
| J.A.R.V.I.S | NO LICENSE | Defer | Drop — 2019 Python boilerplate; legacy | — |
| Windows-Terminal-Guide | n/a (collection) | Reference | Drop — sysops reference; CCC is macOS+Linux primary | — |

#### From K56 (2026-05-21) — agentic-infra ingest

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| evilsocket/audit | MIT | Adopt (pattern) | **Promoted to page** | ccc-wiki |
| arkon | PolyForm Internal Use 1.0.0 | Reference (pattern) | Catalog — RBAC MCP server for per-user memory partitioning | ccc-wiki |
| offensive-claude | (claude-code-plugin) | Reference | Catalog — 25 offensive/defensive skill modules + 6 sub-agents; also cybersec | cybersec-wiki |
| OpenPipe/ART | Apache-2.0 | Reference | Catalog — GRPO RL training infrastructure for agent fine-tuning; 9.5k★ | ccc-wiki |
| Alephant AI Gateway | GPL-3.0 | Reference (architecture) | Catalog — Rust AI gateway; per-agent virtual keys, 3-tier budget circuit breakers | ccc-wiki |
| presenton | Apache-2.0 | Reference | Catalog — self-hosted AI presentation generator; BYOK/local Ollama | ccc-wiki |
| tiptop | MIT | Reference | Catalog — Textual TUI system monitor; minor relevance | ccc-wiki |

#### Cross-wiki posts (K56 Posts.docx)

| Post | Author | CCC Action |
|------|--------|-----------|
| "How top AI labs are building RL agents in 2026" | @_avichawla | Catalog — system-prompt-mutation as RL primitive; reference |
| "Karpathy's CLAUDE.md hit #1 with 82k stars" | @0xDepressionn | **Backlink** → extend @concepts/twelve-rule-claude-md-template.md |
| "Turn Obsidian Into a Personal OS" | @cyrilXBT | Catalog — PKM workflow; cross-reference to OSINT curator/librarian model |
