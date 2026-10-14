# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge 2023→2025 sums to -10.76 and names variable cost per parcel as the largest driver | yes | Bridge table: +2.20+2.60-7.49-1.87-4.16-1.04-1.00 = -10.76 (EBIT 16.00→5.24); headline frames 'variable cost per parcel moved +9.7%' vs price +1.25% as the core driver |
| Splits variable cost into labour, fuel, subcontractors; labour into wage and productivity effects | yes | Table rows: 'Labour — wage rate ... −7.49', 'Labour — productivity ... −1.87', 'Fuel ... −4.16', 'Subcontractors ... −1.04' |
| Root cause stated first in one sentence: unit cost +0.28/9.7% vs price +0.05/1.25%, mainly due to 60% fixed-price contracts without indexation | yes | '60% of volume (31.2m parcels) sits on 2023 fixed-price contracts with zero fuel/wage indexation — price moved +1.25% while variable cost per parcel moved +9.7%.' |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~1.6m EBITDA) as constraint on one-off costs/timing | yes | 'Net debt/EBITDA = 44/14.2 = 3.10x against a 3.5x covenant — EBITDA could fall only ~11% (to €12.6m) before breach'; open question ties one-off costs to 'when the plan clears the covenant-headroom risk noted above' |
| Action plan in one reconciled bridge with EBIT effect, range, one-off cost, timing, owner, confidence; renewal repricing timed to 2026 window with volume risk shown | yes | Table columns 'EBIT effect (base) / Range / One-off cost / Timing / Owner / Confidence'; repricing action: 'Phases in H1 2026... volume-retention risk not quantified' |
| Actions reach or show remaining gap to ~12.6m EBIT (6%) by 2027 | yes | 'required EBIT gain of ≈€7.4m (to reach 6% margin ... €12.6m) ... two sized actions deliver €5.77m ... remaining ~€1.5–1.6m needs to come from fuel pass-through, overhead' |
| Treats peer margin claim as unverified; names peer figures to compile (normalised margin, indexation practice) before internal-cause claim | yes | Open question: 'Do peers' 2024–2025 margins, once compiled (reported and normalised), actually hold steady, and what is their contract-indexation practice?' |
| No euro counted twice (price/volume effects on same contracts consistent) | yes | Segment table reconciles weighted avg price (0.6×4.00+0.4×4.125=€4.05) exactly to reported 2025 figures alongside the separate volume/price bridge lines |
| Does not propose across-the-board cost cut before diagnosis or cuts to drivers/sorters without addressing productivity/service | yes | 'An overhead cost-cutting programme would only touch ~€1.0m of the €10.76m EBIT decline' — plan instead centers on repricing and productivity recovery, not headcount cuts |
| Does not invent peer margins or industry wage data | yes | Peer margins explicitly flagged as 'not yet compiled'; wage figure (+9%) is treated as pack-given data, not fabricated industry data |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

Saved as `case-profitability-turnaround-kestrel.md`. Headline for the CFO:

**This is a contracting problem, not a cost problem.** 60% of volume (31.2m parcels) sits on 2023 fixed-price contracts with zero fuel/wage indexation — price moved +1.25% while variable cost per parcel moved +9.7%. An overhead cost-cutting programme would only touch ~€1.0m of the €10.76m EBIT decline.

The reconciled profit bridge (2023 → 2025, ties exactly):
- Volume +€2.2m, Price +€2.6m
- Labour: −€7.49m wage-driven, −€1.87m productivity-driven (18.0→17.6 parcels/driver-hour)
- Fuel −€4.16m, Subcontractors −€1.04m, Fixed cost −€1.0m

Plan: reprice/index the 31.2m fixed-contract parcels at the H1 2026 renewal to parity with the current annual-contract price (+€3.9m) and recover driver productivity to 2023 levels (+€1.9m). That lands around 5.5–5.7% margin on today's volumes — close to but not certainly at the 6% target; the last ~€1.5m needs fuel pass-through and overhead/subcontractor work that the data pack can't size yet.

Liquidity isn't an immediate issue (≈9 months cash runway), but covenant headroom is thin — net debt/EBITDA is already 3.10x against a 3.5x limit, so EBITDA has only ~11% room to fall before breach.

Six open questions are flagged in the file (peer benchmark not yet compiled, fuel price-vs-consumption split, 2026–27 volume forecast, renewal negotiating leverage, one-off costs, and the unsized overhead/subcontractor levers) — these are what would move the answer from "plausible" to "proven."


## Files in work dir after run

- case-profitability-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-profitability-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics (parcel division), what caused the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore ≥6% by 2027?

**Answer:** The decline is 73% commercial, not operational: 31.2m parcels (60% of 2025 volume) sit on 2023-vintage fixed-price contracts with no fuel or wage indexation, so price barely moved (+1.25%) while variable cost per parcel rose 9.7%. A cost-cutting programme on fixed overhead — the usual first instinct — would address at most €1.0m of the €10.76m EBIT decline. Repricing/indexing that 60% at the 2026 renewal (+€3.9m) plus recovering driver productivity to the 2023 level (+€1.9m) gets to roughly 5.5–5.7% margin on today's volumes; closing the last ~€1.5m to 6% depends on fuel pass-through and overhead actions that are not yet sized.

**Confidence:** Medium — the profit bridge reconciles exactly to the reported numbers and the contract-indexation root cause is well evidenced; the plan's ability to clear 6% rests on three unverified items (peer benchmark, renewal negotiating leverage, fuel rate-vs-consumption split).

**Liquidity check:** Not at immediate risk, but covenant headroom is thin. Net debt/EBITDA = 44/14.2 = 3.10x against a 3.5x covenant — EBITDA could fall only ~11% (to €12.6m) before breach, absent debt paydown. Cash covers ~9 months of fixed cost. No 13-week cash plan is needed today, but the covenant should be tested each quarter through the 2026 renewal window, since a bad renegotiation outcome is the main risk to it.

## Profit bridge 2023 to 2025

Reconciles exactly (16.00 → 5.24, a €10.76m decline):

| Driver | Effect (EUR m) |
|---|---|
| EBIT 2023 (50.0m parcels, 8.0% margin) | +16.00 |
| Volume (+2.0m parcels at 2023 contribution of €1.10/parcel) | +2.20 |
| Price (avg +€0.05/parcel on 52.0m parcels) | +2.60 |
| Labour — wage rate (+9% wage agreement, at 2023 productivity) | −7.49 |
| Labour — productivity (18.0 → 17.6 parcels/driver-hour) | −1.87 |
| Fuel (+€0.08/parcel on 52.0m parcels) | −4.16 |
| Subcontractors (+€0.02/parcel on 52.0m parcels) | −1.04 |
| Fixed cost (€39.0m → €40.0m) | −1.00 |
| **EBIT 2025 (52.0m parcels, 2.49% margin)** | **5.24** |

So-what: volume and price growth added €4.8m; cost inflation and fixed cost took away €15.56m. Labour is the largest single cost driver (−€9.36m), but 80% of that (−€7.49m) is the market-wide wage settlement, not a controllable usage effect — the controllable slice is the €1.87m productivity slip. Fuel (−€4.16m) and the price shortfall are the two drivers most tied to contract design rather than operations.

## Where profit is lost

| Segment | Volume (2025) | Price/parcel | Variable cost/parcel* | Contribution margin | Trend |
|---|---|---|---|---|---|
| Fixed 3-yr contracts, signed 2023, no indexation | 31.2m (60%) | €4.00 | €3.18 | €0.82/parcel (20.5%) | Fixed since 2023; cost has risen under it every year; renews H1 2026 |
| Annual contracts, repriced | 20.8m (40%) | €4.125 | €3.18 | €0.945/parcel (22.9%) | Already tracks cost inflation |

*Variable cost per parcel assumed uniform across segments (see Assumptions #1). The two segments' weighted average price (0.6×4.00 + 0.4×4.125 = €4.05) and the fixed-cost base reconcile exactly to the reported 2025 figures.

The fixed-price book earns ~13% less contribution per parcel than the repriced book, on contracts that haven't moved since 2023 and won't move again until mid-2026. This is the one lever worth a tenth of the gap or less if left alone, and the biggest lever in the plan once renewed.

## Action plan

| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reprice + add fuel/wage indexation on the 31.2m fixed-contract parcels at 2026 renewal, to at least parity with current annual-contract price (€4.125) | +3.90 | 2.5–4.5 | Negotiation effort; volume-retention risk not quantified | Phases in H1 2026; full run-rate 2027 | Commercial | Medium |
| Recover driver productivity 17.6 → 18.0 parcels/driver-hour (scheduling, route density) | +1.87 | 0.9–1.9 | Possible scheduling/training spend, not quantified | 2026–2027 | Operations | Medium |
| Fuel surcharge/indexation clause on same renewal, to pass through future tariff moves | Not sized — needs fuel price-vs-consumption split | — | — | With contract renewal, H1 2026 | Commercial/Procurement | Low (unsized) |
| Overhead discipline: hold fixed-cost growth below revenue growth | +0.5 (indicative) | 0–1.0 | Not quantified | 2026–2027 | Operations/Finance | Low (unsized) |
| Subcontractor rate renegotiation | +0.3 (indicative) | 0–1.0 | Not quantified | 2026 | Procurement | Low (unsized) |
| **Total, reconciled, no double counting** | **~6.6** | **4.2–8.4** | — | — | — | — |

Against a required EBIT gain of ≈€7.4m (to reach 6% margin on 2025's €210.6m revenue base, from today's €5.24m), the two sized, high-confidence actions (contract repricing + productivity) deliver €5.77m — roughly 5.5–5.7% margin on current volumes. The remaining ~€1.5–1.6m needs to come from fuel pass-through, overhead, or subcontractor terms, none of which are sized yet. The target is plausible, not yet proven, with this data.

## Risks and what would change the answer

1. If the 2026 renewal lands below €4.125/parcel (weak negotiating position or customer attrition), the single largest lever shrinks pro-rata — e.g. at €4.08 it's worth €2.5m instead of €3.9m, and 6% is out of reach without additional fixed-cost or fuel action.
2. If peer margins, once compiled, show the same erosion, the cause is partly structural/market-wide (industry-wide wage and fuel inflation), not purely a Kestrel contracting mistake — the fix shifts from "renegotiate" toward "the whole market needs to reprice," which may limit how aggressively Kestrel can push at renewal.
3. If the fuel cost increase is mostly consumption (route inefficiency) rather than price, a surcharge clause doesn't fix it — the lever becomes operational (routing/vehicle utilisation) instead of commercial, and is not currently sized.
4. If 2026–2027 volumes grow materially, the euro gap to 6% changes (a larger revenue base needs a larger EBIT to hit the same percentage); this plan is built on a flat-volume assumption.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Variable cost per parcel is the same across the fixed-contract and annual-contract segments | €3.18/parcel for both | No segment-level cost data in the pack | Fixed-contract volume has different cost-to-serve (e.g. denser/longer routes), changing segment margins materially |
| 2 | 2027 target base = 2025 volume and price (52.0m parcels, €210.6m revenue) | Flat volume/price | No 2026–2027 volume forecast given | Volume grows or shrinks materially, changing the euro EBIT needed for 6% |
| 3 | Renewal repricing target = parity with current annual-contract price | €4.125/parcel | Best available comparable in the pack | Negotiated renewal price differs from this due to competitive or customer pressure |
| 4 | Labour cost increase splits cleanly into a wage-rate effect and a productivity effect | 80% rate (−€7.49m) / 20% productivity (−€1.87m) | HR wage agreement (+9%) and ops productivity data (18.0→17.6 parcels/driver-hour), both from the pack | Other labour-mix changes (headcount mix, overtime) also moved the cost per parcel |
| 5 | Fuel and subcontractor cost increases are addressable via indexation/surcharge clauses | Treated as commercial pass-through candidates | Analogy to the labour/contract fix; no fuel rate-vs-consumption data given | Fuel increase is driven by consumption/route inefficiency rather than price, requiring an operational fix instead |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Do peers' 2024–2025 margins, once compiled (reported and normalised), actually hold steady, and what is their contract-indexation practice? | Determines whether the cause is purely internal (fixable by Kestrel alone) or partly industry-wide | Commercial/strategy team, from peers' annual reports | Could shift root-cause framing and the realism of the 6% target |
| What is the split between fuel price (tariff) and fuel consumption (litres/parcel) behind the €0.08/parcel increase? | Decides whether the fuel lever is a commercial surcharge clause or an operational routing fix, and sizes it | Procurement/Operations | Sizes the currently-unsized €4.16m fuel driver and the matching action |
| What volume/revenue is realistically expected for 2026–2027? | The €7.4m EBIT gap to 6% is calculated on a flat-volume assumption | Commercial/FP&A | Resizes the gap and every action's required value |
| What negotiating leverage does Kestrel have at the 2026 renewal of the 31.2m-parcel book — attrition risk, competitive alternatives available to those customers? | Biggest swing factor on the largest single lever (€2.5–4.5m range) | Commercial/Sales leadership | Narrows the range on the plan's largest action |
| What one-off costs (negotiation, legal, scheduling/training for productivity recovery) would the plan incur, and over what period? | Net EBIT benefit and timing against covenant headroom depend on this | Finance/Operations | Could delay when the plan clears the covenant-headroom risk noted above |
| How much of the €1.0m fixed-cost growth and €1.04m subcontractor cost increase is recoverable, and by when? | Needed to close the remaining ~€1.5m gap to 6% with confidence | Operations/Procurement | Converts two "indicative, unsized" rows into costed actions |

