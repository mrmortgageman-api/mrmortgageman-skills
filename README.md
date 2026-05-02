# MrMortgageMan API — System Architecture

> AI-powered infrastructure for mortgage lending, lead generation, and real estate content automation.

***

## What This Org Does

This GitHub organization houses the backend systems, AI skill libraries, and web applications that power the **MrMortgageMan** brand ecosystem. Everything here connects to a broader automation stack built around HubSpot, Zapier, Notion, and Claude AI.

***

## Repositories

| Repo | Visibility | Purpose | Status |
|---|---|---|---|
| [mrmortgageman-skills](https://github.com/mrmortgageman-api/mrmortgageman-skills) | Private | Claude AI skill files for content, email, and RevOps | 🟢 Live |
| [mortgage-scenario-engine](https://github.com/mrmortgageman-api/mortgage-scenario-engine) | Private | WOW Calculator API — mortgage scenario modeling | 🟢 Live |
| [nextjs-boilerplate](https://github.com/mrmortgageman-api/nextjs-boilerplate) | Private | Active Next.js application (48 Vercel deployments) | 🟢 Live |
| [skill-library](https://github.com/mrmortgageman-api/skill-library) | Public | Defensive Midfield operator skills for AI agents | 🟢 Live |

***

## System Architecture

```
MrMortgageMan AI Ecosystem
│
├── Content & Marketing Layer
│   └── mrmortgageman-skills (Claude skill files)
│       ├── Phase 1: cold-email, copywriting, email-sequence
│       └── Phase 2: SEO, video scripts, social (planned)
│
├── Product Layer
│   ├── nextjs-boilerplate (web application)
│   └── mortgage-scenario-engine (WOW Calculator API)
│
├── Automation Layer (external)
│   ├── HubSpot CRM
│   ├── Zapier workflows
│   └── Notion Control Tower
│
└── AI Agent Layer (external)
    ├── Claude Code (uses skill files from this org)
    ├── SignalStrike (lead intelligence)
    └── Buyer Supply Engine
```

***

## Tech Stack

- **Frontend:** Next.js, Vercel
- **API:** Node.js (mortgage-scenario-engine)
- **AI:** Claude Code, Claude API
- **CRM:** HubSpot
- **Automation:** Zapier
- **Docs:** Notion

***

## Contact

**Scott Thompson** — Loan Officer & System Architect
🌐 [mrmortgageman.com](https://mrmortgageman.com)

***

*This organization is part of the MrMortgageMan brand. Not all repos are public.*
