# mrmortgageman-skills

> **Status: LIVE** — Phase 1 skill library for the MrMortgageMan AI system.

This repo contains all Claude-compatible skill files used across the MrMortgageMan content, marketing, and RevOps workflows. Skills are loaded by Claude Code and AI agents to execute specialized tasks without manual prompting.

---

## Extended Skill Index

| File | Purpose | Typical Use Cases | Status |
|---|---|---|---|
| `cold-email.md` | Cold outreach email generation for real estate agents and buyers | First-touch outreach, follow-ups on lead lists, agent recruiting sequences | ✅ Live |
| `copy-editing.md` | Editing and polishing copy for clarity, tone, and conversion | Tightening emails, landing pages, scripts, and social posts while keeping Scott’s voice | ✅ Live |
| `copywriting.md` | Long-form and short-form copy generation | Landing pages, ad copy, social captions, video scripts, webinar promos | ✅ Live |
| `email-sequence.md` | Multi-step drip sequence writing for lead nurture flows | New lead nurture, post-application follow-up, realtor partner onboarding | ✅ Live |
| `product-marketing-context.md` | Brand voice, ICP, and positioning context | Shared context file that other skills read so everything stays on-brand | ✅ Live |
| `revops.md` | Revenue operations instructions for HubSpot pipeline and workflow automation | Describing lifecycle stages, deal stages, automation rules, and reporting expectations | ✅ Live |

---

## Repo Structure
mrmortgageman-skills/
├── CLAUDE.md # Claude Code root instructions
├── /.claude/
│ └── settings.local.json # Local Claude Code settings
└── /skills/
├── cold-email.md
├── copy-editing.md
├── copywriting.md
├── email-sequence.md
├── product-marketing-context.md
└── revops.md

text

---

## How This Repo Fits Into The System

This repo is the **LIVE skill source of truth** for the MrMortgageMan AI ecosystem. Claude Code and other AI agents pull from these files when:
- Writing or editing outbound and nurture emails
- Generating marketing and sales copy
- Following RevOps rules for HubSpot pipelines and workflows

The skills are designed to be:
- **Composable** — you can load multiple skills in the same session
- **Upgradable** — Phase 2 and 3 skills can be added without breaking the Phase 1 set
- **Documented** — each skill file includes clear operator instructions

---

## Usage Patterns

### With Claude Code
- Open this repo in Claude Code
- Claude automatically reads `CLAUDE.md` and can load any file in `/skills/`
- Reference skills by filename (for example: `cold-email`, `revops`)

### With Other AI Sessions
- Copy-paste the contents of the relevant skill file into the system prompt
- Or, attach the file as a reference document at the beginning of the session

### Skill Naming Convention
All skill files use lowercase, hyphenated names that match their function. When referencing skills in prompts, use the filename without the `.md` extension.

---

## Phase Roadmap

| Phase | Skills | Focus | Status |
|---|---|---|---|
| Phase 1 | cold-email, copy-editing, copywriting, email-sequence, product-marketing-context, revops | Core content + RevOps | ✅ Complete |
| Phase 2 | seo-content, video-script, social-media, hubspot-automation | Top-of-funnel traffic + deeper HubSpot hooks | 🔜 Planned |
| Phase 3 | lead-scoring, deal-analysis, market-report | Intelligence layer and decision support | 🔜 Planned |

---

## Related Repositories

- `skill-library` — Defensive Midfield operator skills (public)
- `mortgage-scenario-engine` — WOW Calculator API
- `nextjs-boilerplate` — Active Next.js application

---

*Part of the MrMortgageMan AI infrastructure. For a high-level map, see the `mrmortgageman-api` org profile README.*

---

## Cowork Operator Pack — Phase 2

Phase 2 adds 13 operator skills focused on session management, system health, data integrity,
and cowork workflow governance. All skills live in `skills/cowork-operator-pack/`.

| File | Purpose | Typical Use Cases | Status |
|---|---|---|---|
| `01-source-of-truth-registry-auditor.md` | Audit which system owns each data type and surface conflicts | Data ownership disputes, new integration onboarding, cross-system sync prep | ✅ Live |
| `02-cowork-session-closer.md` | Close a cowork session with a structured log and next-session boot queue | End of every cowork session | ✅ Live |
| `03-archive-triage-decay-rater.md` | Score archived content by accuracy, relevance, and reusability | Workspace cleanup, content library audits, vault triage | ✅ Live |
| `04-open-decisions-manager.md` | Track, surface, and force resolution on unresolved decisions | Ongoing decision governance, session close, queue building | ✅ Live |
| `05-signalstrike-scouting-report.md` | Build a scored outreach-ready dossier on a prospect before Touch 0 | Agent evaluation, prospect scoring, outreach prep | ✅ Live |
| `06-pending-review-router.md` | Route pending items to the right owner and next action | Review queue management, approval routing, session triage | ✅ Live |
| `07-cowork-queue-manager.md` | Build, prioritize, and time-box the active session queue | Session start, mid-session triage, carry-forward management | ✅ Live |
| `08-mcp-health-check.md` | Verify all MCP server connections before session work begins | Session boot, tool failure diagnosis, pre-write safety check | ✅ Live |
| `09-context-stack-refresher.md` | Reload prior session context so work continues without re-briefing | Every session start that follows a prior cowork session | ✅ Live |
| `10-crm-notion-file-sync-checker.md` | Verify HubSpot and Notion records are in sync field by field | Contact and deal data integrity checks, pre-outreach sync audit | ✅ Live |
| `11-scheduled-boot-briefing-builder.md` | Build a five-section morning briefing for scheduled or recurring sessions | Daily boot, recurring scheduled session setup | ✅ Live |
| `12-notion-mirror-gatekeeper.md` | Gate all Notion writes with a classification and approval checkpoint | Any session that writes to Notion, cross-system update workflows | ✅ Live |
| `13-github-repository-registry-builder.md` | Build and maintain the org-level GitHub repository registry | Repo onboarding, org audit, skill-to-repo mapping | ✅ Live |

### Phase 2 Repo Structure Addition

```
skills/
└── cowork-operator-pack/
    ├── 01-source-of-truth-registry-auditor.md
    ├── 02-cowork-session-closer.md
    ├── 03-archive-triage-decay-rater.md
    ├── 04-open-decisions-manager.md
    ├── 05-signalstrike-scouting-report.md
    ├── 06-pending-review-router.md
    ├── 07-cowork-queue-manager.md
    ├── 08-mcp-health-check.md
    ├── 09-context-stack-refresher.md
    ├── 10-crm-notion-file-sync-checker.md
    ├── 11-scheduled-boot-briefing-builder.md
    ├── 12-notion-mirror-gatekeeper.md
    └── 13-github-repository-registry-builder.md
```

### Phase 2 Skill Chains

**Session open chain:** `08-mcp-health-check` → `09-context-stack-refresher` → `07-cowork-queue-manager`

**Session close chain:** `04-open-decisions-manager` → `06-pending-review-router` → `02-cowork-session-closer`

**Outreach prep chain:** `05-signalstrike-scouting-report` → `cold-email` → `revops`

**Data integrity chain:** `01-source-of-truth-registry-auditor` → `10-crm-notion-file-sync-checker` → `12-notion-mirror-gatekeeper`
