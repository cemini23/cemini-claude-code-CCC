---
title: Operator model selection for workflows and subagents
type: concept
tags: [models, workflows, subagents, codex, claude, k142]
keywords: [gpt-5.5, sonnet-5, opus-4.8, fable-5, codex exec, model selection]
related:
  - concepts/failure-mode-harness-adaptation-mapping.md
  - concepts/mcp-multi-agent-graceful-degradation-stack.md
  - concepts/local-open-weight-agentic-coding-eval.md
  - sources/arxiv-agentic-coding-without-cloud-2607.21482.md
  - entities/tools/openai-codex-cli.md
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - sources/arxiv-screenshots-or-tools-gui-mcp-2608.03327.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - sources/arxiv-canary-tools-mcp-tool-selection-2608.04719.md
  - concepts/canary-tools-mcp-selection-diagnosis.md
  - entities/tools/canary-tools-mcp.md
maturity: draft
created: 2026-07-03
updated: 2026-08-06
---

## Relations

- Source screenshot: `x.jpeg` archived through OSINT K142.
- `@concepts/failure-mode-harness-adaptation-mapping.md` — K168: cheap-model tier via harness adaptation on low-diversity tasks

## Narrative

Operator policy from K142 screenshot: cost is a tie-breaker only. For anything that ships, rank tradeoffs as **intelligence > taste > cost**. Use GPT-5.5 for bulk/mechanical Codex CLI work where effectively free; use higher-taste Claude models for user-facing UI/copy/API design and independent reviews. Never use Haiku.

Availability/pricing is operator-specific and should remain `[NEEDS VERIFICATION 2026-07-03]`; treat this as routing policy, not benchmark truth.

### K245 — MCP benefit sign-flip (2026-08-05)

Identical GUI–MCP harness: reasoning models **+4.0pp** with MCP tools; non-reasoning **−5.9pp**. Model tier matters for whether MCP availability helps — see `@concepts/hybrid-gui-mcp-tool-adoption-gap.md`.

### K250 — CSR tier≠safety (2026-08-06)

K250 Canary Tools: CSR varies ~36× across models; **capability mirages trap frontier** models while other canary types fire on small models. Do not equate model tier with MCP tool-selection safety. See `@concepts/canary-tools-mcp-selection-diagnosis.md`.

| Model | Cost | Intelligence | Taste |
|-------|------|--------------|-------|
| gpt-5.5 | 9 | 8 | 5 |
| sonnet-5 | 5 | 5 | 7 |
| opus-4.8 | 4 | 7 | 8 |
| fable-5 | 2 | 9 | 9 |
