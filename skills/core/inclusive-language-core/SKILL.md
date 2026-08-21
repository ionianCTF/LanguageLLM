---
skill: core.inclusive-language-core
title: Inclusive Language Core — Definitions, Principles & Routing
version: 1.0.0
category: core
requires: []
triggers: [inclusive language, gender-sensitive, gender-neutral, gender-inclusive,
  inclusive writing, non-sexist language, bias-free language]
sources: [EIGE-2019, EIGE-2024, UNW-EN]
---

## Purpose

Entry point for every inclusive-language task. Establishes shared definitions, the
inclusivity scale, the three operating principles, and routes work to the correct
specialised skill.

## When to use

Load this skill at the start of any task that involves producing, transforming, or
auditing natural-language content for inclusivity. After reading it, dispatch to
Tier 2–5 skills per the routing table below.

## Rules

**R1 — Know the scale.** Classify every usage against the language inclusivity
scale before acting:

| Position on scale | Label | Disposition |
|---|---|---|
| Worst | Sexist / gender-discriminatory / gender-biased language | Avoid always |
| Middle | Gender-neutral / gender-blind language | Consider carefully — acceptable when gender is irrelevant; risky when it hides real differences |
| Best | Gender-inclusive (formerly "gender-sensitive") language | Favour |

Definitions:
- **Sexist language** — intentionally derogatory/discriminatory toward a gender.
- **Gender-biased language** — implicitly or explicitly favours one gender; a form
  of gender-discriminatory language even without sexist intent (e.g. generic "he").
- **Gender-discriminatory language** — words/phrases fostering stereotypes or
  demeaning/ignoring a gender (e.g. "Ambassadors and their wives are invited").
- **Gender-neutral language** — not gender-specific; refers to people in general
  ("People do not fully appreciate the impact they have on the environment.").
- **Gender-sensitive language** — gender equality made manifest through language;
  women, men, and those outside the binary addressed as persons of equal value,
  dignity, integrity, and respect.
- **Gender-inclusive language** — speaking/writing that does not exclude or
  discriminate against a particular sex, gender, or gender identity and does not
  perpetuate sexism or stereotypes. The current standard target (EIGE-2024).

**R2 — Apply the three principles** (identical across EIGE-2019 and EIGE-2024):
1. Recognise and challenge gender stereotypes.
2. Maintain inclusivity — ensure visibility of women, men, girls, boys, and
   non-binary people in all their diverse situations; avoid omission/invisibility.
3. Uphold dignity, respect, and equal treatment; avoid trivialisation and subordination.

**R3 — Decide whether gender should be visible at all.** Ask, in order:
1. Does mentioning gender shed light on key aspects of the issue?
   Yes → make gender visible (inclusive form). No → neutral form.
2. Are you referring to people in general or a specific group? General → neutral
   may be acceptable; specific group → gender is usually relevant.
3. Is explicit non-binary inclusion the goal? → neutral forms (singular "they") or
   explicitly inclusive phrasing.
4. Policy/legal/official texts → default to making gender visible; there is almost
   always a gender dimension to public policy.

**R4 — Research, don't assume.** If introducing a gender dimension (e.g. splitting
a statistic by gender), the split must reflect actual data supplied in the task —
never invented values. If no data exists, keep the neutral form and note why.

**R5 — Do not conflate transgender with non-binary.** Many transgender people
identify with one binary gender. Use the individual's actual identity.

**R6 — Intersectionality.** Gender interacts with age, ethnicity, migrant
background, disability, and sexual orientation, producing distinct experiences
(e.g. older migrant women disproportionately affected by energy poverty). When a
text concerns a group, consider whether an intersectional dimension is being
erased by a single-axis description.

## Routing table

After classification, load:

| Situation | Skill |
|---|---|
| Rewriting gendered sentences | `gender.gender-inclusive-rewriting` |
| Pronoun choices (generic he, unknown gender, entities, individuals) | `gender.pronoun-strategy` |
| Detecting stereotypes, invisibility, trivialisation | `gender.stereotype-detection` |
| Salutations, courtesy titles, naming conventions | `gender.address-and-titles` |
| Contracts, legislation, collective agreements, official policies | `gender.formal-legal-texts` |
| Disability / ethnicity / LGBTQIA+ / age / class / religion terms | corresponding `identity-domains.*` skill |
| Images, video, voice-over, social media, events | `communication.multimodal-inclusion` |
| Generating new content or prompts for AI tools | `communication.ai-content-generation` |
| Full-document review job | `workflows.document-audit` |

## Guardrails

- Never "correct" a person's self-description (GUARDRAILS G2).
- Gender-neutral is a legitimate destination, not a failure state — but flag when
  neutrality hides a material gender dimension (R3.4, D3 resolution in SOURCES.md).

## Uncertainty

If it is unclear whether gender is relevant to the content, prefer the neutral
form, log a low-confidence entry, and surface the question to the requester.

## Sources

- EIGE-2019: ch.2 (terms, inclusivity scale, principles, choosing whether to mention gender), ch.4 (false generics), ch.6 (checklist).
- EIGE-2024: Introduction, "Different approaches to language", glossary.
- UNW-EN: "Our Goal" section.
