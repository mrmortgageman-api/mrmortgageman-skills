---
name: cowork-session-closer
description: >
  Close out a Claude Code cowork session cleanly. Captures decisions made, tasks opened,
  tasks closed, open items carried forward, and any cross-system writes that need to happen.
  Use at the end of every cowork session. Outputs a structured session log and a next-session
  boot queue so nothing falls through.
triggers:
  - "close the session"
  - "wrap up"
  - "end of session"
  - "session closer"
  - "write the session log"
  - "what did we do today"
  - "capture session decisions"
  - "close out"
related_skills:
  - cowork-queue-manager (use to update the queue before closing)
  - open-decisions-manager (use to log any decisions made or deferred)
  - context-stack-refresher (use at next session start to reload this log)
  - notion-mirror-gatekeeper (use if session output needs to write to Notion)
---

# Cowork Session Closer

## Purpose

Every session has a beginning and an end.
This skill handles the end: what was done, what is open, and what needs to happen before next time.

---

## Session Close Protocol

Run these steps in order at the end of every cowork session.

Step 1: Decisions log
List every decision made during the session.
Format: [Topic] — [Decision] — [Owner] — [Due]

Step 2: Tasks closed
List every task completed during the session.
Format: [Task name] — [System updated] — [Done by]

Step 3: Tasks opened
List every new task created during the session.
Format: [Task name] — [Owner] — [Due] — [Priority: High / Medium / Low]

Step 4: Open items carried forward
List anything that was raised but not resolved.
Format: [Item] — [Why deferred] — [Next session action]

Step 5: Cross-system writes needed
List any updates that need to happen in HubSpot, Notion, or GitHub before next session.
Scott must approve all cross-system writes.
Format: [System] — [What to write] — [Approved by Scott: Y / N]

Step 6: Next-session boot queue
List the first 3 items to load at the start of the next session.
Format: [Priority] — [Item] — [Context needed]

---

## Session Log Output Format

Session: [Date]
Duration: [Approximate]
Participants: Scott Thompson + Claude Code

### Decisions
[Decisions log]

### Tasks closed
[Tasks closed]

### Tasks opened
[Tasks opened]

### Carried forward
[Open items]

### Cross-system writes
[Pending writes — awaiting Scott approval]

### Next session boot queue
1. [Highest priority item]
2. [Second priority item]
3. [Third priority item]

---

## Hard Rules

- Do not mark a task as closed unless the work is confirmed done, not just started.
- Every open item needs a next-session action. Vague deferrals are not allowed.
- Cross-system writes are not executed by Claude. They go on the approval list for Scott.
- The next-session boot queue must have exactly 3 items. Not 2, not 5.

---

## Quality Check Before Delivering Session Log

- Every decision has an owner?
- Every task has a status: closed or carried forward?
- Cross-system write list is complete and waiting for Scott?
- Next-session queue is ready to paste into context-stack-refresher?
