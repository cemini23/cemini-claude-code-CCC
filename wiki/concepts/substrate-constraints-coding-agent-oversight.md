---
title: Substrate constraints for scalable coding-agent oversight
type: concept
tags: [concept, harness, coding-agents, verification, cross-wiki, k138]
keywords: [substrate constraints, docs cli, scalable oversight, 2607.02389, invariant locality]
related:
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - sources/brief-k138-substrate-constraints-agent-oversight-2026-07-07.md
  - entities/tools/openshell.md
  - concepts/agent-completion-verification-gates.md
  - concepts/skill-vetting.md
  - concepts/subagent-orchestration.md
  - concepts/mcp-context-optimization.md
  - concepts/etclovg-harness-layers.md
  - concepts/code-as-agent-harness.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/skills/super-audit.md
  - entities/tools/lazy-tool.md
  - briefs/2026-07-07_ccc-handoff-steerability-substrate-ingest.md
  - "@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md"
  - "@cybersecurity-wiki/sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md"
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/trustx-agent-risk-classification.md
  - concepts/standing-policy-instruction-following-benchmark.md
  - sources/arxiv-handbook-md-long-context-agentic-policy-2607.25398.md
maturity: draft
created: 2026-07-07
updated: 2026-07-30
cross-wiki-primary: "@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md"
---

## Relations

- `@sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md` — CCC ingest provenance (K138)
- `@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md` — primary synthesis + L1–L5 backdoor taxonomy
- `@briefs/2026-07-07_ccc-handoff-steerability-substrate-ingest.md` — harness handoff
- `@concepts/agent-completion-verification-gates.md` — objective done gates complement substrate shape

## Raw Concept

K138 ingest 2026-07-07: arXiv **2607.02389** — coding-agent oversight scales when **code refuses invalid shapes** and reviewers get **bounded AST projections**, not full MCP dumps or prompt-only rules.

## Narrative

### Three layers

```
Advisory     → prompts, skills, planner instructions (may drift)
Substrate    → linters, types, runtime contracts (refuse violations)
Projection   → docs CLI / AST views (bounded context for reviewers)
Machine      → VM, egress allowlist, inference proxy (OpenShell peer)
```

### Substrate conventions (Python) [TENTATIVE]

| Control | Purpose |
|---------|---------|
| ruff security + bugbear + bandit | Block bare-except, obvious injection patterns |
| pyrefly + jaxtyping | Narrow types visible in headers |
| beartype + pydantic strict | Runtime contract enforcement |
| Frozen/slotted/kw-only dataclasses | Prevent smuggling via mutable extras |
| `tuple` / `Mapping` over `list` / `dict` | Reduce silent mutation |
| **Invariants in module docstrings** | Locality beats centralized ARCHITECTURE.md |
| `core/` purity split | Per-function review bundles stay ≤4K tokens |

### Projection CLI pattern

~200 LoC AST tool (griffe): `docs module`, `docs symbol`, `docs examples` (planned). For **developer-owned local repos**, beats MCP context dumps that saturate reviewer context (`@concepts/mcp-context-optimization.md`). Does **not** replace prod MCP admission for untrusted servers.

### Multi-pass per-function review

8B reviewer fixates on first finding in single-pass. Minimum scaffolding:

1. Self-consistency (name ↔ body ↔ docstring)
2. I/O contract (type width vs misuse)
3. Invariant check (module docstring vs body)

Pair with `@entities/skills/super-audit.md` for prod ship and small-model review subagents in `@concepts/subagent-orchestration.md`.

### CCC mapping

| Paper layer | Cemini surface |
|-------------|----------------|
| Substrate | `wiki_lint.py`, ruff/pyright on CI, OpenSpec AC |
| Projection | Future `docs symbol` CLI; today: targeted `Read` + module docstrings |
| Verification | `@concepts/agent-completion-verification-gates.md`, super-audit |
| Machine | `@entities/tools/cua.md`; `@entities/tools/openshell.md` on server-class paths |
| Governance | `@concepts/skill-vetting.md` Phase-0 before harness surface changes |

### Eval template

Benchmark oversight with 2×2 **substrate × projection tools** — not only strong-writer / weak-reviewer capability gaps. Cross-link SeClaw trajectory eval (`@concepts/seclaw-agent-security-evaluation.md`) for unsafe intermediate steps.

**David adoption:** `@cybersecurity-wiki/briefs/2026-07-07_harness-substrate-constraints-checklist.md`

| Verdict | **REFERENCE** — adopt substrate + projection patterns in rules/skills |

## Snippets

> "Recall rises from 54.5% to 90.9% with constrained substrate plus docs CLI."
> — [Source: arxiv-2607.02389-steerability-via-constraints-coding-agent-oversight.pdf abstract, retrieved 2026-07-07]

> "Substrate constraints, in contrast, are not advisory: linters, type checkers, runtime contract validators … refuse to run code that violates them."
> — [Source: arxiv-2607.02389 §3.1, retrieved 2026-07-07]
