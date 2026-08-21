# Pre-Execution Checklist (Pipeline Stage E1)

Run **before** any transform / generate / audit task. Purpose: load exactly the
right guardrail surface and arm the checks that will matter.

> Version 1.0.0 · Companion to [`ARCHITECTURE.md`](../ARCHITECTURE.md) §2

---

- [ ] **1. Classify the task** — `generate` | `transform` | `audit` | `question`
      (`_meta/ARCHITECTURE.md §3`).
- [ ] **2. Detect the register** — pick the matching row in
      [`register-matrix.md`](../register-matrix.md); if detection is uncertain,
      choose the more restrictive plausible register and state the assumption (G8, G9).
- [ ] **3. Scan domain signals** — load the matching sections of
      [`domain-guardrails.md`](../domain-guardrails.md) (gender, disability,
      ethnicity, LGBTQIA+, age, class, religion, multimodal, AI-generation, audit).
- [ ] **4. Check for a governing style guide** — if the client supplied one, it
      wins over the register matrix (G9); record that it governs.
- [ ] **5. Language scope** — output language ≠ English? Prepare the G13 notice
      and the pointer to the relevant language-specific guide.
- [ ] **6. Inventory unknowns** — persons whose pronouns/titles/affiliations are
      unknown → plan G8 (ask → neutral default → low-confidence flag).
- [ ] **7. Sensitive-material scan of the source** — verbatim quotes, titles,
      statistics, potentially hostile vocabulary present? Arm G5 (quote
      integrity) and G12 (slur handling) accordingly.
- [ ] **8. Binding text?** — contracts, legislation, collective agreements,
      policies → arm `gender/formal-legal-texts` rules: noun repetition first,
      pluralisation caution, human-review flags (GD-GEN-03/04).
- [ ] **9. Load plan** — Tiers 0+1 always; add only the tiers the signals demand;
      never load more than one tier ahead (`_meta/ARCHITECTURE.md §2`).
- [ ] **10. Initialise metrics counters** — `g_checks_total`, `v_block`,
      `v_warn`, `v_log`, `human_review_requests`.
