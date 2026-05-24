---
name: mcp-health-check
description: >
  Verify that MCP server connections (HubSpot, Notion, Gmail, Google Calendar, Google Drive,
  Airtable, and others in the stack) are reachable and returning valid responses. Use at the
  start of any session that depends on live MCP data, or when a tool call is returning
  unexpected results. Outputs a connection status report with a recommended recovery action
  for any failed or degraded connection.
triggers:
  - "check MCP connections"
  - "are the tools working"
  - "MCP health check"
  - "tool status"
  - "why is HubSpot not responding"
  - "connection check"
  - "verify integrations"
  - "test the stack"
related_skills:
  - source-of-truth-registry-auditor (use if a failed connection affects data ownership)
  - crm-notion-file-sync-checker (use if HubSpot or Notion connection is degraded)
  - scheduled-boot-briefing-builder (include health check in boot sequence)
  - context-stack-refresher (run after recovery to reload any missed context)
---

# MCP Health Check

## Purpose

A bad MCP connection gives bad data or silent failures.
This skill forces a live status check on every connected tool before work that depends on them begins.

---

## MCP Connection Inventory

| Tool | MCP Server | Check Method | Expected Response |
|---|---|---|---|
| HubSpot | claude.ai HubSpot | get_user_details | User name and org returned |
| Notion | claude.ai Notion | notion-search with blank query | Returns page list without error |
| Gmail | claude.ai Gmail | list_labels | Returns label list without error |
| Google Calendar | claude.ai Google Calendar | list_calendars | Returns calendar list without error |
| Google Drive | claude.ai Google Drive | list_recent_files | Returns file list without error |
| Airtable | claude.ai Airtable | ping | Returns pong without error |
| Fireflies | claude.ai Fireflies | fireflies_get_user | Returns user record without error |
| Gamma | claude.ai Gamma | get_gammas | Returns gamma list without error |

---

## Health Check Protocol

Step 1: Run a lightweight check call against each MCP server in the inventory.
Step 2: Record the result: OK, Degraded, or Failed.
Step 3: For any Degraded or Failed connection, attempt one retry after 30 seconds.
Step 4: If still Degraded or Failed after retry, flag for recovery.
Step 5: Output the status report.
Step 6: Do not proceed with session tasks that depend on a Failed connection until recovery is confirmed.

---

## Status Definitions

OK — Tool responded within expected time with valid data.
Degraded — Tool responded but returned partial data, an error code, or exceeded normal response time.
Failed — Tool did not respond or returned an authentication or connection error.

---

## Status Report Format

Health check run: [Date and time]

| Tool | Status | Response time | Notes |
|---|---|---|---|
| HubSpot | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Notion | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Gmail | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Google Calendar | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Google Drive | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Airtable | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Fireflies | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |
| Gamma | [OK / Degraded / Failed] | [ms or timeout] | [One-line note if not OK] |

Overall status: [All OK / Partial — N tools degraded or failed / Critical — core tools down]

---

## Recovery Actions by Status

Degraded:
- Note which data may be incomplete.
- Proceed with caution. Flag any outputs that relied on the degraded connection.
- Retry the connection at the next natural break in the session.

Failed:
- Do not run any session tasks that depend on this tool.
- Check if the MCP server requires re-authentication.
- If re-auth is needed, prompt Scott to complete authentication before proceeding.
- Log the failure and the recovery action in the session log.

---

## Hard Rules

- Do not skip the health check if the session involves a live HubSpot read or write.
- Do not proceed with a cross-system write if the target system shows Failed status.
- A Degraded HubSpot connection is treated as Failed for any write operation.
- Re-authentication requires Scott's action. Claude cannot complete it autonomously.

---

## Quality Check Before Delivering Status Report

- Every tool in the inventory has a status?
- Failed and Degraded tools have a recovery action assigned?
- Session plan adjusted to exclude tasks that depend on Failed connections?
