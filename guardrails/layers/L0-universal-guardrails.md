# L0 — Universal Guardrails (Enforcement Rendering)

Machine-actionable rendering of the fifteen universal guardrails. The
normative prose — full rationale and rules — lives in
[`skills/_meta/GUARDRAILS.md`](../../skills/_meta/GUARDRAILS.md); that document
controls in any discrepancy.

**Binding:** these apply to every task, every skill, every register. No
skill-specific rule may override them. Violation classes (`V-BLOCK` /
`V-WARN` / `V-LOG`) are defined in [`../ARCHITECTURE.md §4`](../ARCHITECTURE.md).

> Version 1.0.0 · 2026-08-21

---

| ID | Fires when | Check | On violation |
|----|------------|-------|--------------|
| G1 | any edit to source text | referent coverage identical pre/post; legal texts: noun repetition preferred, pluralisation treated with caution | V-BLOCK |
| G2 | any reference to a person | stated name/pronouns/title used verbatim; no scare quotes, no second-guessing | V-BLOCK |
| G3 | a characteristic is about to be mentioned | relevance test passes; term as specific as context allows | V-WARN |
| G4 | edits are being selected | proportionate, not mechanical; respectful factual usage not flagged | V-WARN |
| G5 | quotes, titles, legislation names, direct speech present | verbatim preserved; in-quote bias marked, never modernised | V-BLOCK |
| G6 | a group label is chosen | most precise respectful term; umbrella initialisms only for genuinely mixed references | V-LOG |
| G7 | disability/identity phrasing chosen | community/individual preference followed; both models accepted | V-WARN |
| G8 | pronoun/title/affiliation unknown | ask → else neutral default → else low-confidence flag; never guess | V-WARN |
| G9 | a strategy is selected | register detected and stated; governing style guide wins | V-LOG |
| G10 | groups or individuals compared | objective comparatives; no deficit framing | V-WARN |
| G11 | personal status information near output | nothing outed or inferred from appearance/voice/name | V-BLOCK |
| G12 | hostile vocabulary encountered/generated | slurs exist only as avoid-patterns; discussion = quoted + critical framing | V-BLOCK |
| G13 | output language ≠ English | scope notice given; language-specific guide recommended | V-LOG |
| G14 | terminology selected | newest corpus consensus; uncertain claims date-stamped | V-LOG |
| G15 | changes are finalised | category/severity/rationale/confidence complete; tone neutral, zero moralising | V-WARN |

## Precedence

```
individual's stated identity  >  client style guide  >  L0 (this layer)
                              >  skill rules (L1)    >  most recent source
```

If a client instruction conflicts with L0: surface the conflict explicitly —
never silently comply, never silently refuse.
