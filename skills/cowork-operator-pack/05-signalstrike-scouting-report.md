---
name: signalstrike-scouting-report
description: >
  Build a structured SignalStrike scouting report for a real estate agent or referral partner
  target. Use when Scott is evaluating a new prospect for outreach and needs a scored profile
  before writing a Touch 0 or Touch 1. Pulls from HubSpot data, public signals, and intent
  scoring to produce an outreach-ready dossier with recommended touch strategy.
triggers:
  - "run a scouting report"
  - "scout this agent"
  - "SignalStrike report"
  - "who is this agent"
  - "should I reach out to this person"
  - "score this contact"
  - "build a dossier"
  - "evaluate this prospect"
related_skills:
  - cold-email (use after scouting report to write the Touch 0 or Touch 1)
  - product-marketing-context (read first — defines ICP and scoring context)
  - revops (use to confirm HubSpot record exists and score is logged)
  - cowork-queue-manager (use to queue scouting reports for batch processing)
---

# SignalStrike Scouting Report

## Purpose

Before writing a single word of outreach, know who you are targeting.
This skill turns a name and a platform handle into a scored, actionable outreach brief.

---

## Required Inputs

Before running the report, confirm you have at least three of these:

- Full name
- Brokerage or company
- Market or zip codes they work
- Platform where the signal was spotted (YouTube, Instagram, LinkedIn, Google Business)
- Signal type (new listing, new video, sold listing, review response, content post)
- HubSpot record ID if the contact already exists

---

## Scouting Report Format

Contact: [Full name]
Brokerage: [Name]
Market: [City / Region / Zip codes]
Platform spotted: [Platform]
Signal type: [Signal]
HubSpot record: [ID or Not yet created]
Whale Flag: [Yes / No / Unknown]

### Signal Analysis
[2-3 sentences describing what the signal tells you about this agent's business right now.
Focus on volume, activity level, niche, buyer vs. seller side, and price point.]

### ICP Match Score (1-5)
Score: [1-5]
Rationale: [One sentence explaining the score. What makes them a strong or weak fit?]

ICP match criteria:
5 — Active buyer-side agent, high volume, works markets where Scott closes deals, no existing lender lock
4 — Strong buyer-side indicators, moderate volume, some overlap with Scott's markets
3 — Mixed signals. Buyer and seller side. Worth one touch to qualify.
2 — Primarily seller-side. Low buyer volume. Low priority.
1 — No buyer-side signals. Wrong market. Do not pursue.

### Intent Signal Score (1-5)
Score: [1-5]
Rationale: [One sentence explaining the signal strength.]

Signal scoring guide:
5 — Multiple signals in the last 30 days. Active posting, new listings, fresh reviews, recent video.
4 — 2-3 signals in the last 60 days.
3 — Single strong signal in the last 90 days.
2 — Signal is older than 90 days or weak (one comment, one post).
1 — No clear signal. Do not use SignalStrike on this contact.

### Combined Score
Total: [ICP score + Intent score, out of 10]
Outreach eligible: [Yes — score 6 or higher / No — score below 6]

### Recommended Touch Strategy
[Based on combined score and Whale Flag status, recommend which touch to start with
and what angle to use. Reference cold-email skill for execution.]

Touch to start: [Touch 0 / Touch 1 / Skip]
Angle: [One-sentence outreach angle specific to this agent's signal]
Timing: [Now / Wait for stronger signal / Monitor and re-score in 30 days]

### HubSpot Action Required
[What needs to be logged or updated in HubSpot before outreach begins.
Scott must approve all writes.]

---

## Hard Rules

- Do not run a scouting report on a contact with an ICP score below 2. Not worth the session.
- Do not start outreach on a contact with a combined score below 6.
- Whale Flag contacts must be confirmed with Scott before any outreach is written.
- Signal scores older than 90 days must be noted. Stale signals do not justify fresh outreach.
- HubSpot must have a record before Touch 1 goes out. Touch 0 can happen first.

---

## Quality Check Before Delivering Report

- Combined score calculated and outreach eligibility stated?
- Touch strategy includes a specific angle, not a generic recommendation?
- HubSpot action list ready for Scott to approve?
- Whale Flag status confirmed or flagged as unknown?
