---
name: tca-apex-session-start
description: TCA APEX session boot loader. Use this skill at the start of any TCA APEX session, or whenever Scott says "start TCA session", "load the brief", "begin TCA work", "boot up TCA", "what's the current TCA state", or any phrase indicating a new TCA APEX working session is beginning. Also trigger when Scott asks what sprint we're on, what's locked, or what's blocked in TCA. This skill loads TCA_APEX_BRIEF_CURRENT from Notion before any TCA work begins. If the Brief is unavailable, stale, or missing required sections, it stops and reports to Scott — it does not proceed from memory or old chat context.
---

# TCA APEX Session Boot Loader

## Purpose

This skill is the on-ramp for every TCA APEX working session. Its one job is to load TCA_APEX_BRIEF_CURRENT before any TCA work begins, verify it is complete and current, and report the session state to Scott.

The Brief is the session boot file. The full manual is in the Brain. This skill loads the boot file and confirms the session is ready to execute.

**Governing law:** No session begins without a loaded Brief. Do not proceed from memory. Do not proceed from old chat context. Do not proceed from partial documents.

---

## BRIEF LOCATION

**TCA_APEX_BRIEF_CURRENT:**
- Notion URL: https://app.notion.com/p/3843a2b0c9da817dbaefe9e330883c79
- Notion page ID: 3843a2b0-c9da-817d-baef-e9e330883c79

---

## EXECUTION SEQUENCE

### Step 1 — Load the Brief

Fetch TCA_APEX_BRIEF_CURRENT from Notion using the available Notion MCP tool.

If the page cannot be fetched:
- Stop immediately
- Report: "TCA_APEX_BRIEF_CURRENT could not be loaded from Notion. Do not proceed. Verify Notion connection and try again."
- Do not attempt to work from memory or reconstruct the Brief from prior context

### Step 2 — Verify Brief completeness

Check that the loaded Brief contains all 8 required sections:

1. Current governing doctrine (with links)
2. Source-of-truth hierarchy
3. Execution rules
4. Role authority table
5. Current validation files
6. Current lock blockers
7. Do not build / do not expand rules
8. Current sprint status

If any section is missing:
- Stop
- Report which sections are missing
- Tell Scott: "The Brief is incomplete. Update TCA_APEX_BRIEF_CURRENT before proceeding."
- Do not attempt to fill in missing sections from memory

### Step 3 — Check for staleness

The Brief is considered potentially stale if:
- The "Last updated" date is more than 14 days ago
- The current sprint status date has passed without a gate update
- Any doctrine change has occurred in this session that is not yet reflected in the Brief

If stale signals are detected:
- Flag them: "The Brief may be stale. [Specific signal]. Consider updating before proceeding."
- This is a warning, not a hard stop — Scott decides whether to proceed

### Step 4 — Report session state

Deliver a clean session opening report:

```
TCA APEX SESSION OPEN
─────────────────────────────────────
Brief loaded: TCA_APEX_BRIEF_CURRENT [date]
Brief status: [CURRENT / POTENTIALLY STALE — reason]

CURRENT SPRINT
[Sprint name and status]
[Gate status]
[Active branch and file]

LOCK BLOCKERS
[List, or "None"]

DO NOT TOUCH
[Key items]

ROLE AUTHORITY
[Compact role table]

READY TO PROCEED: [Yes / No — reason if No]
─────────────────────────────────────
```

### Step 5 — Await instruction

After delivering the session report, wait for Scott's direction. Do not begin building, retrieving, or planning until Scott gives a specific instruction.

---

## FAILURE MODES

| Failure | Response |
|---|---|
| Notion not connected | Stop. Report. Do not proceed. |
| Brief page not found | Stop. Report. Do not proceed. |
| Brief missing required sections | Stop. List missing sections. Do not proceed. |
| Brief is stale | Warn. Flag the signal. Scott decides. |

The failure rule: It is always better to stop and report than to proceed on stale or incomplete information.

---

## BRIEF MAINTENANCE REMINDER (Chief of Staff duty)

At session close, if any of the following occurred, update TCA_APEX_BRIEF_CURRENT before closing:
- Doctrine change
- Execution rule change
- Role change
- Validation finding
- Lock blocker resolved or added
- Sprint status change

**Governing law:** No session closes with a stale Brief.

---

## QUICK REFERENCE

| Item | Value |
|---|---|
| Brief URL | https://app.notion.com/p/3843a2b0c9da817dbaefe9e330883c79 |
| Brain URL | https://app.notion.com/p/3843a2b0c9da81029dfde40c01457008 |
| Doctrine URL | https://app.notion.com/p/3843a2b0c9da817ba93bc7e897c50eb6 |
| COS Authority | https://app.notion.com/p/3843a2b0c9da8194b4d3db6397db6f82 |
| Authority Structure | https://app.notion.com/p/3843a2b0c9da81bbab8ee4a3eca272cd |