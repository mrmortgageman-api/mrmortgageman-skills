---
name: signalstrike-scouting-report
version: 1
description: Converts SignalStrike observations into a ranked scouting report. Helps Scott turn live agent signals into journal-ready intelligence, next-action recommendations, and follow-up angles. Does not send outreach, update CRM fields, change relationship tiers, or bypass Notion journaling.
---

# Skill: signalstrike-scouting-report

## Purpose

Convert raw SignalStrike observations into a ranked scouting report.

Minimum viable operating loop:
1. Observe signal
2. Capture in Notion
3. Classify signal
4. Rank opportunity
5. Recommend next action
6. Scott approves
7. Log result

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## When to Activate

- "SignalStrike scouting report"
- "rank these agent signals"
- "who should I follow up with?"
- "build the SignalStrike report"

## Signal Quality Ratings

- HIGH, MEDIUM, LOW, NEEDS CONTEXT

## Relationship Lane

Active Partner, Warm Relationship, Target Agent, Whale / High-Value Prospect, New Contact, Dormant Relationship, Watchlist, Do Not Touch Yet, Needs Research

Do not declare Whale unless Scott provides evidence or explicitly approves.

## Guardrails

Claude may summarize signals, rank agents, identify relationship lane, recommend next touch, flag CRM update needed, and create Notion journal-ready entries.

Claude may not send outreach, log CRM activity, update CRM fields, change relationship tier, or declare Whale status without Scott approval.

## Final Rule

SignalStrike is live before it is perfect. Capture the signal, read the field, recommend the next pass, keep the journal clean. Scott decides the play.
