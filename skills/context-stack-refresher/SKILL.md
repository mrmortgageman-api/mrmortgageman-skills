---
name: context-stack-refresher
description: "Reviews and refreshes the Claude Cowork context stack so every session starts with the right priorities, open decisions, queue status, pending review items, and CRM-neutral operating context."
---

# Skill: context-stack-refresher

## Purpose

Keep Claude Cowork oriented. Reviews the Cowork context stack and produces a refresh report.

## When to Activate

- "refresh context"
- "check the context stack"
- "start Cowork"
- "boot sequence"
- "what is current?"
- "where did we leave off?"

## Context Stack Files

- SCOTT_TODAY.md
- OPEN_DECISIONS.md
- ACTIVE_DEALS_SNAPSHOT.md
- QUEUE.md
- PENDING_REVIEW
- SESSION_LOGS
- CLAUDE_CALIBRATION.md
- CRM_TRANSITION_RULE_CURRENT_2026-05-02.md

## Freshness Ratings

- CURRENT — up to date
- STALE — outdated or inconsistent
- MISSING — unavailable
- NOT NEEDED — not relevant
- NEEDS SCOTT — requires Scott input

## CRM Transition Rule

CRM is the role. HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## What Claude May Not Do

- Rewrite SCOTT_TODAY.md without Scott approval
- Remove items from OPEN_DECISIONS.md
- Mark decisions resolved
- Mark queue items complete
- Override CLAUDE_CALIBRATION.md

## Final Rule

Context first, action second.
