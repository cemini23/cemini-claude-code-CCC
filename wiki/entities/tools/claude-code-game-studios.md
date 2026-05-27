---
title: Claude-Code-Game-Studios — multi-agent role graphs (MIT, steal-from)
type: entity
tags: [tool, claude-code, multi-agent, steal-from, cross-wiki-route]
keywords: [claude-code-game-studios, donchitos, role-graph, multi-agent, game-dev]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/citadel-agent-orchestration.md
  - entities/tools/the-architect.md
  - entities/tools/superclaude-framework.md
  - entities/tools/cc-wf-studio.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/claude-code-software-factory.md
  - entities/tools/three-man-team.md
maturity: draft
created: 2026-05-24
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — **dedup here** — role-specialized agents map to Explore/Plan/general-purpose dispatch
- `@entities/patterns/scatter-gather.md` — parallel role fan-out topology
- `@entities/patterns/citadel-agent-orchestration.md` — apex orchestration comparison
- `@entities/tools/the-architect.md` — blueprint generator vs game-studio role graphs
- `@entities/tools/superclaude-framework.md` — cognitive personas overlap
- `@entities/tools/cc-wf-studio.md` — visual workflow editor overlap

Cross-wiki: `@osint-wiki/entities/tools/claude-code-game-studios.md`; K63 URL #8.

## Raw Concept

`Donchitos/Claude-Code-Game-Studios` — multi-agent **role graph** for Claude Code (game-dev framing). MIT [CONFIRMED 2026-05-24, ~20k★]. K63 **Steal-from** — extract orchestration diagrams only; do not adopt game-specific assets wholesale.

## Narrative

### Steal-from targets

- Named roles + handoff edges between agents
- Separation of planner vs implementer vs reviewer in a graph (compare Glasswing adversarial gating)

### Dedup vs existing CCC pages

| Existing | Overlap |
|----------|---------|
| `@concepts/subagent-orchestration.md` | When to dispatch subagents |
| `@entities/patterns/citadel-agent-orchestration.md` | Campaign persistence + tiers |
| `@entities/tools/superclaude-framework.md` | Persona packs |

**No new orchestration primitive** — this repo is a **reference layout** for multi-agent graphs, not a dependency.

### Adoption posture

| Verdict | **STEAL-FROM** — patterns only |

## Snippets

> "Steal-from: Claude-Code-Game-Studios multi-agent role graphs — dedup vs existing orchestration pages."
> — [Source: briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md]
