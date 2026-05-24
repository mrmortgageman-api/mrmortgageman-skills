---
name: context-stack-refresher
description: >
  Reload the operating context at the start of a new session or after a long gap. Reads the
  prior session log, open decisions, and queue carry-forwards, then rebuilds the working
  context stack so Claude can continue without repeating ground that was already covered.
  Use at the start of every session that follows a prior cowork session.
triggers:
  - "refresh context"
  - "reload the session"
  - "what did we cover last time"
  - "pick up where we left off"
  - "context stack"
  - "catch me up"
  - "boot context"
  - "reload prior session"
related_skills:
  - cowork-session-closer (source of the session log this skill reads)
  - cowork-queue-manager (use after refresh to rebuild the session queue)
  - open-decisions-manager (use to reload open decisions into the current session)
  - scheduled-boot-briefing-builder (replaces this skill for scheduled boot workflows)
---

# Context Stack Refresher

## Purpose

Every new session starts cold. This skill warms it up by loading what matters from the prior
session without requiring Scott to re-explain the full situation.

---

## Context Stack Components

The context stack has four layers. Load them in order.

Layer 1 — Prior session summary
Source: cowork-session-closer output from the last session.
Load: Decisions made, tasks closed, tasks opened, carried-forward items.

Layer 2 — Open decisions
Source: open-decisions-manager current log.
Load: All decisions in Open or Deferred state with their owners and due dates.

Layer 3 — Queue carry-forwards
Source: cowork-queue-manager carry-forward list from the last session.
Load: All items that did not complete in the last session, in their carry-forward priority order.

Layer 4 — System health context
Source: mcp-health-check last report.
Load: Any tools that were Degraded or Failed in the prior session. Note if they were recovered.

---

## Context Load Protocol

Step 1: Ask Scott for the prior session log if it is not already in the conversation.
Step 2: Parse the session log for Layer 1 content.
Step 3: Pull open decisions from the open-decisions-manager for Layer 2.
Step 4: Pull carry-forwards from the cowork-queue-manager for Layer 3.
Step 5: Note any system health issues from the last mcp-health-check for Layer 4.
Step 6: Output the refreshed context stack summary below.
Step 7: Confirm with Scott that the context is accurate before starting session work.

---

## Refreshed Context Stack Output Format

Context stack loaded: [Date and time]
Prior session: [Date of last session]

### Layer 1 — Prior session summary
Decisions made:
[List]

Tasks closed:
[List]

Tasks opened and still pending:
[List]

### Layer 2 — Open decisions
[Prioritized list from open-decisions-manager, P1 decisions first]

### Layer 3 — Queue carry-forwards
[Carry-forward items in recommended next-session order]

### Layer 4 — System health context
[Any tools that were Degraded or Failed last session — status as of now if known]

### Recommended session start
Based on the above, the recommended first action for this session is:
[One sentence — specific next action, not a category]

---

## Hard Rules

- Do not start session work until Layer 1 through Layer 3 are loaded and confirmed.
- If the prior session log is unavailable, ask Scott to summarize the last 3 decisions and the current top priority before proceeding.
- Do not invent or assume carry-forwards. If the prior session log is missing, note the gap explicitly.
- The recommended session start is a single action, not a list. Force the choice.

---

## Quality Check Before Starting Session Work

- All four layers loaded or explicitly noted as unavailable?
- Open decisions with imminent due dates are surfaced in Layer 2?
- Recommended session start is specific and actionable?
- Scott has confirmed context is accurate?
