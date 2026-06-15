---
title: Agents All the Way Down — custom agent methodology (arXiv 2606.11869)
type: source
tags: [source, arxiv, custom-agents, methodology, mcp, k115]
keywords: [2606.11869, agents-all-the-way-down, turtle-pattern, agent-tests-agent]
related:
  - concepts/agents-all-the-way-down-custom-methodology.md
  - concepts/code-as-agent-harness.md
  - entities/tools/claude-code.md
  - concepts/skill-vetting.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- `@concepts/agents-all-the-way-down-custom-methodology.md` — CCC synthesis
- `@concepts/code-as-agent-harness.md` — harness substrate framing
- `@entities/tools/claude-code.md` — general-purpose tier for P3 prototype
- `@concepts/skill-vetting.md` — security boundaries in custom agents

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agents All the Way Down: A Methodology for Building Custom AI Agents from Substrate to Production |
| **Authors** | Alier Forment et al. (UPC, UPV/EHU, USAL) |
| **arXiv** | 2606.11869 |
| **Location** | `raw-sources/arxiv-2606.11869-agents-all-the-way-down.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (P1–P5 methodology, custom vs general-purpose axes) |

## Narrative

Methodology for **custom agents** (fit to one job inside one application) vs general-purpose tier (Claude Code, Cursor). **Five phases** with asymmetry: two preconditions crossed once, three practices repeated:

| Phase | Name | Content |
|-------|------|---------|
| P1 | **Substrate** | LLM as software component: tools → system → messages; cache discipline |
| P2 | **Building blocks** | Function calling, MCP, CLI, liteshell, agent loop, skills, characters, hooks |
| P3 | **Prototype with GP agent** | Claude Code/OpenCode/Cursor as pair-programmer on real platform |
| P4 | **Harvest → CLI (Turtle)** | Fold tools/skills/scaffolding into small agent loop; ship as CLI |
| P5 | **Agent-tests-agent** | GP agent drives custom agent through behavioral scenarios |

**Six custom-agent axes:** embedded domain knowledge, private tools/APIs, in-app deployment, security allow-lists, right-sized model routing, brand/audit/compliance.

Worked example: Agent-Assisted Creator (AAC) in educational platform.

**CCC relevance:** maps cleanly to Cemini workflow (P3 = Claude Code/Cursor, P4 = briefs → `settings.json`/skills, P5 = ship-subagent + honesty critic). **REFERENCE** — no framework install; methodology paper only.

## Snippets

> "The custom agent is the cabinet maker's jig: built for one specific job … fitted to one piece of work."

> "P5 — Agent-tests-agent: use a general-purpose CLI agent to drive the custom agent through scenarios."
