# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: runs the price waterfall first and states that a list increase only reaches pocket price if discounts do not widen, with the uncapped 22% for small direct accounts named as the leak. | yes | 3a waterfall run first in deciding analyses; 'A list increase with no execution fix risks being discounted away in that segment... small-direct, uncapped'; 'small-direct segment (15% of volume) carries the highest discount (22%) with no approval cap' |
| Must: break-even volume loss of about 11% computed with contribution margin, formula or arithmetic shown. | yes | 'Formula: break-even loss ... = 1 − m/(m+p). With p=5% and contribution margin m=40%: 1 − 0.40/0.45 = ... 11.1%' |
| Must: uses the 2023 change (-2% for +3%) as revealed behaviour and compares the expected loss (about 3% to 4%, or a stated range) with the break-even. | yes | 'a 3% list increase in January 2023 was followed by a 2% volume fall... Linear extrapolation to a 5% increase... 3.3% expected volume loss... Compared with the expected loss of 2–5% (3d), the increase clears break-even with substantial room' |
| Must: EBIT effect as a range across volume reactions (e.g. about EUR 0.55m to 1.0m), with the arithmetic shown so finance can check it. | yes | Profit effect table: 0%→+1.20m, -2%→+0.98m, -3.3%→+0.84m, -5%→+0.66m, break-even→0; 'Arithmetic: new contribution = ... EBIT effect = 10.8×(1−loss%) − 9.6' |
| Must: differentiates by segment (e.g. OEM timing at the January renewal, distributor 60-day notice, discount cap and approval rule for small direct accounts). | yes | Implementation table: 'Fold into contract renewal / OEM key accounts / January 2027 renewal cycle'; 'Confirm 60-day distributor notice clears before 1 Mar'; 'Cap discretionary discount / Small direct accounts / ... Move approval above today's ~22% average to sales-director sign-off' |
| Must: anchors the recommendation on customer value and the like-for-like competitor gap, not on cost. | yes | 'Cost sets price floor only. Price justified by competitive position (3b) and revealed low elasticity (3d), not by cost'; benchmark notes Ravensworth's better on-time delivery (96% vs 90%) despite lower price, used as the value justification for not discounting |
| Must: names competitor reaction as a scenario (follow, hold, undercut) and says what would trigger a different answer. | yes | 3g table: 'Competitors hold current list prices', 'Competitors follow with their own increase', 'A competitor with spare capacity undercuts' each with a 'Signal to watch' |
| Must: answer line states the decision type (price level plus execution), the amount, the segments, the date and the EBIT range. | yes | 'raise list prices 5% on the standard seal range across all three segments from 1 March 2027 ... and cap small-direct-account discretionary discounts at the same time. Expected EBIT effect: +EUR 0.7m to +1.2m in year one' |
| Must: names the source of the 2023 market comparison (industry association data) and treats the 2023 response as one data point, stating whether the recommendation depends on it. | NO | Transcript never attributes the 2023 volume/market comparison to 'industry association data' or any named source anywhere in either file; it only says 'against flat market volume (so the loss is attributable to the price move, not the market)' without sourcing it, though it does treat it as a single |
| Must not: compute break-even with gross margin or without showing the formula. | yes | Break-even uses 'contribution margin 40%' with formula '1 − m/(m+p)' shown explicitly, not gross margin. |
| Must not: suggest sharing price intentions with competitors or using competitor contract data. | yes | Trap check: 'No competitor price coordination. Only public price lists (Sept 2026) and Ravensworth's own invoice/rebate data were used.' |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

I ran the pricing quick case on the Ravensworth data pack. Two files are saved in the working directory:

- `case-pricing-ravensworth.md` — full playbook trail (sharpened question, issue tree, all deciding analyses, trap checks)
- `case-pricing-ravensworth-answer.md` — the board-ready answer page

**Bottom line:** Yes, raise list prices 5% on the standard seal range from 1 March 2027, across all three segments, and cap small-direct-account discretionary discounts at the same time. Expected EBIT effect **+EUR 0.7m to +1.2m** in year one (base case ≈ +EUR 0.84m), well clear of the **11.1% break-even volume loss** (computed from 40% contribution margin and 5% price change) against an estimated 2–5% actual loss (extrapolated from the 2023 price-change episode). Confidence is **medium** — the competitor benchmark (7–9% below both rivals despite better on-time delivery) and the break-even math are solid, but the volume estimate rests on one historical data point.

Two things could change the answer before the January board meets:
1. **Distributor notice timing** — need the exact board date to confirm 60 days' notice clears before 1 March.
2. **OEM contract lock-in** — if January-renewing OEM contracts (55% of volume) fix price for 12 months, the increase may not reach them until the 2028 renewal, roughly halving year-one EBIT impact.

Both are flagged as open questions in the answer page, along with the missing customer-value data and a legal/competition-law check on the discount cap.


## Files in work dir after run

- case-pricing-ravensworth-answer.md
- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth-answer.md

# Pricing: Ravensworth Industrial Seals, can we raise standard-seal list prices 5% from 1 March 2027?

**Answer:** Yes — raise list prices 5% on the standard seal range across all three segments from 1 March 2027 (subject to the two timing checks below), and cap small-direct-account discretionary discounts at the same time. Expected EBIT effect: **+EUR 0.7m to +1.2m in year one** (base case ≈ +EUR 0.84m), against a break-even volume loss of 11.1% that is 2–5x the volume loss actually expected.
**Confidence:** Medium — the competitor benchmark and break-even arithmetic are strong, internal, recent data; the volume-loss estimate rests on a single historical episode (2023) and two implementation-timing questions (OEM contract renewal, distributor notice period) are unresolved.
**Specialists and review:** Legal/competition counsel should confirm the price-list announcement and the proposed small-direct discount cap raise no resale-price-maintenance issues before launch; contracts team to confirm OEM renewal timing (see Open questions).

## Price position
| Offer | Our price | Competitors | Value difference | Gap explained? |
|---|---|---|---|---|
| 40 comparable part numbers (same material, size, pressure rating) | Index 100 | Index 107–109 | Lead times comparable; Ravensworth on-time delivery 96% vs customers' stated 90% average | No — gap is unexplained headroom, not a discount for worse service |

## Value to customer
Not available from the pack — no customer downtime/failure-cost data to quantify value against the next-best alternative. The price benchmark above and the revealed volume response below substitute as evidence for this quick case; a full engagement would add customer interviews (see Open questions).

## Price waterfall (average, all segments, per EUR 100 of list)
| Step | Per 100 of list | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | -12% |
| Invoice price | 88 | 88% |
| Annual volume rebates | -4 | -4% |
| Free freight | -3 | -3% |
| **Pocket price** | **81** | **81%** |

19% of list already leaks before pocket price; the small-direct segment (15% of volume) carries the highest discount (22%) with no approval cap — the main execution risk to the increase reaching pocket price.

## Profit effect
Base: 2025 pocket revenue EUR 24.0m; contribution margin 40% (EUR 9.6m); price change p = 5%; break-even loss = 1 − 0.40/0.45 = **11.1%**.

| Volume reaction | Revenue effect | EBIT effect |
|---|---|---|
| 0% (no loss) | +EUR 1.20m | +EUR 1.20m |
| -2% (low end of estimate) | — | +EUR 0.98m |
| -3.3% (central estimate, from 2023 episode) | — | +EUR 0.84m |
| -5% (high end of estimate) | — | +EUR 0.66m |
| **Break-even volume loss** | — | **11.1% → EUR 0** |

Arithmetic: new contribution = (pocket revenue × 1.05 × (1 − loss%)) − (variable cost, fixed in EUR, scaled only by retained volume) = EUR 10.8m × (1 − loss%); original contribution = EUR 9.6m. EBIT effect = 10.8×(1−loss%) − 9.6.

## Implementation
| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|
| Raise list price 5% | All (standard seal range) | Announce by ~early Jan 2027; effective 1 Mar 2027 | Sales director | Confirm 60-day distributor notice clears before 1 Mar (see Open questions) |
| Fold into contract renewal | OEM key accounts (55% of volume) | January 2027 renewal cycle | Key account director | Confirm new contracts carry the 5% list price, not the prior rate |
| Cap discretionary discount | Small direct accounts (15% of volume) | Same date as the list change | Sales director | Move approval above today's ~22% average to sales-director sign-off; no more uncapped rep discretion |
| Hold distributor/OEM discount rules unchanged | Distributors, OEM | Same date | Key account director / Sales director | Already approved at director level; monitor for creep |

## What would change the answer
1. If the January board meets late enough that 60 days' notice to distributors does not clear before 1 March 2027, then push the distributor effective date to the next compliant date (e.g., 1 April 2027) rather than delaying the whole programme.
2. If OEM contracts renewing in January 2027 lock the prior price for the full 12-month term, then ~55% of volume will not see the increase until the January 2028 renewal, roughly halving the year-one EBIT effect.
3. If actual volume loss comes in above the 11.1% break-even (e.g., a competitor undercuts distributors), then hold distributor pricing and re-test before extending the increase further.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Volume loss from a 5% increase extrapolates linearly from the 2023 episode | 3.3% central estimate, 2-5% range | Only historical data point in the pack (3% increase → 2% loss vs flat market) | 2027 market/competitive conditions differ materially from 2023, or the true elasticity curve is non-linear at larger price changes |
| 2 | The 5% list increase flows proportionally through to pocket price (same discount/rebate %, no extra leakage) | 5% pocket price increase on retained volume | Simplifying assumption for the waterfall; execution fix (discount cap) is recommended specifically to make this hold | Small-direct discounting is not capped and absorbs part of the increase, shrinking the EBIT gain |
| 3 | Variable cost per unit is unaffected by the price change (contribution margin mechanics) | 40% margin, EUR 9.6m base contribution | Given by Ravensworth finance | Input costs change materially at the same time as the price move |
| 4 | Competitive position (Sept 2026 benchmark) still holds in March 2027 | 7-9% gap used as current headroom | Most recent competitor data available | A competitor repriced its list between Sept 2026 and March 2027 |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the exact January 2027 board date? | Determines whether distributors' 60-day notice clears before 1 March 2027 | Sales director / board secretary | May require a later effective date for distributors only |
| Do OEM contracts renewing in January 2027 lock in price for the full year, or can the new list price be built into that renewal? | 55% of volume; could defer most of the EBIT effect by a year if locked | Key account director / contracts team | Could roughly halve year-one EBIT effect if OEM is locked out |
| What volume-loss tolerance is the board actually willing to accept? | No threshold was given; this case used the 11.1% break-even as the test | Sales director / board | A stated lower tolerance could still pass (expected loss is 2-5%) but changes how the case is framed |
| What is the customer's economic value of a seal failure/downtime avoided? | Would let the increase be anchored on value, not just competitor gap and historical elasticity | Sales/marketing, via customer interviews | Could support a larger increase, or reveal a segment where 5% is too aggressive |
| Does the competition-law and resale-pricing review clear the announcement and the discount cap? | Legal risk check before launch | Legal counsel | Could require wording changes to the discount-cap rule |


## File written by the run: case-pricing-ravensworth.md

# Pricing quick case: Ravensworth Industrial Seals

Source: `cp-01-input.md`. Case type: pricing — price level decision.

## Step 1: Sharpen the question

Sharpened question: "By how much can Ravensworth raise list prices on the standard seal range, across all three customer segments, in 2027 without losing more than the break-even volume (11.1%, see Step 3e), and what is the EBIT effect?"

The sales director already named the move (list price, +5%, standard seal range, 1 March 2027, board decides in January). What the pack does not state, and this quick case cannot resolve from the data given:
- The volume risk the board is willing to accept (no stated threshold — so this case uses the computed break-even loss as the test, see Step 3e).
- The exact January board date, which determines whether distributors' 60-day notice period clears before 1 March 2027.
- Whether OEM key-account contracts renewing in January 2027 can carry the new price, or lock current price for 12 months.

These are carried into Open questions rather than blocking the arithmetic below.

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Position | List prices sit below both main competitors without a quality/service reason | Gap disappears, or is explained by worse spec/service | **Confirmed killed-the-kill-criterion**: gap is 7–9% and Ravensworth's service is *better* (96% vs 90% on-time), not worse |
| Execution | A material share of list price leaks between list and pocket price, concentrated where discount control is weakest | Leakage small and controlled | **Confirmed**: 19% average leakage; small-direct segment (15% of volume) has the highest discount (22%) and no approval cap |
| Volume reaction | Expected volume loss from a 5% increase stays well below the break-even loss | Expected loss near/above break-even, or contract cycles force mass renegotiation | **Confirmed, weak evidence**: one historical data point (2023) extrapolates to ~2–5% loss vs an 11.1% break-even |
| Competitor reaction | Main competitors hold or follow rather than undercut | A competitor with spare capacity undercuts in the core segment | **Provisionally confirmed, weak evidence**: competitors already price 7–9% higher; no capacity data in the pack |
| Value to customer | Customer value (seal reliability, downtime avoided) exceeds price by a wide margin | Value gap small/unquantifiable | **Open — no data**: pack has no customer economics; position + revealed behaviour substitute for this quick case |
| Structure | Charging differently captures more value | Not raised by the question | **Out of scope**: sales director asked about list price level only |

## Step 3: Deciding analyses

### 3a. Price waterfall

| Step | EUR per 100 list | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | -12% |
| Invoice price | 88 | 88% |
| Annual volume rebates | -4 | -4% |
| Free freight | -3 | -3% |
| **Pocket price** | **81** | **81%** |

By segment, on-invoice discount only (no segment breakdown exists for rebates/freight in the pack):

| Segment | Share of volume | On-invoice discount | Approver |
|---|---|---|---|
| OEM key accounts | 55% | 8% | Key account director |
| Distributors | 30% | 12% | Sales director |
| Small direct accounts | 15% | 22% | Any sales rep, **no cap** |

Weighted check: 0.55×8 + 0.30×12 + 0.15×22 = 11.3%, close to the reported 12% average (minor rounding, not material).

**Hypothesis: confirmed.** 19% of list price already leaks before pocket price, and the control is weakest exactly where the discount is highest (small-direct, uncapped). A list increase with no execution fix risks being discounted away in that segment. **Fix:** cap small-direct discretionary discount (e.g., at today's 22% average, or move approval above a threshold to the sales director) at the same time the list price rises.

### 3b. Price benchmark

| Offer | Our price | Competitors | Value difference | Gap explained? |
|---|---|---|---|---|
| 40 comparable part numbers (same material, size, pressure rating) | Index 100 | Index 107–109 (both main competitors) | Lead times comparable; Ravensworth on-time delivery 96% vs customers' stated 90% average for competitors | **No** — Ravensworth is priced below on a like-for-like basis despite a *better* service record, not a worse one |

**Hypothesis: confirmed.** There is no spec or service reason for the discount; it is headroom, not a market signal to hold price.

### 3c. Value to customer

Not available. The pack has no customer economics (downtime cost, failure cost, TCO of a seal) to quantify value against the next-best alternative. Marked **open** rather than estimated from memory — see Open questions. The price benchmark (3b) and revealed volume response (3d) substitute as the operative evidence for this quick case.

### 3d. Willingness to pay / volume reaction

Revealed behaviour, the only evidence in the pack: a 3% list increase in January 2023 was followed by a 2% volume fall over the next 12 months, against flat market volume (so the loss is attributable to the price move, not the market). Implied elasticity ≈ -2%/+3% ≈ -0.67.

Linear extrapolation to a 5% increase: 0.67 × 5% ≈ **3.3% expected volume loss**, with a plausible range of 2–5% given this rests on a single episode.

**Hypothesis: confirmed, weak evidence.** Treat 3.3% as a central planning estimate, not a precise forecast; the single 2023 data point is cross-checked against competitor benchmark in 3b.

### 3e. Break-even volume

Formula: break-even loss for a price increase = 1 − m / (m + p).

With p = 5% and contribution margin m = 40%: 1 − 0.40/0.45 = 1 − 0.8889 = **11.1%**.

Compared with the expected loss of 2–5% (3d), the increase clears break-even with substantial room (roughly 2–5x the expected loss).

### 3f. Segmentation

No segment-specific value or elasticity data exists to justify a differentiated *percentage*. The competitor gap (7–9%) is reported across all 40 comparable parts without segment split, so a uniform 5% list increase is defensible on the evidence in hand. What should differ by segment is **execution control**, not the headline number:
- OEM (55% of volume): lowest discount, most controlled approval, annual contract cycle — lowest execution risk, but timing-dependent (see Open questions).
- Distributors (30%): moderate discount, sales-director approval, 60-day notice period — needs lead time for the effective date.
- Small direct (15%): highest discount, no cap — highest execution risk; needs a discount cap alongside the increase (3a).

### 3g. Reaction and stress test

| Scenario | Likelihood (qualitative) | EBIT effect | Signal to watch |
|---|---|---|---|
| Competitors hold current list prices | Most likely — they already price 7-9% higher, no stated reason to cut | Gap narrows to ~2–4%, still below competitors; EBIT effect as in Profit effect table | No change to competitors' public price lists |
| Competitors follow with their own increase | Possible — same input cost pressure plausible industry-wide | Full EBIT effect, gap may persist | Competitor price lists rise in the following cycle |
| A competitor with spare capacity undercuts | Not evidenced in the pack (no capacity data) | Would mainly threaten distributors (no contract lock-in); OEM protected by annual contracts | A competitor's public list price drops, or distributor win-rate falls |

Sensitivity on volume loss: see Profit effect table below (0% to break-even 11.1%).

**Hypothesis: provisionally confirmed, weak evidence** (no direct competitor-capacity data; inferred from current price position only).

## Step 4: Trap checks

- [x] **Cost sets the floor only.** Price justified by competitive position (3b) and revealed low elasticity (3d), not by cost; contribution margin is used only for break-even, not to set the price.
- [x] **Stated WTP treated with care.** No stated-intent data exists in the pack; used revealed behaviour (2023 episode) instead, and flagged it as a single weak data point, not a precise elasticity.
- [ ] **Differs by segment where value/sensitivity differ.** Not fully met: no data supports a differentiated *percentage* by segment (open — see Open questions); execution controls are differentiated (3a, 3f).
- [x] **Execution fixed with the level.** Explicit recommendation to cap small-direct discretionary discount alongside the list change (3a).
- [x] **Break-even computed with contribution margin, compared with expected loss.** 11.1% vs 2–5% expected (3e).
- [ ] **Sales has arguments, incentives, approval rules.** Not addressed in the pack — open question.
- [x] **No competitor price coordination.** Only public price lists (Sept 2026) and Ravensworth's own invoice/rebate data were used.

## Step 5: Answer page

See `case-pricing-ravensworth-answer.md` (reproduced in the chat response).

