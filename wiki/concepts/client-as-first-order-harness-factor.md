---
title: Client is a first-order harness factor — same model, 2.1× capability gap
type: concept
tags: [concept, harness, evaluation, mcp, tool-orchestration, cross-wiki, k140]
keywords: [driving client, harness first-order, client naming, 2.1x gap, hexstrike, 2607.02873, harness is everything]
related:
  - concepts/harness-layer-competition-cursor-claude-perplexity.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-context-optimization.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - briefs/2026-07-07_ccc-handoff-hexstrike-client-orchestration-ingest.md
  - "@cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md"
  - "@cybersecurity-wiki/sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md"
  - meta/ccc-cross-wiki-handoff-briefs.md
  - sources/brief-k140-hexstrike-client-orchestration-2026-07-07.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - concepts/multilingual-long-horizon-agent-eval.md
  - sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/mcp-multi-agent-graceful-degradation-stack.md
  - sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md
  - sources/arxiv-jw-astclaw-solar-telescope-multi-agent-mcp-2607.13549.md
  - concepts/acp-mcp-three-layer-human-agent-execution.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - sources/arxiv-agent-client-protocol-hri-genai-2607.14919.md
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
  - concepts/theory-of-mind-personalized-agent-explanations.md
  - entities/tools/tars-vscode.md
  - sources/arxiv-tars-theory-of-mind-ide-2607.15948.md
maturity: draft
created: 2026-07-07
updated: 2026-07-20
cross-wiki-primary: "@cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md"
---

## Relations

- `@concepts/harness-layer-competition-cursor-claude-perplexity.md` — "the harness is everything" thesis, now empirically supported
- `@concepts/code-as-agent-harness.md` — harness as first-class capability layer
- `@cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md` — primary synthesis (HexStrike study)
- `@briefs/2026-07-07_ccc-handoff-hexstrike-client-orchestration-ingest.md` — CCC handoff

## Raw Concept

K140 routing from cybersec ingest 2026-07-07: arXiv **2607.02873** (HexStrike-AI, 774 picoCTF trials) empirically shows the **driving client/harness is a first-order capability factor** — a **2.1× solve-rate gap** between two clients running the *same* model.

## Narrative

The K92 "harness is everything" claim (`@concepts/harness-layer-competition-cursor-claude-perplexity.md`) was `[TENTATIVE]`. This paper upgrades the evidence: holding the model fixed, **RooCode 76.4% vs 5ire 49.6%** post-fix — the harness moved capability 2.1×.

### CCC operating consequences

1. **Name the harness** — any internal model comparison (super-audit slots, subagent model picks) must record `(model, client/harness, tool-regime)`. A model verdict without the harness named is under-specified.
2. **Fix the harness before the model** — the study's 55.4%→72.0% lift came from **tool-description + agent-behavior** fixes, not a model swap. Mirrors CCC harness-first discipline and substrate-constraints (`@concepts/substrate-constraints-coding-agent-oversight.md`).
3. **Fewer, sharper tools** — residual failures were reasoning-bound, not missing-tool; corroborates lazy-tool / least-privilege exposure (`@concepts/mcp-context-optimization.md`).

### Limits

Single benchmark; fixes tuned on eval set; client effect shown for one model — magnitude `[TENTATIVE]`, direction robust.

| Verdict | **REFERENCE** — harness-first evidence; adopt client-naming in eval discipline |

## Snippets

> "A benchmark that varies the model while fixing an unnamed harness may be measuring the harness as much as the model."
> — [Source: @cybersecurity-wiki/sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md, retrieved 2026-07-07]
