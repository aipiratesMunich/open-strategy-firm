# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the price waterfall first and states that a list increase only reaches pocket price if discounts do not widen, with the uncapped 22% for small direct accounts named as the leak. | yes | 'Price waterfall (run first)' ... 'a list increase should scale through to pocket price mechanically — provided discretionary discounting doesn't absorb it. The one segment with no discount cap (small direct accounts, any rep, 22% average, 15% of volume) is the specific leak' |
| Break-even volume loss of about 11% computed with contribution margin, formula or arithmetic shown. | yes | 'break-even loss = 1 − m/(m+p) ... = 1 − 0.40/(0.40+0.05) = 1 − 0.8889 = 11.1%' |
| Uses the 2023 change (-2% for +3%) as revealed behaviour and compares the expected loss with the break-even. | yes | 'the January 2023 increase of 3% was followed by a 2% volume decline ... Linear extrapolation to a 5% increase: 2% × (5/3) ≈ 3.3%' compared against '11.1%' break-even |
| EBIT effect as a range across volume reactions, with arithmetic shown. | yes | Table: 0%→+1.20, -2%→+0.98, -3.3%→+0.84, -5%→+0.66, break-even→0.00, with arithmetic column (e.g. '24.0×(1.05×0.95−1); Cost saved: 14.4×0.05') |
| Differentiates by segment (OEM timing, distributor notice, small-direct discount cap/approval). | yes | Implementation table: OEM 'January 2027 renewals', Distributors '60 days' notice', Small direct 'introduce an approval threshold' |
| Anchors the recommendation on customer value and the like-for-like competitor gap, not on cost. | yes | 'The 5% is anchored on the 7–9% competitor gap and Ravensworth's service edge, not on cost. Cost (via contribution margin) only sets the break-even floor.' |
| Names competitor reaction as a scenario (follow, hold, undercut) and says what would trigger a different answer. | yes | 'Main competitors hold or follow' / 'the base case is "hold"' / 'A competitor cutting further would need spare capacity and a strategic reason' |
| Answer line states decision type (price level plus execution), amount, segments, date, EBIT range. | yes | 'raise list prices 5% on the standard seal range from 1 March 2027, uniformly, but fix execution at the same time ... EBIT effect is +EUR 0.7–1.2m' |
| Names the source of the 2023 market comparison (industry association data) and treats it as one data point, stating dependency. | NO | The 2023 analog is discussed ('against a flat market', 'a single data point at a different price level') but no source such as industry association data is ever named anywhere in the transcript. |
| Must not compute break-even with gross margin or without showing the formula. | yes | Break-even formula explicitly uses contribution margin (40%) and is shown algebraically. |
| Must not suggest sharing price intentions with competitors or using competitor contract data. | yes | 'No competitor coordination. Only public competitor price lists (September 2026) and Ravensworth's own invoice/rebate data were used.' |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

Answer page written to `case-pricing-ravensworth.md`.

**Bottom line:** raise list prices 5% on the standard seal range from 1 March 2027, uniformly, but fix execution at the same time (cap the uncapped small-direct discount, confirm OEM contract mechanics, check the distributor 60-day notice window against the January board date). EBIT effect is **+EUR 0.7–1.2m** in realistic volume-loss scenarios (2–5%), versus an **11.1% break-even** loss — a wide safety margin, since Ravensworth stays 2–4 points below both competitors even after the increase.

Confidence is medium rather than high because three implementation facts aren't in the data pack: whether OEM contracts lock an absolute price (would delay ~55% of volume reaching the new pocket price), whether distributor notice timing fits the March 1 date, and the board's own volume-risk tolerance — all listed in Open questions in the file, along with the full waterfall, benchmark, break-even arithmetic, and trap checks.


## Files in work dir after run

- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth.md

# Pricing: Ravensworth Industrial Seals, can list prices on the standard seal range rise 5% from 1 March 2027?

**Answer:** Raise list prices 5% on the standard seal range from 1 March 2027, applied uniformly across segments, but fix execution at the same time — cap the uncapped small-direct discount, confirm how OEM contracts reference list price, and check distributor notice timing. EBIT effect is **+EUR 0.7m to +1.2m** in the first 12 months under realistic volume-loss scenarios (2–5% loss), against a break-even volume loss of **11.1%** — a wide margin of safety.
**Confidence:** Medium — the price/value logic and break-even arithmetic are solid, but three execution facts are unverified (OEM contract mechanics, distributor 60-day notice window against the January board date, and the uncapped small-direct discount) and could delay or erode the gain.
**Specialists and review:** None required for the pricing decision itself. Legal/competition review not triggered — no competitor price information was shared or coordinated, only public list prices and Ravensworth's own data were used. Contracts/legal should confirm OEM contract wording (see open questions) before the sales director commits to a March 1 date for that segment.

## Step 1: Sharpened question

Original ask: "Can we raise list prices on the standard seal range by 5% from 1 March 2027?"

Sharpened: **"By how much can Ravensworth raise list prices on the standard seal range in 2027 without losing more than x% volume, and what is the EBIT effect?"** This is a price-*level* decision (not structure or execution), in scope for the full standard seal range, across all three segments (OEM key accounts, distributors, small direct accounts). The board's own volume-risk tolerance (x%) was not stated in the data pack — carried into Open questions below rather than assumed.

## Step 2: Issue tree (instantiated)

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Position | List prices sit below comparable competitors without a spec/service reason | Like-for-like gap gone after adjusting for spec/service | **Confirmed** — 7–9% below on 40 matched part numbers; Ravensworth's service is *better*, not worse (96% vs 90% on-time) |
| Execution | A material share of list price leaks between list and pocket price | Leakage small and controlled | **Confirmed leakage exists (19 points), but controllable** — mechanism is % of list, so a list increase should pass through *if* discretionary discounting is capped |
| Willingness to pay / volume reaction | Expected volume loss stays well below break-even loss | Expected loss near/above break-even | **Confirmed** — best available evidence (2023 analog) implies 2–5% loss vs an 11.1% break-even |
| Competitor reaction | Main competitors hold or follow | A competitor with spare capacity undercuts in the core segment | **Provisionally confirmed** — post-increase, Ravensworth is still 2–4 points below both competitors, so no reason for them to react |
| Value to customer | Value exceeds price by a wide margin | Value gap small/unquantifiable | **Open** — no downtime/failure-cost data in the pack; only the delivery-performance proxy is available |

## Step 3: Deciding analyses

### a. Price waterfall (run first)

| Step | EUR per 100 list | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | -12% |
| Invoice price | 88 | 88% |
| Annual volume rebates | -4 | -4% |
| Free freight | -3 | -3% |
| **Pocket price** | **81** | **81%** |

19 points of list price leak away before cash is collected. **Hypothesis reshaped, not killed**: leakage is real but every step is expressed as a percentage of list, so a list increase should scale through to pocket price mechanically — *provided* discretionary discounting doesn't absorb it. The one segment with no discount cap (small direct accounts, any rep, 22% average, 15% of volume) is the specific leak to close concurrently with the increase (see Implementation).

On-invoice discount by segment (55/30/15% volume split, 8%/12%/22% average discount) weights to ~11.3%, close enough to the reported 12% average to treat as consistent.

### b. Price benchmark

| Offer | Our list price (index) | Competitors (both, index) | Value difference | Gap explained? |
|---|---|---|---|---|
| Standard seal, 40 matched part numbers | 100 | ~108–110 | Ravensworth cheaper by 7–9% | **No** — lead times comparable and Ravensworth's on-time delivery is *better* (96% vs customers' stated 90% average), so the gap is not a quality or service discount |

After a 5% increase, Ravensworth's index moves to 105 — still 2–4 points below both competitors. The increase closes part of an unexplained gap rather than pricing above the market.

### c. Value to customer

Not quantifiable from the data pack — no downtime, failure-cost, or total-cost-of-ownership figures were supplied. The only available proxy is the delivery-performance edge (96% vs 90% on-time), which supports pricing power directionally but doesn't size it. **Flagged as an open question for a full engagement**, not a blocker for this decision, since the benchmark and break-even evidence already clear a wide margin.

### d. Willingness to pay (revealed behaviour first)

Only revealed-behaviour data point available: the January 2023 increase of 3% was followed by a 2% volume decline over the next 12 months, against a flat market (i.e., a real share loss, not a market-wide dip). Treated as the strongest evidence in hand (revealed, not stated), but it is a **single data point at a different price level (3% vs 5%)**, so scaling it is judgement, not measurement:

- Linear extrapolation to a 5% increase: 2% × (5/3) ≈ **3.3%** expected volume loss.
- Base case used below: **2–5%** range, bracketing the historical analog and a stress case.

**Evidence grade: weak-to-medium.** One historical analog, no segment breakdown, and increases of this size don't always scale linearly — cross-check with segment-level win/loss data before committing (Open questions).

### e. Break-even volume

Formula: break-even loss = 1 − m/(m+p), with m = 40% contribution margin, p = 5% price increase.

break-even loss = 1 − 0.40/(0.40+0.05) = 1 − 0.8889 = **11.1%**

The expected loss range (2–5%) sits well inside this — Ravensworth would need to lose more than two to five times the volume implied by the 2023 analog before the increase destroys value.

### f. Segmentation

No segment-specific competitor benchmark or value data exists to justify a *different* percentage increase by segment — so the 5% is applied uniformly to list price. What *does* differ by segment is execution risk and timing (see Implementation): OEM (55%, annual contracts renewing in January) and small direct (15%, uncapped discount) are the two segments needing specific handling; distributors (30%) are the segment with a hard notice-period constraint.

### g. Reaction and stress test

| Volume reaction | Revenue effect (EURm) | EBIT effect (EURm) | Arithmetic |
|---|---|---|---|
| 0% (volume holds) | +1.20 | +1.20 | 24.0 × 0.05 |
| -2% (2023 analog, unscaled) | +0.70 | +0.98 | Rev: 24.0×(1.05×0.98−1); Cost saved: 14.4×0.02 |
| -3.3% (linear extrapolation to 5%) | +0.37 | +0.84 | Rev: 24.0×(1.05×0.967−1); Cost saved: 14.4×0.033 |
| -5% (stress case) | -0.06 | +0.66 | Rev: 24.0×(1.05×0.95−1); Cost saved: 14.4×0.05 |
| **Break-even** | **-1.60** | **0.00** | at **-11.1%** volume loss |

Base: pocket revenue EUR 24.0m, contribution margin 40% (contribution EUR 9.6m, variable cost EUR 14.4m). EBIT effect = Revenue effect + variable cost saved on lost volume. All scenarios inside the plausible range are solidly EBIT-positive.

**Competitor reaction scenario:** since Ravensworth remains 2–4 points below both competitors even after the increase, the base case is "hold" (no reason for competitors with no price gap to react). A competitor cutting further would need spare capacity and a strategic reason not evidenced in the data pack — flagged as a watch item, not a base case.

## Step 4: Trap checks

- [x] **Cost sets the floor only.** The 5% is anchored on the 7–9% competitor gap and Ravensworth's service edge, not on cost. Cost (via contribution margin) only sets the break-even floor.
- [x] **Stated WTP vs revealed.** No stated-intent data was used; the one willingness-to-pay data point (2023) is revealed behaviour. Marked weak/medium evidence and not overstated.
- [ ] → **Noted, not fully closed. Uniform increase.** No segment-level value or benchmark data exists to differentiate the *percentage*, so 5% is applied uniformly — but execution treatment differs by segment (see Implementation). A full engagement should get segment-level benchmark/WTP data before a second round of changes.
- [x] **Execution fixed with the level.** Small-direct discount cap recommended concurrently (see Implementation) — without it, the increase leaks on 15% of volume with no sales approval barrier today.
- [x] **Break-even computed with contribution margin.** 11.1%, compared against a 2–5% expected loss range above.
- [ ] → **Open.** Sales incentive and argument-equipping not evidenced in the data pack — added to Implementation and Open questions (key account directors and reps need the competitor-gap and service-record numbers as talking points).
- [x] **No competitor coordination.** Only public competitor price lists (September 2026) and Ravensworth's own invoice/rebate data were used.

## Implementation

| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|
| Raise list price 5% | All (standard seal range) | Effective 1 March 2027 | Sales director | Board approval in January |
| Build into contract renewal | OEM key accounts (55%) | January 2027 renewals | Key account director | Confirm first whether contracts lock an absolute price or a list-minus-discount formula (open question) |
| Give 60 days' notice | Distributors (30%) | As soon as board decides | Sales director | Must land 60 days before the effective date — check board decision date against 1 March 2027 (open question) |
| Cap discretionary discount | Small direct accounts (15%) | Concurrent with the increase | Sales director | Currently any rep, no cap, 22% average — introduce an approval threshold so the increase reaches pocket price |
| Equip sales with arguments | All, especially OEM/distributor reps | Before notice goes out | Sales director | Use the competitor benchmark (7–9% gap) and delivery record (96% vs 90%) as the justification |

## What would change the answer

1. If OEM contracts lock an absolute price for the contract year rather than a list-minus-discount formula, the increase will not reach ~55% of pocket revenue until the January 2028 renewal — then the year-1 EBIT effect above would roughly halve.
2. If the small-direct discount cap is not put in place and reps discount the increase away, the 15%-of-volume segment contributes little to the EBIT gain.
3. If actual volume loss comes in near or above 11.1% (e.g., because the 5% increase provokes a non-linear reaction unlike the 2023 3% increase), the increase would destroy value rather than add to it — worth a mid-year check against actual volume.
4. If the board's own accepted volume-loss threshold (not stated in the data pack) is tighter than the 2–5% expected range, the recommendation should be revisited or phased.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | On-invoice discounts, rebates and freight allowances are set as a percentage of list price, so they scale through proportionally when list price rises | Pass-through to pocket price scales with list price | Price waterfall expresses every step as % of list (2025 data) | Rebates or freight are fixed-euro amounts under current contracts — pass-through would be less than 5% at pocket-price level |
| 2 | Expected volume loss from a 5% increase | 2–5% range (base case ~3.3%) | Extrapolated from the 2023 analog (3% increase → 2% loss vs flat market) | Segment-level elasticity turns out non-linear or concentrated (e.g., small-direct accounts far more sensitive) — would need segment win/loss data to refine |
| 3 | Contribution margin stays at 40% of pocket revenue through the March 2027 implementation | 40% | Ravensworth finance, 2025 | Material input-cost moves before March 2027 change the margin and the 11.1% break-even threshold |
| 4 | The 5% increase is applied uniformly across all three segments | Uniform 5% on list | No segment-specific value or benchmark data available to justify differentiation | Segment-level benchmark or WTP data becomes available showing OEM/distributor/small-direct differ materially |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What maximum volume loss is the board willing to accept for this decision? | Sets the real decision bar; this answer uses the 11.1% break-even as the economic floor, but the board's risk appetite may be tighter | Sales director / board | If the accepted threshold is below ~5%, the recommendation still holds on current evidence; if much tighter (e.g., 1%), a smaller or phased increase may be preferred |
| Can the board decision and distributor notice (60 days) land in time for a 1 March 2027 effective date? | Distributors are 30% of volume; a late-January decision may not allow 60 days' notice before March 1 | Sales director / sales ops | May require a later effective date for distributors specifically (e.g., April/May), phased from OEM/small-direct |
| Do OEM annual contracts reference list price with a fixed discount %, or lock an absolute price for the contract year? | OEM is 55% of volume; if contracts lock an absolute price, the increase won't reach OEM pocket price until the *next* renewal | Key account director / contracts | Could materially delay or roughly halve the year-1 EBIT effect |
| Can small-direct account discounting be capped at the same time as the list increase? | This segment has no discount cap today (any rep, 22% average) and is the highest-leakage risk | Sales director | Without a cap, part of the 15%-of-volume segment's increase may be discounted away, reducing the EBIT effect |
| What does segment-level (not just aggregate) win/loss and elasticity data show? | The volume-loss estimate rests on one historical analog with no segment breakdown | Sales / finance (win-loss data), possibly customer interviews | Would narrow the 2–5% range and raise confidence from medium to high |
| What is the quantified customer value (downtime/failure cost) behind the delivery-performance edge? | Would support pricing above the simple competitor-gap benchmark, and could justify a larger or differentiated increase in a follow-up study | Key accounts / technical sales | Out of scope for this quick case; would feed a fuller value-based pricing study if the board wants to go further than 5% |

