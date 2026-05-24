---
title: "cc-wf-studio — visual workflow editor for Claude Code agent pipelines"
type: entity
tags: [tool, vs-code-extension, workflow-editor, subagent-pipelines, conditional-branching, cross-wiki-route]
keywords: [cc-wf-studio, breaking-brake, workflow-editor, visual-orchestration, agent-pipelines, conditional-branching, vs-code]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/scatter-gather.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - entities/tools/claude-code-game-studios.md
maturity: draft
created: 2026-05-21
updated: 2026-05-24
cross-wiki-source: "@osint-wiki/sources/multi-wiki-link-eval-41url-2026-05-18.md"
---

## Relations

- @concepts/subagent-orchestration.md — cc-wf-studio visualises the dispatch decisions this concept page codifies
- @entities/tools/conductor-mcp.md — the conductor's routing logic; cc-wf-studio could visualise conductor fan-out topologies
- @entities/patterns/scatter-gather.md — conditional branching in a visual editor is scatter-gather with explicit branch logic
- @osint-wiki/sources/multi-wiki-link-eval-41url-2026-05-18.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from the OSINT K53 41-URL tool eval (May 2026). `breaking-brake/cc-wf-studio` (~5,000★, v3.34.1) is a VS Code extension providing a visual workflow editor for Claude Code, Copilot, and sub-agent orchestration pipelines — conditional branching, config export to native agent runtimes.

## Narrative

### What it does

A VS Code extension that lets you design Claude Code agent pipelines visually:
- Drag-and-drop agent nodes with conditional branching
- Export pipeline configs to native agent runtimes (Claude Code, Copilot, etc.)
- Visual representation of sub-agent dependency chains

### License caveat

GitHub API reports NOASSERTION. The eval source claims v3.0.0 mutated from MIT → AGPL-3.0-or-later. The K53 brief's policy note applies: CCC-wiki may accept AGPL only for laptop-side / IDE-extension tools never shipped to production or compiled into `/opt/cemini`. Verify the license directly before any adoption.

### CCC relevance

Visual workflow editing is not Cemini's primary interaction model (terminal-first), but cc-wf-studio's conditional-branching export format is interesting as a declarative subagent-pipeline specification language — a potential interchange format between conductor and scatter-gather.

[NEEDS VERIFICATION 2026-05-21] license. GitHub API reports NOASSERTION; eval claims AGPL-3.0-or-later from v3.0.0. Verify before any installation.
