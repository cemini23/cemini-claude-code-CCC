---
title: agent-toolkit — private /route script host
type: entity
tags: [tool, route, federation, k228-followon]
keywords: [agent-toolkit, route-task, ROUTE_KIT, SIP]
related:
  - entities/skills/route.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: validated
created: 2026-08-08
updated: 2026-08-08
---

## Relations

- @entities/skills/route.md
- @concepts/llm-routing-deepseek-openrouter-failover.md

## Raw Concept

Private canon host for Cemini `/route` after TipDrop kit retirement (2026-08-08).

## Narrative

- **Repo:** https://github.com/cemini23/agent-toolkit (private)
- **Laptop:** `~/Projects/agent-toolkit`
- **Prod:** `/opt/cemini/agent-toolkit` (`ROUTE_KIT`)
- **Egress:** `/opt/cemini/agent-toolkit` (rsync; no pwsh — bash shims only)
- **Not** public `agent-toolkit-demo` (vet/phase0/wikilint CI)

Scripts: `route-task`, `handoff-to-grok`, `claude-ds`, SIP/verify/escalate libs. Adopt: `pwsh -File scripts/adopt-route-always-approve.ps1`. TipDrop kit keeps redirect stubs only.
