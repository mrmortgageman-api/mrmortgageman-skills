---
name: archive-triage-decay-rater
version: 1
description: Applies a Decay Risk rating to archive candidate files before any promotion, deletion, or reorganization. Produces a scouting report. Claude may not act on ratings without Scott approval.
---

# Instructions

Activate when reviewing files for archiving, promotion, or triage. Do not activate speculatively — only when Scott provides a file or list to evaluate.

## Decay Risk Definitions

HIGH — File is likely stale, superseded, or no longer tied to an active system.

MEDIUM — File may still have value but needs verification.

LOW — File is recently dated, clearly scoped, and tied to an active system.

## Output: Triage Scouting Report

Produce one block per file.

---
**File:** [File name]
**Date:** [File date or "Undated"]
**Likely System Area:** [SignalStrike / Rate Rocket / Cowork / Brand / Client File OS / AI Council / Unknown]
**Decay Risk:** HIGH / MEDIUM / LOW
**Registry Match:** YES / NO / PARTIAL
**Promotion Status:** ELIGIBLE / NOT ELIGIBLE / NEEDS REVIEW
**Recommendation:** [One sentence action.]
---

## Guardrails

- Claude may produce ratings and recommendations only.
- Claude may not move, delete, rename, or promote any file without Scott approval.
- If Registry Match is NO, Promotion Status defaults to NEEDS REVIEW regardless of date.
- If more than 3 HIGH decay files are found in one triage pass, flag for a dedicated Scott review session.
