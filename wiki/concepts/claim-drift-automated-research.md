---
title: Claim drift — automated research failure mode
type: concept
tags: [concept, harness, verification, ai-scientist, k122]
keywords: [2606.18874, claim-drift, semantic-drift, experimental-drift, mechanistic-drift]
related:
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - concepts/externalized-research-synthesis-validation.md
  - entities/tools/xcientist.md
  - concepts/agent-completion-verification-gates.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/system-scaling-harness-agentic-ai.md
  - concepts/code-as-agent-harness.md
  - entities/tools/deep-scientist.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/skills/grill-with-docs.md
  - entities/skills/to-issues.md
  - concepts/autonomous-coding-agents-enterprise-data.md
  - concepts/cross-model-verified-agent-translation.md
  - sources/arxiv-data-intelligence-agents-dia-2606.19319.md
  - sources/brief-k122-xcientist-claim-drift-prod-2026-06-22.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
maturity: draft
created: 2026-06-22
updated: 2026-07-14
---

## Relations

- `@sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md` — XCIENTIST provenance (2606.18874)
- `@concepts/externalized-research-synthesis-validation.md` — harness designed to reduce drift
- `@concepts/agent-completion-verification-gates.md` — completion proof vs drift at ship boundary
- `@concepts/handoff-validity-agent-harness.md` — handoff contracts preserve claim structure

## Raw Concept

What happens when an automated research run produces plausible code and scores, but the **mechanism in the proposal** is not preserved through implementation and validation?

## Narrative

**Claim drift** [CONFIRMED — 2606.18874 + AI-Scientist-v2 diagnostic runs]: mismatch between the mechanism asserted in a research proposal and what the executable system actually tests or attributes.

### Three subtypes (steal-for harness eval)

| Subtype | Research example | CCC harness analogue |
|---------|------------------|----------------------|
| **Semantic drift** | Memory "revision" is shallow text rewrite without auditable evidence update | Subagent summary rewrites task without preserving cited file paths / test evidence |
| **Experimental drift** | Claimed ablation becomes unrelated standalone model | "Fixed CI" that changes unrelated files; ingest that updates index without source provenance |
| **Mechanistic drift** | Score improvement cannot be tied to claimed component | Lint pass attributed to wrong fix; hook "works" but bypasses the stated verification gate |

### Detection heuristics [TENTATIVE]

- Proposal mechanism keywords ≠ changed files / ablation scope in trace
- Report cites functions or paths that do not exist in workspace artifacts
- Parent task acceptance criteria satisfied locally but integration claim unsubstantiated

### Mitigations (XCIENTIST + CCC mapping)

| XCIENTIST mechanism | Cemini artifact |
|---------------------|-----------------|
| Persistent idea states + repair traces | `wiki/log.md`, git history, OpenSpec specs |
| Validation contracts per step | OpenSpec AC, `/goal` done-criteria, `wiki_lint.py` |
| Component attribution via ablation | Phase-0 scripts, targeted subagent scopes |
| Claim-boundary audit before write | Premortem, ingest "discuss before write", brief → prod gate |

**Verdict:** **REFERENCE** taxonomy — add to eval prompts (v8+) and HarnessFix flaw records when symptom is "looks done but claim unsupported."

## Snippets

> "Claim drift occurs when the mechanism asserted in a proposal is not preserved with sufficient structure through implementation and validation."
> — [Source: arxiv-2606.18874-externalizing-research-synthesis-and-validation.pdf, retrieved 2026-06-22]
