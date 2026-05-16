---
title: Fusion — Multi-Node Agent Orchestrator with Worktree Isolation
type: entity
tags: []
keywords: []
related:
  - concepts/subagent-orchestration.md
maturity: draft
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: @osint-wiki/entities/tools/fusion.md
---

# Fusion — Multi-Node Agent Orchestrator with Worktree Isolation

## Relations

- @concepts/subagent-orchestration.md — worktree-isolation + Plan/Review/Execute gate patterns map onto the subagent dispatch model
- @osint-wiki/entities/tools/fusion.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/fusion.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Node.js/Electron agent orchestrator with Worktree Isolation pattern — each task operates in an isolated git worktree preventing file collisions. MIT license, 520 stars. Key patterns: Plan→Review→Execute→Review workflow gates, Smart Merge conflict resolution. Steal-from tier per K45 v3 multi-wiki tool eval — extract Worktree Isolation + gate patterns; do NOT adopt full Electron stack.
