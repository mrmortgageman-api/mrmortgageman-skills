---
name: pending-review-router
description: "Reviews items staged in PENDING_REVIEW and tells Scott where they belong, what approval is required, and what risk level they carry. Claude may not move, rename, publish, send, delete, or promote staged items without explicit Scott approval."
---

# Skill: pending-review-router

## Purpose

Route staged Cowork outputs safely. Reviews items in PENDING_REVIEW and produces a routing card.

PENDING_REVIEW is the video review booth. Nothing leaves it without Scott approval.

## When to Activate

- "review pending"
- "route pending review"
- "where does this go?"
- "what needs approval?"

## Routing Categories

Governance, Skill file, SignalStrike, CRM, Rate Rocket, Marketing asset, Client file, Agent partner file, Scenario / pricing, Archive triage, Session log, Technical / GitHub, Unknown

## Risk Levels

- LOW, MEDIUM, HIGH, BLOCKED

## Approval Always Required For

- Moving a file out of PENDING_REVIEW
- Publishing or sending content
- Updating CRM fields
- Creating or replacing canonical documents
- Any external-facing communication

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## Final Rule

PENDING_REVIEW protects the system. This skill routes the ball, but Scott decides when it leaves the box.
