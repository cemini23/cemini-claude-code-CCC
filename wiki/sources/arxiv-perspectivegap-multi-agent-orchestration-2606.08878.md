---
title: PerspectiveGap — multi-agent orchestration prompting benchmark (arXiv 2606.08878)
type: source
tags: [source, arxiv, perspectivegap, orchestration-prompting, benchmark, k114]
keywords: [2606.08878, perspectivegap, need-only-rule, prompt-economy, subagent-prompts]
related:
  - concepts/perspectivegap-orchestration-prompting.md
  - concepts/subagent-orchestration.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/agent-completion-verification-gates.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/glasswing-deliberate-disagreement.md
maturity: draft
read_status: read
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@concepts/perspectivegap-orchestration-prompting.md` — CCC failure taxonomy synthesis
- `@concepts/subagent-orchestration.md` — Task-tool dispatch context
- `@concepts/ship-subagent-writer-reviewer-tester.md` — writer/reviewer boundary exemplar
- `@concepts/agent-completion-verification-gates.md` — inspect generated subagent prompts before dispatch
- `@entities/patterns/scatter-gather.md` — loop-centered topology family
- `@entities/patterns/glasswing-deliberate-disagreement.md` — information-boundary discipline

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting |
| **Authors** | Youran Sun, Xingyu Ren, Kejia Zhang, Xinpeng Liu, Jiaxuan Guo |
| **arXiv** | 2606.08878v1 [cs.CL] |
| **Release** | github.com/WhymustIhaveaname/PerspectiveGap |
| **Location** | `raw-sources/arxiv-2606.08878-perspectivegap-a-benchmark-for-multi-agent-orche.pdf` |
| **Retrieved** | 2026-06-13 |
| **Read status** | read — benchmark design, 27-model eval, five failure modes |

## Narrative

**PerspectiveGap** evaluates whether a **main agent** can compose **orchestration prompts** for sub-agents — assigning each role only the information fragments it needs (**need-only rule**). 110 scenarios, 10 loop-centered topologies (cr, dcr, dpc, …), 2–6 roles, 7–13 shuffled fragments + one distractor per scenario.

Two task formats per scenario:

1. **Role-fragment assignment** — map fragment IDs to roles
2. **Free-form prompt writing** — write actual sub-agent prompts (deterministic containment scorer, 716-row human audit)

**Results (27 commercial models):** avg combined strict pass **14.9%**; GPT-5.5 leads at **62.0%**; deepseek-v4-pro second at **32.0%**. Opus 4.7 underperforms vs coding benchmarks. Avg overall leakage **246.5%** (per-role leak events; can exceed 100%).

**Prompt Economy framing:** engineering cost fixed by number of role prompts; benefit accrues across repeated loop invocations — favors critic-loop topologies.

**CCC relevance:** orchestration prompting is **distinct from coding skill**. Generated Task/subagent prompts need human or rubric inspection before trust. Steal need-only discipline for `.claude/agents/` and parent→subagent brief envelopes.

## Snippets

> "Orchestration prompting is a capability distinct from the coding ability current benchmarks reward."

> "Generated sub-agent prompts should not be assumed to preserve role-specific information boundaries without inspection."

> — [Source: arxiv-2606.08878-perspectivegap-a-benchmark-for-multi-agent-orche.pdf §6–7, retrieved 2026-06-13]
