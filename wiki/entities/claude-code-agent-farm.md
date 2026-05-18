---
title: claude_code_agent_farm — Parallel Claude Code Orchestration via tmux
type: entity
tags: []
keywords: []
related:
  - concepts/subagent-orchestration.md
  - entities/tools/roo-code.md
maturity: draft
created: 2026-05-14
updated: 2026-05-17
cross-wiki-source: @osint-wiki/entities/tools/claude-code-agent-farm.md
---

# claude_code_agent_farm — Parallel Claude Code Orchestration via tmux

## Relations

- @concepts/subagent-orchestration.md — parallel-agent orchestration cluster; heartbeat + file-lock patterns are the steal-from value
- @entities/tools/roo-code.md — sibling multi-agent-team tool; Roo-Code is the IDE-plugin form of the same many-agents idea
- @osint-wiki/entities/tools/claude-code-agent-farm.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-code-agent-farm.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Python 3.13+ orchestrator managing up to 50 simultaneous Claude Code agents across tmux panes with lock-based file-write conflict prevention. MIT license, 821 stars. Key patterns: heartbeat tracking, HTML run reports, backup/restore loops. Steal-from tier per K45 v3 multi-wiki tool eval — extract patterns, do NOT adopt tmux orchestrator.
