---
skill: gender.gender-inclusive-rewriting
title: Gender-Inclusive Rewriting — Strategy Ladder & Substitutions
version: 1.0.0
category: gender
requires: [core.inclusive-language-core]
triggers: [rewrite, rephrase, transform text, make inclusive, replace chairman,
  gendered noun, generic masculine, rewrite sentence]
sources: [UNW-EN, EIGE-2019, CAPE-2023, IBEC-2015, EIGE-2024]
---

## Purpose

Transform gender-biased sentences and passages into gender-inclusive equivalents
using a deterministic strategy ladder, preserving meaning exactly.

## When to use

Any `transform` task on text containing gendered nouns, generic masculines,
gendered pronouns for unknown referents, or biased phrasing — outside legal/
contractual registers (use `gender.formal-legal-texts` there).

## Rules

**R1 — Run the strategy ladder in order; stop at the first strategy that produces
natural, meaning-identical prose:**

| Order | Strategy | Example |
|---|---|---|
| 1 | **Gender-neutral expression** — replace the gendered noun | "congressmen" → "legislators"; "chairman" → "chair" |
| 2a | **Omit the masculine reference word** | "Each professor should send one of his assistants" → "Each professor should send one assistant" |
| 2b | **Pluralise nouns + reference words** | "Each participant must present his ID badge" → "All participants must present their ID badges" |
| 2c | **Singular they** | "Each applicant must submit his resumé" → "Each applicant must submit their resumé" |
| 2d | **Passive voice (sparingly)** | "The student must submit his assignment by Monday" → "Assignments must be submitted by Monday" |
| 3a | **Dual forms he or she / she or he** | fallback when restructuring fails |
| 3b | **Alternating genders across examples/text** | alternate she/he between successive generic references |
| 3c | **Slashes her/his, he/she** | last resort; forms/letterheads only; avoid in public-facing narrative texts |

Constraints on the ladder:
- 2b (pluralisation) must not change scope: "Each employee is expected to organize
  his hours…" → plural form may imply collective scheduling. If individual duty
  matters, use 2c instead.
- 2d (passive) must not obscure agency where responsibility attribution matters.
- 3a repeated many times becomes stylistically heavy — prefer 1–2 at document scale.
- 3c is unacceptable in web features, press releases, narrative texts (UNW-EN).

**R2 — Substitute gendered nouns** using `references/substitution-tables.md` §1–§4.
Never substitute Latin-root words containing "man(u)" (manual, manufacture,
manipulate, manuscript).

**R3 — Remove irrelevant gender marking.** Delete "female"/"male"/"woman"/"man"
from neutral occupation terms ("male nurse" → "nurse") unless the gender dimension
is the point of the sentence (e.g. discussing occupational segregation).

**R4 — Fix connotative adjectives and false generics** per substitution tables §5–§6.

**R5 — Alternate fixed-order phrases** (§7): vary "men and women"/"women and men"
across a document; never default to male-first ordering.

**R6 — Replace diminutives and endearments** (§8): -ess/-ette forms → base term;
terms of endearment toward non-intimates → name or role term; adult women are
never "girls".

**R7 — Empowerment framing.** Prefer active voice and non-patronising collocations:
"investing in women" → "investing in women's potential"; "mastering a skill" →
"being competent in a skill". Do not attach negative connotations to verbs used
with women as subjects.

**R8 — Preserve register.** Match the formality of the source. Log which ladder
position was chosen when the choice is register-sensitive (see D1/D2 divergences).

## Procedure

1. Parse the passage; list every gendered token (nouns, pronouns, adjectives,
   fixed phrases, titles).
2. For each token, consult the substitution tables; if absent, construct the
   minimal neutral equivalent.
3. Apply R1 ladder to pronoun-bearing sentences.
4. Re-read the full passage for agreement drift (verb agreement after singular
   they, determiner agreement after pluralisation).
5. Verify meaning preservation (G1): who is covered, what obligations/scopes
   exist, any quantities or conditions unchanged.
6. Emit revised text + change log entries (category, rule, severity, confidence).

## Worked example (EIGE-2024 vacancy notice)

Original:
> The Chocolate Foundation Board is looking for a new chairman … He will be
> expected … drawing from his extensive business insights … Each candidate must
> submit his application by Monday 12 December at 12:00.

Revised:
> The Chocolate Foundation Board is looking for a new chair … He/she/they will be
> expected … drawing from his/her/their extensive business insights … Each
> candidate must submit their application by Monday 12 December at 12:00.

Changes: chairman→chair (R2); pronoun set opened with they (R1-3c acceptable here
as deliberate visibility choice); his→their in procedure line (R1-2c).

## Guardrails

- G1 meaning preservation overrides every table entry.
- G4 no over-correction: do not slash every pronoun pair through a long text.
- If the text deliberately discusses gendered language itself (linguistics,
  moderation), keep quoted forms inside quotation marks (G5).

## Uncertainty

If no neutral equivalent preserves nuance (e.g. "spinster" implying lifetime
unmarried status), keep the least-biased factual paraphrase ("woman who never
married" — only if marital status is relevant) and log low confidence.

## Sources

- UNW-EN: strategies A/B/C, additional tips, checklist.
- EIGE-2019: ch.4 solutions, ch.6 tables.
- CAPE-2023: alternative nouns, singular they, plural caution.
- IBEC-2015: exclusionary forms, false generics, biased terms.
- EIGE-2024: transformation worked example, empowerment framing.
