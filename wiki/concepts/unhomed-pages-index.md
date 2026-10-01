---
title: Unhomed pages index — pages with no concept parent
type: concept
tags: [concept, index, hygiene, ood, parked]
keywords: [orphan, no concept home, OOD stub, parked, receipts, maintenance]
related:
  - concepts/cross-wiki-routing.md
  - concepts/phase1-adopt-wire.md
  - sources/arxiv-poisson-image-denoising-2609.07916.md
  - sources/arxiv-hvac-llm-building-energy-2609.05314.md
  - sources/arxiv-buildocc-llm-occupant-agent-building-energy-2609.02729.md
  - sources/arxiv-drivemcp-adas-agentic-framework-2609.17247.md
  - sources/arxiv-kopa-bench-korean-public-api-2609.05395.md
  - sources/arxiv-muslim-arabic-voice-ai-platform-2609.31511.md
  - sources/arxiv-structured-reasoning-cvsa-safety-2609.31524.md
  - sources/arxiv-ascent-clinical-mcp-agents-2609.24620.md
  - sources/arxiv-obstacle-aware-harness-robot-manipulation-2609.20822.md
  - sources/arxiv-hierarchical-spm-agentic-orchestration-2609.04015.md
  - sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28.md
  - briefs/2026-07-16_deep-interaction-cot-edit-ux-ood.md
  - briefs/2026-07-17_statistical-self-consistency-macro-fallacy-ccc.md
  - sources/arxiv-2609-29333-llm-graders-cs-exams-routed.md
  - sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md
  - entities/tools/caveman.md
  - entities/tools/zero.md
  - entities/tools/portable-llm-wiki.md
  - entities/tools/astryx.md
  - concepts/adk-arena-agent-framework-benchmark.md
  - sources/arxiv-harness-zero-harness-distillation-2609.24974.md
hub: true
maturity: draft
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@concepts/cross-wiki-routing.md` — the routing decisions most of these rows record
- `@concepts/phase1-adopt-wire.md` — where an unhomed page graduates once it earns a wire

## Raw Concept

Wiki lint flags pages with zero inbound `related:` links. After the 2026-10-01 cleanup, 21 pages
remain. They fall into three honest groups, and none of them is a defect:

1. **OOD receipts** — a wave ingest saw an out-of-domain paper, judged it not-CCC, and wrote a short
   stub so the judgment is recorded rather than lost. `wont_wire` by construction.
2. **Cross-wiki routes** — content routed in from a sibling wiki whose primary lives there.
3. **Tools awaiting a concept home** — adopted or steal-from, but the concept page that should own
   them does not exist yet.

This page is their home so they stay discoverable, and it doubles as the worklist for group 3.

## Narrative

### Group 1 — OOD receipts (`wont_wire`, kept deliberately)

| Page | What it is |
|------|-----------|
| [`sources/arxiv-poisson-image-denoising-2609.07916.md`](../sources/arxiv-poisson-image-denoising-2609.07916.md) | Medical/astronomical Poisson noise restoration — classical signal processing |
| [`sources/arxiv-hvac-llm-building-energy-2609.05314.md`](../sources/arxiv-hvac-llm-building-energy-2609.05314.md) | Review of LLMs for HVAC/building automation |
| [`sources/arxiv-buildocc-llm-occupant-agent-building-energy-2609.02729.md`](../sources/arxiv-buildocc-llm-occupant-agent-building-energy-2609.02729.md) | LLM occupant agents for building energy |
| [`sources/arxiv-drivemcp-adas-agentic-framework-2609.17247.md`](../sources/arxiv-drivemcp-adas-agentic-framework-2609.17247.md) | ADAS driver-assistance agent framework |
| [`sources/arxiv-kopa-bench-korean-public-api-2609.05395.md`](../sources/arxiv-kopa-bench-korean-public-api-2609.05395.md) | Multi-step tool-calling over Korean public APIs |
| [`sources/arxiv-muslim-arabic-voice-ai-platform-2609.31511.md`](../sources/arxiv-muslim-arabic-voice-ai-platform-2609.31511.md) | Deployed Arabic voice AI platform |
| [`sources/arxiv-structured-reasoning-cvsa-safety-2609.31524.md`](../sources/arxiv-structured-reasoning-cvsa-safety-2609.31524.md) | Interpretable critical-care safety reasoning |
| [`sources/arxiv-ascent-clinical-mcp-agents-2609.24620.md`](../sources/arxiv-ascent-clinical-mcp-agents-2609.24620.md) | Clinical agentic system over MCP |
| [`sources/arxiv-obstacle-aware-harness-robot-manipulation-2609.20822.md`](../sources/arxiv-obstacle-aware-harness-robot-manipulation-2609.20822.md) | Safe robot manipulation harness |
| [`sources/arxiv-hierarchical-spm-agentic-orchestration-2609.04015.md`](../sources/arxiv-hierarchical-spm-agentic-orchestration-2609.04015.md) | Hierarchical SPM automation orchestration |
| [`sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28.md`](../sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28.md) | Haitian Creole cultural-awareness eval |
| [`briefs/2026-07-16_deep-interaction-cot-edit-ux-ood.md`](../briefs/2026-07-16_deep-interaction-cot-edit-ux-ood.md) | Deep Interaction CoT-edit UX (OOD from Cybersec) |
| [`briefs/2026-07-17_statistical-self-consistency-macro-fallacy-ccc.md`](../briefs/2026-07-17_statistical-self-consistency-macro-fallacy-ccc.md) | Statistical self-consistency / macro fallacy (from Cybersec) |

### Group 2 — cross-wiki routes (primary lives on the source wiki)

| Page | Routed in from |
|------|---------------|
| [`sources/arxiv-2609-29333-llm-graders-cs-exams-routed.md`](../sources/arxiv-2609-29333-llm-graders-cs-exams-routed.md) | image-gen |
| [`sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md`](../sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md) | Cybersecurity |

### Group 3 — tools awaiting a concept home (worklist)

| Page | Verdict | Likely home |
|------|---------|-------------|
| [`entities/tools/caveman.md`](../entities/tools/caveman.md) | Adopt as opt-in mode | `concepts/token-economics-and-prompt-caching.md` |
| [`entities/tools/zero.md`](../entities/tools/zero.md) | Adopt as trial/reference | coding-harness cluster |
| [`entities/tools/portable-llm-wiki.md`](../entities/tools/portable-llm-wiki.md) | Steal-from | wiki-protocol cluster |
| [`entities/tools/astryx.md`](../entities/tools/astryx.md) | Steal-from | design-system cluster |
| [`concepts/adk-arena-agent-framework-benchmark.md`](adk-arena-agent-framework-benchmark.md) | OSINT handoff | agent-framework benchmark cluster |
| [`sources/arxiv-harness-zero-harness-distillation-2609.24974.md`](../sources/arxiv-harness-zero-harness-distillation-2609.24974.md) | ADOPT awareness | harness-distillation concept (K379) |

**Rule for future waves:** when an ingest judges a paper out of domain, it should link the stub here
rather than leave it unlinked. That keeps the lint signal meaningful — an orphan should mean "someone
forgot", not "someone decided".

## Snippets

> "Wiki lint flags pages with zero inbound `related:` links." [Source: `scripts/wiki_lint.py`, check 1]
