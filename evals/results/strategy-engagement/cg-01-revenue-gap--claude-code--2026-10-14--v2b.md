# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap EUR140m→175m by 2030, EUR15m capital, no acquisitions, EBIT margin ≥10%, board March 2027) | yes | Title states gap/capital/margin; constraints row adds 'no acquisitions this cycle'; next steps/answer reference the '2027-03 board meeting'. |
| Computes a momentum case of about EUR140-141m and a gap of about EUR34m | yes | 'Total momentum: 75.2 + 45.5 + 20.0 ≈ EUR140.7m' and 'Gap (momentum vs. target) ... EUR34.3m'. |
| Separates market growth from share change and states Kirkby lost share in both lab instruments and process sensors | yes | 'Hypothesis confirmed: the served markets are growing in all three segments; Kirkby is losing share in all three.' with Lab and Process sensors marked 'Losing share'. |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with base case/range/evidence grade | NO | Price and service levers get base case/range/grade, but 'Lab instruments share-loss fix' and 'Process sensors share-loss fix' rows are explicitly 'Not sized' / EBIT 'Unknown' / grade 'No data in this pack' — share recovery itself is never actually sized, only flagged as an open question. |
| Installed-base lever about EUR4.3m at 50% coverage (or consistent alternative) | yes | Base case +EUR5.6m from 30% capture of the uncontracted base (14,300 contracts × ~EUR1,299), which scales consistently to ~EUR4.3m per 15pp of coverage, matching the reference per-contract economics. |
| Treats EUR15m software as unsupported: widens range or kills it, names the comparison that would settle it without inventing one | yes | Range widened to 'EUR3-8m' (claim range 'EUR3m-15m'), graded 'Weak', and open question asks 'Is there any comparable industrial-software launch ... to benchmark the ramp curve' without fabricating one. |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor | yes | Levers table lists EBIT effect per lever; 'Group EBIT at kept levers ... ≈14.1% margin, comfortably above the 10% floor.' |
| Shows the remaining gap openly after base-case levers and says how it is closed or accepted | yes | 'Remaining gap (kept levers only): EUR26.3m' and recommendation to 'Bring the board a revenue range (EUR149m-164m) ... and ask for either time ... or a revised target.' |
| Answer line names specific levers with amounts/investment and a confidence level with one reason | yes | 'installed-base service-contract conversion (+EUR5.6m revenue / +EUR1.3m EBIT) and a partial lab-instrument price reset (+EUR2.4m revenue / +EUR2.2m EBIT) ... Confidence: Medium — ... Confidence is capped because the two largest value pools ... are identified but not yet sized.' |
| Assumptions table and open-questions table in the skill's format | yes | Both '## Assumptions' and '## Open questions' tables present with #, basis, and 'would change the answer' columns. |
| Must not close the gap by stretching assumptions | yes | 'Even crediting software at the head of strategy's full EUR15m claim ... still EUR11.3m short of EUR175m' — gap left open rather than closed via stretched assumptions. |
| Must not invent market data, competitor prices or benchmark ramp-up rates | NO | Market vs share table asserts Service market growth of '+4%/yr' used to compute a EUR24.3m hold-share figure and EUR4.3m share-loss, but no source/basis for this service market-growth rate appears anywhere (unlike lab's 3%/yr and sensors' 6%/yr, which trace to the pack's cumulative market figures),  |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

Answer page written to `case-growth-kirkby.md`. Headline for the CEO:

**The head of strategy's software pitch doesn't hold up, and isn't the real lever anyway.** Even crediting his EUR15m claim at full face value, the plan reaches only ~EUR164m by 2030 — still EUR11m short of the EUR175m target. But simply **stopping the share loss** Kirkby already has in all three segments (each is growing slower than its own served market) would get to ~EUR171m — 97% of the way there — with zero new capital. 87% of the EUR34.3m gap is a core share-loss problem, not a missing adjacency.

Recommendation: fund the two evidenced core levers now (installed-base service-contract conversion, +EUR5.6m; partial lab-instrument price reset, +EUR2.4m — ~EUR8m revenue for under EUR1m capital), cap the software bet at a ~EUR2m pilot instead of the full EUR9m, and open an urgent workstream on why Lab instruments (EUR17.5m at stake) and Process sensors (EUR8.1m) are losing share — that's where the real gap-closer is. Margin floor (10%) is safe in every scenario modeled (13–14%).

Full numbers, lever-by-lever sizing, assumptions, open questions and trap checks are in the file.


## Files in work dir after run

- case-growth-kirkby.md
- cg-01-input.md

## File written by the run: case-growth-kirkby.md

# Growth strategy: Kirkby Analytical — which levers close the gap from EUR140m to EUR175m revenue by 2030, within EUR15m capital and a 10% group EBIT margin floor?

**This contradicts the head of strategy's premise.** Even crediting his process-analytics-software claim at full face value (EUR15m revenue, no discount for the fact that it rests on no customer interviews, pilots or comparable launches), the plan reaches only ~EUR164m by 2030 — EUR11m short of the EUR175m target. Meanwhile, simply **holding share** in the three existing segments (growing each at its own served-market rate instead of its 2023–25 trend) would reach ~EUR171m — 97% of the way to target — with zero new capital. 87% of the EUR34.3m gap is a share-loss problem in the core, not a market-size or missing-adjacency problem. Software is not the answer; stopping the bleeding in Lab instruments and Process sensors is.

**Answer:** Fund the two evidenced core levers now — installed-base service-contract conversion (+EUR5.6m revenue / +EUR1.3m EBIT, base case) and a partial lab-instrument price reset (+EUR2.4m revenue / +EUR2.2m EBIT) — for ~EUR8m of revenue at under EUR1m of new capital. Do not commit the full EUR9m to process analytics software; fund a ~EUR2m pilot with 2–3 lighthouse customers and release further capital only against pilot evidence. In parallel, open a new workstream on why Lab instruments and Process sensors are losing share against their own growing markets — at stake there is ~EUR25.6m of revenue, more than every other lever combined. Bring the board a realistic 2030 range of EUR149m–164m under today's evidence, not EUR175m, and ask either for time to size the share-loss fix or for a revised target.

**Confidence:** Medium — the core arithmetic (momentum case, share decomposition, installed-base and price levers) is built on Kirkby's own finance, CRM and pricing data and is solid. Confidence is capped because the two largest value pools (Lab instruments and Process sensors share loss, ~EUR25.6m) are identified but not yet sized, and the software claim has no evidence base at all. Would rise with win-loss interviews on the two declining/underperforming segments and a software pilot result.

**Specialists and review:** Pricing/commercial analytics to test lab-instrument price elasticity before a full rollout; sales/competitive-intelligence or win-loss research on why Lab instruments and Process sensors are losing share against growing markets; finance/FP&A to validate the software investment's cost structure and margin phasing before releasing capital beyond the pilot. No legal, tax or regulatory specialist is triggered by this plan (no acquisitions, no new country entry); revisit if the board later adds either.

## The gap

| | 2025 | 2030 |
|---|---|---|
| Revenue, momentum case (each segment continues its 2023–25 CAGR) | EUR140m | EUR140.7m |
| Revenue, if each segment instead just held share (grew at its own served-market rate) | — | EUR170.6m |
| Revenue, target | — | EUR175m |
| **Gap (momentum vs. target)** | | **EUR34.3m** |
| — of which, share loss (gap between hold-share and momentum) | | EUR29.9m (87%) |
| — of which, market-growth shortfall (gap between target and hold-share) | | EUR4.4m (13%) |
| Constraints | capital EUR15m, group EBIT margin floor 10%, no acquisitions this cycle |

**Momentum case by segment** (continuing each segment's 2023–25 CAGR to 2030):
- Lab instruments: 2023–25 CAGR = **−1.23%/yr** (82→80). 2030 = 80 × 0.9877⁵ ≈ **EUR75.2m**.
- Process sensors: 2023–25 CAGR = **+2.60%/yr** (38→40). 2030 = 40 × 1.026⁵ ≈ **EUR45.5m**.
- Service: 2023–25 CAGR = **0%** (20→20). 2030 = **EUR20.0m**.
- Total momentum: 75.2 + 45.5 + 20.0 ≈ **EUR140.7m** — confirms the business has genuinely stalled, not grown, under current trajectory.

**Market vs. share split** (comparing each segment's own CAGR to its served-market growth rate):

| Segment | Kirkby CAGR 2023–25 | Market growth 2023–25/to 2030 | Verdict | 2030 if Kirkby held share | 2030 momentum | Share-loss gap |
|---|---|---|---|---|---|---|
| Lab instruments | −1.23%/yr | +3%/yr | **Losing share** | 80×1.03⁵ ≈ EUR92.7m | EUR75.2m | **EUR17.5m** |
| Process sensors | +2.60%/yr | +6%/yr | **Losing share** | 40×1.06⁵ ≈ EUR53.5m | EUR45.5m | **EUR8.1m** |
| Service | 0%/yr | +4%/yr | **Losing share** | 20×1.04⁵ ≈ EUR24.3m | EUR20.0m | **EUR4.3m** |
| **Total** | | | | **EUR170.6m** | **EUR140.7m** | **EUR29.9m** |

**Hypothesis confirmed:** the served markets are growing in all three segments; Kirkby is losing share in all three. This is a core-competitiveness problem, not a stalling-market problem — the opposite of what an adjacency bet (software) addresses.

## Levers

| Lever | Revenue base case (2030) | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Installed-base service-contract conversion | +EUR5.6m | EUR3.7m–7.4m | +EUR1.3m (at 24% service margin; range +0.9 to +1.8m) | ~EUR1m (sales/CRM capacity) | Ramps 2027–29, full run-rate ~2030 | Medium (service manager's qualitative read; no documented churn/win-back data) | **Keep** |
| Lab-instrument price reset (partial close of the 7% gap) | +EUR2.4m | EUR1.6m–5.6m | +EUR2.0–2.2m (near-full drop-through, no added COGS) | ~EUR0m | Immediate on repricing (2027) | Weak–medium (price gap is documented; no elasticity test, and this segment is already losing share for an unexplained reason, which raises execution risk) | **Keep, as a one-region pilot first** |
| Process analytics software (head of strategy's claim: EUR15m / EUR9m) | +EUR3–8m (outside-view discount from the EUR15m claim) | EUR3m–15m (wide; upper end is the unverified claim) | Not sizable responsibly; assume ~0% margin (breakeven) during 2030 ramp pending real cost data | EUR9m claimed; recommend ~EUR1.5–2m pilot, hold the rest | Multi-year ramp from a zero customer base; minimal revenue likely before 2028–29 | **Weak** — no customer interviews, pilots, or comparable launches cited | **Option — pilot only, do not release full capital** |
| Lab instruments share-loss fix (not yet scoped) | Not sized | Up to EUR17.5m at stake | Unknown | Unknown | Unknown | No data in this pack | **Open — highest-priority next analysis** |
| Process sensors share-loss fix (not yet scoped) | Not sized | Up to EUR8.1m at stake | Unknown | Unknown | Unknown | No data in this pack | **Open — second priority** |

**Sum of kept levers (base case):** EUR140.7m momentum + EUR5.6m (service) + EUR2.4m (price) = **EUR148.7m**.
**Group EBIT at kept levers:** momentum EBIT ≈ EUR17.5m (segment margins held) + EUR1.3m + EUR2.2m ≈ **EUR21.0m → 14.1% margin**, comfortably above the 10% floor.
**Even crediting software at the head of strategy's full EUR15m claim:** EUR148.7m + EUR15m = **EUR163.7m**, still **EUR11.3m short of EUR175m**, and margin still ≈12.8% (above floor) even at 0% software margin.
**Remaining gap (kept levers only): EUR26.3m.** This lines up almost exactly with the unscoped Lab instruments (EUR17.5m) and Process sensors (EUR8.1m) share-loss pools above (EUR25.6m combined) — that is where the rest of the plan has to come from, not from software.

## Killed options and why

None killed outright on the data available. Software is **optioned, not killed** — nothing in the pack shows the addressable market is too small or held by entrenched players; the claim is simply unproven (no interviews, pilots or comparables), so it should be tested with a small pilot rather than funded at EUR9m or dropped entirely.

## Risks and what would change the answer

1. If the Lab instruments and Process sensors share-loss drivers turn out to be structural (product age, distribution, brand) rather than fixable at reasonable cost, up to EUR25.6m of the gap stays open and the board should reset the 2030 target rather than wait for a plan that won't materialize.
2. If the lab-instrument price increase triggers volume loss beyond the range assumed (plausible, since the segment is already losing share for an unexplained reason), the price lever could turn margin-positive but revenue-negative — test in one region before full rollout.
3. If the software pilot shows real traction, the EUR7m held back can be released against evidence; if it does not, the EUR9m is better redeployed into the core share-loss fix once scoped.
4. Group EBIT margin is not the binding constraint in any scenario modeled here (13–14% in all cases) — the binding constraint is revenue, so capital and management attention should follow revenue risk, not margin risk.

## Next steps

| What | Who | By when |
|---|---|---|
| Launch win-loss/customer research on why Lab instruments is losing share against a growing market (biggest value pool, ~EUR17.5m) | Sales & product leadership | 2027-01-15 |
| Scope a sales push on Process sensors (best margin, strongest market, still losing share) | Process sensors BU lead | 2027-01-15 |
| Set a service-contract conversion target and sales plan for the uncontracted installed base | Service manager / sales ops | Start immediately; ramp 2027–29 |
| Run a one-region lab-instrument price pilot and measure volume response before a full reset | Pricing/commercial | 2027-Q1 |
| Fund a ~EUR1.5–2m software pilot with 2–3 lighthouse customers; require pilot revenue/LOI evidence before releasing further capital | Head of strategy + finance | Pilot readout by 2027-06-30 |
| Bring the board a revenue range (EUR149m–164m) against the EUR175m target and ask for either time to size the share-loss fix or a revised target | CEO + board | 2027-03 board meeting |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Service-contract capture rate on the uncontracted installed base | 30% (range 20–40%) | Judgement call; no Kirkby-specific conversion target given in the pack | Actual achievable capture rate (from a sales pilot) is materially above or below this |
| 2 | Net revenue effect of the lab-instrument price reset | +3% net of the 7% list gap (range 2–7%) | List-price gap is documented; no elasticity or volume-response data provided | An elasticity test shows materially more or less volume give-back |
| 3 | Process-analytics-software 2030 revenue, discounted from the head of strategy's EUR15m claim | EUR3–8m | Outside-view discount applied because the claim has no customer interviews, pilots, or comparable launches behind it | A pilot produces signed LOIs or paid revenue that validates a higher trajectory |
| 4 | Software EBIT margin during 2030 ramp | ~0% (breakeven) | No cost/margin structure for the software line was provided | Finance supplies a real cost structure showing materially positive or negative margin |
| 5 | Incremental EBIT margin on converted service contracts | 24% (same as current Service segment average) | No marginal-cost data; infrastructure is largely fixed, so true marginal margin could be higher | A marginal-cost analysis shows a different incremental margin |
| 6 | EBIT drop-through on the price increase | ~90% | Pure price change, no added COGS assumed | Competitors react with their own price moves or added discounting erodes net price |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why is Kirkby losing ~EUR17.5m of potential Lab-instrument revenue against a market growing 3%/yr? | Single largest value pool in the whole case, bigger than every sized lever combined | Sales/product leadership, win-loss interviews | Could supply the lever that actually closes most of the remaining EUR26.3m gap |
| Why is Process sensors (best margin, 6%/yr market) still losing share, at ~EUR8.1m of potential revenue? | Second-largest unaddressed value pool | Sales leadership, competitive intelligence | Could close most of the rest of the remaining gap |
| Why do customers currently use independent service shops instead of Kirkby contracts? | Determines whether 30% capture is conservative or optimistic | Service manager, customer interviews | Shifts the service lever within its EUR3.7–7.4m range |
| What volume response would a lab-instrument price increase trigger, given the segment is already losing share for an unknown reason? | Price increase could accelerate the share loss it's meant to help offset | Pricing/commercial team, customer interviews | Could turn the price lever negative on revenue even if margin-positive |
| Is there any comparable industrial-software launch (Kirkby's or a peer's) to benchmark the ramp curve, and can a pilot be run before committing further capital? | The EUR15m claim has zero evidence base | Head of strategy, R&D/product, finance | Decides whether to scale software funding, hold at pilot level, or shelve it |
| Will the board accept a lower 2030 milestone (~EUR149–164m) or a longer horizon if the honestly-sized plan doesn't reach EUR175m? | Determines whether this is a "close the gap" plan or an "manage expectations + find new levers" plan | CEO / board | Sets the frame for the March 2027 meeting |

## Trap checks

- [x] **Adding up hope.** Each lever is sized on its base case with a stated range; the software claim is explicitly discounted rather than accepted; the remaining EUR26.3m gap (kept levers only) — or EUR11.3m even crediting software at face value — is stated openly, not closed by stretching an assumption.
- [x] **Skipping the core.** Momentum, market-vs-share decomposition, and installed-base/price levers were sized before the software adjacency was assessed at all — and that sequencing is exactly what surfaced the EUR25.6m share-loss opportunity the head of strategy's framing skipped.
- [ ] **Inside view on new moves.** Open: no comparable industrial-software launch was available in the data pack to benchmark the ramp curve. Fix applied: the range was widened (EUR3–8m vs. the claimed EUR15m) and the missing comparison is flagged as an open question before further capital is released.
- [x] **Market growth confused with share growth.** Explicitly separated: 87% of the EUR34.3m gap (EUR29.9m) is share loss across all three segments; only 13% (EUR4.4m) is a true market-growth shortfall even at full share retention.
- [x] **Ignoring the constraints.** No lever uses an acquisition; total new capital committed now (service ~EUR1m + price ~EUR0m + software pilot ~EUR1.5–2m) is ~EUR2.5–3m, well inside the EUR15m cap, leaving headroom once the Lab-instrument and Process-sensor fixes are scoped.
- [x] **Too many initiatives.** Two evidenced levers (service conversion, price reset) carry the plan; software is one bounded pilot/option, not a third large committed bet.
- [x] **Revenue without margin.** Every lever shows its EBIT effect next to revenue; group EBIT margin on kept levers is ≈14.1%, and even in the most generous software scenario modeled it stays ≈12.8% — both above the 10% floor.

