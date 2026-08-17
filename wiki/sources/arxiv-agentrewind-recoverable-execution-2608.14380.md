---
title: "AgentRewind — recoverable execution for long-horizon LLM agents"
type: source
tags: [source, arxiv, agent-harness, checkpointing, recovery, k282]
keywords: [2608.14380, AgentRewind, MettleBench, aligned-checkpoints, rewind-memory, resume-from-checkpoint, replay-agent-recorder]
related:
  - concepts/recoverable-agent-execution-checkpoints.md
  - entities/tools/agentrewind.md
  - entities/tools/mettlebench.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@entities/tools/agentrewind.md`
- `@entities/tools/mettlebench.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md` — K239: irreversible transitions vs recoverable checkpoints
- `@concepts/telemetry-deterministic-agent-failure-repair.md` — K242: rollback/repair in-session

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AgentRewind: Recoverable Execution for Long-Horizon LLM Agents |
| **arXiv** | 2608.14380 |
| **Authors** | Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang (UCAS / Tsinghua IIIS / Zhongguancun Academy / CAS Institute of Automation) |
| **Code** | `github.com/Futuresis/replay-agent-recorder` — **MIT** (verified LICENSE on disk) |
| **Dataset** | `github.com/Kelvin-Coffee/MettleBench` — **Apache-2.0** (verified LICENSE on disk) |
| **Retrieved** | 2026-08-17 |

## Narrative

Runtime recovery framework for long-horizon agent execution. Errors early in a trajectory propagate through **both** the agent context and the controlled environment state, and their effects can be hard to reverse by appending corrective actions. Existing methods (plan refinement, safety checks) reduce errors before/at execution but provide **little support after an error has occurred**.

AgentRewind records **aligned checkpoints** `d_t = (c_t, s_t)` — the agent context *and* the controlled workspace environment state — at every LLM decision boundary. When the agent decides the current trajectory can no longer make progress, it selects an earlier checkpoint, rewinds both context and environment, and resumes with a **rewind memory** summarizing what the failed attempt learned (falsified hypotheses, alternative strategies). The restored prefix is replayed from the execution log rather than regenerated/re-executed, so side effects outside the workspace filesystem are not re-triggered. The environment recovery boundary is the workspace directory tree: rewinding reverts modifications, restores deleted files, removes new files.

**MettleBench** — 82 tasks / 640 ordered acceptance criteria derived from five engineering benchmarks (Terminal-Bench 2.0, ProgramBench, SWE-bench, ProjectEval, GitTaskBench). Each task is one assignment with a hidden, ordered checklist; the backend returns natural-language feedback naming only the first unsatisfied criterion. Task success = all criteria; checklist prefix progress `ρ = ℓ/n` measures partial completion. Every task is screened for a valid forward-only solution so the benchmark is recovery-agnostic.

**Results.** AgentRewind achieves the highest task success + checklist progress across all compared strategies (Continue, Restart-with-Experiences, Safety Review) under GPT-5.4 and GPT-5.4 mini, and across three harnesses (mini-SWE-agent, FnCallAgent/Qwen-Agent, CodeAgent/smolagents). On Terminal-Bench 2.0: 83.1% vs 78.7% Continue. Paired recovery from 50 failed Continue endpoints: **30.0% recovery vs 8.0% Continue** (+12.2pp checklist progress). Ablation: removing **environment rewind** is the largest degradation (87.8 → 43.9 success), then rewind memory (→51.2), then context rewind (→65.9) — aligned context–environment restoration and rewind memory are complementary.

**Limitations.** Only controlled workspace state is restored (network/external-service effects are not undone); relies on external validation to detect stalled execution; forward-only bounded to deterministic/rollback-able environments.

| Verdict | **ADOPT** aligned context+env checkpoints + resume-from-checkpoint recovery with rewind memory. Clone `replay-agent-recorder` (MIT) + `MettleBench` (Apache-2.0) → **GO REFERENCE**. Runtime wiring `wont_wire` (framework layer; no CCC harness integration yet). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.14380-agentrewind-recoverable-execution-for-long-horiz.pdf`
