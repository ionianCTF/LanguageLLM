# Source Corpus & Traceability

All skills in this library are derived from the six public institutional guides in
`material/`. This file maps every source to the skills that consume it, and records
known divergences between sources with their resolution.

---

## 1. Source register

| Key | Document | Publisher | Year | Pages | Scope |
|-----|----------|-----------|------|-------|-------|
| `EIGE-2019` | Toolkit on Gender-sensitive Communication (file: `20193925_mh0119609enn_pdf.pdf`) | European Institute for Gender Equality (EU) | 2019 | 65 | Gender-sensitive language: principles, 3 categories of discriminatory language, solutions tables, checklists, worked test examples |
| `EIGE-2024` | Words Matter — Supporting Gender Equality through Language and Communication (file: `words-matter-...pdf`) | EIGE | 2024 | 32 | Gender-inclusive approach, intersectionality, communication messages & formats (visuals, video, social media, AI prompts, voice-overs, events), glossary |
| `UNW-EN` | Guidelines on Gender-Inclusive Language (English) (file: `guidelines-on-gender-inclusive-language-en.pdf`) | UN Women | n.d. (~2016+) | 7 | Transformation strategies A/B/C, checklist, lexicon pointers |
| `CAPE-2023` | Inclusive Writing Guide, 1st ed. (file: `CAPE_Inclusive Writing Guide_...pdf`) | Canadian Association of Professional Employees | 2023 | 7 | Mechanical rewriting techniques, singular they, legal-text caution, forms |
| `IBEC-2015` | Guidelines on Gender-Neutral Language (file: `IBEC-Guidelines-...pdf`) | IBEC (HR Unit) | 2015 | 8 | Workplace language, titles/labels/biased terms, correspondence rules |
| `INTELLECT-2022` | Inclusive Language Guide (file: `Inclusive-Language-Guide-Sept-2022.pdf`) | Intellect Books | 2022 | 19 | Age, class, disability, ethnicity, LGBTQ+ & gender equality, religion; editorial guardrails |

Note: `EIGE-2024` explicitly supersedes and builds on `EIGE-2019` ("developed from
the EIGE Toolkit ... published in 2019"), shifting the recommended target from
*gender-sensitive* to *gender-inclusive* language while keeping the same three
principles. Both are retained because `EIGE-2019` contains the deepest operational
detail (tables, checklists, worked examples).

---

## 2. Traceability matrix

| Skill | Primary sources | Supporting sources |
|-------|----------------|--------------------|
| `core.inclusive-language-core` | EIGE-2019 ch.2, EIGE-2024 §"Different approaches" | UNW-EN intro |
| `gender.gender-inclusive-rewriting` | UNW-EN (strategies A/B/C) | EIGE-2019 ch.4+6, CAPE-2023, IBEC-2015, EIGE-2024 |
| `gender.gender-inclusive-rewriting/references/substitution-tables.md` | EIGE-2019 ch.6 | UNW-EN, CAPE-2023, IBEC-2015 |
| `gender.pronoun-strategy` | EIGE-2019 ch.4+6 (pronoun tables), CAPE-2023 | UNW-EN, INTELLECT-2022 (LGBTQ+ section), EIGE-2024 glossary |
| `gender.stereotype-detection` | EIGE-2019 ch.4 (three categories) | EIGE-2024, IBEC-2015 §2.2, INTELLECT-2022 (check questions) |
| `gender.address-and-titles` | IBEC-2015 §2.1+2.5, EIGE-2019 (naming conventions, greetings) | UNW-EN (titles), CAPE-2023 (courtesy titles) |
| `gender.formal-legal-texts` | CAPE-2023 (all sections incl. "Other considerations") | EIGE-2019 (legal text example), UNW-EN |
| `identity-domains.disability-language` | INTELLECT-2022 (Disability) | EIGE-2024 (intersectionality framing) |
| `identity-domains.ethnicity-language` | INTELLECT-2022 (Ethnicity) | EIGE-2024 (intersectionality framing) |
| `identity-domains.lgbtqia-language` | INTELLECT-2022 (LGBTQ+ and Gender Equality) | EIGE-2024 glossary, UNW-EN (gender identity) |
| `identity-domains.age-language` | INTELLECT-2022 (Age) | EIGE-2024 (intersectionality framing) |
| `identity-domains.class-language` | INTELLECT-2022 (Class) | EIGE-2024 (intersectionality framing) |
| `identity-domains.religion-language` | INTELLECT-2022 (Religion) | — |
| `communication.multimodal-inclusion` | EIGE-2024 (Communication formats) | EIGE-2019 (images, emoji, colour) |
| `communication.ai-content-generation` | EIGE-2024 (AI prompt example, AI risks) | EIGE-2019 (emoji/virtual assistant notes) |
| `workflows.document-audit` | EIGE-2019 ch.5–6 (test examples + checklist) | UNW-EN checklist, all above |

---

## 3. Divergence register

Where sources disagree, agents follow the precedence chain in
`ARCHITECTURE.md §3` (individual > client style guide > skill rules > guardrails >
recency). Known divergences:

### D1 — Singular "they" in formal texts
- **UNW-EN:** singular they is "more recent and not widely accepted, and it should
  not be adopted in formal texts."
- **CAPE-2023:** singular they/their/them is "the preferred alternative," including
  in collective-agreement contexts.
- **INTELLECT-2022 / EIGE-2024:** recommend singular they as a standard solution.
- **Resolution:** default to singular they (majority + most recent positions);
  in legal/contractual registers, prefer noun repetition first (G1), then apply the
  governing style guide's rule. State which convention was applied.

### D2 — Dual-form pronouns ("he or she")
- **UNW-EN / EIGE-2019:** acceptable strategy; EIGE-2019 even recommends reversing
  to "she or he"/"her/his" in legislation to counter historical male-first drafting.
- **CAPE-2023 / INTELLECT-2022:** treat as stylistically heavy; prefer restructure.
- **Resolution:** dual forms are a fallback, not a default; use reversed order
  (she/he) only where deliberately countering male-as-default tradition, per task intent.

### D3 — Target state of language
- **EIGE-2019:** favour *gender-sensitive*; gender-neutral acceptable in some contexts.
- **EIGE-2024:** adopt *gender-inclusive* as the standard approach.
- **Resolution:** aim for gender-inclusive output; use gender-neutral phrasing when
  gender is irrelevant or when non-binary inclusion is the priority; make gender
  visible when the subject matter has a genuine gender dimension (e.g. statistics,
  policy impacts).

### D4 — Courtesy titles
- **IBEC-2015:** retains Mses./Messrs. for same-gender groups; "Dear Sir or Madam"
  accepted when recipient unknown.
- **CAPE-2023 / UNW-EN:** omit courtesy titles entirely; "Dear" + given name +
  surname; role-based salutations preferred.
- **Resolution:** omit titles by default; fall back to Ms. (never Miss/Mrs.) when a
  title is required and preference unknown; honour an individual's stated title (G2).

### D5 — "Guys"
- **IBEC-2015:** lists under biased terms contextually.
- **CAPE-2023:** "hey, guys!" → "hey, everyone!".
- **EIGE-2024:** removes "guys" from a social post as a stereotype fix.
- **Resolution:** treat mixed-group "guys" as medium-severity; replace with
  everyone/all/team/people.

---

## 4. Corpus-level limitations

- All six guides are **English-language** guidance (G13).
- Publication years span 2015–2024; terminology evolves (G14). The library should
  be re-validated against newer editions of these guides periodically.
- None of the sources provides intersex-specific depth beyond terminology basics;
  agents should defer to specialised intersex organisations' style guidance when
  deep coverage is required.
- Non-binary pronoun inventories differ across sources (`ze/hir` in EIGE-2019;
  singular they elsewhere). Skills present neopronouns as context-dependent options,
  never defaults.
