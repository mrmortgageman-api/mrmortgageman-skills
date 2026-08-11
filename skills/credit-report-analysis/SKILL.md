---
name: credit-report-analysis
description: Analyzes an uploaded credit report (tri-merge, single bureau, or credit monitoring export) and produces a mortgage-underwriter-level diagnostic — score tier classification, tier-crossing opportunities, red flags, and a Scott-voice borrower summary. Use this whenever Scott uploads a credit report or credit report screenshot/PDF and asks for an analysis, breakdown, credit strategy, or "run this file's credit," even if he doesn't say "credit report" explicitly (e.g. "what's this borrower's credit picture," "where does this file sit," "tell me what I'm working with"). Always redacts SSN and DOB from all output — never echoes, stores, or repeats those fields under any circumstance. Feeds Complexity Marker detection and STRATEGY LOCK logic per Scenario Engine doctrine.
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

## Step 4 — Derogatory account strategy: flag only, don't prescribe

Do not recommend pay-for-delete, settlement, or dispute strategy on specific accounts — that
drifts into credit-repair-organization territory and needs a compliance sign-off Scott hasn't
confirmed yet. Instead:

> "Collection account detected: [creditor], [amount], [age]. May require a lender explanation
> letter or payoff at closing depending on program. Flagging for Scott's review — not
> recommending a specific resolution path here."

## Step 5 — Complexity Marker integration

Per Scenario Engine doctrine, these conditions are already Complexity Markers:
recent credit event (bankruptcy, short sale, late payments), thin file, high revolving
utilization.

If this skill detects any of those in the report, **auto-flag them** the same way the rest of
the Enforcement Layer does — surface the marker count and note whether STRATEGY LOCK applies
(2+ markers = STRATEGY LOCK REQUIRED, scenario generation blocked until Scott confirms).

## Step 6 — Output structure

Produce two blocks, standalone — do not auto-write to Notion. Scott decides if/how this folds
into a B2C Notion Handoff Block.

### DIAGNOSTIC (Scott-facing, internal)

- Representative score + method used
- Tier standing across Conventional / FHA / VA / Jumbo-NonQM as applicable to the file type
- Tier-crossing opportunity (if within range) — the headline insight
- Red flags (underwriter lens): what they are, why they matter, severity
- Derogatory accounts: flagged, not prescribed
- Inquiries: excessive or not, and why
- Complexity Markers detected + STRATEGY LOCK status
- Pricing data currency line

### CLIENT-SAFE SUMMARY (borrower-facing, Scott voice)

Written to the Scenario Engine voice rules: short sentences, specific numbers where safe
(never invented point estimates), no jargon, confidence not pressure, no em dashes, every
sentence under 20 words.

Frame as advisory strategy discussion, never as a credit decision or denial. This is
diagnostic and educational — not an adverse action notice, and should never read like one.

End with exactly one clear next step.

## Failure mode

If the report is unreadable, missing key fields, or ambiguous on which score to use as
representative — pause, ask ONE clarifying question, explain why it matters. No speculation,
per Scenario Engine Failure Mode doctrine.
