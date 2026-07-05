---
name: newsletter-studio
description: "Runs the governed #IGot5OnIt newsletter workflow from the existing Notion Newsletter Studio home and Google Drive Library. Does not replace Newsletter Studio or create new doctrine. Requires the Weekly Intelligence Packet before any draft, applies the payment translation patch, requires Griff QA before Scott approval, and supports production baton mode for time-constrained Sunday execution."
---

# Skill: newsletter-studio

## Purpose

Make the existing #IGot5OnIt workflow executable by Sloan, Claude, Griff, or another capable AI operator — without duplicating, replacing, or overriding Newsletter Studio itself.

This skill is a thin operating wrapper. The Notion Newsletter Studio home and the Drive Library remain the source of truth. If this file and Notion ever disagree, Notion wins and the mismatch gets flagged to Scott, not resolved here.

## When to Activate

- "run the newsletter"
- "start this week's #IGot5OnIt"
- "build the intelligence packet"
- "what template this week"
- "prep Monday's newsletter"
- "Sunday production mode"
- "I need a 90% draft"
- "I need Mailchimp-ready HTML"

## Production Baton Mode

Use this mode when Scott is time-constrained, traveling, or explicitly says he cannot argue with the AI.

The operator taking the baton must return usable work, not questions, excuses, or partial process notes. The output must be at least 90% ready for Scott to review.

Required deliverables in Production Baton Mode:

1. Creative brief with the recommended angle
2. Two or three viable theme/title options
3. Weekly Intelligence Packet summary
4. Recommended template selection
5. Full newsletter draft in Scott's voice
6. Payment translation using the approved conforming-only rule
7. Play of the Week
8. Subject line A and B, with preview text
9. Griff QA checklist
10. Mailchimp-ready HTML using the selected template
11. Short notes on what needs Scott's final call

Do not stop at research. Do not stop at the packet. Do not hand Scott a checklist unless he specifically asks for only a checklist. If the source scan is incomplete, make the best supportable draft from available evidence and clearly label any weak spots.

## Step 1 — Load the Operating Home

Before anything else, load or reference:

- Notion: Newsletter Studio | MrMortgageMan (operating home) and the Newsletter Performance Hub
- Drive: the current Master Guide, System Instructions, Source Framework, Play Name Bank, and Voice Guide
- Drive: T1 (Standard), T2 (Mortgage Insider), T3 (Partner Event), T4 (Holiday) templates

Do not hardcode version numbers for these files in this skill. Pull whichever version is current in Notion/Drive at run time. If more than one version of a governing doc appears to be live at once, stop and flag the mismatch to Scott instead of picking one.

## Step 2 — Build the Weekly Intelligence Packet First

Do not draft the newsletter until the packet is complete. The packet must answer:

1. What changed?
2. Why does it matter?
3. What should agents tell clients?
4. What should agents do before Friday?
5. Why should they read Scott again next Monday?

Pull from the five-signal source framework (rate direction, buyer demand, inventory and pricing, affordability and access, agent strategy) independently. Do not hand this list back to Scott as a checklist — go get the data.

## Step 3 — Rate Source and Payment Math

For mortgage-rate inputs, use Mortgage News Daily's mortgage rates page unless Scott explicitly names a different source for that issue:

https://www.mortgagenewsdaily.com/mortgage-rates

The operator owns the rate pull. Scott does not manually confirm rates as a required production step.

For every rate-based payment example, record:

1. Source used
2. Pull date and time
3. Rate numbers used
4. Loan amount used
5. Principal and interest calculation
6. Any assumption or weak spot

Use the conforming-only payment rule in Step 6. If the rate source is unavailable, use the best available approved fallback, label it clearly as a production assumption, and do not stop the draft.

## Step 4 — Template Selection

Pick before writing:

- T1 Standard Weekly — default, no event
- T2 Mortgage Insider — first Wednesday of the month, automatic
- T3 Partner Event — end of month, guest speaker, requires a live registration link
- T4 Holiday — major holiday weeks only

T2 beats T3 in the same week. T4 overrides all. Never mix event blocks.

## Step 5 — Agent Play (Play of the Week)

Select from the Play Name Bank. Never repeat a play name within the same calendar year.

- 2 to 4 words, title case, action-oriented
- Names the move, not the outcome
- Real scenario underneath, anonymized

## Step 6 — Payment Translation Patch

- Conforming payment examples only
- Never quote jumbo payments using conforming pricing
- For jumbo scenarios, route the agent to Scott for a custom quote

## Step 7 — Hand Off to Draft Lane

Once the packet, template, rate inputs, payment math, and play are locked, draft using the Master Guide's output structure and the Voice Guide. Mailchimp is distribution only — it is never the source of truth for content or data.

The draft lane must produce both:

1. A readable editorial draft Scott can review for story and voice
2. Mailchimp-ready HTML using the selected active template

The HTML must be easy for Scott to copy into Mailchimp so he can preview, read, think, and give feedback without rebuilding the issue manually.

## Step 8 — QA and Approval Order

1. Griff QA
2. Scott approval (Scott is Editor-in-Chief — final call always his)

Nothing sends without both, in that order.

## Step 9 — After Send

Capture lessons learned and performance signal back into the Newsletter Performance Hub (Decision Log / Weekly Audit Log) so the next packet starts smarter than the last.

## Non-Negotiables

- No new doctrine gets created by this skill. If a gap shows up, flag it — don't patch it here.
- No Drive files get duplicated into GitHub. This skill points at them; it doesn't copy them.
- No draft starts before the Weekly Intelligence Packet is complete unless Scott explicitly orders emergency best-effort drafting.
- No jumbo payment ever gets quoted at a conforming rate.
- No production baton handoff may end with "I was waiting," "I could not proceed," or process-only notes when a best-effort draft could have been created.
- Scott is not the manual rate checker. The operator pulls rates from the approved rate source and shows Scott the source, timestamp, and math.

## Final Rule

This skill runs the play. It doesn't call the play. That's still Scott.
