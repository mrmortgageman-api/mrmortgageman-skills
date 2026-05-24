# MrMortgageMan Skill Library

Owner: Scott Thompson | MrMortgageMan | New American Funding | NMLS 1864494

## How to use these skills

Before completing any task, read the relevant skill file from the /skills folder.
Always read skills/product-marketing-context.md first. It is the master brand brief.
Every other skill depends on it.

## Skill index

- skills/product-marketing-context.md — Master brand brief. Read first. Always.
- skills/cold-email.md — SignalStrike B2B and B2C outreach. 4-touch sequence.
- skills/email-sequence.md — 6 lifecycle nurture sequences.
- skills/copy-editing.md — 7-point voice audit for existing copy.
- skills/copywriting.md — New marketing copy from scratch.
- skills/revops.md — HubSpot pipeline logic and lead lifecycle.

## Hard rules that never change

- No em dashes. Ever.
- No banned words: hopefully, maybe, no problem, best rate, fingers crossed, crushing it, killing it, game-changer, revolutionary, act now, limited time, dont miss out
- Every sentence under 20 words.
- Signature: Mortgage Made Simple, Scott (comma not period)
- HubSpot is the source of truth for all contacts and deals.
- Scott approves all cross-system writes.
- Template variables use double braces.

## Cowork Operator Pack (Phase 2)

Skills live in skills/cowork-operator-pack/. Load them by number and name.

### Session management
- 02-cowork-session-closer — Run at end of every session. Produces a log and boot queue.
- 07-cowork-queue-manager — Build and prioritize the session queue. Confirm with Scott before starting.
- 09-context-stack-refresher — Run at session start to reload prior session context.
- 11-scheduled-boot-briefing-builder — Use for recurring or scheduled session boot workflows.

### System health and data integrity
- 08-mcp-health-check — Run before any session that depends on live MCP data. Required before cross-system writes.
- 01-source-of-truth-registry-auditor — Run when ownership of a data type is in question.
- 10-crm-notion-file-sync-checker — Run before using Notion contact or deal data for decisions.
- 12-notion-mirror-gatekeeper — Required checkpoint before any write to a Notion mirror page.

### Decision and review governance
- 04-open-decisions-manager — Track all unresolved decisions. Every open item needs an owner and a due date.
- 06-pending-review-router — Route pending items to the right owner. No item leaves without an action.
- 03-archive-triage-decay-rater — Score archived content before reuse or deletion.

### Outreach and registry
- 05-signalstrike-scouting-report — Score and profile a prospect before any outreach is written.
- 13-github-repository-registry-builder — Maintain the org-level repo registry. Registry first, code second.

### Cowork operator hard rules
- Run 08-mcp-health-check before any session that reads from or writes to HubSpot or Notion.
- Run 12-notion-mirror-gatekeeper before every Notion write. No exceptions.
- Never write to a Notion mirror before confirming the HubSpot authoritative value.
- Open decisions must have an owner. Decisions deferred more than twice escalate to Scott.
- Session queues are confirmed by Scott before work begins.
