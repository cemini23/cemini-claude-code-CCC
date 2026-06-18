---
title: pegasus-ai — Pegasus Claude plugin marketplace
type: entity
tags: [tool, pegasus, claude-plugin, scientific-workflow, k118]
keywords: [pegasus-isi, claude-plugin-marketplace, pegasus-ai, apache-2.0]
related:
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
maturity: draft
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- `@sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md` — arXiv 2606.18425 evaluation paper
- `@concepts/specification-driven-scientific-workflow-management.md` — specification-driven pipeline
- `@concepts/claude-plugins-catalog-patterns.md` — marketplace install discipline
- `@concepts/skill-vetting.md` — Phase-0 before plugin use
- `@entities/mcp-servers/anthropic-skills.md` — skill/plugin ecosystem peer

## Raw Concept

`github.com/pegasus-isi/claude-plugin-marketplace` — **pegasus-ai** plugin with eight Pegasus workflow skills cited in 2606.18425.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `pegasus-isi/claude-plugin-marketplace` |
| **License** | Apache-2.0 (API verified 2026-06-18) |
| **Stars** | ~0 (2026-06-18) |
| **Pegasus core** | `pegasus-isi/pegasus` — Apache-2.0, ~232★ |

### pegasus-ai skills (paper)

| Skill | Role |
|-------|------|
| `/pegasus-scaffold` | Full workflow project from pipeline description |
| `/pegasus-wrapper` | Tool wrapper scripts |
| `/pegasus-dockerfile` | Container definitions |
| `/pegasus-debug` | Failure diagnosis from logs |
| `/pegasus-review` | Anti-pattern / correctness review |
| `/pegasus-convert` | Format conversion |
| `/pegasus-help` | Context-aware Pegasus docs |
| `/kiso` | Kiso experiment configs |

### CCC posture

| Question | Answer |
|----------|--------|
| Adopt for Cemini prod? | **No** — HPC/Pegasus scientific stack; not conductor/wiki harness |
| CCC value | **REFERENCE** — spec-before-code plugin pattern; MCP remote WMS control |
| Phase-0 | `scripts/adopt_k118_phase0.sh` — clone + license check |

**Verdict:** CONDITIONAL-GO **reference only** — install only if operator runs Pegasus workflows on FABRIC/HPC.

## Snippets

> "Plugin marketplace serves as a curated collection … pegasus-ai provides skills for Pegasus-based workflow authoring."

> — [Source: arxiv-2606.18425-from-specification-to-execution-ai-assisted-scie.pdf]
