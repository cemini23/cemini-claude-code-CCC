---
title: OpenSpec — spec-driven workflow for AI coding agents
type: entity
tags: [tool, spec-driven, openspec, workflow, claude-code, agent]
keywords: [openspec, spec-driven development, requirements, acceptance criteria, agent spec]
related:
  - entities/tools/claude-code.md
  - entities/patterns/ralph-loop.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/spec-kit.md
  - concepts/2026-05-13_tolaria-steal-from-patterns.md
  - concepts/code-as-agent-harness.md
  - entities/tools/the-architect.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/claude-code-software-factory.md
  - concepts/claude-premortem-skill.md
  - entities/tools/bmad-creative-intelligence-suite.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agentic-pm-review-artifacts.md
  - concepts/autosci-memory-centric-research-agents.md
  - sources/arxiv-autosci-2605.31468.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/llm-as-code-agentic-programming.md
maturity: draft
created: 2026-05-13
updated: 2026-06-16
---

## Relations

- `@entities/tools/claude-code.md` — primary consumer of OpenSpec specs
- `@entities/patterns/ralph-loop.md` — Ralph's `prd.json` is structurally similar to an OpenSpec spec
- `@entities/patterns/full-prompt-goal-template.md` — both are ways of pinning "what done looks like"
- `@concepts/2026-05-13_tolaria-steal-from-patterns.md` — refactoring-workflow patterns (incremental migrations, workflow design language); spec-driven-workflow neighbour
- `@concepts/code-as-agent-harness.md` — OpenSpec as regression-free harness-improvement workflow
- `@concepts/graphflow-verifiable-agent-workflows.md` — spec contracts without compile-time proof (contrast)
- `@concepts/skillrae-retrieval-augmented-execution.md` — compiled skill context vs static spec documents
- `@concepts/claude-code-software-factory.md` — spec gate before multi-repo factory fan-out (K67)
- `@concepts/claude-premortem-skill.md` — failure-mode review before large spec-driven harness changes

Cross-wiki: `@osint-wiki/entities/tools/openspec.md` is the OSINT-side entity (where Cemini first audited it).

## Narrative

OpenSpec is a **spec-driven workflow tool** for AI coding agents. It encodes a project's requirements as a versioned spec document (markdown + structured frontmatter), then drives an agent (typically Claude Code or Codex) to implement against that spec iteration by iteration. The spec is the contract; the agent's job is to close every acceptance criterion.

The private `osint-wiki` workspace cloned the OpenSpec repository at `openspec/` during a K-cycle audit. Cemini has not yet adopted OpenSpec for daily Cemini workflows — it remains a Tier-2 candidate in the workflow-tool field, alongside Ralph's `prd.json` pattern and the `/goal` single-shot template. The three are structurally similar (all encode "what done looks like") but differ in execution model:

| Tool | Execution model | State location | Best for |
|------|-----------------|----------------|----------|
| OpenSpec | Spec-driven, agent re-reads spec each iteration | Versioned spec document | Multi-feature projects with stable scope |
| Ralph `prd.json` | Loop-based, agent re-reads prd.json + progress.txt each iteration | `prd.json` + `progress.txt` + git | Long-running iterations with fresh context per loop |
| `/goal` template | Single-shot, agent reads goal once and executes end-to-end | Inline in prompt envelope | Discrete tasks with clear acceptance criteria |

**Where Cemini might adopt OpenSpec**: any workflow that needs *cross-session spec stability*. The CCC bootstrap itself (this session) is a candidate retroactively — the goal-condition encoded 8 success criteria, which would translate cleanly into an OpenSpec spec. The reason Cemini used the `/goal` template instead: bootstrap is one-shot; an OpenSpec spec is over-engineered for a single execution.

**Phase-0 status**: OSINT-side entity page (`@osint-wiki/entities/tools/openspec.md`) carries the canonical license + maturity verdict. CCC defers to that page rather than duplicating audit content.

**Comparison to Cemini's `/goal` template**: OpenSpec encodes more structure (per-feature task graphs, dependency tracking) but at the cost of authoring overhead. The `/goal` template is denser and fits within a single prompt envelope. For Cemini's solo-dev cadence the `/goal` template is the modal choice; OpenSpec earns its slot when scope outgrows a single envelope.

## Dead Ends

- **Treating OpenSpec, Ralph, and `/goal` as interchangeable** — they're not. They share a goal-pinning function but differ in execution model and authoring overhead.
- **Adopting OpenSpec without an active project that justifies the authoring cost** — premature; would create dead spec docs that drift from reality.
