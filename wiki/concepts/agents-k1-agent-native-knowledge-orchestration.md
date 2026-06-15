---
title: Agents-K1 — agent-native knowledge orchestration (REFERENCE)
type: concept
tags: [concept, agents-k1, knowledge-graph, librarian, cross-wiki-route, k114]
keywords: [2606.13669, scholar-kg, graphanything, five-module-schema, tri-source-cli]
related:
  - sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md
  - concepts/interaction-native-knowledge-harness.md
  - entities/mcp-servers/librarian-kb-server.md
  - entities/tools/conductor-mcp.md
  - concepts/cross-wiki-routing.md
  - osint-wiki/concepts/librarian-server-architecture.md
  - osint-wiki/concepts/interaction-native-knowledge-harness.md
  - entities/mcp-servers/llm-wiki-compiler.md
  - concepts/internet-of-agentic-ai-ioai.md
maturity: draft
created: 2026-06-13
updated: 2026-06-15
cross-wiki-source: "@osint-wiki/entities/mcp-servers/librarian-kb-server.md"
---

## Relations

- `@sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md` — arXiv 2606.13669
- `@concepts/interaction-native-knowledge-harness.md` — graph retrieval + wiki audit parallel (InKH)
- `@entities/mcp-servers/librarian-kb-server.md` — Cemini 24/7 wiki RAG serving
- `@entities/tools/conductor-mcp.md` — cross-wiki query over librarian index
- `@concepts/cross-wiki-routing.md` — wiki ingest vs automated KG pipeline boundary
- `@osint-wiki/concepts/librarian-server-architecture.md` — serving-layer architecture canon
- `@osint-wiki/concepts/interaction-native-knowledge-harness.md` — financial InKH deployment (OSINT)
- `@entities/mcp-servers/llm-wiki-compiler.md` — Karpathy compile-to-MD pattern contrast

## Raw Concept

2606.13669 **Agents-K1** — end-to-end pipeline converting raw documents into **agent-native multimodal knowledge graphs** with auditable provenance and a tri-source agent CLI — vs chunk-RAG or flat citation graphs.

## Narrative

### Agent orchestration vs knowledge orchestration

| Layer | Question | Cemini today |
|-------|----------|--------------|
| Agent orchestration | How do agents plan, delegate, verify? | Claude Code, conductor, subagents, hooks |
| Knowledge orchestration | What structured evidence can agents retrieve and cite? | Git `wiki/` → librarian kb-server; manual ingest |

Agents-K1 targets the second gap: full-paper extraction (entities, claims, mechanisms, citation **intent**, multimodal evidence) into **Scholar-KG** (2.46M papers claimed; 1M subset released).

### Three components

1. **KG layer** — five-module schema (A meta, B explicit mentions, C implicit abstractions, D citation relationships, E fine-grained triples); semantic-anchor multimodal graph
2. **LLM layer** — 4B GRPO extraction backbone (affordable domain retarget)
3. **GraphAnything CLI** — web + graph retrieval + cross-document traversal (MCP/API)

**General-KG** — schema-adaptive views (binary/nary/temporal/event/diy YAML) for legal, medical, financial corpora without retraining weights.

### vs Cemini librarian [TENTATIVE]

| | Agents-K1 Scholar-KG | Cemini wiki + kb-server |
|--|---------------------|-------------------------|
| Provenance | Span-level graph IDs | Markdown pages + `@path` links |
| Multimodal | Figures/tables/equations first-class | PDFs in `/opt/cemini-bulk`; wiki text-primary |
| Citation semantics | support/contrast/extend typed edges | `related:` bidirectional, manual |
| Scale path | Automated 2.46M paper pipeline | Human/LLM curated federation wikis |
| Audit surface | Graph + evidence spans | `wiki/` + `wiki_lint.py` + maturity |

**Verdict:** **REFERENCE** — steal five-module evidence model and tri-source CLI pattern for briefs; **do not** fork Scholar-KG on laptop. KG-at-scale deployment decisions belong on `@osint-wiki` librarian track.

### Posture

- **CCC:** concept + source stubs; link to OSINT for serving implications
- **OSINT:** evaluate GraphAnything MCP vs lazy-tool/kb-server for research-agent workflows
- **Prod:** NO-GO until license/ops audit on Agents-K1 release artifacts

## Snippets

> "Most recent work has focused on agent orchestration. The knowledge counterpart, however, remains much less developed."

> "An agent can trace each answer or decision back to stable graph identifiers and exact evidence."

> — [Source: arxiv-2606.13669-agents-k1-towards-agent-native-knowledge-orchest.pdf §1,3, retrieved 2026-06-13]
