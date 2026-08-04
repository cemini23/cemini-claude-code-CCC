---
title: Self-healing agent sessions — failure taxonomy and retry budget for Claude Code
type: concept
tags: [concept, reliability, self-healing, claude-code, conductor, retry, fault-tolerance, cross-wiki-route]
keywords: [self-healing, failure-taxonomy, retry-budget, corrective-reprompt, replanning, mcp-disconnect, context-truncation, conductor-failure]
related:
  - concepts/code-as-agent-harness.md
  - entities/tools/claude-code.md
  - entities/tools/conductor-mcp.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - entities/mcp-servers/stash.md
  - entities/tools/claude-mem.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/hermes-agent.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - sources/arxiv-skilladaptor-2606.01311.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - sources/arxiv-agent-trajectory-sentinel-2608.02464.md
  - entities/tools/agent-trajectory-sentinel.md
maturity: draft
created: 2026-05-21
updated: 2026-08-04
cross-wiki-source: "@osint-wiki/sources/arxiv-self-healing-llm-agents-2605.06737.md"
---

## Relations

- `@concepts/code-as-agent-harness.md` — harness mechanisms include feedback control; this page is the reliability layer
- `@entities/tools/claude-code.md` — host harness whose sessions fail in predictable ways
- `@entities/tools/conductor-mcp.md` — fan-out failures (kb-server down, subagent timeout)
- `@concepts/subagent-orchestration.md` — subagent return is the monitor boundary for delegated work
- `@concepts/hooks-for-automation.md` — Stop-hook loops are a self-healing risk if misconfigured
- `@entities/mcp-servers/stash.md` — execution traces + outcomes for integrated monitoring
- `@entities/tools/claude-mem.md` — cross-session failure patterns
- `@entities/patterns/glasswing-deliberate-disagreement.md` — recovery via adversarial re-check, not blind retry
- `@entities/patterns/full-prompt-goal-template.md` — `/goal` Stop hook must not create infinite heal loops
- `@concepts/telemetry-deterministic-agent-failure-repair.md` — K242 adds ESN+CUSUM telemetry trigger + rollback+re-run (45% repair vs 16% resample)

Cross-wiki: `@osint-wiki/sources/arxiv-self-healing-llm-agents-2605.06737.md` (Samsung SDS / Yonsei, 13pp); `@osint-wiki/concepts/code-as-agent-harness.md` links verification + feedback in harness mechanisms.

## Raw Concept

Routed from `briefs/2026-05-21_k48-code-as-harness-and-self-healing-from-osint.md`. Question: **what failure classes appear in long Claude Code sessions, and what retry policy avoids infinite loops while mirroring the survey's integrated monitor (reasoning traces + execution outcomes)?**

## Narrative

arXiv:2605.06737 proposes **reliability-aware self-healing**: failure taxonomy → reliability model → pattern-based detection → recovery via adaptive replanning and corrective prompting. The load-bearing idea for CCC: monitor **internal reasoning traces and external execution outcomes together** — not a success-bit alone.

This is a **design pattern document**, not a library adoption. Cemini already has fragments (reviewer subagent, `/goal` gating, conductor fan-out); this page names them under one taxonomy.

### Failure taxonomy — Claude Code / conductor sessions

| Class | Symptom | Typical cause | First response |
|-------|---------|---------------|----------------|
| **Tool timeout** | Bash/MCP call hangs or exceeds limit | Network, large repo op, tunnel down | Narrow scope; retry once with smaller command |
| **MCP disconnect** | Red MCP in UI; tool errors | SSH tunnel stale (`stash`, `prod-mcp`); stale session ID; non-protocol stdout on stdio transport (2606.05339) | Fix tunnel; `Retry` MCP; check session header; verify server logs only on stderr; do not auto-replan in a loop |
| **Context truncation** | Lost early instructions; repeated mistakes | Window fill; harness compaction | Refresh `hot.md`; re-inject goal; delegate heavy read to subagent |
| **User interrupt** | Operator cancelled turn | Intentional | Stop retries; update `hot.md` with abort reason |
| **Hallucinated path** | Edit/Read on non-existent file | Model drift | `Glob`/`Grep` verify; corrective re-prompt with actual paths |
| **Subagent empty/error** | `Agent` returns failure or thin summary | Bad prompt, wrong `subagent_type` | Re-dispatch with tighter task spec; max **2** retries per subagent task |
| **Conductor fan-out fail** | `conductor_query` error or empty synthesis | kb-server down, wrong alias | Fall back to direct `index.md` + `Read` on target wiki |
| **Stop-hook loop** | Session never ends | `/goal` criteria too vague | Human edits goal or disables hook — **never** auto-increment retries on Stop |

### Retry policy (retry budget)

| Severity | Policy | Budget |
|----------|--------|--------|
| Transient infra (MCP, tunnel) | Fix environment, single retry | 1 retry after fix |
| Wrong tool args / path | Corrective re-prompt with evidence | 2 per task |
| Wrong plan / approach | Full replan (new subagent or new user message) | 1 replan before escalate |
| Repeated same failure | Escalate to human | 0 auto — log in `wiki/log.md` or brief |

**Anti-pattern:** infinite Ralph-style loops without a shrinking retry budget. Pair with `@entities/patterns/full-prompt-goal-template.md` — Stop hook blocks exit until done, so healing must not spawn unbounded inner loops.

### Integrated monitor (CCC manifestation)

| Survey monitor input | CCC source |
|---------------------|------------|
| Internal reasoning traces | Assistant turns in session; claude-mem observations |
| External execution outcomes | Tool results (exit codes, MCP errors, file diffs) |
| Reliability signal | Operator judgment + optional reviewer subagent |

`@entities/patterns/glasswing-deliberate-disagreement.md` is the preferred recovery when verification matters — disagreement gates progress instead of blind corrective re-prompt.

### Conductor reliability note

When `@entities/tools/conductor-mcp.md` fails, treat as **Tool Interface / Lifecycle** failure per `@concepts/etclovg-harness-layers.md`: do not burn parent context re-trying conductor; switch to direct wiki reads and file a query log entry if the failure is novel.

### vs HarnessFix (2606.06324)

| Pattern | Scope |
|---------|-------|
| Self-healing (this page) | **In-session** retry/replan within retry budget |
| `@concepts/failed-trajectory-harness-repair.md` | **Cross-session** harness code mutation from failed traces |

When the same failure class repeats across sessions, escalate from self-healing to flaw-record + harness edit (OpenSpec, skill re-vet), not more retries.

### Cross-session harness evolution (2606.05922)

`@concepts/retrospective-harness-optimization-rho.md` — **RHO** batches past trajectories into a coreset, re-rollouts with self-validation/consistency signals, and promotes harness edits only when pairwise self-preference beats baseline (Sj > 0). Complements in-session retry budget on this page.

### MCP fault taxonomy overlay (2606.05339)

`@concepts/mcp-server-runtime-fault-taxonomy.md` names the coordination faults behind generic "MCP disconnect" rows:

| Symptom in session | Likely taxonomy class |
|--------------------|----------------------|
| Tool ran but agent ignored result | Tool → Result propagation |
| Malformed args, opaque stack trace | Tool → Execution (schema validation) |
| Works once, fails after reconnect | State → Session State (stale ID) |
| Intermittent parse errors on stdio MCP | Transport → Stdio (non-protocol stdout) |
| "Success" but wrong data returned | Tool → Silent failure / Data & Schema |

Use taxonomy leaf names when filing `wiki/log.md` entries — speeds dedupe across MCP servers.

## Snippets

> "This study distinguishes itself by establishing an integrated monitoring system that combines the agent's internal reasoning process with external execution results."
> — [Source: arXiv:2605.06737 via @osint-wiki/sources/arxiv-self-healing-llm-agents-2605.06737.md]
