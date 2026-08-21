# Skill Library Architecture

This document defines how the skill library is organised, how an LLM agent should
discover, load, and apply skills, and the conventions every skill file must follow.

---

## 1. Repository layout

```
LanguageLLM/
├── README.md                          # Project overview and skill catalogue
├── material/                          # Source PDFs (read-only reference corpus)
├── guardrails/                        # Operational guardrail layer (L1–L3): guardrails/ARCHITECTURE.md
├── skills/
│   ├── _meta/
│   │   ├── ARCHITECTURE.md            # This file — loading model, routing, conventions
│   │   ├── GUARDRAILS.md              # Universal guardrails (bind ALL skills)
│   │   └── SOURCES.md                 # Source-to-skill traceability + divergence register
│   ├── core/
│   │   └── inclusive-language-core/   # TIER 1 — always load first
│   │       └── SKILL.md
│   ├── gender/                        # TIER 2 — gender-focused transformation skills
│   │   ├── gender-inclusive-rewriting/
│   │   │   ├── SKILL.md
│   │   │   └── references/substitution-tables.md
│   │   ├── pronoun-strategy/
│   │   │   └── SKILL.md
│   │   ├── stereotype-detection/
│   │   │   └── SKILL.md
│   │   ├── address-and-titles/
│   │   │   └── SKILL.md
│   │   └── formal-legal-texts/
│   │       └── SKILL.md
│   ├── identity-domains/              # TIER 3 — non-gender identity domains
│   │   ├── disability-language/SKILL.md
│   │   ├── ethnicity-language/SKILL.md
│   │   ├── lgbtqia-language/SKILL.md
│   │   ├── age-language/SKILL.md
│   │   ├── class-language/SKILL.md
│   │   └── religion-language/SKILL.md
│   ├── communication/                 # TIER 4 — multimodal & generative contexts
│   │   ├── multimodal-inclusion/SKILL.md
│   │   └── ai-content-generation/SKILL.md
│   └── workflows/                     # TIER 5 — orchestration pipelines
│       └── document-audit/SKILL.md
```

---

## 2. Tier model (progressive disclosure)

Skills are layered so an agent loads only what a task requires. This keeps context
small and routing deterministic.

| Tier | Scope | Loading rule |
|------|-------|--------------|
| **0** | `_meta/GUARDRAILS.md` + `guardrails/` | Always in effect. Loaded once per session; never skipped. `guardrails/` is the operational layer: domain rules (L1), register matrix (L2), pre/post checklists, violation taxonomy. |
| **1** | `core/inclusive-language-core` | Load at the start of any inclusive-language task. Provides definitions, the inclusivity scale, principles, and the routing table below. |
| **2** | `gender/*` | Load when the task involves gendered language, pronouns, titles, or gendered documents. |
| **3** | `identity-domains/*` | Load only for the specific domain(s) present in the text (disability, ethnicity, LGBTQIA+, age, class, religion). |
| **4** | `communication/*` | Load when output is multimodal (images/video/audio/events/social) or AI-generated content. |
| **5** | `workflows/document-audit` | Load for full-document review jobs. It orchestrates Tiers 1–4 internally. |

**Rule:** never load more than one tier ahead of what the task needs. A quick
rewrite of one sentence needs Tier 0 + 1 (+2 if gendered). A full policy audit
needs Tier 5, which pulls in the rest on demand.

---

## 3. Routing / dispatch logic

When a user request arrives, resolve in this order:

1. **Classify the task:**
   - `generate` — produce new text → apply core principles proactively.
   - `transform` — rewrite given text → run detection, then rewriting skills.
   - `audit` — review a document without necessarily rewriting → use `workflows/document-audit`.
   - `question` — explain a guideline → answer from the relevant SKILL.md, cite the source institution.

2. **Detect domains present:** scan the text/request for domain signals:
   - Gender signals: pronouns he/she, gendered nouns (chairman, spokesman), titles (Mr./Mrs.), kinship terms, word-order pairs ("men and women").
   - Domain signals: disability terms, ethnicity/nationality terms, LGBTQIA+ terms, age terms, class/socioeconomic terms, religious terms.

3. **Dispatch to skills by trigger match** (each SKILL.md frontmatter lists its `triggers`).

4. **Apply guardrails** (`_meta/GUARDRAILS.md`) before producing any output.

5. **Compose output:** rewritten text (if requested) + optional change log with
   category, severity, rationale, and confidence per change.

### Precedence order (when guidance conflicts)

1. The individual's stated identity/pronouns/self-description (highest).
2. The governing style guide of the client organisation, if one is supplied.
3. Universal guardrails in `_meta/GUARDRAILS.md` (skill rules extend, never override them).
4. Skill-specific rules in the loaded SKILL.md files.
5. The most recent source document (see `SOURCES.md` divergence register).

Known divergences between sources are recorded in `_meta/SOURCES.md §3`; agents
must not silently pick a side — follow this precedence and note the choice in the
change log when it materially affects output.

---

## 4. SKILL.md file convention

Every `SKILL.md` uses the same skeleton so agents can parse them uniformly:

```markdown
---
skill: <dotted.id>            # e.g. gender.pronoun-strategy
title: <human name>
version: 1.0.0                # semver; bump on substantive rule changes
category: core|gender|identity-domains|communication|workflows
requires: [<skill.ids>]       # skills that must be loaded first
triggers: [<keywords/phrases>]# routing signals
sources: [<source-keys>]      # keys from _meta/SOURCES.md
---

## Purpose          — what this skill does
## When to use      — activation conditions
## Rules            — numbered, imperative, testable
## Procedure        — step-by-step algorithm where applicable
## Reference tables — avoid → prefer mappings (or pointer to references/)
## Guardrails       — skill-specific constraints (extend, never override, _meta/GUARDRAILS.md)
## Uncertainty      — what to do when information is missing
## Sources          — which document sections back each rule
```

Rules are written to be **imperative and checkable** ("Replace X with Y", "Never
do Z") rather than advisory, because the consumer is a machine agent, not a human
reader.

---

## 5. Change-log discipline

Any transformation performed under these skills should be able to produce a
structured change entry:

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

Severity scale (used across all skills):

| Level | Meaning |
|-------|---------|
| `critical` | Demeaning, dehumanising, or slur-adjacent language; misgendering a named person. |
| `high` | Systematic exclusion (generic masculine, male-as-default) or stereotype reinforcement. |
| `medium` | Trivialisation, unnecessary gendering, non-preferred but recognisable terms. |
| `low` | Style/readability improvements; borderline cases flagged for human decision. |

---

## 6. Extension guide

To add a new skill:

1. Create `skills/<tier-dir>/<skill-name>/SKILL.md` following §4 exactly.
2. Add its `sources` keys to `_meta/SOURCES.md` (register new PDFs in `material/` first).
3. Add routing triggers; keep them disjoint from existing skills where possible.
4. If the skill introduces rules that conflict with an existing skill, record the
   conflict and resolution in `_meta/SOURCES.md §3`.
5. Update the catalogue table in the root `README.md`.

Do not put example text containing slurs in skill files unless marked as
`avoid` entries inside tables — agents need the negative pattern for detection,
but files must never present slurs as usable vocabulary.
