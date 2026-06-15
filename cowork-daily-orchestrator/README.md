# 🎯 Cowork Daily Orchestrator

**Status:** MVP READY FOR COWORK DEPLOYMENT  
**Owner:** Claude (Digital Chief of Staff)  
**Created:** 2026-06-15  
**Version:** 1.0 - Phase 1 (MVP)

---

## What This Skill Does

Surfaces four daily rituals that keep Scott aligned, focused, and executing his operating system.

### Four Daily Modules

**6:00 AM — SignalStrike Approval Queue** (daily)
- Displays 8 pending posts from SIGNALSTRIKE_APPROVAL_QUEUE
- Shows Claude's drafted comment for each post
- Scott: Approve or Skip

**8:30 AM — Pre-Work Ritual + Theme Day Queue** (weekdays)
- Pre-work ritual checklist (5 items)
- Today's theme day (Monday/Tuesday/etc)
- HubSpot tasks filtered by theme day prefix [MON], [TUE], etc

**5:00 PM — Pre-Leave Ritual** (weekdays)
- Day scorecard (did you hit your target?)
- "Who still needs to hear from you today?" prompt

**Sunday 7:00 PM — Sunday Night Ritual** (Sundays only)
- Week review (5 reflection questions)
- Next week preview (5 prep items)

---

## Schema Decision (Option A — LOCKED)

**Theme Day Filtering:** Tasks are filtered by prefix in `hs_task_subject`
- Format: `[MON] Agent Name - Task Description`
- Honors Zap 2 governance: No custom properties, theme logic in task subject
- Locked: 2026-06-15 (Griff confirmed no theme_day_tag field exists)

---

## Files

- **cowork_daily_orchestrator_FINAL.py** - Production skill
- **hubspot_integration.py** - HubSpot API wrapper (Option A parsing)
- **notion_integration.py** - Notion API wrapper
- **README.md** - This file

---

## Testing

```bash
python cowork_daily_orchestrator_FINAL.py
```

---

**Last Updated:** 2026-06-15  
**Status:** DEPLOYED TO GITHUB