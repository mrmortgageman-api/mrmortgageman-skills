---
Type: Builder Brief (Execution)
Status: CURRENT
Issued: 2026-07-14
Issued By: Digital Chief of Staff (Claude)
Authority: Scott Thompson
Builder: Claude Code
Repo: mrmortgageman-api/mrmortgageman-skills
File: loan-strategy-presenter/MMM_Loan_Strategy_Presenter.html
Governs: This file only. Do not touch app/tca-apex or the nextjs-boilerplate repo. Different system, different sprint.
---

# BUILD BRIEF — Four-Layer Flexible-Count TCA Presenter

## 1. WHY THIS BRIEF EXISTS

Scott locked a doctrine on 2026-06-18 that scenario cards must show four layers, Product, Strategy, Why, Outcome, always in that order. The `loan-strategy-presenter` skill (SKILL.md, already updated, commit `1f6e7ee`) now instructs Claude to build cards this way, and to build anywhere from 1 to 4 cards depending on what Scott provides. The HTML template the skill renders into does not support either change yet. It is hardcoded to exactly 4 scenario slots in the edit drawer, the data model, the chart color arrays, and the KPI logic, and its scenario cards only show a partial mix of Product and Outcome data with no Why sentence anywhere.

This brief closes that gap. Read it fully before touching code.

**Source doctrine (read these first):**
- Notion: `🔍 APEX_DESIGN_DISCOVERY_StrategyNamesAreNotLoanProducts_2026-06-18` (LOCKED)
- GitHub: `loan-strategy-presenter/SKILL.md` (already updated, this is your spec for card content and behavior)

## 2. WHAT "AMAZING" MEANS HERE

This is a client-facing, screen-share-live, PDF-leave-behind tool. Nothing about the rebuild should look like a patch. When you're done:
- A 1-scenario file, a 3-scenario file, and a 4-scenario file should all look intentionally designed, not like a 4-slot grid with empty holes.
- The four-layer card should read top to bottom like an answer, not a form: what is it, what's it for, why would I pick it, what does it get me.
- Dark mode, print, and the live-edit drawer must survive untouched in behavior, just generalized to N scenarios instead of 4.

## 3. CURRENT STATE (WHAT'S BROKEN)

Confirmed by direct read of the live file on `main`:

1. **Hardcoded 4-slot data model.** `DATA.scenarios` is a fixed 4-item array. Edit drawer inputs are literally `ei-r0` through `ei-r3` / `ei-p0` through `ei-p3`, written individually into the HTML, not generated.
2. **No Why Layer.** Cards show label, rate, points, P&I, PITIA, optional net carry, cash to close, equity. No philosophy sentence anywhere.
3. **Incomplete Product Layer.** Loan type and term live once in the global header (`d.loanType`), not per scenario. A file where Conservative is a 15-year and Balanced is a 30-year cannot render correctly today.
4. **Math engine assumes 30-year term for every scenario.** `calcPI`, `buildCurve`, and the interest/principal loop in `buildScenarios` all hardcode `30` or a 120-month (10-year) loop. No per-scenario term support, no full-term total interest, no payoff date.
5. **KPI row hardcodes index 3.** `S[3].pit` is used directly for the "Lowest PITIA / Wealth accelerator" KPI card. Breaks the moment fewer than 4 scenarios exist, or the order changes.
6. **Chart color arrays and legends assume 4.** `CL` / `CD` are 4-item arrays indexed positionally. Fine to keep as a 4-color palette, but every place that reads `CL[i]` needs to key off the scenario's fixed label identity, not its position in a possibly-shorter array, so a lone Conservative card doesn't render in the "Current Loan" navy.
7. **Casing mismatch.** Default `DATA.scenarios` labels are `"Current loan"` and `"Wealth accelerator"` (sentence case). The doctrine's locked label set and Why-sentence lookup use `"Current Loan"` and `"Wealth Accelerator"` (title case). This needs to be normalized everywhere or the Why-sentence lookup will silently fail.

## 4. LOCKED LABEL SET AND WHY SENTENCES (DO NOT CHANGE WORDING)

```js
const SCENARIO_LABELS = ["Current Loan", "Conservative", "Balanced", "Wealth Accelerator"];

const WHY_SENTENCES = {
  "Current Loan":       "Preserves maximum monthly cash flow.",
  "Conservative":       "Lowest risk. Highest certainty. Fastest payoff.",
  "Balanced":           "Balances monthly payment and long-term wealth creation.",
  "Wealth Accelerator": "Maximizes equity and minimizes total interest paid.",
};

const SCENARIO_COLORS_LIGHT = {
  "Current Loan":       "#1e3a5f",
  "Conservative":       "#01696f",
  "Balanced":           "#437a22",
  "Wealth Accelerator": "#d19900",
};

const SCENARIO_COLORS_DARK = {
  "Current Loan":       "#5591c7",
  "Conservative":       "#4f98a3",
  "Balanced":           "#6daa45",
  "Wealth Accelerator": "#e8af34",
};
```

Colors and Why sentences are keyed by label identity, never by array position. This is what makes a lone Conservative card still render in teal instead of defaulting to navy because it happened to be `scenarios[0]`.

## 5. DATA MODEL — TARGET SHAPE

Replace the fixed 4-item `DATA.scenarios` array with a variable-length array, 1 to 4 entries, each carrying its own full Product Layer:

```js
const DATA = {
  borrowerName:  "",
  subtitle:      "",
  reportDate:    "",
  closingDate:   "",       // NEW — used for payoff date math. Falls back to reportDate if absent.
  fileTypeLabel: "",
  inv:           false,
  purchasePrice: 0,
  downPayment:   0,
  loanAmount:    0,        // NEW — explicit, don't only derive from price - down, some scenarios may have different loan amounts (buydown points financed, etc.) — default derivation stays purchasePrice - downPayment unless a scenario overrides.
  taxMonthly:    0,
  insMonthly:    0,
  hoaMonthly:    0,
  rentMonthly:   0,
  recScenario:   "",       // must be a label present in DATA.scenarios
  recText:       "",
  scenarios: [
    // 1 to 4 of these, in the fixed label order when multiple are present:
    // Current Loan, Conservative, Balanced, Wealth Accelerator
    {
      label:       "Balanced",              // must be one of SCENARIO_LABELS
      loanType:    "30-Year Conventional Fixed",  // Product Layer
      termYears:   30,                             // Product Layer — per-scenario now
      rate:        6.25,                            // Product Layer
      pts:         0.5,                              // Product Layer
      loanAmount:  0,   // optional override, defaults to DATA.loanAmount
      downPayment: 0,   // optional override, defaults to DATA.downPayment
      featured:    true,  // replaces old `ft:true`, drives "Most balanced path" badge + border
    },
    // ...
  ]
};
```

**Validation rule to build in:** if `DATA.scenarios.length` is 0 or greater than 4, or any `label` is not in `SCENARIO_LABELS`, throw a clear console error and render a visible error state instead of silently breaking. This tool goes live on a screen share, it should never fail quietly.

## 6. MATH ENGINE CHANGES

- `calcPI(loan, rate, years)` already takes `years`. Stop hardcoding `30` when calling it. Pull `termYears` from each scenario.
- `buildCurve(loan, rate, years)` needs the same treatment. The 10-year amortization chart stays a 10-year window regardless of term (that's a fixed comparison horizon, keep it), but the payment calculation itself must use the scenario's actual term.
- **New: full-term total interest paid.** Run the amortization loop for the scenario's actual `termYears * 12` months (not fixed 120), sum total interest across the full term. This is the doctrine's Outcome Layer "Total interest paid" field, distinct from the existing 10-year snapshot used for the chart. Keep both: `hi10` (10yr interest, powers the chart/table if you want to preserve it) and `totalInterest` (full term, powers the Outcome Layer).
- **New: payoff date.** `closingDate` (or `reportDate` fallback) plus `termYears` in months, formatted as a readable date (e.g. "August 2056").
- Equity-at-10-years logic stays as-is, it's horizon-based by design, not term-based.

## 7. SCENARIO CARD — FOUR-LAYER LAYOUT

Rebuild the `.sc` card markup and CSS to render, top to bottom, no exceptions:

**Layer 1 — Product.** Small, factual, sits above the strategy name. Loan type, rate, term, down payment, points. This is the borrower's "what am I looking at" anchor.

**Layer 2 — Strategy.** The label, styled the way the current `.sn` header already is (Instrument Serif italic). This is identity, not data.

**Layer 3 — Why.** One sentence, pulled verbatim from `WHY_SENTENCES[label]`. Give this its own visual treatment, distinct from the metric rows, e.g. a short italic or accent-colored line directly under the strategy name. It should read like a caption, not a data row.

**Layer 4 — Outcome.** The metric rows: P&I, PITI/PITIA, total interest paid (full term), equity at horizon, payoff date, net carry (investment mode only).

Featured card (`featured: true`, normally Balanced) keeps its existing teal border treatment (`.sc.ft`) and badge, just re-skinned to sit correctly with the new layer order.

**Card count behavior:**
- 1 card: no grid needed, center it, cap width so it doesn't stretch full-bleed and look like an empty layout.
- 2-4 cards: existing `auto-fit, minmax(225px,1fr)` grid behavior is fine, just driven by `DATA.scenarios.length` instead of a fixed 4.

## 8. EVERYTHING ELSE THAT MUST GO DYNAMIC

Audit every place in the current file that assumes exactly 4 scenarios and generalize it to `DATA.scenarios.length`:

- **Edit drawer:** generate the `.scenario-input-group` blocks in JS from `DATA.scenarios`, not as 4 static HTML blocks with `ei-r0..r3`/`ei-p0..p3` ids. Use `ei-r-${label}` / `ei-p-${label}` (or an index into the live array) so it scales to any count.
- **KPI row:** replace the hardcoded `S[3].pit` "Lowest PITIA" card with logic that finds `Math.min` across whatever scenarios actually exist, and labels it dynamically with that scenario's actual label, not a hardcoded "Wealth accelerator" string.
- **Comparison table:** already builds columns from `S.map(...)`, this one mostly works, just confirm it degrades cleanly at 1 column (no orphaned borders/padding looking broken).
- **Equity bars:** already loops over `S`, same as above, confirm 1-bar case looks intentional, not just a maxed-out single bar.
- **Charts:** both charts already map over `S` for datasets, this is close to fine already, just make sure the line chart legend doesn't look sparse/off-center with 1-2 datasets. Consider hiding chart 2 (balance line) entirely when there's only 1 scenario, since a single-line "comparison" chart isn't a comparison. Use judgment, this is called out in the skill doc too.

## 9. RECOMMENDATION LOGIC

- If a `Balanced` scenario is present among `DATA.scenarios`, it is `featured: true` and is `DATA.recScenario` by default.
- If not present, whatever Scott set as `DATA.recScenario` drives the featured card. Don't invent a default, trust the data Claude/Scott provided.
- If only one scenario exists, it's featured by definition, the "Most balanced path" badge language should probably just not show (there's no comparison happening), swap for something like "Your scenario" or suppress the badge entirely. Use judgment, flag your choice in the PR description.

## 10. BACKWARD COMPATIBILITY

Every existing 4-scenario file (this is still the common case, Stage 2 calls default to all four) must render identically in substance to today's output, just with the new four-layer card content added. Don't regress the polish that's already there (hover states, click-to-highlight during calls, dark mode transitions, print stripping the UI chrome).

## 11. TEST MATRIX BEFORE HANDOFF

Build and visually check all of these before calling it done:

1. **4 scenarios, purchase file** (current default case) — confirm four-layer cards, confirm nothing regressed.
2. **3 scenarios, purchase file, no Wealth Accelerator** — real case waiting on this: Raymond & Sharon Young, loan #1002371682, three rate points already modeled (6.500% / 6.625% / 6.750%), no Balanced/Conservative/Wealth Accelerator framing was used originally, so this is also a good test of mapping arbitrary rate comparisons onto the locked label set, flag if that mapping is ambiguous rather than guessing silently.
3. **1 scenario, investment file** — confirm net carry still shows, confirm layout doesn't look broken/empty at 1 card, confirm chart 2 behavior per your judgment call above.
4. **Dark mode toggle** on all three above.
5. **Print / Save PDF** on the 4-scenario case, confirm drawer/toggle/Calendly button still strip correctly.
6. **Live edit drawer**, add and remove a scenario's rate live if your dynamic-generation approach supports it, otherwise confirm it correctly reflects whatever `DATA.scenarios` was loaded with.

## 12. OUT OF SCOPE

- Do not touch `app/tca-apex/page.jsx` or anything in `nextjs-boilerplate`. That's a separate build (TCA APEX Sprint 1, gated on Brennan Fong validation), different repo, different sprint, different doctrine thread.
- Do not change the Why-sentence wording, the label set, or the brand colors/logo/Calendly link.
- Do not change the compliance footer language.

## 13. WHEN DONE

- Commit to `main` (or a short-lived branch + note it in your handoff if you'd rather Scott eyeball a diff first, your call given the size of this change).
- Update `loan-strategy-presenter/SKILL.md`'s "OUTPUT" section only if your implementation changes the numbered render-order list, otherwise leave it, it's already correct.
- Report back: what you built, what judgment calls you made (chart-2-at-1-scenario, single-card badge language, etc.), and confirmation the test matrix in Section 11 passed.

Mortgage Made Simple.
