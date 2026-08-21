---
skill: workflows.document-audit
title: Full-Document Inclusive-Language Audit
version: 1.0.0
category: workflows
requires: [core.inclusive-language-core]
triggers: [audit document, review report, check policy, full review,
  proofread inclusive, scan text]
sources: [EIGE-2019, UNW-EN, EIGE-2024]
---

## Purpose

Orchestrate a complete, reproducible audit of a document across all domains,
producing a structured findings report and (optionally) a revised version.

## When to use

Any `audit` task on documents > ~200 words, or any task explicitly requesting a
review/report. Short snippets go directly to the relevant Tier 2/3 skill.

## Rules

**R1 — Guardrails run first.** `_meta/GUARDRAILS.md` is applied before any scan;
conflicts between skills resolve via the ARCHITECTURE §3 precedence chain.

**R2 — Never fabricate.** Disaggregated statistics, names, or pronouns are never
invented; missing data becomes a flagged question, not an edit.

**R3 — Every finding carries an exact span.** Findings without a quotable excerpt
and location are invalid output.

**R4 — Human-review threshold.** Any fix with confidence < 0.7, or any legal-scope
risk, moves to the "For human decision" subsection instead of being auto-applied.

## Procedure

### Phase 0 — Intake
1. Record: document type, audience, jurisdiction/locale, register (informal /
   business / legal), governing style guide if supplied.
2. Set strategy defaults per register (divergences D1/D2/D4).
3. If non-English → apply G13 and stop or proceed principles-only with notice.

### Phase 1 — Mechanical term scan
4. Scan against all substitution tables (`gender-inclusive-rewriting/references/`)
   and every loaded identity-domain table. Log hits with exact spans.
5. Latin-root filter: exclude man(u)- words (manual, manufacture…).

### Phase 2 — Structural analysis
6. Pronoun chains: resolve every third-person pronoun to antecedent; classify via
   pronoun-strategy decision table.
7. Generic-masculine sweep: he/his/him, man/men compounds, male-default pairs.
8. Word-order hierarchy instances; naming/titling consistency; salutations.
9. Statistics passages: check for hidden gender dimensions needing visibility
   (core R3/R4) — flag only; never fabricate disaggregated data.

### Phase 3 — Domain passes
10. Load and apply each identity-domain skill whose trigger vocabulary appears.
11. Apply stereotype-detection three-category classification to remaining hits.

### Phase 4 — Multimodal pass (if assets present)
12. Run multimodal-inclusion checks on referenced images/scripts/forms/events.

### Phase 5 — Report
13. Emit findings in this schema:

```
# Inclusive Language Audit — <document>
Register: <...> | Style guide: <...|none> | Strategy defaults: <D1/D2/D4 choices>

## Summary
Total findings: N (critical: n, high: n, medium: n, low: n)

## Findings
| # | Location | Excerpt | Category | Severity | Rule | Suggested revision | Confidence |
|---|----------|---------|----------|----------|------|--------------------|------------|

## Notes
- Register assumptions, divergences applied, items requiring human decision.
```

14. If revision requested: apply fixes in severity order (critical→low),
    re-run agreement/scope verification after each batch, deliver revised text +
    change log (ARCHITECTURE §5 schema).

### Phase 6 — Final checklist (all must pass)
EIGE-2019 ch.6 checklist:
1. Stereotypes recognised and not repeated?
2. Active inclusivity for women and men?
3. Women, men, non-binary people as persons of equal value/dignity/integrity/respect?
4. Hidden gender elements considered where neutral language used?
5. No patronising/belittling terms?
6. Adjectives applicable across genders?
7. Document checked for gender-biased language?
8. No women described solely in relation to men?
9. No 'man'/'he' for everyone's experiences?
10. Gender-neutral occupational terms used?

UNW-EN checklist:
11. Replaceable gender-specific expressions replaced?
12. No masculine forms in generic references?
13. No occupational/other stereotypes?
14. No unnecessary sex/gender references?
15. Same kinds of information for different genders?

## Guardrails

- G1: any fix that risks scope change in binding text → formal-legal-texts rules +
  human-review flag.
- G4/G15: report tone is factual; no moralising; borderline items are flagged,
  not auto-fixed.

## Uncertainty

Findings with confidence < 0.7 go to a "For human decision" subsection instead of
the main table.

## Sources

- EIGE-2019 ch.5 (worked audits: 7+2 / 9+2 / 3 findings methodology), ch.6 checklist.
- UNW-EN: 5-question checklist.
- EIGE-2024: format-specific guiding questions.
