---
title: Scaffolding matters more than MCP vs CLI interface (K262)
type: concept
tags: [concept, harness, mcp, cli, scaffolding, k262]
keywords: [2608.08654, scaffold, tool-cost, HarnessOpt]
related:
  - sources/arxiv-scaffolding-matters-more-than-interface-2608.08654.md
  - entities/tools/scaffolding-mcp-cli-study.md
  - concepts/model-harness-six-responsibilities.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
  - concepts/phase1-adopt-wire.md
  - entities/tools/vectrayx-vision-1b.md
  - sources/arxiv-vectrayx-vision-1b-cyber-vlm-2608.08477.md
  - concepts/black-box-rl-opaque-harness-optimization.md
  - sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-11
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-scaffolding-matters-more-than-interface-2608.08654.md`
- `@entities/tools/scaffolding-mcp-cli-study.md`
- `@concepts/model-harness-six-responsibilities.md`

## Raw Concept

When comparing MCP vs CLI (or any tool transport), what actually drives cost and success?

## Narrative

K262 (2608.08654): across seven scaffolds × five models on one verified git task, **scaffolding dominates** interface choice. CLI-only scaffolds can fully succeed; MCP is not required for that workload.

### Steal (ADOPT)

1. Benchmark / optimize **agent scaffolding** (prompts, control flow, memory, verify) before blaming MCP vs CLI.
2. Verify completion via **external state** (repo/tests), not agent self-report.
3. Pairs HarnessOpt-Bench (K226): harness axis first-class.

| Verdict | **ADOPT** policy. |
