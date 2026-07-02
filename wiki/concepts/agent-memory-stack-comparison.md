---
title: Agent memory stack comparison — mem0, OpenClaw, Hermes, claude-mem
type: concept
tags: [concept, memory, openclaw, hermes, mem0, k72]
keywords: [mem0ai, openclaw, hermes-agent, claude-mem, memory-comparison]
related:
  - entities/tools/claude-mem.md
  - entities/tools/hermes-agent.md
  - entities/tools/claude-subconscious.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/three-cache-architecture.md
  - concepts/dual-representation-agent-memory.md
  - sources/arxiv-metis-text-code-memory-2606.24151.md
  - concepts/procedural-memory-transfer-after.md
  - sources/arxiv-procedural-memory-after-2606.23127.md
  - entities/mcp-servers/stash.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - concepts/agent-personality-file-hermes-openclaw.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - sources/arxiv-multi-factor-agentic-memory-2606.12945.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md
  - concepts/selective-experience-memory-harness.md
  - sources/arxiv-finacumen-experience-memory-harness-2606.17642.md
  - concepts/executable-user-memory-user-as-code.md
  - sources/arxiv-user-as-code-executable-memory-2606.16707.md
  - concepts/governed-fleet-shared-memory.md
  - entities/tools/memclaw.md
  - sources/arxiv-governed-shared-memory-2606.24535.md
  - concepts/event-sourced-poly-agent-handoff.md
  - sources/arxiv-esaa-conversational-event-sourced-2606.23752.md
  - concepts/hidden-user-state-recovery-audit.md
  - sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md
  - entities/tools/memprobe.md
  - concepts/metamemory-scaffold-proficiency-training.md
  - sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md
maturity: draft
created: 2026-05-27
updated: 2026-07-02
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@entities/tools/claude-mem.md` — **adopted** CCC session memory
- `@entities/tools/hermes-agent.md` — reference runtime (not prod)
- `@entities/tools/claude-subconscious.md` — Letta layer (K71); parallel-impl check
- `@concepts/agent-token-discipline-openclaw-hermes.md` — cost of always-on memory agents
- `@concepts/three-cache-architecture.md` — stash vs claude-mem vs wiki layering
- `@entities/mcp-servers/stash.md` — episodic goals/hypotheses

Cross-wiki: K72 Post 1 (@mem0ai); OSINT `@entities/tools/hermes-agent.md`.

## Raw Concept

K72 Post 1 — marketing comparison of **mem0**, **OpenClaw**, and **Hermes** persistent-memory approaches for always-on agents. CCC documents **selection matrix**, not multi-install.

## Narrative

| Layer | Product | CCC posture |
|-------|---------|-------------|
| Session + observation index | claude-mem | **In use** |
| Episodic federation | stash | **Global MCP** |
| Personal-agent runtime | Hermes / OpenClaw | **In use (operator)** — Hermes on librarian + laptop; not prod trading |
| Vector user memory API | mem0 | **Evaluate** — overlap risk with claude-mem |

| Recovery audit benchmark | MemProbe | **REFERENCE** — hidden user-state recovery; CC-BY-4.0 (K128) |
| Metamemory training | AutoMem (2607.01224) | **REFERENCE** — scaffold/proficiency loops; not verygoodplugins/automem (K137) |
| Fleet governed store | MemClaw | **REFERENCE** — scope/provenance; cybersec checklist K125 |
| Event-sourced handoff | ESAA-Conversational | **CONDITIONAL-GO** Windows only — receiver-validated replay |

**Rule:** one **SessionStart** memory owner — see `@entities/tools/claude-obsidian.md` rejection case study.

| Verdict | **REFERENCE** for product selection; **Hermes operator path live** — see `@osint-wiki/concepts/hermes-laptop-operator-playbook.md` |

## Snippets

> "mem0 + OpenClaw + Hermes memory comparison."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 1]
