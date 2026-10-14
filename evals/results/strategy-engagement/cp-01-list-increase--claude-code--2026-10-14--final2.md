# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs price waterfall first, states list increase only reaches pocket price if discounts don't widen, names uncapped 22% small-direct-accounts discount as the leak | yes | "~19 points of every 100 of list already leak before pocket price... small direct accounts, 22% average discount, any rep can approve with no cap... a list increase there will not reach pocket price unless the approval rule changes alongside it." |
| Break-even volume loss ~11% computed with contribution margin, formula/arithmetic shown | yes | "Break-even volume loss = 1 − m / (m + p) = 1 − 0.40 / 0.45 = 11.1%." |
| Uses 2023 change (-2% for +3%) as revealed behaviour, compares expected loss (~3-4%) with break-even | yes | "Implied elasticity ≈ −0.67... Applied to a 5% increase: expected volume loss ≈ 3.3% — well below the 11.1% break-even." |
| EBIT effect as a range across volume reactions with arithmetic shown | yes | Table shows EBIT from +1.20m (0% loss) down to −0.42m (15% loss), each with arithmetic (e.g. "gain 5%×24.0m×0.967=1.16m; lost 3.3%×40%×24.0m=0.32m; 1.16−0.32=0.84m") |
| Differentiates by segment (OEM January renewal, distributor 60-day notice, small-account discount cap/approval) | yes | Implementation table: OEM renewal "January 2027 renewal", Distributors "Give 60 days' contractual notice", Small direct accounts "Introduce an approval cap... above the current 22%" |
| Anchors recommendation on customer value and like-for-like competitor gap, not cost | yes | "the gap sits in Ravensworth's favour on service, so there is no quality/service reason for list prices to be below the market" — no cost-based justification appears anywhere |
| Names competitor reaction as a scenario (follow/hold/undercut) and what would trigger a different answer | yes | Assumption 4: competitor prices "stay roughly flat"; What-if 4: "If either competitor raises or cuts list prices before March 2027, the 7–9% benchmark gap... changes and the position case should be rechecked" |
| Answer line states decision type, amount, segments, date, EBIT range | yes | "raise list prices 5% across the standard seal range from 1 March 2027, provided the increase is paired with two execution fixes... Base-case EBIT effect: +EUR 0.8m to +1.2m" |
| Names source of 2023 comparison (industry association data), treats it as one data point, states dependency | yes | "against flat market volume (industry-association shipment data)"; "Caveat: one historical observation, at a smaller increase... Treat 3.3% as a central estimate inside a wider range, not a precise forecast" |
| Must not compute break-even with gross margin or without showing formula | yes | Used "m = contribution margin = 40%" with formula shown, not gross margin |
| Must not suggest sharing price intentions with competitors or using competitor contract data | yes | "benchmark uses only public price lists and customer audit data, no competitor contact" |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

Answer page written to `case-pricing-ravensworth.md`.

**Bottom line:** yes to the 5% increase from 1 March 2027 — base case adds **+EUR 0.8–1.2m EBIT**, and the break-even volume loss (11.1%) is more than 3x the loss seen after the 2023 increase. But two conditions matter: cap the uncapped small-accounts discount (22%, no approval limit) so the increase actually reaches pocket price, and clarify whether January-renewing OEM contracts (55% of volume) can carry the increase or push it to 2028.

Flagged as open with the board/sales director: their real volume-loss tolerance (vs. the technical 11.1% break-even), OEM contract lock-in terms, and whether competitors move price before March 2027 — all listed in the Open Questions table.


## Files in work dir after run

- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth.md

# Pricing: Ravensworth Industrial Seals — can list prices on the standard seal range rise 5% from 1 March 2027?

**Answer:** Yes — raise list prices 5% across the standard seal range from 1 March 2027, provided the increase is paired with two execution fixes: a discount cap in the small-direct-accounts segment, and carrying the increase into the January 2027 OEM contract renewals rather than relying on a mid-contract change. Base-case EBIT effect: **+EUR 0.8m to +1.2m** in year one (0–3.3% volume loss); the move only destroys value above an ~11.1% volume loss, more than three times the loss seen after the last increase.

**Confidence:** Medium — the competitor benchmark (7–9% gap) and the 2023 revealed-elasticity evidence both point the same way, but the elasticity rests on a single historical data point at a smaller increase (3%, not 5%), there is no direct customer-value data, and 55% of volume (OEM) sits on contracts whose renewal timing could delay the effect.

**Specialists and review:** No competition-law exposure (benchmark uses only public price lists and customer audit data, no competitor contact). Key account director and sales director must sign off on the segment-specific execution rules below; finance should check the break-even and EBIT arithmetic in the tables below (one-minute check).

## Price position
| Offer | Our price | Both main competitors | Value difference | Gap explained? |
|---|---|---|---|---|
| Standard seal range, 40 comparable part numbers, same material/size/pressure rating (Sept 2026 public price lists) | Index 100 | Index ~108–110 (7–9% above Ravensworth) | Lead times comparable; Ravensworth has the better on-time delivery record (96% vs ~90% customer-stated average, 2025 audits) | **No** — the gap sits in Ravensworth's favour on service, so there is no quality/service reason for list prices to be below the market |

*Hypothesis "list prices sit below comparable competitors without a spec or service reason": **confirmed**.*

## Value to customer
| Segment | Next-best alternative | Customer value of our offer | Current price | Share of value captured |
|---|---|---|---|---|
| OEM / distributors / small accounts | Comparable competitor seals, same spec | Not quantified in the pack — only an indirect signal (better delivery reliability) | List net of segment discount | Not computable from the data given |

*Data gap, not a kill — the benchmark and revealed-behaviour evidence below carry the case instead. See open questions.*

## Price waterfall (average, standard seal range)
| Step | EUR per 100 of list | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | 12% |
| Invoice price | 88 | 88% |
| Annual volume rebate | -4 | 4% |
| Free freight | -3 | 3% |
| **Pocket price** | **81** | **81%** |

By segment (on-invoice discount only):

| Segment | Share of volume | On-invoice discount | Approver |
|---|---|---|---|
| OEM key accounts | 55% | 8% | Key account director |
| Distributors | 30% | 12% | Sales director |
| Small direct accounts | 15% | 22% | Any sales rep, **no cap** |

*So-what: ~19 points of every 100 of list already leak before pocket price. The leakage is worst and least controlled exactly where it is cheapest to give away — small direct accounts, 22% average discount, any rep can approve with no cap. Hypothesis "leakage is small and controlled": **killed** for this segment; a list increase there will not reach pocket price unless the approval rule changes alongside it.*

## Break-even volume loss
m = contribution margin = 40% of pocket revenue; p = price increase = 5%.

Break-even volume loss = 1 − m / (m + p) = 1 − 0.40 / 0.45 = **11.1%**.

Ravensworth can lose up to ~11% of volume on the standard range before the 5% increase stops adding EBIT.

## Volume reaction (revealed evidence)
2023: +3% list price → Ravensworth volume −2% over the following 12 months, against flat market volume (industry-association shipment data) — i.e., a net 2-point share/volume loss attributable to the price move.

Implied elasticity ≈ −2% / +3% ≈ **−0.67**.

Applied to a 5% increase: expected volume loss ≈ 5% × 0.67 ≈ **3.3%** — well below the 11.1% break-even.

*Caveat: one historical observation, at a smaller increase (3% vs 5%); elasticity may not stay linear at a larger move. Treat 3.3% as a central estimate inside a wider range (say 2–6%), not a precise forecast.*

*Hypothesis "expected volume loss stays well below break-even loss": **confirmed**, with weak-to-medium evidence strength (single data point).*

## Profit effect
Base pocket revenue EUR 24.0m; contribution margin 40% (contribution EUR 9.6m). Variable cost is assumed unchanged by the price move (cost doesn't move with price); it scales only with volume.

EBIT effect ≈ [price gain on retained volume] − [contribution lost on volume that leaves]
= [p × Revenue × (1 − loss)] − [loss × m × Revenue]

| Volume reaction | Revenue effect | EBIT effect | Arithmetic |
|---|---|---|---|
| 0% (volume holds) | +EUR 1.20m | **+EUR 1.20m** | 5% × 24.0m |
| −3.3% (expected, from 2023 elasticity) | +EUR 0.36m | **+EUR 0.84m** | gain 5%×24.0m×0.967=1.16m; lost 3.3%×40%×24.0m=0.32m; 1.16−0.32=0.84m |
| −8% (stress case) | — | **+EUR 0.34m** | gain 5%×24.0m×0.92=1.10m; lost 8%×40%×24.0m=0.77m; 1.10−0.77=0.34m |
| −11.1% (break-even) | — | **EUR 0** | by definition of break-even |
| −15% (above break-even) | — | **−EUR 0.42m** | gain 5%×24.0m×0.85=1.02m; lost 15%×40%×24.0m=1.44m; 1.02−1.44=−0.42m |

*So-what: base case adds roughly EUR 0.8m–1.2m to EBIT, about 8–13% of the range's current EUR 9.6m contribution. This assumes the 5% reaches pocket price in full — not guaranteed given current leakage and the uncapped small-accounts discount (see Implementation).*

## Implementation
| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|
| Publish 5% list increase | All (standard seal range) | 1 March 2027 | Sales director | Updated price list |
| Give 60 days' contractual notice | Distributors (30% of volume) | By early January 2027 (≈60 days before 1 March) | Sales director | Confirm notice is sent before/at the January board decision, not after |
| Carry increase into contract renewal | OEM key accounts (55% of volume) | January 2027 renewal | Key account director | Write the 5% into the 2027 annual contract terms at renewal, rather than a mid-contract change — check first whether renewed contracts lock price for the full 12 months |
| Cap discretionary discount | Small direct accounts (15% of volume) | 1 March 2027 | Sales director | Introduce an approval cap (e.g., sales-director sign-off required above the current 22% average), so reps cannot discount the increase away |

## What would change the answer
1. If expected volume loss is confirmed above ~8–9% (approaching the 11.1% break-even) once OEM/distributor reaction is tested, the EBIT gain shrinks toward zero and the case weakens sharply.
2. If OEM contracts renewing January 2027 lock price for the full 12 months and the 5% cannot be written into that renewal, ~55% of volume (and EBIT) is delayed to the January 2028 renewal — recompute year-one effect on the remaining 45% of volume only (distributors + small accounts), which roughly halves the year-one EBIT gain.
3. If the small-accounts discount cap is not adopted, assume leakage there continues at 22%+ and the increase does not reach pocket price for that 15% of volume — scale the EBIT effect down roughly pro-rata.
4. If either competitor raises or cuts list prices before March 2027, the 7–9% benchmark gap (and the room it implies) changes and the position case should be rechecked using public price lists at that time.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 5% list increase flows through proportionally to invoice price, rebates and freight (discount %s and freight cost treated as proportional for this estimate) | Pocket price scales 1:1 with list price, absent new leakage | Pack gives the waterfall only as % of list; no per-unit freight cost given | Freight is actually a fixed EUR cost per shipment rather than a %; pocket-price gain would be slightly larger than the proportional estimate |
| 2 | Variable cost per unit does not move with the price change | 40% contribution margin applied only to the volume change, not the price change | Standard pricing economics; no cost data suggesting otherwise | Input costs are rising at the same time, eroding margin independent of the price move |
| 3 | The 2023 elasticity (−0.67) applies linearly to a 5% increase | Expected volume loss ≈ 3.3% | Only historical price-change data point in the pack | Customer resistance is non-linear and larger at 5% than at 3% — real loss could sit nearer the 11.1% break-even |
| 4 | Competitor list prices stay roughly flat between the Sept 2026 benchmark and March 2027 | 7–9% gap narrows to roughly 2–4% below competitors post-increase | No forward-looking competitor pricing data in the pack | A competitor move (up or down) before March 2027 changes the post-increase gap and the volume-risk read |
| 5 | "Standard seal range" is priced uniformly across all three segments, with no stated exemptions | 5% applied across OEM, distributors and small accounts alike | The sales director's question names a flat 5%, with no segment split given | Given how different the three segments' discount and control profiles are, the board may prefer a differentiated increase (e.g., smaller for OEM, larger for small accounts) rather than one flat number |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What volume loss would the board actually accept, and over what period? | This is the real decision threshold, not just the technical 11.1% break-even | Sales director / board | If the board's real tolerance is below ~3–4%, the margin of safety shrinks sharply |
| Do OEM annual contracts renewing in January 2027 lock the price for the full 12 months, and can the 5% be written into contracts signed before 1 March? | 55% of volume — a timing mismatch could delay most of the EBIT effect by up to ~10 months | Key account director | If the increase can't enter January renewals, recompute year-one EBIT on ~45% of volume only |
| Can the small-accounts discount be capped before 1 March, and will the sales team accept it? | 15% of volume, with the highest (22%) and only uncapped discount, is most exposed to leakage | Sales director / sales reps | Without a cap, assume most of the increase in this segment is given straight back as discount |
| Is there any more recent evidence of customer reaction (e.g., signals from current renewal conversations), beyond the single 2023 data point? | One historical observation is thin evidence for extrapolating to a larger (5% vs 3%) increase | Sales director / account teams | A direct, recent signal would sharpen the volume-loss estimate well beyond the 2023 extrapolation |
| Will either main competitor change list prices before March 2027? | Determines whether the 7–9% benchmark gap narrows, holds or widens as planned | Sales / competitive intelligence, using public price lists only | A competitor increase preserves headroom for Ravensworth; a competitor hold or cut narrows the gap further and raises volume risk |

