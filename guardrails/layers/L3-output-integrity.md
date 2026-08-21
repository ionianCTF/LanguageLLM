# L3 — Output Integrity

Specifications every deliverable must satisfy before it leaves the agent.
The runbook that applies this layer is
[`checklists/post-execution.md`](../checklists/post-execution.md).

> Version 1.0.0 · 2026-08-21 · Grounded in root README §8 and `_meta/ARCHITECTURE.md §5`

---

## 1. Change-log schema (G15)

Every non-trivial change emits one structured entry:

```json
{
  "original": "Each applicant must submit his resumé.",
  "revised": "Each applicant must submit their resumé.",
  "category": "invisibility-omission",
  "rule": "gender.pronoun-strategy R2",
  "severity": "high",
  "confidence": 0.95,
  "rationale": "Generic masculine pronoun for unknown-gender referent."
}
```

Required fields: `original · revised · category · rule · severity · confidence · rationale`
Optional fields: `uncertainty_note` · `human_review`

## 2. Severity scale

| Level | Meaning |
|---|---|
| `critical` | Demeaning/dehumanising language; misgendering a named person |
| `high` | Systematic exclusion (generic masculine, male-as-default) or stereotype reinforcement |
| `medium` | Trivialisation, unnecessary gendering, non-preferred but recognisable terms |
| `low` | Style/readability improvements; borderline cases for human decision |

## 3. Confidence policy (G8 + G15)

| Confidence | Behaviour |
|---|---|
| ≥ 0.90 | ship silently |
| 0.70 – 0.89 | ship with `uncertainty_note` attached to the entry |
| < 0.70 | `human_review: true` — never guess |

## 4. Hard integrity constraints

- **Quote integrity (G5):** quotations, titles, legislation names, direct speech
  preserved verbatim; bias inside quotes is *marked*, never silently modernised.
- **Tone (G15):** explanations neutral and professional; zero moralising;
  audits report findings, they do not lecture.
- **Language scope (G13):** non-English output carries the scope notice plus a
  pointer to the relevant language-specific guide.
- **No fabrication:** never invent sex-disaggregated or demographic statistics.

## 5. Deliverable modes

| Mode | Condition | Output |
|---|---|---|
| `full` | no violations above V-LOG | text + change log |
| `flagged` | ≥1 V-WARN or open human-review item | text + annotations + review items at top |
| `blocked` | any unresolved V-BLOCK | findings + required fixes only — the text itself is **not** emitted |

## 6. Metrics counters

Emit with every change log so behaviour stays regression-testable:

```
g_checks_total · v_block · v_warn · v_log · human_review_requests
```
