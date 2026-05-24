---
name: archive-triage-decay-rater
description: >
  Score archived content, campaigns, and Notion pages by how stale, irrelevant, or
  misleading they have become. Use when cleaning up a workspace, auditing a content library,
  or deciding whether old material can be revived or must be deleted. Outputs a decay score
  and a recommended action for each item reviewed.
triggers:
  - "is this still relevant"
  - "rate this archive"
  - "decay check"
  - "audit old content"
  - "should we keep this"
  - "clean up the vault"
  - "triage the archive"
  - "how stale is this"
related_skills:
  - source-of-truth-registry-auditor (use to confirm which system the archive lives in)
  - notion-mirror-gatekeeper (use if archive purge touches Notion)
  - cowork-session-closer (log archive decisions in session log)
  - open-decisions-manager (escalate borderline items as open decisions)
---

# Archive Triage Decay Rater

## Purpose

Old content does not die on its own. It sits in a folder, gets referenced by mistake,
and causes confusion. This skill forces a decay verdict on every item reviewed.

---

## Decay Scoring System

Score each archived item on three dimensions. Total score determines the action.

### Accuracy (0-3)
3 — Fully accurate, could be used today
2 — Minor updates needed (rates, dates, brand refresh)
1 — Significant updates needed (strategy shift, new audience, new product)
0 — Wrong or misleading. Cannot be fixed with edits.

### Relevance (0-3)
3 — Directly relevant to current campaigns or workflows
2 — Adjacent — could be relevant with a new angle
1 — Tangentially relevant — would require a full rewrite to be useful
0 — No longer relevant to any active initiative

### Reusability (0-3)
3 — Can be used as-is or with minor copy edits
2 — Can be templated or stripped for structure
1 — Salvageable only for research or reference
0 — No reusable value

Total score (0-9):
8-9 — Archive but keep. Low decay. Review again in 90 days.
5-7 — Conditional keep. Needs a refresh before next use. Assign owner.
3-4 — High decay. Retire unless Scott sees a specific near-term use.
0-2 — Delete. Do not carry this forward.

---

## Decay Report Format

For each item reviewed:

Item: [File name or page title]
System: [Where it lives]
Last modified: [Date]
Accuracy score: [0-3]
Relevance score: [0-3]
Reusability score: [0-3]
Total decay score: [0-9]
Verdict: [Archive / Refresh / Retire / Delete]
Owner if refresh: [Name or Unassigned]
Notes: [One-line explanation of the rating]

---

## Hard Rules

- No item gets "keep as-is" unless it scores 8 or 9. Anything lower gets an action.
- Delete verdicts require Scott approval before execution.
- Do not refresh an item during a triage session. Rate it, assign it, move on.
- Rate each item independently. Do not let one good piece inflate the score of related weak items.
- Brand voice decay is automatic if product-marketing-context.md has been updated since the item was created.

---

## Quality Check Before Delivering Decay Report

- Every item has a numeric score, not just a description?
- Every item with a score below 8 has an assigned action?
- Delete verdicts are flagged for Scott approval?
- Refresh items have an owner and a rough timeline?
