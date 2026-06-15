---
title: PerspectiveGap — orchestration prompting failure taxonomy
type: concept
tags: [concept, perspectivegap, subagent, orchestration-prompting, k114]
keywords: [2606.08878, need-only-rule, prompt-economy, information-leakage, subagent-boundaries]
related:
  - sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md
  - concepts/subagent-orchestration.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/agent-completion-verification-gates.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/glasswing-deliberate-disagreement.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md` — arXiv 2606.08878 provenance
- `@concepts/subagent-orchestration.md` — when to dispatch; this page covers **what to put in the prompt**
- `@concepts/ship-subagent-writer-reviewer-tester.md` — concrete writer/reviewer/tester boundary pattern
- `@concepts/agent-completion-verification-gates.md` — inspect subagent prompts before execution
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — delivery failures after prompt is written
- `@entities/patterns/scatter-gather.md` — loop topologies from benchmark
- `@entities/patterns/glasswing-deliberate-disagreement.md` — adversarial separation of evaluator context

## Raw Concept

2606.08878 **PerspectiveGap** — benchmark + failure taxonomy for **orchestration prompting**: can the parent LLM assign each sub-agent only the context fragments that role needs (**need-only rule**)?

## Narrative

### Distinct capability [CONFIRMED — 27-model eval]

Orchestration prompting is **not reducible to coding skill**. Opus 4.7 underperforms on PerspectiveGap despite strong SWE-bench posture. Parent agents must reason from each sub-agent's **perspective**, not flatten all context into every role prompt.

### Five failure modes (CCC steal-from)

| # | Mode | Symptom | Cemini mitigation |
|---|------|---------|-------------------|
| 1 | **Distractor leakage** | Parent passes prompt-engineering tips / meta-advice into subagent prompt | Strip parent-only instructions from Task `prompt`; keep subagent envelope task-scoped |
| 2 | **Out-of-role leakage** | Role A's private context copied to Role B (reward-hacking channel) | `/ship` private-test boundary; SkillHone redacted evidence pattern |
| 3 | **Artifact ownership confusion** | Handoff instructions sent to wrong role (PLAN.md vs SOLUTION.md swap) | Explicit artifact ownership in subagent template; one writer per file |
| 4 | **Dropped shared context** | Shared background omitted from roles that need it | Repeat minimal shared context block in each role that requires it |
| 5 | **Bootstrap paradox** | Instruction to read artifact placed inside artifact; or redundant no-go rules | Put read instructions in dispatch envelope, not inside deliverable template |

### Prompt Economy

Loop-centered topologies (coder–reviewer, dispatcher–worker–critic) amortize prompt-engineering cost: fixed N role prompts, repeated invocations. Aligns with `@concepts/ship-subagent-writer-reviewer-tester.md` and critic-loop patterns in `@entities/patterns/scatter-gather.md`.

### Operational posture

| Verdict | Guidance |
|---------|----------|
| **REFERENCE** | Do not assume Cursor/Claude Code Task prompts preserve boundaries |
| Inspect | Parent should review subagent `prompt` for need-only violations on Tier-2 or high-stakes dispatch |
| Measure | PerspectiveGap repo available for regression if customizing orchestrator |

Assignment-vs-writing gap: models may pass fragment-ID assignment yet fail free-form prompt writing — knowledge of boundaries ≠ execution when composing natural-language instructions.

## Snippets

> "The failures are not cosmetic: models leak distractors, expose out-of-role information, drop shared context, confuse artifact ownership, and sometimes place instructions where the sub-agent cannot see them."

> "Each role receives exactly the fragments it needs to do its stated job."

> — [Source: arxiv-2606.08878-perspectivegap-a-benchmark-for-multi-agent-orche.pdf §3,6, retrieved 2026-06-13]
