# CCC Wiki — Operations Log

Append-only chronological record of wiki operations: bootstraps, ingests, sweeps, retractions. Newest entries on top.

---

## [2026-06-06] briefs | K102 ingest + backlog processed markers

- **K102** (`briefs/2026-06-06_k102-…`) — wiki: `typst`, `flowforge-skill`, K102 source stub; `scripts/adopt_k102_phase0.sh` (harness plugin PASS; typst not installed)
- **Processed markers** — 9 briefs tagged (k94, k95, k97, k98, inkh/automem handoffs, phase0 trials/scope/trial-plan)
- **Handoffs confirmed** — automem + inkh already in `OSINT WORKSPACE/briefs/`; cybersecurity handoff already in cybersec wiki

## [2026-06-06] phase-0 | SkillAdaptor + MCP fault taxonomy

- **SkillAdaptor** (`zjunlp/SkillAdaptor`): MIT, 6★, README stub only → **NO-GO install**, **REFERENCE** methodology
- **MCP fault taxonomy** (2606.05339): **ADOPT checklist**; figshare replication cited; no tool install
- **Lint:** bidirectional gap fixed (`agentic-memory-cross-scenario-generality` ↔ `failed-trajectory-harness-repair`)

## [2026-06-06] ingest | Daily digest batch — SkillAdaptor + MCP fault taxonomy

- **Preingest:** 2 NEW, 0 DUPLICATE (`arxiv-2606.01311`, `arxiv-2606.05339`)
- **Sources (2):** SkillAdaptor (2606.01311); MCP runtime fault taxonomy (2606.05339)
- **Concepts (2):** `skilladaptor-step-level-skill-adaptation`, `mcp-server-runtime-fault-taxonomy`
- **Pages updated (10):** `muse-autoskill-skill-lifecycle`, `skill-vetting`, `failed-trajectory-harness-repair`, `self-healing-agent-sessions`, `mcp-context-optimization`, `mcp-server-catalog-curation`, `continual-harness-online-self-improvement`, `agent-skills-progressive-disclosure`, `thin-harness-fat-skills-garrytan`, `seclaw-agent-security-evaluation`, `index.md`
- **Cross-wiki:** MCP Security category → `@cybersecurity-wiki/concepts/mcp-security-posture.md` (pointer only)
- **Raw:** PDFs → `raw-sources/`; inbox cleared

## [2026-06-05] deep-read | K100 HarnessFix + memory routing cleanup

- **Deep-read:** arXiv 2606.06324 (HarnessFix) — HTIR, ETCLOVG, repair operators, regression acceptance
- **Read:** arXiv 2606.04315 (AutoMEM / agentic memory); arXiv 2605.30738 MAVEN canonical source bumped to `read`
- **Concepts created/expanded:** `failed-trajectory-harness-repair`, `etclovg-harness-layers`, `agentic-memory-cross-scenario-generality`
- **Dedupe removed:** `agentic-tool-calling-generalization`, duplicate `arxiv-maven-...-2026-06-05` source stub
- **Routing fix:** 2606.04315 is **memory** (OSINT-primary), not tool-calling; dangling link → `@osint-wiki/concepts/exploration-graph-dead-ends.md`
- **Pages updated (10):** `code-as-agent-harness`, `skill-vetting`, `subagent-orchestration`, `seclaw-agent-security-evaluation`, `self-healing-agent-sessions`, `lazy-tool`, `maven-agentic-tool-calling-generalization`, three source pages, `index.md`
- **Brief:** `briefs/2026-06-05_automem-memory-cross-scenario-osint-handoff.md` — OSINT eval handoff for AutoMEM

## [2026-06-05] ingest | K100 federation morning — MAVEN + harness repair batch

- **Sources (3)** — 2605.30738 MAVEN; 2606.04315 cross-scenario generality; 2606.06324 failed-trajectory harness repair
- **Concepts (2)** — `failed-trajectory-harness-repair` (stub → deep-read in follow-up); MAVEN deduped to canonical page
- **Raw** — PDFs → librarian; inbox cleared

## [2026-06-04] adopt | LLM routing DeepSeek → OpenRouter failover

Cross-project routing shipped in OSINT WORKSPACE (`scripts/llm_routing.py`, `config/llm-routing.env.example`, `source_llm_routing_env.sh`, `install_llm_routing_env.sh`). CeminiSuite `deepseek_client.py` wired; poker `cemini_hl_loop.sh` auto-sources env.

- **CCC page:** `concepts/llm-routing-deepseek-openrouter-failover.md`
- **One-time:** `~/.cemini/llm-routing.env` created; `DEEPSEEK_API_KEY` merged from OSINT `.env` — operator still adds `OPENROUTER_API_KEY`

## [2026-06-04] brief → prod | Phase-0 adoption deployment scope

Answer: laptop adoptions **do not** apply across all projects or prod automatically.

**Updated:** `concepts/cross-wiki-tool-adoption-routing.md` — deployment scope table (Mac user vs project vs prod vs librarian).

**Prod brief scp'd:** `briefs/2026-06-04_phase0-adoption-scope-cemini-prod.md` → `cemini-prod:/opt/cemini/briefs/` (7268 bytes). Prod: Phase 1 governance doc + optional skill-scanner trial vs `vet_skill.py`; NO-GO harness/openevolve/Skill_Seekers.

## [2026-06-04] adopt | Full Phase-0 trial run + cross-wiki routing

Nine-tool trial batch in `/tmp/ccc-trials-full-20260604/`; CCC-local adoptions applied.

**Created:** `concepts/cross-wiki-tool-adoption-routing.md`

**Updated:** `skill-vetting` (step 3b skill-scanner), `skillnet`, `scienceaix-agentskills`, `seclaw-agent-security-evaluation`, `revfactory-harness`, `agents-best-practices`, `index.md`

**CCC hands-on:** expanded `.claude/skills/agents-best-practices/references/` (4 files); skill-scanner on all project skills.

**Handoff:** `briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md` → cybersecurity-wiki.

**Blocked:** harness generation (org API); Webwright plugin (SSH clone); defenseclaw sidecar (LLM key).

## [2026-06-04] adopt | Phase-0 GO trials — hands-on installs

Trials run in `/tmp/ccc-adopt-trials-20260604/` + project `.claude/skills/` (gitignored). Verdicts in each entity `## Adoption trial (2026-06-04)`.

| Tool | Trial outcome | Posture |
|------|---------------|---------|
| openevolve | smoke PASS (venv) | ADOPTED smoke tier |
| Webwright | pip + project skill; plugin SSH fail | ADOPTED project skill |
| Skill_Seekers | wiki/concepts export + package zip | ADOPTED CLI workflow |
| revfactory/harness | `harness@harness-marketplace` user plugin | ADOPTED Claude Code plugin |
| agents-best-practices | project skill + wiki steal | ADOPTED cherry-pick |
| defenseclaw | `make all` + skill-scanner | ADOPTED CLI scanners |
| SkillNet / scienceaix / SeClaw | no install (REFERENCE / NO-GO) | unchanged |

**Wiki:** `@concepts/subagent-orchestration.md` — harness control plane steal.

**Artifacts (local):** `/tmp/ccc-adopt-trials-20260604/skill-seekers-out-markdown.zip`; `.claude/skills/{webwright,agents-best-practices}/`.

## [2026-06-04] phase-0 | K88/K93/K98 backlog batch (9 tools)

GitHub API + README skim audits; openevolve smoke via `scripts/openevolve-phase0-smoke.sh`. Verdicts in each page `## Phase-0 Audit (2026-06-04)` section.

| Tool | Verdict | Notes |
|------|---------|-------|
| openevolve | **CONDITIONAL-GO** | Smoke PASS (isolated venv); Docker eval still gated |
| Webwright | **CONDITIONAL-GO** | MIT; Claude Code plugin path only — not Cursor browser replacement |
| Skill_Seekers | **CONDITIONAL-GO** | MIT; one wiki-chapter export trial + vet output before prod skills |
| SkillNet | **CONDITIONAL-GO (REFERENCE)** | MIT; no routing layer until gap vs lazy-tool proven |
| revfactory/harness | **CONDITIONAL-GO** | Apache-2.0; isolated worktree trial; pick one meta-harness |
| agents-best-practices | **CONDITIONAL-GO (cherry-pick)** | MIT; no global install until dedup vs wiki |
| defenseclaw | **CONDITIONAL-GO** | Apache-2.0; pattern theft > full sidecar for laptop workflow |
| SeClaw | **NO-GO (install) / REFERENCE** | No LICENSE file; code "coming soon" |
| scienceaix/agentskills | **REFERENCE** | MIT confirmed; stale catalog — discovery queue only |

## [2026-06-04] ingest | Daily digest — 2 arXiv papers (agent skills + InKH)

Ingested from `research to be indexed/` (daily digest 2026-06-04 sweep).

**Pages created (5):** `agent-skills-progressive-disclosure`, `interaction-native-knowledge-harness`, `scienceaix-agentskills`, `sources/arxiv-agent-skills-architecture-security-2602.12430`, `sources/arxiv-interaction-native-knowledge-harness-2606.01886`.

**Pages updated (10):** `agent-skills-taxonomy`, `skill-vetting`, `anthropic-skills`, `mcp-context-optimization`, `thin-harness-fat-skills-garrytan`, `muse-autoskill-skill-lifecycle`, `context-engineering`, `llm-wiki-compiler`, `index.md`.

**Cross-wiki:** InKH financial deployment → OSINT ingested K99 (`@osint-wiki/concepts/interaction-native-knowledge-harness.md`). 2602.12430 CCC-primary.

**Raw:** 2 PDFs → `raw-sources/`; inbox cleared.

## [2026-06-04] brief ingest | K98 agent org chart + MCP from OSINT

Ingested `briefs/2026-06-04_k98-ccc-agent-org-chart-mcp-from-osint.md` — Posts.docx K98 (13 posts, sha `32400c1f…`) harness cluster + SeClaw arXiv.

**Pages created (5):** `agent-five-gate-org-chart`, `mcp-server-catalog-curation`, `seclaw-agent-security-evaluation`, `sources/trading-posts-compilation-18-2026-06-04`, `sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04`.

**Pages updated (9):** `claude-code-subagent-templates`, `subagent-orchestration`, `code-as-agent-harness`, `conductor-mcp`, `lazy-tool`, `skill-vetting`, `k67-explorax-100-repos-reference`, `index.md`.

**Cross-wiki:** `@osint-wiki/sources/trading-posts-compilation-18-2026-06-04.md`, `@osint-wiki/concepts/seclaw-agent-security-evaluation.md`, `@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md`.

**Explicit non-actions:** Bloome / MiroFish / TradingAgents install without Phase-0; NEMO laptop REFERENCE only.

## [2026-06-03] brief ingest | K97 agent-harness cluster from OSINT

Ingested `briefs/2026-06-03_k97-ccc-agent-harness-from-osint.md` — Posts.docx K97 (17 posts, sha `bf5682b3…`), 10 harness posts routed to CCC.

**Pages created (4):** `claude-code-cheat-sheet-shortcuts`, `runtime-context-mcp-file-refs`, `agent-rubrics-self-correction`, `claude-cowork-automation-vs-hooks`.

**Pages updated (11):** `sources/trading-posts-compilation-17-2026-06-03`, `claude-harness-dynamic-workflows-k88`, `agent-token-discipline-openclaw-hermes`, `hermes-agent`, `codex-side-fork-workflow`, `claude-obsidian-notebooklm-bridge`, `monokern-compounding-research-pipeline`, `damidefi`, `kimi-agent-swarm`, `subagent-orchestration`, `claude-code`, `context-engineering`, `index.md`.

**Cross-wiki:** `@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md` (canon).

## [2026-06-03] ingest | K95

Daily digest fetch (`wiki/sweeps/2026-06-03-daily.md`). Five NEW arXiv harness/agent papers from `research to be indexed/` (+ CLI-Anything brief from OSINT per prior stub).

**Pages created (11):** `runtime-harness-interface-adaptation`, `adaptive-auto-harness-open-ended-streams`, `embedded-agent-modular-edge-architecture`, `slm-agent-orchestration-gateway`, `life-harness`, `adaptive-auto-harness`, `sources/arxiv-runtime-harness-adaptation-2605.22166`, `sources/arxiv-adaptive-auto-harness-2606.01770`, `sources/arxiv-agentxgcore-mobile-core-2606.00417`, `sources/arxiv-embedded-agent-modular-edge-2606.02862`, `sources/arxiv-slm-orchestration-gateway-2606.03557`.

**Pages updated (11):** `code-as-agent-harness`, `continual-harness-online-self-improvement`, `harness-updating-vs-benefit-nonmonotonic`, `system-scaling-harness-agentic-ai`, `subagent-orchestration`, `agent-sandbox-unikraft`, `lazy-tool`, `conductor-mcp`, `openevolve`, `index.md`.

**Cross-wiki (log only):** Five arXiv papers not yet on `@osint-wiki`. OSINT daily sweep flagged same PDFs — CCC owns harness-interface + lazy-tool/conductor routing synthesis; OSINT may own prediction-market stream eval (2606.01770) and telecom AgentxGCore (2606.00417) if routed. CLI-Anything (2606.03854) brief ingested separately — no duplicate full OSINT pages.

**Raw:** 5 PDFs → `raw-sources/` + `cemini-librarian:/opt/cemini-bulk/research/`; inbox cleared.

## [2026-06-02] brief ingest | K94 agent skills + Tool Forge from OSINT

Ingested `briefs/2026-06-02_2026-06-02_k94-ccc-agent-skills-agyn-toolforge-from-osint.md`.

**Pages created (4):** `agent-skills-taxonomy`, `tool-forge`, `sources/arxiv-agent-skills-survey-2605.07358-2026-06-02`, `sources/arxiv-tool-forge-governed-agentic-2605.28000-2026-06-02`.

**Pages updated (8):** `agyn`, `maven-agentic-tool-calling-generalization`, `worldmemarena-multimodal-agent-memory-eval`, `muse-autoskill-skill-lifecycle`, `autosci-memory-centric-research-agents`, `system-scaling-harness-agentic-ai`, `skill-vetting`, `thin-harness-fat-skills-garrytan`, `lazy-tool`, `index.md`.

**Cross-wiki:** `@osint-wiki` steal-from stubs on harness papers (MAVEN, WorldMemArena, MUSE, AutoSci, system-scaling); Agyn → `@osint-wiki/entities/tools/agyn-platform.md`.

**Lint:** `--fix-bidirectional --apply` — 0 gaps post-fix.

## [2026-06-02] ingest | CCC inbox — 5 arXiv papers (digest 2026-06-02)

Daily digest fetch (`scripts/daily_research_digest_run.py`). Scheduled LaunchAgent failed (exit 512 — env); manual run succeeded.

**Pages created (9):** `maven-agentic-tool-calling-generalization`, `worldmemarena-multimodal-agent-memory-eval`, `decoupled-intelligence-multi-agent-reference`, `agyn`, `sources/arxiv-sia-harness-weight-updates-2605.27276` (OSINT stub only), `arxiv-maven-agentic-tool-calling-2605.30738`, `arxiv-worldmemarena-agent-memory-2605.29341`, `arxiv-agyn-agent-platform-2605.27575`, `arxiv-decoupled-intelligence-multi-agent-2605.27685`.

**Pages updated (2):** `harness-updating-vs-benefit-nonmonotonic`, `index.md`.

**Skipped duplicate narrative:** SIA 2605.27276 — canon `@osint-wiki` K84.

**Raw:** 5 PDFs → `raw-sources/`; inbox cleared. Sweep: `wiki/sweeps/2026-06-02-daily.md`.

## [2026-06-01] ingest | CCC inbox — 3 arXiv harness papers (digest fetch)

Ingested from `research to be indexed/` (daily digest 2026-06-01). **Skipped** arXiv 2605.27276 (SIA) — already on `@osint-wiki` K84.

**Pages created (6):** `system-scaling-harness-agentic-ai`, `muse-autoskill-skill-lifecycle`, `autosci-memory-centric-research-agents`, `sources/arxiv-system-scaling-harness-2605.26112`, `sources/arxiv-muse-autoskill-2605.27366`, `sources/arxiv-autosci-2605.31468`.

**Pages updated (8):** `code-as-agent-harness`, `harness-updating-vs-benefit-nonmonotonic`, `continual-harness-online-self-improvement`, `skillrae-retrieval-augmented-execution`, `skill-vetting`, `monokern-compounding-research-pipeline`, `federated-daily-research-digest`, `index.md`.

**Raw:** 3 PDFs → `raw-sources/`; inbox cleared.

## [2026-06-01] brief ingest | K93 digest + monokern + harness (structural + wiki)

Ingested `briefs/2026-06-01_k93-ccc-digest-monokern-harness-from-osint.md`.

**Structural:** federated daily digest install (`scripts/daily_research_digest_run.py`, `daily_research_fetch.py`, `daily_research_config.yaml`, `wiki/sweeps/`, LaunchAgent `com.cemini.daily-research-digest.ccc`).

**Pages created (10):** `revfactory-harness`, `thin-harness-fat-skills-garrytan`, `harness-updating-vs-benefit-nonmonotonic`, `monokern-compounding-research-pipeline`, `federated-daily-research-digest`, `meta/daily-research-digest-cadence`, `sources/multi-wiki-tool-eval-v5-k93-2026-06-01`, `sources/trading-posts-compilation-31-2026-06-01`, `sources/arxiv-harness-updating-not-benefit-2605.30621`, `sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01`.

**Pages updated (3):** `agents-best-practices`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md`, `@osint-wiki/sources/trading-posts-compilation-31-2026-06-01.md`.

## [2026-06-01] adopt | K92 GO items on laptop

- claude-trading-skills (5 skills, trading-* prefix)
- obsidian-second-brain (vault wiki/, bg agent off)

## [2026-06-01] phase0 | K92 eval repos — license + clone audits

- **tradermonty/claude-trading-skills** — GO (MIT, active)
- **eugeniughelbur/obsidian-second-brain** — GO laptop-only (canon @osint-wiki/sources/)

## [2026-06-01] brief ingest | K92 v7 tool eval slice + Posts-12 agent harness

Ingested `briefs/2026-06-01_k92-ccc-agent-harness-from-osint.md`.

**Pages created (8):** `harness-layer-competition-cursor-claude-perplexity`, `deepseek-coding-cost-routing`, `agentic-pm-review-artifacts`, `obsidian-second-brain-eugeniughelbur`, `claude-trading-skills`, `slot-casino-game-developer-skills`, `sources/multi-wiki-tool-eval-v7-k92-2026-06-01`, `sources/trading-posts-compilation-12-2026-06-01` (filled).

**Pages updated (4):** `agent-personality-file-hermes-openclaw`, `obsidian-vellum-second-brain-stack`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md`, `@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md`.

## [2026-05-31] brief ingest | K90 v6 tool eval + Posts-16 agent harness

Ingested `briefs/2026-05-31_k90-ccc-agent-harness-from-osint.md`.

**Pages created (12):** `agent-personality-file-hermes-openclaw`, `nine-stage-agent-team-production`, `remote-hermes-access-pattern`, `ai-agents-learning-roadmap-reference`, `claude-artifacts-app-building`, `npxskillui`, `hermes-desktop`, `librechat`, `skyhook-radar`, `sources/multi-wiki-tool-eval-v6-k90-2026-05-31`, `sources/trading-posts-compilation-16-2026-05-31`.

**Pages updated (8):** `cross-wiki-tool-eval-inventory`, `deep-research-evaluation-prompt`, `everything-claude-code`, `hermes-agent`, `agent-token-discipline-openclaw-hermes`, `claude-code-software-factory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`, `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`.

## [2026-05-31] brief ingest | K88 v5 tool eval + Posts-42 harness workflows

Ingested `briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md`.

**Pages created (15):** `karpathy-agent-infrastructure-basics`, `claude-code-subagent-templates`, `claude-harness-dynamic-workflows-k88`, `webwright`, `skill-seekers`, `book-to-skill`, `skillnet`, `cc-thinking-skills`, `claude-skill-registry`, `alirezarezvani-claude-skills`, `jezweb-claude-skills`, `ruflo`, `sources/multi-wiki-tool-eval-v5-k88-2026-05-31`, `sources/trading-posts-compilation-42-2026-05-31`.

**Pages updated (7):** `cross-wiki-tool-eval-inventory`, `deep-research-evaluation-prompt`, `karpathy-token-efficiency-patterns`, `claude-plugins-catalog-patterns`, `obsidian-vellum-second-brain-stack`, `index.md`.

**Lint:** `scripts/wiki_lint.py` — cross-wiki alias resolution + citation-safe `@alias/path` boundary check.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md`, `@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md`.

## [2026-05-30] prompt | v5 deep-research multi-wiki eval

Added `prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md` — current default (world-cup-bot inventory, inline `gh` license lookup, NO-GO registry, TIME-VOLATILE sports LP).

**Updated:** `concepts/deep-research-evaluation-prompt`, `index.md`.

## [2026-05-30] brief ingest | K84 Codex /side /fork /goal harness patterns

Ingested `briefs/2026-05-30_k84-codex-harness-from-osint-posts.md`.

**Pages created (2):** `codex-side-fork-workflow`, `sources/trading-posts-compilation-k84-2026-05-30`.

**Pages updated (8):** `2026-05-13_multi-codex-codex-home-isolation`, `full-prompt-goal-template`, `cursor-ide-workspace`, `lazy-tool`, `conductor-mcp`, `claude-code`, `claude-desktop-vs-claude-code`, `code-as-agent-harness`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md`.

## [2026-05-30] brief ingest | K78 five-tool stack + Obsidian contribution-rate workflows

Ingested `briefs/2026-05-29_k78-five-tool-obsidian-workflows-from-osint.md`.

**Pages created (4):** `five-layer-operator-stack`, `obsidian-contribution-rate-workflow`, `sources/trading-posts-compilation-6-2026-05-29`, `entities/people/damidefi`.

**Pages updated (9):** `obsidian-vellum-second-brain-stack`, `claude-obsidian-notebooklm-bridge`, `obsidian-agent-maintenance-workflow`, `hermes-agent`, `kimi-agent-swarm`, `cursor-ide-workspace`, `claude-code`, `trading-posts-compilation-20-2026-05-27`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md`.

## [2026-05-28] brief ingest | K76 Skills.md + CLAUDE.md five-section workflows

Ingested `briefs/2026-05-28_k76-claude-skills-claude-md-workflows-from-osint.md`.

**Pages created (3):** `claude-code-skills-md-institutional-memory`, `claude-md-five-section-template`, `sources/trading-posts-macro-charts-skills-md-2026-05-28`.

Cross-wiki: `@osint-wiki/concepts/claude-code-skills-md-workflow.md`, `@osint-wiki/sources/trading-posts-macro-charts-skills-md-2026-05-28.md`.

## [2026-05-28] brief ingest | K73 Phase-0 audit decisions

Ingested `briefs/2026-05-28_k73-phase0-audit-ccc-decisions.md`.

**Pages created (3):** `k73-phase0-audit-decisions`, `entities/tools/mermaid-skill`, `entities/tools/tvscreener`.

**Page updated:** `entities/tools/metatrader-mcp-server` posture changed to NO-GO for current scope.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-25url-2026-05-28.md`.

## [2026-05-28] brief ingest | K73 license skepticism + workflow patterns

Ingested `briefs/2026-05-28_k73-ccc-tool-eval-license-skepticism.md` and `briefs/2026-05-28_k73-ccc-workflows-from-osint.md`.

**Pages created (6):** `tool-eval-license-skepticism-patterns`, `enterprise-auto-mode-telemetry-rollout`, `harness-de-bloat-4x4-pattern`, `sources/multi-wiki-tool-eval-25url-2026-05-28`, `sources/trading-posts-compilation-38-2026-05-28`, `sources/arxiv-continual-harness-self-improving-agents-2605.09998` (backlink refresh).

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-25url-2026-05-28.md`, `@osint-wiki/sources/trading-posts-compilation-38-2026-05-28.md`.

## [2026-05-27] brief ingest | K72 Posts-25 workflows + Continual Harness

Ingested `briefs/2026-05-27_k72-ccc-workflows-from-osint.md`.

**Pages created (12):** `agent-completion-verification-gates`, `agent-memory-stack-comparison`, `claude-plugins-catalog-patterns`, `claude-prompt-engineering-techniques`, `claude-code-finance-research-setup`, `obsidian-vellum-second-brain-stack`, `karpathy-token-efficiency-patterns`, `full-stack-ai-engineer-agent-path`, `train-llm-agents-2026-curriculum`, `agentic-programming-full-stack-thesis`, `continual-harness-online-self-improvement`, `sources/arxiv-continual-harness-self-improving-agents-2605.09998`, `sources/trading-posts-compilation-25-2026-05-27`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md`, `@osint-wiki/concepts/continual-harness-online-self-improvement.md`.

## [2026-05-27] brief ingest | K71 27-URL eval (CCC tooling slice)

Ingested `briefs/2026-05-27_k71-ccc-tooling-from-osint.md`.

**Pages created (11):** `metatrader-mcp-server`, `three-man-team`, `claude-subconscious`, `council-of-high-intelligence`, `open-claude-code`, `mercury-agent-skills`, `solo-founder-superpowers`, `build-your-own-openclaw`, `ai-infra-engineer-learning`, `andrej-karpathy-skills-multica`, `bmad-creative-intelligence-suite`.

**Policy:** `multica-ai/andrej-karpathy-skills` Adopt demoted (no LICENSE).

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md`.

## [2026-05-27] wire | notebooklm-py laptop + agent skills

- **CLI:** `notebooklm-py` 0.5.0, Playwright chromium, `notebooklm login`, `auth check --test --json` ok
- **Skills:** `notebooklm skill install` (user + OSINT project) → `.claude/skills/notebooklm`, `.agents/skills/notebooklm`
- **OSINT:** `.cursor/skills/notebooklm-osint-bridge` (Cemini redaction + workflow)
- **Wiki:** `notebooklm-py` + `claude-obsidian-notebooklm-bridge` → validated

## [2026-05-27] brief ingest | K69 Claude/Obsidian/LLM workflows (Posts.docx CCC slice)

Ingested `briefs/2026-05-27_k69-claude-obsidian-llm-workflows-from-osint.md`.

**Pages created (8):** `llm-engineering-stack-curriculum`, `agent-sandbox-unikraft`, `rag-binary-quantization`, `claude-code-large-codebase-workflow`, `agent-token-discipline-openclaw-hermes`, `claude-obsidian-notebooklm-bridge`, `entities/tools/notebooklm-py`, `sources/trading-posts-compilation-20-2026-05-27.md`.

**Updated:** `local-llm-mechanics-primer`, `context-engineering`, `token-economics-and-prompt-caching`, `claude-code`, `hermes-agent`, `tier1-tier2-agent-model`, `obsidian-agent-maintenance-workflow`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md`.

## [2026-05-26] brief ingest | K68 22-URL eval (CCC tooling slice)

Ingested `briefs/2026-05-26_k68-ccc-tooling-from-osint.md`.

**Pages created (5):** `google-eng-practices`, `ml-intern`, `rowboat`, `centaur`, `purple-cli`.

**Policy:** `MadAppGang/claudish` eval Adopt overturned → `@concepts/tools-we-dont-use.md` K68 section.

**Backlinks:** `cross-wiki-tool-eval-inventory`, `index.md`, orchestration/skill pages via lint.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md`.

## [2026-05-26] brief ingest | K67 Claude/Obsidian workflows (Posts.docx CCC slice)

Ingested `briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md`.

**Pages created (6):** `claude-premortem-skill`, `obsidian-agent-maintenance-workflow`, `obsidian-trading-journal-workflow`, `claude-code-software-factory`, `claude-code-personal-os-scope`, `sources/k67-explorax-100-repos-reference` (unread-stub).

**Updated:** `claude-obsidian` (K67 pattern-only note), `skill-vetting`, `subagent-orchestration`, `openspec`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md`.

## [2026-05-21] brief ingest | K65 Kimi Agent Swarm vs Claude Agent Teams

Ingested `briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md` (was in correct `briefs/` folder; missed on prior pass).

**Pages created (2):** `concepts/kimi-agent-swarm-vs-claude-agent-teams.md`, `entities/tools/kimi-agent-swarm.md`.

**Backlinks:** `subagent-orchestration`, `scatter-gather`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: OSINT K65 canon (`@osint-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md`).

## [2026-05-21] query | Brief inbox check + K64 Hermes routing stub

**Briefs:** 22 files in `briefs/` — all have `processed:` markers; no new drops in `research to be indexed/`.

**Action:** K64 exists on OSINT only (CeminiSuite target); CCC slice = Hermes catalog → conductor reference. Created `entities/tools/hermes-agent.md`; backlinks on `conductor-mcp`, `cross-wiki-tool-eval-inventory`, `index.md`.

## [2026-05-21] hands-on | K63 Cursor adoption (CCC project)

Implemented K63 **Adopt** slice for this repo (not OSINT lazy-tool):

- `.cursor/mcp.json` — **exa** (`scripts/mcp_exa.sh`) + **fetch**
- `.cursor/rules/ccc-*.mdc` (4) — wiki workflow, page format, visual deliverables, rejected piracy tools
- `.cursor/curated-rules/README.md` — awesome-cursorrules mapping
- `scripts/openevolve-phase0-smoke.sh` — Phase-0 PASS (isolated venv)

**Wiki:** `cursor-ide-workspace`, `awesome-cursorrules` → validated; `openevolve` smoke noted.

## [2026-05-24] brief ingest | K63 Cursor/agent tooling (36-URL eval CCC slice)

Ingested `briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md`.

**Pages created (6):** `openevolve`, `awesome-cursorrules`, `claude-code-game-studios`, `agents-best-practices` (defer), `everything-claude-code` (ECC defer stub), `cursor-community-plugins` (CONDITIONAL-GO).

**Policy:** cursor piracy cluster added to `@concepts/tools-we-dont-use.md`.

**Backlinks:** `cursor-ide-workspace`, `subagent-orchestration`, `cross-wiki-tool-eval-inventory`, `tools-we-dont-use`.

## [2026-05-23] brief ingest | K60 Ai-Engineering-Roadmap (reference-only)

Ingested `briefs/2026-05-23_k60-ai-engineering-roadmap-from-osint.md`.

**Page created:** `entities/tools/ai-engineering-roadmap.md` — MIT CONFIRMED (~552★); curriculum gap-check vs existing conductor/skills/MCP docs; no install.

**Inventory:** upgraded K53 `ai-engineer-roadmap` catalog row; added K60 section.

**Also marked processed:** `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md` (ingested prior commit; marker was missing).

## [2026-05-23] brief ingest | K59 SkillRAE + GraphFlow (OSINT Tier-B harness papers)

Ingested `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md`.

**Pages created (4):**
- `concepts/skillrae-retrieval-augmented-execution.md` + `sources/arxiv-skillrae-2605.10114.md`
- `concepts/graphflow-verifiable-agent-workflows.md` + `sources/arxiv-graphflow-2605.14968.md`

**Backlinks:** `code-as-agent-harness`, `lazy-tool`, `mcp-context-optimization`, `context-engineering`, `skill-vetting`, `openspec`, `conductor-mcp`, `cc-wf-studio`, `scatter-gather`, `glasswing`, `anthropic-skills`, `the-architect`, `cross-wiki-tool-eval-inventory`.

**Deferred:** SkillsVote (2605.18401) — not downloaded.

**OSINT backlink:** `@ccc-wiki/...` on both OSINT concept stubs.

## [2026-05-22] brief ingest | K57 local-LLM + agent infra + K55-2 ridark CCC subset

**K57** (`briefs/2026-05-22_k57-local-llm-and-agent-infra-from-osint.md`):
- `concepts/local-llm-mechanics-primer.md` — @TheAhmadOsman LLMs 101 stub
- `entities/tools/open-design.md`, `entities/tools/the-architect.md` — MIT/Apache-2.0 CONFIRMED via `gh api`
- AI OS essay (Post 5) — reference note on `conductor-mcp` only (no new page)
- `rag-from-scratch` — catalog row in `cross-wiki-tool-eval-inventory.md` only

**K55-2 ridark** (`briefs/2026-05-21_k55-2-ridark-eth-ccc-relevant-repos.md`):
- `concepts/tools-we-dont-use.md` — reject register (#1, #5, #18, #30 + skepticism tier)
- `entities/tools/repomix.md`, `n8n-mcp.md`, `anything-llm.md` — MIT verified 2026-05-22
- `entities/tools/claude-code-tips.md` — NOASSERTION license, defer
- OpenHands / ida-pro-mcp / rtk / ClawRouter — inventory catalog only (no stub farm)

**Backlinks:** `claude-code`, `context-engineering`, `token-economics`, `cross-wiki-routing`, `skill-vetting`, `twelve-rule-claude-md-template`, `cross-wiki-tool-eval-inventory`, `conductor-mcp` (+ lint `--fix-bidirectional --apply`).

## [2026-05-21] docs | Multi-wiki eval prompt v3 restore + v4 (Cursor-primary)

**Canonical prompts (repo root `prompts/`):**
- `deep-research-multi-wiki-eval-v3-2026-05-21.md` — frozen verbatim (7 surfaces, CCC = surface 7); reproduces K53/K54/K55
- `deep-research-multi-wiki-eval-v4-2026-05-21.md` — current default: same 7 surfaces, CCC surface expanded for **Cursor primary** + Claude Code secondary + post-run spot-check

**Wiki pages (2):**
- `concepts/deep-research-evaluation-prompt.md` — version lineage + ingest workflow
- `concepts/cursor-ide-workspace.md` — Open Folder / MCP / rules / vs Claude Code

**Note:** An earlier draft mistakenly split into 8 surfaces (Cursor #7 + Claude Code #8); discarded in favor of user's v3 structure.

## [2026-05-21] brief ingest | K48 code-as-harness + self-healing (OSINT arXiv)

Ingested `briefs/2026-05-21_k48-code-as-harness-and-self-healing-from-osint.md` (post-batch; arrived after 15-brief sweep).

**Pages created (2):**
- `concepts/code-as-agent-harness.md` — three-layer survey model → Claude Code / conductor / MCP / hooks mapping
- `concepts/self-healing-agent-sessions.md` — failure taxonomy + retry budget for long sessions

**Backlinks updated (12):** `claude-code`, `conductor-mcp`, `subagent-orchestration`, `hooks-for-automation`, `glasswing-deliberate-disagreement`, `openspec`, `skill-vetting`, `stash`, `lazy-tool`, `claude-mem`, `full-prompt-goal-template` (+ mutual link between the two new concepts).

**OSINT backlink:** `@ccc-wiki/concepts/code-as-agent-harness.md` added to `@osint-wiki/concepts/code-as-agent-harness.md`.

## [2026-05-21] batch ingest | 15 cross-wiki briefs triaged and ingested

Bulk triage of all unprocessed briefs in `briefs/` (15 total). Two were already-ingested (concept stubs existed); 13 were unprocessed.

**Pages created (8):**
- `entities/patterns/citadel-agent-orchestration.md` — apex agent-orchestration OS layer (K51)
- `entities/patterns/glasswing-deliberate-disagreement.md` — evilsocket/audit adversarial-verification pattern (K56)
- `entities/tools/defenseclaw.md` — Cisco security governance for agentic AI (K45)
- `entities/tools/cc-wf-studio.md` — VS Code visual workflow editor for CC pipelines (K53)
- `entities/tools/delive.md` — system-audio capture + MCP + agent skill bridge (K54/K55)
- `entities/tools/everos.md` — context-offload-to-disk memory OS (K54)
- `entities/skills/src-hunter-skill.md` — 305-payload SKILL.md design exemplar (K55)
- `concepts/cross-wiki-tool-eval-inventory.md` — consolidated catalog of all ~35 CCC-routed items from K45–K56

**Already-ingested (2, added processed marker):**
- `2026-05-13_multi-codex-codex-home-isolation.md` → concept stub existed at `concepts/2026-05-13_multi-codex-codex-home-isolation.md`
- `2026-05-13_tolaria-steal-from-patterns.md` → concept stub existed at `concepts/2026-05-13_tolaria-steal-from-patterns.md`

**Backlinks updated (5 existing pages):**
- `concepts/subagent-orchestration.md` — added citadel, glasswing, cc-wf-studio
- `concepts/agent-vm-sandboxing.md` — added defenseclaw
- `concepts/skill-vetting.md` — added defenseclaw, src-hunter-skill
- `concepts/twelve-rule-claude-md-template.md` — added Karpathy 82k★ reference
- `concepts/cross-wiki-routing.md` — added cross-wiki-tool-eval-inventory

**Remaining items cataloged** in `concepts/cross-wiki-tool-eval-inventory.md` (one-line per item, ~35 items across K45–K56).

All 15 briefs marked `processed: 2026-05-21`. Briefs retained for provenance trail.

## [2026-05-17] cross-wiki route | ai-token-monitor + CodexBar + SuperClaude_Framework + Roo-Code (OSINT 56-repo tool eval)

Four entity pages cross-routed into CCC from the OSINT-side 56-repo multi-wiki tool eval `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`. All four are CCC-primary-fit, all tier **Adopt** in the eval.

**New pages (4, all `entities/tools/`)**:
- `entities/tools/ai-token-monitor.md` — cross-platform Tauri desktop app monitoring Claude Code + Codex token usage; offline-first except opt-in leaderboards. MIT. Token telemetry for the laptop-side fleet.
- `entities/tools/codexbar.md` — lightweight macOS menu-bar app; live API stats, daily/weekly limit tracking, desktop overrun notifications for Claude Code + Codex. MIT. The enforcement/alerting layer for token-economic policy.
- `entities/tools/superclaude-framework.md` — Claude Code configuration/automation framework (slash commands + cognitive personas + KNOWLEDGE.md integrations). ~22.8k★. MIT. Maps to CCC's document/extend/standardize mandate.
- `entities/tools/roo-code.md` — autonomous AI agent team embedded in the code editor; ~24.1k★. Apache-2.0. **Repo ARCHIVED by owner** — recorded as adoptable only as a fork-and-maintain blueprint, not a live dependency; Apache-2.0 permits the fork. Archived-repo caveat called out in Narrative + Dead Ends.

**Bidirectional backlinks added** to 4 existing CCC pages: `entities/openusage.md` (sibling token tool — linked from both monitors), `concepts/token-economics-and-prompt-caching.md` (concept link for both monitors), `concepts/subagent-orchestration.md` (concept link for SuperClaude_Framework persona model + Roo-Code agent team), `entities/tools/claude-code.md` (harness link for SuperClaude_Framework), `entities/claude-code-agent-farm.md` (sibling multi-agent tool — linked from Roo-Code). `updated:` bumped on all five.

**`index.md` updated**: 4 tool rows + 4 cross-wiki-link rows. No pre-existing near-equivalent pages — `openusage` is the closest sibling (token telemetry) but is a distinct tool (Go daemon vs Tauri app vs Swift menu-bar); linked, not merged. Do NOT git commit — left staged.

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

## [2026-05-31] cross-wiki route | Trading posts compilation 16 K90

Cross-wiki stub routed from `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`.
- Filled `wiki/sources/trading-posts-compilation-16-2026-05-31.md` + K90 concept pages (see ingest entry above)

## [2026-05-31] cross-wiki route | Multi-wiki tool eval v6 K90

Cross-wiki stub routed from `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`.
- Filled `wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` + K90 tool entity pages (see ingest entry above)

## [2026-06-01] cross-wiki route | Trading posts compilation K92 (12 posts)

Cross-wiki stub routed from `@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md`.
- Filled source + K92 harness pages (see ingest entry above)

## [2026-06-05] skill | cursor-audit — multi-model Cursor debug harness

Mirrored from OSINT WORKSPACE `.cursor/skills/cursor-audit/` (origin: codex + opus caught different errors on same bug).
- Created `.cursor/skills/cursor-audit/` (SKILL.md + reference.md + examples.md) in CCC + OSINT
- Created `wiki/entities/skills/cursor-audit.md`
- Backlinks: `@concepts/subagent-orchestration.md`, `@entities/patterns/glasswing-deliberate-disagreement.md`, `@entities/tools/council-of-high-intelligence.md`, `@entities/skills/tech-debt-audit.md`

## [2026-06-06] cross-wiki route | ADK Arena — agent framework benchmark (OSINT handoff)

Cross-wiki stub routed from `@osint-wiki/sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md`.
- Created wiki/concepts/adk-arena-agent-framework-benchmark.md (stub)
