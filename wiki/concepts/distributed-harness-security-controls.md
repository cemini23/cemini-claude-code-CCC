---
title: Distributed harness security controls (SHarD pattern)
type: concept
tags: [concept, harness, security, sandbox, skill-scan, k225]
keywords: [SHarD, OWASP agentic, OS sandbox, tool restriction]
related:
  - sources/arxiv-shard-harness-security-distribution-2607.25890.md
  - entities/tools/shard-secure-harness-distribution.md
  - concepts/etclovg-harness-layers.md
  - concepts/model-harness-six-responsibilities.md
  - concepts/skill-vetting.md
  - concepts/agent-vm-sandboxing.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-shard-harness-security-distribution-2607.25890.md`
- `@entities/tools/shard-secure-harness-distribution.md`
- `@concepts/skill-vetting.md`
- `@concepts/agent-vm-sandboxing.md`

## Raw Concept

Can off-the-shelf agent security controls be scaled to a distributed engineering base via a custom harness rather than vendor-only suites?

## Narrative

**SHarD** packages three control classes into a Pi-based distributable harness: **OS sandboxing**, **skill scanning**, **tool restriction**. On a 23-test OWASP-agentic suite it matched the best secured commercial agent (adjusted **100%**). Model non-determinism can make security outcomes inconsistent — retest, don't one-shot.

**Cemini steal:** Prefer harness-level distribution of controls (federation skills + sandbox + tool allowlists) over hoping each teammate configures vendor UI identically. Never `curl | sh` their demo installer — clone MIT repos instead.

**Verdict:** **ADOPT** pattern. **GO** REFERENCE clones: `agent-security-lab`, `shard-demo`.
