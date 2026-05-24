---
name: scheduled-boot-briefing-builder
description: >
  Build a structured morning boot briefing that loads context, surfaces priority actions,
  and gets Scott oriented in under 5 minutes. Use to build a briefing template for recurring
  scheduled sessions, or to generate a one-time briefing at the start of a high-priority day.
  Outputs a briefing document with five sections: system status, open decisions, priority
  queue, calendar and deal watch, and first action.
triggers:
  - "build a boot briefing"
  - "morning briefing"
  - "scheduled briefing"
  - "daily brief"
  - "boot me up"
  - "start of day brief"
  - "what do I need to know today"
  - "session briefing"
related_skills:
  - mcp-health-check (run first — system status populates Section 1)
  - context-stack-refresher (run to populate prior session context for Section 2 and 3)
  - open-decisions-manager (use to populate Section 2)
  - cowork-queue-manager (use to populate Section 3)
  - crm-notion-file-sync-checker (use if deal watch in Section 4 requires sync verification)
---

# Scheduled Boot Briefing Builder

## Purpose

A boot briefing is not a summary. It is a launch checklist.
Scott reads it, knows what is on, and starts work. Five minutes max. No narrative.

---

## Boot Briefing Structure

Every briefing has exactly five sections. In order.

---

### Section 1 — System Status

Source: mcp-health-check output
Content: Which MCP tools are OK, Degraded, or Failed.
Format: Bullet list. OK tools in a single line. Degraded and Failed called out individually.

If all tools are OK: All systems operational.
If any tool is Degraded: HubSpot: Degraded — data may be stale. Do not write until recovered.
If any tool is Failed: HubSpot: FAILED — skip HubSpot tasks this session. See recovery plan.

---

### Section 2 — Open Decisions

Source: open-decisions-manager current log
Content: All decisions in Open or Escalated state, sorted by due date.
Format: Numbered list. Three items max. If more than three, show the three closest to due.

Format per item:
[D-ID] [Topic] — Due: [Date] — [One-line recommended resolution]

---

### Section 3 — Priority Queue

Source: cowork-queue-manager current queue or carry-forward list
Content: Top 5 items for today, sorted by priority.
Format: Numbered list.

Format per item:
[P1/P2/P3] [Item] — [Estimated time] — [Skill needed or None]

---

### Section 4 — Calendar and Deal Watch

Source: Google Calendar (via MCP) and HubSpot deal pipeline
Content: What is on the calendar today and which deals are closing or moving this week.
Format: Two sub-sections.

Calendar:
[Time] [Event name] [Prep needed or None]

Deals to watch this week:
[Deal name] — Stage: [Stage] — Close: [Date] — Action needed: [Yes / No]

---

### Section 5 — First Action

Content: One sentence. What Scott should do first when he opens Claude Code today.
This is a forced choice. Not a list. Not options. One action.

Format:
First action: [Specific task] using [Skill if applicable].

---

## Briefing Build Protocol

Step 1: Run mcp-health-check. Populate Section 1.
Step 2: Pull open decisions. Populate Section 2.
Step 3: Pull queue or carry-forwards. Populate Section 3.
Step 4: Pull calendar from Google Calendar. Pull top deals from HubSpot. Populate Section 4.
Step 5: Determine the single highest-value first action. Populate Section 5.
Step 6: Assemble the five sections. Total length target: under 400 words.
Step 7: Deliver to Scott.

---

## Hard Rules

- Section 5 is exactly one sentence. Force the choice. Do not give options.
- No narrative prose in the briefing. Every line is a data point or a directive.
- If a system check fails for a section, note the failure in that section. Do not skip the section.
- Section 2 shows three decisions max. The rest go to the open-decisions-manager log.
- Section 3 shows five queue items max. The rest are in the cowork-queue-manager carry-forward.
- Total briefing must be readable in under 5 minutes. If it is longer, cut it.

---

## Quality Check Before Delivering Briefing

- All five sections present?
- Section 5 is a single sentence with one action?
- Total word count under 400?
- System failures from Section 1 reflected in Section 3 queue (no tasks queued for failed tools)?
