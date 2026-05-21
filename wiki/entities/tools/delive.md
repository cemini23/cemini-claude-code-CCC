---
title: "DeLive — system-audio capture + MCP server + agent skill (Apache-2.0)"
type: entity
tags: [tool, mcp-server, agent-skill, audio-capture, asr, desktop-bridge, cross-wiki-route]
keywords: [delive, ximilalaxiang, system-audio, asr, mcp-server, agent-skill, electron, desktop-bridge]
related:
  - entities/mcp-servers/anthropic-skills.md
  - concepts/hooks-for-automation.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md"
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — DeLive ships both MCP server + agent skill; a clean worked example of the dual-surface pattern
- @concepts/hooks-for-automation.md — real-time audio triggers could feed hook events (e.g., "agent task complete" → TTS notification)
- @osint-wiki/sources/multi-wiki-tool-eval-26url-2026-05-19.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from OSINT K54 (26-URL eval) and K55 (19-URL eval). `XimilalaXiang/DeLive` (Apache-2.0, 165★, Electron + TypeScript + React) captures local system audio, translates to real-time subtitles via 12 ASR backends across 60+ languages, and exposes the capability to Claude Code via both an MCP server and a configurable Agent Skill. Clean exemplar of the desktop-app → MCP → Claude Code capability-exposure pattern.

## Narrative

### Architecture

- **System audio capture** — Electron desktop app captures local system audio
- **12 ASR backends** — real-time speech-to-text across 60+ languages
- **MCP server** — stdio transport exposing transcription context to Claude Code
- **Agent Skill** — configurable, disabled by default, Bearer-auth gated
- **Apache-2.0** — clean for Cemini IP-sale readiness

### Why CCC cares

DeLive is the cleanest worked example in the current tool-eval corpus of a desktop app exposing its capability to Claude Code via MCP without giving up auth/control:

1. **Dual-surface pattern** — ships both MCP server AND Agent Skill; the skill wraps the MCP tools for Claude Code ergonomics while the MCP server handles auth/transport
2. **Bearer-auth gating** — the agent skill is disabled by default; Bearer auth ensures only authorised Claude Code sessions can access system audio
3. **Audio→Markdown→agent pipeline** — novel in the Claude Code ecosystem; system audio becomes agent-readable text becomes agent-actionable context

### Adoption posture

Apache-2.0. Phase-0 install + Bearer-auth audit recommended before wiring into any Cemini workflow. The architectural pattern (desktop capability → MCP → agent skill with auth gating) is extractable regardless of whether DeLive itself is adopted.

[CONFIRMED] — Apache-2.0 verified via GitHub API (K54 cross-wiki source).
