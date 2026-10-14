# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | No questions were asked at all (0 rounds, satisfying 'at most one'); the run proceeded directly with an explicit 'Assumptions' table and 'Open questions' table flagging what was unverified. |
| Computes price change as ~22.5% and break-even customer loss via 1 - m/(m+p), arithmetic consistent with margin used | yes | "Price change: €89 → €109 = +€20, +22.5%" and "One-time break-even volume loss: 1 − (75.65/95.65) = ~21% of customers" — mathematically equivalent to 1−0.85/(0.85+0.225)=20.9%, matching reference within rounding. |
| Flags that gross margin is not contribution margin and states which value it uses and why | NO | The run only says "Gross margin 85% → variable cost ≈ €13.35/clinic/month" and treats it directly as the margin for contribution math; nowhere does it state that gross margin and contribution margin are conceptually different metrics or justify using gross margin as a stand-in. |
| Translates break-even into churn terms over 12 months vs. 2% baseline | yes | "break-even churn = 2% × (95.65/75.65) = ~2.53%/month (vs. 2% today)" with a table mapping churn levels to steady-state contribution impact. |
| Names structure options as a question to test (tiers, grandfathering, annual prepay) rather than only a single level change | yes | "Does churn differ by clinic size/segment today? ... Could shift to a tiered increase (smaller % for solo clinics)" and recommendation to "grandfather existing customers with 60–90 days' notice." |
| Gives a provisional answer with confidence low or medium and what would change it | yes | "Confidence: Medium. ... there's no competitor-price or willingness-to-pay data behind it — that's the real risk, not the math." |
| Names revealed-behaviour data that would settle willingness to pay, treats any survey as a range | yes | "What happened to churn after any past price change? ... Direct revealed-behaviour evidence beats the arithmetic buffer / Vetrona's historical billing data"; no survey was invoked so no violation there. |
| Must not invent competitor prices or industry benchmarks (churn, price-increase size, conversion) as facts | NO | "2%/month churn (~22% annualized) is high for workflow-embedded practice software" is stated flatly as fact with no data or hedge, inventing an implicit industry churn benchmark. |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

**Short answer: yes, worth doing — the math gives you a lot of room.**

The +€20 (22.5%) increase only needs variable cost held fixed in euros (≈€13.35/clinic from your 85% margin) to raise contribution per clinic from €75.65 to €95.65. Translating that into steady-state churn terms: your break-even churn is **~2.53%/month**, vs. 2% today. So churn can rise by a relative ~26% and you still come out ahead — at unchanged churn you're up ~26% on steady-state contribution; even at 3%/month churn you're only down ~16%.

Caveats that actually matter more than the arithmetic:
- No data here on competitor pricing or willingness-to-pay — that's the real risk, not the break-even math.
- A uniform increase across all clinics is probably wrong; solo-vet practices and multi-vet clinics likely differ in sensitivity.
- 2%/month churn (~22% annualized) is high for workflow-embedded practice software — worth investigating separately regardless of this pricing call.

**Recommendation:** raise to €109, grandfather existing customers with 60–90 days' notice, test on new sign-ups first, and watch churn against the ~2.5%/month trigger for a couple of months rather than rolling it out cold to the whole base.

Full workup with the issue tree, trap checks, and open-questions table saved to `case-pricing-vetrona.md`.


## Files in work dir after run

- case-pricing-vetrona.md

## File written by the run: case-pricing-vetrona.md

# Pricing: Vetrona, raise list price from €89 to €109/month per clinic — good idea?

## Step 1: Sharpen the question
Decision type: price **level** (list price), structure and execution unchanged. Scope: all clinics, single plan (no tiers mentioned). Sharpened question: "By how much can Vetrona raise list price in 2026 without pushing monthly churn past the break-even level, and what is the margin effect?" Missing to fully sharpen: last price change and its volume effect, any existing tiering by clinic size, competitor pricing — listed under Open questions.

## Step 2: Issue tree
| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Value | Switching cost + workflow lock-in (patient records, staff training) make demand inelastic at this price | Clinics report easy, cheap switching to alternatives | Untested — no data |
| Position | €109 remains competitive vs. other vet practice-management tools | A comparable competitor is priced materially below €109 | Untested — no data |
| Volume reaction | Expected churn increase stays below break-even churn | Expected/observed churn rises above break-even churn | **Core analysis — see Step 3e** |
| Execution | Raising list price reaches pocket price (no informal discounting creep) | Sales/success team discounts around the new price | Untested — no data, but low risk (self-serve-like SMB motion typical for this ACV) |
| Structure | Uniform increase is appropriate here | Clinic segments (solo vet vs. multi-vet) differ sharply in sensitivity | Likely false — flagged as open question |

## Step 3: Deciding analyses

**3e. Break-even volume / churn (the decisive one — run with the numbers given)**

- Price change: €89 → €109 = +€20, **+22.5%** on list price.
- Gross margin 85% → variable cost ≈ €13.35/clinic/month. Per the rule "keep variable cost per customer fixed in euros, never apply the margin % to the new price":
  - Old contribution/clinic: €89 − €13.35 = **€75.65**
  - New contribution/clinic: €109 − €13.35 = **€95.65** (new margin ≈ 87.8%)
- One-time break-even volume loss: 1 − (75.65/95.65) = **~21% of customers** could be lost on the increase alone before it stops paying for itself.
- Translated to subscription churn (steady-state base ∝ 1/churn): break-even churn = 2% × (95.65/75.65) = **~2.53%/month** (vs. 2% today). That means monthly churn can rise by **~0.5 points (a ~26% relative jump)** before the increase becomes value-destructive in steady state.

| New steady-state churn | Steady-state contribution vs. today |
|---|---|
| 2.0% (unchanged) | +26% |
| 2.25% | +12% |
| **2.53% (break-even)** | **0%** |
| 2.75% | −8% |
| 3.0% | −16% |
| 4.0% | −37% |

Hypothesis "volume reaction stays below break-even" — **provisionally confirmed**, strength weak (no clinic-level price-sensitivity data, just the arithmetic buffer): a 22.5% list increase only needs churn to stay under ~2.5%/month, which is a generous cushion for software with real switching costs (patient records, staff retraining).

**3b/3c/3d (benchmark, value-to-customer, willingness-to-pay):** not run — no competitor price or customer-interview data supplied. Flagged as open questions below; this is the main source of residual risk, not the break-even math.

## Step 4: Trap checks
- [x] Cost sets the floor only — price is being checked against churn/value tolerance, not cost-plus.
- [ ] Willingness to pay cross-checked with revealed behaviour — **not done**, no data.
- [ ] Segmented by clinic value/sensitivity — **not done**, uniform increase assumed; flagged as likely wrong.
- [x] Execution: low risk for this ACV/motion, but not verified.
- [x] Break-even computed on contribution margin, compared to plausible churn reaction.
- [x] No competitor price coordination involved.

---

**Answer:** Raise list price from €89 to €109/month (+22.5%) for all clinics from the next billing cycle; grandfather existing clinics with 60–90 days' notice to blunt a churn spike. Expected margin effect: **+12% to +26% uplift in steady-state contribution**, turning negative only if monthly churn rises above ~2.53% (vs. 2% today) and stays there.

**Confidence:** Medium. The arithmetic buffer is comfortable (churn would need to rise by a relative ~26% before this backfires), but there's no competitor-price or willingness-to-pay data behind it — that's the real risk, not the math.

**Separately worth flagging:** 2%/month churn (~21–24% annualized) is high for sticky, workflow-embedded practice-management software. That's a retention problem worth investigating on its own, independent of this pricing decision — and if the cause is price sensitivity among a specific segment (e.g., solo-vet clinics), a uniform increase could make it worse there even while the aggregate math works.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Variable cost/clinic is fixed in euros, not a % of price | €13.35/clinic/mo (15% of €89) | Derived from stated 85% gross margin | Variable cost actually scales with price (e.g., usage-based infra costs) |
| 2 | No material discounting today | Full list price assumed as pocket price | Not stated by user | Significant existing discounting would mean the list change doesn't reach pocket price |
| 3 | Acquisition rate stays constant post-increase | Used to translate churn → steady-state base via 1/churn | Standard SaaS steady-state approximation | New-customer conversion also drops at higher price (would need its own analysis) |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What do competing vet-practice platforms charge? | Tests whether €109 still sits below/at/above market | Competitor websites, sales team | Could change confidence from medium to high, or flag a ceiling |
| Does churn differ by clinic size/segment today? | Tests whether a uniform increase is the right structure | Vetrona's own billing/CRM data | Could shift to a tiered increase (smaller % for solo clinics) |
| What happened to churn after any past price change? | Direct revealed-behaviour evidence beats the arithmetic buffer | Vetrona's historical billing data | Would replace the "weak evidence" assumption with real evidence |
| Is any current discounting happening (annual deals, sales concessions)? | Confirms list increase reaches pocket price | Finance/sales | If material, the increase needs an execution fix alongside the level change |

**Recommendation:** Go ahead, but test on new sign-ups first (or a cohort) rather than an all-at-once increase on the full existing base, and watch monthly churn against the ~2.5% trigger for 2–3 months before declaring it a win.

