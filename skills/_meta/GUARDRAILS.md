# Universal Guardrails

These guardrails bind **every** skill in this library. No skill-specific rule may
override them. If a client instruction conflicts with a guardrail, surface the
conflict explicitly instead of silently complying or refusing.

---

## G1 — Meaning preservation (supreme rule)

A transformation must never alter the meaning, application, scope, value, or legal
effect of the source text. Inclusive rewording that changes who or what a clause
covers is a failed transformation.

- In contracts, collective agreements, legislation, and policies: prefer repeating
  the noun over pronoun substitution when ambiguity could arise; treat pluralisation
  with caution (it can convert an individual duty into a collective one).
- See `gender/formal-legal-texts` for the full procedure.

## G2 — Self-identification primacy

If a person's stated name, pronouns, title, or self-description is known, it
overrides every default rule in this library. Never second-guess, correct, or
debate a person's identity. Never refer to a person's pronouns or name in scare
quotes or in any way that invalidates them.

## G3 — Relevance rule

Do not mention a protected characteristic (gender, ethnicity, disability, religion,
age, sexuality, class) unless it is genuinely relevant to the point being made.
When it is relevant, be as specific as the context allows (e.g. "transgender woman",
not "LGBT"; "people from the Chinese ethnic group", not "Chinese people" when
ethnicity, not nationality, is meant).

## G4 — No over-correction

Flag and fix genuine issues; do not manufacture them. Concretely:

- Do not mechanically replace every "he/she" pair with slashes throughout a long
  text — readability is part of inclusivity (UN Women: dual forms become
  stylistically heavy when repeated).
- Do not rewrite quotes, historical documents, or titles of works (apply G5 instead).
- Do not flag a term as biased when it is used factually and respectfully in
  context (e.g. "enslaved people" in a history text is correct; "the blind" as a
  collective noun is the issue, not every instance of the word "blind").

## G5 — Quote and citation integrity

Verbatim quotations, legislation names, book/article titles, and direct speech are
preserved exactly. If quoted material contains biased or offensive language:
retain it inside quotation marks, minimise repetition, and — where the surrounding
text discusses it — make the bias explicit ("the term used in the source, now
considered derogatory"). Never silently modernise a quote.

## G6 — Specificity over umbrella terms

Prefer the most precise respectful term over broad labels. Umbrella initialisms
(LGBTQIA+, BAME, BIPOC) are fallbacks for genuinely mixed references, not
defaults. Homogenising distinct groups is a defect, not a convenience.

## G7 — Person-first vs identity-first: follow preference

Default to person-first phrasing ("person with epilepsy"), except where a community
predominantly prefers identity-first ("disabled person", "Deaf person" for cultural
membership) or where the individual's stated preference is known. Both models are
legitimate; do not police an author's coherent choice.

## G8 — Uncertainty protocol

When the respectful choice depends on unknown facts (a person's pronouns, preferred
title, tribal/national affiliation):

1. Ask the user or consult the subject, if possible.
2. Otherwise default to the neutral option (singular "they", omit the title,
   use the broader respectful category).
3. Mark the output point with low confidence in the change log rather than guessing.

## G9 — Register awareness

Strategies differ by register. Formal/legal texts tolerate fewer strategies than
informal prose (e.g. some institutional guides restrict singular "they" in formal
texts; newer guides accept it). Detect register before choosing a strategy and
state the assumption. When a governing style guide exists, it wins (precedence §3
of ARCHITECTURE.md).

## G10 — Non-judgemental comparatives

When comparing groups or individuals, avoid evaluative wording ("better", "best")
where objective comparatives work ("more likely to", "less access to", "as likely
to"). Deficit framing ("poorly educated", "high-school dropouts") is replaced by
neutral description of circumstance ("people without a diploma").

## G11 — Privacy and outing

Never disclose or imply a person's gender history, medical status, immigration
status, or other sensitive characteristic when it is irrelevant to the content.
Do not infer identity from appearance, voice, or name.

## G12 — Slur handling

Slurs and dehumanising terms are never generated as usable vocabulary. They appear
in skill tables only as `avoid` patterns required for detection. If a task requires
discussing such a term (moderation, education, historical analysis), name it
minimally, inside quotation marks, with clear critical framing.

## G13 — Language scope honesty

The source corpus is English-specific. Grammar-driven strategies (gendered noun
endings, agreement) do not transfer to other languages. When operating in another
language, state that these skills cover principles only, and recommend the
corresponding language-specific guide (e.g. UN Women publishes French/Spanish
versions; CAPE publishes a French guide).

## G14 — Evolving terminology

Inclusive language is time-stamped knowledge. Terms accepted in older sources may
be superseded (e.g. "preferred pronouns" → "pronouns"; "Sexual Reassignment
Surgery" → "Gender Confirmation Surgery"). Prefer the most recent consensus in the
source corpus, date-stamp uncertain claims, and treat community self-description
as the tiebreaker.

## G15 — Explain, don't just edit

Every non-trivial change ships with: category, severity, one-line rationale, and
(when confidence < 0.9) an explicit uncertainty note. Audits report findings; they
do not lecture. Tone of explanations: neutral, professional, zero moralising.

---

## Enforcement checklist (run before finalising any output)

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
