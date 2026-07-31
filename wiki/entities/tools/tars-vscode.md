---
title: TARS — VS Code Theory-of-Mind code explanation agent
type: entity
tags: [tool, vscode, personalization, theory-of-mind, mit, k192]
keywords: [leotodisco/tars, LangGraph, ToM profiler, VSIX]
related:
  - sources/arxiv-tars-theory-of-mind-ide-2607.15948.md
  - concepts/theory-of-mind-personalized-agent-explanations.md
  - concepts/client-as-first-order-harness-factor.md
  - entities/tools/cc-wf-studio.md
maturity: draft
created: 2026-07-20
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-ccc-harness.mdc"
---

## Relations

- `@sources/arxiv-tars-theory-of-mind-ide-2607.15948.md` — paper
- `@concepts/theory-of-mind-personalized-agent-explanations.md` — pattern steal
- `@concepts/client-as-first-order-harness-factor.md` — IDE harness factor
- `@entities/tools/cc-wf-studio.md` — other VS Code Claude tooling peer

## Raw Concept

`github.com/leotodisco/tars` — MIT VS Code extension: ToM profiler + RAG + inline explanations (LangGraph). Local clone `.local/adopts/tars` (~15MB).

## Narrative

### Phase-0

| Check | Result |
|-------|--------|
| License | **MIT** [CONFIRMED SPDX + LICENSE file] |
| Size | ~15MB — OK |
| Host | VS Code ≥1.97; OpenAI key via Configure Tars |
| Cursor | **Not a drop-in** — VSIX targets VS Code; pattern-port only |

### Verdict

**GO** local REFERENCE clone. **ADOPT** ToM profiler pattern into skills/rules. **NO-GO** as default Cursor extension until a Cursor-compatible build exists.

## Dead Ends

- Installing the VSIX into Cursor and expecting parity — different extension host; treat as reference only.
