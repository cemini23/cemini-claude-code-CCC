---
title: user-as-code — Pine AI executable user memory
type: entity
tags: [tool, memory, pine-ai, user-as-code, k120]
keywords: [19PINE-AI, user-as-code, apache-2.0, executable-memory]
related:
  - sources/arxiv-user-as-code-executable-memory-2606.16707.md
  - concepts/executable-user-memory-user-as-code.md
  - concepts/skill-vetting.md
  - entities/tools/claude-mem.md
maturity: draft
created: 2026-06-20
updated: 2026-07-31
wire_status: wont_wire
wire_target: "NO-GO CCC — overlaps claude-mem + wiki"
---

## Relations

- `@sources/arxiv-user-as-code-executable-memory-2606.16707.md` — arXiv 2606.16707
- `@concepts/executable-user-memory-user-as-code.md` — paradigm synthesis
- `@concepts/skill-vetting.md` — Phase-0 before install
- `@entities/tools/claude-mem.md` — CCC adopted memory layer (orthogonal)

## Raw Concept

`github.com/19PINE-AI/user-as-code` — reference implementation for User as Code executable memory paper.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `19PINE-AI/user-as-code` |
| **License** | Apache-2.0 (API verified 2026-06-20) |
| **Stars** | ~3 (2026-06-20) |
| **Maintainer** | Pine AI (Bojie Li) |
| **Website** | https://01.me/research/user-as-code |

**What it ships:** experiments + pipeline code turning conversations into typed Python user state with executable constraint rules.

### Phase-0 verdict

| Question | Answer |
|----------|--------|
| Adopt for CCC wiki harness? | **NO-GO** — overlaps claude-mem + git wiki; personal-agent niche |
| CONDITIONAL-GO | Laptop experiments for **personalized operator agents** (Hermes-style) with Phase-0 + isolated venv |
| Steal-from | WAL + checkpoint memory pipeline; proactive rule pattern for skills |

## Snippets

> "Executable memory for personalized agents: typed Python state + constraints an interpreter can run."

> — [Source: github.com/19PINE-AI/user-as-code README]
