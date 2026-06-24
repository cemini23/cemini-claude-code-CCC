---
title: cua — Computer Use Agent (M-series Mac VM sandbox)
type: entity
tags: [tool, agent-vm, sandbox, lume, apple-virtualization, mcp, claude-code]
keywords: [cua, computer use agent, lume, apple virtualization, agent sandbox, tracing, m-series mac, mcp server, isolation chamber]
related:
  - entities/tools/claude-code.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - entities/tools/gym-anything.md
  - concepts/agent-vm-sandboxing.md
  - concepts/agent-sandbox-unikraft.md
  - entities/tools/fara.md
maturity: draft
created: 2026-05-13
updated: 2026-06-24
---

## Relations

- `@entities/tools/claude-code.md` — host harness; cua plugs in as an MCP server
- `@entities/patterns/tier1-tier2-agent-model.md` — cua provides the isolation chamber Tier 2 agents need
- `@concepts/subagent-orchestration.md` — cua is the isolation primitive for execution-capable subagents
- `@concepts/hooks-for-automation.md` — companion to PreToolUse hooks for execution-gating
- `@entities/tools/gym-anything.md` — CMU visual-observation reference agents (coordinate mouse/keyboard); same VM-driven agent class, DEFER verdict
- `@concepts/agent-vm-sandboxing.md` — methodology page for which cua is the reference implementation

Cross-wiki: `@cybersecurity-wiki/entities/tools/cua.md` carries the canonical Phase-0 audit (GO verdict, 2026-05-13). `@osint-wiki/entities/tools/cua.md` carries the OSINT-side cross-route notes.

## Raw Concept

`github.com/trycua/cua` — MIT, 16k+ stars, 60 contributors. Apple-Silicon-native VM sandbox built on Lume (a thin wrapper around Apple's Virtualization.Framework — no QEMU overhead). Exposes the VM substrate to Claude Code (and any MCP client) via an MCP server.

## Narrative

cua's value to Cemini is the **isolation chamber pattern**: spin up a fresh OS image inside Lume, drive a Claude Code agent through whatever destructive / suspicious / experimental work needs doing, and capture a full trace (screenshot + accessibility tree + API-call log) at every step. The host OS stays untouched; the trace is replayable.

This is exactly the missing piece for Cemini's Tier-2 agent pattern (`@entities/patterns/tier1-tier2-agent-model.md`): Tier-2 agents declare `requires_scope: true` in YAML, but agent-policy ≠ network-policy ≠ filesystem-policy. cua provides the missing layer — actual VM isolation rather than trust-based policy gates.

### Hardware floor

- macOS Ventura (13.0)+ on Apple Silicon (M1+)
- Intel Macs out of scope (Lume relies on Virtualization.Framework's M-series-specific paths)
- ~2-5 GB per VM image (macOS guest), ~1-2 GB (Linux guest)
- Tracing payloads are GB-scale on long runs — plan rotation/offload

### Three install surfaces

```bash
# canonical
pip install cua
lume run --image ubuntu-22.04-arm64 --cpu 4 --memory 8G
cuabot --tracing-dir ./traces/2026-05/ "enumerate the local network"
```

- **MCP server** — exposes cua to Claude Code / Desktop. Standard skill-style integration.
- **Python SDK** — programmatic batches (CI-integrated test suites).
- **`cuabot` CLI** — ad-hoc interactive sessions.

### Cemini-side adoption posture (2026-05-13)

DRAFT — not in active Cemini use yet. Documented because:

1. **Tier-2 agent pattern needs an isolation chamber** — without one, the Tier-1/Tier-2 split is policy-only.
2. **Hooks-for-automation discipline** suggests pre-tool-use hooks for sandboxing-gated commands; cua is a candidate for that gate's other side.
3. **Cybersec wiki adopted it 2026-05-13** — Cemini may cross-pollinate the pattern when CCC develops a Tier-2 use case (e.g., experimental SKILL.md installs, untrusted MCP-server audits).

### What cua is NOT

- Not a Docker replacement — Docker images are the unit; cua's units are macOS/Linux VM images.
- Not a security guarantee — VM-escape attack surface is non-zero. cua isolates; it does not absolve. Host-OS patching still matters.
- Not free disk — tracing dirs fill GBs/day under heavy use; budget rotation.

## Snippets

> "Every agent action emits a screenshot + accessibility tree + API-call log, which makes post-mortem replay possible."
> [Source: `@cybersecurity-wiki/entities/tools/cua.md` 2026-05-13]

## Dead Ends

- **Running on Intel Mac** — won't work; M-series-only.
- **Treating cua-trace dirs as ephemeral** — they fill disk fast on long runs. Set rotation early.
- **Trusting Lume to be VM-escape-proof** — young framework; absence of published escapes is not absence of escapes. Patch the host.
