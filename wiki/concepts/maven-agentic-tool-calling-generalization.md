---
title: MAVEN — generalization in agentic tool calling
type: concept
tags: [concept, tool-calling, mcp, arxiv]
keywords: [maven, 2605.30738, tool-orchestration, cross-domain]
related:
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - concepts/mcp-context-optimization.md
  - entities/tools/lazy-tool.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/subagent-orchestration.md
  - concepts/code-as-agent-harness.md
  - "@osint-wiki/concepts/mcp-tool-calling-eval-scaffold.md"
maturity: draft
created: 2026-06-02
updated: 2026-06-05
---

## Relations

- `@sources/arxiv-maven-agentic-tool-calling-2605.30738.md` — canonical source page (K94)
- `@concepts/mcp-context-optimization.md` — tool surface discipline
- `@entities/tools/lazy-tool.md` — deferred MCP discovery
- `@concepts/failed-trajectory-harness-repair.md` — complementary: MAVEN generalizes tool *calling*; HarnessFix repairs harness *flaws*
- `@concepts/etclovg-harness-layers.md` — shared layer vocabulary
- `@osint-wiki/sources/arxiv-maven-agentic-tool-calling-2605.30738-2026-06-05.md` — OSINT K100 read

## Raw Concept

arXiv **2605.30738** — tool-calling agents fail to **compose strategies** and **preserve intermediate state** across benchmark domains. MAVEN adds modular verification + execution scaffolding.

**K100 dedupe:** stub source `arxiv-maven-agentic-tool-calling-2605.30738-2026-06-05.md` removed; OSINT K100 deep-read retained as `read` on canonical source.

## Narrative

| MAVEN idea | CCC mapping |
|------------|-------------|
| Structured decomposition | `/goal`, OpenSpec, subagent fan-out |
| Adaptive tool orchestration | conductor + lazy-tool + MCP allowlists |
| Cross-domain generalization | **REFERENCE** — evaluate against real CCC MCP matrix before adopt |

**Verdict:** **REFERENCE** — benchmark for designing tool-calling eval harnesses, not a prod dependency.

## Snippets

> "Generalization across agentic tool-calling environments remains a central challenge."
> — [Source: arxiv-2605.30738-maven-improving-generalization-in-agentic-tool-calling.pdf]
