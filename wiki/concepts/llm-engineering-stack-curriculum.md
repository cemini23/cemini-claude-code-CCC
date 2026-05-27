---
title: LLM engineering stack curriculum — hands-on project path (2026)
type: concept
tags: [concept, llm-engineering, curriculum, k69]
keywords: [ahmad-osman, llm-engineering, fine-tuning, eval, rag, deployment]
related:
  - concepts/local-llm-mechanics-primer.md
  - concepts/rag-binary-quantization.md
  - concepts/context-engineering.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-20-2026-05-27.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @concepts/local-llm-mechanics-primer.md — K57 mechanics primer (Post 1); this page is the **project curriculum** layer (Post 2)
- @concepts/rag-binary-quantization.md — K69 Post 4 RAG memory optimization
- @concepts/context-engineering.md — window + retrieval discipline for agent harnesses
- @entities/tools/claude-code.md — Cemini primary harness; curriculum is reference for evaluating BYOK/local claims
- @sources/trading-posts-compilation-20-2026-05-27.md — Post 2 (@TheAhmadOsman)

## Raw Concept

K69 Post 2: step-by-step **LLM engineering projects** narrative (2026 edition) — build-from-scratch path covering data, training/fine-tuning, eval, RAG, and serving. Distinct from @concepts/local-llm-mechanics-primer.md (token/KV-cache mechanics only).

## Narrative

### CCC posture [TENTATIVE]

| Layer | Takeaway for Cemini |
|-------|---------------------|
| Curriculum shape | Ordered projects beat scattered tool installs — aligns with Phase-0 before Adopt |
| Primary stack | **Anthropic API + Claude Code** remains default; curriculum informs local/BYOK **evaluation**, not migration |
| Overlap | Post 2 author also wrote K57 LLMs-101 primer — read both; avoid duplicating mechanics on this page |

### Steal-from (pattern, not repo list)

- **Eval before scale** — benchmark harness before production agent loops
- **RAG as optional layer** — not a substitute for librarian/kb-server federation in Cemini
- **Serving tradeoffs** — prefill/decode + quantization vocabulary from primer applies when comparing Ollama claims

### Non-actions

- Do not treat the post's repo/tool list as vetted Adopt queue without Phase-0 (`@concepts/cross-wiki-tool-eval-inventory.md`).

## Snippets

> Step-by-step LLM engineering stack build (2026 projects edition). [TENTATIVE — @TheAhmadOsman, Posts.docx K69 Post 2]
