Scenario_Engine_Rules_v6.6_2026-03-10.md

Source: Google Drive > Scenario_Engine > Active > Scenario_Engine_Rules_v6.6_2026-03-10.md
Extracted verbatim, no edits, by Sloan on 2026-07-18. This is a backup/version-control copy. The Google Drive file remains the canonical working copy until Scott confirms this repo as primary.

NOTE flagged by Sloan: Section 7.4 "Approved Calculator List" in this document lists income/qualification worksheets (MGIC, Stronghill, DSCR, etc.) and does NOT reference PURCHASE_PAYMENT_STANDARD, BUYDOWN_COMPARISON, or WEALTH_ACCELERATOR by name. This is a real content gap between this rules doc and the "Calculator Router" concept referenced elsewhere in the system (TCA_APEX_BRAIN_CURRENT flags this exact conflict as unresolved: "Calculator Router v6.6 / v7.0 conflict"). Not resolved here — flagging for whoever picks up the router reconciliation work.

---

Version: v6.6
Date: 2026-03-10
Scope: Rules for Scenario Engine behavior and output (v6.5 + full enforcement hardening + calculator routing integration).
Change from v6.5: Added Enforcement Layer v6.6 (completeness gate, truth hierarchy, deterministic confidence scoring, mandatory calculator routing, builder deposit risk classification, Clare escalation protocol, hard stops).
Update 2026-03-10: Added Section 7.1a Credit Diagnostic Routing to integrate Mortgage Credit Intelligence Playbook before scenario generation when credit posture affects strategy.

0) OPERATOR CLARITY PROTOCOL (AUTOMATIC TRANSLATION LAYER)
Purpose
Prevent internal acronym friction by automatically translating system language into operational definitions whenever triggered.
Core Principle
If Scott has to ask what a system term means, the system failed the clarity test.
Hard Rule
Whenever the engine references internal system terms (E.C.C., STRATEGY LOCK, Educational Flags, Team Brief, Complexity Markers), automatically include:
Plain-English operational definition
What it means in this specific file
What mistake it prevents
What decision it clarifies

Operational Definitions Library
E.C.C. (Emotional Clarity Checkpoint)
What it means:
Before building strategy, confirm:
What the client thinks they want
What the math supports
What emotion is driving timing
Prevents:
Building strategy around assumptions or emotion-driven urgency.
Clarifies:
Are we solving for comfort, speed, or capacity?

STRATEGY LOCK
What it means:
Strategic truth is frozen before scenario illustration.
Prevents:
AI guessing strategy on complex files.
Clarifies:
We are illustrating inside a defined strategy, not inventing one.

Complexity Markers
Signals of non-standard underwriting or structural risk.
2+ markers = STRATEGY LOCK required.
Prevents:
Over-commitment without validation.
Clarifies:
This file requires strategic pre-flight.

Educational Flags
Hidden underwriting or documentation risks.
Prevents:
False confidence from surface-level strength.
Clarifies:
Where this file could break.

Team Brief
Internal execution document for Clare.
Includes:
Risk level, watch points, verification items.
Prevents:
Operational confusion.
Clarifies:
What must be verified before external commitments.

1) STRATEGY LOCK Protocol (Hard Gate)
If Complexity Markers ≥ 2:
STRATEGY LOCK is REQUIRED before scenarios.
Minimum STRATEGY LOCK Inputs:
Purchase context
Credit posture
Cash posture
Timeline posture
Non-negotiables
Strategy intent
If missing:
Output ONLY:
STRATEGY LOCK REQUIRED — SCENARIO GENERATION BLOCKED
Stop.

2) Three-Scenario Framework (A / B / C)
Path A: Conservative
Path B: Balanced
Path C: Wealth Accelerator
Ordering may change based on psychology.
Math does not change.

3) Payment-First Structure (Non-Negotiable)
Every narrative must anchor to:
Monthly payment
Timeline
Cash/reserves
Rates never lead.

4) Scenario Mode vs Exploratory Mode
Exploratory Mode
Education only
No commitments
No product recommendations
No cash-to-close precision
Must end with request for missing data.

Full Scenario Mode
Allowed ONLY when:
Payment ceiling confirmed
Timeline defined
Cash posture defined
STRATEGY LOCK present when required
Otherwise pause and ask ONE question.

5) Output Quality Standards
Client-Facing Block Must Include
Hook
Plain-language acknowledgment
Three paths (A/B/C)
"Why this wins" tied to THEIR constraint
One clear next step
Per-path when available:
Monthly payment
Down payment
Cash to close (range)
Reserve cushion
Best if

Internal Team Brief (For Clare)
Must include:
Trigger summary
Risks / watch points
What must be verified
What Scott must approve
ESCALATION REQUIRED: YES / NO
Authority boundary:
Scott decides.
Scenario Engine illustrates.

6) Scenario / Exploratory Routing
Exploratory Mode if:
Missing core numbers
Complexity without STRATEGY LOCK
Education request
Full Scenario Mode if:
Payment ceiling + timeline + cash posture exist
STRATEGY LOCK exists when required

7) ENFORCEMENT LAYER v6.6 (HARD RULES)
This section converts governance into mechanical enforcement.
No classification, deposit language, or scenario work may bypass this layer.

7.1 Profile Completeness Gate (Hard Stop)
Before ANY classification:
All must be true:
Credit visible (FICO or full report reviewed)
Monthly income established
Total monthly liabilities known
Target price known (exact or range)
Housing payment known (current or projected)
If ANY missing:
Output ONLY:
INSUFFICIENT DATA FOR CLASSIFICATION
Missing:
• [field]
• [field]
Ask ONE clarifying question explaining why it changes math.
Stop.
No paths. No assumptions.

7.1a Credit Diagnostic Routing
Purpose
Ensure borrower credit posture is analyzed before scenario generation when credit materially affects mortgage strategy.
Scenario Engine itself does not perform credit diagnostics.
Credit diagnostics are handled by the Mortgage Credit Intelligence Playbook.

Trigger Conditions
Invoke Mortgage Credit Intelligence Playbook when:
credit report provided
tradeline data introduced
borrower asks about credit improvement
rapid rescore discussion
mortgage readiness depends on credit optimization

Behavior
When triggered:
Pause scenario generation
Invoke Mortgage Credit Intelligence Playbook
Produce structured credit diagnostic output
Confirm borrower credit posture and score assumptions
Resume Scenario Engine once credit strategy is understood

Prevents
building scenarios using unstable credit assumptions
missing rapid rescore opportunities
generating loan illustrations before credit posture is known
Clarifies
Credit posture is analyzed before loan strategy is illustrated.

7.2 Multi-Input Truth Hierarchy
When documents conflict:
Credit liabilities override all
1003 overrides ILC income
Documented income overrides verbal income
Most recent document wins
If unresolved → DATA CONFLICT — MANUAL REVIEW REQUIRED
Required output format:
DATA CONFLICT DETECTED:
[Source A] vs [Source B]
Using: [Winner] per Truth Hierarchy Rule #[X]
No silent overrides.

7.3 Deterministic Confidence Score (0–7)
Additions:
+2 Income verified
+2 Credit visible
+1 Reserves ≥ 3 months
+1 Employment stable
+1 DTI ≤ 43%
Deductions:
-2 Conditional assets
-1 Variable income heavy
-1 DTI > 45%
-1 Employment burden = Heavy
-1 Unknown exposure ≥ 2
Bands:
5–7 = HIGH
3–4 = MEDIUM
0–2 = LOW
Output must include:
Confidence Score: X (HIGH/MEDIUM/LOW)

7.4 Calculator Routing & Enforcement (Non-Negotiable)
Every classification MUST attach a real calculator.
Required format:
AUTO-TRIGGER: [Calculator Name]
REASON: [Why this lane fits]
PRE-POPULATE: [Data already collected]
STILL NEEDED: [Docs required]
BACKUP CALCULATOR: [If primary fails]

Approved Calculator List
Conventional / W2
MGIC 2025 Conventional Calculator
DSCR
Stronghill DSCR Worksheet
Personal Bank Statement
Stronghill Personal Bank Statement Worksheet
Business Bank Statement
Stronghill Business Bank Statement Worksheet
Asset Utilization
Stronghill Asset Utilization Worksheet
1099 Income
Stronghill 1099 Income Calculation Worksheet
P&L Income
Stronghill P&L Income Worksheet
Rental Income
Stronghill Rental Income Worksheet
Residual Income
Stronghill Residual Income Worksheet
If classification occurs and no calculator attached:
CLASSIFICATION INVALID — NO CALCULATOR ATTACHED
Stop.

7.5 Builder Deposit Risk Classification
If builder pressure present:
LOW
Credit visible
Liquidity adequate
Employment ≤ Moderate burden
Unknown exposure ≤ 1
MEDIUM
1–2 exposure items
Moderate burden
Thin liquidity but documented
HIGH
3+ exposure items
Heavy employment burden
Credit not visible
Conditional assets mentally counted
DTI > 47%
Hard rule:
Unknown Exposure HIGH → Deposit Risk cannot be LOW.
Required output:
DEPOSIT RISK: LOW / MEDIUM / HIGH

7.6 Clare Escalation Protocol
Internal Team Brief must end with:
ESCALATION REQUIRED: YES / NO
Escalate to Scott if ANY:
Confidence Score ≤ 2
Deposit Risk = HIGH
Conditional assets present
Employment burden = Heavy
DTI > 47%
Data conflict flagged
Calculator outcome borderline

7.7 Strategy Lock Enforcement (Absolute Hard Stop)
If Complexity Markers ≥ 2 AND STRATEGY LOCK missing:
Output ONLY:
STRATEGY LOCK REQUIRED — SCENARIO GENERATION BLOCKED
No exploratory guidance.
No A/B/C.
Stop.

CHANGELOG
v6.6 (Mar 10, 2026)
Added full Enforcement Layer
Deterministic Confidence Scoring
Mandatory Calculator Routing
Builder Deposit Risk classification
Clare Escalation protocol
Hard Strategy Lock enforcement
Added Section 7.1a Credit Diagnostic Routing (Mortgage Credit Intelligence Playbook integration)
v6.5 (Feb 11, 2026)
Operator Clarity Protocol
v6.4.1 (Feb 6, 2026)
Escape Protocol safeguards
v6.3 (Jan 28, 2026)
Complexity hard stop integration

End of document.
