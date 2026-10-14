# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge 2023→2025 by driver sums to -10.76 and names variable cost per parcel as the largest driver | yes | Bridge table: volume +2.2, price +2.6, labour -9.36, fuel -4.16, subcontractors -1.04, fixed -1.0 → EBIT 5.24; 'price/volume recovered +4.8m, against a −14.56m variable-cost shock plus −1.0m fixed-cost growth' |
| Splits variable cost into labour, fuel, subcontractors; labour into wage and productivity effects | yes | 'Variable cost — labour / −9.36 / ... wage-rate (+9% deal) ≈ −7.30, driver-productivity loss (18.0→17.6/hr) ≈ −2.06' plus fuel −4.16 and subcontractors −1.04 rows |
| Root cause stated upfront: unit cost +~0.28/9.7% vs price +~0.05/1.25%, mainly due to 60% volume on non-indexed fixed contracts | yes | Answer: 'variable cost per parcel rose EUR 0.28 (+9.7%)... the 60% of volume locked into 2023-vintage three-year contracts with no fuel or wage indexation captured none of the pass-through'; bridge table shows 'Price (+EUR 0.05/parcel at 2025 volume)' |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~1.6m EBITDA) as constraint on one-off costs/timing | yes | 'Net debt/EBITDA = 44/14.2 = 3.10x against a 3.5x covenant cap — EBITDA has about EUR 1.6m... further room to fall before breach'; Risk #5 ties this to one-off programme costs narrowing headroom before 2027 benefit lands |
| Action plan in one reconciled bridge, each with EBIT effect/range/one-off cost/timing/owner/confidence; renewal timed to 2026 window with volume risk shown | yes | Action table has all six columns per row; renewal row: 'Renews H1 2026... customer-attrition risk unquantified'; Risk #4 notes volume loss risk at renewal |
| Actions reach or show remaining gap to ~12.6m EBIT (6%) by 2027 | yes | 'Target: 6% margin by 2027 requires EBIT ≈ EUR 12.6–12.9m... a gap of ≈ EUR 7.4m'; 'Reading the gap' section quantifies shortfall at parity case (~5.6%) vs stretch case closing it |
| Treats peer margin claim as unverified and names peer figures to compile before claiming internal cause | yes | 'The CFO's claim that two listed peers "held their margins"... is unverified... Needs the actual reported and normalized peer margins, and whether peer contracts carry indexation' |
| No euro counted twice | yes | 'Fuel pass-through is folded into the renewal action... not counted as a separate lever, to avoid double counting with the renewal price effect' |
| Does not propose across-the-board cost cut before diagnosis or cuts to drivers/sorters without addressing productivity/service | yes | 'resist an across-the-board cost target'; 'a targeted (not blanket) overhead review'; trap check confirms 'No action cuts capability the recovery depends on' |
| Does not invent peer margins or industry wage data | yes | Peer margins explicitly flagged as open/unverified rather than assumed; no fabricated industry wage figures introduced |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

Answer page written to `case-profitability-turnaround-kestrel.md`. Headline:

**Root cause:** not a cost blowout or volume problem — variable cost/parcel rose 9.7% (mostly the 9% wage deal + driver productivity slipping from 18.0 to 17.6/hour), but it's a contract-design failure: the 60% of volume on 2023-vintage three-year contracts has **zero fuel/wage indexation**, so price only recovered 32% of the cost increase (all of it from the other 40% repricing to EUR 4.125 — the fixed book contributed nothing). The bridge reconciles exactly (EUR 16.0m → 5.24m EBIT) and the blended-price identity (0.6×4.00+0.4×4.125=4.05) pins the fault precisely on that 60% block.

**Plan to hit 6% by 2027:** reprice that block at its H1 2026 renewal to ~EUR 4.15–4.20/parcel with indexation, recover driver productivity to 18.0/hour, plus a targeted (not blanket) overhead review. Merely matching the other book's price (4.125) gets to ~5.6% — short by ~0.9m EBIT.

Flagged as open/unverified rather than guessed: peer margins (CFO's claim, uncompiled), any 2026-27 wage round, cost benchmarks, and renegotiation/capex one-off costs — these sit in the Open questions table. Covenant headroom (3.10x vs 3.5x cap) is safe but worth monthly tracking given the plan's costs land before its 2027 payoff.


## Files in work dir after run

- case-profitability-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-profitability-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics parcel division, what explains the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore at least 6% by 2027?

**Answer:** The decline is a contract-design failure, not a cost or volume problem: variable cost per parcel rose EUR 0.28 (+9.7%, mostly the 9% wage deal and lower driver productivity), but the 60% of volume locked into 2023-vintage three-year contracts with **no fuel or wage indexation** captured none of the pass-through the other 40% achieved — repricing that 60% block to roughly EUR 4.15–4.20/parcel at its H1 2026 renewal, recovering driver productivity from 17.6 back to 18.0 parcels/hour, and a targeted (not across-the-board) ~EUR 0.5–1.0m overhead review together close the gap to a 6%+ margin by 2027; simply matching the 60% block to the price the 40% annual book already gets (EUR 4.125) falls about EUR 0.7–0.9m short, landing around 5.5–5.6%.

**Confidence:** Medium — the diagnosis is high-confidence (the bridge reconciles exactly to the reported EBIT fall and the contract math ties out to the cent), but the answer depends on a single lumpy negotiation (the 2026 renewal of 60% of volume) and on peer and cost-benchmark data the CFO flagged as "not compiled yet." Would change if the renewal yields less than ~EUR 4.15/parcel, if a new wage round lands before 2027, or if peers turn out to have suffered the same decline (suggesting a sector cost shock rather than a fixable Kestrel contract-design gap).

**Liquidity check:** Safe for now, but watch. Net debt/EBITDA = 44/14.2 = 3.10x against a 3.5x covenant cap — EBITDA has about EUR 1.6m (≈11%) further room to fall before breach. Cash covers roughly 9 months of fixed cost (~EUR 30m against ~EUR 3.3m/month). Not at risk today, but the plan's one-off renegotiation and productivity-programme costs (not yet sized — see Open questions) and the 12–18 month gap before the 2026 renewal pays off mean covenant headroom should be tracked monthly, not assumed.

## Profit bridge 2023 to 2025

Reconciles exactly: EUR 16.0m → EUR 5.24m (reported as EUR 5.2m / 2.5% margin).

| Driver | Effect (EUR m) | Basis |
|---|---|---|
| EBIT 2023 (8.0% margin on EUR 200.0m revenue) | +16.0 | 50.0m parcels × (4.00 − 2.90) − 39.0 |
| Volume (+2.0m parcels at 2023 contribution/parcel) | +2.2 | 2.0m × (4.00 − 2.90) |
| Price (+EUR 0.05/parcel at 2025 volume) | +2.6 | 0.05 × 52.0m |
| Variable cost — labour | −9.36 | (1.78 − 1.60) × 52.0m; of which wage-rate (+9% deal) ≈ −7.30, driver-productivity loss (18.0→17.6/hr) ≈ −2.06 |
| Variable cost — fuel | −4.16 | (0.78 − 0.70) × 52.0m |
| Variable cost — subcontractors | −1.04 | (0.62 − 0.60) × 52.0m |
| Fixed cost | −1.0 | 40.0 − 39.0 |
| **EBIT 2025 (2.5% margin on EUR 210.6m revenue)** | **5.24** | ties to reported EUR 5.2m |

Check: volume + price recovered **+4.8m**, against a **−14.56m** variable-cost shock plus **−1.0m** fixed-cost growth — price/volume offset only 32% of the cost increase. Labour is 65% of the variable-cost deterioration, fuel 29%, subcontractors 7%. Fixed cost grew only 2.6% against 4% volume growth — it is not the driver; **resist an across-the-board cost target**.

## Where profit is lost: it is a whole contract vintage, not a few bad contracts

| Contract type | Share of 2025 volume | Price/parcel | Contribution/parcel (at 2025 cost of EUR 3.18) | Cost pass-through since 2023 |
|---|---|---|---|---|
| 3-year fixed, signed early 2023, no fuel/wage indexation | 60% (≈31.2m parcels) | EUR 4.00 | EUR 0.82 | **None** — price unchanged since 2023 |
| Annual, repriced | 40% (≈20.8m parcels) | EUR 4.125 | EUR 0.945 | Partial — +3.1% price vs +9.7% cost |

Blended price check: 0.6 × 4.00 + 0.4 × 4.125 = **4.05**, exactly the reported 2025 revenue/parcel — confirms the entire price-realization problem sits in the 60% fixed book, which renews in H1 2026. This kills the "a handful of underpriced contracts" sub-hypothesis: the mispricing is structural across an entire contract vintage, not a few outliers.

## Is it internal or market-wide?

Open. The CFO's claim that two listed peers "held their margins" in 2024–25 is unverified — figures not yet compiled. This is the single biggest swing factor on confidence: if true, it points to a Kestrel-specific contract-design failure (fixable at renewal, as sized below); if peers also declined, it points to a sector-wide cost shock that the whole market is still working through, which would support the same renewal action but lower confidence in reaching 6% from pricing power alone. Needs the actual reported and normalized peer margins, and whether peer contracts carry indexation, before this is more than a client statement.

## Action plan (reconciled, no double counting)

Target: 6% margin by 2027 requires EBIT ≈ EUR 12.6–12.9m (vs EUR 5.24m in 2025, flat-volume base) — a gap of **≈ EUR 7.4m**.

| Action | EBIT effect (base case) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reprice the 60% fixed book at 2026 renewal with fuel + wage indexation clauses, to ≥ EUR 4.15–4.20/parcel (parity with the 40% book, EUR 4.125, is a floor, not the target) | +3.9 at parity (4.125); +5.5–6.0 at 4.15–4.20 | 3.0 – 6.0 | Not sized — legal/commercial renegotiation cost; customer-attrition risk unquantified | Renews H1 2026; half-year 2026 effect, full 2027 effect | Commercial director | Medium — single negotiation, competitive dynamics unknown |
| Recover driver productivity from 17.6 to 18.0 parcels/driver-hour (routing, sort-center scheduling) | +2.1 | 1.5 – 2.5 | Capex/IT cost not sized | 12–18 months, starts now | Ops director | Medium |
| Targeted overhead review (not a blanket cut) on the fixed-cost growth and any slack it reveals | +0.7 | 0.5 – 1.0 | Low, mostly internal effort | 6–12 months | CFO office | Low-medium — no cost benchmark data yet to size precisely |
| **Total, reconciled** | **+6.7** (parity case) to **+9.5** (stretch case) | **5.0 – 9.5** | **not yet fully sized** | parity case lands 2027, stretch case needs full renewal upside | | |

Fuel pass-through is folded into the renewal action (one indexation clause), not counted as a separate lever, to avoid double counting with the renewal price effect.

**Reading the gap:** at parity pricing (EUR 4.125) plus the base-case ops and overhead actions, 2027 EBIT ≈ EUR 11.95m on EUR 214.5m revenue = **5.6%** — about EUR 0.9m / 0.4 points short of 6%. Closing the rest needs the renewal to land nearer **EUR 4.15–4.20/parcel** on the 60% block (a 4–5% ask on top of what the 40% book already achieved, still far below the 9% cost inflation it is meant to offset) rather than mere parity — a reasonable renegotiation ask, but not guaranteed, hence the Medium confidence.

## Risks and what would change the answer

1. If the 2026 renewal lands at or below EUR 4.125/parcel (parity only), 2027 margin lands around 5.5–5.6%, not 6% — the plan needs a second lever (larger overhead programme, volume growth, or a second price step) agreed now as a fallback.
2. If peer margins turn out to have declined similarly, the cause is partly a sector cost shock, not solely a Kestrel contract-design gap — lowers confidence that price alone restores 6%, and argues for weighting the productivity and overhead levers higher.
3. If a new wage agreement is signed before 2027, the EUR 7.4m gap grows and the renewal price target in the action plan above is too low.
4. If customers contest the indexation clauses and volume is lost at renewal, the +3.9 to +6.0m price effect does not fully materialize — the bridge above assumes volume held flat at 52.0m through the renegotiation.
5. If the productivity and overhead programmes carry meaningful one-off costs or require capex that temporarily depresses EBITDA, covenant headroom (currently ~EUR 1.6m of further EBITDA room) narrows before the renewal benefit lands in 2027 — sequence and size these before committing.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2027 volume held flat at 52.0m parcels for gap sizing | 52.0m | No market/volume forecast in the data pack | Real growth or decline materializes; each ±1m parcels ≈ ±EUR 0.87m EBIT at 2025 contribution/parcel, before any fixed-cost step change |
| 2 | Variable cost per parcel is the same regardless of contract type | EUR 3.18/parcel for both books | Data pack gives one blended cost figure, not segmented by contract | The fixed-price book is served by different routes/density with a different true unit cost |
| 3 | Renewal base case repricing level | EUR 4.125/parcel (parity with the annual book); stretch case EUR 4.15–4.20 | Only observed market reference point in the pack is the 40% book's realized price | Actual negotiated renewal price lands materially above or below this range |
| 4 | No further wage-agreement increase 2025–2027 beyond the known +9% (2023–25) | 0% further increase assumed | No 2026/27 wage data given | A new wage round is signed before 2027 |
| 5 | Targeted overhead programme size | EUR 0.5–1.0m (midpoint 0.75m) | No cost-benchmark or activity-based cost data provided; placeholder range | A value-chain/zero-based review sizes materially more or less |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Peer margins and indexation practice (CFO says peers "held their margins" — not compiled) | Determines whether this is a Kestrel-specific, fixable contract-design gap or a sector-wide cost shock | CFO / commercial, from peer annual reports | Could raise or lower confidence materially; may change the weighting between price and cost levers |
| Is a 2026–27 wage agreement signed or under negotiation? | Changes the size of the EUR 7.4m gap and the renewal price target | HR / commercial | Larger future wage step raises the required renewal price and/or productivity gain |
| Expected 2026–27 volume / market growth | Changes the revenue base the 6% target is measured against | Commercial / planning | Volume growth makes 6% easier to reach; decline makes it harder |
| Customer retention risk and competitive pricing at the 2026 renewal for the 60% fixed book | Directly sizes the largest lever in the plan | Commercial / sales leadership | Determines whether EUR 4.15–4.20/parcel is achievable or whether volume is lost instead |
| One-off cost of contract renegotiation and the driver-productivity programme (capex/IT) | Not yet sized; affects cash and covenant headroom through 2026–27 | Ops / IT / legal | Could delay or reduce the net EBIT benefit and tighten covenant headroom |
| Normalized peer cost per parcel (labour, fuel, subcontractor; scope and outsourcing adjusted) | Needed to confirm whether Kestrel's cost base itself is out of line, beyond the pass-through gap | Commercial / finance benchmarking | Could reveal an additional, separate cost lever or rule one out |
| Do the three-year contracts permit mid-term renegotiation, or only renewal at term; any MFN or notice-period clauses? | Affects timing and feasibility of the renewal action | Legal / commercial | Could accelerate or delay when the EUR 3.9–6.0m price effect lands |

**Specialists and review:** Commercial/contract legal counsel should review renegotiation mechanics (indexation clause drafting, notice periods, most-favoured-customer clauses) before the 2026 renewal is launched. Treasury should pre-brief the lending bank on covenant headroom given the plan's timing (benefit lands mostly in 2027) and any interim one-off costs.

## Trap checks

- [x] Diagnosis came before any cost target — the bridge was built first; no cost target was set in advance.
- [x] Averages were broken down — split into volume/price/three cost components, and further into contract type, revealing the 60% fixed book as the entire source of the price-realization failure.
- [ ] Benchmarks normalized before any gap claimed — **open**: no peer or normalized cost-per-parcel data available. The cause is diagnosed from Kestrel's own bridge, not from an external benchmark; peer figures are requested above, not assumed.
- [x] All actions sit in one reconciled bridge, no euro counted twice — fuel pass-through is inside the renewal action, not a separate fuel lever; price (renewal) and productivity (ops) act on cleanly separate cost lines.
- [~] One-off costs, notice periods and renewal dates are in the timing — renewal date (H1 2026) and the lag to full 2027 effect are built in; the euro cost of renegotiation and the productivity programme are **not yet sized** — see Open questions.
- [x] Liquidity was checked separately from profitability — covenant and cash-runway section above, independent of the profit bridge.
- [x] No action cuts capability the recovery depends on — the plan explicitly avoids an across-the-board overhead cut; the fixed-cost action is targeted, and the productivity action builds capability (routing/scheduling technology) rather than cutting driver headcount or service depth.
- [x] Model passes Model Red Flags spot checks — the bridge sums exactly to the reported EBIT change (16.0 → 5.24m), the blended-price identity (0.6×4.00+0.4×4.125=4.05) ties to the reported 2025 revenue/parcel, and units (EUR, EUR/parcel, m parcels) are consistent throughout. Action costings (programme capex) remain placeholders pending the data requests above — a data gap, not an error in the existing bridge.

