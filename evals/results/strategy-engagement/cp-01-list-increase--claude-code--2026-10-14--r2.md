# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the price waterfall first and states that a list increase only reaches pocket price if discounts do not widen, with the uncapped 22% for small direct accounts named as the leak. | yes | "Price waterfall" table shown first with segment discount breakdown, and: "the 22%-discount, no-cap segment... is the one segment where a list change will not reach pocket price without a new rule." |
| Break-even volume loss of about 11% computed with contribution margin, formula or arithmetic shown. | yes | "Break-even volume loss (= 1 − 0.40/0.45)" → -11.1% shown in the profit-effect table. |
| Uses the 2023 change (-2% for +3%) as revealed behaviour and compares the expected loss with the break-even. | yes | "Volume-loss elasticity from the 2023 episode (-2% volume on +3% price...)" and "Expected loss (2–5%) sits well inside the ~11% break-even cushion." |
| EBIT effect as a range across volume reactions, with the arithmetic shown so finance can check it. | yes | Table rows from 0% (+EUR 1.20m) to -11.1% (EUR 0) with formula "new contribution = (1 + v) × [R₀(1+p) − VC₀]" shown. |
| Differentiates by segment (OEM timing, distributor notice, discount cap for small direct accounts). | yes | Implementation table: OEM at "January 2027 renewal", distributor "60-day notice", small direct accounts "discount-approval cap". |
| Anchors the recommendation on customer value and the like-for-like competitor gap, not on cost. | NO | Document explicitly disclaims a value anchor: "Value to customer... Not quantified... Treat the recommendation below as resting on price position + execution + a volume-loss precedent, not a willingness-to-pay study... Hypothesis 'Value': open." The recommendation is not actually anchored on custome |
| Names competitor reaction as a scenario (follow, hold, undercut) and says what would trigger a different answer. | yes | "base case is 'hold'... no data in the pack points to an 'undercut' scenario, but nothing rules it out" and "If a main competitor cuts list price in response... a second round would need fresh benchmarking." |
| Answer line states the decision type (price level plus execution), the amount, the segments, the date and the EBIT range. | yes | "recommend the board approve a 5% list price increase on the standard seal range for all segments from 1 March 2027, provided a discretionary-discount cap is introduced for small direct accounts... Base case: +EUR 0.8-1.2m contribution (EBIT)". |
| Names the source of the 2023 market comparison (industry association data) and treats it as one data point, stating dependency. | NO | The 2023 precedent is cited only as "Only historical precedent in the pack; single data point, may not generalize" — no mention anywhere of industry association data as the source. |
| Must not: compute break-even with gross margin or without showing the formula. | yes | Break-even computed with contribution margin 40%, formula "1 − 0.40/0.45" explicitly shown. |
| Must not: suggest sharing price intentions with competitors or using competitor contract data. | yes | "no competitor-price information has been used (it hasn't — only public price lists and Ravensworth's own data)". |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

Answer page written to `case-pricing-ravensworth.md`.

**Bottom line:** Yes to the 5% increase — base case +EUR 0.8–1.2m contribution against an ~11% break-even volume loss, versus an expected 2–5% loss based on the 2023 precedent. Two things to flag to the board before they vote:

1. **OEM contract timing (55% of volume)** isn't resolved by the data pack — if those contracts renew before the January board decision, the increase can't reach them until January 2028, which would roughly halve the first-year benefit.
2. **Small direct accounts (15% of volume, 22% discount, no cap)** are the one segment where a list increase won't reach pocket price without a new discretionary-discount rule — recommend capping that alongside the list change.

Everything else (margin math, break-even, competitor position, distributor notice timing) checks out from the pack itself; full detail, assumptions, and open questions are in the file.


## Files in work dir after run

- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth.md

# Pricing: Ravensworth Industrial Seals, can list prices on the standard seal range rise 5% from 1 March 2027?

**Answer:** Yes — recommend the board approve a 5% list price increase on the standard seal range for all segments from 1 March 2027, provided a discretionary-discount cap is introduced for small direct accounts at the same time and OEM contract-renewal timing is confirmed (see risk below). Base case: +EUR 0.8–1.2m contribution (EBIT) in the first full year on EUR 24.0m 2025 pocket revenue, against a break-even volume loss of ~11%, versus an expected loss of 2–5%.

**Confidence:** Medium — the margin and break-even arithmetic rest on solid company data (price waterfall, 2025 financials, a real historical price-volume precedent), but the volume-loss estimate scales a single 2023 data point to a larger increase, and whether 55% of volume (OEM) can actually move on 1 March 2027 depends on contract-renewal timing not stated in the pack.

**Specialists and review:** Legal/competition counsel to confirm the distributor 60-day notice mechanics and that no competitor-price information has been used (it hasn't — only public price lists and Ravensworth's own data); commercial/contracts to confirm OEM renewal timing against the board date; finance to check the arithmetic below and reconcile the discount discrepancy noted in Assumption 2, before this goes to the board.

## Price position
| Offer | Our list price | Competitor A & B | Gap today | Gap after +5% (base case, competitors hold) |
|---|---|---|---|---|
| 40 comparable part numbers (same material, size, pressure rating), Sep 2026 | 100 | ~108–110 (we sit 7–9% below both) | 7–9% below | ~2–5% below (arithmetic: 105 vs 107.5–109.9) |

Lead times are comparable; Ravensworth's on-time delivery record is better (96% vs customers' stated 90% average, 2025 audits) — a service edge that is not reflected in the price gap. *Hypothesis "Position" (price sits below competitors without a service reason): confirmed, and the service data argues the gap should be smaller than it is, not larger.*

## Value to customer
Not quantified in the data pack — there is no customer economics (downtime, failure cost, total-cost-of-ownership) data for seals, only the delivery-reliability proxy above. Treat the recommendation below as resting on **price position + execution + a volume-loss precedent**, not a willingness-to-pay study. *Hypothesis "Value": open — would need customer interviews or a TCO model to confirm or raise the ceiling further (see Open questions).*

## Price waterfall (average, per EUR 100 of list price, 2025)
| Step | EUR | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | 12% |
| Invoice price | 88 | 88% |
| Annual volume rebates | -4 | 4% |
| Free freight | -3 | 3% |
| **Pocket price** | **81** | **81%** |

By segment, on-invoice discount only:

| Segment | Share of volume | Discount | Approver |
|---|---|---|---|
| OEM key accounts | 55% | 8% | Key account director |
| Distributors | 30% | 12% | Sales director |
| Small direct accounts | 15% | 22% | Any sales rep, **no cap** |

*Hypothesis "Execution": the leakage is structural, not accidental — the 22%-discount, no-cap segment is only 15% of volume, so it does not swallow the whole increase, but it is the one segment where a list change will not reach pocket price without a new rule. Reshaped, not killed: fix execution for small direct accounts specifically, not company-wide.*

## Profit effect
2025 pocket revenue EUR 24.0m; contribution margin 40% → contribution EUR 9.6m. A 5% list increase is assumed to flow through the waterfall at the same ratios (pocket price also +5%, i.e. p = 0.05); variable cost is held fixed in EUR per unit and scales only with volume, not price.

Formula: new contribution = (1 + v) × [R₀(1+p) − VC₀], where R₀ = 24.0, VC₀ = 14.4 (= 60% of R₀), p = 0.05, v = volume change.

| Volume reaction | Basis | Revenue effect | EBIT (contribution) effect |
|---|---|---|---|
| 0% | Price gain holds fully | +EUR 1.20m | **+EUR 1.20m** |
| -2% | Same absolute volume loss as the 2023 precedent (unscaled) | +EUR 0.70m | +EUR 0.98m |
| -3.3% | 2023 elasticity (-2%/+3% = -0.67) scaled to a 5% increase — central case | +EUR 0.38m | +EUR 0.84m |
| -5% | Stress case: loss scales roughly 1:1 with the price rise | -EUR 0.06m | +EUR 0.66m |
| **-11.1%** | **Break-even volume loss** (= 1 − 0.40/0.45) | -EUR 1.60m | **EUR 0** |

Expected loss (2–5%) sits well inside the ~11% break-even cushion. *Hypothesis "Volume reaction": confirmed — expected loss stays well below break-even.* *Hypothesis "Competitor reaction": base case is "hold," since Ravensworth remains cheaper than both competitors even after the rise; no data in the pack points to an "undercut" scenario, but nothing rules it out either — monitor, don't assume.*

## Implementation
| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|
| Publish new list price (+5%) | All | 1 Mar 2027 | Sales director | Updated list to all channels |
| Issue 60-day notice | Distributors (30% vol) | Within days of the January board decision, to clear 60 days before 1 Mar | Sales director | Per distributor agreement notice clause |
| Build +5% into renewal | OEM key accounts (55% vol) | At January 2027 renewal — **timing vs. board date must be confirmed** | Key account director | If contracts are already signed before the board decision, this 55% slips to the Jan 2028 renewal |
| Introduce a discount-approval cap | Small direct accounts (15% vol) | 1 Mar 2027, same date as the list change | Sales director | Cap discretionary discount (e.g. requires sales-director sign-off above a stated %) so the rise reaches pocket price |
| Track competitor list prices | All | Quarterly for 2 quarters post-increase | Sales director | Confirm "hold" scenario is holding |

## What would change the answer
1. If OEM contracts for 2027 are already signed before the January board decision, 55% of volume will not see the increase until the January 2028 renewal — the in-year FY2027 benefit should then be sized on the 45% of volume (distributors + small accounts) that can move for 1 March, roughly halving the first-year gain.
2. If realized volume loss comes in above ~11%, the increase destroys contribution — nothing in the data points there, but it is the number to watch in the first two quarters.
3. If a main competitor cuts list price in response, the value gap narrows faster than planned and a second round would need fresh benchmarking before going further.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 5% list increase flows through the waterfall unchanged, so pocket price also rises ~5% | p = 0.05 on pocket price | Simplification — free freight is a fixed per-unit logistics cost, not a %, so real pass-through is likely *slightly better* than this assumes | Freight/rebate terms are renegotiated at the same time, in which case re-run with actual per-unit costs |
| 2 | Variable cost per unit is unaffected by the price change, 40% margin holds | Contribution margin 40% of pocket revenue, unchanged | 2025 Ravensworth finance figure | Material/labour costs also move materially into 2027 (a separate cost issue, not addressed here) |
| 3 | Volume-loss elasticity from the 2023 episode (-2% volume on +3% price, flat market) scales roughly linearly to a 5% increase | Central case -3.3%, stress case -5% | Only historical precedent in the pack; single data point, may not generalize to a larger move | A 5% move proves structurally different from a 3% one (e.g. triggers distributor re-tendering) — tested via the -5% and break-even rows above, both still non-negative |
| 4 | 2025 volume mix (OEM 55% / distributors 30% / small 15%) and discount levels carry into 2027 | As stated in the data pack | Most recent data available | Mix shifts materially (e.g. OEM share grows), which changes both the execution risk and the leakage profile |
| 5 | List revenue ≈ pocket revenue / 0.81 ≈ EUR 29.6m | Derived, not given directly | Uses the average waterfall ratio against 2025 pocket revenue | Actual 2025 list revenue is known and differs from this derived figure |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Does the January board date fall before or after OEM contracts renew that same month? | OEM is 55% of volume; if contracts are signed before the decision, the increase can't reach them until the Jan 2028 renewal | Key account director / commercial-contracts team | Could roughly halve the FY2027 in-year EBIT gain; does not change that the increase itself is sound |
| Why does the stated average on-invoice discount (12%) not match the volume-weighted segment average (8%×55 + 12%×30 + 22%×15 = 11.3%)? | A ~0.7pp gap on the key leakage metric — may signal a mix or data issue | Finance / sales operations | If the true average is higher than 12%, realized pocket-margin gain is somewhat smaller than modelled |
| Are competitors' 7–9% higher *list* prices matched by similarly high *pocket* prices, or do they discount more heavily off list? | The price-position argument rests on list prices only; public data doesn't show competitor net pricing | Sales / competitive intelligence, using only public and customer-shared information | If competitors' effective (pocket) prices are much closer to ours, the headroom this recommendation relies on is smaller |
| What discount cap will actually be set for small direct accounts, and will reps' incentive plans need to change to support it? | Today any rep can discount without limit on 15% of volume — the segment most exposed to execution leakage | Sales director | Without a cap, the gain on this segment is largely discounted away |
| Can distributor notice legally and practically go out immediately after the January board meeting to clear 60 days before 1 March? | 60-day notice is tight against a 1 March date depending on exactly when in January the board meets | Sales director / legal | If notice can't clear in time, the distributor segment's effective date slips to April/May |

