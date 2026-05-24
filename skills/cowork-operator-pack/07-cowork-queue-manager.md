---
name: cowork-queue-manager
description: >
  Build, prioritize, and maintain the active queue for a cowork session. Use at the start
  of a session to load what needs to get done, during a session to triage new items as they
  surface, and before closing to hand off unfinished work. Outputs a ranked, time-boxed
  session queue that Scott can execute against without re-sorting.
triggers:
  - "build the queue"
  - "what are we working on today"
  - "session queue"
  - "prioritize these tasks"
  - "queue manager"
  - "load the queue"
  - "what should we tackle first"
  - "time-box this session"
related_skills:
  - context-stack-refresher (use to load prior session context before building the queue)
  - cowork-session-closer (use at end of session to capture what the queue produced)
  - pending-review-router (use to import pending items into the queue)
  - open-decisions-manager (use to import open decisions into the queue)
  - scheduled-boot-briefing-builder (use to pull queue from a pre-built boot briefing)
---

# Cowork Queue Manager

## Purpose

A session without a queue is a brainstorm. This skill turns a pile of tasks and open items
into a ranked, time-boxed list that keeps Scott and Claude working on the right thing
in the right order.

---

## Queue Item Format

For each queue item:

Queue position: [1, 2, 3...]
Item: [One-line description]
Type: [Task / Decision / Review / Research / Write]
Source: [Where this came from — prior session, Notion, HubSpot, Scott ad hoc]
Priority: [P1 / P2 / P3]
Estimated time: [In minutes]
Skill needed: [Skill name or None]
Blocker: [What must be true before this can start, or None]

---

## Priority Definitions

P1 — Must happen this session. Blocking something live or has an external deadline.
P2 — Should happen this session. High value but not blocking.
P3 — Nice to do this session. Will carry forward if time runs out.

---

## Queue Build Protocol

Step 1: Pull context from the prior session log (use context-stack-refresher if available).
Step 2: Pull open decisions from open-decisions-manager.
Step 3: Pull pending items from pending-review-router.
Step 4: Add any new items Scott raises at session start.
Step 5: Assign priorities using the definitions above.
Step 6: Estimate time for each item.
Step 7: Sort by P1 first, then P2, then P3.
Step 8: Check total estimated time against available session time.
Step 9: If over budget, move P3 items to the carry-forward list.
Step 10: Confirm queue with Scott before starting work.

---

## Mid-Session Triage Protocol

When a new item surfaces mid-session:

1. Assign a priority immediately.
2. If P1: pause current item, add to queue at position 1 or 2.
3. If P2: add to queue after current P1 items.
4. If P3: add to the carry-forward list, do not interrupt current flow.

Do not let mid-session items derail the P1 work without Scott's explicit decision to reprioritize.

---

## Carry-Forward Format

At the end of the session, output a carry-forward list for the session closer:

Carry-forward item: [Description]
Original priority: [P1 / P2 / P3]
Reason not completed: [Time / Blocker / Deprioritized]
Recommended position in next session: [Early / Mid / End]

---

## Hard Rules

- P1 items go before P2. Always. No exceptions during queue build.
- Never add more than 6 P1 items to a single session queue. If everything is P1, nothing is.
- Time estimates are required for every item. If unknown, default to 20 minutes and note the estimate.
- Carry-forward items are not failures. They are the next session's starting point.
- Scott confirms the queue before work begins. Do not start P1 items without confirmation.

---

## Quality Check Before Starting Session

- Queue is sorted P1, P2, P3?
- Total estimated time calculated and compared to available session time?
- P3 items are in carry-forward if time is over budget?
- Scott has confirmed the queue?
