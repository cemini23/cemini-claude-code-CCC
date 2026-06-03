---
title: Runtime harness interface adaptation (LIFE-HARNESS)
type: concept
tags: [concept, agent-harness, k95]
keywords: [life-harness, 2605.22166, interface-adaptation, frozen-llm, deterministic-agents]
related:
  - sources/arxiv-runtime-harness-adaptation-2605.22166.md
  - concepts/code-as-agent-harness.md
  - concepts/system-scaling-harness-agentic-ai.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - entities/tools/life-harness.md
  - entities/tools/claude-code.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@sources/arxiv-runtime-harness-adaptation-2605.22166.md` — primary paper
- `@concepts/code-as-agent-harness.md` — harness-interface layer focus
- `@entities/tools/claude-code.md` — host harness being adapted

## Raw Concept

K95 arXiv **2605.22166** — improve agents by evolving the **runtime interface** (contracts, skills, action realization, trajectory control) without updating model weights. Complements model-centric fine-tuning/RL.

## Narrative

### Four intervention classes (paper)

| Class | CCC analogue |
|-------|----------------|
| Environment contracts | MCP tool schemas, `.claude/settings.json` permissions |
| Procedural skills | `SKILL.md` files, slash commands |
| Action realization | Bash/Edit tool wrappers, hook validators |
| Trajectory regulation | Stop hooks, `/goal`, subagent dispatch limits |

### Cemini mapping [TENTATIVE]

| Paper claim | CCC practice |
|-------------|--------------|
| Frozen LLM + evolved harness | Skills/hooks evolve in git; model tier fixed per session |
| Cross-model harness transfer | Project-level `.claude/` + wiki rules portable across Opus/Sonnet |
| Deterministic domains | Lint gates, `skill_audit.py`, OpenSpec acceptance criteria |

| Verdict | **STEAL-FROM** — formalizes "adapt interface not model" already implicit in CCC skill/hook iteration |

## Snippets

> "Runtime interface adaptation as a complementary alternative to model-centric agent training."
> — [Source: arxiv-2605.22166-adapting-the-interface-not-the-model-runtime-har.pdf p.1]
