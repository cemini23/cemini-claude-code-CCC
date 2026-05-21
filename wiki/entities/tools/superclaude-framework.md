---
title: SuperClaude_Framework — Claude Code configuration/automation framework
type: entity
tags: [tool, claude-code, framework, slash-commands, personas, automation, python, mit, adopt]
keywords: [superclaude, superclaude-framework, claude code configuration, slash commands, cognitive personas, KNOWLEDGE.md, automation framework, claude code extension]
related:
  - entities/tools/claude-code.md
  - concepts/subagent-orchestration.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
---

# SuperClaude_Framework — Claude Code configuration/automation framework

## Relations

- `@entities/tools/claude-code.md` — the harness SuperClaude_Framework configures and extends (slash commands, personas, KNOWLEDGE.md integrations)
- `@concepts/subagent-orchestration.md` — the framework's cognitive personas are a structured-persona pattern adjacent to subagent dispatch; the comparison informs CCC's own persona/agent design
- `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` — cross-wiki tool-eval source

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17 (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). The eval flagged SuperClaude_Framework as a CCC-primary-fit tool: it maps directly onto the CCC wiki's mandate to document, extend, and standardize laptop-side Claude Code tooling.

Repo: `github.com/SuperClaude-Org/SuperClaude_Framework` · License: MIT · Stack: Python · Stars: ~22.8k · Tier: **Adopt** (CCC primary fit).

## Narrative

SuperClaude_Framework is a Claude Code **configuration and automation framework**. Rather than a standalone tool, it is a packaged layer that installs onto an existing Claude Code setup and injects three classes of extension:

1. **Specialized slash commands** — pre-built `/`-commands for common engineering workflows, extending the harness's native command surface.
2. **Cognitive personas** — named role profiles (architect, reviewer, etc.) that reshape how the model approaches a task. A structured-persona system layered on top of the base harness.
3. **`KNOWLEDGE.md` architectural integrations** — a project-knowledge file convention the framework reads, comparable in spirit to `CLAUDE.md` but framework-managed.

At ~22.8k stars it is one of the most-adopted third-party Claude Code extension frameworks.

### Fit for CCC

CCC exists to document, extend, and standardize how Cemini runs Claude Code — slash commands (`entities/commands/`), prompting patterns (`entities/patterns/`), and configuration conventions. SuperClaude_Framework occupies exactly that space: it is a reference implementation of the *extend-and-standardize* mandate, and a source of patterns to compare against Cemini's own `/goal`, Ralph-loop, and OpenSpec approaches.

Two evaluation angles for a CCC follow-up:

- **As an adoption candidate** — install the framework's slash-command + persona layer if it complements (rather than collides with) Cemini's existing command set. Watch for overlap with `entities/commands/` and the `@entities/patterns/full-prompt-goal-template.md` `/goal` template.
- **As a steal-from source** — the cognitive-persona model and the `KNOWLEDGE.md` convention are extractable design patterns even without adopting the whole framework. `KNOWLEDGE.md` is worth comparing against Cemini's `CLAUDE.md` schema discipline.

### Adoption posture

MIT license — no IP-sale or redistribution constraint; the eval cleared it as Adopt. Phase-0 audit pending: clone, verify license via `gh api`, check the most-likely failure mode for the framework class — **does it collide with existing `.claude/` config, slash commands, or `CLAUDE.md` conventions?** A framework that overwrites or shadows Cemini's hand-built command set would be a CONDITIONAL-GO at best. See `@concepts/skill-vetting.md` Phase-0 pattern.

## Snippets

> Tier: Adopt — CCC primary fit. ~22.8k stars. A Claude Code configuration/automation framework — injects specialized slash commands, cognitive personas, and KNOWLEDGE.md architectural integrations. Maps to the CCC-wiki's mandate to document/extend/standardize laptop-side Claude Code tooling. MIT.
[Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
