---
name: email-sequence
description: >
  Create multi-email automated flows and nurture sequences for MrMortgageMan.
  Use when Scott needs a drip campaign, lifecycle email program, buyer nurture sequence,
  post-close follow-up cadence, or Realtor warm-up series. Covers sequence architecture,
  individual email copy, timing, and subject lines. Always read product-marketing-context first.
  Do NOT use for first-touch cold outreach to new agents - that is cold-email.
triggers:
  - "email sequence"
  - "drip campaign"
  - "nurture sequence"
  - "buyer nurture"
  - "post-close emails"
  - "Realtor warm-up"
  - "welcome sequence"
  - "follow-up series"
  - "email cadence"
  - "what emails should I send"
  - "lifecycle emails"
related_skills:
  - product-marketing-context (read first, always)
  - cold-email (for first-touch outreach before a relationship exists)
  - sales-enablement (for pitch decks and one-pagers referenced in sequences)
  - copywriting (for landing page copy tied to sequence CTAs)
---

# MrMortgageMan Email Sequence Skill

## Context Load - Required First Step

Before building any sequence, read product-marketing-context.md.
Confirm the audience type before writing a single email.
The wrong sequence for the wrong audience is worse than no sequence.

---

## Sequence Types This Skill Covers

B2C Sequences (Buyers and Borrowers):
1. Pre-approval nurture (lead opted in, not yet booked)
2. Post-ILC nurture (consulted, not yet in contract)
3. In-transaction update cadence (active file, escrow updates)
4. Post-close follow-up (client for life sequence)
5. Rate watch re-engagement (past leads, market change trigger)

B2B Sequences (Realtor Partners and Referral Partners):
6. Realtor warm-up (new relationship, building trust pre-referral)
7. Realtor in-transaction update (active deal, keep agent informed)
8. Professional referral partner nurture (financial advisor, divorce attorney, accountant)
9. Post-referral thank-you and reinforcement

---

## Hard Rules - Never Break These

Voice rules:
- No em dashes. Use periods or commas.
- No banned words: hopefully, maybe, no problem, best rate, fingers crossed, crushing it, killing it, game-changer, revolutionary, act now, limited time, dont miss out
- Every sentence under 20 words
- Lead with confidence, not pressure
- No mortgage jargon on first read

Email structure:
1. Hook: 1 line. Acknowledge their situation or feeling.
2. Insight: 2-3 sentences. Complexity to clarity.
3. Action: One clear CTA only. Never multiple options.

Subject line rules: No question marks. No emojis. Under 45 characters. Coach tone.

Signature: Mortgage Made Simple, Scott (comma, not period)
Never include full signature block. Outlook appends it.
Template variables use {{double braces}}.

Compliance: No rate quotes in automated sequences. Reference the process, not the number.

---

## Sequence Architecture Rules

Define these before writing any emails:
- Audience: Who is this for exactly?
- Trigger: What action or event starts this?
- Goal: One outcome only.
- Length: How many emails and what spacing?
- Exit condition: What stops the sequence early?

Every sequence needs an exit condition. If they take the desired action, they stop receiving emails.

---

## Sequence 1: Pre-Approval Nurture

Trigger: Lead opts in or is added without booking ILC
Goal: Book the ILC
Length: 4 emails, 10 days
Exit: Books ILC via Calendly

Email 1 - Day 0:
Subject: Your next step with the mortgage
Hook: You took the first step. Here is exactly what happens next.
Insight: What the ILC is, what to bring, what they know after.
CTA: Book your 30-minute ILC: {{calendly_link}}

Email 2 - Day 3:
Subject: The question most buyers ask first
Hook: The most common question before a consultation is about credit.
Insight: Debunk the credit pull myth. One authorized pull does not tank their score.
CTA: If you are ready to run the numbers: {{calendly_link}}

Email 3 - Day 6:
Subject: What a pre-approval actually means
Hook: A pre-approval is not a guarantee. It is a strategy.
Insight: Difference between a pre-qual and a real pre-approval. What Scott actually does.
CTA: Let us build yours. 30 minutes: {{calendly_link}}

Email 4 - Day 10:
Subject: Last note before I close this out
Hook: I do not want to keep filling your inbox if the timing is not right.
Insight: No pressure close. Process is here when they are ready.
CTA: If the timing is ever right: {{calendly_link}}

---

## Sequence 2: Post-ILC Nurture

Trigger: ILC completed. Client not yet in contract.
Goal: Keep Scott top of mind when they find a home
Length: Monthly (indefinite)
Exit: Client submits application or contacts Scott directly

Cadence: Monthly. Not weekly. They consulted. They know who Scott is. Do not over-email.

Monthly email example:
Subject: What buyers in {{market}} are doing right now

{{first_name}}, one pattern I am seeing a lot in {{market}} right now.

Buyers who have their financing dialed in before house hunting are writing cleaner offers. Not because they are offering more money. Because sellers and listing agents can see the loan is real.

If you are still watching the market, the strategy conversation is worth a refresh. Things shift.

Reply here or grab a time: {{calendly_link}}

Mortgage Made Simple, Scott

---

## Sequence 3: In-Transaction Update Cadence

Trigger: Client in contract, file active
Goal: Zero surprises. Everyone informed at every milestone.
Audience: Send buyer version to buyer. Agent version to Realtor simultaneously.
Exit: File closes

Milestone 1 - Application submitted:
Subject: File submitted - here is what is next
Content: Confirm receipt. Explain underwriting process. Set timeline expectations.
CTA: Clare is reachable at {{clare_email}} | {{clare_phone}}

Milestone 2 - Appraisal ordered:
Subject: Appraisal ordered on your file
Content: What an appraisal is, what triggers a problem, what happens if it comes in low.
CTA: No action needed. We will update you when results come back.

Milestone 3 - Conditional approval:
Subject: Conditional approval - what this means
Content: Explain conditions. What they need to provide. Timeline to clear.
CTA: Clare will be in touch with a checklist.

Milestone 4 - Clear to close:
Subject: Clear to close - you are almost there
Content: Congratulate. What happens at signing. What to bring. Wire instructions.
CTA: Signing is scheduled for {{signing_date}}.

Milestone 5 - Closed:
Subject: Congratulations - you did it
Content: Acknowledge the win. Remind them of post-close strategy.
CTA: I will be in touch in 12 months for your annual mortgage review.

---

## Sequence 4: Post-Close Client for Life

Trigger: File closes
Goal: Stay in Scotts orbit. Generate referrals.
Length: Annual plus event-triggered

Annual email (12 months post-close):
Subject: Your mortgage - one year in

{{first_name}}, it has been a year since you closed on {{address}}.

A few things worth reviewing: your equity position, whether your rate still makes sense, and whether anything in your financial picture has changed.

This is not a pitch. It is the annual check-in I do for every client.

15 minutes. Reply here or grab a time: {{calendly_link}}

Mortgage Made Simple, Scott

Event-triggered touches:
- Rate drop of 1% or more from their note rate: send refinance analysis offer
- Major market shift in their neighborhood: send equity update offer
- 3 years post-close: send move-up buyer planning email

---

## Sequence 5: Realtor Warm-Up

Trigger: New Realtor relationship via SignalStrike. Score 3+. First reply or connection made.
Goal: Earn a buyer referral
Length: 4 emails, 6 weeks
Exit: Agent sends a referral or books a call

Email 1 - Week 1:
Subject: Good to connect - one thing I do differently

{{first_name}}, glad we connected.

One thing I do that most lenders skip: I model the buyers payment at multiple price points before they write an offer. Not after. Before.

That means when your buyer wants to write on a home that is $50k over asking, they already know the monthly impact. No surprises in escrow.

If you ever have a buyer where the financing is the wild card, I am worth a conversation.

Mortgage Made Simple, Scott

{{phone}}

Email 2 - Week 2:
Subject: Pre-approval that listing agents trust

{{first_name}}, a quick follow-up on something agents tell me matters.

My pre-approvals include full income analysis, asset sourcing, and debt ratio review. Not a soft pull and a checkbox.

Listing agents notice the difference. It affects whether your offer gets taken seriously in a competitive situation.

Worth a 15-minute call to walk you through how I do it?

Mortgage Made Simple, Scott

Email 3 - Week 4:
Subject: Buyers in {{market}} right now

{{first_name}}, one pattern I am seeing in {{market}} this month.

Buyers who have their financing strategy dialed in before house hunting are moving faster and writing cleaner offers. Not because they have more money. Because they know their number.

Happy to do a quick pre-approval strategy call with any buyer you have. No cost, no commitment.

Mortgage Made Simple, Scott

Email 4 - Week 6:
Subject: Checking in before I move on

{{first_name}}, I have sent a few notes over the past weeks.

If the timing is not right or you have a lender relationship you are happy with, I completely understand. No pressure.

If there is ever a buyer where you want a second opinion on the financing, I am easy to reach.

Mortgage Made Simple, Scott
{{phone}} | {{calendly_link}}

---

## Sequence 6: Professional Referral Partner Nurture

Trigger: Financial advisor, divorce attorney, or accountant identified and initial contact made
Goal: Become the mortgage resource they think of first
Length: Quarterly
Exit: They send a referral

Quarterly email (financial advisor):
Subject: RSU income and mortgage qualification - a note

{{first_name}}, one scenario that comes up often with tech clients.

RSU income is treated differently by underwriters depending on vesting schedule and employment history. It can make or break a loan approval.

If you have clients navigating home purchases with equity compensation, I am worth a conversation before they start shopping.

Happy to be a resource. No obligation on your end.

Mortgage Made Simple, Scott

Quarterly email (divorce attorney):
Subject: Financing through a divorce decree - what works

{{first_name}}, a quick note on something that creates complications.

When one spouse is buying out the other, or when the decree requires a refinance within a timeframe, lenders handle it differently. Not all of them know how to document it correctly.

I have done this more than once. If you have a client in that situation, I am easy to connect with.

Mortgage Made Simple, Scott

---

## Quality Check Before Any Sequence Goes Out

- High school B student understands it?
- Specific situation or insight, not generic advice?
- Exactly one clear next step?
- Builds confidence, not pressure?
- Every sentence under 20 words?
- No em dashes?
- No banned words?
- No rate quotes?
- Exit condition defined?
- Signature is Mortgage Made Simple, Scott (comma, not period)?

---

## Output Format

Sequence: [Name]
Audience: [Who]
Trigger: [What starts it]
Goal: [One outcome]
Exit condition: [What stops it early]
Length: [Number of emails, spacing]

Then for each email:
Email [number] - [Timing]
Subject: [Subject line]
---
[Email body]
---
Notes: [Any personalization instructions]
