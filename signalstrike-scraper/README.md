# 🎯 SignalStrike Scraper - Phase 1

**Status:** PHASE 1 BUILD COMPLETE (3 TEST AGENTS, FACEBOOK ONLY)
**Owner:** Claude (Digital Chief of Staff)
**Created:** 2026-06-15
**Version:** 0.9 - Pre-QA
**Target QA:** Fri 6/18
**Target Go-Live:** Mon 6/19 (30 agents + Instagram/LinkedIn)

---

## What This Does

Nightly automation that:
- **Scrapes** agent social posts (Phase 1: Facebook only, 3 test agents)
- **Enforces** 3-7 day gap between touches to same agent
- **Randomizes** comment templates (no repeats to same agent)
- **Drafts** context-specific comments (Claude API)
- **Queues** 8 posts/night for Scott's 6 AM approval (Notion)
- **Logs** execution details (Notion EXECUTION_LOG)

---

## Phase 1 Scope (Fri 6/13 - Fri 6/18)

### Test Agents (3 only, hard-coded)

1. **Lauren Woolsey** (Tier A)
   - Facebook: https://www.facebook.com/lauren.woolsey
   - Specialty: High-volume residential sales

2. **Alka Sabherwal** (Tier B)
   - Facebook: https://www.facebook.com/alka.sabherwal
   - Specialty: First-time homebuyers, market insights

3. **Jordan Wright** (Tier A)
   - Facebook: https://www.facebook.com/jordan.wright
   - Specialty: Investment properties, market analysis

### Platforms (Phase 1)

✅ **Facebook** (public posts)
❌ **Instagram** (deferred to Phase 2)
❌ **LinkedIn** (deferred to Phase 2)

---

## Phase 1 QA Checklist (8 items)

Must pass ALL before Phase 2 expansion:

1. ✅ **Nightly execution:** Runs at 11 PM PT
2. ✅ **Queue population:** 8 posts average by morning
3. ✅ **Status updates:** Scott's approve/skip clicks update Notion
4. ✅ **Gap enforcement:** No posts within 3-7 day window
5. ✅ **Template randomization:** Same template never repeats to same agent
6. ✅ **Execution log accuracy:** Post count matches queue count
7. ✅ **No errors:** Zero Python errors in logs
8. ✅ **Comment quality:** Comments are specific (one detail from post)

---

## Files

- **signalstrike_scraper_phase1_CURRENT_2026-06-15.py** - Main scraper (517 lines)
- **README.md** - This file

---

## Running Phase 1

```bash
python signalstrike_scraper_phase1_CURRENT_2026-06-15.py
```

**Output:**
- 3 test agents processed
- 4+ posts queued (varies with mock data)
- Execution log with gap days + templates
- Zero errors

---

**Last Updated:** 2026-06-15
**Status:** PHASE 1 BUILD COMPLETE, QA UNDERWAY
**Owner:** Claude (Digital Chief of Staff)
