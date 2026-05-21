---
title: Roo-Code — autonomous AI agent team embedded in the code editor
type: entity
tags: [tool, ide-integration, agent-team, autonomous-agents, vscode, typescript, apache-2.0, archived, adopt-as-blueprint]
keywords: [roo-code, roocodeinc, ide plugin, vscode extension, autonomous agents, agent team, code editor integration, archived repo, fork-and-maintain]
related:
  - concepts/subagent-orchestration.md
  - entities/claude-code-agent-farm.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
---

# Roo-Code — autonomous AI agent team embedded in the code editor

## Relations

- `@concepts/subagent-orchestration.md` — Roo-Code's in-editor agent team is a gold-standard exemplar of multi-agent orchestration; the IDE-integration angle complements CCC's `Agent`-tool delegation model
- `@entities/claude-code-agent-farm.md` — sibling parallel-agent orchestrator (tmux-pane); Roo-Code is the IDE-plugin form of the same multi-agent-team idea
- `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` — cross-wiki tool-eval source

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17 (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). The eval flagged Roo-Code as a CCC-primary-fit tool: a gold-standard exemplar for IDE-plugin integration workflows.

Repo: `github.com/RooCodeInc/Roo-Code` · License: Apache-2.0 · Stack: TypeScript · Stars: ~24.1k · Tier: **Adopt** (CCC primary fit) — see archived-repo caveat below.

## Narrative

Roo-Code embeds a **team of autonomous AI agents directly into the code editor**. Rather than a single chat assistant, it stands up multiple specialized agents that operate inside the IDE — a multi-agent orchestration model expressed as an editor plugin rather than a CLI harness. At ~24.1k stars it was one of the most-adopted IDE-integration agent tools, and the eval names it a **gold-standard exemplar for IDE-plugin integration workflows**.

For CCC this matters as a *reference architecture*: Cemini runs Claude Code as a CLI harness with `Agent`-tool subagents (`@concepts/subagent-orchestration.md`), and also uses the Claude Code IDE extension. Roo-Code shows how an autonomous agent *team* can be surfaced inside the editor itself — a design worth studying when CCC documents IDE-side workflow patterns.

### Caveat — the repo is archived

**IMPORTANT: the `RooCodeInc/Roo-Code` repository has been archived by its owner.** An archived repo is read-only and receives no further commits, releases, security patches, or maintainer support. Roo-Code is therefore **adoptable only as a fork-and-maintain blueprint, not as a live dependency**:

- Do **not** install it as an ongoing tool or wire it into the workflow expecting updates — it is frozen.
- Treat it as a **steal-from / clone-and-study** exemplar: read the architecture, extract the IDE-integration and agent-team patterns, and if any of it is used directly, **fork it** and own the maintenance.
- The **Apache-2.0 license permits the fork** — Apache-2.0 is a permissive license allowing redistribution and modification of a fork, including for a commercial or IP-sale context, provided the license and notices are preserved. This is the one license condition cleared by the eval; a Phase-0 pass should re-verify it via `gh api repos/RooCodeInc/Roo-Code --jq '.license.spdx_id'` and confirm the `archived: true` flag.

The eval's "Adopt" tier here means *adopt the patterns / adopt as a fork blueprint* — it does not mean treat the upstream repo as a maintained dependency.

## Dead Ends

- **Adding archived `RooCodeInc/Roo-Code` as a live dependency** — the repo is frozen; no patches will ever land. Any use must be a maintained fork. Recorded here so a future session doesn't re-evaluate it as a live tool.

## Snippets

> Tier: Adopt — CCC primary fit. ~24.1k stars; embeds a team of autonomous AI agents into the code editor — a gold-standard exemplar for IDE-plugin integration workflows. The repo has been archived by its owner — adoptable only as a fork-and-maintain blueprint, not a live dependency. Apache-2.0 permits the fork.
[Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
