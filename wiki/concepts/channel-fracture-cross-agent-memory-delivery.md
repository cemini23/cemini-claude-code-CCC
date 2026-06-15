---
title: Channel fracture — silent cross-agent memory delivery failures
type: concept
tags: [concept, multi-agent, memory, verification, hermes, k111]
keywords: [2606.04896, channel-fracture, cadvp, inverse-verification, cron]
related:
  - sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md
  - entities/tools/hermes-agent.md
  - concepts/agent-completion-verification-gates.md
  - concepts/subagent-orchestration.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/hooks-for-automation.md
  - concepts/self-healing-agent-sessions.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - concepts/perspectivegap-orchestration-prompting.md
maturity: draft
created: 2026-06-12
updated: 2026-06-15
---

## Relations

- `@sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md` — Hermes cron fracture + CADVP
- `@entities/tools/hermes-agent.md` — reference runtime where fracture was found
- `@concepts/agent-completion-verification-gates.md` — completion proof at receiver
- `@concepts/subagent-orchestration.md` — hierarchical team injection use case
- `@concepts/agent-memory-stack-comparison.md` — persistent memory backends
- `@concepts/hooks-for-automation.md` — scheduled/cron execution contexts
- `@concepts/self-healing-agent-sessions.md` — session vs scheduler isolation contrast

## Raw Concept

Question: why do cross-agent "write this to agent B's memory" tasks appear to succeed but leave B's store empty?

## Narrative

**Channel fracture** [TENTATIVE — single production Hermes study, 2606.04896]: when orchestration dispatches **scheduled** agents (cron) to inject into another agent's persistent memory, the natural channel can fail **silently** because the scheduler execution context lacks memory-tool registration or hardcodes memory skip flags. Writer-side steps look correct; only **receiver-side inspection** reveals failure.

**Steal-from for Cemini harness:**

1. **Inverse verification principle** — prove delivery at the **receiver** (read-back, FTS query, hash of expected fact) not the sender's tool-return.
2. **Channel matching principle** — match delivery mechanism to execution context (interactive session vs cron vs subagent vs hook).
3. **CADVP CC-0** — veto-level channel confirmation before other verification dimensions.
4. **Three-Gate Quality** (L1 self / L2 evidence / L3 cross-review) — maps to writer/reviewer/tester subagent gates.

Applies beyond Hermes: Claude Code **Task** subagent returns, conductor/librarian cross-wiki writes, claude-mem injection, Stop-hook state files — any path where the writer context ≠ target store context.

**Bypass channels** (Hermes study): direct DB write or target self-write succeed; cron-delegated write fails — prefer explicit receiver pull or shared store with atomic commit over blind push from isolated scheduler.

## Snippets

> "Only receiver-side inspection reveals the failure."

> "CC-0 channel confirmation check … prevents false-positive delivery assurance."
