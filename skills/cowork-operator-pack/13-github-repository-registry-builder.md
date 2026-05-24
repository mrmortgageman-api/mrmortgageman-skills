---
name: github-repository-registry-builder
description: >
  Build and maintain a structured registry of all repositories under the mrmortgageman-api
  GitHub organization. Use when onboarding a new repo, auditing the current org structure,
  or answering the question of which repo owns which part of the system. Outputs a
  registry table with repo name, purpose, status, tech stack, and related skills or systems.
triggers:
  - "build the repo registry"
  - "what repos do we have"
  - "GitHub org audit"
  - "repository registry"
  - "add a repo to the registry"
  - "which repo handles this"
  - "org structure"
  - "update the registry"
related_skills:
  - source-of-truth-registry-auditor (use to confirm which system owns repo-level data)
  - notion-mirror-gatekeeper (use if registry is written to Notion)
  - mcp-health-check (verify GitHub connection before running org audit)
  - cowork-session-closer (log registry updates in session log)
---

# GitHub Repository Registry Builder

## Purpose

The mrmortgageman-api org holds multiple repos with different owners and purposes.
Without a registry, it is easy to build in the wrong place, duplicate functionality,
or lose track of what is live. This skill maintains the authoritative registry.

---

## Registry Schema

Each repo in the registry gets a record with these fields:

| Field | Description |
|---|---|
| Repo name | Full name as it appears in GitHub (e.g. mrmortgageman-api/mrmortgageman-skills) |
| Status | Live / In Development / Archived / Deprecated |
| Purpose | One sentence — what this repo does |
| Primary tech | Language, framework, or file type (e.g. Markdown, Next.js, Python) |
| Owner | Scott / Engineering / AI Operator |
| Related skills | Skill files that reference or depend on this repo |
| Related systems | HubSpot, Notion, Claude Code, or other tools that read from or write to this repo |
| Last updated | Date of most recent commit or meaningful change |
| Notes | Any active work, blockers, or upcoming changes |

---

## Known Registry (Current State)

| Repo | Status | Purpose | Tech | Owner |
|---|---|---|---|---|
| mrmortgageman-api/mrmortgageman-skills | Live | Claude-compatible skill library for content, marketing, and RevOps | Markdown | Scott / AI Operator |
| mrmortgageman-api/nextjs-boilerplate | Live | Active Next.js application | Next.js / TypeScript | Engineering |
| mrmortgageman-api/mortgage-scenario-engine | Live | WOW Calculator API | API / Backend | Engineering |
| mrmortgageman-api/skill-library | Live | Defensive Midfield operator skills (public) | Markdown | AI Operator |

---

## Registry Build Protocol

Step 1: List all repos in the mrmortgageman-api org using GitHub API or manual input from Scott.
Step 2: For each repo, populate all fields in the registry schema.
Step 3: Flag any repo with Status Deprecated or Archived for Scott's review.
Step 4: Flag any repo with no commit in the last 90 days as potentially stale.
Step 5: Identify any gaps — functionality that should be in a repo but does not have one.
Step 6: Output the registry table.
Step 7: Log any updates to the registry in the session log.

---

## Adding a New Repo to the Registry

When a new repo is created:

1. Add it to the registry with all fields populated before the first commit is made.
2. Assign an owner immediately. Unowned repos create governance gaps.
3. Link it to any related skill files or systems it will interface with.
4. Set Status to In Development until the first production-ready release.
5. Note the relationship to existing repos (does it replace, extend, or stand alone?).

---

## Registry Health Checks

Run these checks each time the registry is updated:

- Every repo has an owner assigned.
- Every Live repo has a commit within the last 30 days or a documented reason for inactivity.
- No two repos have the same stated purpose (duplication check).
- Every repo listed in a skill file's related_skills field exists in the registry.
- Deprecated repos are not referenced in any active skill file.

---

## Hard Rules

- The registry lives in mrmortgageman-skills. It is not mirrored to Notion without Scott's approval.
- Deprecated repos stay in the registry with Status Deprecated. They are not deleted from the registry.
- Adding a new repo to the org without a registry entry is not allowed. Registry first, code second.
- Owner is never left blank. If ownership is unclear, escalate to Scott before adding the repo.

---

## Quality Check Before Delivering Registry

- Every repo has all schema fields populated?
- Stale repos (no commit in 90 days) are flagged?
- New repos have an owner and a status?
- Deprecated repos are present but clearly marked?
- No duplicate purposes in the registry?
