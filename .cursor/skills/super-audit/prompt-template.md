# {{AUDIT_TITLE}} — super audit (5 auditors)

You are auditor **{{MODEL_SLOT}}** in a **5-model super audit**.

**Mode:** `{{MODE}}` · **Readonly** — markdown report only; no edits.

---

## Mission (single sharp question)

{{MISSION_QUESTION}}

Deliver:

1. **Verdict** PASS/WARN/FAIL on current posture
2. **What's working** vs **what isn't**
3. **Ranked patch backlog** (P0 before deadline, P1 after) — smallest diffs first
4. {{EXTRA_DELIVERABLE_4}}
5. {{EXTRA_DELIVERABLE_5}}

---

## Context

{{DOMAIN_CONTEXT_TABLES_AND_NARRATIVE}}

---

## Regime boundaries

{{REGIME_DISCIPLINE_BULLETS}}

---

## Data pack files (READ these paths)

```
{pack_index}
```

---

## Prior audit consensus (validate — do not repeat blindly)

{{PRIOR_AUDIT_BULLETS_OR_NONE}}

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|

### {{DOMAIN_RECOMMENDATION_SECTION_TITLE}}
{{DOMAIN_RECOMMENDATION_FIELDS}}

### Root cause
One paragraph — or "insufficient evidence" + what to inspect next

### Ranked patch backlog
| P | Patch | Effort | Expected lift |
|---|-------|--------|---------------|

### Unique angle
One thing other auditors might miss

### Confidence
high | medium | low

---

## Constraints

{{CONSTRAINT_BULLETS}}

---

## Already ruled out

{{RULED_OUT_OR_NONE}}
