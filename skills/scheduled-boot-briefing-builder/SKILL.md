---
name: scheduled-boot-briefing-builder
description: "Builds a morning or session-start briefing for Claude Cowork by reading the approved boot stack, context files, queue, open decisions, and pending review items. Claude may brief and recommend only."
---

# Skill: scheduled-boot-briefing-builder

## Purpose

Build a clean Cowork briefing at the start of the day or work session.

Turns the boot stack into a short operational brief. Does not execute the queue, update CRM, move files, or resolve open decisions.

## When to Activate

- "morning briefing"
- "boot briefing"
- "start Cowork"
- "what should I know today?"
- "what is the first move?"

## Required Source Checks

1. SYSTEM_SOURCE_OF_TRUTH_REGISTRY_CURRENT
2. MMM_SYSTEM_ARCHITECTURE_MAP_CURRENT
3. AI_COUNCIL_OPERATING_MODEL_CURRENT
4. Latest SESSION log
5. SCOTT_TODAY.md
6. OPEN_DECISIONS.md
7. QUEUE.md
8. PENDING_REVIEW
9. ACTIVE_DEALS_SNAPSHOT.md (if CRM work)
10. CRM_TRANSITION_RULE_CURRENT

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## Final Rule

The boot briefing is the pregame team talk. It sets shape, tempo, and first move. It does not play the match for Scott.
