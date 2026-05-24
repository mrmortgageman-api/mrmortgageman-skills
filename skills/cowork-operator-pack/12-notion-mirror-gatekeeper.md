---
name: notion-mirror-gatekeeper
description: >
  Gate all writes to Notion mirror pages to prevent unauthorized or unreviewed updates from
  overwriting authoritative data. Use any time Claude is about to write to a Notion page
  that mirrors a HubSpot record, a skill file, or another authoritative source. Forces
  a confirmation checkpoint and ensures every Notion write is logged and traceable.
triggers:
  - "write to Notion"
  - "update Notion"
  - "Notion write"
  - "mirror update"
  - "push to Notion"
  - "sync to Notion"
  - "create a Notion page"
  - "gatekeeper check"
related_skills:
  - source-of-truth-registry-auditor (confirms which system is authoritative before any write)
  - crm-notion-file-sync-checker (use before write to understand current sync state)
  - open-decisions-manager (log any write decision that requires Scott's sign-off)
  - cowork-session-closer (log all approved Notion writes in session log)
---

# Notion Mirror Gatekeeper

## Purpose

Notion holds mirrors, not originals. A write to a Notion mirror that contradicts HubSpot
or a skill file creates drift that is hard to find and expensive to fix.
This skill forces a checkpoint before any Notion write executes.

---

## Write Classification

Before any Notion write, classify the write type:

Type A — New page creation
A new Notion page that does not correspond to an existing record in an authoritative system.
Requires: Scott approval if the page will be referenced by other systems or workflows.

Type B — Mirror update
A write to a Notion page that mirrors a HubSpot contact, deal, or company record.
Requires: Scott approval always. HubSpot value must be confirmed as the source before overwriting.

Type C — Standalone content
A write to a Notion page that contains original content not mirrored from another system
(meeting notes, campaign briefs, session logs, open decisions).
Requires: Scott approval if the page is shared with external collaborators or feeds an automation.

Type D — Structural change
Adding, removing, or renaming a Notion database, view, or property.
Requires: Scott approval always.

---

## Gatekeeper Checkpoint Protocol

Step 1: Identify the write type (A, B, C, or D).
Step 2: If Type B or D, stop. Do not proceed without Scott's explicit approval.
Step 3: If Type A or C, assess whether the page feeds an automation or is shared externally.
        If yes, stop and get Scott's approval. If no, proceed with standard logging.
Step 4: Confirm the authoritative source for any data being written.
Step 5: Log the write in the pending write log below.
Step 6: Execute the write only after approval is confirmed.
Step 7: Log the execution in the session log.

---

## Pending Write Log Format

For each pending Notion write:

Write ID: [Sequential number, e.g. NW-001]
Type: [A / B / C / D]
Target page: [Notion page name and URL if known]
Data source: [HubSpot / GitHub / Session log / Scott ad hoc]
Content to write: [Summary — what changes]
Authoritative value confirmed: [Yes / No — if No, do not proceed]
Scott approval: [Pending / Approved — [date] / Rejected]
Executed: [Yes — [date and time] / No]

---

## Post-Write Log Format

After a write is executed:

Write ID: [NW-XXX]
Executed: [Date and time]
Written by: Claude Code
Approved by: Scott Thompson on [date]
Pages affected: [List]
HubSpot sync status after write: [In sync / Not applicable / Pending verification]

---

## Hard Rules

- Never write to a Notion mirror before confirming the authoritative system value.
- Type B and Type D writes require Scott's approval. No exceptions.
- Batch writes (updating more than 3 Notion pages at once) are treated as Type D regardless of content type. Each page needs individual approval.
- If a write fails partway through, stop immediately. Do not retry without Scott's awareness.
- All Notion writes are logged. Nothing executes off the record.

---

## Quality Check Before Executing Any Notion Write

- Write classified as Type A, B, C, or D?
- Type B and D writes have explicit Scott approval with date?
- Authoritative source value confirmed before any mirror update?
- Write is logged in the pending write log with an ID?
