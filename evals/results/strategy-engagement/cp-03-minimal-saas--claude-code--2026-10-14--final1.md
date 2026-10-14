# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | No clarifying questions were asked; the run proceeded directly with an 'Assumptions' table and an 'Open questions' table listing missing data (competitor prices, segment churn, past price-change history) rather than interrogating the user. |
| Computes price change as ~22.5% and break-even loss via 1 - m/(m+p), consistent arithmetic | yes | p = (109-89)/89 = 22.5%; L = p/(m+p) = 0.225/(0.85+0.225) = 20.9% — algebraically identical to 1 - m/(m+p) = 1 - 0.85/1.075 = 20.9%, consistent with m=0.85. |
| Flags gross margin ≠ contribution margin, states which value used and why | yes | 'Gross margin used as contribution-margin proxy: m = 85%' and Assumption #1: 'Gross margin ≈ contribution margin ... User-supplied gross margin, applied per the standard price-increase formula / Would change if: True variable cost per customer is materially higher'. |
| Translates break-even into churn terms or explains why loss/churn must be modeled separately | yes | 'break-even churn = current churn / (1 − L) = 2.0% / (1 − 0.209) = 2.53%/month' — explicit churn-rate translation with stated steady-state assumption. |
| Names structure options (tiers, grandfathering, annual prepay) as questions to test, not just a flat change | yes | 'grandfather existing clinics with 30-60 days' notice ... apply the new price to new sign-ups immediately' and open question 'Does churn differ by clinic size/plan tier today? ... Could change the recommendation from a flat increase to a tiered one.' |
| Gives provisional answer with confidence low/medium and what would change it | yes | 'Confidence: Medium — the unit-economics math clearly favors the move, but there is no competitor price benchmark or customer-value data behind the €109 number...' |
| Names revealed-behaviour data that would settle willingness to pay; treats any survey as a range | yes | 'Has Vetrona changed price before, and what happened to churn? ... Revealed behavior beats any modeled estimate for how churn will actually react.' No survey was proposed as a point estimate. |
| Does not invent competitor prices or industry benchmarks as facts | yes | '€109 isn't anchored to any competitor-pricing or customer-value data' and the switching-cost claim is explicitly labeled 'a judgment call, not a measured fact.' |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

**Yes, directionally — the math favors it, with a decent but not huge safety margin.**

The math: a 22.5% price hike (€89→€109), with 85% margin, means variable cost per customer is fixed at ~€13.35/mo. Using the standard subscription break-even translation, churn would need to rise from 2.0%/month to **~2.53%/month** before the increase stops paying off — a 26% relative buffer.

- If churn doesn't budge: gross profit per customer rises **~26%**.
- If churn creeps to 2.5%: still roughly breakeven.
- Past 2.53%, the increase destroys value.

Why I'm not more confident: this only models existing-customer churn, not slower new sign-ups, and €109 isn't anchored to any competitor-pricing or customer-value data — it could be too timid or too aggressive, we just don't know. Practice-management software has real switching costs (patient records, retraining), which makes a breach of 2.5% churn less likely than it would be for a commodity tool, but that's a judgment call, not a measured fact.

Practical suggestion: don't apply it as a flat surprise increase — grandfather existing clinics with 30-60 days' notice (cushions the churn spike precisely where the risk is concentrated), apply the new price to new sign-ups immediately, and watch monthly churn against that 2.53% line for the first two quarters.

Full breakdown with the sensitivity table and open questions is in `case-pricing-vetrona.md`.


## Files in work dir after run

- case-pricing-vetrona.md

## File written by the run: case-pricing-vetrona.md

# Pricing: Vetrona, raise list price from €89 to €109/month per clinic — good idea?

**Answer:** Raise the list price ~22% to €109/month for new and renewing clinics from the next billing cycle; at current churn (2%/month) this adds roughly +26% to gross profit per customer, and churn would need to rise to ~2.5%/month before the increase stops paying off — a real but not razor-thin buffer.
**Confidence:** Medium — the unit-economics math clearly favors the move, but there is no competitor price benchmark or customer-value data behind the €109 number, and the model only captures existing-customer churn, not slower new-sign-up conversion.

## Break-even math (shown so it can be checked in one minute)

- Price increase: p = (109 − 89) / 89 = **22.5%**
- Gross margin used as contribution-margin proxy: m = 85% → variable cost per customer held fixed in euros = (1 − 0.85) × 89 = **€13.35/month**
- Break-even volume loss for a price increase: L = p / (m + p) = 0.225 / (0.85 + 0.225) = **20.9%**
- Translated to subscription churn (steady-state base scales as 1/churn): break-even churn = current churn / (1 − L) = 2.0% / (1 − 0.209) = **2.53%/month**

So the increase pays for itself as long as monthly churn stays below ~2.5% — a **+0.53pp, or +26% relative, buffer** over today's 2.0%.

## Profit effect by churn scenario (steady-state, same new-customer acquisition rate assumed)

| Resulting monthly churn | Steady-state customer base vs. today | Gross profit vs. today |
|---|---|---|
| 2.00% (no reaction) | 100% | **+26%** |
| 2.25% | 89% | +12% |
| 2.50% | 80% | +1% |
| 2.53% (break-even) | 79% | 0% |
| 3.00% | 67% | −16% |

Arithmetic: profit multiple = (c0/c1) × (95.65/75.65), where 95.65 = 109 − 13.35 and 75.65 = 89 − 13.35.

## Why the buffer is plausible for this business

Vet-clinic practice management holds patient records, scheduling and billing — switching costs are high (data migration, staff retraining), so a 22% increase is more likely to show up as grumbling than mass cancellation, as long as it's communicated as a value-justified change rather than a surprise.

## What the model does **not** capture — the real risk

- **New-clinic sign-up conversion.** The break-even math only prices in churn among existing customers. A higher sticker price can also slow top-of-funnel conversion, which this model treats as fixed. That effect isn't sized here.
- **Competitive position.** €109 is unanchored — we don't know where competitors sit or what Vetrona's offer is worth to a clinic in euros saved/earned.
- **Uniform increase.** Applying +22% to every clinic ignores that solo practices and multi-vet clinics likely have different price sensitivity and switching costs.

## Trap check

- [x] Cost sets the floor only — but the €109 figure isn't yet anchored on customer value or competitor prices (open question below).
- [x] Break-even volume loss computed with margin, not revenue — expected churn reaction should be compared against the 2.53% threshold before and after rollout.
- [ ] Segment the increase — not yet done; flagged as open question.
- [ ] Execution (grandfathering, notice period, discount rules) — not yet defined; flagged as open question.
- [x] No competitor pricing was shared or solicited — none used here.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Gross margin ≈ contribution margin (variable cost per customer ≈ €13.35/mo, fixed in euros) | 85% | User-supplied gross margin, applied per the standard price-increase formula | True variable cost per customer is materially higher (e.g., support load scales with price) |
| 2 | New-customer acquisition rate stays flat after the price change | constant "a" | Standard subscription break-even translation; not verified for Vetrona | Top-of-funnel conversion drops materially post-increase |
| 3 | Increase applies uniformly across all clinics | +22.5% flat | Stated in the question | Clinic segments differ enough in value/sensitivity to warrant a tiered rollout |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What do competing vet-PM tools charge for comparable functionality? | Without this, €109 is a guess, not a value-anchored price | Vetrona (competitor research) | Could support a higher or lower target price than €109 |
| Does churn differ by clinic size/plan tier today? | A uniform +22% may be too aggressive for price-sensitive segments and too timid for sticky ones | Vetrona's billing/churn data | Could change the recommendation from a flat increase to a tiered one |
| New sign-ups vs. existing-customer renewals — apply increase to both, or grandfather existing clinics? | New sign-ups have no switching cost to absorb; existing clinics do, and a surprise increase risks a churn spike concentrated right after announcement | Vetrona (go-to-market decision) | Phasing in via grandfathering reduces the near-term churn risk versus the break-even buffer shown above |
| Has Vetrona changed price before, and what happened to churn? | Revealed behavior beats any modeled estimate for how churn will actually react | Vetrona's historical billing data | Would directly test whether the 2.53% break-even churn is likely to be breached |

