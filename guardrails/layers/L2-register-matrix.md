# Register Matrix (Layer L2)

Which transformation strategies are permitted, per register. Grounded in the
divergence register (`_meta/SOURCES.md §3`, D1–D5) and the formal/legal rules
(`gender/formal-legal-texts`). Detect the register **before** choosing a
strategy and state the assumption (G9). A governing client style guide always
wins over this matrix.

> Version 1.0.0 · 2026-08-21

---

## Strategy permission values

| Value | Meaning |
|---|---|
| `preferred` | first-choice strategy on the ladder |
| `allowed` | acceptable without annotation |
| `fallback_only` | use only when better strategies fail; note in change log |
| `restricted` | only with explicit justification + human-review flag |
| `discouraged` | avoid; prefer restructure |
| `contextual` | decide per case; state reasoning |

## Matrix

| Register | Singular "they" | Dual forms ("he or she") | Slash pairs ("s/he", "he/she") | Courtesy titles | Gender visibility |
|---|---|---|---|---|---|
| **Legal / binding** (contracts, legislation, CBAs, policies) | `restricted` (D1) | `fallback_only` (D2) | `restricted` | `contextual` (D4) | `contextual` |
| **Official / policy** (public-sector guidance, reports) | `allowed` | `fallback_only` | `discouraged` | `omit_default` (D4) | `visible_ok` |
| **Business / professional** (corporate comms, HR, email) | `preferred` | `fallback_only` | `discouraged` | `omit_default` | `visible_ok` |
| **Public communications** (web, press, newsletters) | `preferred` | `contextual` | `discouraged` | `omit_default` | `visible_ok` |
| **Marketing / social** (campaigns, posts, hashtags) | `preferred` | `contextual` | `discouraged` | `free` | `audience-dependent`; mixed "guys" per D5 |
| **Informal / internal** (chat, drafts, notes) | `allowed` | `allowed` | `discouraged` | `free` | `free` |

Universal guardrails L0 bind in **every** row — permissiveness never licenses
meaning alteration (G1), misgendering (G2), or slur generation (G12).

## Register detection signals

- **Legal/binding:** defined terms, "shall/must", party names, clause numbering,
  recitals, signature blocks.
- **Official/policy:** institutional letterhead, recommendations addressed to
  member states/organisations, footnoted sources.
- **Business/professional:** workplace documents, HR processes, client email.
- **Public communications:** outward-facing prose, general-audience web copy.
- **Marketing/social:** brand voice, calls to action, hashtags, emoji.
- **Informal/internal:** low-stakes drafts, chat, meeting notes.

If detection is uncertain: choose the **more restrictive** plausible register
and say so (G8/G9).

## Legal/binding special rules

From `gender/formal-legal-texts` (these override the matrix cells above):

1. Prefer **repeating the noun** over any pronoun strategy.
2. Treat **pluralisation with caution** — it can convert an individual duty into
   a collective one (scope change, G1).
3. Any fix that risks altering who or what a clause covers → neutral
   construction + `requires-human-review` flag (GD-GEN-04).
4. Interpretive-clause handling and full procedure: `gender/formal-legal-texts`.

## Divergence register (drives this matrix)

| ID | Disagreement | Resolution applied here |
|----|--------------|--------------------------|
| D1 | Singular "they" in formal texts — UN Women restricts; CAPE/EIGE-2024 embrace | `restricted` in legal, `allowed` upward elsewhere |
| D2 | Dual-form pronouns as fallback vs default | `fallback_only` everywhere; never default |
| D3 | Gender-sensitive vs gender-inclusive target state | neutrality legitimate, but flag hidden material gender dimensions (GD-CORE-02) |
| D4 | Courtesy-title omission vs retention | omit-by-default unless client style guide says otherwise |
| D5 | Mixed-group "guys" | audience-dependent in marketing/social; avoid in professional+ registers |

Full rationale: `_meta/SOURCES.md §3`.
