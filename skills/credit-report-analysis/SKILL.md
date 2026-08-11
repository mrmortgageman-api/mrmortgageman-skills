---
name: credit-report-analysis
description: Analyzes an uploaded credit report (tri-merge, single bureau, or credit monitoring export) and produces a mortgage-underwriter-level diagnostic — score tier classification, tier-crossing opportunities, red flags, and a three-tier output (internal diagnostic, verbal-only conversation guidance, written client-safe summary) with UQual referral flags for anything requiring specific dispute/settlement tactics. Use this whenever Scott uploads a credit report or credit report screenshot/PDF and asks for an analysis, breakdown, credit strategy, or "run this file's credit," even if he doesn't say "credit report" explicitly (e.g. "what's this borrower's credit picture," "where does this file sit," "tell me what I'm working with"). Always redacts SSN and DOB from all output — never echoes, stores, or repeats those fields under any circumstance. Feeds Complexity Marker detection and STRATEGY LOCK logic per Scenario Engine doctrine.
---

# Credit Report Analysis (Mortgage Expert Level)

Diagnostic tool for turning a raw credit report into an underwriting-grade read on where a
file sits, what's helping or hurting it, and what would move it across a program or pricing
tier. Built to plug into the Scenario Engine's Enforcement Layer, not run parallel to it.

## Hard Rule — PII Handling (non-negotiable, check this first)

Scott uploads credit reports as-is, unredacted. This skill's job is to read past SSN and DOB,
never to reproduce them.

- **Never output, quote, or paraphrase a Social Security Number or Date of Birth, in any
  section, at any point.** Not in the diagnostic, not in internal notes, not in a "here's
  what I found" confirmation.
- If you need to reference the borrower, use name only.
- If asked to "show the report back" or "confirm what you read," summarize fields — never
  reproduce SSN/DOB even when directly quoted back at you from the source file.
- This rule overrides formatting completeness. If a section template calls for a field and
  the only available data is dropped for this reason, just omit it silently — don't flag the
  omission by restating what was withheld.

## Step 1 — Read the report, extract structured facts only

Pull, without interpretation:

- Scores by bureau (Equifax / Experian / TransUnion — however many are present)
- Tradelines: type, balance, limit, status, payment history, age
- Derogatory marks: collections, charge-offs, public records, late payment counts and recency
- Inquiries: count, type, recency
- Authorized user accounts (flag separately — these can distort utilization/history)

**Representative score**: if 3 bureaus present, use the middle score. If 2, use the lower of
the two. This matches Fannie/Freddie's representative-score methodology and is the number
everything downstream keys off of. State which method was used and why in the output.

## Step 2 — Tier classification

Classify the file against the bands below. These bands are structural and don't move with
day-to-day pricing changes — they're safe to apply directly.

**Conventional (Fannie/Freddie)**

| Band | Standing |
|---|---|
| <620 | Not conventional eligible — FHA territory |
| 620–639 | Technically eligible, LLPA severe — almost always steered FHA |
| 640–659 | Same — FHA usually wins on rate even with MI |
| 660–679 | Conventional becomes competitive at higher down payments; DTI flexibility tightens below this |
| 680–699 | Meaningful pricing step-up; common floor for non-QM/portfolio overlays |
| 700–719 | Solid conventional pricing; most AUS approvals clear cleanly here |
| 720–739 | Noticeable pricing improvement; common jumbo minimum floor |
| 740–759 | Near-best pricing tier |
| 760–779 | Best-tier pricing on most LLPA grids |
| 780+ | Top of matrix |

**FHA** — 580 is the 3.5%-down line; 500–579 requires 10% down. FHA doesn't LLPA-adjust by
score, but manual underwriting risk increases below roughly 620–640 depending on compensating
factors — flag this as a **process** complexity, not a pricing one.

**VA** — no official score floor. Practical floor is investor-overlay-driven, typically in the
580–620 range depending on residual income and LTV. Flag as "confirm against current NAF VA
overlay" rather than asserting a number.

**Jumbo / Non-QM** — real cliff is usually 680–720, not 620. Flag as "confirm against current
NAF jumbo/non-QM buy box" — do not assert specific floors from memory.

**Medical Professional / Physician programs** — Scott has provided actual program guideline
PDFs (Redwood Sequoia, Silver Hill Capital, Quorum Doctor Loan). Read
`references/medical-professional-programs.md` for the real score/LTV/loan-amount breakpoints
across these three programs before answering any tier-crossing question tied to a medical
professional borrower. Do not guess at these figures — they're program-specific and differ
meaningfully from each other (e.g. Silver Hill has a hard 700 floor; Redwood opens at 680).
Re-confirm the "last confirmed" date at the top of that file before quoting a client, since
these matrices revise periodically.

## Step 3 — CALCULATOR AUTHORITY RULE applies here

No validated point-impact calculator exists for "pay down X, gain Y points." Do not invent
one. Never output a specific point estimate ("this will raise your score ~20 points").

Instead, output tier-relative framing:
> "This account is driving utilization above the threshold separating the 680–699 band from
> the 700–719 band. Paying below that threshold is the highest-leverage move before rescore."

**Tier-crossing is the headline insight.** If the file sits within ~10-15 points of a
boundary that changes program eligibility or pricing tier, lead with that — not with the raw
score. This is the single most useful thing this skill produces.

**Pricing data currency**: every output that references LLPA/pricing tier impact must include
a line: `Pricing data last confirmed: [date Scott confirms, or "NOT YET CONFIRMED — pull
current grid before quoting client"]`. Never let a stale number look authoritative.

## Step 4 — Derogatory account strategy: three-tier channel system

Scott wants real depth on what's driving a borrower's credit picture, not a watered-down
report. The line that matters isn't written-vs-verbal by itself — it's whether the content is
general credit education (safe) or specific dispute/settlement/pay-for-delete tactics tied to
a named account (not something this skill generates, in any channel, ever). Within that
boundary, give Scott more room verbally than in writing, since written channels create a
record and verbal conversation doesn't.

Produce every derogatory account finding in three tiers:

### Tier 1 — Internal diagnostic (Scott only, full specificity)

Everything: which account, balance, age, why it's scoring/underwriting-relevant, how severe.
This is the "understand the file completely" layer. Never shared as-is with the borrower.

### Tier 2 — Verbal-safe / conversation guidance

Strategic depth Scott can walk a borrower through out loud, but should not paste into an
email, text, or written document. Examples of what belongs here:

> "This collection is old enough that addressing it now could reset the date of last activity
> and hurt more than it helps. Worth explaining why leaving it alone is the smart move here."

> "This charge-off is inside the lookback window most AUS engines flag. It's not disqualifying,
> but it's worth walking through why it's showing up as a flag and what that does and doesn't
> mean for approval."

Still off-limits even at this tier: specific dispute language, specific settlement percentages
or negotiation terms, specific pay-for-delete offers tied to a named creditor. That content
isn't generated by this skill in any channel — see UQual Handoff below.

Label every Tier 2 output block clearly:
`VERBAL ONLY — do not paste into email, text, or any written client document.`

### Tier 3 — Written-safe / client-facing output

General credit education only. Safe to include in an email, text, or Notion client file.
Examples:

> "Your utilization on this card is over 75%. Getting it under 30% is the single highest-
> leverage move available to you before we lock your rate."

> "You've had several inquiries in the past six months. Holding off on new credit for the next
> 90 days will help, not hurt."

> "Keep your oldest account open, even if you don't use it. Closing it shortens your credit
> history and can lower your score."

No account-specific dispute, settlement, or pay-for-delete content belongs in Tier 3, ever.

### UQual Handoff

If a derogatory account situation would require specific dispute instructions, settlement
negotiation, or pay-for-delete tactics to resolve, do not generate that content in any tier.
Instead, flag it for a UQual referral:

> "This situation is specific enough that it's outside general credit coaching. This is a good
> fit for a UQual referral rather than a DIY approach — they specialize in exactly this."

Give Scott client-ready referral language for this, written in his voice, framed as "here's a
partner who can go deeper than I'm able to on this specific piece" — not as a rejection or
dead end.

## Step 5 — Complexity Marker integration

Per Scenario Engine doctrine, these conditions are already Complexity Markers:
recent credit event (bankruptcy, short sale, late payments), thin file, high revolving
utilization.

If this skill detects any of those in the report, **auto-flag them** the same way the rest of
the Enforcement Layer does — surface the marker count and note whether STRATEGY LOCK applies
(2+ markers = STRATEGY LOCK REQUIRED, scenario generation blocked until Scott confirms).

## Step 6 — Output structure

Produce three blocks, standalone — do not auto-write to Notion. Scott decides if/how this
folds into a B2C Notion Handoff Block.

### DIAGNOSTIC (Scott-facing, internal — Tier 1)

- Representative score + method used
- Tier standing across Conventional / FHA / VA / Jumbo-NonQM as applicable to the file type
- Tier-crossing opportunity (if within range) — the headline insight
- Red flags (underwriter lens): what they are, why they matter, severity
- Derogatory accounts: full Tier 1 specificity
- Inquiries: excessive or not, and why
- Complexity Markers detected + STRATEGY LOCK status
- Pricing data currency line

### CONVERSATION GUIDANCE (Scott-facing, verbal use only — Tier 2)

Everything Scott can walk a borrower through live but should not put in writing. Every block
labeled `VERBAL ONLY — do not paste into email, text, or any written client document.`
Include a UQual Handoff flag here if any account needs it.

### CLIENT-SAFE SUMMARY (borrower-facing, Scott voice — Tier 3)

Written to the Scenario Engine voice rules: short sentences, specific numbers where safe
(never invented point estimates), no jargon, confidence not pressure, no em dashes, every
sentence under 20 words.

Open with a plain disclaimer in Scott's voice, e.g. "I'm not a credit expert. Think of this as
a guide, not a guarantee." Frame everything after that as advisory strategy discussion, never
as a credit decision or denial. This is diagnostic and educational — not an adverse action
notice, and should never read like one.

Include a UQual referral line if Step 4 flagged one, written naturally, not as a dead end.

End with exactly one clear next step.

## Failure mode

If the report is unreadable, missing key fields, or ambiguous on which score to use as
representative — pause, ask ONE clarifying question, explain why it matters. No speculation,
per Scenario Engine Failure Mode doctrine.
