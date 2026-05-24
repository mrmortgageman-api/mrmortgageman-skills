---
name: open-decisions-manager
description: >
  Track, surface, and force resolution on open decisions across the MrMortgageMan operation.
  Use when decisions are being deferred, when Scott needs a clean view of what is unresolved,
  or when a session produces new choices that need to be logged. Outputs a prioritized open
  decisions list with a recommended resolution path for each.
triggers:
  - "what decisions are open"
  - "log this decision"
  - "defer this"
  - "open decisions"
  - "unresolved items"
  - "decision log"
  - "what do we still need to decide"
  - "force a decision"
related_skills:
  - cowork-session-closer (use at end of session to capture new open decisions)
  - cowork-queue-manager (use to prioritize which open decisions hit the next session queue)
  - source-of-truth-registry-auditor (use when a decision involves system ownership)
  - notion-mirror-gatekeeper (use if decision is logged in Notion)
---

# Open Decisions Manager

## Purpose

Deferred decisions create drag. This skill makes every open decision visible,
assigns it an owner, and gives it a deadline or a forcing function.

---

## Decision States

Every decision lives in one of these states:

Open — Not yet decided. Active or queued.
Deferred — Deliberately delayed. Has a trigger condition or a date.
Decided — Resolution is confirmed. Logged for reference.
Escalated — Needs Scott's explicit input before it can move.

---

## Open Decision Log Format

For each open decision, capture:

Decision ID: [Sequential number, e.g. D-001]
Topic: [One line, plain language]
State: [Open / Deferred / Decided / Escalated]
Context: [Why this came up. One or two sentences max.]
Options on the table:
  A — [Option A]
  B — [Option B]
  C — [Other, if applicable]
Recommended path: [Claude's recommendation with one-line rationale]
Owner: [Scott / Name / TBD]
Due: [Date or trigger condition]
Blockers: [What is preventing resolution, if anything]

---

## Session Decision Capture Protocol

When a decision is made during a cowork session:

1. Record the decision in the log above.
2. Change state from Open to Decided.
3. Note who made the call and when.
4. If the decision triggers a cross-system write, flag it for Scott's approval.
5. Add it to the cowork-session-closer output under Decisions.

When a decision is deferred:

1. Record why it was deferred. A reason is required. "Not sure yet" is not a reason.
2. Set a trigger condition or a hard date. Open-ended deferrals are not allowed.
3. Add it to the next session boot queue if it is time-sensitive.

---

## Prioritization Rules

Priority 1 — Escalate immediately:
- Decision is blocking active campaign or live deal
- Decision involves a cross-system write to a system Scott owns
- Decision has been deferred more than twice

Priority 2 — Queue for next session:
- Decision affects workflow or process but nothing is actively blocked
- Decision involves a third-party vendor or integration

Priority 3 — Log and monitor:
- Decision is strategic but not urgent
- Decision depends on external information not yet available

---

## Hard Rules

- Every open decision needs an owner. Unowned decisions do not get resolved.
- No decision can be deferred without a trigger condition or a date.
- Decisions deferred more than twice are automatically escalated to Scott.
- Decided decisions are never deleted. They are logged in state Decided.
- Claude recommends but Scott decides. Do not mark a decision as Decided unless Scott confirmed.

---

## Quality Check Before Delivering Decision List

- Every open decision has an owner?
- Every deferral has a trigger condition or date?
- Decisions deferred twice or more are escalated?
- Decided decisions include who made the call?
