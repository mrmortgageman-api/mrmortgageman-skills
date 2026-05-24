---
name: source-of-truth-registry-auditor
description: >
  Audit which system owns which data type across the MrMortgageMan stack and flag any
  conflicts, gaps, or orphaned records. Use when Scott suspects a system is out of sync,
  a new integration was added, or a team member is writing to the wrong place.
  Outputs a ranked conflict list with recommended resolution for each gap.
triggers:
  - "which system owns this"
  - "is this in HubSpot or Notion"
  - "source of truth audit"
  - "registry check"
  - "where should this live"
  - "data ownership review"
  - "find the authoritative source"
related_skills:
  - product-marketing-context (read first — defines which systems are in the stack)
  - crm-notion-file-sync-checker (use after audit to validate sync status)
  - notion-mirror-gatekeeper (use to enforce ownership decisions)
  - github-repository-registry-builder (use when repo ownership is in question)
---

# Source of Truth Registry Auditor

## Purpose

One system owns each data type. When multiple systems hold the same data, drift happens.
This skill audits the current ownership map and surfaces conflicts before they cause a bad sync.

---

## System Ownership Map (Default State)

| Data Type | Authoritative System | Mirror / Read Replica |
|---|---|---|
| Contacts and leads | HubSpot CRM | Notion (read-only mirror) |
| Deals and pipeline stages | HubSpot CRM | None |
| Skill files | GitHub (mrmortgageman-skills) | Claude Code session |
| Meeting notes and decisions | Notion | None |
| Campaign briefs | Notion | None |
| Email templates | HubSpot | None |
| Brand voice and positioning | skills/product-marketing-context.md | Notion summary page |
| SignalStrike scores | HubSpot (custom property) | Notion scouting log |
| Repository registry | GitHub org (mrmortgageman-api) | Notion dev index |
| Open decisions | Notion (Open Decisions database) | None |

---

## Audit Protocol

Step 1: Identify the data type in question.
Step 2: Match against the ownership map above.
Step 3: Check whether a write has occurred in the wrong system.
Step 4: Flag any system that holds a stale or conflicting copy.
Step 5: Output the conflict report below.

---

## Conflict Report Format

For each conflict found, output:

Data type: [name]
Authoritative system: [system]
Conflicting copy found in: [system]
Last modified (authoritative): [date if known]
Last modified (conflict): [date if known]
Resolution: [delete / overwrite / merge / escalate to Scott]
Urgency: [High / Medium / Low]

---

## Hard Rules

- Scott approves all cross-system writes. Never write to a mirror without confirmation.
- HubSpot is always authoritative for contacts and deals. No exceptions.
- GitHub is always authoritative for skill files. Notion copies are for reference only.
- If two systems show different values for the same contact field, HubSpot wins.
- Do not delete records from any system without Scott's explicit approval.

---

## Quality Check Before Delivering Audit

- Every data type has exactly one authoritative system named?
- Every conflict has a resolution recommendation?
- Nothing marked as authoritative that is actually a mirror?
- Scott can action this list without additional context?
