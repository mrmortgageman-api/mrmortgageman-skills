---
name: source-of-truth-registry-auditor
version: 1
description: Before Claude acts on any file, doc, prompt, or system idea, this skill classifies it against the known source-of-truth registry. Output is a classification card only. Claude may not promote, rename, move, delete, or mark anything as superseded without explicit Scott approval.
agents: [claude_cowork]
trigger_phrases:
  - "Check if this is canonical"
  - "Can we promote this?"
  - "Is this still current?"
  - "Compare this against the registry"
  - "Should we use this?"
  - "Is this the right version?"
---

# Skill: source-of-truth-registry-auditor

## Purpose

Classify a candidate document, file, or action before Claude acts on it. Produces a classification card only.

## Authority Hierarchy

1. Notion: strategic truth
2. Google Drive: supporting docs, canonical only if registered in Notion
3. Claude context window: temporary only, never canonical

## Classification Card Output

Required fields:
- Candidate Item
- Claimed Purpose
- Current Authority Check
- Registry Match: YES / NO / PARTIAL
- Conflicting or Older Docs
- Status: CANONICAL / SUPERSEDED / REFERENCE ONLY / NEEDS REVIEW / PROPOSED ONLY
- Recommended Next Action
- Approval Required: YES / NO

## Guardrails

Claude may produce the classification card, recommend a next action, and flag conflicts.

Claude may not promote docs, mark anything SUPERSEDED, rename/move/delete files, or act on NEEDS REVIEW items without Scott approval.

## Ambiguity Rule

If registry data is unavailable, default status is NEEDS REVIEW.

## Version Conflict Rule

Newer CURRENT-dated doc governs unless Notion explicitly records otherwise. Flag both to Scott. Do not self-resolve.
