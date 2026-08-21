# Guardrails — Operational Layer

This folder turns the library's guardrails from prose into an enforceable
system: layered rules, a register matrix, intake/finalisation checklists, and a
violation taxonomy with deliverable modes.

**Normative source:** [`skills/_meta/GUARDRAILS.md`](../skills/_meta/GUARDRAILS.md)
defines the fifteen universal guardrails (G1–G15) and their rationale. This
folder never contradicts it — it operationalises it.

> Version 1.0.0 · Built 2026-08-21 from a whole-project analysis: G1–G15 +
> the `## Guardrails` sections of all 15 SKILL.md files + the severity/change-log
> model + divergence register D1–D5.

---

## Contents

| File | Layer | What it gives the agent |
|---|---|---|
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | — | Layer model L0–L3, enforcement pipeline E1–E4, precedence, violation taxonomy |
| [`layers/L0-universal-guardrails.md`](layers/L0-universal-guardrails.md) | L0 | G1–G15 as trigger → check → on-violation table |
| [`layers/L1-domain-guardrails.md`](layers/L1-domain-guardrails.md) | L1 | 32 rules consolidated from all 15 skills, keyed by domain, each with G-refs and violation class |
| [`layers/L2-register-matrix.md`](layers/L2-register-matrix.md) | L2 | Which transformation strategies are permitted per register; divergence resolutions D1–D5 |
| [`layers/L3-output-integrity.md`](layers/L3-output-integrity.md) | L3 | Change-log schema, severity scale, confidence policy, deliverable modes, metrics |
| [`checklists/pre-execution.md`](checklists/pre-execution.md) | E1 | 10-point intake checklist |
| [`checklists/post-execution.md`](checklists/post-execution.md) | L3 runbook | Final sweep + deliverable-mode decision |

## Agent quick start

```
load  _meta/GUARDRAILS.md                 # L0 — always
run   guardrails/checklists/pre-execution.md
        -> classify task, detect register, scan domains
load  layers/L1-domain-guardrails.md      # only matched domains
apply layers/L2-register-matrix.md row    # permissions for this register
     ... do the work (skill rules) ...
run  guardrails/checklists/post-execution.md
        -> V-BLOCK? -> blocked
        -> V-WARN? -> flagged
        -> else   -> full (change log attached)
emit change log + metrics counters        # spec: layers/L3-output-integrity.md
```

## Counts

- 15 universal guardrails (L0, G1–G15)
- 32 domain rules (L1, `GD-*`) drawn from all 15 skills
- 6 registers × 5 strategy dimensions (L2)
- 2 operational checklists (E1 intake, L3 finalisation)
- 3 violation classes → 3 deliverable modes

## Governance

- Edits here must not contradict `_meta/GUARDRAILS.md`; conflicts resolve in
  favour of L0 and get logged in `_meta/SOURCES.md §3`.
- New domain rules: id `GD-<DOMAIN>-NN`, cite source skill + G-refs
  (procedure: [`ARCHITECTURE.md §7`](ARCHITECTURE.md)).
- Bump the version line of any file you change.
