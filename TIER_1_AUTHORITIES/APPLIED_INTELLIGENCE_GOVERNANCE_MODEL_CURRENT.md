# APPLIED_INTELLIGENCE_GOVERNANCE_MODEL_CURRENT

**Version:** 2026-06-27  
**Status:** Constitutional Document  
**Change Frequency:** Rare (only when experience reveals fundamental improvement)

---

## Core Purpose

This document describes how intelligence becomes governed execution.

It defines the roles, decision classes, promotion rules, institutional memory, and feedback loop that translate Applied Intelligence Principles into disciplined action.

---

## Governance Flow

```
INTELLIGENCE
(Multiple perspectives gathered)
        ↓
GOVERNANCE
(Decision authority synthesizes)
        ↓
INSTITUTIONAL MEMORY
(Approved decision recorded)
        ↓
EXECUTION
(Decision implemented)
        ↓
FEEDBACK
(Results inform next cycle)
        ↓
INTELLIGENCE
(Loop continues)
```

Every step is necessary. Skipping steps creates chaos or stagnation.

---

## Roles and Functions

### Decision Authority
**Function:** Synthesize intelligence and make final decisions

**Responsibilities:**
- Gather perspectives before deciding
- Make clear, timely decisions
- Own the outcome (success or failure)
- Identify when a decision should be revisited

**Implementation:** Assigned in operational protocols (not in constitution)

**Key Principle:** One authority per decision domain prevents diffusion and enables accountability.

---

### Intelligence Gathering
**Function:** Provide specialized perspectives

**Roles (by function):**
- **Synthesis / Strategy:** Reviews systems holistically, integrates across domains, controls scope
- **Challenge / Divergence:** Tests assumptions, explores alternatives, brings fresh perspectives
- **Validation:** Provides external perspective, tests market assumptions, validates feasibility
- **Governance / Records:** Maintains institutional memory, enforces framework consistency
- **Execution / Feedback:** Reports implementation constraints, surfaces feasibility issues, closes feedback loop

**Implementation:** Specific assignments defined in operational protocols (not in constitution)

**Key Principle:** Different perspectives have different roles. They don't compete; they contribute.

---

### Institutional Memory
**Function:** Improve future decisions by preserving approved decisions and their rationale

**Responsibilities:**
- Record decisions with authority and rationale
- Keep memory clean (debate does not get recorded)
- Make decisions searchable and retrievable
- Support future decisions that build on past decisions
- Enable organizational learning across time

**Implementation:** Platform defined in operational protocols (not in constitution)

**Key Principle:** Institutional memory exists to improve future decisions, not just to document.

---

### Execution
**Function:** Implement approved decisions

**Responsibilities:**
- Execute approved strategy faithfully
- Surface feasibility issues early
- Implement with fidelity to architectural intent
- Report outcomes to feed the feedback loop

**Implementation:** Assigned in operational protocols (not in constitution)

**Key Principle:** Execution should not second-guess strategy, but should flag when strategy proves unworkable.

---

## Decision Classes

Not every decision requires full governance. Decision class determines the governance path.

### Class A: Strategic / Architectural

**Requires full governance loop**

**Criteria:**
- Affects product architecture or core operating system
- Impacts data model or system boundaries
- Establishes naming conventions or taxonomy
- Defines integration boundaries with external systems
- Changes core workflow or user decision path

**Examples:**
- Product architecture (MortgagePipeline Pro as operating system vs. calculator)
- Data model decisions (B2B/B2C contact separation)
- Naming conventions (Borrower vs. Contact, Loan vs. Deal)
- Integration boundaries (SignalStrike producer/consumer boundary)
- Core workflows (TCA as two-lane: quick calculator + governed scenario engine)
- System principles (promotion rules, institutional memory policy)

**Governance Path:**
```
Intelligence → Governance → Institutional Memory → Execution
```

**Decision Authority:** The Decision Authority role (assigned in operational protocols)

**Latency Tolerance:** High (worth the rigor; affects system for months/years)

**Promotion Rule:** Always promoted to institutional memory with full rationale

---

### Class B: Product / Workflow

**Requires targeted review**

**Criteria:**
- Affects feature behavior or user workflow
- Impacts KPI definitions or measurement
- Changes default configurations
- Influences future decisions without affecting architecture

**Examples:**
- Feature behavior (How does Rate Watcher alert trigger?)
- User workflow (Steps in pre-approval process)
- KPI design (What counts as "activity"?)
- Default configurations (Default loan programs, MI thresholds)
- Integrations within approved boundaries (which fields sync to HubSpot?)

**Governance Path:**
```
Targeted Review → Governance → Institutional Memory → Execution
```

**Decision Authority:** The Decision Authority role (assigned in operational protocols)

**Latency Tolerance:** Medium (same-day or next-day decisions acceptable)

**Promotion Rule:** Promoted if decision affects future Class A/B decisions; otherwise optional

---

### Class C: Execution

**Chris authority. Escalate only if it affects approved architecture.**

**Criteria:**
- Affects only implementation details
- Does not expose gaps in architectural decisions
- Remains within approved boundaries
- Can be reversed without affecting other systems

**Examples:**
- UI polish (Button color, spacing, hover states)
- Icons (Which icon represents a borrower?)
- Microcopy (Labels, error messages, help text)
- Layout adjustments (Sidebar width, card arrangement)
- Minor implementation details (Validation logic, error message formatting)

**Governance Path:**
```
Execution Decision (Execution Authority)
         ↓
[If it exposes architectural gap]
         ↓
Escalate to Class A/B
```

**Decision Authority:** The Execution Authority role (assigned in operational protocols)

**Latency Tolerance:** Immediate (no governance wait)

**Promotion Rule:** Not promoted unless it affects future decisions

**Escalation Rule:** If Class C decision reveals that an approved architectural decision was wrong, escalate to Class B or A.

---

## Promotion Rules

Only approved decisions become institutional memory. Everything else is conversation.

### What Gets Promoted

- **Class A decisions:** Always (architectural decisions must be recorded for future reference)
- **Class B decisions:** When they affect future Class A/B decisions (when in doubt, promote)
- **Class C decisions:** Only when they reveal gaps in Class A/B decisions

### What Doesn't Get Promoted

- Ideas that were explored but not adopted
- Debate about options
- Rejected alternatives
- Process conversations
- Tool/implementation details that don't affect architecture

### Promotion Format

Every promoted decision includes:

- **Decision:** Clear statement of what was decided
- **Authority:** Who made the decision (Scott, Chris, etc.)
- **Class:** A, B, or C
- **Rationale:** Why this decision matters
- **Date:** When the decision was made
- **Source:** Link to originating conversation or document if relevant
- **Affected Systems:** What this decision impacts

---

## Institutional Memory

### Purpose

Improve future decisions by preserving approved decisions and their rationale.

Execution is enabled by institutional memory, but enabling execution is not its primary purpose.

### Capability Requirements

An institutional memory system must:
- Record decisions with clear authority and rationale
- Keep memory clean (debate does not get recorded)
- Make decisions searchable and retrievable
- Support future decisions that build on past decisions
- Enable organizational learning across time
- Remain accessible to all roles that need to reference decisions

### Structure

Organized by class and domain:

```
CONSTITUTIONAL_LAYER/
├─ APPLIED_INTELLIGENCE_PRINCIPLES_CURRENT
├─ APPLIED_INTELLIGENCE_GOVERNANCE_MODEL_CURRENT

STRATEGIC_DECISIONS/
├─ Architecture Decisions
├─ Data Model Decisions
├─ Integration Boundary Decisions
├─ Naming Conventions
└─ Core Workflow Decisions

PRODUCT_DECISIONS/
├─ Feature Decisions (by domain)
├─ Workflow Decisions
├─ KPI Definitions
└─ Configuration Decisions

OPERATIONAL_DECISIONS/
├─ Process Decisions
├─ Tool Assignments
└─ Role Assignments
```

### Implementation

The specific platform (Notion, GitHub, Google Drive, or other systems) is defined in operational protocols, not in the constitution.

The constitutional layer defines only the capability required. The operational layer chooses the implementation.

---

## Feedback Loop

The system improves because it closes the loop between execution and intelligence.

### How Feedback Works

1. **Execution reports outcomes**
   - What worked as designed?
   - What didn't work as expected?
   - What gaps did we discover?

2. **Gaps surface as new intelligence**
   - Operational issues become Class B questions
   - Architectural problems become Class A questions
   - Tool limitations become evaluation questions

3. **New questions trigger review**
   - Did we make a wrong decision?
   - Do we need a new decision?
   - Should we change how we decide?

4. **Outcomes inform next cycle**
   - Lesson learned documents capture improvements
   - Next review is better informed
   - System improves through iteration

### Escalation Examples

**Execution discovers a gap:**
- "The UI can't support the approved data model" → Escalate to Class A
- "Borrowers are confused by this workflow" → Escalate to Class B
- "This button placement feels wrong" → Class C (Chris decides)

**Feedback becomes new intelligence:**
- "SignalStrike scoring isn't predicting deal quality" → New Class B review needed
- "Rate Watcher alerts are too noisy" → New Class B review needed
- "The B2B/B2C data model is causing sync issues" → New Class A review needed

---

## Decision Authority Handoff

### When Authority Escalates

If a Class C decision reveals it should have been Class B or A, the decision moves to the appropriate authority:

```
Chris implements → Discovers gap → Escalates to Scott
Scott reviews → Determines class → Routes to appropriate authority
```

### When Authority Descends

If a Class A/B decision needs tactical adjustment that doesn't affect the core principle, authority returns to execution:

```
Scott decides (Class B) → Chris implements → Minor adjustments (Class C)
```

---

## Roles Are Durable; Assignments Are Changeable

The governance model depends on functions and roles, not specific people or platforms.

- If the Decision Authority is unavailable → role assignment changes; governance model stays same
- If the Institutional Memory platform changes → new platform implements same capability; governance model stays same
- If Intelligence Gathering roles are reassigned → new people fill roles; governance model stays same

The operating system survives role and tool changes because it's built on enduring functions, not specific implementations.

---

## Governance Quality Checks

### This governance model is working if:

- ✓ Class A decisions are rare, intentional, and well-documented
- ✓ Class B decisions happen quickly (within days, not weeks)
- ✓ Class C decisions happen in real-time (no waiting)
- ✓ Institutional memory is clean (searchable, not cluttered)
- ✓ Escalations happen when needed, not reflexively
- ✓ Feedback loop improves outcomes (same decision doesn't need to be made twice)
- ✓ Execution authority is respected (Chris makes Class C calls without committee review)
- ✓ Decision authority is clear (no ambiguity about who decides)

### This governance model is failing if:

- ✗ All decisions are treated as Class A (paralysis)
- ✗ Class B decisions take weeks (excessive governance)
- ✗ Chris waits for approval on icon changes (process overhead)
- ✗ Institutional memory is cluttered with rejected ideas (noise)
- ✗ Same decision needs to be made twice (memory failure)
- ✗ Authority is unclear (decision gets made three times by different people)
- ✗ Feedback loop is closed (execution insights don't inform future decisions)

---

## Connected Documents

- **APPLIED_INTELLIGENCE_PRINCIPLES_CURRENT** — Why we organize this way
- **Domain Protocols** — How these roles and classes apply to specific operational contexts
- **Operational Role Assignments** — Current role-to-person/platform assignments
- **Runtime Implementations** — How specific platforms or AI implementations operate within this framework

---

## Governance Metadata

**Document Type:** Constitutional  
**Authority:** Applied Intelligence Operating System  
**Change Frequency:** Rare. Amend only when experience reveals a fundamental improvement to how intelligence becomes governance.  
**Approval Required:** Decision Authority  
**Review Cadence:** Annual, or when a governance question is raised  
**Supersedes:** None (first version)  
**Referenced By:** 
- CURRENT_OPERATING_CONFIGURATION_CURRENT
- All Domain Protocols
- All Runtime Skills

**Note:** This document is enduring. Changes to roles, decision classes, or promotion rules require explicit governance review and are treated as constitutional amendments.