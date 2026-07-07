---
title: Steerability via constraints — coding-agent oversight substrate (arXiv 2607.02389)
type: source
tags: [source, arxiv, coding-agents, oversight, substrate, steerability, k138]
keywords: [2607.02389, substrate constraints, scalable oversight, docs cli, backdoor detection, gemma reviewer]
related:
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/agent-completion-verification-gates.md
  - concepts/mcp-context-optimization.md
  - entities/tools/openshell.md
  - concepts/skill-vetting.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/skills/super-audit.md
  - sources/brief-k138-substrate-constraints-agent-oversight-2026-07-07.md
  - concepts/subagent-orchestration.md
  - concepts/etclovg-harness-layers.md
  - concepts/code-as-agent-harness.md
  - entities/tools/lazy-tool.md
  - briefs/2026-07-07_ccc-handoff-steerability-substrate-ingest.md
  - "@cybersecurity-wiki/sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md"
  - "@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md"
maturity: draft
read_status: read
created: 2026-07-07
updated: 2026-07-07
phase_0_verdict: "REFERENCE 2026-07-07 — ICML DL4Code workshop; no canonical public repo at Phase-0; steal substrate + docs-CLI + multi-pass review methodology"
---

## Relations

- `@concepts/substrate-constraints-coding-agent-oversight.md` — CCC synthesis (cross-wiki primary in cybersec)
- `@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md` — security eval + backdoor taxonomy depth

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Steerability via constraints: a substrate for scalable oversight of coding agents |
| **Author** | Thomas Winninger (Télécom SudParis; ENS Paris-Saclay) |
| **Venue** | Deep Learning for Code Workshop, ICML 2026, Seoul |
| **arXiv** | 2607.02389 |
| **Code** | Promised with experiment artifacts (`BACKDOORS.md`); **no public repo URL at Phase-0** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.02389-2607-02389v1-steerability-via-constraints-a-subs.pdf` |
| **Retrieved** | 2026-07-07 |
| **Read status** | read (stance, system sketch, 2×2 backdoor experiment, OpenShell peer note) |

## Narrative

Coding agents can generate thousands of LoC; the bottleneck shifts to **verification before execution**. Paper argues pre-LLM engineering controls — access control, network policy, linter-enforced conventions — transfer to agents and are **cheaper in tokens** than heavy MCP/agentic scaffolding.

### Three layers

| Layer | Role |
|-------|------|
| **Substrate** | Linters, types, runtime contracts — refuse invalid code shapes |
| **Projection** | ~200 LoC `docs` CLI (griffe AST) — bounded module/symbol views for reviewers |
| **Machine** | VM isolation, egress allowlist, inference proxy with semantic probes |

### Experiment (2×2)

~500 LoC Python with **11 stratified backdoors** (L1–L5 taxonomy). Small reviewer (Gemma 4 e4b 8B):

| Condition | Backdoor recall |
|-----------|-----------------|
| Unconstrained, no tools | **54.5%** |
| Substrate + docs CLI | **90.9%** |

Substrate and projection tools contribute **independently**. Module-local `Invariants:` docstrings beat centralized `ARCHITECTURE.md` for reviewer signal.

### MCP critique

MCP-mediated retrieval can **saturate reviewer context** with raw payloads — opposite of layered documentation discipline. For **developer-owned local repos**, lightweight AST projection beats dumping MCP tool results into review context. Does not replace prod MCP admission for untrusted third-party servers.

### OpenShell peer

NVIDIA **OpenShell** (Apache-2.0) is the mature machine-layer peer; paper's forward path is OpenShell + content-inspection probes (out-of-tree or upstream).

**CCC relevance:** pairs with `@concepts/agent-completion-verification-gates.md` (objective done proof) and `@entities/skills/super-audit.md` (multi-pass small-model review). **REFERENCE** — steal patterns; no installable paper artifact at Phase-0.

## Snippets

> "Recall rises from 54.5% (unconstrained, no tools) to 90.9% (constrained substrate plus a ~200-LoC docs CLI), with substrate and tools contributing independently."
> — [Source: arxiv-2607.02389-steerability-via-constraints-coding-agent-oversight.pdf abstract, retrieved 2026-07-07]

> "We instantiate the projection principle in docs, a ~200-LoC CLI built on griffe. Three commands suffice: docs module X … docs symbol X.Y … docs examples X (planned)."
> — [Source: arxiv-2607.02389 §4, retrieved 2026-07-07]

> "The closest mature peer, NVIDIA OpenShell, has a broader and better-tested feature set in every dimension except content-level message inspection."
> — [Source: arxiv-2607.02389 §6, retrieved 2026-07-07]
