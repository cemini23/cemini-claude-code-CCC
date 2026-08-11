---
title: K268 — SHE safety harness evolution (2608.09885)
type: brief
target: hands-on
created: 2026-08-11
---

## Target

Hands-on (lab shelf) · claude.ai · Claude Desktop. Wiki: `@concepts/safety-harness-evolution.md` + `@sources/arxiv-2608-09885-she-safety-harness-evolution.md` + `@entities/tools/she-safety-harness-evolution.md`.

## Summary

**SHE** makes the **agent harness** (context, memory, tools, permissions, runtime control) an *evolvable* safety object: four functionally decoupled artifacts, an attribution-guided evolution loop, and a validity check + safety–utility selection that stops reward-hacking. Results: Agent-SafetyBench ASR **8.6%→5.5%**, Clean UBR **25.7%→19.8%**, UA **33.5%→47.6%**; vs static SafeHarness **3.1× lower ASR**. **GO** clone — Apache-2.0, `github.com/RainbowQTT/SHE` @ `0c656460`, local `raw-sources/repos/SHE` (~4.7MB). Wire **K268** → phase1-policy-wires + lab-redteam. Lab/offline only; HITL before mutating prod harnesses.

## Body

### The four artifacts

| Artifact | Responsibility |
|----------|----------------|
| System Prompt | Global behavioral contract: source hierarchy, capability grounding, trust-boundary commitments |
| Rule Bank | Structured rules for risk classification + intervention (allow/warn/block/sanitize/judge) |
| Safety Memory | Experience from failure cases unresolved after repeated evolution attempts |
| Tool Policy | Tool authority + runtime enforcement for calls, observations, blocked actions, final-response recovery |

### The evolution loop

rollout → `RiskRelevant` cases → diagnose along **harm domain · attack surface · failure mode** → route to the **smallest responsible artifact** → bounded local edit → `ValidEdit` (rejects reward-hacking/evaluator-specific shortcuts and capability-removal-only "gains") → select only if `S↑ ∧ U≥` → store rejection feedback `Frej` for later rounds.

### Results worth quoting

- Agent-SafetyBench: ASR 8.6%→5.5%, Clean UBR 25.7%→19.8%, UA 33.5%→47.6%.
- vs static SafeHarness: ASR 17.1%→5.5% (3.1×), UA 31.6%→47.6%.
- Held-out AgentHarm: Harm Score 19.8%→9.8%, Harm Refusal 78.4%→86.4% — **cross-model transfer** without re-evolution (evolved on DeepSeek-V3.2 → Kimi K2.6 / GLM-5.2 / MiniMax M2.7).
- 20 rounds over 15-task split (90 task-condition instances, 180 trajectories/round); 185 other tasks held out.

### Lab-adoption constraints

- **No unbounded self-modification of a LIVE/production harness** — run evolution in a lab/offline loop with safety–utility selection and a rollback path (pairs HarnessOpt K230-adjacent + self-evolving-agent-security).
- The validity check is the guardrail *on the evolution itself* — it exists to stop the loop from gaming its own evaluator.
- Judge/diagnosis model quality bounds attribution quality — audit the judge before trusting evolved artifacts.
- **Not** a model-weight trainer and **not** an attack generator — it's a harness-safety tool.

### Ref / wire

- Concept: `safety-harness-evolution.md` · Entity: `she-safety-harness-evolution.md` (GO, local adopt) · Wire: `cemini-phase1-policy-wires.mdc` (K268) + `cemini-cybersec-lab-redteam.mdc`.

## Sources

- arXiv:2608.09885 (15 pp) + `github.com/RainbowQTT/SHE` README @ `0c656460` — `wiki/sources/arxiv-2608-09885-she-safety-harness-evolution.md`
