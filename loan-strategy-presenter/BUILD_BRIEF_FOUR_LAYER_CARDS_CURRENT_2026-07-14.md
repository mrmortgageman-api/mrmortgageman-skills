# BUILD BRIEF — Four-Layer Flexible Scenario Cards
**Target file:** `loan-strategy-presenter/MMM_Loan_Strategy_Presenter.html`
**Repo:** mrmortgageman-api/mrmortgageman-skills
**Branch:** feature/four-layer-cards (open PR against main, do not push directly)
**Status:** READY FOR BUILD
**Owner:** Scott Thompson
**Builder:** Claude Code
**Filed:** 2026-07-14
**Governs:** MMM Loan Strategy Presenter HTML template only. Does not touch TCA APEX (`app/tca-apex/page.jsx`) or the MVP (`app/tca-mvp/page.jsx`) in `nextjs-boilerplate`. Those are separate systems, separate sprint, do not touch.

---

## 1. WHY THIS EXISTS

Two locked doctrine documents govern this build. Read both before writing code.

1. **🔍 APEX_DESIGN_DISCOVERY_StrategyNamesAreNotLoanProducts_2026-06-18** (Notion, LOCKED)
   Core rule: strategy names (Conservative, Balanced, Wealth Accelerator, Current Loan) are philosophies, not loan products. A borrower must never have to ask "what loan product is the Balanced scenario?" Every scenario card must show four layers, in order: **Product → Strategy → Why → Outcome**.

2. **loan-strategy-presenter/SKILL.md** (updated 2026-07-14, commit `1f6e7ee`)
   Already updated to instruct Claude to build 1-4 scenario cards (not locked to 4) and to populate all four layers per card, pulling Why-layer sentences from a locked table rather than improvising them.

**The gap:** the SKILL.md now promises something the HTML template cannot render. The template is hardcoded to exactly 4 scenario slots in six different places, has no Why Layer anywhere, and assumes every scenario shares one global loan type and term. This brief closes that gap.

---

## 2. WHAT'S BROKEN TODAY (confirmed by direct inspection, 2026-07-14)

| Location in file | Problem |
|---|---|
| `.edit-drawer` → `.scenario-inputs` | Four hardcoded `.scenario-input-group` blocks (`ei-r0`/`ei-p0` through `ei-r3`/`ei-p3`). No way to show fewer, no way to show a 5th if ever needed. |
| `DATA.scenarios` | Array literal assumes exactly 4 entries with fixed labels in fixed order. |
| `buildScenarios(d)` | Uses `d.loanAmount` and 30-year term globally for every scenario. No per-scenario term or loan type. |
| `calcPI` / `buildCurve` | Hardcoded `years = 30` default, called without per-scenario term. |
| `CL` / `CD` color arrays | Indexed by array position (`CL[i]`), not by label. If only "Balanced" and "Wealth Accelerator" are built, they'd get colors 0 and 1 (navy/teal) instead of their locked colors (green/gold). |
| `.sc` card markup (inside `render()`) | Shows label + badge, then a flat list of rate/points/P&I/PITIA/net carry/cash-to-close/equity. No Strategy Layer badge distinct from label, no Why sentence, no explicit Product Layer grouping, no Outcome Layer grouping. |
| KPI row | `S[3].pit` is hardcoded — assumes a 4th scenario always exists ("Lowest PITIA" pulls from index 3). Will throw or show garbage with fewer cards. |
| Equity bars / comparison table | These two are already `S.map()`-driven and will mostly survive a variable count, but need verification once `S` can be length 1-4. |

---

## 3. NEW DATA SCHEMA

Replace the current `DATA.scenarios` shape with this. Every scenario is now self-contained on the Product Layer, not inherited from globals.

```js
const DATA = {
  borrowerName:  "[BORROWER_NAME]",
  subtitle:      "[FILE_SUBTITLE]",
  reportDate:    "[REPORT_DATE]",
  fileTypeLabel: "[FILE_TYPE_LABEL]",   // "Purchase" or "Investment Property"
  inv:           false,
  purchasePrice: 0,
  downPayment:   0,                      // default down payment, used unless a scenario overrides
  taxMonthly:    0,
  insMonthly:    0,
  hoaMonthly:    0,
  rentMonthly:   0,
  recScenario:   "[RECOMMENDATION_LABEL]",
  recText:       "[RECOMMENDATION_TEXT]",

  // 1 to 4 entries. Order when multiple are present: Current Loan, Conservative,
  // Balanced, Wealth Accelerator. Build ONLY the labels Claude was given rates for.
  scenarios: [
    {
      label:        "Balanced",              // must be one of the 4 locked labels — see §4
      loanType:     "30-Year Conventional Fixed",
      term:         30,                      // years — drives amortization math, no longer hardcoded
      rate:         6.25,
      pts:          0.5,
      downPayment:  null,                    // null = inherit DATA.downPayment; number = override
      featured:     true                     // exactly one scenario should be featured/recommended
    }
    // ...1-3 more entries as applicable
  ]
};
```

Rules:
- `scenarios.length` can be 1, 2, 3, or 4. Every part of the render pipeline must work at every length.
- `term` is now per-scenario. `calcPI`, `buildCurve`, and the interest/principal loop must all accept and use it instead of a hardcoded `30`.
- `downPayment` per scenario is optional — `null` inherits the file-level default. This supports cases like Wealth Accelerator buying down with points funded differently than the baseline.
- Exactly one scenario should carry `featured: true`. If none does, treat the first scenario in the array as featured (matches SKILL.md: "if only one card is built, that card is the recommendation").

---

## 4. THE LOCKED LABEL SET (do not deviate)

Pull these Why-layer sentences verbatim into the template as a constant. Do not let Claude Code, Claude, or Cowork improvise new wording here — this is locked doctrine, not copy to be polished.

```js
const STRATEGY_META = {
  "Current Loan": {
    why:   "Preserves maximum monthly cash flow.",
    color: { light: "#1e3a5f", dark: "#5591c7" }
  },
  "Conservative": {
    why:   "Lowest risk. Highest certainty. Fastest payoff.",
    color: { light: "#01696f", dark: "#4f98a3" }
  },
  "Balanced": {
    why:   "Balances monthly payment and long-term wealth creation.",
    color: { light: "#437a22", dark: "#6daa45" }
  },
  "Wealth Accelerator": {
    why:   "Maximizes equity and minimizes total interest paid.",
    color: { light: "#d19900", dark: "#e8af34" }
  }
};
```

Color assignment must key off `STRATEGY_META[s.label].color`, never off array index. This fixes the bug in §2 where a 2-card build would get the wrong colors.

---

## 5. SCENARIO CARD — NEW MARKUP (four layers, mandatory, every card)

Replace the current `.sc` card template inside `render()` with a four-section layout. Suggested structure (adapt class names to existing CSS conventions, but keep the four visually distinct sections — this is the actual point of the doctrine, borrowers scan top to bottom and get product → philosophy → reason → result):

```html
<div class="sc{{ featured ? ' ft' : '' }}" onclick="togglePick({{i}})">
  <div class="pick-indicator">...</div>

  <!-- LAYER 1: PRODUCT -->
  <div class="sc-product">
    <div class="sc-product-type">{{ loanType }}</div>
    <div class="sc-product-terms">
      {{ rate.toFixed(3) }}% · {{ term }}yr · {{ pts }} pts · {{ downPaymentPct }}% down
    </div>
  </div>

  <!-- LAYER 2: STRATEGY -->
  <div class="sc-strategy">
    <span class="sn">{{ label }}</span>
    {{#if featured}}<span class="sb">Most balanced path</span>{{/if}}
  </div>

  <!-- LAYER 3: WHY -->
  <div class="sc-why">{{ STRATEGY_META[label].why }}</div>

  <!-- LAYER 4: OUTCOME -->
  <div class="sm">
    <div class="mr"><span class="ml2">P&I</span><span class="mv">{{ f(pi) }}/mo</span></div>
    <div class="mr"><span class="ml2">Total PITIA</span><span class="mv lg p">{{ f(pit) }}/mo</span></div>
    {{#if inv}}<div class="mr"><span class="ml2">Net carry</span><span class="mv">{{ f(nc) }}/mo</span></div>{{/if}}
    <div class="mr"><span class="ml2">Total interest ({{term}}yr)</span><span class="mv">{{ f(totalInterest) }}</span></div>
    <div class="mr"><span class="ml2">Equity at 10 yrs</span><span class="mv">{{ f(eq) }}</span></div>
    <div class="mr"><span class="ml2">Payoff date</span><span class="mv">{{ payoffDate }}</span></div>
  </div>
</div>
```

New CSS needed (additive, don't touch existing `.sc`, `.sm`, `.mr` rules — those still apply to Layer 4):

```css
.sc-product{margin-bottom:10px;padding-bottom:10px;border-bottom:1px solid var(--div)}
.sc-product-type{font-size:.68rem;font-weight:600;color:var(--mut);text-transform:uppercase;letter-spacing:.04em}
.sc-product-terms{font-size:.72rem;color:var(--txt);margin-top:2px}
.sc-strategy{margin-bottom:6px}
.sc-why{font-size:.72rem;color:var(--mut);line-height:1.4;margin-bottom:12px;font-style:italic}
```

Test on one card at 225px min-width (existing `.sg` grid-template) before assuming it fits — four layers is more vertical content than the current card. If it's cramped, reduce `.sc` internal padding slightly rather than shrinking font below `.68rem` anywhere (readability floor).

---

## 6. MATH ENGINE CHANGES

```js
function calcPI(loan, rate, years) {          // years now always passed explicitly, no default
  if (!loan || !rate) return 0;
  const r = rate / 1200, n = years * 12;
  return loan * (r * Math.pow(1+r,n)) / (Math.pow(1+r,n)-1);
}

function buildCurve(loan, rate, years) {       // now term-aware
  if (!loan || !rate) return Array(11).fill(0);
  const r = rate / 1200, pmt = calcPI(loan, rate, years);
  let b = loan;
  const pts = [Math.round(b)];
  const horizonMonths = Math.min(120, years * 12);
  for (let m = 1; m <= horizonMonths; m++) {
    b -= (pmt - b * r);
    if (m % 12 === 0) pts.push(Math.round(b));
  }
  // pad remaining points at 0 balance if term < 10yr horizon
  while (pts.length < 11) pts.push(0);
  return pts;
}
```

`buildScenarios(d)` must compute per scenario:
- `loanAmount = d.purchasePrice - (s.downPayment ?? d.downPayment)`
- `pi = calcPI(loanAmount, s.rate, s.term)`
- Interest/principal loop runs over `Math.min(120, s.term*12)` months for the 10-year snapshot, but **total interest paid** (new Outcome field, see §7) sums over the *full term*, not just 10 years — that's a separate longer loop or closed-form total: `totalInterest = pi * term * 12 - loanAmount`.
- `payoffDate`: closing/report date + `term` years (simple date-math, not critical-path precision — this is a directional field for the card, not a legal amortization schedule).

---

## 7. NEW OUTCOME FIELDS

Per SKILL.md §"SCENARIO CARD — FOUR-LAYER STRUCTURE," the Outcome Layer needs fields the current engine doesn't compute yet:

| Field | Formula | Notes |
|---|---|---|
| `totalInterest` | `pi * term * 12 - loanAmount` | Full term, not 10-year snapshot |
| `payoffDate` | report/closing date + term years | Format as "Mon YYYY" |

`eq` (equity at 10yr) and `nc` (net carry) already exist in the current engine, keep as-is, just make sure they read `s.term`-aware loan amount instead of the old global.

---

## 8. EDIT DRAWER — MAKE IT DYNAMIC

Delete the four hardcoded `.scenario-input-group` blocks. Replace with a JS-generated section:

```js
function renderScenarioInputs() {
  const container = document.getElementById('scenarioInputsContainer');
  container.innerHTML = DATA.scenarios.map((s, i) => `
    <div class="scenario-input-group">
      <div class="scenario-input-label">${s.label}</div>
      <div class="edit-field" style="margin-bottom:6px">
        <label class="edit-label">Loan type</label>
        <input class="edit-input" id="ei-type${i}" value="${s.loanType}" oninput="liveUpdate()">
      </div>
      <div class="edit-field" style="margin-bottom:6px">
        <label class="edit-label">Term (yrs)</label>
        <input class="edit-input" id="ei-term${i}" type="number" value="${s.term}" oninput="liveUpdate()">
      </div>
      <div class="edit-field" style="margin-bottom:6px">
        <label class="edit-label">Rate (%)</label>
        <input class="edit-input" id="ei-r${i}" type="number" step="0.125" value="${s.rate}" oninput="liveUpdate()">
      </div>
      <div class="edit-field">
        <label class="edit-label">Points</label>
        <input class="edit-input" id="ei-p${i}" type="number" step="0.125" value="${s.pts}" oninput="liveUpdate()">
      </div>
    </div>`).join('');
}
```

Call `renderScenarioInputs()` once on load and again any time `DATA.scenarios.length` changes (it won't change mid-session in practice — Claude sets it once at generation time — but don't hardcode assumption of 4 anywhere in the drawer HTML itself).

`.scenario-inputs` grid CSS currently does `grid-template-columns:repeat(4,1fr)` — change to `repeat(auto-fit, minmax(150px, 1fr))` so it lays out cleanly at 1, 2, 3, or 4 columns.

---

## 9. KPI ROW FIX

Current bug: `{ l:'Lowest PITIA', v: f(S[3].pit) + '/mo', s: 'Wealth accelerator' }` hardcodes index 3.

Fix: compute dynamically —
```js
const lowestPitia = S.reduce((min, s) => s.pit < min.pit ? s : min, S[0]);
// then: { l:'Lowest PITIA', v: f(lowestPitia.pit) + '/mo', s: lowestPitia.label }
```

Same audit needed anywhere else in the file that indexes `S[n]` by position instead of by find/reduce. Search the whole file for `S[` and `d.scenarios[` before considering this done.

---

## 10. CHARTS

`ch1` (PITIA bar) and `ch2` (balance line) already iterate `S.map(...)` for datasets, so they should mostly survive a variable count. Two things to verify:
- Color arrays (`c = gc()`) must now pull per-scenario from `STRATEGY_META[s.label].color[theme]`, not by array position (same fix as §4).
- At `S.length === 1`, the balance-over-time line chart is still useful (shows the amortization curve), but the PITIA bar chart becomes a single bar. That's fine, don't hide it, but don't let Chart.js render it awkwardly wide — cap max bar thickness or it'll look broken with one category.

---

## 11. NON-NEGOTIABLES (do not touch, do not "improve")

- Logo URL, Calendly URL, contact footer, compliance disclaimer text — unchanged, byte-for-byte.
- Dark mode toggle behavior and CSS variable system — unchanged.
- Print/Save PDF button and `@media print` rules — unchanged, and must still hide the edit drawer/toggle/Calendly button on print.
- Colors `#1e3a5f` / `#01696f` / `#437a22` / `#d19900` (light) and their dark-mode equivalents stay tied to their existing labels (Current Loan/Conservative/Balanced/Wealth Accelerator respectively) — this brief keys color by label instead of index, but the actual hex values and which label owns which color do not change.
- File must still be a single self-contained HTML file (current architecture: inline `<style>`, inline `<script>`, one external Chart.js CDN link). Don't split into multiple files or add a build step.

---

## 12. TEST PLAN — RUN ALL FOUR BEFORE CALLING THIS DONE

Use these as literal test fixtures, swap into `DATA` and visually check:

**Test A — 1 card (edge case low end)**
```js
scenarios: [
  { label:"Balanced", loanType:"30-Year Conventional Fixed", term:30, rate:6.25, pts:0.5, downPayment:null, featured:true }
]
```
Check: card renders full 4-layer, no "featured" comparison noise, KPI row doesn't break, equity bar renders one bar, PITIA bar chart doesn't look absurd, comparison table has one data column, no console errors.

**Test B — 2 cards, mixed terms**
```js
scenarios: [
  { label:"Current Loan", loanType:"30-Year Conventional Fixed", term:30, rate:6.625, pts:0, downPayment:null, featured:false },
  { label:"Conservative", loanType:"15-Year Conventional Fixed", term:15, rate:5.75, pts:1, downPayment:null, featured:true }
]
```
Check: 15-year amortization curve looks correct (pays off before 10-year mark, `buildCurve` padding logic kicks in), colors are Current Loan navy + Conservative teal (not navy+teal by position, verify against label-keyed lookup), total interest reflects the shorter term correctly (should be dramatically lower than a 30yr).

**Test C — 4 cards, investment file**
Use the existing default 4-scenario shape with `inv: true` and a `rentMonthly` value. Check: net carry appears in Layer 4 on all 4 cards, KPI row shows rental income + net carry KPIs, nothing regresses from current production behavior.

**Test D — dark mode + print, all of the above**
Toggle dark mode on Test C. Confirm STRATEGY_META dark colors apply correctly per label. Open print preview on Test A and Test C — confirm edit drawer/toggle/Calendly hidden, cards still legible, four-layer structure survives print CSS.

Do not hand this back until all four tests pass with no console errors and no visual breakage. This is client-facing and gets screen-shared live, there's no "fix it after" — Scott doesn't want to find a bug mid-call with a borrower watching.

---

## 13. DEFINITION OF DONE

- [ ] `DATA.scenarios` accepts 1-4 entries, any subset of the 4 locked labels, any order
- [ ] Every card renders all four layers: Product, Strategy, Why, Outcome
- [ ] Why-layer text pulled from `STRATEGY_META`, never hardcoded per-card, never paraphrased
- [ ] Colors keyed by label via `STRATEGY_META`, not array index
- [ ] Per-scenario `term` and `loanType` supported end-to-end (math engine, card display, comparison table)
- [ ] New Outcome fields (`totalInterest`, `payoffDate`) computed and displayed
- [ ] KPI row has zero hardcoded array indices (search file for `S[` to confirm)
- [ ] Edit drawer generates scenario inputs dynamically, no hardcoded r0-r3/p0-p3 blocks
- [ ] `.scenario-inputs` grid CSS reflows cleanly at 1-4 columns
- [ ] Charts render correctly at all four test-fixture counts (A/B/C/D above)
- [ ] Dark mode and print both verified against the new card layout
- [ ] Logo, Calendly link, contact footer, compliance disclaimer unchanged
- [ ] File remains a single self-contained HTML file, no build step introduced
- [ ] PR opened against `main` on branch `feature/four-layer-cards`, not pushed directly — Scott reviews before merge

---

*Prepared by Claude (Digital Chief of Staff) on instruction from Scott Thompson, 2026-07-14.*
*Companion doc: loan-strategy-presenter/SKILL.md, commit 1f6e7eebdc65dafc4a380f0187bf39763212c92e*
*Governing doctrine: 🔍 APEX_DESIGN_DISCOVERY_StrategyNamesAreNotLoanProducts_2026-06-18 (Notion)*
