---
title: "Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents"
type: source
tags: [source, arxiv, least-privilege, mcp, terminal, security, k290]
keywords: [2608.18351, least privilege, excess-authority, MCP, brokered environment, Dr GRPO]
related:
  - concepts/task-conditioned-least-privilege-agent-learning.md
  - entities/patterns/task-conditioned-least-privilege-envelope.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@concepts/task-conditioned-least-privilege-agent-learning.md`
- `@entities/patterns/task-conditioned-least-privilege-envelope.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents |
| **arXiv** | 2608.18351 |
| **Authors** | Alexander Tu, Michael Tu (Purdue Northwest) |
| **Code** | none public |
| **Retrieved** | 2026-08-20 |

## Narrative

Post-training framework teaching a 4B model (Qwen3.5-4B + LoRA + Dr. GRPO) **task-conditioned least privilege** in brokered terminal and MCP environments. Each action is audited pre- and post-execution along six risk dimensions with deterministic verifiers (completion, evidence, exact state, prohibited attempts, safe success). Task-specific **sufficient-authority envelopes** define excess-privilege penalties.

Results: 98.48% safe success vs 64.36% base on 2,896 held-out episodes; excess-authority events 4.56% → 0.79%. Complements — does not replace — permission gates and sandboxing (pairs K285 Mandato, K239).

| Verdict | **ADOPT** learned restraint layer + brokered audit + task-relative authority envelopes. **Policy only** (no public code). Pairs K285/K271/K239. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.18351-task-conditioned-least-privilege-learning-for-ex.pdf` |
