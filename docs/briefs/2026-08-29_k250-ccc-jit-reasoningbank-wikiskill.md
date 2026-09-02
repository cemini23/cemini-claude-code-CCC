## Target
CCC wiki + harness policy — alert-only REFERENCE

## Summary
K250 harness-intelligence batch: JIT-Agent (2608.25593), ReasoningBank (2509.25140), WikiSkill (2608.27454). REFERENCE clones only; trainer wont_wire.

## Body
- **JIT-Agent** — `.local/adopts/JIT` (~124MB). Just-in-time harness synthesis; competitive with OpenCode/Claude Code on reported benches. Do **not** PATH-swap `/route`.
- **ReasoningBank** — `.local/adopts/reasoning-bank`. Reasoning-memory + MaTTS. Pairs K314 EM/WM vocabulary.
- **WikiSkill** — no public repo; policy pattern for validation-gated skill+wiki co-evolution (K324/K237).
- **Phase-1:** already policy_wired K313/K281/K292. HITL before harness mutation.

## Sources
@concepts/k250-harness-intelligence-wave.md · @concepts/k250-skill-evolution-wave.md
