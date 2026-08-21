# Post-Execution Checklist (Layer L3)

Run **before finalising any output**. Decides whether the deliverable ships as
`full`, `flagged`, or `blocked`.

> Version 1.0.0 · Mirrors the enforcement checklist of
> [`skills/_meta/GUARDRAILS.md`](../../skills/_meta/GUARDRAILS.md)

---

## Part A — Universal guardrail sweep (L0)

- [ ] Meaning preserved? (G1)
- [ ] Known identities respected verbatim? (G2)
- [ ] No irrelevant characteristic introduced? (G3)
- [ ] Changes proportionate — no mechanical over-application? (G4)
- [ ] Quotes untouched? (G5)
- [ ] Terms as specific as justified? (G6)
- [ ] Person-first/identity-first handled per preference? (G7)
- [ ] Unknowns defaulted neutrally and flagged? (G8)
- [ ] Register detected and stated? (G9)
- [ ] Comparatives objective? (G10)
- [ ] Nothing outed or inferred? (G11)
- [ ] No slur generated outside avoid-tables? (G12)
- [ ] Language scope stated if non-English? (G13)
- [ ] Terminology current per corpus recency? (G14)
- [ ] Change log entries complete? (G15)

## Part B — Domain sweep (L1)

For each domain loaded during E1, confirm its `GD-*` entries held — full list
with violation classes in [`../layers/L1-domain-guardrails.md`](../layers/L1-domain-guardrails.md).
Pay special attention to the V-BLOCK entries:

- GD-CORE-01, GD-GEN-01, GD-GEN-04, GD-GEN-10
- GD-ETH-01, GD-LGB-01, GD-CLS-02, GD-REL-01, GD-REL-02
- GD-AI-01, GD-AUD-01

## Part C — Deliverable-mode decision

| Condition | Mode |
|---|---|
| Any unresolved **V-BLOCK** violation | `blocked` — do not emit the text; return findings + required fixes |
| No V-BLOCK, but ≥1 **V-WARN** or open human-review item | `flagged` — ship with annotations; list review items at top |
| Neither | `full` — ship with change log attached |

## Part D — Change-log completeness (G15)

Every non-trivial change entry carries:
`original · revised · category · rule · severity · confidence · rationale`
plus `uncertainty_note` when confidence < 0.9 and `human_review` where routed.
Tone of explanations: neutral, professional, zero moralising.

Emit metrics counters with the change log:
`g_checks_total · v_block · v_warn · v_log · human_review_requests`.
