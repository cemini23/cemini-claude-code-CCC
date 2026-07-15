---
title: ETCLOVG — seven-layer agent harness taxonomy
type: concept
tags: [concept, agent-harness, taxonomy, etclovg, k100]
keywords: [etclovg, execution, tooling, context, lifecycle, observability, verification, governance]
related:
  - concepts/failed-trajectory-harness-repair.md
  - concepts/code-as-agent-harness.md
  - concepts/skill-vetting.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/tier1-tier2-agent-model.md
  - sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md
  - concepts/self-healing-agent-sessions.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/time-series-native-agent-harness.md
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - concepts/agent-harness-operational-definition.md
  - sources/arxiv-agent-harness-operational-definition-2606.10106.md
  - concepts/harnessx-composable-evolution-foundry.md
  - sources/arxiv-harnessx-composable-harness-foundry-2606.14249.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - concepts/model-harness-six-responsibilities.md
  - sources/arxiv-agent-harness-survey-2606.20683.md
  - concepts/governed-fleet-shared-memory.md
  - concepts/mcp-trust-orchestration-collaboration.md
  - sources/arxiv-governed-shared-memory-2606.24535.md
  - concepts/recoverable-tool-reliability-hazards.md
  - sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md
  - concepts/agentic-orchestration-options-abpm.md
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md
  - concepts/failure-mode-harness-adaptation-mapping.md
maturity: validated
created: 2026-06-05
updated: 2026-07-10
---

## Relations

- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix maps failures to these layers
- `@concepts/code-as-agent-harness.md` — three-layer survey model; ETCLOVG is finer-grained runtime taxonomy
- `@concepts/skill-vetting.md` — Tool Interface + Governance gates before harness changes
- `@concepts/hooks-for-automation.md` — Lifecycle + Observability injection points
- `@concepts/model-harness-six-responsibilities.md` — six-responsibility survey decomposition (2606.20683)
- `@concepts/failure-mode-harness-adaptation-mapping.md` — K168 failure→adaptation map overlays context/tools/control

## Raw Concept

Seven-layer harness taxonomy from recent harness-engineering literature, formalized in arXiv **2606.06324** (HarnessFix) as **ETCLOVG**: Execution, Tooling, Context, Lifecycle, Observability, Verification, Governance. Used to localize *which harness layer* failed — not just “the model was wrong.”

## Narrative

| Layer | Responsibilities | Cemini / Claude Code mapping |
|-------|------------------|------------------------------|
| **Execution** (sandbox) | Safe, isolated, reproducible action environments | `@concepts/agent-vm-sandboxing.md`, Tier-2 scope; prod EMS boundaries |
| **Tool Interface** | Tool discovery, schemas, docs, validation, error feedback | MCP manifests, `@entities/tools/lazy-tool.md`, SKILL.md tool lists |
| **Context & Memory** | What the model sees each step: window, summaries, retrieval, persistent memory | `hot.md`, `@entities/tools/claude-mem.md`, stash, progressive disclosure |
| **Lifecycle & Orchestration** | Think-act-observe, retries, task state, multi-agent coordination, termination | Subagents, Stop hooks, `/goal`, conductor fan-out; **OO3/OO4** process frames (K136) |
| **Observability** | Traces, tool calls, errors, cost — enough to diagnose | `wiki/log.md`, claude-mem, defenseclaw discovery; **engine logs over agent self-log** (K136) |
| **Verification & Evaluation** | Readiness checks, intermediate validation, final eval, regression | `@concepts/skill-vetting.md`, OpenSpec criteria, `wiki_lint.py`, Glasswing review; **ToolBench-X** hazard recovery eval (K129); **substrate constraints + docs CLI** for code audit (K138) |
| **Governance & Security** | Permissions, approvals, audit trails, policy enforcement | Tier 1/2 model, defenseclaw scanners, SeClaw trajectory eval |

### Why CCC owns this page

The taxonomy is **harness vocabulary**, not domain finance. Use it when filing `## Dead Ends`, Stop-hook failures, or Phase-0 audits: tag the implicated layer before patching prompts.

### vs three-layer survey (`code-as-agent-harness`)

| Survey layer | ETCLOVG layers (approximate) |
|--------------|------------------------------|
| Harness interface | Tool Interface |
| Harness mechanisms | Context, Lifecycle, Observability |
| Scaling | Lifecycle (multi-agent), Verification |

## Snippets

> "The harness is realized through editable implementation artifacts such as prompt templates, tool specifications, orchestration code, configuration files, adapters, logging hooks, and verification scripts."
> — [Source: arxiv-2606.06324 §II, retrieved 2026-06-05]
