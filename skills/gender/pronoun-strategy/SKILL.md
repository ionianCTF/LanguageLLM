---
skill: gender.pronoun-strategy
title: Pronoun Strategy — Generic, Unknown, Entity & Stated Pronouns
version: 1.0.0
category: gender
requires: [core.inclusive-language-core]
triggers: [pronoun, he or she, singular they, ze hir, generic he, his or her,
  misgendering, pronouns]
sources: [EIGE-2019, CAPE-2023, UNW-EN, INTELLECT-2022, EIGE-2024]
---

## Purpose

Decide the correct pronoun treatment in every situation: unknown-gender referents,
generic human referents, organisations/entities, mixed groups, and known
individuals.

## When to use

Any sentence containing third-person pronouns whose antecedent's gender is
unknown, irrelevant, non-human, or stated by the person themselves.

## Rules

**R1 — Known individuals: stated pronouns win absolutely.**
Use the pronouns the person uses for themselves (or asked you to use). Never:
- put pronouns or names in quotation marks ("she" said) or otherwise invalidate them;
- use derogatory substitutes (he/she, (wo)man, it, shim, she-male);
- infer pronouns from appearance, voice, or name;
- disclose that someone is transgender without relevance (G11).
When writing about a transgender person, use nouns/pronouns consistent with their
gender identity regardless of sex assigned at birth.

**R2 — Unknown-gender individual (one person, specific role).** Preference order:
1. Rephrase to omit the pronoun ("The contractor should make his request" →
   "The contractor should make the request").
2. Singular they/their/them ("Each applicant must submit their resumé").
3. Definite/indefinite article ("A researcher was awarded a prize for the research paper").
4. Dual form his or her / her or his (fallback; alternate order across the document).
5. s/he, her/his slashes (forms/tables only, never narrative prose).
Neopronouns (ze/hir/hirs/hirself) only when established for the context/person —
never imposed as a default.

**R3 — Generic human referent ("any citizen", "the reader").** Same order as R2;
additionally prefer direct address ("you") in instructional writing, relative
"who" clauses, and "one" in formal registers (tone shift noted by IBEC).

**R4 — Plural conversion** when the sentence can become plural without changing
scope: "Every participant contributes his own ideas" → "All participants contribute
their own ideas". Check collective-vs-individual duty drift first (G1).

**R5 — Entities, organisations, objects: it.** "The bargaining agent called all
his members" → "The bargaining agent called all its members." Countries, ships,
machines take *it* ("The ship slipped its moorings"; "France and its citizens").
Never personify inanimate things with she/her except in clearly marked fiction,
and even there audit for stereotype (see multimodal-inclusion).

**R6 — Mixed groups:** they/them/their; never "the guys", never generic "he".
For Q&A addressing an audience, use role/appearance-neutral pointers only when
needed ("the person in the green shirt").

**R7 — Agreement discipline.** After singular they: "they are", "themselves",
"their". After entity-it: restart the pronoun chain if another subject intervenes;
when two subjects coexist, repeat the noun instead of any pronoun (CAPE):
"The Employer may authorize the employee to work the employee's normal work day."

**R8 — Pronoun fields.** In forms/registrations, label the field "Pronouns:"
(not "preferred pronouns"); make it optional/free-text; never require disclosure.

## Decision table

| Antecedent | Correct treatment |
|---|---|
| Named person, pronouns known | Their stated pronouns (always) |
| Named person, pronouns unknown | Ask (G8); else repeat name / singular they |
| Unspecified individual | Omit > singular they > article > dual form > slashes |
| Humanity in general | people/they; never generic he/man |
| Organisation, country, ship, object | it / its |
| Mixed group | they / everyone / all |
| User being instructed | you / your |

## Guardrails

- Never generate content that mocks or invalidates anyone's pronouns (G2, G12).
- In formal/legal registers apply formal-legal-texts rules first (noun repetition
  before pronoun tricks) — see divergence D1.

## Uncertainty

If pronouns cannot be verified for a named person, use the person's full name /
role noun until verification; log low confidence rather than guessing.

## Sources

- EIGE-2019 ch.4 ("Avoid gendered pronouns", ze/hir note) + ch.6 pronoun tables.
- CAPE-2023: singular they (since 1526, OED), entity-it, noun repetition.
- UNW-EN: strategy B options incl. singular-they caveat (divergence D1).
- INTELLECT-2022: LGBTQ+ section (scare-quote ban, they-solutions list).
- EIGE-2024: glossary (personal pronouns), event Q&A guidance.
