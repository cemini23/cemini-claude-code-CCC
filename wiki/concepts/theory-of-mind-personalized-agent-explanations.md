---
title: Theory-of-Mind personalized agent explanations
type: concept
tags: [concept, personalization, theory-of-mind, ide, ux, k192]
keywords: [2607.15948, ToM profiler, perspective taking, RAG explanations, TARS]
related:
  - sources/arxiv-tars-theory-of-mind-ide-2607.15948.md
  - entities/tools/tars-vscode.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/agent-skills-progressive-disclosure.md
  - entities/patterns/full-prompt-goal-template.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@sources/arxiv-tars-theory-of-mind-ide-2607.15948.md` — provenance
- `@entities/tools/tars-vscode.md` — MIT VS Code reference clone
- `@concepts/client-as-first-order-harness-factor.md` — IDE as harness
- `@concepts/agent-skills-progressive-disclosure.md` — depth control peer
- `@entities/patterns/full-prompt-goal-template.md` — operator profile in goal envelope

## Raw Concept

K192 TARS: store a lightweight developer **mind profile** (expertise, role, style) and adapt explanation depth/tone; ground in project docs via RAG; keep explanations in-IDE.

## Narrative

### Steal checklist (ADOPT)

1. One short profiler quiz (or settings) → persistent profile, not per-prompt "explain like I'm X".
2. Adapt **depth and tone**, not just verbosity — juniors get scaffolding; seniors get diffs/assumptions.
3. Prefer **in-surface** answers (inline / panel) over copy-paste to chat when the host allows.
4. Cursor: implement as skill/rule pattern; do not expect TARS VSIX to load in Cursor without a port.

| Verdict | **ADOPT** ToM profiler pattern; **GO** local MIT clone REFERENCE; **NO-GO** blind Cursor install of VS Code VSIX |

## Snippets

> "Built around a lightweight Theory of Mind paradigm, TARS profiles a developer's expertise, role, and stylistic preferences"
> — [Source: arxiv-2607.15948]
