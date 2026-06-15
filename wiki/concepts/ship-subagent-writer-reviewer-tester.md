---
title: /ship subagent pattern — writer, reviewer, tester (K108)
type: concept
tags: [concept, subagents, claude-code, k108]
keywords: [ship, 0x-rody, writer, reviewer, tester, parallel-subagents]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/scatter-gather.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/skillhone-continual-skill-decision-history.md
  - sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md
  - concepts/perspectivegap-orchestration-prompting.md
  - sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md
  - concepts/agents-all-the-way-down-custom-methodology.md
  - concepts/claude-honesty-critic-agent.md
  - sources/arxiv-parthenon-law-self-evolving-legal-agent-2606.04602.md
  - sources/brief-k112-ccc-claude-honesty-critic-2026-06-12.md
maturity: draft
created: 2026-06-09
updated: 2026-06-15
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — parent orchestration
- `@entities/patterns/scatter-gather.md` — parallel writer + tester fan-out
- `@concepts/agent-rubrics-self-correction.md` — reviewer gate
- `@concepts/agent-completion-verification-gates.md` — human approve before commit
- `@sources/trading-posts-compilation-8-2026-06-09.md` — K108 Post 4 (@0x_rody)
- `@concepts/perspectivegap-orchestration-prompting.md` — need-only boundary failures on generated role prompts

## Raw Concept

K108 Post 4 (@0x_rody): **`/ship`** — four files: `writer.md`, `reviewer.md`, `tester.md`, `commands/ship.md`. Orchestrator writes brief → parallel writer + tester → reviewer on diff → summary → **human approve before commit**.

## Narrative

| Stage | Agent | Role |
|-------|-------|------|
| Brief | Orchestrator | Scoped task envelope |
| Parallel | Writer + Tester | Implementation + test harness |
| Gate | Reviewer | Diff review against brief |
| Human | Operator | Approve before commit |

**Sweet spot:** multi-file medium tasks. **Skip:** one-liners (overhead > value).

CCC mapping: Task tool scatter-gather + `@concepts/agent-completion-verification-gates.md` + git commit only on explicit operator ask (user rule).

**K111 SkillHone parallel:** eval subagents return **redacted evidence** to optimization subagents — same permission boundary as tester vs writer; see `@concepts/skillhone-continual-skill-decision-history.md`.

**Verdict:** **REFERENCE** — steal file layout for `.claude/agents/` + slash command; no install.

## Snippets

> Writer/reviewer/tester parallel `/ship` — human approve before commit. [TENTATIVE — @0x_rody, Posts.docx K108 Post 4]
