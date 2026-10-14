# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge 2023→2025 by driver sums to -10.76 and names variable cost per parcel as the largest driver | yes | Bridge table: +2.20 volume, +2.60 price, -9.36 labour, -4.16 fuel, -1.04 subcontractors, -1.00 fixed = -10.76 net; text states 'The whole decline, and then some, is a variable-cost story — mostly labour' |
| Splits variable cost into labour, fuel, subcontractors; labour into wage and productivity effects | yes | Table rows '-9.36' labour 'of which ≈ −7.3 wage-rate and ≈ −2.0 driver-productivity', '-4.16' fuel, '-1.04' subcontractors |
| Root cause stated in one sentence first with unit cost rise (~EUR0.28/9.7%) vs price rise (EUR0.05/1.25%) due to 60% unindexed fixed-price volume | NO | The opening Answer sentence only states 'none of the 9.7% rise in variable cost per parcel was recovered on that book' — it never pairs this with the price-side figure (EUR0.05 / 1.25%) in the same sentence anywhere in the document |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~EUR1.6m EBITDA) as constraint on one-off costs/timing | yes | 'Net debt/EBITDA = 44.0/14.2 = 3.1x vs. a 3.5x covenant ceiling — about EUR 1.6m of EBITDA headroom... one-off renewal/restructuring costs or a bumpy 2026 renegotiation should be checked against it before the plan is locked' |
| Action plan in one reconciled bridge with EBIT effect, range, one-off cost, timing, owner, confidence per action; repricing timed to 2026 renewal window with volume risk shown | yes | Action table includes all six columns per row; repricing row timed 'H1 2026 renewal' with 'some risk of volume loss to re-tender' noted |
| Actions reach or show remaining gap to ~EUR12.6m EBIT (6%) by 2027 | yes | 'Lands EBIT at ~EUR 13.3m on ~EUR 216.5m revenue ≈ 6.1% margin in the base case' |
| Treats peer margin claim as unverified and names peer figures to compile (normalised margin, indexation practice) before claiming internal cause | yes | 'the figures are not yet compiled — this is a client assertion, not evidence'; open question asks 'What are the two peers' actual reported and normalised EBIT margins for 2024-25, and do their contracts carry indexation?' |
| No euro counted twice | yes | Action plan explicitly labeled '(reconciled, no double counting)' and actions map distinctly to separate bridge components (productivity, fuel/subcontractor, overhead) without overlapping the repricing lever |
| Does not propose an across-the-board cost cut before diagnosis, or driver/sorter cuts without addressing productivity and service | yes | 'Targeted overhead efficiency... no across-the-board cut' and productivity action is 'Recover driver productivity... via routing/sort optimisation' rather than headcount cuts |
| Does not invent peer margins or industry wage data | yes | Peer margins flagged as unverified/open question rather than asserted; wage figures used are from the company's own wage-agreement data (+9%), not invented industry data |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

Answer page saved to `case-profitability-turnaround-kestrel.md`.

**Bottom line:** The margin collapse (8.0%→2.5%) is almost entirely a contract-design problem, not a generic cost blowout. The bridge from 2023→2025 reconciles exactly: +€2.2m volume, +€2.6m price, offset by −€9.4m labour, −€4.2m fuel, −€1.0m subcontractors, −€1.0m fixed cost. Breaking the average open shows why: 60% of volume sits on 3-year contracts signed in early 2023 at a flat €4.00/parcel with zero fuel/wage indexation — their contribution margin fell from 27.5% to 20.5% while the other 40% (repriced annually) held up better at 22.9%.

That legacy book renews in H1 2026 — squarely inside the plan window — making contract repricing with an indexation clause the single biggest, best-timed lever (an estimated €3.9m–7.8m of EBIT), topped up with smaller productivity, procurement and overhead moves (~€2.3m). Base case lands around 6.1% margin by 2027 — clearing the target, but only barely, and over half of it rides on a 2026 renewal that hasn't been negotiated yet.

Flagged as open rather than guessed: the peers' "held margin" claim is unverified, there's no 2026-27 wage/fuel forecast in the pack, and the covenant headroom (3.1x vs. 3.5x cap, ~€1.6m of EBITDA buffer) should be checked against any one-off renewal/restructuring costs before the plan is locked.


## Files in work dir after run

- case-profitability-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-profitability-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics parcel division, what caused the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore at least 6% by 2027?

**Answer:** The fall is a contract-design problem, not an across-the-board cost problem: 60% of 2025 volume sits on 3-year contracts signed in early 2023 at a fixed EUR 4.00/parcel with no fuel or wage indexation, so none of the 9.7% rise in variable cost per parcel was recovered on that book; repricing it at its H1 2026 renewal (worth an estimated EUR 3.9m–7.8m of EBIT) plus targeted productivity, procurement and overhead moves (EUR ~2.3m) can plausibly land the margin around 6.1% by 2027 — but only if the renewal lands at or above today's other contract price, and only before any further wage round between now and 2027.
**Confidence:** medium, because the 2023→2025 bridge ties exactly to the reported figures and the single largest lever is well identified and timed inside the plan window, but the 2027 landing point depends on an unverified peer benchmark, an un-negotiated 2026 renewal outcome, and no 2026-27 wage/fuel forecast being in the data pack.
**Liquidity check:** Net debt/EBITDA = 44.0/14.2 = 3.1x vs. a 3.5x covenant ceiling — about EUR 1.6m of EBITDA headroom (EBITDA could fall to ~EUR 12.6m at today's debt before breach). Cash covers ~9 months of fixed cost. Safe today, but thin enough that one-off renewal/restructuring costs or a bumpy 2026 renegotiation should be checked against it before the plan is locked — not done here (see Open questions).

## Profit bridge 2023 to 2025

Parcels 2023: 50.0m at EUR 4.00 revenue / EUR 2.90 variable cost → EBIT EUR 16.0m (8.0% of EUR 200.0m revenue). Parcels 2025: 52.0m at EUR 4.05 / EUR 3.18 → EBIT EUR 5.24m (2.5% of EUR 210.6m revenue, matches the CFO's 8.0%→2.5% and the EUR 5.2m EBIT behind the stated EUR 14.2m EBITDA). Bridge below reconciles exactly (16.0 + 2.2 + 2.6 − 9.36 − 4.16 − 1.04 − 1.0 = 5.24).

| Driver | Calculation | Effect (EUR m) |
|---|---|---|
| EBIT 2023 | | +16.00 |
| Volume | +2.0m parcels × EUR 1.10 2023 contribution/parcel | +2.20 |
| Price (blended) | +EUR 0.05/parcel × 52.0m parcels | +2.60 |
| Variable cost – labour | −EUR 0.18/parcel × 52.0m, of which ≈ −7.3 wage-rate and ≈ −2.0 driver-productivity (18.0→17.6 parcels/hour) | −9.36 |
| Variable cost – fuel | −EUR 0.08/parcel × 52.0m | −4.16 |
| Variable cost – subcontractors | −EUR 0.02/parcel × 52.0m | −1.04 |
| Fixed cost | −EUR 1.0m (39.0→40.0m, roughly tracking the 4% volume growth) | −1.00 |
| **EBIT 2025** | | **+5.24** |

The wage/productivity split uses the wage-agreement (+9%) and parcels-per-driver-hour data to back out an implied hourly rate (EUR 28.80 in 2023 → EUR 31.39 in 2025); it is an approximation against the pack's rounded per-parcel figures, not an exact decomposition.

Takeaway: volume and the average price both moved in Kestrel's favour. The whole decline, and then some, is a variable-cost story — mostly labour — that the average price failed to track. But an average hides where that failure sits.

## Where profit is lost

| Segment | Volume | Revenue | Revenue/parcel | Contribution/parcel (at 2025 cost) | Contribution margin |
|---|---|---|---|---|---|
| Legacy fixed-price contracts (signed early 2023, no indexation, renew H1 2026) | 31.2m (60%) | EUR 124.8m | EUR 4.00 | EUR 0.82 | 20.5% |
| Annual contracts (repriced to 2025) | 20.8m (40%) | EUR 85.8m | EUR 4.125 | EUR 0.945 | 22.9% |
| **Total 2025** | 52.0m | EUR 210.6m | EUR 4.05 | EUR 0.87 | 21.5% |

The legacy book sits at the exact 2023 price while absorbing the full 2023→2025 cost increase — its contribution margin fell from 27.5% (2023 economics) to 20.5%, versus 22.9% for contracts that got at least one repricing cycle. It is also the one piece of the portfolio with a hard, dated fix: the H1 2026 renewal.

## Internal vs. market

The CFO cites two listed peers that "held their margins" in 2024-25, but the figures are not yet compiled — this is a client assertion, not evidence (see Open questions). Regardless of the peer outcome, the mechanism found here — a 3-year fixed-price contract signed without a fuel/wage indexation clause — is a Kestrel-specific commercial-terms issue that would need fixing even if peers also saw margin pressure from the same industry-wide cost inflation.

## Sizing the gap to 6% by 2027

2025 base: EBIT EUR 5.24m on EUR 210.6m revenue (2.5%). At flat 52.0m-parcel volume (ASSUMPTION), reaching 6% needs EBIT of roughly EUR 12.6m–13.3m depending on how much the repricing itself lifts revenue — call it an EBIT gap of **~EUR 7–8m** to close by 2027.

## Action plan (reconciled, no double counting)

| Action | EBIT effect (base case) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reprice legacy fixed-price contracts at 2026 renewal, adding a fuel/wage indexation clause | +5.9 | +3.9 (match today's annual-contract price of EUR 4.125) to +7.8 (also covers expected 2026-27 input inflation) | Negotiation effort; some risk of volume loss to re-tender | H1 2026 renewal | Commercial | Medium — depends on customer acceptance and competitive response |
| Recover driver productivity (18.0→17.6 parcels/driver-hour) by ~half via routing/sort optimisation | +1.0 | +0.5 to +1.5 | Minor, ops time | 2026 | Operations | Medium — root cause of the drop not yet diagnosed |
| Fuel and subcontractor cost actions (procurement, route efficiency, rate renegotiation) | +0.75 | +0.5 to +1.0 | Low | 2026-27 | Procurement | Low-medium — not costed in detail, needs a dedicated workstream |
| Targeted overhead efficiency (fixed cost grew roughly in line with volume, not the primary driver — no across-the-board cut) | +0.5 | +0.3 to +0.7 | Possible severance if headcount-related | 2026-27 | Finance/Ops | Medium |
| **Total, reconciled** | **+8.1** | **+5.2 to +11.0** | | | | Lands EBIT at ~EUR 13.3m on ~EUR 216.5m revenue ≈ **6.1%** margin in the base case |

The plan clears 6% only in the base-to-upper range, and more than half of the total comes from one lever (contract repricing) that is not yet negotiated. Treat it as the first thing to test, not a given.

## Risks and what would change the answer

1. If the 2026 renewal lands at or below EUR 4.00 (customers resist any increase, or volume shifts to re-tender), the plan recovers less than EUR 4m and the 6% target is missed by roughly EUR 3-4m — reprice outcome is the single biggest swing factor.
2. If a new wage agreement is struck before 2027 at a similar +9%-type step, variable cost per parcel rises again and erodes most of the productivity/procurement/overhead gains — the plan assumes labour and fuel rates are flat post-2025, which is unverified.
3. If the two peers turn out to have also lost margin over the same period, the diagnosis should broaden beyond Kestrel's own contract design to an industry-wide cost shock, which would argue for also testing whether competitors are repricing and by how much.
4. If renewal negotiations or any related restructuring create a temporary EBITDA dip, check it against the 3.5x covenant (EUR 1.6m of headroom today) before committing to the plan's timing.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2027 parcel volume held flat | 52.0m | No demand forecast in the data pack | Commercial pipeline shows material growth or decline |
| 2 | No further wage/fuel inflation beyond 2025 levels in the base case | Variable cost per parcel flat at EUR 3.18 post-2025 | No 2026-27 wage or fuel forecast in the pack | A new wage agreement or fuel price move is already expected before 2027 |
| 3 | Repriced legacy contracts land between EUR 4.125 (today's annual rate) and EUR 4.125 plus forward indexation | EUR 4.125-4.39 range used for the EUR 3.9m-7.8m action sizing | Bounded by Kestrel's own current annual-contract price; no external benchmark used | Actual negotiated rate, or competitive intelligence on peer pricing, becomes available |
| 4 | Fixed cost grows modestly without a dedicated overhead programme | ~2.5%/year, in line with the 2023-25 trend (39.0→40.0m, +2.6% over 2 years) | Historical trend in the pack | A specific overhead or site-consolidation programme is scoped |
| 5 | Variable cost per parcel is uniform across contract types | Used 2025 blended EUR 3.18 for both segments in the contribution-by-segment table | No contract-level cost data in the pack | Legacy-contract routes/customers are shown to have a materially different cost profile |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What price and indexation terms will the 2026 renewal actually land at, and what is the expected customer retention/win-rate at a higher price? | This is >70% of the sized gap to 6% | Commercial/sales leadership | Could move 2027 EBIT by several EUR m either way |
| What are the two peers' actual reported and normalised EBIT margins for 2024-25, and do their contracts carry indexation? | Tests whether the cause is Kestrel-specific or industry-wide | Compiled from peer annual reports | If peers also declined, broadens the diagnosis beyond contract design; if they held margin via indexation, strengthens this plan |
| Why did driver productivity fall from 18.0 to 17.6 parcels/hour — network growth, new routes, hiring mix, something structural? | Determines whether the ~EUR 2m productivity effect is recoverable | Operations | Changes the size and feasibility of the productivity action |
| Is a wage agreement renewal due before 2027, and at what expected rate? | Further wage inflation would erode the repricing gain | HR | Changes the 2026-27 cost assumption materially |
| What one-off costs (negotiation, possible severance, system/process changes for indexation clauses) are expected, and how do they sit against the 3.5x covenant and 9-month cash runway? | One-off costs could delay reaching 6% or pressure the covenant | Finance | Could shift the timing or size of the 2027 landing point |

