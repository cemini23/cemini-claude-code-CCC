---
title: "red-run — offensive-sec Claude Code agent-team orchestrator (orchestration patterns extractable; payloads not)"
type: entity
category: tool
tags: [entity, tool, claude-code-agent-teams, sliver-c2-wrapper, sqlite-state, chromadb-rag, k44, steal-from-orchestration-patterns-only-phase-0-2026-05-14, gpl-3-poison-pill, evasion-features-auto-reject-signal]
keywords: [red-run, blacklanternsecurity, kevinoriley-solo, agent-team-coordination, lead-router-pattern, single-writer-state-mgr, enum-ops-pair, semantic-skill-router, gpl-3-poison-pill, AMSI-bypass-do-not-extract]
related:
  - concepts/subagent-orchestration.md
maturity: validated
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @concepts/subagent-orchestration.md — lead-router + single-writer state-mgr + enum/ops-pair patterns are clean-room extractable orchestration designs
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python offensive-security agent-team orchestrator using the standard **Claude Code agent-teams API** (`TeamCreate` / `Agent(team_name=…)` / `SendMessage`) — NOT tmux-pane routing as K44 framed it. Uses `sliver-py` gRPC client (Sliver is BSD-3-Clause; the wrapper is GPL-3.0). SQLite for state, ChromaDB + sentence-transformers for semantic skill retrieval. **GPL-3.0, 162 stars verified (vs claimed 160), 19 forks, 4 contributors (kevinoriley solo: 272/280 commits), created 2026-02-22, last push 2026-04-01**. K44 verdict refined to **STEAL-FROM-ORCHESTRATION-PATTERNS-ONLY** with strict offensive-payload blocklist.

## Narrative

### Phase-0 audit verdict (2026-05-14): STEAL-FROM-ORCHESTRATION-PATTERNS-ONLY (CCC) / REFERENCE-ONLY (Cybersec)

Two compounding constraints govern this audit: **GPL-3.0 isolation** + **offensive-security context**. Even under MIT, Cemini would not adopt the offensive payloads; the GPL license rules out vendoring; the only path is clean-room re-implementation of domain-neutral orchestration patterns.

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | License = GPL-3.0 verbatim | **PASS-CONFIRMED** | LICENSE = GNU GPL v3.0, no commercial dual-license |
| G1 | Active maintenance | **PASS** | 6-week-old push, 360-line CHANGELOG, active issue closes |
| G2 | Contributor diversity | **WEAK** | Single-author (kevinoriley: 272/280 commits, bus factor 1) |
| G3 | Sliver = wrapper or embedded | **WRAPPER ONLY** | `sliver-py` gRPC client, no Sliver code embedded. Sliver itself is BSD-3-Clause but irrelevant — red-run's wrapper IS GPL-3.0 |
| G4 | Authorized-use disclaimer | **PASS** | README §Disclaimer explicit on CFAA, "CTF and lab use only," written-permission requirement |
| G5 | **Detection-evasion features** | **FAIL — AUTO-REJECT SIGNAL** | `agents/evasion-agent.md`, `teammates/bypass.md`, `skills/evasion/av-edr-evasion/` covering AMSI bypass, ETW patching, AV/EDR evasion, mingw payload compilation |
| G6 | Orchestration cleanly separable | **PARTIAL** | Lead / teammate / state-mgr / skill-router are domain-neutral patterns; technique skills are inseparably offensive |
| G7 | Cemini stack-fit (defensive/quant) | **NO-FIT** | Entire tool is offensive-purpose; zero overlap with quant-finance |
| G8 | Skill-router design portable | **YES** | ChromaDB + sentence-transformers + YAML-frontmatter indexing is generic (already conceptually in Cemini's `kb-server`) |
| G9 | Multi-agent novelty vs CCC existing | **LOW** | Uses standard Claude Code agent-teams API; pattern documented at code.claude.com/docs/en/agent-teams |

### Clean-room re-implementable orchestration patterns (CCC-wiki only)

1. **Lead-as-router + AskUserQuestion gates** — orchestrator NEVER executes target-touching tools, only routes; every spawn + task assignment requires explicit operator approval via `AskUserQuestion`. Source: `skills/ctf/SKILL.md` §"DO NOT RUN TOOLS DIRECTLY". **High value** for Cemini's confirmation-gated tool calls.
2. **Single-writer state-mgr teammate pattern** — one persistent agent is the sole writer to a shared SQLite store; peer agents send structured `[action]` messages (key=value protocol) instead of calling write tools directly. Centralizes dedup + graph coherence. Source: `teammates/state-mgr.md`.
3. **Enum/Ops teammate split** — paired teammates per domain: one discovers (read-only), one actions (write/exploit), lead routes between them on findings. Domain-neutral (works for "research-agent vs writer-agent").
4. **Semantic skill-router (RAG over skill library)** — index `skills/<cat>/<name>/SKILL.md` YAML frontmatter into ChromaDB with `all-MiniLM-L6-v2`; agents call `search_skills(query)` for natural-language retrieval. Cemini's `kb-server` covers indexing; the novelty is the `get_skill()` MCP load-on-demand pattern.

### DO NOT EXTRACT (explicit blocklist)

- `tools/sliver-server/` — Sliver C2 plumbing (combined work is GPL-3.0 + offensive)
- `skills/evasion/`, `skills/post-exploit/`, `skills/privesc/`, `skills/credential/`, `skills/ad/` — AMSI/ETW/payload code, Kerberoasting, NTLM relay, lateral-movement
- `agents/evasion-agent.md`, `agents/*-privesc-agent.md`, `agents/password-spray-agent.md`, `teammates/bypass.md`, `teammates/spray.md`, `teammates/recover.md`
- `tools/shell-server/`, `tools/rdp-server/`, `tools/nmap-server/`, `tools/browser-server/` — target-touching MCP wrappers
- Payload templates in `operator/templates/`
- Attack-technique terminology from CHANGELOG ("actioned vulnerabilities," "via_credential_id" graph schema)

### Red flags (auto-reject signals)

- **G5 auto-reject confirmed**: `skills/evasion/av-edr-evasion/SKILL.md` explicitly covers AMSI bypass, ETW patching, CrowdStrike/SentinelOne evasion (`opsec: high`). This disqualifies the tool from any role in Cemini's stack beyond pattern reference.
- Repo CLAUDE.md openly states "fully autonomous AI agents" + "no stealth considerations" + "may trigger Anthropic content policy warnings on your account" — operational risk well outside Cemini's defensive perimeter.

### K44 framing corrections

- "Distributed terminal pentest ops via tmux panes" — **wrong**. red-run uses the standard Claude Code agent-teams API, not tmux pane routing. tmux is not mentioned in the codebase.
- "Subagent orchestration masterclass" — accurate for the lead/router/single-writer/skill-router patterns; everything else is offensive payload code.

### Recommended next step (CCC concept pages, no code)

Port the four orchestration patterns into `@ccc-wiki/concepts/`:
- `concepts/lead-router-pattern.md`
- `concepts/single-writer-state-mgr.md`
- `concepts/enum-ops-pair-pattern.md`
- `concepts/mcp-skill-router-pattern.md`

High-level prose specs only — no code, no skill text, no payloads — suitable for clean-room re-implementation.

## Snippets

> "This repository offers a masterclass in subagent orchestration, utilizing Claude Code agent teams to coordinate operators across distinct tmux panes via orchestrator variants such as /red-run-ctf. The architecture relies on SQLite for state tracking and ChromaDB for RAG-based semantic skill retrieval."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶37 — Phase-0 audit confirms the agent-teams + ChromaDB framing but contradicts "tmux panes" (red-run uses the standard Claude Code agent-teams API, not tmux). Evasion features in `skills/evasion/` are auto-reject for Cemini adoption beyond pattern-level reference.]
