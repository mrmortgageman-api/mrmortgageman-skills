---
name: open-decisions-manager
version: 1
description: Surfaces open decisions from OPEN_DECISIONS.md that have aged without resolution. Prevents drift by flagging stale items and prompting Scott for a decision. Claude may not resolve or close decisions without Scott approval.
---

# Skill: open-decisions-manager

## Purpose

Surface unresolved decisions from OPEN_DECISIONS.md before they become hidden drift.

## When to Activate

- "check open decisions"
- "what decisions are still open?"
- "what is aging?"
- "close the loop"

## Age Thresholds

- URGENT: 7+ days
- AGING: 3-6 days
- CURRENT: 0-2 days

## Guardrails

Claude may surface, summarize, and rank open decisions.

Claude may not mark any decision resolved, closed, or deferred without Scott approval.

## Escalation Rule

If there are 3+ URGENT items, recommend a dedicated decision-clearing session before new governance work begins.

## Final Rule

This skill manages visibility, not authority. Scott decides.
