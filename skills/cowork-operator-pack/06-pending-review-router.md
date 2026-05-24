---
name: pending-review-router
description: >
  Route items that are waiting on review to the right owner, system, or next action.
  Use when a queue of pending items has built up and Scott needs to know what is waiting,
  who it is waiting on, and what the fastest path to resolution is. Outputs a sorted
  routing list with owner, deadline, and recommended action for each pending item.
triggers:
  - "what is pending review"
  - "route these items"
  - "pending queue"
  - "who needs to review this"
  - "what is waiting on me"
  - "review router"
  - "pending approvals"
  - "clear the review queue"
related_skills:
  - cowork-queue-manager (use to build the queue before routing)
  - open-decisions-manager (use if a pending item requires a decision before routing)
  - cowork-session-closer (capture routing actions in session log)
  - notion-mirror-gatekeeper (use if pending items involve a Notion write)
---

# Pending Review Router

## Purpose

Things pile up. This skill creates a clean routing list that tells Scott exactly what is
waiting, who owns it, and what to do next. No item leaves this skill without an owner
and an action.

---

## Pending Item States

Waiting on Scott — Needs Scott's explicit review or approval before moving.
Waiting on Claude — Claude needs to produce or revise something.
Waiting on system — Blocked by an integration, sync, or external process.
Waiting on third party — Blocked by a vendor, partner, or external contact.
Ready to close — Review is complete. Needs confirmation to mark done.

---

## Routing Report Format

For each pending item:

Item ID: [Sequential number, e.g. R-001]
Item: [One-line description]
State: [State from list above]
Owner: [Name or system]
Due: [Date or SLA window]
Blocked by: [What is preventing resolution, if anything]
Recommended action: [Specific next step — one sentence, actionable]
Priority: [High / Medium / Low]

---

## Routing Priority Rules

High — Blocks a live deal, active campaign, or a deliverable with an external deadline.
Medium — Affects workflow efficiency but nothing is immediately blocked.
Low — Can wait until next session without consequence.

Any item that has been in the pending queue for more than 7 days is automatically escalated to High,
regardless of original priority.

---

## Owner Assignment Rules

When assigning owners, use this hierarchy:

1. If the item requires a judgment call or approval, owner is Scott.
2. If the item requires content generation or analysis, owner is Claude.
3. If the item requires a system action (HubSpot update, Notion write, GitHub push), owner is Claude with Scott approval.
4. If the item requires a third-party response, owner is the third party with a follow-up date assigned to Scott.

Never leave owner as Unassigned. If the right owner is unclear, escalate to Scott.

---

## Batch Routing Protocol

When processing a full queue:

Step 1: List all pending items and assign states.
Step 2: Assign owners using the hierarchy above.
Step 3: Sort by priority (High first).
Step 4: Flag items that have been waiting more than 7 days.
Step 5: Identify any items that can be closed immediately (Ready to close state).
Step 6: Output routing report.
Step 7: Get Scott's approval on any items in Waiting on Scott state before proceeding.

---

## Hard Rules

- Every item gets an owner. No exceptions.
- Every item over 7 days old is flagged as High priority regardless of original priority.
- Items in Waiting on Scott state cannot be moved by Claude without explicit approval.
- Do not close an item unless the work is confirmed complete by the owner.
- Routing is not resolving. This skill sorts and assigns. It does not execute.

---

## Quality Check Before Delivering Routing Report

- Every item has an owner and a priority?
- Items over 7 days are flagged High?
- Items in Waiting on Scott state are clearly separated from Claude-owned items?
- Ready to close items are identified so Scott can approve closure?
