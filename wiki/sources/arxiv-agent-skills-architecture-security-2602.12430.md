---
title: Agent Skills for LLMs — architecture, acquisition, security (arXiv 2602.12430)
type: source
tags: [source, arxiv, agent-skills, skill-md, mcp, security]
keywords: [2602.12430, progressive-disclosure, skill-trust, agentskills]
related:
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/agent-skills-taxonomy.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/tools/scienceaix-agentskills.md
  - concepts/mcp-context-optimization.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/thin-harness-fat-skills-garrytan.md
maturity: draft
read_status: read
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- `@concepts/agent-skills-progressive-disclosure.md` — CCC synthesis (3-level loading, skills vs MCP)
- `@concepts/agent-skills-taxonomy.md` — prior survey 2605.07358; complementary scope
- `@concepts/skill-vetting.md` — 26.1% vulnerability stat + four-tier trust framework
- `@entities/mcp-servers/anthropic-skills.md` — Anthropic open standard (Dec 2025)
- `@entities/tools/scienceaix-agentskills.md` — companion resource catalog repo

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward |
| **Authors** | Renjun Xu, Yang Yan (ReDiscovery / Westlake University) |
| **arXiv** | 2602.12430 |
| **DOI** | 10.48550/arXiv.2602.12430 |
| **Code** | https://github.com/scienceaix/agentskills |
| **Location** | `raw-sources/arxiv-2602.12430-agent-skills-for-large-language-models-architect.pdf` |
| **Retrieved** | 2026-06-04 |
| **Read status** | read (abstract + architecture/security sections) |

## Narrative

AgentSkills '26 workshop survey (Feb 2026). First focused treatment of the **skill abstraction layer** — distinct from broad LLM-agent or tool-use surveys (2605.07358). Four axes: architecture (SKILL.md + progressive disclosure + MCP complement), acquisition (SAGE, SEAgent, compositional synthesis), deployment (CUAs + SWE benchmarks), security (26.1% community skill vulnerabilities → **Skill Trust and Lifecycle Governance Framework**).

**CCC relevance:** validates Cemini's thin-harness + fat-skills + Phase-0 `skill-vetting.md` posture. Skills supply "what to do"; MCP supplies "how to connect."

## Snippets

> "26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework—a four-tier, gate-based permission model."

> "Skills supply the 'what to do' and MCP supplies the 'how to connect.'"

> — [Source: arxiv-2602.12430-agent-skills-for-large-language-models-architect.pdf p.1–2, retrieved 2026-06-04]
