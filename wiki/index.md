# CCC Wiki — Index

Content-oriented catalog of every page in this wiki. Update on every new page or major refactor. Pages with `maturity: core` are battle-tested; `validated` is cross-checked; `draft` is bootstrap-quality.

## entities/tools/

| Page | Maturity | Summary |
|------|----------|---------|
| [`claude-code`](entities/tools/claude-code.md) | core | The CLI harness — modes, slash commands, skills, hooks, MCP, agents, surrounding tool stack |
| [`claude-mem`](entities/tools/claude-mem.md) | validated | Passive observation memory; second layer beside `hot.md` |
| [`exa-mcp`](entities/tools/exa-mcp.md) | core | Claude-Code-side wiring of the Exa search MCP |
| [`conductor-mcp`](entities/tools/conductor-mcp.md) | validated | Cross-wiki query router (FastMCP) |
| [`openspec`](entities/tools/openspec.md) | draft | Spec-driven workflow alternative to Ralph and `/goal` |
| [`syncthing`](entities/tools/syncthing.md) | draft | Peer-to-peer file sync underneath Claude Code |
| [`lazy-tool`](entities/tools/lazy-tool.md) | validated | MCP discovery proxy, 46% input-token reduction (source claim) |
| [`claude-code-router`](entities/tools/claude-code-router.md) | draft | Local LLM proxy for routing + caching headers |
| [`spec-kit`](entities/tools/spec-kit.md) | draft | GitHub's CLI for spec-driven development |
| [`ttok`](entities/tools/ttok.md) | draft | Token-counter CLI; preview before paste |
| [`tech-debt-skill`](entities/tools/tech-debt-skill.md) | validated | Whole-repo audit skill (Cemini's first installed third-party skill) |
| [`cua`](entities/tools/cua.md) | draft | M-series Mac VM sandbox for Tier-2 isolation |
| [`claude-code-ultimate-guide`](entities/tools/claude-code-ultimate-guide.md) | draft | 24k-line CC reference + 28-CVE catalog + 655 malicious-skill patterns |
| [`claude-for-legal`](entities/tools/claude-for-legal.md) | draft | Anthropic-official legal-vertical plugin suite; STEAL-FROM 4 patterns (managed-agent cookbooks, cold-start interviews, Trust Layer, MCP connectors) |
| [`skillkit`](entities/tools/skillkit.md) | draft | Cross-agent skill translation/management bridge; ships `@skillkit/mcp` runtime-discovery server — ADOPT |
| [`polyterm-tui-pattern`](entities/tools/polyterm-tui-pattern.md) | draft | Cross-wiki stub — terminal-native UI-design reference (ASCII charts, keyboard chords) |
| [`osmedeus-acp-orchestration`](entities/tools/osmedeus-acp-orchestration.md) | draft | Cross-wiki stub — YAML-workflow engine orchestrating ACP subprocess agents; conductor-architecture reference |
| [`claude-obsidian`](entities/tools/claude-obsidian.md) | draft | Cross-wiki stub — DO NOT ADOPT (parallel-impl with claude-mem; SessionStart hook collision) |
| [`ai-token-monitor`](entities/tools/ai-token-monitor.md) | draft | Cross-platform Tauri desktop app monitoring Claude Code + Codex token usage (offline-first); MIT, Adopt |
| [`codexbar`](entities/tools/codexbar.md) | draft | macOS menu-bar app — live API stats, daily/weekly limit tracking + overrun notifications; MIT, Adopt |
| [`superclaude-framework`](entities/tools/superclaude-framework.md) | draft | Claude Code config/automation framework — slash commands, cognitive personas, KNOWLEDGE.md; ~22.8k★, MIT, Adopt |
| [`roo-code`](entities/tools/roo-code.md) | draft | Autonomous AI agent team in the code editor; ~24.1k★, Apache-2.0 — repo ARCHIVED, adopt only as fork-and-maintain blueprint |
| [`defenseclaw`](entities/tools/defenseclaw.md) | draft | Cisco security governance for agentic AI — MCP scanner, skill scanner, admission control, CodeGuard (Apache-2.0) |
| [`cc-wf-studio`](entities/tools/cc-wf-studio.md) | draft | VS Code visual workflow editor for Claude Code agent pipelines; conditional branching (license unverified) |
| [`delive`](entities/tools/delive.md) | draft | System-audio capture + MCP server + agent skill bridge pattern (Apache-2.0) |
| [`everos`](entities/tools/everos.md) | draft | Long-term-memory OS — context-offload-to-disk pattern for token savings (Apache-2.0) |

## entities/mcp-servers/

| Page | Maturity | Summary |
|------|----------|---------|
| [`anthropic-skills`](entities/mcp-servers/anthropic-skills.md) | draft | SKILL.md spec, Phase-0 skill audit checklist, Cemini's installed skills |
| [`exa`](entities/mcp-servers/exa.md) | core | Exa neural search MCP server (paid API) |
| [`librarian-kb-server`](entities/mcp-servers/librarian-kb-server.md) | validated | Hetzner-hosted REST API serving the OSINT wiki |
| [`pmxt-mcp-pattern`](entities/mcp-servers/pmxt-mcp-pattern.md) | draft | Cross-wiki stub — MCP-exposes-trading-execution pattern (`@pmxt/mcp`); Tier-2-gated MCP class |
| [`stash`](entities/mcp-servers/stash.md) | draft | Cross-wiki stub — persistent episodic-memory MCP (Go, Apache-2.0, Wave 5A Adopt-but-fork) |
| [`llm-wiki-compiler`](entities/mcp-servers/llm-wiki-compiler.md) | draft | Cross-wiki stub — Karpathy-pattern wiki compiler + MCP server (npm, Wave 4B Adopt) |
| [`polymarket-mcp-server`](entities/mcp-servers/polymarket-mcp-server.md) | draft | Cross-wiki stub — 45-tool autonomous-trading MCP; execution-MCP class exemplar |

## entities/skills/

| Page | Maturity | Summary |
|------|----------|---------|
| [`tech-debt-audit`](entities/skills/tech-debt-audit.md) | validated | Cemini's installed code-audit skill (100% SKILL.md compliant after 2026-05-13 retrofit) |
| [`claude-seo-agrici`](entities/skills/claude-seo-agrici.md) | validated | Local-SEO Claude Code skill (GBP, NAP, geo-grid) |
| [`marketingskills`](entities/skills/marketingskills.md) | draft | Marketing-framework skill bundle (PAS, brand voice, localized copy) |
| [`geo-seo-claude`](entities/skills/geo-seo-claude.md) | validated | Generative-engine SEO skill (citability, AI crawlers, schema) |
| [`src-hunter-skill`](entities/skills/src-hunter-skill.md) | draft | 305-payload, 19-playbook SKILL.md — largest single CC skill in the wild (MIT); design exemplar |

## entities/commands/

| Page | Maturity | Summary |
|------|----------|---------|
| [`plugin`](entities/commands/plugin.md) | validated | `/plugin marketplace add` + `/plugin install` workflow |

## entities/patterns/

| Page | Maturity | Summary |
|------|----------|---------|
| [`ralph-loop`](entities/patterns/ralph-loop.md) | draft | File-based memory for autonomous loop iterations |
| [`full-prompt-goal-template`](entities/patterns/full-prompt-goal-template.md) | validated | `/goal` single-shot meta-template (5 sections + 10 ops rules) |
| [`tier1-tier2-agent-model`](entities/patterns/tier1-tier2-agent-model.md) | validated | Scope-enforcement pattern for execution-capable agents |
| [`cpr-context-compression`](entities/patterns/cpr-context-compression.md) | draft | Cross-wiki stub — Compress/Preserve/Resume pattern; `hot.md` + claude-mem manifestation |
| [`autoresearch-loop`](entities/patterns/autoresearch-loop.md) | draft | Cross-wiki stub — proposal × objective × mutation loop; 5 documented instantiations |
| [`scatter-gather`](entities/patterns/scatter-gather.md) | draft | Cross-wiki stub — LangGraph parallel fan-out topology; parallel Agent tool calls |
| [`citadel-agent-orchestration`](entities/patterns/citadel-agent-orchestration.md) | draft | Apex agent-orchestration OS layer — 4-tier /do routing, campaign persistence, lifecycle hooks, circuit breaker |
| [`glasswing-deliberate-disagreement`](entities/patterns/glasswing-deliberate-disagreement.md) | draft | evilsocket/audit adversarial-verification pattern — multi-agent disagreement as safety primitive (MIT) |

## concepts/

| Page | Maturity | Summary |
|------|----------|---------|
| [`context-engineering`](concepts/context-engineering.md) | validated | The four levers Cemini pulls to manage the model's window |
| [`token-economics-and-prompt-caching`](concepts/token-economics-and-prompt-caching.md) | validated | 5-min cache TTL governs pacing; never sleep 300 s; MCP overhead numbers |
| [`subagent-orchestration`](concepts/subagent-orchestration.md) | validated | When to dispatch via the `Agent` tool; Tier 1/Tier 2 split |
| [`cross-wiki-routing`](concepts/cross-wiki-routing.md) | validated | Where new content belongs in the federation; brief vs stub |
| [`hooks-for-automation`](concepts/hooks-for-automation.md) | draft | `.claude/settings.json` hook events, scope, blast radius |
| [`claude-desktop-vs-claude-code`](concepts/claude-desktop-vs-claude-code.md) | validated | Two surfaces, two extension formats, two config files |
| [`three-cache-architecture`](concepts/three-cache-architecture.md) | validated | OpenRouter Response + OpenRouter Edge + Anthropic KV |
| [`mcp-context-optimization`](concepts/mcp-context-optimization.md) | validated | Four-layer optimization stack for MCP-heavy sessions |
| [`agent-vm-sandboxing`](concepts/agent-vm-sandboxing.md) | draft | Cross-wiki stub — disposable-VM isolation for Tier-2 / unvetted-skill execution |
| [`skill-vetting`](concepts/skill-vetting.md) | draft | Phase-0 audit checklist for third-party Claude Code skills (5 steps) |
| [`twelve-rule-claude-md-template`](concepts/twelve-rule-claude-md-template.md) | draft | Cross-wiki stub — Karpathy → Forrest Chang → Mnilax 12-rule template |
| [`cross-wiki-tool-eval-inventory`](concepts/cross-wiki-tool-eval-inventory.md) | draft | Consolidated receipt — all CCC-routed items from OSINT tool evaluations K45–K56 |
| [`code-as-agent-harness`](concepts/code-as-agent-harness.md) | draft | Three-layer harness model mapped to Claude Code / conductor / MCP (K48 arXiv) |
| [`self-healing-agent-sessions`](concepts/self-healing-agent-sessions.md) | draft | Failure taxonomy + retry budget for long Claude Code sessions (K48 arXiv) |
| [`deep-research-evaluation-prompt`](concepts/deep-research-evaluation-prompt.md) | validated | v1→v4 lineage; canonical copy-paste at `prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md` |
| [`cursor-ide-workspace`](concepts/cursor-ide-workspace.md) | validated | Cursor as primary laptop harness; MCP map, rules, canvas, deployment boundary |
| [`local-llm-mechanics-primer`](concepts/local-llm-mechanics-primer.md) | draft | KV cache / prefill-decode primer for local inference (K57 Post 1) |
| [`tools-we-dont-use`](concepts/tools-we-dont-use.md) | draft | Institutional reject register (ToS bypass, ridark list discipline) |
| [`open-design`](entities/tools/open-design.md) | draft | Modular skill Markdown + BYOK wiring — steal-from (K57, Apache-2.0) |
| [`the-architect`](entities/tools/the-architect.md) | draft | Claude Code meta-agent blueprint generator (K57, MIT) |
| [`repomix`](entities/tools/repomix.md) | draft | Pack repo → single LLM file (K55-2, MIT) |
| [`n8n-mcp`](entities/tools/n8n-mcp.md) | draft | n8n workflows via MCP (K55-2, MIT, CONDITIONAL-GO) |
| [`anything-llm`](entities/tools/anything-llm.md) | draft | Private local document AI — reference (K55-2, MIT) |
| [`claude-code-tips`](entities/tools/claude-code-tips.md) | draft | Community tips — license NOASSERTION, defer (K55-2) |
| [`ai-engineering-roadmap`](entities/tools/ai-engineering-roadmap.md) | draft | OSSU-style agent-engineering curriculum — reference-only (K60, MIT) |
| [`openevolve`](entities/tools/openevolve.md) | draft | Evolutionary harness optimizer — Adopt after Docker Phase-0 (K63) |
| [`awesome-cursorrules`](entities/tools/awesome-cursorrules.md) | draft | CC0 Cursor rules catalog — curated import (K63) |
| [`claude-code-game-studios`](entities/tools/claude-code-game-studios.md) | draft | Multi-agent role graphs — steal-from (K63, MIT) |
| [`agents-best-practices`](entities/tools/agents-best-practices.md) | draft | Agent practices collection — defer (K63) |
| [`everything-claude-code`](entities/tools/everything-claude-code.md) | draft | ECC harness bundle — defer; canon on osint-wiki (K63) |
| [`cursor-community-plugins`](entities/tools/cursor-community-plugins.md) | draft | Cursor plugin index — no LICENSE (K63 CONDITIONAL-GO) |
| [`skillrae-retrieval-augmented-execution`](concepts/skillrae-retrieval-augmented-execution.md) | draft | Skill-graph RAE — post-retrieval context compilation (K59 arXiv) |
| [`graphflow-verifiable-agent-workflows`](concepts/graphflow-verifiable-agent-workflows.md) | draft | Proof-carrying visual workflows + durable runtime (K59 arXiv) |

## sources/

| Page | Maturity | Summary |
|------|----------|---------|
| [`arxiv-skillrae-2605.10114`](sources/arxiv-skillrae-2605.10114.md) | draft | SkillRAE paper provenance (K59) |
| [`arxiv-graphflow-2605.14968`](sources/arxiv-graphflow-2605.14968.md) | draft | GraphFlow paper provenance (K59) |

## entities/sources/hooks/people

Hooks/people subdirs still placeholder beyond `sources/` arXiv stubs above. As Cemini ingests Claude Code release notes, conference talks, and hook recipes, those subdirectories will populate. See `ROADMAP.md` for the deepening backlog.

## Cross-wiki links from this wiki

| From | To | Reason |
|------|----|--------|
| `entities/tools/openspec.md` | `@osint-wiki/entities/tools/openspec.md` | Audit + verdict canon lives in OSINT |
| `entities/tools/conductor-mcp.md` | `@osint-wiki/concepts/conductor-orchestrator.md` | Architecture history |
| `entities/patterns/ralph-loop.md` | `@osint-wiki/concepts/ralph-autonomous-agent-pattern.md` | Original audit + Steal-from verdict |
| `entities/patterns/full-prompt-goal-template.md` | `@osint-wiki/sources/autonomous-agent-meta-prompt-2026-05.md` | Original source page |
| `entities/mcp-servers/librarian-kb-server.md` | `@osint-wiki/concepts/librarian-server-architecture.md` | Architecture canon |
| `concepts/subagent-orchestration.md` | `@osint-wiki/concepts/conductor-orchestrator.md` | Parallel-fan-out history |
| `concepts/cross-wiki-routing.md` | `@osint-wiki/concepts/librarian-server-architecture.md` | Serving-layer design |
| `entities/tools/lazy-tool.md` | `@osint-wiki/concepts/mcp-context-optimization.md` | K34 4-layer methodology source |
| `entities/tools/lazy-tool.md` | `@seo-wiki/entities/tools/claude-code-tool-stack.md` | SEO-side adoption brief |
| `entities/tools/claude-code-router.md` | `@seo-wiki/entities/tools/claude-code-tool-stack.md` | Tool 2 of the SEO stack reference |
| `entities/tools/spec-kit.md` | `@seo-wiki/entities/tools/claude-code-tool-stack.md` | Tool 6 of the SEO stack reference |
| `entities/tools/ttok.md` | `@seo-wiki/entities/tools/claude-code-tool-stack.md` | Tool 4 of the SEO stack reference |
| `concepts/three-cache-architecture.md` | `@seo-wiki/entities/tools/claude-code-tool-stack.md` | "Three caches" original write-up |
| `concepts/mcp-context-optimization.md` | `@osint-wiki/concepts/mcp-context-optimization.md` | Original methodology source |
| `concepts/claude-desktop-vs-claude-code.md` | `@seo-wiki/concepts/claude-platforms.md` | Original distinction write-up |
| `entities/commands/plugin.md` | `@seo-wiki/concepts/claude-platforms.md` | Operator-facing install instructions |
| `entities/skills/claude-seo-agrici.md` | `@seo-wiki/entities/tools/claude-seo-agrici.md` | Operator-facing canonical page + Phase-0 GO |
| `entities/skills/claude-seo-agrici.md` | `@seo-wiki/sources/github-repo-audit-2026-05-07.md` | Phase-0 audit source |
| `entities/skills/marketingskills.md` | `@seo-wiki/entities/tools/marketingskills.md` | Operator-facing write-up + Phase-0 GO |
| `entities/skills/geo-seo-claude.md` | `@seo-wiki/entities/tools/geo-seo-claude.md` | Operator-facing canonical page |
| `entities/skills/geo-seo-claude.md` | `@seo-wiki/sources/github-repo-audit-2026-05-07.md` | Phase-0 audit source |
| `entities/tools/cua.md` | `@cybersecurity-wiki/entities/tools/cua.md` | Canonical Phase-0 GO verdict |
| `entities/tools/cua.md` | `@osint-wiki/entities/tools/cua.md` | OSINT cross-route notes |
| `entities/tools/claude-code-ultimate-guide.md` | `@cybersecurity-wiki/entities/tools/claude-code-ultimate-guide.md` | Cybersec adoption notes |
| `entities/tools/claude-code-ultimate-guide.md` | `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` | Eval origin (URL 17) |
| `entities/patterns/tier1-tier2-agent-model.md` | `@cybersecurity-wiki/concepts/llm-pentest-automation.md` | Canonical pattern write-up |
| `entities/patterns/tier1-tier2-agent-model.md` | `@cybersecurity-wiki/entities/tools/pentest-ai-agents.md` | Reference implementation |
| `entities/tools/claude-for-legal.md` | `@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md` | Cross-wiki tool-eval source |
| `entities/tools/skillkit.md` | `@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md` | Cross-wiki tool-eval source |
| `entities/mcp-servers/pmxt-mcp-pattern.md` | `@osint-wiki/entities/tools/pmxt.md` | Primary page (prediction-market tool detail) |
| `entities/tools/polyterm-tui-pattern.md` | `@osint-wiki/entities/tools/polyterm.md` | Primary page (Polymarket analytics tool detail) |
| `entities/tools/osmedeus-acp-orchestration.md` | `@cybersecurity-wiki/entities/tools/osmedeus.md` | Primary page (security-orchestration engine detail) |
| `concepts/agent-vm-sandboxing.md` | `@cybersecurity-wiki/concepts/agent-vm-sandboxing.md` | Primary methodology + threat model |
| `concepts/twelve-rule-claude-md-template.md` | `@osint-wiki/concepts/claude-md-12-rule-template.md` | Primary lineage + empirical claims |
| `entities/tools/claude-obsidian.md` | `@osint-wiki/entities/tools/claude-obsidian.md` | Primary Phase-0 audit + Dead Ends |
| `entities/patterns/cpr-context-compression.md` | `@osint-wiki/concepts/context-compression-resume-pattern.md` | Primary architectural detail |
| `entities/patterns/autoresearch-loop.md` | `@osint-wiki/concepts/autoresearch-loop-pattern.md` | Primary definition + 5 instantiations |
| `entities/patterns/scatter-gather.md` | `@osint-wiki/concepts/scatter-gather-topology.md` | Primary LangGraph + conductor write-up |
| `entities/mcp-servers/stash.md` | `@osint-wiki/sources/alash3al-stash.md` | Primary source (Phase-0 audit) |
| `entities/mcp-servers/llm-wiki-compiler.md` | `@osint-wiki/sources/atomicmemory-llm-wiki-compiler.md` | Primary source (Karpathy pattern coverage) |
| `entities/mcp-servers/polymarket-mcp-server.md` | `@osint-wiki/sources/caiovicentino-polymarket-mcp-server.md` | Primary source (45-tool inventory) |
| `entities/patterns/citadel-agent-orchestration.md` | `@osint-wiki/sources/multi-wiki-tool-eval-prompt-2026-05-18.md` | K51 cross-wiki source (36-repo eval) |
| `entities/patterns/glasswing-deliberate-disagreement.md` | `@osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md` | K56 cross-wiki source (agentic-infra ingest) |
| `entities/tools/defenseclaw.md` | `@osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md` | K45 cross-wiki source (52-URL eval) |
| `entities/tools/cc-wf-studio.md` | `@osint-wiki/sources/multi-wiki-link-eval-41url-2026-05-18.md` | K53 cross-wiki source (41-URL eval) |
| `entities/tools/delive.md` | `@osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md` | K54 cross-wiki source (26-URL eval) |
| `entities/tools/everos.md` | `@osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md` | K54 cross-wiki source (26-URL eval) |
| `entities/skills/src-hunter-skill.md` | `@osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md` | K55 cross-wiki source (19-URL eval) |
| `concepts/cross-wiki-tool-eval-inventory.md` | `@osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md` | Cross-wiki routing pattern (K45–K56) |
| `concepts/code-as-agent-harness.md` | `@osint-wiki/concepts/code-as-agent-harness.md` | K48 arXiv 2605.18747 survey hub |
| `concepts/code-as-agent-harness.md` | `@osint-wiki/sources/arxiv-code-as-agent-harness-survey-2605.18747.md` | Primary source |
| `concepts/self-healing-agent-sessions.md` | `@osint-wiki/sources/arxiv-self-healing-llm-agents-2605.06737.md` | K48 arXiv 2605.06737 |
| `entities/tools/ai-token-monitor.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/codexbar.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/superclaude-framework.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/roo-code.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |

## Concepts

- [Nested Learning (Behrouz et al, NeurIPS 2025)](concepts/nested-learning.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [multi-codex — CODEX_HOME env-var isolation pattern](concepts/2026-05-13_multi-codex-codex-home-isolation.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [tolaria — refactoring-workflow patterns (STEAL-FROM, AGPL-3.0)](concepts/2026-05-13_tolaria-steal-from-patterns.md) — cross-wiki stub routed from ingest — `cross-wiki`

## Entities

- [visual-explainer — Agent Skill for Rich HTML Diagram Generation](entities/visual-explainer.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [openusage — Local Token Economics Dashboard](entities/openusage.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [claude_code_agent_farm — Parallel Claude Code Orchestration via tmux](entities/claude-code-agent-farm.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Fusion — Multi-Node Agent Orchestrator with Worktree Isolation](entities/fusion.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [cross-wiki-tool-eval-inventory — CCC-routed items from OSINT tool evaluations](concepts/cross-wiki-tool-eval-inventory.md) — consolidated catalog K45–K56 — `cross-wiki`
