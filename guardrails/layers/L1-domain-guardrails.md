# Domain Guardrails (Layer L1)

Consolidated skill-level guardrails for the whole library, extracted from the
`## Guardrails` section of **all 15 SKILL.md files** on 2026-08-21 and grouped
by domain. Each entry cites its source skill and the universal guardrails
(G-refs) it depends on.

**Binding rule:** these extend, never override, Layer L0
(`_meta/GUARDRAILS.md`). If an entry ever appears to conflict with a G-rule,
L0 wins and the conflict is treated as a bug.

> Version 1.0.0 · 32 rules · Source of truth: the skills themselves. When a
> SKILL.md changes, update its entries here.

On-violation classes (`V-BLOCK` / `V-WARN` / `V-LOG`) are defined in
[`../ARCHITECTURE.md §4`](../ARCHITECTURE.md).

---

## Core (Tier 1)

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-CORE-01 | Never "correct" a person's self-description. | G2 | V-BLOCK | core/inclusive-language-core |
| GD-CORE-02 | Gender-neutral is a legitimate destination, not a failure state — but flag when neutrality hides a material gender dimension (divergence D3). | D3 | V-WARN | core/inclusive-language-core |

## Gender (Tier 2)

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-GEN-01 | A person's stated title/pronouns override every default in title and pronoun rules. | G2 | V-BLOCK | gender/address-and-titles |
| GD-GEN-02 | Courtesy titles: omit-by-default wins unless the client style guide says otherwise (divergence D4). | D4 | V-LOG | gender/address-and-titles |
| GD-GEN-03 | In formal/legal registers apply formal-legal-texts rules first: noun repetition before pronoun strategies (divergence D1). | G1, G9, D1 | V-WARN | gender/pronoun-strategy |
| GD-GEN-04 | Any legal fix that risks scope change → neutral construction + `requires-human-review` flag. G1 overrides everything in this skill. | G1 | V-BLOCK | gender/formal-legal-texts |
| GD-GEN-05 | This skill never provides legal advice; it flags interpretive risk only. | — | V-LOG | gender/formal-legal-texts |
| GD-GEN-06 | Single occurrences of "he or she" are not violations; never double-count one issue across categories — pick the dominant category. | G4 | V-LOG | gender/stereotype-detection |
| GD-GEN-07 | Quoted/historical material is flagged at most `low`, with note "quote preserved". | G5 | V-LOG | gender/stereotype-detection |
| GD-GEN-08 | Do not slash every pronoun pair through a long text — readability is part of inclusivity. | G4 | V-WARN | gender/gender-inclusive-rewriting |
| GD-GEN-09 | Text that deliberately discusses gendered language itself (linguistics, moderation) keeps quoted forms inside quotation marks. | G5 | V-LOG | gender/gender-inclusive-rewriting |
| GD-GEN-10 | Never generate content that mocks or invalidates anyone's pronouns. | G2, G12 | V-BLOCK | gender/pronoun-strategy |

## Identity domains (Tier 3)

### Disability

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-DIS-01 | Individual preference beats table defaults; person-first and identity-first are both acceptable coherent choices. | G2, G7 | V-WARN | identity-domains/disability-language |
| GD-DIS-02 | No deficit framing ("despite her disability she…") — describe achievement directly. | G10 | V-WARN | identity-domains/disability-language |

### Ethnicity

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-ETH-01 | Slurs appear only inside quotes with critical framing, minimised. | G5, G12 | V-BLOCK | identity-domains/ethnicity-language |
| GD-ETH-02 | Umbrella terms are fallbacks; specificity wins whenever known. | G6 | V-LOG | identity-domains/ethnicity-language |
| GD-ETH-03 | EU institutions use "Roma" as umbrella even though not all Romani-speaking groups self-identify so — state the convention being followed. | G14 | V-LOG | identity-domains/ethnicity-language |

### LGBTQIA+

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-LGB-01 | Never out anyone; never frame being LGBTQ+ as shameful, negative, or a "preference". | G2, G11 | V-BLOCK | identity-domains/lgbtqia-language |
| GD-LGB-02 | Historical/legal analysis may quote derogatory terms only with explicit bias-marking, minimised. | G5 | V-WARN | identity-domains/lgbtqia-language |

### Age

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-AGE-01 | Mention age only when relevant. | G3 | V-WARN | identity-domains/age-language |
| GD-AGE-02 | No judgemental comparatives about age groups ("surprisingly competent for her age" → describe competence directly). | G10 | V-WARN | identity-domains/age-language |

### Socioeconomic class

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-CLS-01 | Mention class only when relevant. | G3 | V-WARN | identity-domains/class-language |
| GD-CLS-02 | Immigration status is sensitive — never speculate about it or expose it. | G11 | V-BLOCK | identity-domains/class-language |

### Religion

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-REL-01 | Scripture and liturgy are quoted verbatim, including gendered deity language. | G5 | V-BLOCK | identity-domains/religion-language |
| GD-REL-02 | Antisemitic/Islamophobic tropes are never generated; historical discussion requires explicit critical framing. | G12 | V-BLOCK | identity-domains/religion-language |

## Communication (Tier 4)

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-MOD-01 | Diverse representation ≠ token checklist; represent what the content's audience/context actually involves (G3 applies visually too). | G3 | V-WARN | communication/multimodal-inclusion |
| GD-MOD-02 | Do not demand impossible stock: if suitable inclusive assets don't exist, recommend commissioning/adjusting rather than accepting stereotype defaults. | — | V-LOG | communication/multimodal-inclusion |
| GD-AI-01 | All universal guardrails apply to self-generated content with equal force (G1–G15). | G1–G15 | V-BLOCK | communication/ai-content-generation |
| GD-AI-02 | Change logs distinguish "source text was biased" from "our draft was biased". | G15 | V-WARN | communication/ai-content-generation |

## Workflows (Tier 5)

| ID | Rule | Refs | On violation | Source skill |
|----|------|------|--------------|--------------|
| GD-AUD-01 | Any fix that risks scope change in binding text → formal-legal-texts rules + human-review flag. | G1 | V-BLOCK | workflows/document-audit |
| GD-AUD-02 | Report tone is factual; no moralising; borderline items are flagged, not auto-fixed. | G4, G15 | V-WARN | workflows/document-audit |

---

## Coverage note

Every one of the 15 SKILL.md files contributes at least one entry above; the
extraction covered all `## Guardrails` sections verbatim and assigned IDs,
violation classes, and cross-references. Total: **32 domain rules** across
6 groups, referencing 13 of the 15 universal guardrails (G1–G12, G14, G15;
G13 language-scope lives only at L0 because it binds all outputs equally).
