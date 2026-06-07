---
name: crm-notion-file-sync-checker
description: "Compares the active CRM against Notion strategic records to identify missing links, stale next actions, mismatched file status, and CRM transition issues. Claude may flag discrepancies only and may not update CRM or Notion without Scott approval."
---

# Skill: crm-notion-file-sync-checker

## Purpose

Check whether the active CRM and Notion are aligned. Compares operational truth against strategic truth.

## Source-of-Truth Rule

CRM owns operational truth. Notion owns strategic truth. Drive holds supporting artifacts.

## CRM Transition Rule

HubSpot is current CRM. Rate Rocket is expected future CRM. Use CRM-neutral language.

## When to Activate

- "check CRM and Notion"
- "sync check"
- "is the file aligned?"
- "CRM Notion sync"

## Status Ratings

- ALIGNED
- MINOR GAP
- MATERIAL GAP
- BLOCKED
- NEEDS SCOTT

## Guardrails

Claude may flag discrepancies and recommend fixes.

Claude may not update CRM, update Notion records, change relationship tier, change file status, or change next action without Scott approval.

## Final Rule

CRM tells us what is operationally true. Notion tells us what we understand strategically. This skill compares the two and waits for Scott before changing anything.
