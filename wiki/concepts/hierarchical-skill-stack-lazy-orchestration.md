---
title: Hierarchical skill stack — lazy discovery and capability fencing
type: concept
tags: [concept, orchestration, hierarchy, lazy-loading, stack, mcp, k164]
keywords: [2607.11138, skill tree, LIFO, lazy manifest, capability fencing, decision vs executable skill, UPI Help]
related:
  - sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md
  - entities/tools/lazy-tool.md
  - concepts/mcp-context-optimization.md
  - concepts/subagent-orchestration.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/recoverable-tool-reliability-hazards.md
  - sources/brief-k164-hierarchical-skill-stack-lazy-orchestration-2026-07-14.md
  - briefs/2026-07-14_ccc-handoff-rsi-hierarchical-orchestration-ingest.md
  - concepts/agent-completion-verification-gates.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md
maturity: draft
created: 2026-07-14
updated: 2026-07-16
---

## Relations

- `@sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md` — K164 provenance
- `@entities/tools/lazy-tool.md` — MCP-level lazy discovery (sibling pattern)
- `@concepts/mcp-context-optimization.md` — four-layer stack; hierarchy is routing-layer steal
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — this page's empirical anchors are single-source (already flagged TENTATIVE below); apply the K169 evaluation checklist before upgrading past "design checklist" ADOPT
- `@concepts/failure-mode-harness-adaptation-mapping.md` — K169 sibling framework; stack-frame + capability-fencing design pairs with the tool-management (T2) adaptation strategy

## Raw Concept

K164 arXiv **2607.11138** — formal hierarchical architecture for agentic orchestration: **capability tree** + **stack-based execution** + **lazy manifest discovery**, motivated by UPI Help (payment-support) production constraints.

## Narrative

### Core distinctions

| Term | Meaning |
|------|---------|
| **Tool** | Isolated API endpoint dumped into a flat registry |
| **Skill** | Node in a hierarchy — either **decision** (orchestrate/delegate) or **executable** (deterministic leaf) |
| **Lazy discovery** | Load only immediate children’s schemas when a node is entered |
| **Stack frame** | Localized memory + return semantics (pushdown / LIFO) |
| **Capability fencing** | Untrusted child output stays in frame — reduces injection persistence into global context |

### When to use hierarchy vs flat [from paper §9.8]

| Prefer hierarchy | Prefer flat |
|------------------|-------------|
| Growing tool catalogs, rich schemas | Bounded N, distinct tools |
| Multi-step workflows + audit/resume | Operational simplicity wins |
| Domains can be **mutually exclusive** | Overlapping domains without redesign |

### Empirical anchors [TENTATIVE — single-source paper]

- Flat routing: context-fail at N=256–512 with 800-char schemas; hierarchy succeeds with ~4 calls and bounded schema tokens/call
- Workflow + noisy history: both ~0.73 success; hierarchy prompts ~10× smaller
- Overlapping top-level domains → wrong-branch errors at depth 1; clean domains eliminate wrong-choice, leave format-validation failures

### Cemini mapping

| Pattern | Steal |
|---------|-------|
| lazy-tool / progressive skills | Already partial — extend to **domain trees** not only MCP search |
| Cursor/Claude multi-MCP | Cap visible tools per turn; route by project domain |
| TipDrop bots | Tree: signals / vendors / compliance / posting — never flat UW+Discord+… dump |
| Poker arena | Opponent/memory/tools as exclusive top domains |
| Prod agents | Stack frames for nested subagent returns + Prebind (K151) at leaf actions |

| Verdict | **REFERENCE** architecture; **ADOPT** tree-design checklist locally — no product install |

## Snippets

> "a 'Tool' is an isolated API endpoint … a 'Skill' is a contextually-bound node within a strict structural hierarchy"
> — [Source: arxiv-2607.11138 intro]

> "Capability fencing and localized execution boundaries also reduce the risk of indirect prompt injection"
> — [Source: arxiv-2607.11138 conclusion]
