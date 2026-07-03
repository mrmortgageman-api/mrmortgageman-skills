---
name: cowork-session-closer-draft
version: 2-draft
status: DRAFT — NOT CERTIFIED, NOT DEPLOYED
description: Draft revision of cowork-session-closer. Adds a tiered capture model and cross-platform layering notes. Does not replace the live SKILL.md until Scott reviews and approves.
agents: [claude_cowork, claude_act]
trigger_phrases:
  - "close the session"
  - "wrap up"
  - "session done"
  - "end session"
  - "log this session"
  - "stand down"
---

# DRAFT — Session Closer, Extended

**Status: prep only. This file does not replace skills/cowork-session-closer/SKILL.md. Nothing here is standing doctrine until Scott approves it and the live SKILL.md is updated in a separate, deliberate step.**

## What this draft adds to the existing skill

The live skill already handles: files touched, decisions made, pending review, batons, Notion mirror yes/no. This draft adds two things on top, both discussed and provisionally approved by Scott on 2026-07-03, prep stage:

1. A tiered capture model, so half-formed ideas aren't lost but also don't bloat the journal at the same weight as real decisions.
2. Explicit cross-platform notes, since this skill's logic may need adapted copies for Griff and Hank, not just Claude.

## Tiered Capture Model

**Tier 1 — Decision.** Something Scott approved, rejected, or modified this session. Gets a full entry: what was decided, why, status.

**Tier 2 — Parked idea.** A concept, framing, or open question that didn't resolve into a decision but matters enough to not lose. Gets one short line, not a full write-up. Example from 2026-07-03: the Clark Kent / Superman framing for Claude ACT identity switching. Not a decision. Worth keeping.

**Tier 3 — Pure discussion.** Talking something through with no lasting artifact. Not captured. Not every sentence needs a home.

Claude decides the tier at close-out. If uncertain whether something is Tier 1 or Tier 2, default to Tier 2, a short parked line, rather than silently dropping it.

## Routing Lanes

**Lane 1 — Notion.** Governance decisions, identity rules, anything that changes how the system operates. This is Tier 1 material, per the Tri-Platform Stability Rule (Notion = Brain).

**Lane 2 — Scott, flagged action item.** Anything needing a human step: a Drive paste, a tool decision, an approval not yet given. Shown as a short list at close, not buried in prose.

**Lane 3 — Nowhere.** Tier 3 material. Intentionally not logged.

## Cross-Platform Note

This skill, in its current and draft form, is written for Claude. Griff (ChatGPT) and Hank (Perplexity) don't read Claude Skills natively. If session close-out logic is wanted for their sessions too, each needs its own adapted copy of this logic, in whatever instruction format that platform supports. This file is the master copy. Any platform-specific adaptation is a real edit, not a copy-paste, and needs Scott's sign-off before it's trusted, per the Tri-Platform Stability Rule (GitHub = Workshop, builds live here).

## Open Question, Not Resolved

Whether close-out should trigger automatically when Claude senses a session ending, or only on an explicit phrase, matching how "Claude ACT" itself is triggered. No recommendation made yet. Needs Scott's call.

## Everything Else

All guardrails, output format, and rules from the live SKILL.md carry forward unchanged in this draft: no marking a session closed with unresolved pending items, no treating discussed ideas as confirmed decisions, no marking a Notion mirror complete if Notion was unavailable, no moving or renaming files during close-out without approval.
