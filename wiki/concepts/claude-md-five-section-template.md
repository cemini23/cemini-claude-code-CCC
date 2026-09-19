---
title: CLAUDE.md five-section template — Role / Style / Constraints / Workflow / Quality
type: concept
tags: [concept, claude-md, prompting, schema, k76]
keywords: [five-section, role, style, constraints, workflow, quality, bootstrap]
related:
  - concepts/claude-code-skills-md-institutional-memory.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/asd-ste100-writing-style.md
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - concepts/claude-premortem-skill.md
  - sources/trading-posts-macro-charts-skills-md-2026-05-28.md
  - concepts/claude-harness-dynamic-workflows-k88.md
maturity: draft
created: 2026-05-28
updated: 2026-08-25
cross-wiki-source: "@osint-wiki/concepts/claude-code-skills-md-workflow.md"
---

## Relations

- `@concepts/claude-code-skills-md-institutional-memory.md` — Skills.md layer beneath CLAUDE.md schema
- `@concepts/twelve-rule-claude-md-template.md` — rule-discipline template (complementary, not duplicate)
- `@concepts/asd-ste100-writing-style.md` — **Style** section for readable technical prose (required on new CLAUDE.md)
- `@entities/tools/claude-code.md` — harness that loads CLAUDE.md every session
- `@concepts/context-engineering.md` — persistent schema as context lever
- `@concepts/claude-premortem-skill.md` — pre-ship review before changing harness files

Cross-wiki: `@osint-wiki/concepts/claude-code-skills-md-workflow.md`, `@osint-wiki/concepts/cemini-repository-topology.md`.

## Raw Concept

K76 — five-section CLAUDE.md hierarchy for bootstrap in ~15 minutes. Hierarchy: **system setup (CLAUDE.md / Skills.md) → prompts → output**.

## Narrative

### Five sections

| Section | Purpose | Example constraint |
|---------|---------|-------------------|
| **Role** | Specific operator persona | "CCC wiki librarian agent" not generic assistant |
| **Style** | Output shape | **ASD-STE100** adapted prose — short sentences, one term per concept; see `@osint-wiki/concepts/asd-ste100-writing-style.md` |
| **Constraints** | Hard boundaries | Never commit secrets; never invent wiki pages |
| **Workflow** | Step pipeline | Read index → pages → `@relations` → synthesize |
| **Quality** | Pre-delivery checklist | Lint clean; bidirectional links |

### vs 12-rule template

- **Five-section** = structural scaffold for new CLAUDE.md files.
- **12-rule** = operational discipline for agent failure modes (token budget, fail loud, checkpoint discipline).

Use both: five-section for shape; 12-rule for behavioral guardrails. CCC's own `CLAUDE.md` is schema-heavy; sibling wikis may use subsystem CLAUDE.md per `@osint-wiki/concepts/cemini-repository-topology.md`.

### 15-minute bootstrap recipe [TENTATIVE]

1. Draft Role + Constraints (5 min).
2. Add Workflow mirroring your real session ritual (5 min).
3. Add **Style (ASD-STE100)** + Quality gates tied to verifiable commands (5 min). Paste block: `@osint-wiki/scripts/snippets/claude-md-ste100-section.md`.
4. Link to 2–3 skill files rather than duplicating skill bodies in CLAUDE.md.

## Snippets

> "claude-md is infrastructure. It persists. It compounds."
> — [Source: briefs/2026-05-28_k76-claude-skills-claude-md-workflows-from-osint.md]

> Hierarchy: system setup → prompts → output.
> — [Source: @osint-wiki/concepts/claude-code-skills-md-workflow.md]
