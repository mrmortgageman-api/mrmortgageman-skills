---
name: crm-notion-file-sync-checker
description: >
  Verify that HubSpot CRM records and their Notion mirror pages are in sync. Use when a
  contact, deal, or company record may have been updated in one system but not the other,
  or when Scott suspects the Notion mirror is stale. Outputs a sync status report with a
  per-record conflict list and a recommended resolution for each mismatch.
triggers:
  - "check CRM sync"
  - "is Notion up to date"
  - "sync check"
  - "HubSpot Notion sync"
  - "mirror is out of date"
  - "CRM discrepancy"
  - "contact mismatch"
  - "check if Notion matches HubSpot"
related_skills:
  - source-of-truth-registry-auditor (use to confirm HubSpot is authoritative before syncing)
  - notion-mirror-gatekeeper (use to execute approved writes to Notion after sync check)
  - revops (use to understand HubSpot lifecycle stages and field definitions)
  - open-decisions-manager (use if sync conflict requires a resolution decision)
---

# CRM Notion File Sync Checker

## Purpose

HubSpot is the source of truth for all contacts and deals. Notion mirrors are read-only.
When a mirror drifts, decisions get made on stale data. This skill finds the drift and
surfaces the fix before that happens.

---

## Sync Scope

This skill checks sync status for these record types:

| Record Type | HubSpot Authority | Notion Mirror |
|---|---|---|
| Contacts | Contact record (all fields) | Notion contact page |
| Deals | Deal record and stage | Notion deal tracker page |
| Companies | Company record | Notion company page |
| SignalStrike scores | Custom contact property | Notion scouting log |
| Lifecycle stage | Contact property | Notion pipeline view |

---

## Sync Check Protocol

Step 1: Identify the records to check. Get from Scott or pull from a list.
Step 2: Read the HubSpot record for each contact or deal.
Step 3: Read the corresponding Notion page.
Step 4: Compare field by field on the fields listed in the sync scope below.
Step 5: Flag any field where HubSpot and Notion show different values.
Step 6: Output the sync status report.
Step 7: Get Scott's approval before writing any updates to Notion.

---

## Fields to Compare (Contacts)

- First name and last name
- Email address
- Phone number
- Brokerage or company name
- Lifecycle stage
- SignalStrike score
- Whale Flag status
- Last outreach date
- Last reply date
- Touch sequence position (Touch 0 / 1 / 2 / 3 / Done)

---

## Fields to Compare (Deals)

- Deal name
- Associated contact
- Deal stage
- Close date
- Loan amount
- Property address (if logged)
- Last activity date

---

## Sync Status Report Format

Sync check run: [Date and time]
Records checked: [Count]

For each mismatch:

Record: [Contact or Deal name]
Record type: [Contact / Deal / Company]
HubSpot ID: [ID]
Field in conflict: [Field name]
HubSpot value: [Value]
Notion value: [Value]
Last updated (HubSpot): [Date]
Last updated (Notion): [Date]
Resolution: [Overwrite Notion with HubSpot value — pending Scott approval]

Overall sync status: [In sync / N mismatches found / Critical mismatch — do not use Notion data]

---

## Hard Rules

- HubSpot always wins. Notion is never the source of truth for any field.
- Do not write to Notion without Scott's explicit approval.
- A mismatch on lifecycle stage or SignalStrike score is a Critical flag. Pause and confirm before proceeding with any outreach that depends on these fields.
- Do not batch-overwrite Notion records. Resolve one at a time with Scott's approval.
- If Notion shows a higher lifecycle stage than HubSpot, this is a data integrity issue. Flag immediately.

---

## Quality Check Before Delivering Sync Report

- Every mismatch has both the HubSpot and Notion values shown?
- Critical mismatches on lifecycle stage and score are flagged separately?
- No Notion writes queued without Scott approval notation?
- Record count matches the input list?
