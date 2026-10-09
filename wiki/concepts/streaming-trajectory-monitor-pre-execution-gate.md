---
title: "OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectori (CCC K444)"
type: concept
tags: [concept, k444]
keywords: [2610.12375, k444]
related:
  - sources/arxiv-ontrack-streaming-monitor-2610.12375.md
  - concepts/instrumental-monitor-evasion-under-task-pressure.md
  - concepts/agent-completion-verification-gates.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/intent-based-tool-call-oversight.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-09_ccc-k441-k444-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-09
updated: 2026-10-09
---

## Relations

- `@sources/arxiv-ontrack-streaming-monitor-2610.12375.md`
- `@concepts/instrumental-monitor-evasion-under-task-pressure.md`
- `@concepts/agent-completion-verification-gates.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@concepts/intent-based-tool-call-oversight.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-09_ccc-k441-k444-sip-ready.md`

## Raw Concept

K444: ADOPT pattern (real-time process monitor + pre-execution gate) — arXiv 2610.12375.

## Narrative

**A monitor that decides, not scores — and blocks irreversible actions before they run.** OnTrack is a **streaming** process monitor: it models the agent's execution as a growing **DAG** (each step a node; an edge when one step consumes another's output) and aligns it against recorded successful runs with **structure-aware optimal transport**, at **~1 ms/step**. Three tiers that switch off as inputs disappear: **L1 vital signs** (loop, stall, information-gain — reference-free, always on), **L2 transport alignment** (needs references), **L3 pre-execution policy gate** (needs tool schemas; the only *synchronous* component — it checks an **irreversible** tool call's declared prerequisites *before* the tool runs and can **BLOCK**). Verdicts are actions — `OK / EXPLORING / WARN / LOOP / STALLED / CAUSAL INVERSION / OFF TRACK / BLOCK` — never a thresholded score, because **'a score value means different things at different trajectory lengths'** (its challenge S4). On **2,294 SWE-agent trajectories**: **+0.057 AUROC over cosine similarity at the first 8 steps** (the early-trajectory regime an in-flight monitor lives in), and a severe-flag-density **abort policy** saves **~18% of compute** with **83% of aborted runs genuinely heading to failure**. **Honest boundaries kept:** it is a *process monitor, not an outcome predictor* — once trace length is controlled, no task-generic signal predicts patch correctness; on homogeneous traces, loops/stalls are carried by the reference-free L1 heuristics and the transport layer's contribution is a *lower false-alarm operating point*, not better ranking; and the L3 gate is *a policy gate, not a soundness guarantee*. **CCC reading:** the clearest design doc CCC has for a **hook-like checkpoint layer** inside the agent loop — the L3 pre-execution gate is exactly a `PreToolUse`-style block on irreversible actions, and 'per-step signals, short grace window, never the aggregate score' is a rule for writing hooks and gates. It also names the harness dependency: the dependency metadata `ζt` **comes from the harness's own logs** (full / partial / none), so monitor quality is bounded by what the harness records — the same affordance argument as K442. Pairs `instrumental-monitor-evasion-under-task-pressure`, `agent-completion-verification-gates`, `execution-fidelity-irreversible-agent-invariants`, `intent-based-tool-call-oversight`. **No public repo URL.** Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.12375 locators." [Source: CCC K444 synthesis]
