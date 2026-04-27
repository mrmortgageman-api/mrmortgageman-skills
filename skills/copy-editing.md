---
name: copy-editing
description: >
  Edit, review, and improve existing MrMortgageMan marketing copy, email templates,
  QUO snippets, and communication drafts. Use when Scott needs to polish an existing
  piece of writing before it goes out, audit a template library for voice compliance,
  or fix copy that sounds off. Flags em dashes, banned words, weak CTAs, over-length
  sentences, and AI-sounding language. Always read product-marketing-context first.
  Do NOT use to write new copy from scratch - that is copywriting.
triggers:
  - "edit this email"
  - "fix this template"
  - "review this copy"
  - "polish this"
  - "audit my templates"
  - "does this sound right"
  - "check this against voice"
  - "clean this up"
  - "QUO snippet"
  - "Notion template"
  - "flag the issues"
  - "run a voice check"
related_skills:
  - product-marketing-context (read first, always)
  - copywriting (for writing new copy from scratch)
  - cold-email (for outreach-specific voice standards)
  - email-sequence (for sequence-specific structure rules)
---

# MrMortgageMan Copy-Editing Skill

## Context Load - Required First Step

Before editing anything, read product-marketing-context.md.
Voice standards, banned words, and approved phrases all live there.
Do not edit without loading that context first.

---

## What This Skill Does

This skill does two things:

1. Audit mode: Scans a piece of copy and returns a flagged report with every issue found and a corrected version.
2. Polish mode: Takes a draft and returns a clean, ready-to-send version in MrMortgageMan voice with no issues.

When Scott pastes a template, snippet, or draft, default to Audit + Polish.
Show what was wrong, then show the fixed version.

---

## The 7-Point Voice Checklist

Run every piece of copy against all 7 points before delivering output.

1. Em Dash Check
Em dashes are never permitted. Zero exceptions.
Find every em dash and replace with a period or comma.

Flag: "rates are moving - here is what that means"
Fix: "rates are moving. Here is what that means."

2. Banned Word Scan
Banned list: hopefully, maybe, no problem, best rate, fingers crossed, crushing it, killing it, game-changer, revolutionary, act now, limited time, dont miss out

Flag: "hopefully this helps"
Fix: "this should help clarify the situation"

3. AI-Sounding Opener Scan
Banned openers: "I hope this email finds you well", "I wanted to reach out", "I came across your profile", "Just checking in", "Touching base", "Circling back", "Per my last email", "As per our conversation"

Fix: Replace with a specific, direct opener tied to the readers situation.

4. Sentence Length Check
Every sentence must be under 20 words. Count them. Do not estimate.
Flag any sentence over 20 words and break it into two.

5. CTA Check
Every email or message must have exactly one CTA.
Zero CTAs = problem. Two or more CTAs = problem.
Also flag: "act now", "dont miss out", "click here", "learn more".

Flag (two CTAs): "Reply here or call me or grab a time on my calendar"
Fix: "Grab a time here: {{calendly_link}}"

6. Signature Check
Every email must end with: Mortgage Made Simple, Scott
Comma after Simple. Not a period.
No full signature block in templates (Outlook appends it automatically).

Flag: "Best, Scott Thompson | Senior Loan Consultant"
Fix: "Mortgage Made Simple, Scott"

7. Confidence vs Pressure Check
Flag any language that creates urgency through fear or scarcity.

Flag: "Rates could go up any day. Don't wait."
Fix: "Smart strategy beats perfect timing. Let us run your numbers now."

---

## Bonus Checks

Template Variable Format: All variables must use {{double braces}}.
Flag: [First Name], (First Name), {first_name}
Fix: {{first_name}}

Subject Line Check (email only): No question marks. No emojis. Under 45 characters. Coach tone.
Flag: "Are you ready to buy your dream home?"
Fix: "Your next step with the mortgage"

Jargon Check: Flag mortgage jargon a non-industry reader would not understand.
Flag: "Your DTI needs to be under 43% for conforming"
Fix: "Your monthly debt payments need to stay below 43% of your gross income to qualify"

Passive Voice Check: Flag passive constructions and rewrite as active.
Flag: "The pre-approval will be sent by Clare"
Fix: "Clare will send your pre-approval"

---

## Audit Report Format

COPY AUDIT - [Name of piece]
Issues found: [number]

---

Issue 1 - [Type]
Original: [exact text]
Problem: [one-line explanation]
Fix: [corrected text]

...

---

CLEAN VERSION:
[Full corrected copy]

---

Quality check: Pass / [Note if anything still needs Scotts review]

---

## Polish Mode Format

When Scott says "just clean this up" or polish this:
Skip the audit report. Deliver the clean version only.
Add a one-line note at the bottom if anything significant changed.

POLISHED VERSION:
[Full corrected copy]

---
Changes made: [2-3 bullet summary]

---

## Notion Template Library Audit

When Scott asks to audit a batch of templates:
Run each through all 7 checks.
Deliver a summary table first, then corrected versions one by one.

Severity scale:
- High: banned words, no CTA, wrong signature, or AI-sounding opener
- Medium: sentence length, em dash, passive voice
- Low: variable format, minor tone issues

---

## QUO Snippets Standards

QUO snippets are used on live phone calls. Different rules:
- Conversational. Should sound natural spoken aloud.
- Short. One idea per snippet. Maximum 3 sentences.
- No subject lines needed.
- CTAs are verbal: "Let me send you the link" not "Click here"
- No signature needed in QUO snippets

Stages: First Touch / Active Transaction / Post-Close / Objection Handling
Flag any snippet that does not match its stage label.

---

## Quality Standard

The bar for passing: Scott can copy-paste and send without reading it twice.
If Scott would stop and question any word, sentence, or CTA, it has not passed.
Fix it until it passes.
