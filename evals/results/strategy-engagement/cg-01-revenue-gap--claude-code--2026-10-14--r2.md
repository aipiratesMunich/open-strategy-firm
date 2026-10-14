# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap 140m→175m by 2030, EUR 15m capital, no acquisitions, EBIT margin ≥10%, board March 2027) | yes | Title: 'the EUR 35m gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, for the March 2027 board meeting' plus constraints row 'ruled out: acquisitions this cycle' |
| Computes momentum case ~EUR 140-141m and gap ~EUR 34m using CFO convention | yes | 'Lab instruments 80 → 75.2 ... Process sensors 40 → 45.5 ... Service 20 → 20.0 ... Sum = 140.7m' and 'Gap: EUR 34.3m' — matches reference exactly |
| Separates market growth from share change and states Kirkby lost share in lab instruments and process sensors | yes | 'Lab instruments / −1.2%/yr / +3%/yr / Losing share...' and 'Process sensors / +2.6%/yr / +6%/yr / Losing share...' |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with base case/range/evidence grade | yes | Lever table gives price (+2.3m, 1.5-3.0m, medium), service (+3.7m, 2.8-5.6m, medium), and lab/sensor share-loss (up to 17.5m/8.1m, 0-X range, weak/none), all listed before the software row |
| Installed-base lever about EUR 4.3m at 50% coverage (or consistent alternative) | NO | Service lever base case is '+EUR 3.7m' using '15–30% conversion of 14,300 uncontracted instruments', with no coverage-percentage framing or explicit ~4.3m figure anywhere; assumptions table admits the conversion rate 'No historical conversion/win-back rate given in pack', diverging from the referenc |
| Treats EUR 15m software figure as unsupported, widens range/kills it, names comparison that would settle it | yes | 'no credible range from this pack' / 'do not fund at full scale; commission a paid pilot' and 'comparable analytics launches typically reach a small fraction of ambition in year one — no comparable is cited here, so this must be tested, not assumed' |
| Shows profit next to revenue for every kept lever and checks 10% EBIT floor | yes | Price lever 'EBIT effect +EUR 2.0m', service lever '+EUR 0.9m', and 'adding the two levers brings EBIT to ≈ EUR 20.4m on ≈ EUR 146.6m revenue (≈13.9% margin...above the 10% floor)' |
| Shows remaining gap openly after base-case levers and says how it is closed or accepted | yes | 'Remaining gap against the EUR 34.3m target: EUR 28.3m. This is not closed in this pack — it is closed only if the win-loss research...' |
| Answer line names specific levers with amounts/investment and a confidence level with one reason | yes | 'fund the two evidenced levers now (~EUR 6m, low capital)...' and 'Confidence: Low on hitting EUR 175m, because the two largest value pools...are sized but not root-caused' |
| Assumptions table and open-questions table in the skill's format | yes | Both tables present with columns #/Assumption/Value used/Basis/Would change the answer if, and Question/Why it matters/Who can answer/Effect on the answer |
| Must not close the gap by stretching assumptions (e.g. full share recovery plus EUR15m software at base case, no range) | yes | Software explicitly excluded from base case ('should not be counted into the plan as given'); share recovery kept as 'option, pending research' not assumed in base case |
| Must not invent market data, competitor prices, or benchmark ramp-up rates | yes | Ramp-up claim is explicitly hedged: 'no comparable is cited here, so this must be tested, not assumed'; growth/price figures are sourced from pack-consistent CAGRs matching reference values |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

Answer page written to `case-growth-kirkby-analytical.md`. Headline finding: the head of strategy's software pitch is the wrong frame — Kirkby is losing share in all three segments despite growing markets, the momentum case lands at EUR 140.7m (a EUR 34.3m gap to the EUR 175m target), and the two levers the pack actually supports (a partial lab price reset + service-contract conversion) only close ~EUR 6m of that gap. The two biggest value pools — EUR 17.5m in lab instruments and EUR 8.1m in process sensors — are real but undiagnosed (no win-loss data in the pack), and the software bet (EUR 15m claimed revenue, EUR 9m of the EUR 15m capital budget) has no interviews, pilots, or comparables behind it, so it isn't counted into the base case. Recommendation: fund the two small evidenced levers now, commission win-loss research and a software pilot before committing the EUR 9m, and tell the board plainly that EUR 175m isn't yet closable with current evidence.


## Files in work dir after run

- case-growth-kirkby-analytical.md
- cg-01-input.md

## File written by the run: case-growth-kirkby-analytical.md

# Growth strategy: Kirkby Analytical, which levers close the EUR 35m gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, for the March 2027 board meeting?

**Answer:** This contradicts the head of strategy's framing. The real problem is not a flat market that needs a new software revenue stream — Kirkby is **losing share in all three segments** despite growing served markets (lab +3%/yr, sensors +6%/yr, service +4%/yr). On current trend (momentum case), 2030 revenue is only **EUR 140.7m**, a gap of **EUR 34.3m**. With the two levers the pack actually evidences — a partial lab-instrument price reset and converting uncontracted service accounts — the base case adds only **EUR 6.0m** (range EUR 4.3m–8.6m), closing about **17% of the gap**. The single largest value pool in the case (EUR 17.5m, if Kirkby simply stopped losing share in lab instruments) is **undiagnosed**: the pack gives no win-loss or competitive data beyond the 7% price gap. The head of strategy's software bet (EUR 15m revenue, EUR 9m investment — 60% of the capital budget) has **no customer interviews, pilot or comparable launch** behind it and should not be counted into the plan as given. **Recommendation for the March 2027 meeting:** fund the two evidenced levers now (~EUR 6m, low capital), commission a lab/sensor win-loss study and a paid software pilot before committing the EUR 9m, and tell the board plainly that EUR 175m is not yet closable with evidenced levers — the honest range today is **EUR 147m–155m**, with EUR 175m reachable only if the win-loss research confirms the full share-loss reversal is fixable (which would add up to another EUR 25.6m).

**Confidence:** Low on hitting EUR 175m, because the two largest value pools (lab and sensor share loss, EUR 25.6m combined) are sized but not root-caused, and the software case has no supporting evidence. High on the diagnosis itself (share loss, not market stagnation) — the market-growth and own-growth figures are both from the same pack and point the same way in all three segments.
**Specialists and review:** Commercial/pricing team to test price elasticity before a lab list-price move; service operations to pilot the contract-conversion rate before it is budgeted; finance to confirm whether the EUR 15m covers opex (service headcount, sales commissions) or capex only. No legal, tax or regulatory question is raised by the facts given.

## The gap

| | 2025 | 2030 |
|---|---|---|
| Revenue, momentum case (segment CAGR 2023–25 continued) | EUR 140m | **EUR 140.7m** |
| Revenue, target | | EUR 175m |
| **Gap** | | **EUR 34.3m** |
| Constraints | capital EUR 15m, margin floor 10% group EBIT, ruled out: acquisitions this cycle |

Momentum by segment (CAGR 2023–25 applied to 2030, EUR m): Lab instruments 80 → 75.2 (CAGR −1.2%/yr); Process sensors 40 → 45.5 (CAGR +2.6%/yr); Service 20 → 20.0 (CAGR 0%). Sum = 140.7m.

## Market vs share — the core finding

| Segment | Kirkby CAGR 2023–25 | Market growth 2023–25 (continuing to 2030) | Verdict |
|---|---|---|---|
| Lab instruments | −1.2%/yr | +3%/yr | **Losing share**, ~4.2pp/yr gap |
| Process sensors | +2.6%/yr | +6%/yr | **Losing share**, ~3.4pp/yr gap, despite being the fastest-growing market |
| Service | 0%/yr | +4%/yr | **Losing share**, ~4pp/yr gap |

Hypothesis "revenue is flat because the market is flat" is **killed**: every served market is growing. Hypothesis "the core is losing share, not stalling with the market" is **confirmed** in all three segments.

If Kirkby had simply held share (grown at market rate) from 2025 to 2030 instead of its own trend:

| Segment | Momentum 2030 | Hold-share 2030 | Value of stopping the share loss |
|---|---|---|---|
| Lab instruments | 75.2 | 92.7 | **17.5** |
| Process sensors | 45.5 | 53.5 | **8.1** |
| Service | 20.0 | 24.3 | **4.3** |
| **Total** | **140.7** | **170.6** | **29.9** |

Even fully arresting share loss across the whole portfolio (EUR 170.6m) does not reach EUR 175m — it leaves a residual EUR 4.4m. So the plan needs both a share-loss fix and some net-new growth; it cannot rest on defense alone.

## Levers

| Lever | Revenue base case 2030 | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Lab instrument price reset (close part of the 7% list-price gap, no volume reason recorded) | +EUR 2.3m | 1.5–3.0m | +EUR 2.0m (~90% drop-through) | not quantified in pack; expected low/no capex | immediate; full run-rate <1yr | medium (hard price-gap data; no elasticity data) | keep — pilot in one region/channel first |
| Service contract attach (convert uncontracted installed base) | +EUR 3.7m | 2.8–5.6m (15–30% conversion of 14,300 uncontracted instruments at EUR 1,300/yr) | +EUR 0.9m (at 24% service margin) | not quantified; expected modest opex (service/sales capacity) | ramps over 2–3 yrs | medium (hard CRM data on base and price; conversion rate assumed) | keep — calibrate with a pilot campaign on a sample of accounts |
| Lab instruments: close the rest of the 17.5m share-loss gap | up to EUR 17.5m | 0–17.5m | not sizeable yet | not sizeable yet | unknown | **weak/none** — no win-loss or competitive data | option, pending research — largest single value pool in the case |
| Process sensors: close the 8.1m share-loss gap | up to EUR 8.1m | 0–8.1m | not sizeable yet | not sizeable yet | unknown | **weak/none** | option, pending research |
| Process analytics software (head of strategy) | claimed EUR 15m | **no credible range from this pack** | unknown — no cost/margin data beyond EUR 9m investment | EUR 9m (60% of the EUR 15m budget) | unknown — no comparable cited | **weak** — explicitly "no customer interviews, pilots or comparable launches cited" | do not fund at full scale; commission a paid pilot with 2–3 target customers first |

**Sum of kept levers (hard-evidenced base case): EUR 6.0m** (range EUR 4.3m–8.6m). **Remaining gap against the EUR 34.3m target: EUR 28.3m.** This is not closed in this pack — it is closed only if the win-loss research on lab instruments and process sensors confirms some or all of the EUR 25.6m of undiagnosed share-loss value, or if a validated software pilot replaces the current unsupported EUR 15m claim.

Group EBIT check on the two kept levers only: momentum-case EBIT ≈ EUR 17.5m on EUR 140.7m (12.4% margin, holding 2025 segment margins constant); adding the two levers brings EBIT to ≈ EUR 20.4m on ≈ EUR 146.6m revenue (**≈13.9% margin** — comfortably above the 10% floor). Margin is not the binding constraint for the moves evidenced here; it would become one only if the software bet is funded and proves loss-making during ramp-up, which is unknown from this pack.

## Killed / downgraded and why

- **"The answer is process analytics software" (head of strategy):** downgraded from "the answer" to "an unvalidated option." No customer interviews, pilots, or comparable launches cited — a textbook inside-view forecast. It also asks for 60% of the total capital budget on that basis alone.
- **"Revenue is flat because the market is flat":** killed. All three served markets grew 3–6%/yr over 2023–25; Kirkby's own segments grew −1.2% to +2.6%. The flat EUR 140m total is share loss, not a stalled market.
- **"Two or three large levers can carry this plan" (trap check):** fails as things stand. The only two levers with hard evidence (price, service attach) are small (EUR 6.0m combined); the two large pools (lab and sensor share loss, EUR 25.6m) are sized but undiagnosed, and the one large claimed lever (software) is unsupported. The honest state of the plan today is two small confirmed levers plus three large open questions — not a finished portfolio.

## Risks and what would change the answer

1. If the lab/sensor win-loss research finds the share loss is **not fixable** within the plan horizon (e.g., structural competitor advantage, channel lock-in), the achievable 2030 revenue stays near **EUR 147–150m**, and the board should be told now that EUR 175m needs either a longer horizon, more capital (e.g., to fund an acquisition, currently ruled out), or a lower target.
2. If a software pilot validates even a modest ramp (e.g., comparable analytics launches typically reach a small fraction of ambition in year one — no comparable is cited here, so this must be tested, not assumed), it could add a validated third lever; until then it should not be budgeted at EUR 9m.
3. If the lab price reset causes material volume loss (untested), the lever could be smaller than base case or even negative — recommend a limited pilot before a blanket list-price move.

## Next steps

| What | Who | By when |
|---|---|---|
| Win-loss / competitive research on lab instruments (largest value pool, EUR 17.5m) | Sales/competitive intelligence | Before March 2027 board meeting |
| Win-loss research on process sensors (EUR 8.1m, fastest-growing market) | Sales/competitive intelligence | Before March 2027 board meeting |
| Pilot price increase (2–4%) in one region/channel to measure volume response | Commercial/pricing team | Q1 2027 |
| Pilot service-contract conversion campaign on a sample of uncontracted accounts to calibrate real take-up | Service operations | Q1 2027 |
| Paid pilot with 2–3 target customers for process analytics software before committing EUR 9m | Head of strategy | Before any capital is committed |
| Clarify whether the EUR 15m budget is capex-only or covers opex (service headcount, sales commissions) | CFO | Before March 2027 board meeting |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Lab instrument price reset realized net of any volume response | +2% to +4% net price | No elasticity data in pack; illustrative range only | Elasticity testing shows material volume loss, or the price gap is explained by an unrecorded factor (spec, warranty, service bundling) |
| 2 | Service contract conversion rate on the 14,300 uncontracted instruments | 15%–30% over the plan period | No historical conversion/win-back rate given in pack | A pilot campaign shows a materially different rate |
| 3 | EBIT drop-through: price lever ~90%; service lever at the segment's stated 24% margin | as above | No incremental cost data provided | Contract conversion requires new service capacity (lower margin), or price move needs channel-margin adjustment |
| 4 | Investment needed for the price and service levers | low / non-capital, not separately quantified | Not provided in pack | Finance identifies a material cost that competes with the EUR 15m budget |
| 5 | Segment EBIT margins held constant under the momentum case | 9% / 13% / 24% (2025 levels) | Only 2025 margins given; no trend provided | Margins are known to be moving independently of revenue mix |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why is Kirkby losing share in lab instruments beyond the 7% price gap? | Largest single value pool in the case (up to EUR 17.5m) | Sales / competitive intelligence, win-loss interviews | Could be the single largest lever in the whole plan |
| Why is Kirkby losing share in process sensors despite the fastest-growing market (6%/yr)? | Second-largest unexploited pool (up to EUR 8.1m) | Sales / competitive intelligence | Determines whether the sensors segment is a growth engine or a continuing drag |
| What conversion rate can the service organization actually achieve on uncontracted accounts, and at what cost to serve? | Determines whether the service lever is EUR 2.8m, 5.6m, or more | Service manager / sales ops, pilot campaign | Recalibrates the only other evidenced lever |
| Will a lab price increase hold volume, and does the 7% gap reflect unrecorded value the market already perceives? | Determines whether the price lever is EUR 1.5m, 3.0m, or negative | Pricing/commercial team, customer research | Could reverse the lever from a gain to a loss |
| Can the software thesis be validated with a paid pilot before EUR 9m (60% of capital) is committed? | Determines whether this lever should be funded at all, and at what scale | Head of strategy, 2–3 target customers | Removes or replaces the only "large" lever currently on the table |
| Does the EUR 15m capital limit cover opex (service headcount, sales commissions) or capex only? | Changes how much is actually free to fund the price/service levers alongside any software pilot | CFO | Changes what is affordable without breaching the capital constraint |
| Is EUR 175m by 2030 flexible in amount or timing if fully-evidenced organic levers land around EUR 147m–171m? | The honest base case, even in the best case where all share-loss is reversed, lands at EUR 170.6m, short of target | Board / CEO | Determines whether March 2027 is "here is the plan" or "here is the plan plus a renegotiation ask" |

