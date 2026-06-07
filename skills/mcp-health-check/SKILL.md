---
name: mcp-health-check
description: "Checks whether Claude Cowork has access to Notion, Drive, CRM, GitHub, local Cowork files, and Claude skills before acting as an operator."
---

# Skill: mcp-health-check

## Purpose

Check whether Claude Cowork has the required tool access before acting as an operator.

## Activate When

- "run health check"
- "check MCP"
- "are the tools connected?"
- "start Cowork"
- "boot check"

## Systems to Check

- Notion, Google Drive, Active CRM, GitHub, Local Cowork folder, Claude skill library

## Status Labels

- LIVE, LIMITED, NOT AVAILABLE, NOT NEEDED, UNKNOWN

## Session Safety Ratings

- GREEN: Safe to proceed
- YELLOW: Proceed with limitations
- RED: Stop before system action

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM.

## Final Rule

No tool access, no operator action. Claude can think, draft, and advise, but cannot claim live system truth without live system access.
