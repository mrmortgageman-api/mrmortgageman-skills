---
name: notion-mirror-gatekeeper
description: "Determines whether a Claude Cowork session log or output should be mirrored into Notion. Prevents Notion clutter while protecting governance-grade decisions. Claude may recommend mirroring only."
---

# Skill: notion-mirror-gatekeeper

## Purpose

Decide whether a Claude Cowork session or output belongs in Notion.

Notion is the governance and strategic memory layer, not a dumping ground.

## Mirror Decision Types

- NOTION MIRROR REQUIRED
- DRIVE LOG ONLY
- OPEN DECISION ENTRY NEEDED
- NOTION JOURNAL ENTRY NEEDED
- DO NOT LOG
- NEEDS SCOTT REVIEW

## Notion Mirror Required When

- Governance decision made
- System architecture changed
- Canonical file created, updated, renamed, or proposed
- Council decision recorded
- New workflow approved
- Integration changed
- Skill installed, updated, or retired
- SignalStrike or Rate Rocket operating rule changed

## Drive Log Only When

- Routine drafting, internal brainstorming, queue review with no decision, execution-only work with no system change

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## Final Rule

Notion is the memory that matters. Do not clutter it, and do not skip it when the system changed.
