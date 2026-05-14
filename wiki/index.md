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

## entities/mcp-servers/

| Page | Maturity | Summary |
|------|----------|---------|
| [`anthropic-skills`](entities/mcp-servers/anthropic-skills.md) | draft | SKILL.md spec, Phase-0 skill audit checklist, Cemini's installed skills |
| [`exa`](entities/mcp-servers/exa.md) | core | Exa neural search MCP server (paid API) |
| [`librarian-kb-server`](entities/mcp-servers/librarian-kb-server.md) | validated | Hetzner-hosted REST API serving the OSINT wiki |

## entities/skills/

| Page | Maturity | Summary |
|------|----------|---------|
| [`tech-debt-audit`](entities/skills/tech-debt-audit.md) | validated | Cemini's installed code-audit skill (100% SKILL.md compliant after 2026-05-13 retrofit) |
| [`claude-seo-agrici`](entities/skills/claude-seo-agrici.md) | validated | Local-SEO Claude Code skill (GBP, NAP, geo-grid) |
| [`marketingskills`](entities/skills/marketingskills.md) | draft | Marketing-framework skill bundle (PAS, brand voice, localized copy) |
| [`geo-seo-claude`](entities/skills/geo-seo-claude.md) | validated | Generative-engine SEO skill (citability, AI crawlers, schema) |

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

## entities/sources/hooks/people

Currently empty / placeholder. As Cemini ingests Claude Code release notes, conference talks, and hook recipes, those subdirectories will populate. See `ROADMAP.md` for the deepening backlog.

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

## Concepts

- [Nested Learning (Behrouz et al, NeurIPS 2025)](concepts/nested-learning.md) — cross-wiki stub routed from ingest — `cross-wiki`
