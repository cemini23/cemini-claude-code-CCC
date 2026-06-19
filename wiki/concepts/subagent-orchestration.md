---
title: Subagent orchestration — when and how to delegate
type: concept
tags: [concept, subagent, agent, delegation, claude-code, parallelism, explore-agent, plan-agent]
keywords: [subagent, Agent tool, Explore agent, Plan agent, code-reviewer, general-purpose, isolation, worktree, parallel agents]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/cross-wiki-routing.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/cua.md
  - entities/claude-code-agent-farm.md
  - entities/fusion.md
  - entities/tools/jcode.md
  - entities/tools/red-run.md
  - concepts/2026-05-13_multi-codex-codex-home-isolation.md
  - entities/tools/claude-for-legal.md
  - entities/mcp-servers/pmxt-mcp-pattern.md
  - entities/tools/osmedeus-acp-orchestration.md
  - concepts/agent-vm-sandboxing.md
  - concepts/twelve-rule-claude-md-template.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/autoresearch-loop.md
  - entities/mcp-servers/polymarket-mcp-server.md
  - entities/tools/superclaude-framework.md
  - entities/tools/roo-code.md
  - entities/patterns/citadel-agent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/tools/cc-wf-studio.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - entities/tools/n8n-mcp.md
  - entities/tools/the-architect.md
  - entities/tools/ai-engineering-roadmap.md
  - entities/tools/claude-code-game-studios.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - entities/tools/kimi-agent-swarm.md
  - concepts/claude-code-software-factory.md
  - concepts/claude-code-personal-os-scope.md
  - entities/tools/centaur.md
  - entities/tools/ml-intern.md
  - entities/tools/rowboat.md
  - concepts/claude-code-large-codebase-workflow.md
  - entities/tools/council-of-high-intelligence.md
  - entities/skills/cursor-audit.md
  - entities/skills/super-audit.md
  - entities/tools/three-man-team.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agentic-programming-full-stack-thesis.md
  - concepts/enterprise-auto-mode-telemetry-rollout.md
  - concepts/harness-de-bloat-4x4-pattern.md
  - concepts/claude-code-subagent-templates.md
  - concepts/karpathy-agent-infrastructure-basics.md
  - entities/tools/ruflo.md
  - concepts/nine-stage-agent-team-production.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - entities/tools/revfactory-harness.md
  - concepts/decoupled-intelligence-multi-agent-reference.md
  - concepts/agent-backpressure-loop.md
  - sources/trading-posts-compilation-19-2026-06-07.md
  - concepts/maven-agentic-tool-calling-generalization.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - entities/tools/agyn.md
  - sources/arxiv-agyn-agent-platform-2605.27575.md
  - sources/arxiv-agentxgcore-mobile-core-2606.00417.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - entities/people/damidefi.md
  - concepts/agent-five-gate-org-chart.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/long-thread-context-decay.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/queen-bee-beespec-enterprise-orchestration.md
  - sources/arxiv-queen-bee-beespec-enterprise-mcp-2606.06545.md
  - concepts/progressive-autonomy-incident-resolution.md
  - sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md
  - concepts/skillhone-continual-skill-decision-history.md
  - sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md
  - concepts/perspectivegap-orchestration-prompting.md
  - sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-internet-of-agentic-ai-2606.12835.md
  - sources/arxiv-parthenon-law-self-evolving-legal-agent-2606.04602.md
  - concepts/recursive-agent-harness-harness-recursion.md
  - sources/arxiv-recursive-agent-harnesses-2606.13643.md
  - concepts/tool-response-context-pruning-summarization.md
  - sources/arxiv-less-context-better-agents-2606.10209.md
  - concepts/claude-honesty-critic-agent.md
  - entities/tools/hermes-workspace.md
  - sources/brief-k112-ccc-claude-honesty-critic-2026-06-12.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md
  - concepts/handoff-validity-agent-harness.md
  - sources/arxiv-agentic-eda-handoff-2606.19795.md
maturity: validated
created: 2026-05-13
updated: 2026-06-19
---

## Relations

- `@entities/tools/claude-code.md` — the harness providing the `Agent` tool
- `@concepts/context-engineering.md` — subagent dispatch is one of the four levers
- `@concepts/token-economics-and-prompt-caching.md` — the cost trade-off behind subagent dispatch
- `@concepts/cross-wiki-routing.md` — multi-wiki queries are a canonical multi-subagent fan-out
- `@entities/patterns/tier1-tier2-agent-model.md` — scope-enforcement pattern for execution-capable subagents
- `@entities/tools/cua.md` — VM isolation chamber for Tier 2 subagents that need actual containment
- `@entities/claude-code-agent-farm.md` — tmux-pane parallel-agent orchestrator (steal-from: heartbeat + lock patterns)
- `@entities/fusion.md` — multi-node orchestrator with git-worktree isolation per task
- `@entities/tools/jcode.md` — Rust CC competitor; swarm-coordinator / worktree-manager architecture is the extractable pattern
- `@entities/tools/red-run.md` — agent-team orchestrator; lead-router + single-writer state-mgr patterns are clean-room extractable
- `@concepts/2026-05-13_multi-codex-codex-home-isolation.md` — per-instance `CODEX_HOME` isolation, generalizable to per-subagent home dirs
- `@entities/tools/claude-for-legal.md` — Trust Layer injection-detection guardrail + managed-agent cookbooks for cadence jobs (STEAL-FROM)
- `@entities/mcp-servers/pmxt-mcp-pattern.md` — execution-capable MCP server; the Tier-2-gated tool class
- `@entities/tools/osmedeus-acp-orchestration.md` — YAML-workflow engine orchestrating ACP subprocess agents; conductor-architecture reference
- `@entities/tools/superclaude-framework.md` — Claude Code config framework; its cognitive-persona model is a structured-persona pattern adjacent to subagent dispatch
- `@entities/tools/roo-code.md` — autonomous AI agent team embedded in the code editor; gold-standard IDE-integration exemplar of multi-agent orchestration
- `@entities/patterns/citadel-agent-orchestration.md` — apex agent-orchestration OS layer; 4-tier /do routing, campaign persistence, lifecycle hooks, circuit breaker
- `@entities/patterns/glasswing-deliberate-disagreement.md` — evilsocket/audit's adversarial-verification pattern; multi-agent disagreement as a safety primitive
- `@entities/tools/cc-wf-studio.md` — visual workflow editor for Claude Code agent pipelines; conditional-branching export format
- `@concepts/code-as-agent-harness.md` — scaling the harness via isolated subagent contexts
- `@concepts/self-healing-agent-sessions.md` — subagent error/empty-return retry budget
- `@concepts/kimi-agent-swarm-vs-claude-agent-teams.md` — external hub-and-spoke swarm vs Claude Teams / `Agent` tool (K65)
- `@entities/tools/kimi-agent-swarm.md` — Moonshot product reference only; not a CCC harness
- `@concepts/claude-code-software-factory.md` — multi-repo subagent fan-out metaphor (K67)
- `@concepts/claude-code-personal-os-scope.md` — scope warning vs unbounded personal-OS workspace (K67)
- `@entities/skills/cursor-audit.md` — three parallel Task subagents on different models; readonly Tier 1 audit synthesis
- `@entities/skills/super-audit.md` — five-auditor pre-ship council (3 Task + 2 HTTP API); tailored audit packs on disk
- `@concepts/perspectivegap-orchestration-prompting.md` — K114 need-only failure taxonomy for subagent prompts
- `@sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md` — orchestration prompting benchmark
- `@concepts/internet-of-agentic-ai-ioai.md` — Internet-scale MAS vision vs harness-local dispatch
- `@sources/arxiv-parthenon-law-self-evolving-legal-agent-2606.04602.md` — solver–evaluator–learner role isolation

Cross-wiki: `@osint-wiki/concepts/conductor-orchestrator.md` carries the OSINT-side conductor history (parallel subagent dispatch for cross-wiki queries).

## Raw Concept

Question this page answers: **when does Cemini delegate to a subagent rather than do the work in the parent session?**

## Narrative

Claude Code's `Agent` tool spawns an isolated subagent that gets its own context window, its own tool surface, and returns a single message to the parent. Several agent types are pre-defined:

| Type | When to use |
|------|-------------|
| `general-purpose` | Default; broad research / multi-step tasks |
| `Explore` | Read-only code search. Fast pattern-finding ("where is X defined / which files reference Y") |
| `Plan` | Architect-style implementation planning |
| `code-reviewer` | Independent second-opinion review |
| `statusline-setup` | Configures the harness status line |
| `claude-code-guide` | Q&A about Claude Code / Agent SDK / Anthropic API |

User-authored agents inherit a similar surface unless explicitly restricted.

### When to dispatch

The dispatch decision reduces to: **does the subagent save the parent more tokens than its own setup costs?**

- **Heavy reads (>10K of raw content)** — yes. The parent ingests the subagent's brief reply; the bulk of the read stays in the subagent's window.
- **Independent second opinions** — yes. Independence is the deliverable; the parent's context can't provide it. See `@entities/skills/cursor-audit.md` (3 models) or `@entities/skills/super-audit.md` (5 models + API leg) when the deliverable is **cross-model** disagreement, not just a second agent of the same family.
- **Genuinely parallel work** — yes. Multiple subagents in a single message run concurrently. The parent waits for all replies.
- **Trivial lookups, single file reads** — no. Direct `Read`/`Grep` is cheaper.
- **Tasks requiring the parent's working state** — no. Subagents don't share the parent's context.

### Parallelism rules

When dispatching multiple independent subagents, **send them in a single message with multiple `Agent` tool uses**. They run concurrently. Sequential `Agent` calls run serially. Cemini's typical multi-subagent fan-out: 2-4 parallel agents for a Phase-0 audit (license check + entry-point read + dependency audit + maturity-signal check).

### Foreground vs background

- **Foreground** — block on the result. Use when the next action depends on the subagent's findings.
- **Background (`run_in_background: true`)** — fire-and-forget; you get notified when complete. Use for genuinely-independent work you can do alongside.

### Isolation

`isolation: "worktree"` puts the subagent in a temporary git worktree. Use when the subagent is going to edit files and you want the changes contained. Worktree auto-cleans on no-changes; on changes you get the path back.

### Prompt brief discipline

The subagent doesn't see the parent conversation. The prompt must be **self-contained**: state the goal, what's been ruled out, what the constraint is, what form the answer should take. Bad: "fix the bug." Good: "investigate why test_X.py fails on Python 3.11+; expected fix is in src/foo.py; report findings only — don't edit." Under-briefed subagents do shallow generic work.

### Cross-wiki orchestration

The `conductor` MCP server (`@entities/tools/conductor-mcp.md`) is a subagent-orchestration primitive for the federation: it fans a query across multiple wikis and returns one synthesis. The same pattern is reusable for any "search across N independent corpora and merge" problem — see `@concepts/cross-wiki-routing.md` for the routing layer that decides which wikis to fan to.

### K98 five-gate org chart [TENTATIVE]

@Voxyz_ai Post 1 reframes subagent dispatch as an **org chart** (Intake → Specialist → Adversary → Lead → Memo) rather than ad-hoc Task calls. See `@concepts/agent-five-gate-org-chart.md` for Cemini gate mapping; `@concepts/claude-code-subagent-templates.md` for Zephyr four-lane weekend templates (K98 Post 4).

### What not to outsource

- **Synthesis and judgment.** "Based on the findings, fix it" pushes synthesis onto the subagent. The parent should integrate.
- **Per-session state writes.** Subagents don't share the parent's `hot.md` view. The parent updates `hot.md` after merging subagent results.
- **Anything requiring authorization the subagent doesn't have.** Subagents inherit permission allowlists; locked-down subagents can't run the tools the work needs.

### Tier 1 vs Tier 2 — when subagents need scope gates

Adapted from `@entities/patterns/tier1-tier2-agent-model.md` (full pattern there). Short version:

- **Tier 1 subagents** = advisory-only. Cemini's `Plan`, `Explore`, `code-reviewer`, `claude-code-guide` agents are all Tier 1 — they read, reason, recommend. No external state changes.
- **Tier 2 subagents** = execution-capable. Anything that runs commands with effects, writes outside the working directory, or makes API calls with state. Requires declared scope before invocation.

The split is the safety contract for subagent dispatch. Cemini currently runs no Tier 2 subagents in production; the pattern is documented because future skill adoptions may require it (and because cybersec sibling pages already implement it operationally — see `@cybersecurity-wiki/concepts/llm-pentest-automation.md`).

When a future Cemini Tier 2 subagent earns its slot:

1. YAML declares `requires_scope: true` and `allowed_targets: ["{{ ... }}"]`
2. The harness's permission UX confirms scope before invocation
3. `cua` (`@entities/tools/cua.md`) provides VM isolation as the actual containment layer (policy alone isn't enough)
4. Findings emit as structured JSON for downstream ingestion

### Subagent agent-permission inheritance

Subagents inherit the parent session's permission allowlist unless explicitly restricted. A subagent dispatched from a parent session with `Bash(rm -rf *)` denied still has that deny rule. Permission policy travels — but the subagent's prompt envelope does not see the parent conversation. Brief discipline matters: the subagent has Cemini's permissions but none of Cemini's intent; the prompt must carry that intent.

### Harness control plane (steal-from agents-best-practices) [CONFIRMED 2026-06-04]

Cherry-picked from `@entities/tools/agents-best-practices.md` adoption trial — provider-neutral loop that complements Task-tool dispatch:

```text
user/task → context builder → model call → tool proposal
  → schema validation → permission decision → execute or pause
  → structured observation → context update → repeat within budget
```

Non-negotiables for CCC subagent design:

- The **model proposes**; the **harness validates, authorizes, executes, records** observations.
- Every tool call must receive a tool result (denial, timeout, error, or success).
- Risky side effects require **runtime policy outside the model** — Tier 2 scope gates (`§ Tier 1 vs Tier 2` above).
- **Draft vs commit** stay separate for external, financial, destructive, or regulated actions.

Project skill copy: `.claude/skills/agents-best-practices/` (not global install).

### Lifecycle layer failures (K100)

Recurring subagent mis-dispatch (wrong `subagent_type`, empty summaries, parallel fan-out that should be serial) implicates **Lifecycle & Orchestration** in `@concepts/etclovg-harness-layers.md`. Log with layer tag; if pattern repeats, follow `@concepts/failed-trajectory-harness-repair.md` flaw-record discipline rather than prompt-only tweaks.

## Dead Ends

- **Subagent for a 1-file read** — pays setup, saves nothing. Direct `Read`.
- **Serial subagent calls when they could be parallel** — wastes wall-clock time.
- **Trusting the subagent's summary as a description of what it did** — verify by checking the actual changes / outputs. The harness tracks file state separately.
- **Skipping the Tier 2 scope gate "because it's annoying"** — see `@entities/patterns/tier1-tier2-agent-model.md` § Dead Ends.
