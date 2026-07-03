---
title: Tool-Guard isolated planning — prod-mcp handoff
type: brief
tags: [brief, mcp, tool-poisoning, prod-mcp, lazy-tool]
created: 2026-06-24
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

hands-on | prod-mcp / lazy-tool | Claude Desktop agent harness

## Summary

arXiv:2606.20922 / Tool-Guard: **cross-tool description poisoning** persists poisoned metadata in planner context. Influenced-list quarantine cuts AgentDojo ASR **43%→2%** (GPT-4o) without deleting tools from allowlist.

## Body

### Threat test (add to MCP red-team)

1. Poison tool **A** description in allowlisted server
2. Craft task requiring tool **B** only
3. Measure whether poison steers **B** selection/args — poisoned tool never invoked
4. Compare ASR vs standard tool-output IPI suite

### Harness pattern

| Step | Action |
|------|--------|
| Pre-plan | Run alignment + suspiciousness on all manifest descriptions |
| On flag | Move tool to **influenced list** — strip from planning context |
| Execute | Tool still callable if planner explicitly needs it |
| Post-step | Re-evaluate influenced list after each invocation |

### Integration notes

- **Before** blanket tool filtering (destroys utility on AgentDojo)
- **After** DefenseClaw DCI scan — DCI catches dishonest authorized tools; Tool-Guard catches cross-tool metadata steering
- Budget ~1.4× tokens, ~3.7× latency on AgentDojo — profile on lazy-tool catalog size

### Phase-0

`github.com/shishishi123/Tool-Guard` — **CONDITIONAL-GO** (MIT, 0★, ICML artifact)

## Sources

- @sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
- @concepts/cross-tool-description-poisoning.md
- @entities/tools/tool-guard.md
