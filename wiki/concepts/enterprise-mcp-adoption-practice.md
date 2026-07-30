---
title: Enterprise MCP adoption — practitioner interview synthesis
type: concept
tags: [concept, mcp, enterprise, adoption, k110]
keywords: [2606.09182, ecosystem-fragmentation, fault-diagnosis, low-code-mcp]
related:
  - sources/arxiv-enterprise-mcp-adoption-2606.09182.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - concepts/mcp-context-optimization.md
  - concepts/skill-vetting.md
  - concepts/openagenet-trusted-agent-discovery.md
  - concepts/queen-bee-beespec-enterprise-orchestration.md
  - concepts/seclaw-agent-security-evaluation.md
  - "@cybersecurity-wiki/concepts/mcp-security-posture.md"
  - "@cybersecurity-wiki/concepts/enterprise-mcp-adoption-interviews.md"
  - concepts/mcp-app-hitl-approval-gap.md
  - sources/arxiv-empirical-mcp-applications-hitl-2607.25635.md
maturity: draft
created: 2026-06-11
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-enterprise-mcp-adoption-2606.09182.md` — n=20 interviews, Internet + financial sectors
- `@concepts/mcp-server-catalog-curation.md` — fragmentation → Phase-0 catalog discipline
- `@concepts/mcp-server-runtime-fault-taxonomy.md` — fault diagnosis gap in operations
- `@concepts/seclaw-agent-security-evaluation.md` — security vs function-calling perception
- `@cybersecurity-wiki/concepts/mcp-security-posture.md` — security posture cross-wiki

## Raw Concept

arXiv **2606.09182** — first empirical study of **how enterprises adopt MCP** for LLM-driven software engineering (not benchmarks alone).

## Narrative

### What practitioners value

- Cross-system tool collaboration without bespoke adapters per pair  
- Task decoupling (host/client/server boundaries)  
- Knowledge reuse across workflows  

### What blocks adoption

| Bottleneck | CCC analogue |
|------------|----------------|
| Ecosystem fragmentation | `@concepts/mcp-server-catalog-curation.md`, lazy-tool deferral |
| Cross-component coordination | conductor, Queen-Bee BeeSpec scope compilation |
| Distributed state management | stash, claude-mem, context engineering |
| Fault diagnosis | `@concepts/mcp-server-runtime-fault-taxonomy.md`, `wiki/log.md` ETCLOVG tags |

### What they want next

- Stronger **standardization** (aligns with OAN trust layer — `@concepts/openagenet-trusted-agent-discovery.md`)  
- **Low-code / plugin** onboarding (skills marketplace patterns)  
- **Operational support** (SeClaw trajectory eval, defenseclaw admission)  

### vs Queen-Bee (2606.06545)

Queen-Bee is **architecture prototype** for governed MCP; this paper is **qualitative adoption evidence** from practitioners — complementary, not duplicate.

## Snippets

> "Participants also expressed strong demand for better standardization, lower adoption barriers through low-code or plugin-based approaches, and more systematic operational support."

> — [Source: arxiv-enterprise-mcp-adoption-2606.09182.md, retrieved 2026-06-11]
