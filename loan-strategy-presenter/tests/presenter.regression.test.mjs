// Regression checks for MMM_Loan_Strategy_Presenter.html (v7.1.0 contract).
//
// Run from the repo root:
//   node --test loan-strategy-presenter/tests/presenter.regression.test.mjs
//
// Part 1 (always runs, no dependencies): loads the template's script in a Node
// vm sandbox and tests fromTCA() and pickFeatured() directly.
// Part 2 (runs when Playwright is installed): renders the template in headless
// Chromium with a TCA_BLOCK injected and checks the DOM. Chart.js is stubbed so
// the test needs no network.

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import vm from 'node:vm';

const HERE = dirname(fileURLToPath(import.meta.url));
const HTML = readFileSync(join(HERE, '..', 'MMM_Loan_Strategy_Presenter.html'), 'utf8');

// ---------- Part 1: pure-function checks in a vm sandbox ----------

function loadEngine() {
  const scripts = [...HTML.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  assert.equal(scripts.length, 1, 'expected exactly one inline <script> in the template');
  let code = scripts[0];
  const init = /\/\/ Initial render\s*\nrender\(\);\s*\nsetVerificationNotice\(\);\s*$/;
  assert.match(code, init, 'initial render block not found; update this test if it moved');
  code = code.replace(init, '');
  code += '\n;globalThis.__engine = { fromTCA, pickFeatured, validateData, buildScenarios, DATA };';
  const el = () => ({ addEventListener() {}, setAttribute() {}, style: {} });
  const sandbox = {
    document: { getElementById: el, documentElement: el(), querySelector: el },
    matchMedia: () => ({ matches: false }),
    console,
  };
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);
  return sandbox.__engine;
}

const E = loadEngine();

const BASE_BLOCK = {
  mode: 'purchase',
  analysisDate: '2026-10-20',
  loanType: 'Conventional',
  purchasePrice: 850000,
  loanAmount: 680000,
  monthlyTax: 885,
  monthlyInsurance: 125,
};

test('single Today\'s Rate scenario, no featured, no Best Monthly Value: nothing is featured', () => {
  const block = { ...BASE_BLOCK, scenarios: [{ label: "Today's Rate", term: 30, rate: 0.06625 }] };
  const out = E.fromTCA(block, E.DATA);
  assert.equal(out.errs.length, 0, String(out.errs));
  assert.equal(out.data.scenarios.length, 1);
  assert.equal(out.data.scenarios[0].featured, false);
  const S = E.buildScenarios(out.data);
  assert.equal(E.pickFeatured(S), null, 'a lone card must not be featured by fallback');
});

test('pickFeatured keeps the documented order: flagged, else Best Monthly Value, else none', () => {
  const flagged = [{ label: "Today's Rate", featured: false }, { label: 'Fastest Payoff', featured: true },
    { label: 'Best Monthly Value', featured: false }];
  assert.equal(E.pickFeatured(flagged).label, 'Fastest Payoff');
  const bmv = [{ label: "Today's Rate", featured: false }, { label: 'Best Monthly Value', featured: false }];
  assert.equal(E.pickFeatured(bmv).label, 'Best Monthly Value');
  assert.equal(E.pickFeatured([{ label: "Today's Rate", featured: false },
    { label: 'Maximum Savings', featured: false }]), null);
  // A lone card is featured only when explicitly flagged.
  assert.equal(E.pickFeatured([{ label: "Today's Rate", featured: true }]).label, "Today's Rate");
  assert.equal(E.pickFeatured([{ label: 'Best Monthly Value', featured: false }]).label, 'Best Monthly Value');
});

test('fromTCA converts decimal rates to percent with s.rate * 100, no rounding of the stored value', () => {
  const rates = [0.06625, 0.06125, 0.0599999, 0.0612345678, 0.07];
  const labels = ["Today's Rate", 'Fastest Payoff', 'Best Monthly Value', 'Maximum Savings'];
  for (const r of rates) {
    const block = { ...BASE_BLOCK, scenarios: labels.map(label => ({ label, term: 30, rate: r })) };
    const out = E.fromTCA(block, E.DATA);
    assert.equal(out.errs.length, 0, String(out.errs));
    for (const s of out.data.scenarios) {
      assert.equal(s.rate, r * 100, `rate ${r} must store exactly ${r * 100}, got ${s.rate}`);
    }
  }
  // A value the old 5-decimal rounding would have changed.
  const fine = { ...BASE_BLOCK, scenarios: [{ label: "Today's Rate", term: 30, rate: 0.0612345678 }] };
  const stored = E.fromTCA(fine, E.DATA).data.scenarios[0].rate;
  assert.notEqual(stored, Math.round(0.0612345678 * 100 * 100000) / 100000);
  assert.equal(stored.toFixed(3), '6.123', 'display rounding still happens separately');
});

// ---------- Part 2: DOM checks in headless Chromium (optional) ----------

let chromium = null;
try { ({ chromium } = await import('playwright')); } catch { /* not installed */ }

const CHART_STUB = 'window.Chart = class { constructor() {} destroy() {} };';

async function renderWithBlock(block) {
  const html = HTML.replace('const TCA_BLOCK = null;', `const TCA_BLOCK = ${JSON.stringify(block)};`);
  assert.notEqual(html, HTML, 'TCA_BLOCK placeholder not found in template');
  const launchOpts = process.env.PW_CHROMIUM_PATH ? { executablePath: process.env.PW_CHROMIUM_PATH } : {};
  const browser = await chromium.launch(launchOpts);
  try {
    const page = await browser.newPage();
    const pageErrors = [];
    page.on('pageerror', e => pageErrors.push(String(e)));
    await page.route('**/*', route => {
      const url = route.request().url();
      if (url.includes('chart.js')) return route.fulfill({ contentType: 'text/javascript', body: CHART_STUB });
      if (url.startsWith('http')) return route.fulfill({ status: 204, body: '' });
      return route.continue();
    });
    await page.setContent(html, { waitUntil: 'load' });
    const result = await page.evaluate(() => ({
      cards: document.querySelectorAll('#sg .sc').length,
      featuredCards: document.querySelectorAll('#sg .sc.ft').length,
      badges: [...document.querySelectorAll('#sg .sb')].map(b => b.textContent),
      recDisplay: getComputedStyle(document.querySelector('.rec')).display,
      productTerms: [...document.querySelectorAll('.sc-product-terms')].map(e => e.textContent),
      storedRates: DATA.scenarios.map(s => s.rate),
      errorPage: /presentation not rendered/i.test(document.querySelector('.wrap').innerText),
    }));
    return { ...result, pageErrors };
  } finally {
    await browser.close();
  }
}

test('DOM: lone Today\'s Rate card renders with no badge and no recommendation panel',
  { skip: !chromium && 'playwright not installed' }, async () => {
    const r = await renderWithBlock({ ...BASE_BLOCK, scenarios: [{ label: "Today's Rate", term: 30, rate: 0.06625 }] });
    assert.deepEqual(r.pageErrors, []);
    assert.equal(r.errorPage, false);
    assert.equal(r.cards, 1);
    assert.equal(r.featuredCards, 0);
    assert.deepEqual(r.badges, []);
    assert.equal(r.recDisplay, 'none');
  });

test('DOM: stored rate keeps full precision, display rounds to 3 places',
  { skip: !chromium && 'playwright not installed' }, async () => {
    const r = await renderWithBlock({ ...BASE_BLOCK, featured: "Today's Rate",
      scenarios: [{ label: "Today's Rate", term: 30, rate: 0.0612345678 }] });
    assert.deepEqual(r.pageErrors, []);
    assert.deepEqual(r.storedRates, [0.0612345678 * 100]);
    assert.match(r.productTerms[0], /^6\.123% /);
    assert.equal(r.featuredCards, 1, 'explicit featured on a lone card still features it');
    assert.deepEqual(r.badges, ['Your scenario']);
    assert.notEqual(r.recDisplay, 'none');
  });
