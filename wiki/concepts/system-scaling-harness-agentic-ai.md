---
title: System scaling the harness — beyond model-centric agent eval
type: concept
tags: [concept, agent-harness, system-scaling, arxiv]
keywords: [2605.26112, system-scaling, auditable-harness, verifiable-orchestration]
related:
  - sources/arxiv-system-scaling-harness-2605.26112.md
  - concepts/code-as-agent-harness.md
  - concepts/harness-layer-competition-cursor-claude-perplexity.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/claude-code.md
  - "@osint-wiki/concepts/system-scaling-harness-evaluation.md"
  - concepts/runtime-harness-interface-adaptation.md
  - sources/arxiv-runtime-harness-adaptation-2605.22166.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/claim-drift-automated-research.md
  - concepts/agentic-web-infrastructure-gap-taxonomy.md
  - sources/arxiv-agentic-web-infrastructure-agentverse-2606.20570.md
  - concepts/os-level-agent-harness-android.md
  - sources/arxiv-aohp-os-level-agent-harness-2606.23449.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
maturity: draft
created: 2026-06-01
updated: 2026-06-23
---

## Relations

- `@sources/arxiv-system-scaling-harness-2605.26112.md` — arXiv 2605.26112
- `@concepts/code-as-agent-harness.md` — Cemini three-layer stack
- `@concepts/harness-layer-competition-cursor-claude-perplexity.md` — harness-as-product thesis (K92)
- `@concepts/thin-harness-fat-skills-garrytan.md` — complementary social framing (K93)

## Raw Concept

arXiv **2605.26112** (Gu) — agent progress requires **system scaling**: treat memory, retrieval, tools, orchestration, verification, and governance as measurable harness subsystems, not implementation footnotes.

## Narrative

### CCC evaluation checklist [TENTATIVE]

| Harness dimension | Cemini artifact |
|-------------------|-----------------|
| Auditable | `wiki/log.md`, git history, `@entities/tools/claude-mem.md` |
| Persistent | wiki git, stash, librarian (OSINT) |
| Modular | MCP servers, skills, subagents |
| Verifiable | `@concepts/agent-completion-verification-gates.md`, lint, pytest on prod |
| Orchestration | conductor, `@concepts/subagent-orchestration.md` |

**K122:** XCIENTIST argues eval unit should be **research trajectory** (synthesis + validation process), not final artifact alone — aligns with harness-dimension checklist above.

**Verdict:** **REFERENCE** — use when arguing for harness metrics in eval prompts (v5/v6/v8) vs model-only success rates.

## Snippets

> "Evaluation remains largely model-centric… treating memory, retrieval, tool use, orchestration, verification, and governance as secondary."
> — [Source: arxiv-2605.26112-from-model-scaling-to-system-scaling-scaling-the.pdf]
