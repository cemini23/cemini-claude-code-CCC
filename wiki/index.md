# CCC Wiki — Index

Content-oriented catalog of every page in this wiki. Update on every new page or major refactor. Pages with `maturity: core` are battle-tested; `validated` is cross-checked; `draft` is bootstrap-quality.

## entities/tools/

| Page | Maturity | Summary |
|------|----------|---------|
| [`claude-code`](entities/tools/claude-code.md) | core | The CLI harness — modes, slash commands, skills, hooks, MCP, agents, surrounding tool stack |
| [`portable-llm-wiki`](entities/tools/portable-llm-wiki.md) | draft | OKF/MCP wiki protocol and lint UI — STEAL-FROM (K142) |
| [`zero`](entities/tools/zero.md) | draft | Local Go coding harness — ADOPT/TRIAL (K142) |
| [`caveman`](entities/tools/caveman.md) | draft | Opt-in terse-output token compression skill — ADOPT/TRIAL (K142) |
| [`astryx`](entities/tools/astryx.md) | draft | Agent-ready React design-system MCP/CLI pattern — STEAL-FROM (K142) |
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
| [`openshell`](entities/tools/openshell.md) | draft | NVIDIA agent runtime peer — REFERENCE (K138, Apache-2.0) |
| [`areal`](entities/tools/areal.md) | draft | Online-RL bridge for LLM agents — REFERENCE/WATCH (K139, Apache-2.0) |
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
| [`notebooklm-py`](entities/tools/notebooklm-py.md) | draft | NotebookLM SDK/CLI + agents skill dir — Adopt catalog (K69 Post 18) |
| [`webwright`](entities/tools/webwright.md) | draft | Microsoft Webwright browser harness — CONDITIONAL-GO (K88) |
| [`pegasus-ai-plugin-marketplace`](entities/tools/pegasus-ai-plugin-marketplace.md) | draft | Pegasus scientific-workflow Claude plugin — REFERENCE (K118) |
| [`user-as-code`](entities/tools/user-as-code.md) | draft | Pine AI executable user memory — CONDITIONAL-GO (K120) |
| [`dynamo-orchestration`](entities/tools/dynamo-orchestration.md) | draft | DynAMO topological workflow engine — REFERENCE (K120) |
| [`lightmem2`](entities/tools/lightmem2.md) | draft | TokenPilot-integrated memory — CONDITIONAL-GO (K121) |
| [`xcientist`](entities/tools/xcientist.md) | draft | Research harness + claim drift — REFERENCE (K122) |
| [`aohp`](entities/tools/aohp.md) | draft | Android OS-level agent harness — CONDITIONAL-GO (K123) |
| [`skill-seekers`](entities/tools/skill-seekers.md) | draft | Doc/PDF→skill converter — CONDITIONAL-GO (K88) |
| [`book-to-skill`](entities/tools/book-to-skill.md) | draft | Book corpus→skill pipeline — CONDITIONAL-GO (K88) |
| [`skillnet`](entities/tools/skillnet.md) | draft | SkillNet routing — compare lazy-tool (K88) |
| [`cc-thinking-skills`](entities/tools/cc-thinking-skills.md) | draft | Thinking-skills bundle — CONDITIONAL-GO (K88) |
| [`claude-skill-registry`](entities/tools/claude-skill-registry.md) | draft | Registry index pattern — CONDITIONAL-GO (K88) |
| [`alirezarezvani-claude-skills`](entities/tools/alirezarezvani-claude-skills.md) | draft | Curated skills — per-skill Phase-0 (K88) |
| [`jezweb-claude-skills`](entities/tools/jezweb-claude-skills.md) | draft | Production skill layouts — STEAL-FROM (K88) |
| [`ruflo`](entities/tools/ruflo.md) | draft | Swarm orchestrator — REFERENCE vs conductor (K88) |
| [`npxskillui`](entities/tools/npxskillui.md) | draft | Skill UI / marketplace CLI — CONDITIONAL-GO (K90) |
| [`hermes-desktop`](entities/tools/hermes-desktop.md) | draft | Tauri GUI for Hermes ecosystem — reference-only (K90) |
| [`librechat`](entities/tools/librechat.md) | draft | Multi-model chat UI — REFERENCE (K90) |
| [`skyhook-radar`](entities/tools/skyhook-radar.md) | draft | skyhook-io/radar — DEFER (K90) |
| [`obsidian-second-brain-eugeniughelbur`](entities/tools/obsidian-second-brain-eugeniughelbur.md) | draft | Obsidian vault cron agents — CONDITIONAL-GO laptop-only (K92) |
| [`claude-trading-skills`](entities/tools/claude-trading-skills.md) | draft | Trading skill pack — CONDITIONAL-GO Phase-0 pending (K92) |
| [`slot-casino-game-developer-skills`](entities/tools/slot-casino-game-developer-skills.md) | draft | iGaming slot skills — NO-GO prod (K92 catalog) |
| [`revfactory-harness`](entities/tools/revfactory-harness.md) | draft | Dynamic agent-team meta-skill — CONDITIONAL-GO (K93/K102) |
| [`typst`](entities/tools/typst.md) | draft | PDF compiler for brief exports — CONDITIONAL-GO (K102) |
| [`flowforge-skill`](entities/tools/flowforge-skill.md) | draft | draw.io diagram skill — CONDITIONAL-GO steal-from (K102) |
| [`agents-best-practices`](entities/tools/agents-best-practices.md) | draft | DenisSergeevitch patterns — cherry-pick Adopt (K93) |
| [`agyn`](entities/tools/agyn.md) | draft | Agent ops platform — REFERENCE (2605.27575) |
| [`tool-forge`](entities/tools/tool-forge.md) | draft | Validation-carrying toolchain — CONDITIONAL-GO (2605.28000, Apache-2.0) |
| [`scienceaix-agentskills`](entities/tools/scienceaix-agentskills.md) | draft | Agent Skills survey resource catalog — REFERENCE (2602.12430) |
| [`life-harness`](entities/tools/life-harness.md) | draft | LIFE-HARNESS runtime interface adaptation — CONDITIONAL-GO (2605.22166, K95) |
| [`adaptive-auto-harness`](entities/tools/adaptive-auto-harness.md) | draft | A-EVO-Lab stream harness tree — REFERENCE (2606.01770, K95) |
| [`retro-harness`](entities/tools/retro-harness.md) | draft | RHO reference implementation — CONDITIONAL-GO (2606.05922) |
| [`agent-skill-manager`](entities/tools/agent-skill-manager.md) | draft | asm skill registry CLI — CONDITIONAL-GO (K103) |
| [`pydantic-ai`](entities/tools/pydantic-ai.md) | draft | Typed Python agent framework — GO; reject AGPL gateway (K103) |
| [`deep-scientist`](entities/tools/deep-scientist.md) | draft | ResearAI hypothesis-loop — steal-from (K103) |
| [`autoresearch-claw`](entities/tools/autoresearch-claw.md) | draft | Research claw scheduling — steal-from (K103) |
| [`application-skills`](entities/tools/application-skills.md) | draft | Membrane application-skills — NO-GO (K103) |
| [`timeclaw`](entities/tools/timeclaw.md) | draft | Time-series-native agent harness — CONDITIONAL-GO (2606.05404) |
| [`omnifs`](entities/tools/omnifs.md) | draft | Projected API filesystem — CONDITIONAL-GO (K108) |
| [`bayesian-agent`](entities/tools/bayesian-agent.md) | draft | Posterior-guided skill evolution — CONDITIONAL-GO (K109, MIT) |
| [`paperclaw`](entities/tools/paperclaw.md) | draft | Autonomous research lifecycle harness — CONDITIONAL-GO (K124, MIT) |
| [`fara`](entities/tools/fara.md) | draft | Microsoft CUA models + FaraGen pipeline — REFERENCE (K124, MIT) |
| [`awesome-agent-engineering`](entities/tools/awesome-agent-engineering.md) | draft | Harness survey curated list — REFERENCE (K124, MIT) |
| [`esaa-conversational`](entities/tools/esaa-conversational.md) | draft | Event-sourced poly-agent handoff CLI — CONDITIONAL-GO Windows (K125) |
| [`memclaw`](entities/tools/memclaw.md) | draft | Governed fleet shared memory SaaS — REFERENCE (K125) |
| [`argusfleet`](entities/tools/argusfleet.md) | draft | Fleet memory eval harness — REFERENCE pending repo (K125) |
| [`memprobe`](entities/tools/memprobe.md) | draft | Hidden user-state recovery benchmark — REFERENCE CC-BY-4.0 (K128) |
| [`toolbench-x`](entities/tools/toolbench-x.md) | draft | Tool-environment unreliability benchmark — REFERENCE (K129) |
| [`clarus`](entities/tools/clarus.md) | draft | Web-scale research collaboration SaaS — REFERENCE (K135) |
| [`simple-agentic-scenario`](entities/tools/simple-agentic-scenario.md) | draft | TUM ABPM light-sensing reference repo — REFERENCE (K136) |
| [`automem-stanford-cognitive-skill`](entities/tools/automem-stanford-cognitive-skill.md) | draft | Stanford AutoMem metamemory framework — REFERENCE (K137) |
| [`codebase-memory-mcp`](entities/tools/codebase-memory-mcp.md) | validated | Tree-sitter code graph MCP — CONDITIONAL-GO federation deploy (K134) |
| [`migration-analysis-replication-package`](entities/tools/migration-analysis-replication-package.md) | draft | CMU harness-adaptation paper replication package — NO-GO adopt, no LICENSE (K168) |
| [`rethinking-harness-evolution-eval-harness`](entities/tools/rethinking-harness-evolution-eval-harness.md) | draft | Matched-budget harness-eval methodology repo — NO-GO adopt (no LICENSE, paid infra), REFERENCE design (K169) |

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
| [`cursor-audit`](entities/skills/cursor-audit.md) | validated | Multi-model Cursor audit — public distro in agent-toolkit-demo; vet CI (2026-06-06) |
| [`super-audit`](entities/skills/super-audit.md) | validated | Five-model pre-ship council — 3 Cursor + 2 API (OpenRouter/DeepSeek); agent-toolkit-demo (2026-06-09) |
| [`to-issues`](entities/skills/to-issues.md) | draft | mattpocock vertical-slice issue decomposition — K126 Adopt (MIT) |
| [`grill-with-docs`](entities/skills/grill-with-docs.md) | draft | mattpocock plan interview + ADRs — K126 Adopt (grill-me alias) |
| [`goal`](entities/skills/goal.md) | validated | Cursor `/goal` single-shot envelope — federation-wide (K124) |

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
| [`cross-wiki-tool-adoption-routing`](concepts/cross-wiki-tool-adoption-routing.md) | draft | Phase-0 trial matrix — which wiki owns each tool adoption (2026-06-04) |
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
| [`deep-research-evaluation-prompt`](concepts/deep-research-evaluation-prompt.md) | validated | v1→v10 lineage; canonical copy-paste at `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` |
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
| [`awesome-cursorrules`](entities/tools/awesome-cursorrules.md) | validated | CC0 Cursor rules catalog — `.cursor/rules/ccc-*.mdc` adopted |
| [`claude-code-game-studios`](entities/tools/claude-code-game-studios.md) | draft | Multi-agent role graphs — steal-from (K63, MIT) |
| [`everything-claude-code`](entities/tools/everything-claude-code.md) | draft | ECC harness bundle — defer; canon on osint-wiki (K63) |
| [`cursor-community-plugins`](entities/tools/cursor-community-plugins.md) | draft | Cursor plugin index — no LICENSE (K63 CONDITIONAL-GO) |
| [`hermes-agent`](entities/tools/hermes-agent.md) | draft | Nous Hermes runtime — reference vs conductor (K64 OSINT routing) |
| [`nvidia-skills`](entities/tools/nvidia-skills.md) | draft | Signed SKILL.md distribution — K126 OSINT stub (CONDITIONAL-GO) |
| [`mattpocock-skills`](entities/tools/mattpocock-skills.md) | draft | Composable skill library — K126 Adopt stub (MIT) |
| [`kimi-agent-swarm-vs-claude-agent-teams`](concepts/kimi-agent-swarm-vs-claude-agent-teams.md) | draft | Kimi Swarm hub vs Claude Teams mesh — CCC decision matrix (K65) |
| [`kimi-agent-swarm`](entities/tools/kimi-agent-swarm.md) | draft | Moonshot swarm product — reference only (K65) |
| [`claude-premortem-skill`](concepts/claude-premortem-skill.md) | draft | Pre-mortem SKILL pattern before harness changes (K67) |
| [`obsidian-agent-maintenance-workflow`](concepts/obsidian-agent-maintenance-workflow.md) | draft | Vault hygiene agent — pattern not claude-obsidian install (K67) |
| [`obsidian-trading-journal-workflow`](concepts/obsidian-trading-journal-workflow.md) | draft | Morning research + trading journal in Obsidian (K67) |
| [`claude-code-software-factory`](concepts/claude-code-software-factory.md) | draft | Multi-repo codegen orchestration metaphor (K67) |
| [`claude-code-personal-os-scope`](concepts/claude-code-personal-os-scope.md) | draft | Personal-OS scope discipline — narrow Cemini prod (K67) |
| [`llm-engineering-stack-curriculum`](concepts/llm-engineering-stack-curriculum.md) | draft | Hands-on LLM engineering project path (K69 Post 2) |
| [`agent-sandbox-unikraft`](concepts/agent-sandbox-unikraft.md) | draft | Lambda→Unikraft microVM agent isolation (K69 Post 3) |
| [`rag-binary-quantization`](concepts/rag-binary-quantization.md) | draft | RAG vector 32× memory reduction pattern (K69 Post 4) |
| [`claude-code-large-codebase-workflow`](concepts/claude-code-large-codebase-workflow.md) | draft | Monorepo navigation + context discipline (K69 Post 9) |
| [`agent-token-discipline-openclaw-hermes`](concepts/agent-token-discipline-openclaw-hermes.md) | draft | Always-on agent token waste anti-patterns (K69 Post 13) |
| [`claude-obsidian-notebooklm-bridge`](concepts/claude-obsidian-notebooklm-bridge.md) | draft | Vault thinking + NotebookLM CLI bridge (K69 Posts 17–18) |
| [`google-eng-practices`](entities/tools/google-eng-practices.md) | draft | Google code review heuristics — REFERENCE (K68, CC-BY-3.0) |
| [`ml-intern`](entities/tools/ml-intern.md) | draft | HF research-agent workflows — REFERENCE (K68) |
| [`rowboat`](entities/tools/rowboat.md) | draft | Multi-agent orchestration — STEAL-FROM (K68, Apache-2.0) |
| [`centaur`](entities/tools/centaur.md) | draft | Paradigm agent architecture — steal patterns only (K68, NOASSERTION) |
| [`purple-cli`](entities/tools/purple-cli.md) | draft | Lightweight CLI utility — CONDITIONAL-GO doc-level (K68, MIT) |
| [`metatrader-mcp-server`](entities/tools/metatrader-mcp-server.md) | draft | MetaTrader MCP bridge — NO-GO current scope after K73 Phase-0 |
| [`three-man-team`](entities/tools/three-man-team.md) | draft | Three-role agent team template (K71, MIT) |
| [`claude-subconscious`](entities/tools/claude-subconscious.md) | draft | Letta persistent memory — CONDITIONAL-GO (K71; check claude-mem collision) |
| [`council-of-high-intelligence`](entities/tools/council-of-high-intelligence.md) | draft | Multi-model deliberation harness (K71, MIT) |
| [`open-claude-code`](entities/tools/open-claude-code.md) | draft | Open Claude Code implementation study (K71, MIT) |
| [`mercury-agent-skills`](entities/tools/mercury-agent-skills.md) | draft | Agent skills library — STEAL-FROM (K71) |
| [`solo-founder-superpowers`](entities/tools/solo-founder-superpowers.md) | draft | Founder workflow skills — STEAL-FROM (K71, MIT) |
| [`build-your-own-openclaw`](entities/tools/build-your-own-openclaw.md) | draft | OpenClaw rebuild tutorial — REFERENCE (K71) |
| [`ai-infra-engineer-learning`](entities/tools/ai-infra-engineer-learning.md) | draft | AI infra curriculum — REFERENCE (K71) |
| [`andrej-karpathy-skills-multica`](entities/tools/andrej-karpathy-skills-multica.md) | draft | Karpathy skills — no LICENSE, reference only (K71 demote) |
| [`bmad-creative-intelligence-suite`](entities/tools/bmad-creative-intelligence-suite.md) | draft | BMAD creative module — DEFER (K71) |
| [`agent-completion-verification-gates`](concepts/agent-completion-verification-gates.md) | draft | Completion proof / done criteria (K72 Post 0) |
| [`agent-memory-stack-comparison`](concepts/agent-memory-stack-comparison.md) | draft | mem0 vs OpenClaw vs Hermes vs claude-mem (K72) |
| [`claude-plugins-catalog-patterns`](concepts/claude-plugins-catalog-patterns.md) | draft | Marketplace plugin discovery (K72 Post 4) |
| [`claude-prompt-engineering-techniques`](concepts/claude-prompt-engineering-techniques.md) | draft | 10-technique prompt catalog (K72 Post 5) |
| [`claude-code-finance-research-setup`](concepts/claude-code-finance-research-setup.md) | draft | Investment analyst harness (K72 Post 10) |
| [`obsidian-vellum-second-brain-stack`](concepts/obsidian-vellum-second-brain-stack.md) | draft | Obsidian + Claude/Vellum 24/7 brain (K72) |
| [`karpathy-token-efficiency-patterns`](concepts/karpathy-token-efficiency-patterns.md) | draft | Token savings checklist (K72 Post 15) |
| [`full-stack-ai-engineer-agent-path`](concepts/full-stack-ai-engineer-agent-path.md) | draft | Prompt engineer → builder path (K72 Posts 17–18) |
| [`train-llm-agents-2026-curriculum`](concepts/train-llm-agents-2026-curriculum.md) | draft | Train agents curriculum pointer (K72 Post 20) |
| [`agentic-programming-full-stack-thesis`](concepts/agentic-programming-full-stack-thesis.md) | draft | Agentic programming = full-stack (K72 Post 23) |
| [`continual-harness-online-self-improvement`](concepts/continual-harness-online-self-improvement.md) | draft | Reset-free harness refinement — arXiv 2605.09998 (K72) |
| [`agent-harness-operational-definition`](concepts/agent-harness-operational-definition.md) | draft | T1–T4 membership test for agent harness — 2606.10106 (K109) |
| [`openagenet-trusted-agent-discovery`](concepts/openagenet-trusted-agent-discovery.md) | draft | OAN pre-connection trust layer — REFERENCE (2606.03161) |
| [`queen-bee-beespec-enterprise-orchestration`](concepts/queen-bee-beespec-enterprise-orchestration.md) | draft | BeeSpec IR for governed enterprise MCP — 2606.06545 |
| [`bayesian-posterior-guided-skill-evolution`](concepts/bayesian-posterior-guided-skill-evolution.md) | draft | Posterior-guided skill/SOP evolution — 2606.08348 |
| [`progressive-autonomy-incident-resolution`](concepts/progressive-autonomy-incident-resolution.md) | draft | Agentic AIOps progressive autonomy — 2606.09122 |
| [`mcp-adaptive-systems-context-survey`](concepts/mcp-adaptive-systems-context-survey.md) | draft | MCP adaptive-systems survey lens — 2508.19239 |
| [`self-harness-model-specific-improvement-loop`](concepts/self-harness-model-specific-improvement-loop.md) | draft | Self-Harness weakness→proposal→validation loop — 2606.09498 |
| [`enterprise-mcp-adoption-practice`](concepts/enterprise-mcp-adoption-practice.md) | draft | Enterprise MCP interviews n=20 — 2606.09182 |
| [`channel-fracture-cross-agent-memory-delivery`](concepts/channel-fracture-cross-agent-memory-delivery.md) | draft | Silent cron cross-agent memory failures — 2606.04896 (K111) |
| [`skillhone-continual-skill-decision-history`](concepts/skillhone-continual-skill-decision-history.md) | draft | SkillHone decision-history skill evolution — 2606.08671 (K111) |
| [`tool-response-context-pruning-summarization`](concepts/tool-response-context-pruning-summarization.md) | draft | MCP tool-pair pruning N=5/W=3 — 2606.10209 (K115) |
| [`agents-all-the-way-down-custom-methodology`](concepts/agents-all-the-way-down-custom-methodology.md) | draft | Custom agent P1–P5 methodology — 2606.11869 (K115) |
| [`multi-factor-agentic-memory-value-model`](concepts/multi-factor-agentic-memory-value-model.md) | draft | Blind vs oracle forgetting — 2606.12945 (K115) |
| [`recursive-agent-harness-harness-recursion`](concepts/recursive-agent-harness-harness-recursion.md) | draft | RAH harness recursion — 2606.13643 (K115) |
| [`perspectivegap-orchestration-prompting`](concepts/perspectivegap-orchestration-prompting.md) | draft | Subagent orchestration prompt failure taxonomy — 2606.08878 (K114) |
| [`internet-of-agentic-ai-ioai`](concepts/internet-of-agentic-ai-ioai.md) | draft | IoAI vision survey — discovery, trust, controlled emergence (K114) |
| [`agents-k1-agent-native-knowledge-orchestration`](concepts/agents-k1-agent-native-knowledge-orchestration.md) | draft | Agent-native KG pipeline — REFERENCE vs librarian (2606.13669, K114) |
| [`orchestration-reward-modeling-orch-rm`](concepts/orchestration-reward-modeling-orch-rm.md) | draft | Orch-RM orchestration-level reward — 2606.13598 (K116) |
| [`harnessx-composable-evolution-foundry`](concepts/harnessx-composable-evolution-foundry.md) | draft | HarnessX nine-dim harness evolution — 2606.14249 (K116) |
| [`llm-as-code-agentic-programming`](concepts/llm-as-code-agentic-programming.md) | draft | Program-owned control flow — 2606.15874 (K116) |
| [`llm-as-orchestrator-failure-modes`](concepts/llm-as-orchestrator-failure-modes.md) | draft | ReAct loop structural failures — 2606.15874 (K116) |
| [`storage-budgeted-agent-memory-compression`](concepts/storage-budgeted-agent-memory-compression.md) | draft | MemRefine delete/merge/preserve — 2606.13177 (K117) |
| [`seagym-self-evolving-harness-evaluation`](concepts/seagym-self-evolving-harness-evaluation.md) | draft | SEAGym harness evolution eval — 2606.17546 (K117) |
| [`selective-experience-memory-harness`](concepts/selective-experience-memory-harness.md) | draft | τ-gated experience memory — 2606.17642 (K117) |
| [`specification-driven-scientific-workflow-management`](concepts/specification-driven-scientific-workflow-management.md) | draft | Intent→spec→code Pegasus pipeline — 2606.18425 (K118) |
| [`agent-first-web-framework`](concepts/agent-first-web-framework.md) | draft | ATML, ten principles, agents.txt — 2606.19116 (K119) |
| [`handoff-validity-agent-harness`](concepts/handoff-validity-agent-harness.md) | draft | Handoff contracts + EACP layers — 2606.19795 (K119) |
| [`executable-user-memory-user-as-code`](concepts/executable-user-memory-user-as-code.md) | draft | Typed Python executable user memory — 2606.16707 (K120) |
| [`plan-then-execute-topological-orchestration`](concepts/plan-then-execute-topological-orchestration.md) | draft | DynAMO DAG plan-then-execute — 2606.19382 (K120) |
| [`prompt-cache-aligned-context-management`](concepts/prompt-cache-aligned-context-management.md) | draft | TokenPilot cache-safe compaction — 2606.17016 (K121) |
| [`safeclawbench-staged-security-endpoints`](concepts/safeclawbench-staged-security-endpoints.md) | draft | Three-endpoint agent security — 2606.18356 (K121) |
| [`gatekeeper-layered-agent-evaluation`](concepts/gatekeeper-layered-agent-evaluation.md) | draft | Gatekeeper + design entropy eval — 2606.18422 (K121) |
| [`claim-drift-automated-research`](concepts/claim-drift-automated-research.md) | draft | Claim drift failure taxonomy — 2606.18874 (K122) |
| [`externalized-research-synthesis-validation`](concepts/externalized-research-synthesis-validation.md) | draft | XCIENTIST harness accountability — 2606.18874 (K122) |
| [`autonomous-coding-agents-enterprise-data`](concepts/autonomous-coding-agents-enterprise-data.md) | draft | DIA ACA-first data intelligence — 2606.19319 (K123) |
| [`cross-model-verified-agent-translation`](concepts/cross-model-verified-agent-translation.md) | draft | Parser + validator cross-model — 2606.20120 (K123) |
| [`agentic-web-infrastructure-gap-taxonomy`](concepts/agentic-web-infrastructure-gap-taxonomy.md) | draft | Agentverse 62-cap gap audit — 2606.20570 (K123) |
| [`os-level-agent-harness-android`](concepts/os-level-agent-harness-android.md) | draft | AOHP agent-native Android — 2606.23449 (K123) |
| [`model-harness-six-responsibilities`](concepts/model-harness-six-responsibilities.md) | draft | Six runtime harness responsibilities — 2606.20683 (K124) |
| [`scalable-cua-training-pipeline`](concepts/scalable-cua-training-pipeline.md) | draft | FaraGen env/solver/verifier CUA data — 2606.20785 (K124) |
| [`multi-agent-evidence-artifact-layers`](concepts/multi-agent-evidence-artifact-layers.md) | draft | Evidence/synthesis/interface layers — 2606.20997 (K124) |
| [`procedural-memory-transfer-after`](concepts/procedural-memory-transfer-after.md) | draft | AFTER procedural skill transfer — 2606.23127 (K124) |
| [`self-compacting-adaptive-context`](concepts/self-compacting-adaptive-context.md) | draft | Rubric-gated SELFCOMPACT — 2606.23525 (K124) |
| [`dual-representation-agent-memory`](concepts/dual-representation-agent-memory.md) | draft | Metis text vs code memory — 2606.24151 (K124) |
| [`mcp-trust-orchestration-collaboration`](concepts/mcp-trust-orchestration-collaboration.md) | draft | TaaS MCP trust layer — 2604.07065 (K125) |
| [`neurosymbolic-adaptive-reasoning-workflows`](concepts/neurosymbolic-adaptive-reasoning-workflows.md) | draft | VADAOrchestra Datalog+/- — OSINT route (K125) |
| [`event-sourced-poly-agent-handoff`](concepts/event-sourced-poly-agent-handoff.md) | draft | ESAA event log handoff — 2606.23752 (K125) |
| [`governed-fleet-shared-memory`](concepts/governed-fleet-shared-memory.md) | draft | MemClaw scope/provenance/supersession — 2606.24535 (K125) |
| [`hidden-user-state-recovery-audit`](concepts/hidden-user-state-recovery-audit.md) | draft | MemProbe recovery vs task success — 2606.24595 (K128) |
| [`recoverable-tool-reliability-hazards`](concepts/recoverable-tool-reliability-hazards.md) | draft | ToolBench-X five hazards — 2606.25819 (K129) |
| [`confidence-aware-tool-orchestration`](concepts/confidence-aware-tool-orchestration.md) | draft | Robust-TO tiered evidence — 2606.26904 (K129) |
| [`web-scale-scientific-collaboration-infrastructure`](concepts/web-scale-scientific-collaboration-infrastructure.md) | draft | Clarus project-agent-resource model — 2606.30246 (K135) |
| [`agentic-orchestration-options-abpm`](concepts/agentic-orchestration-options-abpm.md) | draft | OO1–OO4 ABPM orchestration taxonomy — 2606.31518 (K136) |
| [`orchestration-option-quantitative-metrics`](concepts/orchestration-option-quantitative-metrics.md) | draft | M/ABC/F1 traceability metrics — 2606.31518 (K136) |
| [`metamemory-scaffold-proficiency-training`](concepts/metamemory-scaffold-proficiency-training.md) | draft | AutoMem metamemory loops — 2607.01224 (K137) |
| [`cognitive-heuristics-llm-vuln-detection`](concepts/cognitive-heuristics-llm-vuln-detection.md) | draft | Cognitive bias in LLM scanners — cybersec stub (2606.30587) |
| [`substrate-constraints-coding-agent-oversight`](concepts/substrate-constraints-coding-agent-oversight.md) | draft | Substrate + docs CLI oversight — 2607.02389 (K138) |
| [`agentic-online-rl-self-evolving-systems`](concepts/agentic-online-rl-self-evolving-systems.md) | draft | ATDP / data-proxy / evolution control plane — 2607.01120 (K139) |
| [`client-as-first-order-harness-factor`](concepts/client-as-first-order-harness-factor.md) | draft | Same model, 2.1× gap by client — 2607.02873 (K140) |
| [`model-native-vs-tool-mediated-fulfillment`](concepts/model-native-vs-tool-mediated-fulfillment.md) | draft | Harness design axis; minimize lossy hops — 2606.31693 (K141) |
| [`algorithmic-impermeability-model-agnostic-orchestration`](concepts/algorithmic-impermeability-model-agnostic-orchestration.md) | draft | Routing independent of model; SIP + SDR — 2607.06531 (K150) |
| [`cage-1-enterprise-agent-governance-eval`](concepts/cage-1-enterprise-agent-governance-eval.md) | draft | Prebind Assurance + 12-dimension enterprise eval — 2607.03510 (K151) |
| [`multilingual-long-horizon-agent-eval`](concepts/multilingual-long-horizon-agent-eval.md) | draft | PolyWorkBench hybrid eval + compounding degradation — 2607.06008 (K152) |
| [`modular-instruction-memory-learnable-selection`](concepts/modular-instruction-memory-learnable-selection.md) | draft | MILES coarse-to-fine memory selection — 2607.06974 (K153) |
| [`hierarchical-bounded-agent-memory`](concepts/hierarchical-bounded-agent-memory.md) | draft | Short/mid/long capped memory + eviction — 2607.07666 (K154) |
| [`verifiable-search-agent-environment`](concepts/verifiable-search-agent-environment.md) | draft | DeepSearch-World deterministic verifiable search env — 2607.07820 (K156) |
| [`trustx-agent-risk-classification`](concepts/trustx-agent-risk-classification.md) | draft | TrustX ARC 12-dimension agent risk tiering — 2607.09586 (K157) |
| [`bounded-self-refinement-vs-rsi-taxonomy`](concepts/bounded-self-refinement-vs-rsi-taxonomy.md) | draft | RSI survey taxonomy + verification hierarchy — 2607.07663 (K162) |
| [`hierarchical-skill-stack-lazy-orchestration`](concepts/hierarchical-skill-stack-lazy-orchestration.md) | draft | Capability tree + LIFO stack + lazy manifests — 2607.11138 (K164) |
| [`tool-eval-license-skepticism-patterns`](concepts/tool-eval-license-skepticism-patterns.md) | draft | K73 license-eval anti-patterns (NO-LICENSE false negatives, BSL parsing) |
| [`enterprise-auto-mode-telemetry-rollout`](concepts/enterprise-auto-mode-telemetry-rollout.md) | draft | Auto Mode policy rollout via telemetry loops (K73 Post 1) |
| [`harness-de-bloat-4x4-pattern`](concepts/harness-de-bloat-4x4-pattern.md) | draft | 4-skills/4-agents simplification pattern (K73 Post 2) |
| [`k73-phase0-audit-decisions`](concepts/k73-phase0-audit-decisions.md) | draft | K73 two-gate policy and local scope decisions |
| [`mermaid-skill`](entities/tools/mermaid-skill.md) | draft | Local diagramming skill pattern — CONDITIONAL-GO (K73) |
| [`tvscreener`](entities/tools/tvscreener.md) | draft | Market-screening utility — reference/conditional local (K73) |
| [`claude-code-skills-md-institutional-memory`](concepts/claude-code-skills-md-institutional-memory.md) | draft | Skills.md as persistent behavioral infrastructure (K76 Post 2) |
| [`claude-md-five-section-template`](concepts/claude-md-five-section-template.md) | draft | Role/Style/Constraints/Workflow/Quality CLAUDE.md scaffold (K76) |
| [`five-layer-operator-stack`](concepts/five-layer-operator-stack.md) | draft | DamiDefi five-tool map — Claude/Obsidian/Hermes/Kimi/Cursor roles (K78) |
| [`obsidian-contribution-rate-workflow`](concepts/obsidian-contribution-rate-workflow.md) | draft | cyrilXBT three-zone vault + contribution-rate metric (K78) |
| [`codex-side-fork-workflow`](concepts/codex-side-fork-workflow.md) | draft | Codex `/side`/`/fork`/`goal` mapped to Cursor + Claude Code (K84) |
| [`karpathy-agent-infrastructure-basics`](concepts/karpathy-agent-infrastructure-basics.md) | draft | Karpathy 7-layer agent infra checklist (K88 Post 0) |
| [`claude-code-subagent-templates`](concepts/claude-code-subagent-templates.md) | draft | 15-min bounded subagent dispatch template (K88 Post 2) |
| [`claude-harness-dynamic-workflows-k88`](concepts/claude-harness-dynamic-workflows-k88.md) | draft | AGENTS.md + plugin + token discipline post cluster (K88) |
| [`agent-personality-file-hermes-openclaw`](concepts/agent-personality-file-hermes-openclaw.md) | draft | Personality file pattern for de-genericizing agents (K90 Post 2) |
| [`nine-stage-agent-team-production`](concepts/nine-stage-agent-team-production.md) | draft | 0xCodez 9-stage production agent team (K90 Post 10) |
| [`remote-hermes-access-pattern`](concepts/remote-hermes-access-pattern.md) | draft | Remote Hermes gateway — reference only (K90 Post 11) |
| [`ai-agents-learning-roadmap-reference`](concepts/ai-agents-learning-roadmap-reference.md) | draft | @amitiitbhu agents curriculum pointer (K90) |
| [`claude-artifacts-app-building`](concepts/claude-artifacts-app-building.md) | draft | Claude Artifacts lightweight app pattern (K90 Post 13) |
| [`harness-layer-competition-cursor-claude-perplexity`](concepts/harness-layer-competition-cursor-claude-perplexity.md) | draft | Harness layer competition post (K92 Post 9) |
| [`deepseek-coding-cost-routing`](concepts/deepseek-coding-cost-routing.md) | draft | DeepSeek cheap codegen routing (K92 Post 10) |
| [`llm-routing-deepseek-openrouter-failover`](concepts/llm-routing-deepseek-openrouter-failover.md) | draft | Shared `~/.cemini/llm-routing.env` + automatic OpenRouter backup when DeepSeek quota exhausted |
| [`agentic-pm-review-artifacts`](concepts/agentic-pm-review-artifacts.md) | draft | Agentic PM review artifacts (K92 Post 6) |
| [`thin-harness-fat-skills-garrytan`](concepts/thin-harness-fat-skills-garrytan.md) | draft | Thin harness + fat skills (@garrytan, K93) |
| [`agent-skills-taxonomy`](concepts/agent-skills-taxonomy.md) | draft | Agent skills survey — procedural gap (2605.07358, K94 OSINT) |
| [`harness-updating-vs-benefit-nonmonotonic`](concepts/harness-updating-vs-benefit-nonmonotonic.md) | draft | arXiv 2605.30621 harness-updating vs benefit (K93) |
| [`monokern-compounding-research-pipeline`](concepts/monokern-compounding-research-pipeline.md) | draft | Weekly NotebookLM deep-research overlay (K93) |
| [`federated-daily-research-digest`](concepts/federated-daily-research-digest.md) | core | Per-wiki Exa/inbox discovery automation (K93) |
| [`system-scaling-harness-agentic-ai`](concepts/system-scaling-harness-agentic-ai.md) | draft | System scaling vs model scaling — arXiv 2605.26112 |
| [`runtime-harness-interface-adaptation`](concepts/runtime-harness-interface-adaptation.md) | draft | Runtime harness adaptation — 2605.22166 (K95) |
| [`adaptive-auto-harness-open-ended-streams`](concepts/adaptive-auto-harness-open-ended-streams.md) | draft | Adaptive auto-harness — 2606.01770 (K95) |
| [`embedded-agent-modular-edge-architecture`](concepts/embedded-agent-modular-edge-architecture.md) | draft | Modular embedded agents — 2606.02862 (K95) |
| [`slm-agent-orchestration-gateway`](concepts/slm-agent-orchestration-gateway.md) | draft | SLM orchestration gateway — 2606.03557 (K95) |
| [`cli-anything-agent-native-computer-use`](concepts/cli-anything-agent-native-computer-use.md) | draft | CLI-Anything — 2606.03854 (K95 OSINT brief) |
| [`claude-code-cheat-sheet-shortcuts`](concepts/claude-code-cheat-sheet-shortcuts.md) | draft | Hidden shortcuts + command surface (K97 Post 2) |
| [`runtime-context-mcp-file-refs`](concepts/runtime-context-mcp-file-refs.md) | draft | MCP + file refs vs guessing (K97 Post 4) |
| [`agent-rubrics-self-correction`](concepts/agent-rubrics-self-correction.md) | draft | Rubrics eval harness steal (K97 Post 6) |
| [`claude-cowork-automation-vs-hooks`](concepts/claude-cowork-automation-vs-hooks.md) | draft | Cowork day automation vs Code hooks (K97 Post 13) |
| [`agent-five-gate-org-chart`](concepts/agent-five-gate-org-chart.md) | draft | Five-gate org chart — Intake through Memo (K98 Post 1) |
| [`mcp-server-catalog-curation`](concepts/mcp-server-catalog-curation.md) | draft | MCP catalog curation — exploraX USB-C model (K98 Post 10) |
| [`seclaw-agent-security-evaluation`](concepts/seclaw-agent-security-evaluation.md) | draft | SeClaw trajectory-aware agent security eval (2606.02302, K98) |
| [`agent-skills-progressive-disclosure`](concepts/agent-skills-progressive-disclosure.md) | draft | SKILL.md 3-level loading + skills vs MCP (2602.12430) |
| [`interaction-native-knowledge-harness`](concepts/interaction-native-knowledge-harness.md) | draft | InKH passive injection + wiki audit (2606.01886, OSINT handoff) |
| [`muse-autoskill-skill-lifecycle`](concepts/muse-autoskill-skill-lifecycle.md) | draft | MUSE skill create/eval/refine lifecycle — 2605.27366 |
| [`skilladaptor-step-level-skill-adaptation`](concepts/skilladaptor-step-level-skill-adaptation.md) | draft | Step-level skill adaptation from failed trajectories — 2606.01311 |
| [`mcp-server-runtime-fault-taxonomy`](concepts/mcp-server-runtime-fault-taxonomy.md) | draft | MCP server runtime fault taxonomy — 11 categories, 837 threads — 2606.05339 |
| [`retrospective-harness-optimization-rho`](concepts/retrospective-harness-optimization-rho.md) | draft | RHO — label-free harness evolution via self-preference — 2606.05922 |
| [`agent-backpressure-loop`](concepts/agent-backpressure-loop.md) | draft | Backpressure flow control for coding agents — @bibryam K103 |
| [`rl-agent-labs-system-prompt-learning`](concepts/rl-agent-labs-system-prompt-learning.md) | draft | RL agent labs 2026 — system-prompt as trainable artifact — K103 |
| [`long-thread-context-decay`](concepts/long-thread-context-decay.md) | draft | Long-thread quality degradation mitigations — @hooeem K103 |
| [`time-series-native-agent-harness`](concepts/time-series-native-agent-harness.md) | draft | Modality workspace harness — TimeClaw 2606.05404 |
| [`the-hive-loop-routines-pattern`](concepts/the-hive-loop-routines-pattern.md) | draft | Loops + Routines + ant cron — K108 |
| [`ship-subagent-writer-reviewer-tester`](concepts/ship-subagent-writer-reviewer-tester.md) | draft | /ship writer·reviewer·tester pattern — K108 |
| [`autosci-memory-centric-research-agents`](concepts/autosci-memory-centric-research-agents.md) | draft | AutoSci SciMem research lifecycle — 2605.31468 |
| [`maven-agentic-tool-calling-generalization`](concepts/maven-agentic-tool-calling-generalization.md) | draft | MAVEN tool-calling generalization — 2605.30738 |
| [`failed-trajectory-harness-repair`](concepts/failed-trajectory-harness-repair.md) | validated | HarnessFix — diagnosis-first harness repair (2606.06324) |
| [`etclovg-harness-layers`](concepts/etclovg-harness-layers.md) | validated | ETCLOVG seven-layer harness taxonomy (K100) |
| [`agentic-memory-cross-scenario-generality`](concepts/agentic-memory-cross-scenario-generality.md) | draft | AutoMEM cross-scenario memory — OSINT-primary stub (2606.04315) |
| [`worldmemarena-multimodal-agent-memory-eval`](concepts/worldmemarena-multimodal-agent-memory-eval.md) | draft | WorldMemArena memory eval — 2605.29341 |
| [`decoupled-intelligence-multi-agent-reference`](concepts/decoupled-intelligence-multi-agent-reference.md) | draft | Traffic multi-agent — REFERENCE only (2605.27685) |
| [`skillrae-retrieval-augmented-execution`](concepts/skillrae-retrieval-augmented-execution.md) | draft | Skill-graph RAE — post-retrieval context compilation (K59 arXiv) |
| [`graphflow-verifiable-agent-workflows`](concepts/graphflow-verifiable-agent-workflows.md) | draft | Proof-carrying visual workflows + durable runtime (K59 arXiv) |
| [`runtime-harness-interface-adaptation`](concepts/runtime-harness-interface-adaptation.md) | draft | LIFE-HARNESS — adapt interface not model (2605.22166, K95) |
| [`adaptive-auto-harness-open-ended-streams`](concepts/adaptive-auto-harness-open-ended-streams.md) | draft | Stream harness tree + anti-overfit (2606.01770, K95) |
| [`embedded-agent-modular-edge-architecture`](concepts/embedded-agent-modular-edge-architecture.md) | draft | Edge agent tiers + governance layer — REFERENCE (2606.02862, K95) |
| [`slm-agent-orchestration-gateway`](concepts/slm-agent-orchestration-gateway.md) | draft | Intent router + service registry pattern (2606.03557, K95) |
| [`failure-mode-harness-adaptation-mapping`](concepts/failure-mode-harness-adaptation-mapping.md) | draft | Five-axis failure taxonomy → context/tool/loop adaptation strategies; SLM cost-recovery framework — 2607.08938 (K168) |
| [`harness-evolution-vs-test-time-scaling-baseline`](concepts/harness-evolution-vs-test-time-scaling-baseline.md) | draft | Evaluation-rigor checklist — harness evolution vs. parallel-sampling/sequential-refinement at matched budget — 2607.12227 (K169) |

## sources/

| Page | Maturity | Summary |
|------|----------|---------|
| [`arxiv-skillrae-2605.10114`](sources/arxiv-skillrae-2605.10114.md) | draft | SkillRAE paper provenance (K59) |
| [`arxiv-graphflow-2605.14968`](sources/arxiv-graphflow-2605.14968.md) | draft | GraphFlow paper provenance (K59) |
| [`k67-explorax-100-repos-reference`](sources/k67-explorax-100-repos-reference.md) | draft | @exploraX_ OSS list — audit queue stub (K67) |
| [`trading-posts-compilation-20-2026-05-27`](sources/trading-posts-compilation-20-2026-05-27.md) | draft | K69 Posts.docx CCC slice — provenance stub (OSINT canon) |
| [`trading-posts-compilation-25-2026-05-27`](sources/trading-posts-compilation-25-2026-05-27.md) | draft | K72 Posts.docx — provenance stub (OSINT canon) |
| [`arxiv-continual-harness-self-improving-agents-2605.09998`](sources/arxiv-continual-harness-self-improving-agents-2605.09998.md) | draft | Continual Harness paper — unread-stub (K72) |
| [`trading-posts-compilation-38-2026-05-28`](sources/trading-posts-compilation-38-2026-05-28.md) | draft | K73 Posts.docx — provenance stub (OSINT canon) |
| [`multi-wiki-tool-eval-25url-2026-05-28`](sources/multi-wiki-tool-eval-25url-2026-05-28.md) | draft | K73 25-URL eval — provenance stub (OSINT canon) |
| [`trading-posts-macro-charts-skills-md-2026-05-28`](sources/trading-posts-macro-charts-skills-md-2026-05-28.md) | draft | K76 Posts.docx — provenance stub (OSINT canon) |
| [`trading-posts-compilation-6-2026-05-29`](sources/trading-posts-compilation-6-2026-05-29.md) | draft | K78 Posts.docx CCC slice — provenance stub (OSINT canon) |
| [`trading-posts-compilation-k84-2026-05-30`](sources/trading-posts-compilation-k84-2026-05-30.md) | draft | K84 Posts.docx Codex harness slice — provenance stub (OSINT canon) |
| [`multi-wiki-tool-eval-v5-k88-2026-05-31`](sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md) | draft | K88 v5 eval (29 URLs) — provenance stub (OSINT canon) |
| [`trading-posts-compilation-42-2026-05-31`](sources/trading-posts-compilation-42-2026-05-31.md) | draft | K88 Posts.docx harness slice — provenance stub (OSINT canon) |
| [`multi-wiki-tool-eval-v6-k90-2026-05-31`](sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md) | draft | K90 v6 eval (41 URLs) — provenance stub (OSINT canon) |
| [`trading-posts-compilation-16-2026-05-31`](sources/trading-posts-compilation-16-2026-05-31.md) | draft | K90 Posts.docx harness slice — provenance stub (OSINT canon) |
| [`multi-wiki-tool-eval-v7-k92-2026-06-01`](sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md) | draft | K92 v7 eval (90 URLs) — provenance stub (OSINT canon) |
| [`trading-posts-compilation-12-2026-06-01`](sources/trading-posts-compilation-12-2026-06-01.md) | draft | K92 Posts.docx harness slice — provenance stub (OSINT canon) |
| [`multi-wiki-tool-eval-v5-k93-2026-06-01`](sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md) | draft | K93 v5 eval (34 URLs) — provenance stub (OSINT canon) |
| [`trading-posts-compilation-31-2026-06-01`](sources/trading-posts-compilation-31-2026-06-01.md) | draft | K93 Posts.docx harness slice — provenance stub (OSINT canon) |
| [`arxiv-harness-updating-not-benefit-2605.30621`](sources/arxiv-harness-updating-not-benefit-2605.30621.md) | draft | arXiv 2605.30621 harness paper (K93) |
| [`monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01`](sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md) | draft | Monokern pipeline source (K93) |
| [`arxiv-system-scaling-harness-2605.26112`](sources/arxiv-system-scaling-harness-2605.26112.md) | draft | System scaling the harness — arXiv 2605.26112 |
| [`arxiv-runtime-harness-adaptation-2605.22166`](sources/arxiv-runtime-harness-adaptation-2605.22166.md) | draft | Runtime harness adaptation — K95 |
| [`arxiv-adaptive-auto-harness-2606.01770`](sources/arxiv-adaptive-auto-harness-2606.01770.md) | draft | Adaptive auto-harness — K95 |
| [`arxiv-embedded-agent-modular-edge-2606.02862`](sources/arxiv-embedded-agent-modular-edge-2606.02862.md) | draft | Embedded modular agents — K95 |
| [`arxiv-agentxgcore-mobile-core-2606.00417`](sources/arxiv-agentxgcore-mobile-core-2606.00417.md) | draft | AgentXGCore mobile — K95 |
| [`arxiv-slm-orchestration-gateway-2606.03557`](sources/arxiv-slm-orchestration-gateway-2606.03557.md) | draft | SLM orchestration gateway — K95 |
| [`arxiv-cli-anything-2606-03854-2026-06-03`](sources/arxiv-cli-anything-2606-03854-2026-06-03.md) | draft | CLI-Anything — K95 OSINT |
| [`trading-posts-compilation-17-2026-06-03`](sources/trading-posts-compilation-17-2026-06-03.md) | draft | K97 Posts.docx harness slice — provenance (OSINT canon) |
| [`trading-posts-compilation-18-2026-06-04`](sources/trading-posts-compilation-18-2026-06-04.md) | draft | K98 Posts.docx harness slice — provenance (OSINT canon) |
| [`arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04`](sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md) | draft | SeClaw agent security — K98 OSINT |
| [`arxiv-agent-skills-architecture-security-2602.12430`](sources/arxiv-agent-skills-architecture-security-2602.12430.md) | draft | Agent Skills architecture/security survey — 2602.12430 |
| [`arxiv-interaction-native-knowledge-harness-2606.01886`](sources/arxiv-interaction-native-knowledge-harness-2606.01886.md) | draft | InKH financial knowledge harness — 2606.01886 (OSINT handoff) |
| [`arxiv-muse-autoskill-2605.27366`](sources/arxiv-muse-autoskill-2605.27366.md) | draft | MUSE-Autoskill skill lifecycle — arXiv 2605.27366 |
| [`arxiv-autosci-2605.31468`](sources/arxiv-autosci-2605.31468.md) | draft | AutoSci memory-centric research — arXiv 2605.31468 |
| [`arxiv-sia-harness-weight-updates-2605.27276`](sources/arxiv-sia-harness-weight-updates-2605.27276.md) | draft | SIA — OSINT cross-wiki stub (K84 canon) |
| [`arxiv-maven-agentic-tool-calling-2605.30738`](sources/arxiv-maven-agentic-tool-calling-2605.30738.md) | draft | MAVEN tool calling — 2605.30738 (read) |
| [`arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05`](sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md) | draft | HarnessFix harness repair — 2606.06324 (deep-read) |
| [`arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05`](sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md) | draft | Agentic memory cross-scenario — 2606.04315 (read) |
| [`arxiv-worldmemarena-agent-memory-2605.29341`](sources/arxiv-worldmemarena-agent-memory-2605.29341.md) | draft | WorldMemArena — 2605.29341 |
| [`arxiv-agyn-agent-platform-2605.27575`](sources/arxiv-agyn-agent-platform-2605.27575.md) | draft | Agyn platform — 2605.27575 |
| [`arxiv-agent-skills-survey-2605-07358-2026-06-02`](sources/arxiv-agent-skills-survey-2605-07358-2026-06-02.md) | draft | Agent skills taxonomy survey — K94 OSINT |
| [`arxiv-tool-forge-governed-agentic-2605-28000-2026-06-02`](sources/arxiv-tool-forge-governed-agentic-2605-28000-2026-06-02.md) | draft | Tool Forge — K94 OSINT |
| [`arxiv-decoupled-intelligence-multi-agent-2605.27685`](sources/arxiv-decoupled-intelligence-multi-agent-2605.27685.md) | draft | Decoupled Intelligence — 2605.27685 |
| [`arxiv-agent-skills-survey-2605.07358-2026-06-02`](sources/arxiv-agent-skills-survey-2605.07358-2026-06-02.md) | draft | Agent skills taxonomy survey — K94 OSINT mirror |
| [`arxiv-tool-forge-governed-agentic-2605.28000-2026-06-02`](sources/arxiv-tool-forge-governed-agentic-2605.28000-2026-06-02.md) | draft | Tool Forge governed toolchain — K94 OSINT mirror |
| [`arxiv-runtime-harness-adaptation-2605.22166`](sources/arxiv-runtime-harness-adaptation-2605.22166.md) | draft | LIFE-HARNESS runtime interface adaptation — K95 |
| [`arxiv-adaptive-auto-harness-2606.01770`](sources/arxiv-adaptive-auto-harness-2606.01770.md) | draft | Adaptive Auto-Harness open-ended streams — K95 |
| [`arxiv-agentxgcore-mobile-core-2606.00417`](sources/arxiv-agentxgcore-mobile-core-2606.00417.md) | draft | AgentxGCore 6G core — REFERENCE only (K95) |
| [`arxiv-embedded-agent-modular-edge-2606.02862`](sources/arxiv-embedded-agent-modular-edge-2606.02862.md) | draft | Embedded agent modular edge architecture — K95 |
| [`arxiv-slm-orchestration-gateway-2606.03557`](sources/arxiv-slm-orchestration-gateway-2606.03557.md) | draft | SLM orchestration gateway — K95 |
| [`arxiv-skilladaptor-2606.01311`](sources/arxiv-skilladaptor-2606.01311.md) | draft | SkillAdaptor step-level skill adaptation — 2606.01311 (read) |
| [`arxiv-mcp-runtime-fault-taxonomy-2606.05339`](sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md) | draft | MCP server runtime fault taxonomy — 2606.05339 (read) |
| [`multi-wiki-tool-eval-50url-k102-2026-06-06`](sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md) | draft | K102 50-URL eval — CCC harness slice |
| [`arxiv-retrospective-harness-optimization-2606.05922`](sources/arxiv-retrospective-harness-optimization-2606.05922.md) | draft | RHO retrospective harness optimization — 2606.05922 (read) |
| [`multi-wiki-tool-eval-v8-k103-2026-06-07`](sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md) | draft | K103 63-URL eval — CCC harness slice (OSINT canon) |
| [`trading-posts-compilation-19-2026-06-07`](sources/trading-posts-compilation-19-2026-06-07.md) | draft | K103 Posts.docx harness cluster — provenance stub |
| [`arxiv-timeclaw-contextualized-time-series-2606.05404`](sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md) | draft | TimeClaw contextualized time series — 2606.05404 (read) |
| [`trading-posts-compilation-8-2026-06-09`](sources/trading-posts-compilation-8-2026-06-09.md) | draft | K108 Posts — HIVE / ship / omnifs slice |
| [`arxiv-agent-harness-operational-definition-2606.10106`](sources/arxiv-agent-harness-operational-definition-2606.10106.md) | draft | Agent harness operational definition — read (K109) |
| [`arxiv-mcp-externalizing-context-survey-2508.19239`](sources/arxiv-mcp-externalizing-context-survey-2508.19239.md) | draft | MCP adaptive-systems survey — skimmed (K109) |
| [`arxiv-openagenet-oan-white-paper-2606.03161`](sources/arxiv-openagenet-oan-white-paper-2606.03161.md) | draft | OpenAgenet / OAN white paper — read (K109) |
| [`arxiv-queen-bee-beespec-enterprise-mcp-2606.06545`](sources/arxiv-queen-bee-beespec-enterprise-mcp-2606.06545.md) | draft | Queen-Bee BeeSpec enterprise MCP — read (K109) |
| [`arxiv-bayesian-agent-posterior-skill-evolution-2606.08348`](sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md) | draft | Bayesian-Agent skill evolution — read (K109) |
| [`arxiv-autonomous-hyperscale-incident-resolution-2606.09122`](sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md) | draft | Autonomous hyperscale incident resolution — read (K109) |
| [`arxiv-self-harness-improve-themselves-2606.09498`](sources/arxiv-self-harness-improve-themselves-2606.09498.md) | draft | Self-Harness — read (K110) |
| [`arxiv-enterprise-mcp-adoption-2606.09182`](sources/arxiv-enterprise-mcp-adoption-2606.09182.md) | draft | Enterprise MCP adoption interviews — read (K110) |
| [`arxiv-channel-fracture-cross-agent-memory-2606.04896`](sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md) | draft | Channel fracture Hermes cron memory — read (K111) |
| [`arxiv-skillhone-continual-skill-evolution-2606.08671`](sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md) | draft | SkillHone continual skill evolution — read (K111) |
| [`arxiv-parthenon-law-self-evolving-legal-agent-2606.04602`](sources/arxiv-parthenon-law-self-evolving-legal-agent-2606.04602.md) | draft | Parthenon six-layer legal harness + self-evolving loop — read (K114) |
| [`arxiv-perspectivegap-multi-agent-orchestration-2606.08878`](sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md) | draft | PerspectiveGap orchestration prompting benchmark — read (K114) |
| [`arxiv-internet-of-agentic-ai-2606.12835`](sources/arxiv-internet-of-agentic-ai-2606.12835.md) | draft | Internet of Agentic AI vision survey — skimmed (K114) |
| [`arxiv-agents-k1-knowledge-orchestration-2606.13669`](sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md) | draft | Agents-K1 agent-native KG — skimmed (K114) |
| [`arxiv-less-context-better-agents-2606.10209`](sources/arxiv-less-context-better-agents-2606.10209.md) | draft | Less Context Better Agents MCP study — read (K115) |
| [`arxiv-agents-all-the-way-down-2606.11869`](sources/arxiv-agents-all-the-way-down-2606.11869.md) | draft | Agents All the Way Down methodology — read (K115) |
| [`arxiv-multi-factor-agentic-memory-2606.12945`](sources/arxiv-multi-factor-agentic-memory-2606.12945.md) | draft | Multi-factor agentic memory — read (K115) |
| [`arxiv-recursive-agent-harnesses-2606.13643`](sources/arxiv-recursive-agent-harnesses-2606.13643.md) | draft | Recursive Agent Harnesses — read (K115) |
| [`arxiv-orch-rm-multi-agent-orchestration-2606.13598`](sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md) | draft | Orch-RM orchestration reward modeling — read (K116) |
| [`arxiv-harnessx-composable-harness-foundry-2606.14249`](sources/arxiv-harnessx-composable-harness-foundry-2606.14249.md) | draft | HarnessX composable harness foundry — read (K116) |
| [`arxiv-llm-as-code-agentic-programming-2606.15874`](sources/arxiv-llm-as-code-agentic-programming-2606.15874.md) | draft | LLM-as-Code agentic programming — read (K116) |
| [`arxiv-memrefine-storage-budgeted-memory-2606.13177`](sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md) | draft | MemRefine storage-budgeted memory — read (K117) |
| [`arxiv-seagym-self-evolving-harness-eval-2606.17546`](sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md) | draft | SEAGym harness eval environment — read (K117) |
| [`arxiv-finacumen-experience-memory-harness-2606.17642`](sources/arxiv-finacumen-experience-memory-harness-2606.17642.md) | draft | FinAcumen experience memory — read (K117, osint route) |
| [`arxiv-specification-to-execution-scientific-workflow-2606.18425`](sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md) | draft | Pegasus spec-driven scientific workflow — read (K118) |
| [`arxiv-agent-first-web-redesign-2606.19116`](sources/arxiv-agent-first-web-redesign-2606.19116.md) | draft | Agent-first web vision — read (K119) |
| [`arxiv-agentic-eda-handoff-2606.19795`](sources/arxiv-agentic-eda-handoff-2606.19795.md) | draft | EDA handoff validity survey — read (K119) |
| [`arxiv-user-as-code-executable-memory-2606.16707`](sources/arxiv-user-as-code-executable-memory-2606.16707.md) | draft | User as Code executable memory — read (K120) |
| [`arxiv-dynamo-topological-orchestration-2606.19382`](sources/arxiv-dynamo-topological-orchestration-2606.19382.md) | draft | DynAMO topological orchestration — read (K120) |
| [`arxiv-tokenpilot-cache-efficient-context-2606.17016`](sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md) | draft | TokenPilot cache context management — read (K121) |
| [`arxiv-safeclawbench-staged-agent-security-2606.18356`](sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md) | draft | SafeClawBench staged security — read (K121) |
| [`arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422`](sources/arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422.md) | draft | Gatekeeper layered eval — skimmed (K121) |
| [`arxiv-xcientist-research-harness-claim-drift-2606.18874`](sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md) | draft | XCIENTIST research harness — read (K122) |
| [`arxiv-data-intelligence-agents-dia-2606.19319`](sources/arxiv-data-intelligence-agents-dia-2606.19319.md) | draft | DIA enterprise data ACA — read (K123) |
| [`arxiv-dual-agent-cross-model-protocol-translation-2606.20120`](sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md) | draft | Cross-model protocol translation — read (K123) |
| [`arxiv-agentic-web-infrastructure-agentverse-2606.20570`](sources/arxiv-agentic-web-infrastructure-agentverse-2606.20570.md) | draft | Agentic web gap analysis — read (K123) |
| [`arxiv-aohp-os-level-agent-harness-2606.23449`](sources/arxiv-aohp-os-level-agent-harness-2606.23449.md) | draft | AOHP Android harness — read (K123) |
| [`arxiv-agent-harness-survey-2606.20683`](sources/arxiv-agent-harness-survey-2606.20683.md) | draft | Agent harness design survey — read (K124) |
| [`arxiv-fara-scalable-cua-environments-2606.20785`](sources/arxiv-fara-scalable-cua-environments-2606.20785.md) | draft | Fara-1.5 CUA pipeline — read (K124) |
| [`arxiv-bioinsight-multi-agent-biomedical-2606.20997`](sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md) | draft | BioInsight multi-agent biomedical UI — read (K124) |
| [`arxiv-paperclaw-autonomous-research-2606.22610`](sources/arxiv-paperclaw-autonomous-research-2606.22610.md) | draft | PaperClaw research lifecycle — read (K124) |
| [`arxiv-procedural-memory-after-2606.23127`](sources/arxiv-procedural-memory-after-2606.23127.md) | draft | AFTER procedural memory benchmark — read (K124) |
| [`arxiv-self-compacting-agents-2606.23525`](sources/arxiv-self-compacting-agents-2606.23525.md) | draft | SelfCompact adaptive context — read (K124) |
| [`arxiv-metis-text-code-memory-2606.24151`](sources/arxiv-metis-text-code-memory-2606.24151.md) | draft | Metis dual memory — read (K124) |
| [`arxiv-trust-as-a-service-mcp-2604.07065`](sources/arxiv-trust-as-a-service-mcp-2604.07065.md) | draft | TaaS MCP trust — read (K125) |
| [`arxiv-vadaorchestra-neurosymbolic-2606.22485`](sources/arxiv-vadaorchestra-neurosymbolic-2606.22485.md) | draft | VADAOrchestra — read (K125) |
| [`arxiv-esaa-conversational-event-sourced-2606.23752`](sources/arxiv-esaa-conversational-event-sourced-2606.23752.md) | draft | ESAA handoff — read (K125) |
| [`arxiv-governed-shared-memory-2606.24535`](sources/arxiv-governed-shared-memory-2606.24535.md) | draft | MemClaw fleet memory — read (K125) |
| [`brief-k125-memory-orchestration-cluster-2026-06-25`](sources/brief-k125-memory-orchestration-cluster-2026-06-25.md) | validated | K125 prod brief stub |
| [`brief-k125-vadaorchestra-osint-handoff-2026-06-25`](sources/brief-k125-vadaorchestra-osint-handoff-2026-06-25.md) | validated | K125 OSINT handoff stub |
| [`brief-k125-memclaw-fleet-governance-handoff-2026-06-25`](sources/brief-k125-memclaw-fleet-governance-handoff-2026-06-25.md) | validated | K125 cybersec handoff stub |
| [`arxiv-memprobe-hidden-user-state-recovery-2606.24595`](sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md) | draft | MemProbe recovery audit — read (K128) |
| [`brief-k128-memprobe-memory-recovery-2026-06-26`](sources/brief-k128-memprobe-memory-recovery-2026-06-26.md) | validated | K128 prod brief stub |
| [`arxiv-toolbench-x-tool-environment-unreliability-2606.25819`](sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md) | draft | ToolBench-X hazards — read (K129) |
| [`arxiv-confidence-aware-tool-orchestration-video-2606.26904`](sources/arxiv-confidence-aware-tool-orchestration-video-2606.26904.md) | draft | Robust-TO orchestration — read (K129) |
| [`brief-k129-tool-reliability-orchestration-2026-06-27`](sources/brief-k129-tool-reliability-orchestration-2026-06-27.md) | validated | K129 prod brief stub |
| [`brief-k129-robust-to-imagegen-handoff-2026-06-27`](sources/brief-k129-robust-to-imagegen-handoff-2026-06-27.md) | validated | K129 image-gen handoff stub |
| [`brief-k124-harness-memory-research-cluster-2026-06-24`](sources/brief-k124-harness-memory-research-cluster-2026-06-24.md) | validated | K124 prod brief stub |
| [`brief-k124-harness-policy-hands-on-2026-06-24`](sources/brief-k124-harness-policy-hands-on-2026-06-24.md) | validated | K124 policy brief stub |
| [`brief-k115-context-memory-recursion-prod-2026-06-15`](sources/brief-k115-context-memory-recursion-prod-2026-06-15.md) | validated | K115 prod brief stub |
| [`brief-k116-orchrm-harnessx-llm-as-code-prod-2026-06-16`](sources/brief-k116-orchrm-harnessx-llm-as-code-prod-2026-06-16.md) | validated | K116 prod brief stub |
| [`brief-k117-memory-seagym-finacumen-prod-2026-06-17`](sources/brief-k117-memory-seagym-finacumen-prod-2026-06-17.md) | validated | K117 prod brief stub |
| [`brief-k118-spec-driven-pegasus-workflow-prod-2026-06-18`](sources/brief-k118-spec-driven-pegasus-workflow-prod-2026-06-18.md) | validated | K118 prod brief stub |
| [`brief-k119-agent-first-web-eda-handoff-prod-2026-06-19`](sources/brief-k119-agent-first-web-eda-handoff-prod-2026-06-19.md) | validated | K119 prod brief stub |
| [`brief-k120-user-as-code-dynamo-prod-2026-06-20`](sources/brief-k120-user-as-code-dynamo-prod-2026-06-20.md) | validated | K120 prod brief stub |
| [`brief-k121-tokenpilot-safeclaw-gatekeepers-prod-2026-06-21`](sources/brief-k121-tokenpilot-safeclaw-gatekeepers-prod-2026-06-21.md) | validated | K121 prod brief stub |
| [`brief-k122-xcientist-claim-drift-prod-2026-06-22`](sources/brief-k122-xcientist-claim-drift-prod-2026-06-22.md) | validated | K122 prod brief stub |
| [`brief-k126-nvidia-mattpocock-skills-adopt-2026-06-22`](sources/brief-k126-nvidia-mattpocock-skills-adopt-2026-06-22.md) | validated | K126 skills adopt brief stub |
| [`brief-k127-aohp-secure-agent-interfaces-reference-2026-06-23`](sources/brief-k127-aohp-secure-agent-interfaces-reference-2026-06-23.md) | validated | K127 AOHP reference brief stub |
| [`brief-k125-esaa-windows-handoff-2026-06-25`](sources/brief-k125-esaa-windows-handoff-2026-06-25.md) | validated | K125 ESAA Windows handoff stub |
| [`brief-k123-dia-agentic-web-aohp-2026-06-23`](sources/brief-k123-dia-agentic-web-aohp-2026-06-23.md) | validated | K123 prod brief stub |
| [`eval-github-repos-plan-multi-wiki-2026-06-29`](sources/eval-github-repos-plan-multi-wiki-2026-06-29.md) | validated | K134 multi-wiki eval — CCC routing stub |
| [`brief-k134-codebase-memory-cursor-federation-prod-2026-06-29`](sources/brief-k134-codebase-memory-cursor-federation-prod-2026-06-29.md) | validated | K134 prod brief stub |
| [`arxiv-clarus-scientific-collaboration-infrastructure-2606.30246`](sources/arxiv-clarus-scientific-collaboration-infrastructure-2606.30246.md) | draft | Clarus collaboration — read (K135) |
| [`brief-k135-clarus-research-collaboration-2026-06-30`](sources/brief-k135-clarus-research-collaboration-2026-06-30.md) | validated | K135 prod brief stub |
| [`arxiv-agentic-orchestration-options-abpm-2606.31518`](sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md) | draft | ABPM OO1–OO4 orchestration — read (K136) |
| [`brief-k136-agentic-orchestration-options-abpm-2026-07-01`](sources/brief-k136-agentic-orchestration-options-abpm-2026-07-01.md) | validated | K136 prod brief stub |
| [`arxiv-automem-metamemory-cognitive-skill-2607.01224`](sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md) | draft | AutoMem metamemory — read (K137) |
| [`brief-k137-automem-metamemory-cognitive-skill-2026-07-02`](sources/brief-k137-automem-metamemory-cognitive-skill-2026-07-02.md) | validated | K137 prod brief stub |
| [`arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389`](sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md) | draft | Steerability via constraints — read (K138) |
| [`brief-k138-substrate-constraints-agent-oversight-2026-07-07`](sources/brief-k138-substrate-constraints-agent-oversight-2026-07-07.md) | validated | K138 prod brief stub |
| [`arxiv-next-gen-agentic-rl-self-evolving-2607.01120`](sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md) | draft | AReaL self-evolving agentic RL — read (K139) |
| [`brief-k139-agentic-online-rl-self-evolving-2026-07-07`](sources/brief-k139-agentic-online-rl-self-evolving-2026-07-07.md) | validated | K139 prod brief stub |
| [`brief-k140-hexstrike-client-orchestration-2026-07-07`](sources/brief-k140-hexstrike-client-orchestration-2026-07-07.md) | validated | K140 HexStrike handoff brief stub |
| [`arxiv-shopx-intent-to-item-fulfillment-2606.31693`](sources/arxiv-shopx-intent-to-item-fulfillment-2606.31693.md) | draft | ShopX model-native fulfillment — skimmed (K141) |
| [`arxiv-large-cancer-assistant-lca-2607.06531`](sources/arxiv-large-cancer-assistant-lca-2607.06531.md) | draft | LCA impermeability + SIP — read (K150) |
| [`brief-k150-algorithmic-impermeability-orchestration-2026-07-09`](sources/brief-k150-algorithmic-impermeability-orchestration-2026-07-09.md) | validated | K150 prod brief stub |
| [`arxiv-cage-1-enterprise-agentic-governance-2607.03510`](sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md) | draft | CAGE-1 Prebind Assurance — read (K151) |
| [`brief-k151-cage-1-enterprise-agent-governance-2026-07-10`](sources/brief-k151-cage-1-enterprise-agent-governance-2026-07-10.md) | validated | K151 prod + David adopt brief stub |
| [`arxiv-polyworkbench-multilingual-long-horizon-2607.06008`](sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md) | draft | PolyWorkBench benchmark — read (K152) |
| [`brief-k152-polyworkbench-multilingual-agent-eval-2026-07-10`](sources/brief-k152-polyworkbench-multilingual-agent-eval-2026-07-10.md) | validated | K152 prod brief stub |
| [`arxiv-miles-modular-instruction-memory-2607.06974`](sources/arxiv-miles-modular-instruction-memory-2607.06974.md) | draft | MILES learnable selection — read (K153) |
| [`brief-k153-miles-modular-instruction-memory-2026-07-13`](sources/brief-k153-miles-modular-instruction-memory-2026-07-13.md) | validated | K153 prod brief stub |
| [`arxiv-ensemble-qsp-hierarchical-memory-2607.07666`](sources/arxiv-ensemble-qsp-hierarchical-memory-2607.07666.md) | draft | Ensemble QSP hierarchical memory — read (K154) |
| [`brief-k154-hierarchical-bounded-agent-memory-2026-07-13`](sources/brief-k154-hierarchical-bounded-agent-memory-2026-07-13.md) | validated | K154 prod brief stub |
| [`arxiv-deepsearch-world-self-distillation-2607.07820`](sources/arxiv-deepsearch-world-self-distillation-2607.07820.md) | draft | DeepSearch-World — read (K156) |
| [`brief-k156-deepsearch-world-verifiable-search-2026-07-13`](sources/brief-k156-deepsearch-world-verifiable-search-2026-07-13.md) | validated | K156 prod brief stub |
| [`arxiv-trustx-agent-risk-classification-2607.09586`](sources/arxiv-trustx-agent-risk-classification-2607.09586.md) | draft | TrustX ARC — read (K157) |
| [`brief-k157-trustx-agent-risk-classification-2026-07-13`](sources/brief-k157-trustx-agent-risk-classification-2026-07-13.md) | validated | K157 prod + David adopt stub |
| [`arxiv-recursive-self-improvement-survey-2607.07663`](sources/arxiv-recursive-self-improvement-survey-2607.07663.md) | draft | RSI survey verification hierarchy — read (K162) |
| [`brief-k162-rsi-verification-hierarchy-2026-07-14`](sources/brief-k162-rsi-verification-hierarchy-2026-07-14.md) | validated | K162 prod brief stub |
| [`arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138`](sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md) | draft | Hierarchical skill stack — read (K164) |
| [`brief-k164-hierarchical-skill-stack-lazy-orchestration-2026-07-14`](sources/brief-k164-hierarchical-skill-stack-lazy-orchestration-2026-07-14.md) | validated | K164 prod + David + poker stub |
| [`brief-k109-bayesian-agent-harness-cluster-prod-2026-06-10`](sources/brief-k109-bayesian-agent-harness-cluster-prod-2026-06-10.md) | validated | K109 prod brief stub |
| [`brief-k132-local-adoptions-cursor-federation-prod-2026-06-27`](sources/brief-k132-local-adoptions-cursor-federation-prod-2026-06-27.md) | validated | K132 prod brief stub |
| [`brief-k122-k126-federation-cursor-harness-adoptions-2026-06-25`](sources/brief-k122-k126-federation-cursor-harness-adoptions-2026-06-25.md) | validated | K122–K126 federation batch brief stub |
| [`arxiv-better-harnesses-smaller-models-2607.08938`](sources/arxiv-better-harnesses-smaller-models-2607.08938.md) | draft | Building 90% cheaper agents via automated harness adaptation — read (K168) |
| [`brief-k168-slm-harness-adaptation-2026-07-15`](sources/brief-k168-slm-harness-adaptation-2026-07-15.md) | validated | K168 prod + David + poker stub |
| [`arxiv-rethinking-harness-evolution-evaluation-2607.12227`](sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md) | draft | Rethinking evaluation of harness evolution — read (K169) |
| [`brief-k169-harness-adaptation-evaluation-rigor-prod-2026-07-15`](sources/brief-k169-harness-adaptation-evaluation-rigor-prod-2026-07-15.md) | validated | K168+K169 combined rigor prod stub |
| [`brief-k169-harness-evolution-eval-discipline-2026-07-15`](sources/brief-k169-harness-evolution-eval-discipline-2026-07-15.md) | validated | K169 eval-discipline prod stub |

## meta/

| Page | Maturity | Summary |
|------|----------|---------|
| [`daily-research-digest-cadence`](meta/daily-research-digest-cadence.md) | core | CCC LaunchAgent + sweeps cadence (K93) |
| [`ccc-cross-wiki-handoff-briefs`](meta/ccc-cross-wiki-handoff-briefs.md) | validated | Catalog of `wiki/briefs/` cybersec/OSINT handoffs |

## sweeps/

| Page | Summary |
|------|---------|
| [`2026-06-01-daily`](sweeps/2026-06-01-daily.md) | First digest run — 3 arXiv ingested |
| [`2026-06-02-daily`](sweeps/2026-06-02-daily.md) | 5 arXiv fetched — full ingest 2026-06-02 |

## entities/people/

| Page | Maturity | Summary |
|------|----------|---------|
| [`damidefi`](entities/people/damidefi.md) | draft | X author — Obsidian + Claude workflow posts (K69, K78) |

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
| `entities/skills/cursor-audit.md` | [agent-toolkit-demo/skills/cursor-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/cursor-audit) | Multi-model Cursor audit skill; public distro + CCC/OSINT mirrors (2026-06-06) |
| `entities/skills/super-audit.md` | [agent-toolkit-demo/skills/super-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit) | Five-model super audit; public distro + CCC/OSINT mirrors (2026-06-09) |
| `concepts/cross-wiki-tool-eval-inventory.md` | `@osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md` | Cross-wiki routing pattern (K45–K56) |
| `concepts/code-as-agent-harness.md` | `@osint-wiki/concepts/code-as-agent-harness.md` | K48 arXiv 2605.18747 survey hub |
| `concepts/code-as-agent-harness.md` | `@osint-wiki/sources/arxiv-code-as-agent-harness-survey-2605.18747.md` | Primary source |
| `concepts/self-healing-agent-sessions.md` | `@osint-wiki/sources/arxiv-self-healing-llm-agents-2605.06737.md` | K48 arXiv 2605.06737 |
| `entities/tools/ai-token-monitor.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/codexbar.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/superclaude-framework.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `entities/tools/roo-code.md` | `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` | Cross-wiki tool-eval source (56-repo eval) |
| `concepts/agents-k1-agent-native-knowledge-orchestration.md` | `@osint-wiki/concepts/librarian-server-architecture.md` | KG-at-scale serving implications (K114) |
| `concepts/interaction-native-knowledge-harness.md` | `@osint-wiki/concepts/interaction-native-knowledge-harness.md` | Financial InKH deployment canon |

## Concepts

- [ADK Arena — agent framework benchmark (OSINT handoff)](concepts/adk-arena-agent-framework-benchmark.md) — cross-wiki stub routed from ingest — `cross-wiki`

- [`operator-model-selection`](concepts/operator-model-selection.md) — K142 model routing policy for workflows/subagents.

## Sources

- [Latent Space — Ahmad Osman on why local AI is catching up](sources/newsletter-rss-latent-space-2026-06-30-ahmad-osman-on-why-local-ai-is-catching-up.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — [AINews] not much happened today](sources/newsletter-rss-latent-space-2026-06-30-ainews-not-much-happened-today.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers](sources/newsletter-rss-latent-space-2026-07-01-aiewf-daily-dispatch-loops-software-factories-fo.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — [AINews] Sonnet 5 today, and Fable 5 tomorrow](sources/newsletter-rss-latent-space-2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — Autoresearch: The feedback loop behind self-improving agents](sources/newsletter-rss-latent-space-2026-07-01-autoresearch-the-feedback-loop-behind-self-impro.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — Forward Deployed Engineers and the future of software engineering](sources/newsletter-rss-latent-space-2026-07-01-forward-deployed-engineers-and-the-future-of-sof.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — How Cursor deploys AI inside the enterprise](sources/newsletter-rss-latent-space-2026-07-01-how-cursor-deploys-ai-inside-the-enterprise.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — 🔬 The Coolest Diffusion Research Isn't in LLMs — Evan Feinberg & Sergey Edunov, Genesis Molecular AI](sources/newsletter-rss-latent-space-2026-07-01-the-coolest-diffusion-research-isnt-in-llms-evan.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — Warp CEO Zach Lloyd on why software factories are the next phase of coding](sources/newsletter-rss-latent-space-2026-07-01-warp-ceo-zach-lloyd-on-why-software-factories-ar.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — AIEWF Daily Dispatch: Autoresearch and the tension between AI and human agency](sources/newsletter-rss-latent-space-2026-07-02-aiewf-daily-dispatch-autoresearch-and-the-tensio.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — [AINews] not much happened today](sources/newsletter-rss-latent-space-2026-07-02-ainews-not-much-happened-today.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — Skill engineering and the case against one-shot AI design](sources/newsletter-rss-latent-space-2026-07-02-skill-engineering-and-the-case-against-one-shot.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — The website of the future may assemble itself for every visitor](sources/newsletter-rss-latent-space-2026-07-02-the-website-of-the-future-may-assemble-itself-fo.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — AIEWF Daily Dispatch: The great loops debate and the state of AI engineering](sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — Vercel's Andrew Qu on why agents are a new kind of software](sources/newsletter-rss-latent-space-2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-o.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [The Pragmatic Engineer — Impressions from visiting OpenAI, Anthropic, & Cursor](sources/newsletter-rss-pragmatic-engineer-2026-06-30-impressions-from-visiting-openai-anthropic-curso.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [The Pragmatic Engineer — How Kent Beck shapes the software engineering industry](sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Addy Osmani's Blog — Agentic Autonomy Levels](sources/substack-rss-addy-osmani-2026-07-03-agentic-autonomy-levels.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Latent Space — [AINews] The Field Guide to Fable](sources/newsletter-rss-latent-space-2026-07-07-ainews-the-field-guide-to-fable.md) — cross-wiki stub routed from ingest — `cross-wiki`
