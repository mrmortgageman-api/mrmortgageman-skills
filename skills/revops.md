---
name: revops
description: >
  Revenue operations for MrMortgageMan. Use when Scott needs help with HubSpot
  pipeline logic, lead lifecycle management, SignalStrike contact promotion rules,
  contact scoring, CRM data architecture, or marketing-to-conversation handoff
  processes. This skill governs how leads move through the system from detection
  to ILC booking to active file. Always read product-marketing-context first.
triggers:
  - "HubSpot pipeline"
  - "lead scoring"
  - "contact promotion"
  - "lead lifecycle"
  - "CRM logic"
  - "how should this contact be staged"
  - "pipeline stage"
  - "SignalStrike scoring"
  - "contact should move"
  - "HubSpot property"
  - "lead routing"
  - "Monday call list"
  - "revops"
related_skills:
  - product-marketing-context (read first, always)
  - cold-email (for outreach that follows contact promotion)
  - email-sequence (for nurture sequences triggered by pipeline movement)
---

# MrMortgageMan RevOps Skill

## Context Load - Required First Step

Before making any recommendation, read product-marketing-context.md.
This skill operates inside the HubSpot and Notion architecture.
Every recommendation must be compatible with existing property architecture.

---

## System Architecture Overview

Source of truth: HubSpot (all contact and deal data)
Intelligence layer: Notion (scenario timelines, advisory notes, session logs)

Two scoring engines. Do not conflate:

Engine | Scale | Threshold | Audience
SignalStrike B2C | 0-100 composite | 60+ | Buyers/consumers
SignalStrike B2B | 0-5 rubric | 3+ | Realtors/referral partners

Council execution:
- Griff (ChatGPT): HubSpot data entry, contact creation, property updates, logging
- Hank (Perplexity): lead detection, research, scoring, signal intel
- Scott: final approval on all contact promotions and cross-system writes
- Claude: architecture, strategy, skill output

---

## SignalStrike B2C Lead Lifecycle

Stage 1: Detection (Hank, 12:00-12:15 PM daily)
Sources: Reddit, Facebook groups, Twitter/X, LinkedIn
Output: qualified lead candidates with intent signals

Qualification criteria:
- Geographic fit: East Bay 60%, SF 25%, South Bay 15%
- Timeline signals: looking, moving, buying language
- Intent markers: budget mentioned, agent mentioned, urgency
- Recency: posted within 30 days

Stage 2: Scoring (Hank)
Formula: ww_score_composite = (intent_strength x 0.4) + (timeline_urgency x 0.3) + (profile_completeness x 0.2) + (engagement_recency x 0.1)
Scale: 0-100
Threshold: 60 or higher = approved for outreach

HubSpot properties (ww_* group):
- ww_intent_signal: High / Medium / Low / None
- ww_engagement_timeline: 0-3mo / 3-6mo / 6-12mo
- ww_score_composite: 0-100
- ww_trigger_type: Relocation / Life event / Market timing / Budget stated / Agent mentioned
- ww_last_engagement: date
- ww_agent_opportunity: TRUE/FALSE

Stage 3: Validation (Griff)
Checks: existing HubSpot record, duplicate detection, required fields

Stage 4: Scott Approval
Approves: contact quality, outreach angle, no relationship conflicts
Approval method: status change Validation Complete -> Approved

Stage 5: Outreach Execution (Scott, manual)
Time: 12:15-12:30 PM daily
Volume: 2-3 precision DMs per day
Tool: cold-email skill for message construction

Stage 6: Logging (Griff)
Logs: all ww_* properties, source evidence, DM sent, task for follow-up

Cross-System Bridge (when consumer mentions an agent):
1. Set ww_agent_opportunity = TRUE
2. Log agent name in contact notes
3. Hank searches HubSpot for agent as B2B contact
4. Scott decides: boost score (+2), add to B2B list, or note only
5. Griff executes after Scott approval

---

## SignalStrike B2B Lead Lifecycle

Stage 1: Detection (Hank, 6:00-6:15 AM daily)
Tracks:
- Track 1: Platform alerts (YouTube, GBP, Instagram, LinkedIn)
- Track 2: Comet Facebook group audits
- Track 3: Warm relationship maintenance (existing HubSpot contacts)

Stage 2: Scoring (Hank)
Scale: 0-5 rubric
5 = Apex: active content + buyer niche + high production
4 = Strong: regular content + mixed niche + solid production
3 = Ready: recent content + some signals + validated production
2 = Warming: sporadic content + unclear niche
1 = Early: minimal content + low production
0 = Not ready

HubSpot properties (intent_signal_* group):
- hs_intent_signals_enabled: checkbox
- intent_signal_sources: YouTube / Instagram / GBP / LinkedIn / Facebook
- intent_signal_last_seen: date
- intent_signal_score: 0-5
- instagram_handle: text
- facebook_profilepage: text
- hs_linkedin_url: text
- mm_prospect_tier: D / E / F

Whale Flag properties:
- Whale Flag: TRUE/FALSE
- Last Whale Touch Date: date

Stage 3: 2-of-3 Promotion Check
A contact must hit 2 of these 3 before Monday call list:
1. Intent signal score 3 or higher
2. Active content posted within 7 days
3. Niche alignment confirmed (residential buyer-side preferred)

Stage 4: Validation (Griff)
Checks: existing HubSpot record, relationship history, conflict flags
Conflict flags: competitor relationship, past rejection, existing partnership, geographic mismatch

Stage 5: Scott Approval
Approval method: Council Batch Queue status Approved

Stage 6: Manual Execution (Scott)
Volume: 2 comments per agent (Touch 0)
Tool: cold-email skill for angle construction

Stage 7: Logging (Griff)
Logs: contact record, intent_signal_* properties, note with platform and content touched, task for follow-up

---

## Monday Morning Intelligence Brief

Delivery: 7AM every Monday via HubSpot-fed digest
Cap: 15 contacts maximum
Breakdown:
- Call list (score 3+ or Whale Flag, approved)
- New agent candidates (recently detected, in validation)
- Engagement queue (existing contacts needing a touch)
Power hour: 10AM-1PM Monday call block

Call list rules:
- Whale Flag contacts always included
- Score 3+ required for standard contacts
- 2-of-3 promotion rule must be met
- No sub-threshold contacts

---

## HubSpot Minimum Viable Record (MVR)

B2C Contacts (14 required fields):
First name, Last name, Email, Phone, Source (ww_ trigger), ww_intent_signal, ww_score_composite, ww_engagement_timeline, ww_trigger_type, ww_last_engagement, ww_agent_opportunity, mm_prospect_tier, Notion file URL, HubSpot contact creation date

B2C Deals (13 required fields):
Deal name, Pipeline, Stage, Close date (estimated), Purchase price (estimated), Loan amount (estimated), Loan type, file_status, next_action_due_date, scenario_last_updated, primary_constraint, notion_file_url, Associated contact

B2B Contacts (15 required fields):
First name, Last name, Email, Phone, Brokerage, Geographic market, intent_signal_score, intent_signal_sources, intent_signal_last_seen, hs_intent_signals_enabled, mm_prospect_tier, Whale Flag, Last Whale Touch Date, at least one social profile field, Notion file URL

---

## Custom HubSpot Deal Properties

These 5 properties were created via Google Colab API call. Live on B2C Deals:

file_status (Enum): Pre-Application / Application Submitted / Processing / Conditional Approval / Clear to Close / Closed / On Hold / Dead
next_action_due_date (Date): free date field
scenario_last_updated (Date): free date field
primary_constraint (Text): free text
notion_file_url (URL): link to Notion file

notion_file_url also exists on the Contact object for bi-directional linking.

---

## Pipeline Stage Logic

B2C Pipeline:
Lead -> ILC Booked -> Consulting -> Application -> Processing -> Clear to Close -> Closed / Dead

Exit criteria:
- Lead exits when: books ILC
- ILC Booked exits when: ILC completed
- Consulting exits when: submits application
- Application exits when: conditional approval
- Processing exits when: CTC issued
- Clear to Close exits when: file closes

B2B Pipeline (relationship stages):
Detected -> Validated -> Approved -> Touch 0 Sent -> Touch 1 Sent -> Responding -> Relationship Active -> Partner -> Whale

---

## RevOps Output Format

When diagnosing a contact or recommending a pipeline action:

REVOPS RECOMMENDATION
Contact: [Name]
Current stage: [Stage]
Score: [Score]
Issue: [What Scott asked]

---

Assessment: [2-3 sentences on what the data shows]
Recommended action: [one specific next step]
HubSpot update: [exact property name and value Griff should set]
Notion update: [what to log if applicable]
Scott approval required: Yes / No

---

## Governing Rules

1. HubSpot must be completed before any Notion file is built.
2. Scott approves ALL cross-system property writes.
3. No automatic score boosts. Every score change requires Scott sign-off.
4. Sub-threshold contacts do not receive messaging. Period.
5. Whale contacts always get priority treatment. No separate pipeline.
6. If we do not track, we do not care.
