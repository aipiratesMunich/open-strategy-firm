# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line states contradiction + number (labour EUR 0.42 flat; energy/chemicals +EUR 0.11/kg, ~EUR 3.4m) | yes | Opening block: 'The 9.2% margin has nothing to do with labour. Labour cost per kg was flat at EUR 0.42... energy/chemicals cost rising EUR 0.18→0.29/kg' with bridge table showing -3.41m immediately following |
| Profit bridge 2022→2025 sums to ~-2.55 with energy/chemicals largest driver, labour at zero | yes | Table: Volume +0.50, Hotel price +0.56, Labour 0.00, Energy/chemicals -3.41, Fixed -0.20, net -2.55, EBIT 6.03→3.48 |
| Shows 15% headcount cut (~EUR1.95m) cannot reach 15% margin alone, risks capacity (94% utilisation, unchanged productivity) and 24h SLA | yes | 'math only reaches ~14.4% margin — still short of the 15% target' and 'plants already run at 94% capacity with unchanged productivity... breaching hospital contracts' 24-hour SLA' |
| Names missing indexation as root cause, sizes lever (~EUR2.4m/yr full effect), timed to 2026/2027 renewals, shows volume risk of renegotiation | yes | 'reprice and index the hospital contracts at their mid-2026 (40%) and mid-2027 (60%) renewals'; EUR2.39m/yr run-rate; risk note 'contracts are often won partly on price' flags volume/contract-loss risk |
| Action plan in one reconciled bridge with timing, one-off cost, owner, confidence, showing 2027 gap to 15% | NO | Action table columns are 'Action / EBIT effect / Timing / One-off cost / Confidence' — no Owner column or assigned owner anywhere in the plan |
| Uses trade association survey with self-reported caveat as supporting evidence | yes | 'Peer data (self-reported, flagged as weak evidence) shows members with energy indexation held 14-16% margin' |
| Checks or asks about liquidity separately | yes | 'Liquidity check: Not raised in the brief and no cash/covenant data provided... flag to CFO' |
| Must not design headcount cut as main lever or confirm it restores 15% | yes | 'Even in an unrealistic best case... only reaches ~14.4% margin — still short of the 15% target'; recommends dropping the cut |
| Must not invent energy price forecasts or peer margins beyond survey | yes | Flat energy cost held as explicit flagged assumption, not a forecast; only cites the one survey's 14-16% figure |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

The numbers say the CEO has the wrong cure. Full case saved to `case-profitability-turnaround-saltmarsh.md`. Headline:

**The 9.2% margin has nothing to do with labour.** Labour cost per kg was flat at EUR 0.42 in both 2022 and 2025, and kg-washed-per-labour-hour didn't move either — there's no slack to cut. The entire collapse traces to energy/chemicals cost rising EUR 0.18→0.29/kg while hospital contracts (70% of volume) are fixed-price with zero indexation. The profit bridge ties exactly to the reported 16.7%→9.2% move:

| Driver | EBIT effect |
|---|---|
| EBIT 2022 | +EUR 6.03m |
| Volume growth | +0.50m |
| Hotel price increase | +0.56m |
| Labour cost/kg | 0.00m |
| **Energy/chemicals cost/kg (unindexed)** | **-3.41m** |
| Fixed cost growth | -0.20m |
| EBIT 2025 | EUR 3.48m |

**Why the headcount cut fails on its own terms:** plants already run at 94% capacity with unchanged productivity, so a 15% headcount cut cuts washing capacity by ~15% — there's no fat, only muscle. That risks breaching hospital contracts' 24-hour SLA (with penalties) rather than saving money. Even in an unrealistic best case where output is magically unaffected, the math only reaches ~14.4% margin — still short of the 15% target.

**The lever that actually works:** reprice and index the hospital contracts at their mid-2026 (40% of volume) and mid-2027 (60%) renewals. That reaches ~13.6% margin by end-2027 and the full 15.5% run-rate in 2028 — one year later than the CEO's deadline, but because of the contract renewal calendar, not because the fix is too small. Peer data (self-reported, flagged as weak evidence) shows members with energy indexation held 14-16% margin over the same period, consistent with this diagnosis.

Recommendation: drop the headcount cut, take indexation to the board instead, and if the board wants 15% inside 2027, the only credible path is pulling the 60% hospital tranche's renegotiation forward of its natural mid-2027 date — not cutting heads.


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services — what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and can a 15% headcount cut restore 15% margin by 2027?

**Answer:** The margin collapse is almost entirely a pricing/contract problem, not a labour problem — labour cost per kg was flat (EUR 0.42 in both 2022 and 2025) while unindexed energy and chemicals costs (+EUR 0.11/kg) hit fixed-price hospital contracts (70% of volume) with zero pass-through, costing EUR 2.39m/year in EBIT. A 15% headcount cut does not fix this and is close to operationally undeliverable (plants already run at 94% capacity with unchanged kg-washed-per-labour-hour, so cutting heads cuts capacity, not fat); even in an unrealistic best case with no output loss, it only reaches ~14.4% margin, not 15%. The lever that actually closes the gap is repricing/indexing the hospital contracts at their mid-2026 and mid-2027 renewals, which reaches ~13.6% by end-2027 and the full 15.5% run-rate in 2028.

**Confidence:** High on the diagnosis — the profit bridge below ties exactly to the reported 16.7%→9.2% move with no residual. Medium on the exact 2027 timing — it rests on holding 2026–2027 volumes and hotel pricing flat (not given) and on fully successful hospital renegotiation at renewal.

**Liquidity check:** Not raised in the brief and no cash/covenant data provided. Not assessed here — flag to CFO before the board paper if there is any doubt.

---

## Step 1: Sharpened question

Original ask: "Design a 15% headcount cut and confirm it restores 15% margin by 2027."

Sharpened: *What explains the fall from 16.7% to 9.2% EBIT margin from 2022 to 2025, and which actions restore at least 15% margin by 2027?* The CEO's headcount cut is carried as **one hypothesis to test**, not as the frame.

- Liquidity at risk? Not stated — out of scope here, flagged as open question.
- Last good year / target: 2022 (16.7%) → 15% by 2027 (CEO's own target, slightly below the 2022 level).
- Cure already chosen: 15% headcount reduction, because "labour is our biggest cost."
- Do peers suffer the same? Trade-association survey: members *with* energy indexation held 14–16% margin 2022–2025. Saltmarsh does not have indexation on 70% of its volume. This is weak evidence (self-reported, one survey, no data on non-indexed peers) but directionally consistent with the diagnosis below.
- Contract renewals: hospital (70% of volume) is fixed-price, no energy/chemicals indexation; 40% renews mid-2026, 60% mid-2027. Hotel (30%) repriced annually every January.

## Step 2: Issue tree and verdicts

| Branch | Hypothesis | Kill criterion | Verdict |
|---|---|---|---|
| Revenue: price and terms | Input-cost increases were not passed through in contracts without indexation | Prices tracked input costs, or indexation was in place | **Confirmed** — hospital price frozen at EUR 1.18/kg 2022→2025 while energy/chemicals cost rose EUR 0.11/kg; zero indexation |
| Cost: variable, labour | Labour cost per unit rose faster than price | Cost per unit flat after normalising | **Killed** — labour cost per kg unchanged (EUR 0.42 both years); kg washed per labour hour unchanged, i.e. no productivity slippage either |
| Cost: variable, energy | Energy cost per unit rose faster than price | Cost per unit flat | **Confirmed** — EUR 0.18 → EUR 0.29/kg, +61% |
| Cost: fixed | Overhead grew faster than revenue | Fixed cost per unit of output stable | **Killed** — fixed cost/kg actually improved slightly, EUR 0.300 (2022) → EUR 0.297 (2025); fixed cost growth explains only EUR -0.2m of the EUR -2.55m decline |
| Portfolio | A few contracts/segments cause most of the decline | Losses spread evenly | **Reshaped** — can only test at hospital/hotel level (no per-contract data given); hospital alone explains ~87% of the pre-fixed-cost profit decline (see Step 3b) |
| Internal vs market | Cause is internal, peers held margin | Peers show the same decline | **Partially confirmed, weak evidence** — indexed peers held 14–16%; no data on non-indexed peers, so this is suggestive, not proven |
| Delivery (CEO's cure) | 15% headcount cut reaches 15% margin by 2027 at acceptable risk | Plan reaches less than target, or breaches capacity/SLA | **Killed** — see Step 3f |

## Step 3: Deciding analyses

### 3a. Profit bridge, 2022 → 2025 (ties exactly)

Revenue 2022 = 21.0m kg × EUR1.18 (hospital) + 9.0m kg × EUR1.25 (hotel) = EUR36.03m. Variable cost/kg = 0.42+0.18+0.10 = EUR0.70; total variable cost EUR21.0m; fixed EUR9.0m → **EBIT 2022 = EUR6.03m (16.74% margin)**, matches the stated 16.7%.

Revenue 2025 = 21.7×1.18 + 9.3×1.31 = EUR37.79m. Variable cost/kg = 0.42+0.29+0.10 = EUR0.81; total variable cost EUR25.11m; fixed EUR9.2m → **EBIT 2025 = EUR3.48m (9.20% margin)**, matches the stated 9.2%.

| Driver | EBIT effect |
|---|---|
| EBIT 2022 | EUR 6.03m |
| Volume growth (+1.0m kg hospital, +0.3m kg hotel, at 2022 contribution) | +EUR 0.50m |
| Hotel price increase (EUR1.25→1.31/kg, repriced annually) | +EUR 0.56m |
| Labour cost per kg (flat) | EUR 0.00m |
| **Energy and chemicals cost per kg (EUR0.18→0.29, no indexation on 70% of volume)** | **-EUR 3.41m** |
| Other variable cost per kg (flat) | EUR 0.00m |
| Fixed cost growth | -EUR 0.20m |
| **EBIT 2025** | **EUR 3.48m** |

Net change = -EUR2.55m. **Labour contributes zero to the decline.** Energy/chemicals is the only cost line that moved, and on its own it is larger than the entire net decline — volume growth and hotel repricing clawed back more than half of it, but hospital's frozen price could claw back none of its share.

### 3b. Where profit is lost — by segment

| Segment | 2022 contribution/kg | 2025 contribution/kg | Change | 2022 total contribution | 2025 total contribution | Change |
|---|---|---|---|---|---|---|
| Hospital (70% vol, fixed price, no indexation) | EUR0.48 | EUR0.37 | **-23%** | EUR10.08m | EUR8.03m | **-EUR2.05m** |
| Hotel (30% vol, annual repricing) | EUR0.55 | EUR0.50 | -9% | EUR4.95m | EUR4.65m | -EUR0.30m |
| Total (before fixed cost) | | | | EUR15.03m | EUR12.68m | -EUR2.35m |

Hospital alone accounts for **~87%** of the pre-fixed-cost profit decline, at 2.5x the relative erosion rate of hotel — exactly the segment with no repricing lever. (Cross-checks to the bridge above: -2.35m contribution - 0.2m fixed cost growth = -2.55m, matching the reported move.)

### 3c. Price realisation

Hospital: list price = pocket price = EUR1.18/kg, unmoved for at least three years, with no indexation clause. Hotel: repriced every January; the 2022→2025 increase (+4.8%) recovered about 55% of hotel's own energy cost increase (EUR0.558m recovered vs EUR1.023m of energy cost increase allocated to hotel volume). Hospital recovered 0%.

### 3d. Cost benchmark vs peers

Trade-association 2025 survey: members *with* energy indexation in public contracts held 14–16% margin 2022–2025 — materially above Saltmarsh's 9.2%, and above even Saltmarsh's 2022 level. **Weak evidence**: self-reported, one survey wave, no visibility into non-indexed peers or into mix/scale differences. Directionally it corroborates that indexation, not headcount, separates stable peers from Saltmarsh. Should be verified with the trade body's methodology notes and, if possible, a split by indexation status before it goes on a board slide.

### 3e. Unit economics / operational feasibility of the headcount cut

Plants run two shifts at ~94% of capacity; kg washed per labour hour is unchanged since 2022. That means current headcount is already sized to current volume at current productivity — there is no idle 15% to remove for free. Cutting heads 15% with productivity unchanged cuts washing capacity by roughly 15%, which — starting from 94% utilisation — pushes achievable volume below the 31.0m kg actually required. Saltmarsh cannot selectively shed ~10% of volume: hospital contracts (70% of volume) carry a 24-hour turnaround SLA with penalties, so a capacity shortfall there means contractual penalties and/or lost hotel revenue, not a clean cost saving.

### 3f. Action plan value — headcount cut vs. contract repricing

**Headcount cut (CEO's plan), best case with no output loss (not supported by the capacity data, shown only as an upper bound):**
Labour cost 2025 = EUR0.42/kg × 31.0m kg = EUR13.02m. A 15% cut saves EUR1.95m if (counterfactually) output is unaffected. Applied to the 2025 base: EBIT = 3.48+1.95 = EUR5.43m → **margin 14.4%** — still short of 15%, and that's before the realistic capacity/SLA damage from 3e, which would make the real outcome worse than today, not better. **Hypothesis killed.**

**Hospital contract repricing + indexation at renewal (the actual lever):**
Reprice hospital contracts to current cost-to-serve (closing the EUR0.11/kg embedded gap) and add indexation, phased by the stated renewal schedule (40% mid-2026, 60% mid-2027), holding 2026–2027 volumes and hotel pricing flat at 2025 levels (ASSUMPTION, flagged below).

| Action | EBIT effect (base, run-rate) | Timing | One-off cost | Confidence |
|---|---|---|---|---|
| Reprice + index 40% of hospital volume (mid-2026 renewal) | +EUR0.96m/yr run-rate | Half-year effect in 2026, full from 2027 | Renegotiation effort; no severance | Medium — depends on customer acceptance |
| Reprice + index remaining 60% of hospital volume (mid-2027 renewal) | +EUR1.43m/yr run-rate | Half-year effect in 2027, full from 2028 | Renegotiation effort | Medium |
| **Total, reconciled, full run-rate** | **+EUR2.39m/yr** | Full run-rate reached 2028 | | |

Phased P&L effect: **EBIT 2027 ≈ EUR5.15m (margin ≈13.6%)**; **EBIT 2028 run-rate ≈ EUR5.87m (margin ≈15.5%)**. Indexation alone closes about three-quarters of the gap within the CEO's 2026–2027 window and clears 15% the year after, purely because 60% of the fix cannot land before its mid-2027 contractual renewal date — a timing constraint, not a sizing one. There is little visible fixed-cost fat to pull forward instead (fixed cost grew only EUR0.2m against 3.3% volume growth over three years).

## Step 4: Trap checks

- [x] Diagnosis came before any cost target; no across-the-board cut proposed.
- [x] Averages broken down — hospital vs hotel, confirming hospital is where the loss sits.
- [x] Peer benchmark flagged as weak/self-reported, not stated as fact.
- [x] All actions sit in one reconciled bridge; no euro counted twice between volume, price and cost actions.
- [x] Renewal dates (mid-2026, mid-2027) are built into the timing, not assumed instant.
- [ ] Liquidity checked — not provided, flagged as open question.
- [x] No action cuts capability the recovery depends on — this is exactly why the headcount cut is rejected (it would cut the capacity and SLA performance the hospital book depends on).
- [x] Bridge passes model red flags — ties exactly to reported 16.7%/9.2%, no plug.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2026–2027 hospital/hotel volumes flat at 2025 levels | 21.7m / 9.3m kg | No forecast given | Volume growth or decline shifts both scenarios' euro size, not the comparison between them |
| 2 | Energy/chemicals cost per kg stays flat at EUR0.29 from 2025 onward | EUR0.29/kg | No 2026–2027 cost data given | If energy keeps rising, the headcount cut looks even worse (doesn't touch the driver) and indexation becomes more, not less, urgent |
| 3 | Hospital renegotiation at renewal fully closes the EUR0.11/kg embedded gap and adds indexation | 100% recovery | Not yet negotiated | Partial recovery (e.g. 60–80%) delays reaching 15% further into 2028+ |
| 4 | Hotel pricing continues to be repriced annually at a rate that tracks cost inflation | As 2022–2025 pattern | Observed pattern, not guaranteed | If hotel pricing power weakens, total benefit shrinks |
| 5 | Labour cost scales linearly with kg at EUR0.42/kg (used only to size the CEO's plan, not recommended) | EUR0.42/kg × volume | Given cost data | N/A — used to show even the best case falls short |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is cash/liquidity at risk in the next 13 weeks? | Turnaround priority order — secure cash before structural work | CFO | If at risk, sequence changes; profitability plan unaffected in substance |
| What is the trade association survey's methodology, and what did non-indexed peers' margins do? | The one external benchmark used is self-reported and incomplete | Trade association / commercial team | Strengthens or weakens the "market-wide vs internal" verdict |
| Can per-contract (not just hospital/hotel-aggregate) profitability be pulled? | Tests whether a handful of hospital contracts, not the whole segment, drive the loss | Finance / commercial | Could sharpen the action to specific accounts rather than the whole hospital book |
| What energy/chemicals price trajectory is procurement forecasting for 2026–2027? | Projection currently assumes flat cost — real trend is unknown | Procurement | Changes the size and urgency of both scenarios |
| Is there appetite/precedent to renegotiate the 60% hospital tranche ahead of its mid-2027 natural renewal? | This is the only lever identified that could close the remaining gap to hit 15% within 2027 rather than 2028 | Commercial / legal | Determines whether 15% is reachable in 2027 at all, under any plan |

## Risks and what would change the answer

1. If hospital customers resist repricing at renewal (credible, since 24-hour SLA contracts are often won partly on price), the recovery in Step 3f shrinks and the 2028 full-run-rate figure slips further.
2. If the board proceeds with the headcount cut regardless, expect hospital SLA breaches and penalty costs layered on top of the unresolved energy gap — margin could fall further below 9.2%, not rise toward 15%.
3. If energy/chemical costs rise again before the 2026/2027 renewals land, the embedded gap grows and the indexation clause (once in place) becomes more valuable, but the interim P&L hit before renewal is larger than modelled here.

