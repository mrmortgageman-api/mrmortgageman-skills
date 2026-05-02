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
