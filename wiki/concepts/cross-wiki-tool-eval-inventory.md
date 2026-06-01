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
  - concepts/tools-we-dont-use.md
  - entities/tools/open-design.md
  - entities/tools/the-architect.md
  - entities/tools/repomix.md
  - entities/tools/n8n-mcp.md
  - entities/tools/anything-llm.md
  - entities/tools/ai-engineering-roadmap.md
  - entities/tools/openevolve.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/claude-code-game-studios.md
  - entities/tools/agents-best-practices.md
  - entities/tools/everything-claude-code.md
  - entities/tools/cursor-community-plugins.md
  - entities/tools/hermes-agent.md
  - entities/tools/google-eng-practices.md
  - entities/tools/ml-intern.md
  - entities/tools/rowboat.md
  - entities/tools/centaur.md
  - entities/tools/purple-cli.md
  - entities/tools/metatrader-mcp-server.md
  - entities/tools/three-man-team.md
  - entities/tools/claude-subconscious.md
  - entities/tools/council-of-high-intelligence.md
  - entities/tools/open-claude-code.md
  - entities/tools/mercury-agent-skills.md
  - entities/tools/solo-founder-superpowers.md
  - entities/tools/build-your-own-openclaw.md
  - entities/tools/ai-infra-engineer-learning.md
  - entities/tools/andrej-karpathy-skills-multica.md
  - entities/tools/bmad-creative-intelligence-suite.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/claude-prompt-engineering-techniques.md
  - concepts/claude-code-finance-research-setup.md
  - concepts/obsidian-vellum-second-brain-stack.md
  - concepts/karpathy-token-efficiency-patterns.md
  - concepts/full-stack-ai-engineer-agent-path.md
  - concepts/train-llm-agents-2026-curriculum.md
  - concepts/agentic-programming-full-stack-thesis.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - entities/tools/kimi-agent-swarm.md
  - sources/k67-explorax-100-repos-reference.md
  - entities/tools/notebooklm-py.md
  - sources/multi-wiki-tool-eval-25url-2026-05-28.md
  - sources/trading-posts-compilation-38-2026-05-28.md
  - concepts/harness-de-bloat-4x4-pattern.md
  - concepts/enterprise-auto-mode-telemetry-rollout.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - entities/tools/tvscreener.md
  - entities/tools/mermaid-skill.md
  - concepts/k73-phase0-audit-decisions.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - entities/tools/hermes-desktop.md
  - entities/tools/librechat.md
  - entities/tools/skyhook-radar.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - entities/tools/slot-casino-game-developer-skills.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
maturity: draft
created: 2026-05-21
updated: 2026-06-01
---

## Relations

- @concepts/cross-wiki-routing.md — the routing discipline that produced this inventory; every item below arrived via cross-wiki brief
- @concepts/subagent-orchestration.md — many items below are agent-orchestration tools/patterns
- @entities/tools/conductor-mcp.md — the conductor is the cross-wiki query router that fans to the wikis these tools were evaluated from
- @concepts/tools-we-dont-use.md — reject policy layer beneath this inventory
- @entities/tools/open-design.md — K57 promoted steal-from page

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
| hermes-agent | MIT | Reference | `@entities/tools/hermes-agent.md` — Nous runtime; conductor peer, not adopt (K52/K64) | ccc-wiki + osint-wiki |
| hermes-desktop | MIT | Adopt | Catalog — Tauri/React desktop GUI for Hermes Agent; 5.8k★ | osint-wiki |
| ai-engineer-roadmap / Ai-Engineering-Roadmap | MIT (K60) | Reference | **Promoted** → @entities/tools/ai-engineering-roadmap.md | ccc-wiki |
| grex | Apache-2.0 | Reference | Catalog — regex-from-examples CLI; MCP-server wrapping exemplar | cybersec-wiki |
| gridex | Apache-2.0 | Reference | Catalog — native DB IDE; architecture template for unbloated dev tools | osint-wiki |

#### From K54 (2026-05-19) — 26-URL eval

| Tool | License | Eval Verdict | CCC Disposition | Primary Wiki |
|------|---------|-------------|-----------------|-------------|
| DeLive | Apache-2.0 | Adopt | **Promoted to page** | ccc-wiki |
| EverOS | Apache-2.0 | Re-evaluate (license verified) | **Promoted to page** | ccc-wiki |
| notebooklm-py | MIT | Adopt | **Page** → `@entities/tools/notebooklm-py.md` (K69 Post 18); reverse-engineered NotebookLM SDK | ccc-wiki |
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
| open-design | Apache-2.0 | Adopt (steal-from) | **Promoted to page** | ccc-wiki |
| the-architect | MIT | Adopt | **Promoted to page** (Phase-0 pending) | ccc-wiki |
| rag-from-scratch | MIT | Steal-from | Catalog — tutorial RAG patterns for kb-server docs | ccc-wiki |
| repomix | MIT | Reference | **Promoted to page** | ccc-wiki |
| n8n-mcp | MIT | Defer | **Promoted to page** (CONDITIONAL-GO) | ccc-wiki |
| anything-llm | MIT | Reference | **Promoted to page** | ccc-wiki |
| claude-code-tips | NOASSERTION | Defer | **Promoted to page** (license blocked) | ccc-wiki |
| OpenHands | NOASSERTION | Defer | Catalog — agentic IDE; license file present, SPDX unverified | ccc-wiki |
| ida-pro-mcp | MIT | Reference | Catalog — IDA MCP pattern; cybersec-primary | cybersec-wiki |
| rtk-ai/rtk | unverified | Skeptic | Catalog — see @concepts/tools-we-dont-use.md | ccc-wiki |
| ClawRouter | unverified | Skeptic | Catalog — see @concepts/tools-we-dont-use.md | ccc-wiki |
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

#### From K57 (2026-05-22) — Posts.docx + 35-URL eval

| Item | License | CCC disposition |
|------|---------|-----------------|
| @TheAhmadOsman LLMs 101 | n/a (post) | **Page** → @concepts/local-llm-mechanics-primer.md |
| @Suryanshti777 AI OS essay | n/a (post) | Reference only — overlaps conductor/librarian; no new page |
| open-design | Apache-2.0 CONFIRMED | **Page** → @entities/tools/open-design.md |
| the-architect | MIT CONFIRMED | **Page** → @entities/tools/the-architect.md |
| rag-from-scratch | MIT | Catalog (steal-from) |

#### From K55-2 ridark list (2026-05-21) — unaudited curation

| Item | CCC disposition |
|------|-----------------|
| Reject tier (#1, #5, #18, #30) | **Page** → @concepts/tools-we-dont-use.md |
| repomix, n8n-mcp, anything-llm | **Pages** (MIT verified 2026-05-22) |
| claude-code-tips | **Page** (license NOASSERTION — defer) |
| OpenHands, ida-pro-mcp, rtk, ClawRouter | Catalog only — no stub farm |

#### From K59 (2026-05-23) — Tier-B agent-harness papers (same sweep as ForesightFlow)

| Item | CCC disposition |
|------|-----------------|
| SkillRAE (2605.10114) | **Pages** → `@concepts/skillrae-retrieval-augmented-execution.md`, `@sources/arxiv-skillrae-2605.10114.md` |
| GraphFlow (2605.14968) | **Pages** → `@concepts/graphflow-verifiable-agent-workflows.md`, `@sources/arxiv-graphflow-2605.14968.md` |
| SkillsVote (2605.18401) | Deferred — not downloaded |

#### From K60 (2026-05-23) — v4 20-URL eval (CCC slice)

| Item | License | CCC disposition |
|------|---------|-----------------|
| Ai-Engineering-Roadmap | MIT CONFIRMED | **Page** → @entities/tools/ai-engineering-roadmap.md (reference-only) |
| grace-marketplace, COG-second-brain | MIT (eval) | Reject scope — no CCC pages |

#### From K63 (2026-05-24) — 36-URL eval (CCC slice)

| Tool | License | CCC disposition |
|------|---------|-----------------|
| openevolve | Apache-2.0 CONFIRMED | **Page** → @entities/tools/openevolve.md (Adopt, Docker Phase-0) |
| awesome-cursorrules | CC0-1.0 CONFIRMED | **Page** → @entities/tools/awesome-cursorrules.md (curated rules import) |
| Claude-Code-Game-Studios | MIT CONFIRMED | **Page** → @entities/tools/claude-code-game-studios.md (steal-from) |
| agents-best-practices | MIT | **Page** → defer stub |
| everything-claude-code (ECC) | MIT | **Page** → defer; canon @osint-wiki |
| cursor/community-plugins | NO LICENSE | **Page** → CONDITIONAL-GO discovery only |
| cursor-vip, go-cursor-help, cursor2api, cursor-auto-free | mixed | Reject → @concepts/tools-we-dont-use.md |

#### From K65 (2026-05-24) — Kimi Agent Swarm vs Claude Agent Teams

| Tool | License | CCC disposition |
|------|---------|-----------------|
| Kimi Agent Swarm (Moonshot) | Vendor SaaS | **Pages** → `@concepts/kimi-agent-swarm-vs-claude-agent-teams.md`, `@entities/tools/kimi-agent-swarm.md` (REFERENCE; no MCP) |
| Claude Agent Teams | Anthropic | **In use** — aligns with `@concepts/subagent-orchestration.md` |

#### From K67 (2026-05-26) — Claude/Obsidian workflows (Posts.docx CCC slice)

| Item | CCC disposition |
|------|-----------------|
| Pre-mortem skill (Post 29) | **Page** → `@concepts/claude-premortem-skill.md` |
| Obsidian maintenance (21, 33) | **Page** → `@concepts/obsidian-agent-maintenance-workflow.md` |
| Obsidian trading journal (20, 30) | **Page** → `@concepts/obsidian-trading-journal-workflow.md` |
| Software factory (24) | **Page** → `@concepts/claude-code-software-factory.md` |
| Personal OS (25) | **Page** → `@concepts/claude-code-personal-os-scope.md` (scope warning) |
| @exploraX_ 100-repo list (36) | **Stub** → `@sources/k67-explorax-100-repos-reference.md` (audit queue) |
| claude-obsidian tool install | **Unchanged** — `@entities/tools/claude-obsidian.md` DO NOT ADOPT |

#### From K69 (2026-05-27) — Claude/Obsidian/LLM posts (Posts.docx CCC slice)

| Item | CCC disposition |
|------|-----------------|
| LLM engineering curriculum (Post 2) | **Page** → `@concepts/llm-engineering-stack-curriculum.md` |
| Agent sandbox Unikraft (Post 3) | **Page** → `@concepts/agent-sandbox-unikraft.md` |
| RAG binary quantization (Post 4) | **Page** → `@concepts/rag-binary-quantization.md` |
| Large codebase Claude Code (Post 9) | **Page** → `@concepts/claude-code-large-codebase-workflow.md` |
| OpenClaw/Hermes token waste (Post 13) | **Page** → `@concepts/agent-token-discipline-openclaw-hermes.md` |
| Obsidian + NotebookLM CLI (Posts 17–18) | **Page** → `@concepts/claude-obsidian-notebooklm-bridge.md` + `@entities/tools/notebooklm-py.md` |
| notebooklm-py (inventory) | **Entity** — link inventory row to `@entities/tools/notebooklm-py.md` |

#### From K68 (2026-05-26) — 22-URL eval (CCC slice)

| Tool | License | CCC disposition |
|------|---------|-----------------|
| google/eng-practices | CC-BY-3.0 | **Page** → `@entities/tools/google-eng-practices.md` (REFERENCE) |
| huggingface/ml-intern | Apache-2.0 | **Page** → `@entities/tools/ml-intern.md` (REFERENCE) |
| rowboatlabs/rowboat | Apache-2.0 | **Page** → `@entities/tools/rowboat.md` (STEAL-FROM) |
| paradigmxyz/centaur | NOASSERTION | **Page** → `@entities/tools/centaur.md` (architecture only) |
| erickochen/purple | MIT | **Page** → `@entities/tools/purple-cli.md` (CONDITIONAL-GO doc-level) |
| MadAppGang/claudish | **no LICENSE** | Reject → `@concepts/tools-we-dont-use.md` (eval overturn) |

#### From K71 (2026-05-27) — 27-URL eval (CCC slice)

| Tool | License | CCC disposition |
|------|---------|-----------------|
| metatrader-mcp-server | MIT | **Page** → `@entities/tools/metatrader-mcp-server.md` (CONDITIONAL-GO) |
| three-man-team | MIT | **Page** → `@entities/tools/three-man-team.md` |
| claude-subconscious | MIT | **Page** → `@entities/tools/claude-subconscious.md` |
| council-of-high-intelligence | MIT | **Page** → `@entities/tools/council-of-high-intelligence.md` |
| open-claude-code | MIT | **Page** → `@entities/tools/open-claude-code.md` |
| mercury-agent-skills | (verify per file) | **Page** → `@entities/tools/mercury-agent-skills.md` (STEAL-FROM) |
| solo-founder-superpowers | MIT | **Page** → `@entities/tools/solo-founder-superpowers.md` (STEAL-FROM) |
| build-your-own-openclaw | — | **Page** → `@entities/tools/build-your-own-openclaw.md` (REFERENCE) |
| ai-infra-engineer-learning | — | **Page** → `@entities/tools/ai-infra-engineer-learning.md` (REFERENCE) |
| multica-ai/andrej-karpathy-skills | **no LICENSE** | **Page** → `@entities/tools/andrej-karpathy-skills-multica.md` (REFERENCE only) |
| bmad creative-intelligence-suite | — | **Page** → `@entities/tools/bmad-creative-intelligence-suite.md` (DEFER) |

#### From K72 (2026-05-27) — Posts-25 + Continual Harness arXiv

| Item | CCC disposition |
|------|-----------------|
| Agent completion gates (Post 0) | **Page** → `@concepts/agent-completion-verification-gates.md` |
| mem0/OpenClaw/Hermes memory (Post 1) | **Page** → `@concepts/agent-memory-stack-comparison.md` |
| Claude plugins guide (Post 4) | **Page** → `@concepts/claude-plugins-catalog-patterns.md` |
| Prompt engineering 10 techniques (Post 5) | **Page** → `@concepts/claude-prompt-engineering-techniques.md` |
| Finance research harness (Post 10) | **Page** → `@concepts/claude-code-finance-research-setup.md` |
| Obsidian+Vellum stacks (Posts 13–14, 7, 21) | **Page** → `@concepts/obsidian-vellum-second-brain-stack.md` |
| Karpathy token savings (Post 15) | **Page** → `@concepts/karpathy-token-efficiency-patterns.md` |
| Full-stack AI path / Hermes (Posts 17–18) | **Page** → `@concepts/full-stack-ai-engineer-agent-path.md` |
| Train agents 2026 (Post 20) | **Page** → `@concepts/train-llm-agents-2026-curriculum.md` |
| Agentic programming thesis (Post 23) | **Page** → `@concepts/agentic-programming-full-stack-thesis.md` |
| Continual Harness arXiv 2605.09998 | **Pages** → `@concepts/continual-harness-online-self-improvement.md`, `@sources/arxiv-continual-harness-self-improving-agents-2605.09998.md` |
| Posts.docx provenance | **Stub** → `@sources/trading-posts-compilation-25-2026-05-27.md` |

#### From K73 (2026-05-28) — Posts-38 + 25-URL eval

| Item | CCC disposition |
|------|-----------------|
| License skepticism (NO-LICENSE false negatives, blanket BSL language) | **Page** → `@concepts/tool-eval-license-skepticism-patterns.md` |
| Enterprise Auto Mode telemetry rollout (Post 1) | **Page** → `@concepts/enterprise-auto-mode-telemetry-rollout.md` |
| Harness de-bloat 4 skills / 4 agents (Post 2) | **Page** → `@concepts/harness-de-bloat-4x4-pattern.md` |
| K73 posts provenance | **Stub** → `@sources/trading-posts-compilation-38-2026-05-28.md` |
| K73 tool-eval provenance | **Stub** → `@sources/multi-wiki-tool-eval-25url-2026-05-28.md` |

#### From K73 (2026-05-28) — Phase-0 decisions (CCC local scope)

| Item | CCC disposition |
|------|-----------------|
| mermaid-skill (MIT) | **Page** → `@entities/tools/mermaid-skill.md` (**CONDITIONAL-GO local**) |
| metatrader-mcp-server (MIT) | **Updated page** → `@entities/tools/metatrader-mcp-server.md` (**NO-GO current scope**) |
| tvscreener (Apache-2.0) | **Page** → `@entities/tools/tvscreener.md` (**REFERENCE / CONDITIONAL local**) |
| Two-gate policy clarification | **Page** → `@concepts/k73-phase0-audit-decisions.md` |

#### From K88 (2026-05-31) — v5 eval (29 URLs) + Posts-42 harness slice

| Item | CCC disposition |
|------|-----------------|
| Webwright | **Page** → `@entities/tools/webwright.md` (CONDITIONAL-GO; Phase-0 pending) |
| Skill_Seekers | **Page** → `@entities/tools/skill-seekers.md` |
| book-to-skill | **Page** → `@entities/tools/book-to-skill.md` |
| SkillNet | **Page** → `@entities/tools/skillnet.md` |
| cc-thinking-skills | **Page** → `@entities/tools/cc-thinking-skills.md` (MIT license correction) |
| claude-skill-registry | **Page** → `@entities/tools/claude-skill-registry.md` |
| alirezarezvani/claude-skills | **Page** → `@entities/tools/alirezarezvani-claude-skills.md` |
| jezweb/claude-skills | **Page** → `@entities/tools/jezweb-claude-skills.md` (STEAL-FROM) |
| ruflo | **Page** → `@entities/tools/ruflo.md` (REFERENCE; Post 41) |
| Karpathy 7 basics (Post 0) | **Page** → `@concepts/karpathy-agent-infrastructure-basics.md` |
| Subagent 15-min template (Post 2) | **Page** → `@concepts/claude-code-subagent-templates.md` |
| Harness/AGENTS.md cluster | **Page** → `@concepts/claude-harness-dynamic-workflows-k88.md` |
| v5 eval provenance | **Stub** → `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` |
| Posts-42 provenance | **Stub** → `@sources/trading-posts-compilation-42-2026-05-31.md` |

#### From K90 (2026-05-31) — v6 eval (41 URLs) + Posts-16 harness slice

| Item | CCC disposition |
|------|-----------------|
| npxskillui | **Page** → `@entities/tools/npxskillui.md` (CONDITIONAL-GO; Phase-0 pending) |
| hermes-desktop | **Page** → `@entities/tools/hermes-desktop.md` (CONDITIONAL-GO reference GUI) |
| affaan-m/ECC | **Update** → `@entities/tools/everything-claude-code.md` (Gemini Adopt; CCC DEFER until hook audit) |
| LibreChat | **Page** → `@entities/tools/librechat.md` (REFERENCE) |
| skyhook-io/radar | **Page** → `@entities/tools/skyhook-radar.md` (DEFER) |
| Personality file (Post 2) | **Page** → `@concepts/agent-personality-file-hermes-openclaw.md` |
| 9-stage agent team (Post 10) | **Page** → `@concepts/nine-stage-agent-team-production.md` |
| Remote Hermes (Post 11) | **Page** → `@concepts/remote-hermes-access-pattern.md` |
| Agents roadmap (@amitiitbhu) | **Page** → `@concepts/ai-agents-learning-roadmap-reference.md` |
| Claude Artifacts apps (Post 13) | **Page** → `@concepts/claude-artifacts-app-building.md` |
| v6 eval provenance | **Stub** → `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` |
| Posts-16 provenance | **Stub** → `@sources/trading-posts-compilation-16-2026-05-31.md` |

#### From K92 (2026-06-01) — v7 eval (90 URLs, iGaming strip) + Posts-12 harness slice

| Item | CCC disposition |
|------|-----------------|
| obsidian-second-brain | **Page** → `@entities/tools/obsidian-second-brain-eugeniughelbur.md` (CONDITIONAL-GO laptop-only) |
| claude-trading-skills | **Page** → `@entities/tools/claude-trading-skills.md` (CONDITIONAL-GO; repo URL unverified) |
| Slot-Casino-Game-Developer-Skills | **Page** → `@entities/tools/slot-casino-game-developer-skills.md` (NO-GO prod; catalog only) |
| Harness competition (Post 9) | **Page** → `@concepts/harness-layer-competition-cursor-claude-perplexity.md` |
| DeepSeek cost routing (Post 10) | **Page** → `@concepts/deepseek-coding-cost-routing.md` |
| Agentic PM artifacts (Post 6) | **Page** → `@concepts/agentic-pm-review-artifacts.md` |
| Personality file (Post 12) | **Update** → `@concepts/agent-personality-file-hermes-openclaw.md` |
| v7 eval provenance | **Stub** → `@sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md` |
| Posts-12 provenance | **Stub** → `@sources/trading-posts-compilation-12-2026-06-01.md` |

#### From K93 (2026-06-01) — v5 eval (34 URLs) + Posts-31 + structural digest

| Item | CCC disposition |
|------|-----------------|
| revfactory/harness | **Page** → `@entities/tools/revfactory-harness.md` (CONDITIONAL-GO) |
| agents-best-practices | **Update** → `@entities/tools/agents-best-practices.md` (cherry-pick Adopt) |
| Thin harness / fat skills (@garrytan) | **Page** → `@concepts/thin-harness-fat-skills-garrytan.md` |
| Harness updating vs benefit (arXiv) | **Page** → `@concepts/harness-updating-vs-benefit-nonmonotonic.md` |
| Monokern weekly pipeline | **Page** → `@concepts/monokern-compounding-research-pipeline.md` |
| Federated daily digest | **Page** → `@concepts/federated-daily-research-digest.md` + `scripts/` install |
| memory-os | **Defer** — no page (eval Defer; verify repo later) |
| v5 eval provenance | **Stub** → `@sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` |
| Posts-31 provenance | **Stub** → `@sources/trading-posts-compilation-31-2026-06-01.md` |
| arXiv 2605.30621 | **Stub** → `@sources/arxiv-harness-updating-not-benefit-2605.30621.md` |
| Monokern source | **Stub** → `@sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md` |
