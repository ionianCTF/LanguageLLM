---
skill: gender.address-and-titles
title: Address, Titles & Naming Conventions
version: 1.0.0
category: gender
requires: [core.inclusive-language-core]
triggers: [Dear Sir, salutation, courtesy title, Ms Mrs Miss, letter greeting,
  addressee, naming convention, maiden name]
sources: [IBEC-2015, EIGE-2019, CAPE-2023, UNW-EN]
---

## Purpose

Ensure correspondence, documents, and references address people without assuming
or marketing gender, marital status, or hierarchy.

## When to use

Letters, emails, envelopes, form addressing, citations/references to people,
event programmes, certificates.

## Rules

**R1 — Salutation decision tree:**

| Situation | Use |
|---|---|
| Full name known | "Dear <given name(s)> <surname>," — no title (CAPE default) |
| Only initials known | "Dear J Thompson," — initials without any title (IBEC) |
| Role/group known | Dear colleague(s), Dear member(s), Dear applicant(s), Dear Panel |
| Recipient unknown | "Dear Sir or Madam," or reversed "Dear Madam or Sir," (alternate order across documents); or role-based "Dear Office Manager," / "To whom it may concern" |
| Group, mixed genders | Never "Dear Sirs". Omit titles; use collective salutation |
| Group, same gender (only if titles unavoidable) | Mses. / Messrs. (IBEC fallback) |

**R2 — Courtesy titles:**
- Omit in salutations and body text by default (CAPE). Permitted exceptions:
  gender-neutral honorifics Dr., Prof., and equivalent earned titles.
- If a title is required and preference unknown → **Ms.** Never Miss/Mrs. by
  inference. Honour a woman's stated Miss/Mrs (G2).
- Marital status is irrelevant to professional matters (UNW-EN).

**R3 — Naming conventions:**
- Same referencing style for all genders: if you surname a man, surname the woman
  ("Yang and his research assistant Smith", not "Holly").
- Couples: name both individuals ("Jessica Farrar and Alistair Farrar"), not
  "Mr and Mrs Alistair Farrar".
- Replace "maiden name"/"married name" fields with "last name"/"previous name".
- Do not define women by relation to men ("attendees and their wives" →
  "attendees and their spouses/partners/guests").

**R4 — Forms and registration:**
- Provide a Pronouns field (optional, free-text), labelled "Pronouns:".
- Include non-binary option alongside male/female wherever gender is collected;
  never label it "Other".
- Collect dietary/accessibility needs explicitly (see multimodal-inclusion for events).

**R5 — Audience address in speeches/documents:** "Welcome everyone/ladies,
gentlemen, and everyone" → prefer "everyone", "colleagues", "delegates",
"members" (IBEC); avoid habitual "ladies and gentlemen" when a functional
collective exists.

## Worked micro-examples

| Biased | Inclusive |
|---|---|
| Dear Mrs. Chris Eilson | Dear Chris Eilson |
| Dear Sirs | Dear colleagues |
| To whom it may concern (when role knowable) | Dear Office Manager |
| Ms Alice McKinnon, CL Carter, Mr Carl Ellis, Miss Regina Rogers (group letter) | Dear Alice McKinnon, Chris Carter, Carl Ellis, Regina Rogers |

## Guardrails

- G2: a person's stated title/pronouns override every default here.
- Divergence D4 applies: omit-by-default wins unless the client style guide says otherwise.

## Uncertainty

If addressee identity is genuinely unknowable, "Dear Sir or Madam" remains
acceptable; log `low` note suggesting role-based alternative when available.

## Sources

- IBEC-2015 §2.5 correspondence table; §2.1 addresses.
- CAPE-2023: omit courtesy titles; "Dear"+name pattern.
- UNW-EN: titles section (Ms. default; couple naming).
- EIGE-2019 ch.4: greetings; naming conventions; maiden-name tip.
