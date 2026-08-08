---
title: Programmatic vs JSON tool calling (bitter lesson) (K258)
type: concept
tags: [concept, tool-calling, programmatic, code-mode, k258]
keywords: [2608.06370, PTC, BFCL, execute_python, CodeAct]
related:
  - sources/arxiv-bitter-lesson-tool-calling-2608.06370.md
  - entities/tools/programmatic-tool-calling-ptc.md
  - concepts/code-as-agent-harness.md
  - concepts/maven-agentic-tool-calling-generalization.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - briefs/2026-08-07_phase1-wire-status-closeout-k254-k258.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-bitter-lesson-tool-calling-2608.06370.md`
- `@entities/tools/programmatic-tool-calling-ptc.md`
- `@concepts/code-as-agent-harness.md`

## Raw Concept

Should code-capable models call tools via JSON schemas or via executable scripts over typed stubs?

## Narrative

K258 (arXiv **2608.06370**): on BFCL v4, programmatic tool calling (PTC) matches/beats native JSON in 11/14 models; stronger under parallel fan-out; more stable under context rot. Aligns with CodeAct / Cloudflare Code Mode / `@concepts/code-as-agent-harness.md`.

### Cemini steal (ADOPT)

1. For code-capable agent lanes (Claude Code, Cursor): prefer code/script composition for multi-tool chains and fan-out when a sandboxed executor exists.
2. Keep JSON schemas for weak models / strict API gateways; do not force PTC where code exec is banned.
3. PTC does not remove schema-bound / Prebind needs (K151 / K198) — stubs still typed; execution still gated.
4. Measure under context rot — JSON degrades while PTC held in this study.

| Verdict | **ADOPT** PTC policy for capable models. **NO-GO** install. Entity `policy_wired`. |
