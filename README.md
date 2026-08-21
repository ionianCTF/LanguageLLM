# Inclusive Language Skills Library

**A structured repository of SKILLS that teach LLM agents how to use, detect, and transform inclusive language — built from six authoritative institutional guidelines.**

This repository packages inclusive-language expertise into machine-consumable skill files with explicit guardrails, so that any LLM agent can produce, rewrite, or audit text that respects gender, disability, ethnicity, LGBTQIA+ identity, age, socioeconomic class, and religion — without changing meaning, without over-correcting, and with full traceability back to its institutional sources.

---

## Table of contents

1. [Why this exists](#1-why-this-exists)
2. [Source corpus](#2-source-corpus)
3. [Repository architecture](#3-repository-architecture)
4. [Skill catalogue](#4-skill-catalogue)
5. [How an agent uses this library](#5-how-an-agent-uses-this-library)
6. [Guardrails](#6-guardrails)
7. [Handling contradictions between sources](#7-handling-contradictions-between-sources)
8. [Severity model & change log](#8-severity-model--change-log)
9. [Design principles](#9-design-principles)
10. [Extending the library](#10-extending-the-library)
11. [Limitations & ethical notes](#11-limitations--ethical-notes)
12. [Attribution](#12-attribution)

---

## 1. Why this exists

Language shapes attitudes, behaviours, and social norms; it also reflects them.
Institutions from the UN to the EU have codified how to write without excluding or
demeaning people — but that knowledge lives in human-oriented PDF guides. LLM
agents generate enormous volumes of text and inherit exactly the biases these
guides combat (generic masculines, occupational stereotypes, deficit framing,
outdated terminology).

This library converts those guides into **deterministic, rule-based skill files**
that an agent can load, follow, and be audited against. The goal is not to make
agents preachy — it is to make them *precise*: flag real issues, fix them while
preserving meaning exactly, explain every change, and know when to ask a human.

## 2. Source corpus

All skills derive from the public guides in [`material/`](material/). Full
traceability (which document backs which rule) is in
[`skills/_meta/SOURCES.md`](skills/_meta/SOURCES.md).

| Document | Publisher / Year | Pages | Focus |
|---|---|---|---|
| Toolkit on Gender-sensitive Communication | EIGE (EU), 2019 | 65 | Foundational: inclusivity scale, three categories of discriminatory language, solutions tables, checklists, worked test examples |
| Words Matter — Supporting Gender Equality through Language and Communication | EIGE (EU), 2024 | 32 | Gender-inclusive approach, intersectionality, communication formats (visuals, video, social media, AI prompts, voice-overs, events), glossary |
| Guidelines on Gender-Inclusive Language (English) | UN Women | ~2016+ | 7 | Transformation strategies A/B/C, checklist, lexicon pointers |
| Inclusive Writing Guide (1st ed.) | CAPE (Canada), 2023 | 7 | Mechanical rewriting techniques, singular they, legal-text meaning preservation, forms |
| Guidelines on Gender-Neutral Language | IBEC, 2015 | 8 | Workplace language, titles/labels/biased terms, correspondence rules |
| Inclusive Language Guide | Intellect Books, 2022 | 19 | Age, class, disability, ethnicity, LGBTQ+, religion; editorial guardrails |

## 3. Repository architecture

```
LanguageLLM/
├── README.md                        ← you are here
├── material/                        ← source PDFs (read-only corpus)
├── guardrails/                      ← operational guardrail layer (L1–L3, checklists)
└── skills/
    ├── _meta/
    │   ├── ARCHITECTURE.md          ← loading model, routing, file conventions
    │   ├── GUARDRAILS.md            ← universal guardrails G1–G15 (bind all skills)
    │   └── SOURCES.md               ← traceability matrix + divergence register
    ├── core/                        ← TIER 1 · always load first
    │   └── inclusive-language-core/SKILL.md
    ├── gender/                      ← TIER 2 · gender transformation skills
    │   ├── gender-inclusive-rewriting/
    │   │   ├── SKILL.md
    │   │   └── references/substitution-tables.md
    │   ├── pronoun-strategy/SKILL.md
    │   ├── stereotype-detection/SKILL.md
    │   ├── address-and-titles/SKILL.md
    │   └── formal-legal-texts/SKILL.md
    ├── identity-domains/            ← TIER 3 · non-gender domains
    │   ├── disability-language/SKILL.md
    │   ├── ethnicity-language/SKILL.md
    │   ├── lgbtqia-language/SKILL.md
    │   ├── age-language/SKILL.md
    │   ├── class-language/SKILL.md
    │   └── religion-language/SKILL.md
    ├── communication/               ← TIER 4 · multimodal & generative contexts
    │   ├── multimodal-inclusion/SKILL.md
    │   └── ai-content-generation/SKILL.md
    └── workflows/                   ← TIER 5 · orchestration pipelines
        └── document-audit/SKILL.md
```

**Tiered progressive disclosure:** agents load only what a task needs — one
sentence rewrite needs Tiers 0–1 (+2 if gendered); a full policy audit loads Tier
5, which orchestrates everything else on demand. This keeps context windows small
and routing deterministic.

Every `SKILL.md` follows one uniform skeleton (YAML frontmatter → Purpose → When
to use → Rules → Procedure → Reference tables → Guardrails → Uncertainty →
Sources) so agents can parse any skill without special-casing. The convention is
specified in `ARCHITECTURE.md §4`.

## 4. Skill catalogue

| # | Skill ID | Purpose | Primary source |
|---|----------|---------|----------------|
| 0 | `_meta/GUARDRAILS` | Universal constraints binding every skill | corpus-wide |
| 0b | `guardrails/*` | Operational guardrail layer: 32 domain rules from all skills, register matrix, pre/post checklists, violation taxonomy | corpus-wide |
| 1 | `core.inclusive-language-core` | Definitions, inclusivity scale, 3 principles, when-to-show-gender decision, routing table | EIGE 2019/2024 |
| 2 | `gender.gender-inclusive-rewriting` | Strategy ladder (neutral expression → restructure → dual forms) + full substitution tables | UN Women, EIGE, CAPE, IBEC |
| 3 | `gender.pronoun-strategy` | Pronoun decisions: stated pronouns, singular they, entities=it, agreement discipline | EIGE, CAPE, Intellect |
| 4 | `gender.stereotype-detection` | Detect & classify: stereotypes / invisibility-omission / subordination-trivialisation, with severities | EIGE 2019 ch.4–5 |
| 5 | `gender.address-and-titles` | Salutations, Ms./Dr., couple naming, form fields, "Dear Sirs" bans | IBEC, CAPE, UN Women |
| 6 | `gender.formal-legal-texts` | Meaning-preserving inclusion for contracts/legislation/CBAs; interpretive-clause handling | CAPE, EIGE |
| 7 | `identity-domains.disability-language` | Social model, person-first defaults, D/deaf nuance, full term table | Intellect |
| 8 | `identity-domains.ethnicity-language` | Specificity, capitalisation, Indigenous phrasing, slavery language, slur handling | Intellect |
| 9 | `identity-domains.lgbtqia-language` | Current terminology, assigned-at-birth, pronoun discipline, reclaimed-term rules | Intellect, UN Women |
| 10 | `identity-domains.age-language` | Precise age descriptors, no infantilising/stereotyped framing | Intellect |
| 11 | `identity-domains.class-language` | Deficit-framing removal, circumstance-not-identity descriptions | Intellect |
| 12 | `identity-domains.religion-language` | Conflation avoidance, BCE/CE, deity-language conventions, dysphemism ban | Intellect |
| 13 | `communication.multimodal-inclusion` | Images, emoji, colour, video, voice-over, hashtags, events, registration forms | EIGE 2024/2019 |
| 14 | `communication.ai-content-generation` | Inclusive prompt engineering + self-audit of generated output + synthetic-media boundaries | EIGE 2024 |
| 15 | `workflows.document-audit` | Six-phase audit pipeline → structured findings report → verified revision | EIGE ch.5–6, UN Women |

## 5. How an agent uses this library

```
Request ──► Classify task (generate | transform | audit | question)
        ──► Load GUARDRAILS.md (always) + core skill (always)
        ──► Scan for domain signals (gender? disability? ethnicity? …)
        ──► Dispatch to matching skills by frontmatter triggers
        ──► Apply skill rules + guardrails
        ──► Emit result + structured change log
```

Example dispatches:

- *"Rewrite: 'Each applicant must submit his resumé.'"*
  → core + `pronoun-strategy` → "Each applicant must submit their resumé."
  Change log: category `invisibility-omission`, severity `high`, confidence 0.95.
- *"Check our employment contract clause for inclusive language."*
  → core + `formal-legal-texts` (+ audit workflow if long) → noun-repetition-first
  strategy, scope-preservation verification, human-review flags where interpretive
  risk exists.
- *"Generate a launch post for our parental leave policy."*
  → core + `ai-content-generation` (+ `multimodal-inclusion` if visuals) →
  addresses all parents/family compositions, no "mums" default, self-audited draft.

Full routing logic and precedence rules: `ARCHITECTURE.md §3`.

## 6. Guardrails

Fifteen universal guardrails (`_meta/GUARDRAILS.md`) bind every skill; the
[`guardrails/`](guardrails/) folder operationalises them (domain rules, register
matrix, checklists, violation taxonomy). Highlights:

| ID | Guardrail | One-line rule |
|----|-----------|---------------|
| G1 | Meaning preservation | Never alter meaning, scope, application, or legal effect — supreme rule |
| G2 | Self-identification primacy | A person's stated name/pronouns/title override every default |
| G3 | Relevance rule | Don't mention protected characteristics unless relevant |
| G4 | No over-correction | Fix genuine issues only; readability is part of inclusivity |
| G5 | Quote integrity | Verbatim quotes preserved; bias in quotes marked, never silently modernised |
| G6 | Specificity over umbrellas | Prefer precise terms; umbrella initialisms are fallbacks |
| G7 | Person-first vs identity-first | Follow community/individual preference; don't police |
| G8 | Uncertainty protocol | Ask → else neutral default → else flag low confidence; never guess identities |
| G9 | Register awareness | Legal ≠ informal; detect register before choosing strategies |
| G10 | Non-judgemental comparatives | Objective comparisons; no deficit framing |
| G11 | Privacy & outing | Never expose gender history, status, or medical facts irrelevantly |
| G12 | Slur handling | Slurs exist only as avoid-table patterns; never generated as vocabulary |
| G13 | Language-scope honesty | Corpus is English-specific; say so outside English |
| G14 | Evolving terminology | Prefer newest consensus; date-stamp uncertain claims |
| G15 | Explain, don't just edit | Every non-trivial change ships rationale + confidence |

Each skill adds local guardrails that extend — never override — these.

## 7. Handling contradictions between sources

The six guides do not fully agree (they span 2015–2024). Rather than hide this,
the library records five divergences in `SOURCES.md §3` and resolves them by an
explicit precedence chain:

**individual's stated identity > client style guide > universal guardrails > skill rules > most recent source**

Documented divergences include: singular "they" in formal texts (UN Women
restricts; CAPE/EIGE-2024 embrace), dual-form pronouns ("he or she") as fallback
vs default, gender-sensitive vs gender-inclusive as target state, courtesy-title
omission vs retention, and mixed-group "guys". Agents apply the resolution and
note it in the change log when it materially affects output.

## 8. Severity model & change log

All findings use one four-level scale:

| Severity | Meaning |
|----------|---------|
| `critical` | Demeaning/dehumanising language; misgendering a named person |
| `high` | Systematic exclusion (generic masculine, male-as-default) |
| `medium` | Trivialisation, unnecessary gendering, non-preferred terms |
| `low` | Style improvements; borderline cases for human decision |

Every transformation can emit a structured entry:

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

This makes agent behaviour testable: regression suites can assert on categories,
severities, and exact revisions.

## 9. Design principles

1. **Machine-first drafting.** Rules are imperative and checkable ("Replace X
   with Y"), not advisory prose — the reader is an agent.
2. **Progressive disclosure.** Six tiers; load only what the task needs.
3. **Deterministic ladders.** Where multiple valid rewrites exist, skills specify
   a preference order instead of leaving the choice to model mood.
4. **Traceability.** Every rule cites its source institution; SOURCES.md maps the
   full matrix.
5. **Honest disagreement.** Source conflicts are registered and resolved by
   published precedence, not silently averaged.
6. **Meaning supremacy.** Especially in legal registers, a failed meaning-check
   vetoes any inclusivity gain.
7. **Anti-overcorrection.** Detection includes context-neutralisation checks so
   agents don't flag respectful factual usage.
8. **Auditability.** Uniform file schema + severity scale + JSON change logs.

## 10. Extending the library

To add a new skill (full procedure in `ARCHITECTURE.md §6`):

1. Drop the source PDF into `material/`.
2. Create `skills/<tier>/<skill-name>/SKILL.md` using the §4 skeleton.
3. Register the source and traceability in `_meta/SOURCES.md`; record any
   conflicts with existing skills in the divergence register.
4. Add disjoint triggers; update the catalogue table above.
5. Bump versions of any skill whose rules you touch (semver).

Slur-containing example text belongs only inside `avoid` columns of detection
tables — never presented as usable vocabulary.

## 11. Limitations & ethical notes

- **English-only corpus.** Grammar-driven strategies don't transfer across
  languages (G13). UN Women and CAPE publish French/Spanish equivalents worth
  integrating as separate tiers.
- **Time-stamped knowledge.** Terminology evolves quickly (sources span
  2015–2024). Re-validate against newer editions periodically; community
  self-description always wins.
- **Not legal advice.** The formal-legal-texts skill flags interpretive risk;
  it does not clear contractual language.
- **Coverage gaps.** Intersex topics have terminological but not deep coverage in
  the corpus; specialised community style guides should supplement.
- **Inclusion ≠ box-ticking.** Representation guidance (multimodal skill)
  explicitly warns against tokenism; diversity must reflect the actual audience
  and context.

## 12. Attribution

Derived from public guidance documents:
European Institute for Gender Equality (2019 Toolkit; 2024 Words Matter — CC-BY
4.0), UN Women (Gender-Inclusive Language Guidelines), Canadian Association of
Professional Employees (Inclusive Writing Guide, 2023), IBEC (Guidelines on
Gender-Neutral Language, 2015), and Intellect Books (Inclusive Language Guide,
2022). Original PDFs live unmodified in [`material/`](material/); rule-level
citations appear in each SKILL.md's Sources section.
