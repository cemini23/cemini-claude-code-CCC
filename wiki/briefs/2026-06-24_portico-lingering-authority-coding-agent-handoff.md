---
title: PORTICO lingering authority — coding agent handoff
type: brief
tags: [brief, coding-agents, least-privilege, capabilities, claude-code]
created: 2026-06-24
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

hands-on | Claude Code / Cursor agent loops | prod-mcp coding tasks

## Summary

arXiv:2606.22504: **lingering authority** — planner still sees tools after subgoal closes. PORTICO revokes epoch-bound handles from next interface; **10/10** post-closure replays blocked vs 0/10 for non-revoking comparator.

## Body

### Task-contract template

```
User goal → compile:
  - initial_capabilities (minimal)
  - grant_rules (on-demand boundary expansions)
  - closure_predicates (subgoal complete)
  - global_deny_rules
```

### Lifecycle per subgoal

1. Planner **requests** boundary grant (cannot invent new authority)
2. Monitor **mints** opaque epoch handle
3. Invoke through handle
4. On closure: **remove handle from next planner manifest** (not just ACL deny)
5. Reject stale handle replay before side effects

### Relation to existing controls

| Control | Addresses |
|---------|-----------|
| TOOLPRIVBENCH / OPUR | Which authorized tool picked |
| AIRGuard | Execution-time narrowing |
| **PORTICO** | Temporal visibility in planner interface |
| SPI | Cross-session memory poison |

### Phase-0

No public PORTICO repo — **Reference** pattern steal only

## Sources

- @sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md
- @concepts/lingering-authority-revocable-capabilities.md
