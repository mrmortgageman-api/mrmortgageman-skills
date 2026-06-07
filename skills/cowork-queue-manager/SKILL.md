---
name: cowork-queue-manager
description: "Reviews QUEUE.md, classifies each task by action lane, and tells Scott what Claude can prepare versus what requires approval. Claude may not complete, send, move, rename, delete, publish, or update CRM records from the queue without explicit Scott approval."
---

# Skill: cowork-queue-manager

## Purpose

Manage the Claude Cowork task queue safely. Reviews QUEUE.md and classifies queued tasks.

## When to Activate

- "check the queue"
- "work the queue"
- "what is safe to work on?"
- "what needs approval?"
- "run the morning queue"

## Queue Labels

- AUTO — Claude may prepare internal-only work
- REVIEW — Claude may prepare but must pause for Scott review
- CLIENT — Requires Scott approval
- CRM — Requires Scott approval
- RATE ROCKET — Requires Scott approval
- SIGNALSTRIKE — Claude may classify, outreach requires approval
- SEND — Always requires Scott approval
- MOVE — Always requires Scott approval
- RENAME — Always requires Scott approval
- DELETE — Always requires Scott approval
- CANONICAL — Always requires Scott approval
- BLOCKED — Cannot safely classify

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## Queue Completion Rule

A queue item is not complete until output is staged in PENDING_REVIEW, Scott approves, item moves to OPEN_DECISIONS, item is marked BLOCKED, or item is deferred by Scott.

## Final Rule

The queue is the lineup card, not permission to shoot.
