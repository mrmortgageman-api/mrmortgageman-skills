---
name: newsletter-studio
description: "Runs the governed #IGot5OnIt newsletter workflow from the existing Notion Newsletter Studio home and Google Drive Library. Does not replace Newsletter Studio or create new doctrine. Requires the Weekly Intelligence Packet before any draft, applies the payment translation patch, and requires Griff QA before Scott approval."
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

## Step 3 — Template Selection

Pick before writing:

- T1 Standard Weekly — default, no event
- T2 Mortgage Insider — first Wednesday of the month, automatic
- T3 Partner Event — end of month, guest speaker, requires a live registration link
- T4 Holiday — major holiday weeks only

T2 beats T3 in the same week. T4 overrides all. Never mix event blocks.

## Step 4 — Agent Play (Play of the Week)

Select from the Play Name Bank. Never repeat a play name within the same calendar year.

- 2 to 4 words, title case, action-oriented
- Names the move, not the outcome
- Real scenario underneath, anonymized

## Step 5 — Payment Translation Patch

- Conforming payment examples only
- Never quote jumbo payments using conforming pricing
- For jumbo scenarios, route the agent to Scott for a custom quote

## Step 6 — Hand Off to Draft Lane

Once the packet, template, and play are locked, hand off to drafting using the Master Guide's output structure and the Voice Guide. Mailchimp is distribution only — it is never the source of truth for content or data.

## Step 7 — QA and Approval Order

1. Griff QA
2. Scott approval (Scott is Editor-in-Chief — final call always his)

Nothing sends without both, in that order.

## Step 8 — After Send

Capture lessons learned and performance signal back into the Newsletter Performance Hub (Decision Log / Weekly Audit Log) so the next packet starts smarter than the last.

## Non-Negotiables

- No new doctrine gets created by this skill. If a gap shows up, flag it — don't patch it here.
- No Drive files get duplicated into GitHub. This skill points at them; it doesn't copy them.
- No draft starts before the Weekly Intelligence Packet is complete.
- No jumbo payment ever gets quoted at a conforming rate.

## Final Rule

This skill runs the play. It doesn't call the play. That's still Scott.
