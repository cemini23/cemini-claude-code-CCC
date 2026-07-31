---
title: Memory poisoning Write–Execute–Forget lifecycle
type: concept
tags: [concept, memory, security, poisoning, k228]
keywords: [MemSecBench, WEF, selective repair, persistence]
related:
  - sources/arxiv-memsecbench-memory-poisoning-lifecycle-2607.27080.md
  - concepts/agent-data-injection-attacks.md
  - concepts/hidden-user-state-recovery-audit.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/dual-representation-agent-memory.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
maturity: draft
created: 2026-07-30
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-memsecbench-memory-poisoning-lifecycle-2607.27080.md`
- `@concepts/agent-data-injection-attacks.md`
- `@concepts/hidden-user-state-recovery-audit.md`
- `@concepts/hierarchical-bounded-agent-memory.md`

## Raw Concept

Does malicious content persist in agent memory, cause later actions, and can it be selectively repaired without wiping everything?

## Narrative

**MemSecBench** WEF protocol across 310 cases / 24 configs: persistence **84.2%**, Write–Execute **50.3%**, selective repair **56.1%** among poisoned cases. Memory backends differ by up to ~16pp attack success and ~41pp repair.

**Cemini steal:** Audit memory writes (provenance + TTL); re-verify before acting on recalled rules; prefer selective forget over full wipe; test Native vs Mem0-class backends separately (claude-mem / hot.md included).

**Verdict:** **ADOPT** WEF checklist. **NO-GO** bench install (no artifact).
