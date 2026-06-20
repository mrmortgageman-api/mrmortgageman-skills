# Builder PQ Intake — AI Prompt (Canonical)

**Status:** v1 LOCKED | 2026-06-20 | Source of Truth

---

## 🤖 Prompt Instructions (Copy + Paste into Claude / ChatGPT)

Generate **only** the "Key Details" and "Opportunity Summary" sections for a Builder PQ submission email.

### Context
- This is from an in-person builder community interaction
- All information is borrower-stated (not verified)
- AUS has not been run yet in most cases
- Goal is to present the file as an Opportunity PQ whenever reasonable
- Tone: Builder-friendly, forward-moving, concise and direct
- Never overly confident or definitive

### Rules
- Default to Opportunity framing
- Use "stated" for all income, assets, and credit references
- Keep each bullet to one clean sentence
- Opportunity Summary should explain the path forward, not just issues
- All language protects legally at every interaction

---

## Input Section (Fill From Notion Tap Selections)

Copy your tap selections from the ⚡ Builder PQ Intake database and paste below:

```
Payment Goal: [PASTE SELECTION]
Buyer Profile: [PASTE SELECTIONS - can be multiple]
Assets: [PASTE SELECTIONS - can be multiple]
Credit: [PASTE SELECTION]
Income Type: [PASTE SELECTIONS - can be multiple]
Program Direction: [PASTE SELECTION]
Opportunity Driver: [PASTE SELECTION]
Strength Tag: [PASTE SELECTION]
```

---

## Output Format (What You Get Back)

The AI will return this structure. Copy everything below "Key Details:" through "Opportunity Summary:" and paste into your Outlook email over the bullet section:

```
Key Details:
- Payment Goal: [Stated payment target]
- Buyer Profile: [Profile description]
- Assets: [Asset summary]
- Credit & Income: [Credit score range and income type]
- AUS Findings: Not yet run / TBD
- Program Fit: Likely [Conventional/FHA/Pathway] — subject to full review

Opportunity Summary:
[1-2 sentences describing the forward path: profile is {Strength Tag} pending {Opportunity Driver}]
```

---

## Example Workflow

**Input (from Notion taps):**
```
Payment Goal: Payment Sensitive ~$3500
Buyer Profile: FTHB, Currently Renting
Assets: Limited Liquid Assets, Gift Funds Available
Credit: 660-699 Workable Credit
Income Type: Salaried Stable
Program Direction: FHA
Opportunity Driver: Pending Income Documentation
Strength Tag: Workable Structure
```

**Output (what AI generates):**
```
Key Details:
- Payment Goal: Payment sensitive, targeting approximately $3,500 monthly payment
- Buyer Profile: First-time home buyer, currently renting
- Assets: Limited liquid reserves, but gift funds available for down payment
- Credit & Income: 660-699 workable credit, salaried employment (stable)
- AUS Findings: Not yet run / TBD
- Program Fit: Likely FHA — subject to full review

Opportunity Summary:
Profile is a workable structure pending income documentation review. Once pay stubs and employment verification are provided, file will be ready for full underwriting.
```

---

## Quick Copy-Paste Prompt (For Speed)

Paste this directly into Claude or ChatGPT for fastest output:

---

**[START PASTE HERE]**

Generate only the "Key Details" and "Opportunity Summary" sections for a Builder PQ submission email.

Context: In-person builder community interaction. All information is borrower-stated (not verified). AUS has not been run yet. Default to Opportunity PQ framing.

Tone: Builder-friendly, forward-moving, concise, direct.

Rules: Use "stated" for all income/assets/credit. Keep bullets to one sentence. Opportunity Summary explains path forward. All language is protective.

Input values:
- Payment Goal: [PASTE FROM NOTION]
- Buyer Profile: [PASTE FROM NOTION]
- Assets: [PASTE FROM NOTION]
- Credit: [PASTE FROM NOTION]
- Income Type: [PASTE FROM NOTION]
- Program Direction: [PASTE FROM NOTION]
- Opportunity Driver: [PASTE FROM NOTION]
- Strength Tag: [PASTE FROM NOTION]

Output format:

Key Details:
- Payment Goal: [stated]
- Buyer Profile: [stated]
- Assets: [stated]
- Credit & Income: [stated]
- AUS Findings: Not yet run / TBD
- Program Fit: Likely [program] — subject to full review

Opportunity Summary:
[1-2 sentences: profile is {Strength Tag} pending {Opportunity Driver}]

**[END PASTE]**

---

## Canonical Guarantee

This prompt is locked. Do not modify without Scott approval. All PQ emails must use this prompt version.

If you find the output doesn't match expectations, file an issue in the mrmortgageman-skills repo or contact Scott directly.

**Last Updated:** 2026-06-20 | **Next Review:** TBD
