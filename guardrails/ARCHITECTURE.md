# Guardrails Architecture

**Operational enforcement layer for the inclusive-language skills library.**
Normative prose lives in [`skills/_meta/GUARDRAILS.md`](../skills/_meta/GUARDRAILS.md);
this folder makes those guardrails *executable*: when each check fires, how to run
it, and what to do when it fails.

> Version 1.0.0 · Built 2026-08-21 by analysing the whole project: the fifteen
> universal guardrails (G1–G15), the `## Guardrails` sections of **all 15
> SKILL.md files**, the severity/change-log model (root README §8), and the
> divergence register D1–D5 (`_meta/SOURCES.md §3`).

---

## 1. Layer model

| Layer | File | What it contains | Binds | Override policy |
|---|---|---|---|---|
| **L0 — Universal** | `_meta/GUARDRAILS.md` + [`layers/L0-universal-guardrails.md`](layers/L0-universal-guardrails.md) | G1–G15 invariants | every task, every skill | **non-overridable** |
| **L1 — Domain** | [`layers/L1-domain-guardrails.md`](layers/L1-domain-guardrails.md) | 32 consolidated rules extracted from all 15 skills, keyed by domain | tasks matching domain triggers | extends L0 only |
| **L2 — Register** | [`layers/L2-register-matrix.md`](layers/L2-register-matrix.md) | which transformation strategies are permitted per register | strategy selection step | client style guide wins (G9) |
| **L3 — Output integrity** | [`layers/L3-output-integrity.md`](layers/L3-output-integrity.md) · runbook: [`checklists/post-execution.md`](checklists/post-execution.md) | change-log schema, confidence policy, deliverable modes | deliverable assembly | mandatory |

Loading rule: **L0 always**; add L1 sections whose domain triggers match the
task; select the L2 row matching the detected register; close with L3.

## 2. Enforcement pipeline

```
request
   │
   ▼
E1 INTAKE ................ classify task (generate|transform|audit|answer)
   │                       detect register -> pick L2 row
   │                       scan domain signals -> load L1 sections
   │                       inventory unknowns (pronouns/titles/affiliations)
   ▼
E2 TRANSFORM / GENERATE .. apply skill rules; every candidate edit is checked
   │                       against L0 FIRST; violations logged by class
   ▼
E3 ASSEMBLY .............. run post-execution checklist (L3)
   │                       collect violation set {V-BLOCK, V-WARN, V-LOG}
   │                       decide deliverable mode: full | flagged | blocked
   ▼
E4 DELIVERY .............. attach structured change log
                           route human-review items
                           update metrics counters
```

Pre-execution detail: [`checklists/pre-execution.md`](checklists/pre-execution.md).

## 3. Precedence and conflict resolution

Binding order for any decision:

```
individual's stated identity  >  client style guide  >  L0 guardrails
                              >  skill rules (L1)    >  most recent source
```

- L0 sits **above** skill rules: a skill may extend but never override a
  universal guardrail (`GUARDRAILS.md` preamble). If a client instruction
  conflicts with L0, surface the conflict explicitly — never silently comply,
  never silently refuse.
- The L2 matrix resolves *strategy* disagreements between sources via the
  divergence register (D1–D5); see [`register-matrix.md`](register-matrix.md).

## 4. Violation taxonomy and deliverable modes

| Class | Meaning | Typical triggers | Deliverable mode |
|---|---|---|---|
| **V-BLOCK** | Hard stop. Must be fixed or routed to a human before anything is emitted. | meaning altered in binding text (G1); misgendering/scare-quoting a known person (G2); silent quote modernisation (G5); outing (G11); slur generated outside avoid-tables (G12) | `blocked` (return findings + required fixes) or `flagged` with mandatory human review |
| **V-WARN** | Fix, or ship with an explicit annotation. | over-correction (G4); deficit framing (G10); register mismatch (G9); tokenistic representation (L1 multimodal) | `flagged` |
| **V-LOG** | Record in the change log; no delivery barrier. | specificity upgrades (G6); terminology-recency notes (G14); language-scope notice (G13) | `full` |

Deliverable modes:

- **full** — all checks pass; change log attached.
- **flagged** — warnings annotated; human-review items listed at top.
- **blocked** — unresolved V-BLOCK; do **not** emit the text; emit findings.

## 5. L0 enforcement table (G1–G15)

Compact machine-actionable rendering. Full rationale: `_meta/GUARDRAILS.md`.

| ID | Fires when | Check | On violation |
|----|------------|-------|--------------|
| G1 | any edit to source text | referent coverage identical pre/post; legal texts: noun repetition preferred, pluralisation treated with caution | V-BLOCK |
| G2 | any reference to a person | stated name/pronouns/title used verbatim; no scare quotes, no second-guessing | V-BLOCK |
| G3 | a characteristic is about to be mentioned | relevance test passes; term as specific as context allows | V-WARN |
| G4 | edits are being selected | proportionate, not mechanical; respectful factual usage not flagged | V-WARN |
| G5 | quotes, titles, legislation names, direct speech present | verbatim preserved; in-quote bias marked, never modernised | V-BLOCK |
| G6 | a group label is chosen | most precise respectful term; umbrella initialisms only for genuinely mixed references | V-LOG |
| G7 | disability/identity phrasing chosen | community/individual preference followed; both models accepted | V-WARN |
| G8 | pronoun/title/affiliation unknown | ask → else neutral default → else low-confidence flag; never guess | V-WARN |
| G9 | a strategy is selected | register detected and stated; governing style guide wins | V-LOG |
| G10 | groups or individuals compared | objective comparatives; no deficit framing | V-WARN |
| G11 | personal status information near output | nothing outed or inferred from appearance/voice/name | V-BLOCK |
| G12 | hostile vocabulary encountered/generated | slurs exist only as avoid-patterns; discussion = quoted + critical framing | V-BLOCK |
| G13 | output language ≠ English | scope notice given; language-specific guide recommended | V-LOG |
| G14 | terminology selected | newest corpus consensus; uncertain claims date-stamped | V-LOG |
| G15 | changes are finalised | category/severity/rationale/confidence complete; tone neutral, zero moralising | V-WARN |

## 6. Metrics hooks

Every completed task emits counters alongside its change log, making agent
behaviour regression-testable (root README §8):

```
g_checks_total, v_block, v_warn, v_log, human_review_requests
```

## 7. Extending the guardrail system

1. New domain rule → append to `domain-guardrails.md` with id
   `GD-<DOMAIN>-NN`, citing the source skill and every G-ref it depends on.
2. A new rule may **never** contradict L0; if it seems to, the conflict is a
   bug — resolve in favour of L0 and document in `_meta/SOURCES.md`.
3. New register or strategy shift → propose a row change in
   `register-matrix.md` together with its divergence-register entry.
4. Bump the version line at the top of the edited file.

## 8. File map

```
guardrails/
├── README.md                          ← index + agent quick start
├── ARCHITECTURE.md                    ← this file: layers, pipeline, taxonomy
├── layers/
│   ├── L0-universal-guardrails.md     ← G1–G15 enforcement rendering
│   ├── L1-domain-guardrails.md        ← L1: 32 rules from all 15 skills
│   ├── L2-register-matrix.md          ← L2: register × strategy permissions
│   └── L3-output-integrity.md         ← L3: change-log schema, confidence policy, modes
└── checklists/
    ├── pre-execution.md               ← E1 intake checklist
    └── post-execution.md              ← L3 runbook + deliverable mode
```
