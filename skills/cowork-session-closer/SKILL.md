---
name: cowork-session-closer
version: 1
description: Closes every Claude Cowork session cleanly. Generates a session summary card and determines whether a Notion mirror is required.
agents: [claude_cowork]
trigger_phrases:
  - "close the session"
  - "wrap up"
  - "session done"
  - "end session"
  - "log this session"
---

# Skill: cowork-session-closer

## Purpose

Close every Claude Cowork session cleanly. Produces a Session Close Card, identifies loose ends, and determines whether the session must be mirrored into Notion.

## When to Activate

- At the end of any Claude Cowork session
- When Scott says "close the session", "wrap up", "session done", "end session"

## Output: Session Close Card

Required fields:
- Session Type
- Files Touched
- Decisions Made
- Open Decisions Added
- Pending Review Items
- Batons Issued
- Next First Move
- Notion Mirror Required? YES/NO
- Session Status: CLEAN CLOSE or OPEN ITEMS REMAIN

## Notion Mirror Required When

- Governance decision made
- System architecture changed
- Canonical file created or updated
- Council decision recorded
- New workflow approved
- Integration changed

## Final Rule

A session is not cleanly closed unless the next first move is clear.
