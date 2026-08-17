---
title: "Recoverable agent execution checkpoints (K282)"
type: concept
tags: [concept, agent-harness, checkpointing, recovery, k282]
keywords: [2608.14380, AgentRewind, MettleBench, aligned-checkpoints, rewind-memory, resume-from-checkpoint]
related:
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
  - entities/tools/agentrewind.md
  - entities/tools/mettlebench.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - concepts/failed-trajectory-harness-repair.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-agentrewind-recoverable-execution-2608.14380.md`
- `@entities/tools/agentrewind.md`
- `@entities/tools/mettlebench.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md` — K239: irreversible transitions are the counterpart; checkpoints make the irreversible reversible (within the workspace boundary)
- `@concepts/telemetry-deterministic-agent-failure-repair.md` — K242: Sentinel rolls back on telemetry; AgentRewind lets the *agent* choose when to rewind
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix mutates the harness; AgentRewind rewinds the trajectory in-session

## Raw Concept

Long-horizon agent errors propagate through context *and* environment, and appending corrective actions can't always undo them. What if the agent could rewind to an earlier aligned checkpoint and resume with what it learned from the failed attempt?

## Narrative

AgentRewind (arXiv 2608.14380) makes execution **recoverable** by recording aligned checkpoints of the agent context and the controlled workspace environment at each LLM decision boundary. When the agent judges the current trajectory stuck, it selects an earlier checkpoint, restores both state components, and injects **rewind memory** — a summary of the failed attempt (falsified hypotheses, alternative strategies) — before resuming.

### Steal (ADOPT)

1. **Aligned context + environment checkpoints.** A recoverable checkpoint is the pair `(context, environment)`, not either alone. Ablation: dropping environment rewind cuts success 87.8 → 43.9, the single largest component loss — discarded-suffix side effects otherwise remain in place. Dropping context rewind (65.9) leaves discarded actions/observations in context to mislead the next attempt; dropping rewind memory (51.2) risks repeating the same mistake.
2. **Resume-from-checkpoint, not restart-from-zero.** `Restart-with-Experiences` resets to the initial state and discards completed work (the Astropy case study lost the finished library repair); rewind retains the validated prefix and only replaces the failing suffix.
3. **Rewind memory as a first-class artifact.** Keep prior-attempt information (falsified hypotheses, "what went wrong") alongside the restored context so the second attempt is informed, not blind.
4. **Recovery boundary honesty.** Only the workspace directory tree is reversible. Network requests, external-service calls, and external runtime state are *not* undone — and must not be re-triggered, so the retained prefix is replayed from the log, not re-executed.
5. **Checklist-progress scoring for long-horizon work.** Binary success hides partial progress. `ρ = ℓ/n` (longest satisfied prefix of ordered acceptance criteria) distinguishes "nearly done" from "barely started" and gives recovery a measurable target.

### Why this pairs K239 (execution fidelity) and K242 (deterministic rollback)

K239's irreversible-agent-invariants treat some transitions as one-way and gate them with confirm/preview. AgentRewind is the complement: for *reversible* workspace state, it provides a recovery mechanism so that errors need not be permanent. K242's Agent Trajectory Sentinel triggers rollback from telemetry (ESN/CUSUM detection); AgentRewind instead exposes rewind as an **agent decision** — the agent selects the checkpoint from trajectory metadata rather than a monitor forcing it. The two are complementary recovery triggers: monitor-initiated vs agent-initiated.

### Local adopt

- `Futuresis/replay-agent-recorder` — MIT (~3.7MB) → `.local/adopts/replay-agent-recorder` **GO REFERENCE**.
- `Kelvin-Coffee/MettleBench` — Apache-2.0 (~31MB) → `.local/adopts/MettleBench` **GO REFERENCE** (benchmark + task environments).

| Verdict | **ADOPT** aligned checkpoints + resume recovery + rewind memory. REFERENCE clones; runtime wiring `wont_wire`. |
