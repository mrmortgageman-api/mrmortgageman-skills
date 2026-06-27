# CURRENT_OPERATING_CONFIGURATION_CURRENT

**Version:** 2026-06-27  
**Status:** Operational Document (Living)  
**Change Frequency:** As implementation changes  
**Last Updated:** 2026-06-27

---

## Purpose

This document records the current implementation of the Applied Intelligence Operating System.

It maps abstract roles and functions (defined in the constitutional layer) to concrete platforms, tools, and people (today's choices).

When platforms change, this document updates. The constitution remains unchanged.

---

## Current Role Assignments

### Decision Authority
**Role Function:** Synthesize intelligence and make final decisions  
**Current Assignment:** Scott Thompson  
**Authority Domain:** Product strategy, architecture, workflow decisions  
**Escalation Path:** None (final authority)

### Intelligence Gathering — Synthesis / Strategy
**Role Function:** Reviews systems holistically, integrates across domains, controls scope  
**Current Assignment:** Griff (ChatGPT)  
**Access:** Email, chat, product review sessions  
**Primary Domain:** Product strategy, systems integration, scope control, mortgage operations

### Intelligence Gathering — Challenge / Divergence
**Role Function:** Tests assumptions, explores alternatives, brings fresh perspectives  
**Current Assignment:** Kimi (Claude Design)  
**Access:** Email, chat, product review sessions  
**Primary Domain:** Greenfield thinking, assumption testing, design alternatives

### Intelligence Gathering — Validation
**Role Function:** Provides external perspective, tests market assumptions, validates feasibility  
**Current Assignment:** Hank (Perplexity)  
**Access:** Email, chat, on-demand research  
**Primary Domain:** Market validation, external perspectives, trend research  
**Usage:** As-needed, not continuous

### Intelligence Gathering — Governance / Records
**Role Function:** Maintains institutional memory, enforces framework consistency  
**Current Assignment:** Claude (this instance, Cowork)  
**Access:** Daily in Cowork sessions  
**Primary Domain:** Decision documentation, governance enforcement, framework consistency

### Intelligence Gathering — Execution / Feedback
**Role Function:** Reports implementation constraints, surfaces feasibility issues, closes feedback loop  
**Current Assignment:** Chris Arens (Developer)  
**Access:** Direct communication, product reviews  
**Primary Domain:** Implementation insights, feasibility assessment, execution constraints, backlog management

### Execution Authority
**Role Function:** Implement approved decisions, surface feasibility issues, report outcomes  
**Current Assignment:** Chris Arens (Developer, Rate Rocket / MortgagePipeline Pro)  
**Scope:** Rate Rocket codebase, Supabase backend, API integrations  
**Escalation Path:** To Decision Authority when implementation reveals architectural issues

---

## Current AI Runtimes

| Runtime | Platform | Primary Function | Access |
|---------|----------|-------------------|--------|
| Claude | Cowork (Claude Desktop) | Governance, institutional memory, decision records | Daily |
| Griff | ChatGPT (web/app) | Strategy, systems review, synthesis | Email, chat |
| Kimi | Claude Design | Assumption testing, design alternatives | Email, chat |
| Hank | Perplexity | Market research, validation | On-demand |

---

## Current Institutional Memory Platform

**Primary System:** Notion  
**Purpose:** Working institutional memory, decision logs, active documentation  
**Access:** Scott (read/write), Claude (read/write via MCP), team view-only  
**Canonical Location:** Applied Intelligence workspace  

**Secondary System:** GitHub (mrmortgageman-api/mrmortgageman-skills)  
**Purpose:** Version-controlled canonical authority for constitutional documents  
**Access:** Scott (admin), Chris (read/write for code)  
**Repository Structure:**
```
AUTHORITIES/
├─ APPLIED_INTELLIGENCE_PRINCIPLES_CURRENT.md
├─ APPLIED_INTELLIGENCE_GOVERNANCE_MODEL_CURRENT.md
└─ CURRENT_OPERATING_CONFIGURATION_CURRENT.md

PROTOCOLS/
├─ PRODUCT_REVIEW_PROTOCOL_CURRENT.md
├─ [Domain protocols as developed]

SKILLS/
├─ [Cowork skills]
└─ [Runtime implementations]
```

**Tertiary System:** Google Drive  
**Purpose:** Permanent document library, non-code records  
**Access:** Scott (owner), shared as needed  
**Organization:** By domain and review cycle

---

## Current Canonical Authority

**Constitutional Documents:** GitHub (mrmortgageman-api/mrmortgageman-skills AUTHORITIES/)  
**Operational Protocols:** GitHub (mrmortgageman-api/mrmortgageman-skills PROTOCOLS/)  
**Institutional Memory:** Notion (working decisions, active records)  
**Document Archive:** Google Drive (permanent library)  
**Product Review Decisions:** Notion (RATE_ROCKET_REVIEW_JOURNAL_WORKING_2026-06-26 and related)  
**Architecture Decisions:** GitHub (AUTHORITIES/), Notion (indexed)

---

## Current Document Library

**Location:** Google Drive / MrMortgageMan / Applied Intelligence  

**Structure:**
```
Applied Intelligence/
├─ Constitutional Documents/
│  ├─ APPLIED_INTELLIGENCE_PRINCIPLES_CURRENT
│  ├─ APPLIED_INTELLIGENCE_GOVERNANCE_MODEL_CURRENT
│  └─ CURRENT_OPERATING_CONFIGURATION_CURRENT
├─ Product Reviews/
│  ├─ Rate Rocket Review (Screens 1-14)
│  ├─ [Future domain reviews]
├─ Protocols/
│  ├─ Product Review Protocol
│  ├─ [Future domain protocols]
├─ Architecture/
│  ├─ Governance decisions
│  ├─ Data model decisions
│  └─ Integration boundaries
└─ Operational/
   ├─ Role assignments
   ├─ Tool configurations
   └─ Decision logs
```

---

## Current Execution Platform

**Primary:** MortgagePipeline Pro (Rate Rocket)  
**Tech Stack:** Next.js (TypeScript), Supabase (backend), React  
**Location:** mrmortgageman-api/nextjs-boilerplate (GitHub private repo)  
**Deployment:** Vercel  
**Database:** Supabase PostgreSQL  
**Owner:** Chris Arens  

**Supporting:** Mini-PC (Cowork environment)  
**Path:** C:\Users\Scott W Thompson\cowork-build\  
**Primary Function:** Claude Cowork sessions, skill execution  
**Tools:** Pre-approval generator, data analysis, content creation

---

## Current Automation Platform

**Primary:** Zapier  
**Current Status:** Audited and reduced from 23 to 10 active Zaps  
**Scope:** HubSpot ↔ Mailchimp, Quo integration, Notion automation  
**Owner:** Scott / Chris  

**Supporting:** Supabase Functions (future automation layer)  
**Status:** Planned, not yet implemented

---

## Current CRM / LOS Configuration

### HubSpot (Primary CRM)
**Portal ID:** 242239760  
**Owner ID:** 66124405  
**Purpose:** Non-negotiable source of truth for borrower and partner relationships  
**Integration:** SignalStrike, Rate Rocket (planned), Zapier  
**Custom Properties:**
- mm_prospect_tier (B2B partner classification)
- rltr_tier (Realtor tier)
- partner_grade (Partner rating)
- whale_flag (High-value partner indicator)

### Notion (Enrichment & Planning)
**Purpose:** Borrower strategy, workflow documentation, active file management  
**Current Databases:**
- Realtor Partners (B2B partner tracking)
- Active Borrower Files (B2C active deals)
- LO Accountability Tracker (activity tracking through EOY 2026)
- Email Template Library (~35+ templates)
- Rate Watcher Configuration

### Mailchimp (Marketing Email)
**Purpose:** Marketing campaigns, nurture sequences  
**Compliance:** All marketing and nurture email routes through Mailchimp  
**Integration:** Zapier, planned Rate Rocket integration

### Quo (SMS / Call Management)
**Purpose:** SMS inbox, call logging, voicemail transcription  
**Current Status:** Active with Fathom integration

### Fathom.ai (Call Recording & Transcription)
**Purpose:** Call transcription, meeting recording  
**Integration:** Quo inbox  
**Status:** Active

---

## Current Process Configuration

### Daily Operating Rhythm
**Morning (8:00 AM):** Dashboard review, GO Coaching check-in  
**Calls:** Time-blocked by day (Monday = Realtors, Friday = Freestyle)  
**Evening:** LO Activity Tracker update, next-day prep

### Weekly Review Rhythm
**Day:** Friday afternoon  
**Focus:** Pipeline review, partner relationship status, weekly metrics  
**Output:** GO Coaching score, activity summary, next-week priorities

### Product Review Cycle
**Last Cycle:** Rate Rocket review (Screens 1-14, June 26, 2026)  
**Next Cycle:** TBD (recommend quarterly or when significant changes are made)  
**Review Protocol:** Product Review Protocol (to be locked in operational layer)

---

## How This Configuration Works

**If a platform changes:**
- Update this document (CURRENT_OPERATING_CONFIGURATION_CURRENT)
- Update relevant domain protocol (e.g., if Notion is replaced, update institutional memory section)
- Constitutional documents remain unchanged

**If a role changes:**
- Update the role assignment section
- Update relevant protocol (e.g., if Decision Authority changes, protocols adjust)
- Constitutional documents remain unchanged

**If a runtime platform is added or replaced:**
- Update AI Runtimes section
- Create or update runtime skill
- Constitutional documents remain unchanged

---

## Bridge to Operational Layer

**Constitutional Layer Questions:** What should decisions be made? How should they be governed?  
**Configuration Layer Answers:** Who makes them today? What tools do we use today? Where do we store decisions today?  
**Operational Layer Questions:** How do we apply governance to Product Review? How do we run SignalStrike? How does Rate Rocket get built?

This document connects the answers to the questions.

---

## Version History

| Date | Version | Change | Authority |
|------|---------|--------|--------|
| 2026-06-27 | 1.0 | Initial configuration document | Scott Thompson |

---

## Connected Documents

- **APPLIED_INTELLIGENCE_PRINCIPLES_CURRENT** — Why we organize this way (constitutional)
- **APPLIED_INTELLIGENCE_GOVERNANCE_MODEL_CURRENT** — How decisions move through the system (constitutional)
- **PRODUCT_REVIEW_PROTOCOL_CURRENT** — How to conduct product reviews (operational)
- **Domain Protocols** — How to apply governance to specific work (operational, living)
- **Runtime Skills** — How specific AI implementations work (operational, living)

---

## Governance Metadata

**Document Type:** Operational Configuration  
**Authority:** Scott Thompson (Decision Authority)  
**Change Frequency:** Regular. Update whenever platforms, tools, roles, or systems change.  
**Approval Required:** Decision Authority (for significant changes); no approval needed for routine updates  
**Review Cadence:** Quarterly, or whenever a tool/platform/role changes  
**Supersedes:** None (first version)  
**Referenced By:** 
- All Domain Protocols (for current implementation details)
- All Runtime Skills (for current platform information)

**Note:** This document is living. It reflects today's implementation choices. Changes to this document do NOT change the constitutional layer. When tools change, this document is updated; the constitution remains stable.