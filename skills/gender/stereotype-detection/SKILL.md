---
skill: gender.stereotype-detection
title: Stereotype Detection — Three Categories of Gender-Discriminatory Language
version: 1.0.0
category: gender
requires: [core.inclusive-language-core]
triggers: [stereotype, detect bias, audit gender, sexist language, invisibility,
  trivialisation, patronising, semantic non-equivalence]
sources: [EIGE-2019, EIGE-2024, IBEC-2015, INTELLECT-2022]
---

## Purpose

Detect and classify instances of gender-discriminatory language into the three
canonical categories, with severity and evidence, before any rewriting occurs.

## When to use

First pass of any `transform` or `audit` task; also standalone bias scans.

## Rules

**R1 — Classify every finding into exactly one dominant category** (C1, C2, or
C3 below). If a hit plausibly fits several, choose the one matching the primary
harm; never double-count one issue across categories.

**R2 — Context-neutralisation check before flagging.** A signal inside a verbatim
quote, a historical reference, or a discussion *about* biased language is not a
violation (G5): record it at most as `low` with note "quote preserved".

**R3 — Apply the swap test for adjectives:** "Would this adjective describe a
different gender in the same context?" If not → C1 hit.

**R4 — Statistics rule.** If a gender-relevant phenomenon is reported without
disaggregation AND disaggregated data was supplied in the task inputs, flag C2
(medium) with a note. Never invent numbers (core R4).

## The three categories

### C1 — Stereotypes
Assigning gender when it is unknown or irrelevant because of stereotyped role
expectations. Two forms (EIGE): assuming all members of a profession share a
gender; assuming all members of a gender share a trait.

Detection signals:
- Gendered pronoun attached to an occupation/role with unknown referent
  ("I need to speak to the secretary — is she in the office?").
- Irrelevant gender modifiers ("female lawyer", "male nurse", "career woman").
- Gendered verbs ("man the front desk") for possibly-non-male staff.
- Inanimate objects personified as female ("the ship slipped her moorings";
  "France and her citizens"; "mother tongue" → "native language").
- Differential adjectives by gender (bossy/shrill/hysterical for women; see
  substitution tables §5) and semantic non-equivalence pairs (master/mistress).
- Stereotyped descriptors of objects/events ("a ladylike handshake" → "a weak
  handshake"; "throw like a girl" → "does not throw well"; "man up" → "be tough";
  "virile action" → "strong action").

### C2 — Invisibility / omission
Language casting the male as generic norm, erasing women (and non-binary people).

Detection signals:
- Generic "man/men": mankind, man in the street, "under the law all men are equal",
  "fire is man's greatest invention".
- Generic "he/his/him" for unknown referents ("Each applicant must submit his resumé").
- Male-default compounds: manpower, man-made, spokesman.
- False generics that evoke male images (fatherland; "man the desk").
- Asymmetric visibility: women mentioned only via relation to men ("attendees and
  their wives"); men described unmarked while women are marked ("Lithuania is
  playing well… Lithuania's women play tomorrow").
- Neutral wording that statistically describes only one gender without saying so
  ("14% of people experienced sexual violence" hiding the 23% women / 5% men split).

### C3 — Subordination / trivialisation
Language that belittles one gender or marks it as lesser/dependent.

Detection signals:
- Marital-status marking for women only (Miss/Mrs vs Mr); "Mr and Mrs John Smith"
  naming convention; "maiden name".
- Referencing asymmetry: surname for men, first name for women in parallel roles.
- Fixed male-first word order (men and women, husband and wife, boys and girls).
- Diminutive affixes: usherette, authoress, suffragette (historical term excepted).
- Adult women called "girls"; terms of endearment to non-intimates (dear, darling,
  love); dismissive "woman!".
- Exclusionary greetings (Dear Sir; Gentlemen-only salutations).
- Gendered metaphors (Mother Nature, Father Time) where a neutral alternative exists.

## Procedure

1. Tokenise text; scan for signals above per category.
2. For each hit, record: quote span, category, severity, rule reference,
   confidence, and whether context neutralises it (e.g. quoted historical source → G5).
3. Cross-check adjective hits with the swap test: "Would this adjective describe
   a different gender here?" If not → C1 hit.
4. Check statistics passages: if a gender-relevant phenomenon is reported without
   disaggregation AND data was provided in the task inputs, flag as C2 (medium)
   with a note; never invent numbers (core R4).
5. Output findings list ordered by severity.

## Severity defaults

| Finding | Default severity |
|---|---|
| Slur/dehumanising term | critical |
| Misgendering a named person | critical |
| Generic he/man; male-as-default compound | high |
| Occupation stereotype pronoun | high |
| Irrelevant gender modifier | medium |
| Word-order hierarchy, diminutive, endearment | medium |
| Gendered metaphor, borderline connotation | low |

## Guardrails

- G4: single occurrences of "he or she" are not violations; do not double-count
  one issue across categories — pick the dominant category.
- G5: quoted/historical material is flagged at most `low` with note "quote preserved".

## Uncertainty

Connotation judgements (e.g. "feisty") are context-dependent: mark confidence < 0.7
and let the human decide rather than auto-rewriting.

## Sources

- EIGE-2019 ch.4 (all three categories + examples), ch.5 worked tests (7+2 and
  9+2 finding counts), ch.6 checklist.
- EIGE-2024: language inclusivity scale examples; visuals guidance.
- IBEC-2015 §2.2 stereotype sentence pairs.
- INTELLECT-2022: self-check questions (have you used 'man'...; same information
  about different genders; occupational stereotypes).
