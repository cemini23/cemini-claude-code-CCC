---
title: Verifiable deterministic agent benchmarking
type: concept
tags: [concept, evaluation, verifiable, harness, benchmark, k203]
keywords: [2607.19262, BioSecBench, deterministic grading, model-harness pairs]
related:
  - sources/arxiv-biosecbench-surveillance-2607.19262.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/businesscasebench-rubric-from-expert-solutions.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - sources/brief-k202-k205-agents-langgraph-biosec-2026-07-22.md
  - "@cybersecurity-wiki/concepts/biosecbench-surveillance-verifiable-agent-eval.md"
  - concepts/agent-completion-verification-gates.md
  - concepts/traceable-scholarship-citation-first-generation.md
maturity: draft
created: 2026-07-22
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-biosecbench-surveillance-2607.19262.md` — provenance
- Cybersec domain: `@cybersecurity-wiki/concepts/biosecbench-surveillance-verifiable-agent-eval.md`
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — eval discipline
- `@concepts/businesscasebench-rubric-from-expert-solutions.md` — subjective rubric peer (K193)

## Raw Concept

K203 BioSecBench methodology (biosec domain routed out): give agents the same inputs a human gets; grade **structured answers deterministically**; report **model×harness** jointly. Best frontier configs still ~50% on hard surveillance tasks.

## Narrative

### Steal (ADOPT)

1. Prefer deterministic graders over LLM-as-judge when answers can be structured.
2. Always log harness alongside model — PI vs Codex gaps matter.
3. Score surrounding choices (thresholds, refs, filters) separately from "picked the right workflow."
4. Local `biosecbench-surveillance` Apache REFERENCE (~208KB) for eval packaging shape — **not** a CCC biosec ops install.

| Verdict | **ADOPT** verifiable-eval checklist; biosec content → cybersec |
