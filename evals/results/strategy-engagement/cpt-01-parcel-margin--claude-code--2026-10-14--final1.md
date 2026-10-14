# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge 2023→2025 sums to -10.76 and names variable cost per parcel as largest driver | yes | Volume +2.20, Price +2.60, Variable cost/parcel −14.56, Fixed cost −1.00 → EBIT 16.00+2.20+2.60−14.56−1.00=5.24; variable cost per parcel is the largest single driver at −14.56 |
| Splits variable cost into labour/fuel/subcontractors and labour into wage vs productivity | yes | 'labour (−9.36) / fuel (−4.16) / subcontractors (−1.04)'; 'Wage-rate effect: −7.49m (80%...) Productivity effect: −1.87m (20%...)' |
| Root cause stated in one sentence near the top (≈€0.28/9.7% unit cost vs €0.05/1.25% price, driven by 60% non-indexed fixed-price contracts) | yes | 'Variable cost per parcel rose 9.7% ... while blended price per parcel rose only 1.25% — because the three-year contracts covering 60% of volume ... carry no fuel or wage indexation and have not moved.' |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~€1.6m EBITDA) as a constraint on one-off restructuring costs AND timing | NO | Covenant headroom is only linked to timing risk ('could breach covenant before the plan's benefits land in 2027') — no connection is drawn to limiting one-off restructuring/implementation costs of the actions themselves; one-off costs are instead left as an unresolved open question. |
| Action plan as one reconciled bridge with EBIT effect, range, one-off cost, timing, owner, confidence per action; repricing timed to 2026 renewal with volume risk shown | NO | Action table columns are only 'Action / EBIT effect (base) / Range / Confidence / Timing / Owner' — no one-off cost column or figure is included for any action, despite one-off costs being explicitly flagged as unknown/unquantified in the Open Questions section rather than included in the plan. |
| Actions reach or show remaining gap to ~€12.6m EBIT (6%) by 2027 | yes | 'Total, reconciled +€8.4m to +€11.9m ... vs. required +€7.4m (3.5 margin points...) to reach 6%'; 'the two high-confidence items alone ... taking margin from 2.5% to roughly 5.2% — about 0.8 points short of target' |
| Treats peer 'held margins' claim as unverified and names peer figures to compile (normalised margin, indexation practice) before claiming internal cause | yes | 'Are the two listed peers' margins actually holding, on a comparable (normalised) basis, and what are their contract-indexation practices? ... The CFO's claim is unverified' |
| No euro counted twice (consistent price/volume treatment on same contracts) | yes | 'Action plan (reconciled, no double counting)'; contract mix check ties exactly to blended price (0.60×4.00+0.40×4.125=4.05) used consistently across bridge and tranche analysis |
| Does not propose an across-the-board cost cut before diagnosis, or driver/sorter cuts without addressing productivity/service | yes | 'An across-the-board cost-cutting programme would target the smallest piece of the problem'; productivity action is framed as 'Recover driver productivity... (routing, sortation)' with risk note 'None of the actions above reduce service capability' |
| Does not invent peer margins or industry wage data | yes | Peer margins are explicitly flagged as unverified/open question rather than asserted; wage-rate math (1.60, 9%, 18.0, 17.6) is derived from stated data-pack figures, not invented industry benchmarks |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

I worked this as a profitability-turnaround quick case and saved the answer page to `case-profitability-turnaround-kestrel.md`. Here it is in full:

# Profitability turnaround: Kestrel Logistics parcel division — what explains the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore at least 6% by 2027?

**Answer:** This is a contract-pricing problem, not an overhead problem. Fixed cost explains only ~6% of the EBIT drag. Variable cost per parcel rose 9.7% (mostly the 9% wage settlement, plus a driver-productivity slip and fuel inflation) while blended price per parcel rose only 1.25% — because the three-year contracts covering 60% of volume, signed in 2023, carry no fuel or wage indexation and have not moved. That locked tranche alone cost €3.9m of EBIT (1.85 margin points) in 2025. Repricing it at its H1 2026 renewal to at least match the already-repriced annual tier, plus recovering driver productivity, gets margin to roughly 5.2% on 2025 run-rate economics — about 0.8 points short of the Board's 6% target. Closing that last 0.8 points needs one more lever (stretch pricing above parity, verified procurement savings, or fixed-cost discipline), none of which can be sized precisely from this data pack alone.

**Confidence:** Medium. The profit bridge is exact arithmetic and reconciles fully to the reported 8.0%→2.5% move. The plan's ability to clear 6% by 2027 rests on three unverified items — peer pricing power, the next wage settlement, and renewal execution.

**Liquidity check:** Not at risk near-term (cash covers ~9 months of fixed cost, vs. a 13-week trigger). Covenant headroom is thin: net debt/EBITDA is 3.10x against a 3.5x limit — only ~€1.6m (≈11%) of further EBITDA decline before breach.

## Profit bridge, 2023→2025 (reconciles exactly)

| Driver | Effect (€m) |
|---|---|
| **EBIT 2023** | **16.00** |
| Volume (+2.0m parcels) | +2.20 |
| Price (+€0.05/parcel blended) | +2.60 |
| Variable cost/parcel (+€0.28) | **−14.56** |
| — labour (+€0.18/parcel: 80% wage rate, 20% productivity) | (−9.36) |
| — fuel (+€0.08/parcel) | (−4.16) |
| — subcontractors (+€0.02/parcel) | (−1.04) |
| Fixed cost (+€1.0m) | −1.00 |
| **EBIT 2025** | **5.24** (2.49% margin) |

**Contract mix check:** 60%×€4.00 + 40%×€4.125 = €4.05 exactly — ties to the reported blended price. The 60% tranche's lack of indexation cost €3.9m of EBIT (1.85 margin points) in 2025 alone, versus simply matching the already-repriced 40% tier.

## Action plan

| Action | EBIT effect | Confidence | Timing |
|---|---|---|---|
| Reprice 60% tranche to parity (€4.125) + add indexation, at H1 2026 renewal | +€3.9m | High | H1 2026 |
| Stretch pricing above parity (~€4.25-4.30) | +€1.5-2.3m | Low — needs peer verification | H1 2026 |
| Driver productivity recovery to 18.0/hr | +€1.0-1.9m | Medium | through 2027 |
| Fuel/subcontractor procurement rebid | +€1.5-2.9m | Low — no benchmark data | 2026-27 |
| Fixed-cost discipline (hold ~€40m flat) | +€0.5-1.0m | Medium | 2026-27 |
| **Total** | **+€8.4-11.9m** vs. **+€7.4m required** | | |

The two high-confidence items alone get to ~5.2% margin — 0.8 points short. Closing the last mile needs at least one lower-confidence lever, which is why this isn't yet a locked plan.

**Key open questions:** verify the peer "held margins" claim (unverified, from the CFO only); confirm next wage-agreement timing; get fuel/subcontractor rate-vs-volume detail; confirm renewal timing/one-off costs for the 60% tranche. Full detail and assumptions table are in the saved file.


## Files in work dir after run

- case-profitability-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-profitability-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics parcel division — what explains the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore at least 6% by 2027?

**Answer:** This is a contract-pricing problem, not an overhead problem. Fixed cost explains only ~6% of the EBIT drag. Variable cost per parcel rose 9.7% (mostly the 9% wage settlement, plus a driver-productivity slip and fuel inflation) while blended price per parcel rose only 1.25% — because the three-year contracts covering 60% of volume, signed in 2023, carry no fuel or wage indexation and have not moved. That locked tranche alone cost €3.9m of EBIT (1.85 margin points) in 2025. Repricing it at its H1 2026 renewal to at least match the already-repriced annual tier, plus recovering driver productivity, gets margin to roughly 5.2% on 2025 run-rate economics — about 0.8 points short of the Board's 6% target. Closing that last 0.8 points needs one more lever (stretch pricing above parity, verified procurement savings, or fixed-cost discipline), none of which can be sized precisely from this data pack alone.

**Confidence:** Medium. The profit bridge below is exact arithmetic and reconciles fully to the reported 8.0%→2.5% move (high confidence). The plan's ability to clear 6% by 2027 rests on three unverified items — peer pricing power, the next wage settlement, and renewal execution — so the last mile of the plan is lower confidence.

**Liquidity check:** Not at risk in the near term — cash covers ~9 months of fixed cost, well above the 13-week acute-risk trigger. Covenant headroom is thin, though: net debt/EBITDA is 3.10x against a 3.5x limit, leaving only ~€1.6m (≈11%) of further EBITDA decline before breach. Safe today; re-check specifically through the H1 2026 renewal window, where a rocky negotiation or short-term volume loss could compress EBITDA before the plan's gains land.

## Profit bridge, 2023 to 2025

Check: Revenue 2023 = 50.0m × €4.00 = €200.0m; EBIT = €200.0m − (50.0m×€2.90) − €39.0m = €16.0m → 8.0% margin. Revenue 2025 = 52.0m × €4.05 = €210.6m; EBIT = €210.6m − (52.0m×€3.18) − €40.0m = €5.24m → 2.49% margin (≈2.5%, as given). Both tie to the CFO's stated figures.

| Driver | Effect (€m) | Basis |
|---|---|---|
| **EBIT 2023** | **16.00** | 50.0m parcels × (€4.00 − €2.90) − €39.0m |
| Volume (+2.0m parcels, at 2023 contribution of €1.10/parcel) | +2.20 | (52.0−50.0) × (4.00−2.90) |
| Price (+€0.05/parcel blended, on 52.0m parcels) | +2.60 | (4.05−4.00) × 52.0 |
| Variable cost per parcel (+€0.28/parcel, on 52.0m parcels) | **−14.56** | (3.18−2.90) × 52.0 |
| — of which labour (+€0.18/parcel) | (−9.36) | split below |
| — of which fuel (+€0.08/parcel) | (−4.16) | (0.78−0.70) × 52.0 |
| — of which subcontractors (+€0.02/parcel) | (−1.04) | (0.62−0.60) × 52.0 |
| Fixed cost (+€1.0m) | −1.00 | 40.0 − 39.0 |
| **EBIT 2025** | **5.24** | reconciles exactly: 16.00+2.20+2.60−14.56−1.00 = 5.24 |

**Labour split (rate vs. productivity), using the wage-agreement and driver-hour data:**
Implied 2023 wage rate = €1.60/parcel × 18.0 parcels/driver-hour = €28.80/driver-hour. At +9% (2023→2025), 2025 wage rate = €31.39/driver-hour. At unchanged productivity (18.0), that alone would push labour cost to €1.744/parcel (+€0.144). Actual 2025 labour cost is €1.78/parcel, so the extra €0.036/parcel comes from productivity falling 18.0→17.6 parcels/driver-hour (−2.2%).
- Wage-rate effect: −€0.144 × 52.0m = **−7.49m** (80% of the labour drag; contractual, not easily reversible before the next wage round)
- Productivity effect: −€0.036 × 52.0m = **−1.87m** (20% of the labour drag; operationally addressable)

**Net reading of the negative drivers (−15.56m before the offsetting +4.80m of volume and price):** fixed cost is only **6%** of the drag (1.00/15.56); labour is **60%** (9.36/15.56), fuel **27%** (4.16/15.56), subcontractors **7%** (1.04/15.56). An across-the-board cost-cutting programme would target the smallest piece of the problem.

## Where profit is lost: the contract tranche

| Tranche | Share of 2025 volume | Price/parcel | Price change vs. 2023 | Indexation | Renews |
|---|---|---|---|---|---|
| 3-year contracts signed early 2023 | 60% (31.2m parcels) | €4.00 | 0% | None (no fuel or wage clause) | H1 2026 |
| Annual contracts | 40% (20.8m parcels) | €4.125 | +3.1% | Repriced yearly | Ongoing |

Check: 0.60×4.00 + 0.40×4.125 = 2.40+1.65 = **€4.05**, exactly the reported 2025 blended price — the two tranches fully explain the blended figure.

**Cost of the non-indexed tranche:** had the 60% tranche instead carried the annual tier's rate (€4.125) in 2025, revenue would have been €0.125 × 31.2m = **€3.90m** higher — equivalent to **1.85 margin points**. This is the single largest, best-evidenced lever in the plan, and it is purely a contract-renewal question, not a cost or volume question.

## Action plan (reconciled, no double counting)

Base case holds 2025 volume (52.0m parcels) and 2025 variable-cost-per-parcel flat as the 2026-27 starting point (see Assumptions) — i.e., this sizes the identified levers, not a full 2027 forecast with further organic drift.

| Action | EBIT effect (base) | Range | Confidence | Timing | Owner |
|---|---|---|---|---|---|
| Reprice the 60% fixed tranche to at least the current annual rate (€4.125) + add fuel/wage indexation clauses, at H1 2026 renewal | +€3.9m | — (parity is the floor, not a range) | High — arithmetic from two already-observed price points | H1 2026 renewal; full run-rate from 2027 | Commercial |
| Stretch: push the renewed tranche above parity toward full cost-inflation pass-through (~€4.25–4.30/parcel) | +€1.5–2.3m incremental | wide | Low — needs verified peer pricing power (see Open questions) | H1 2026 | Commercial / CFO |
| Recover driver productivity toward 18.0 parcels/driver-hour (routing, sortation) | +€1.0–1.9m (base €1.9m) | — | Medium — operational execution, no benchmark for achievable rate | 12–18 months into 2027 | Operations |
| Procurement: rebid fuel surcharge terms and subcontractor rates (2–4% of €72.8m combined 2025 spend) | +€1.5–2.9m | wide — assumption, no benchmark in pack | Low | 2026–27 | Procurement |
| Fixed-cost discipline: hold absolute fixed cost near €40m through 2027 despite volume growth | +€0.5–1.0m | — | Medium | 2026–27 | Finance / Ops |
| **Total, reconciled** | **+€8.4m to +€11.9m** (base ≈ **+€9.3m**) | vs. required **+€7.4m** (3.5 margin points, on a flat 2025 revenue base) to reach 6% | | | |

**The honest cut:** the two high-confidence items alone (contract parity repricing + productivity recovery) sum to **+€5.8m**, taking margin from 2.5% to roughly **5.2%** — about 0.8 points short of target. Closing that last stretch requires at least one of the three lower-confidence levers (stretch pricing, procurement, or fixed-cost discipline), each individually large enough to close it at its mid-to-high end. The plan should not be locked around any single one of these until the relevant data request below comes back.

## Risks and what would change the answer

1. If the H1 2026 renewal slips or customers churn rather than accept repricing, the largest lever (1.85–2.8 margin points) shrinks or slips past the February 2027 board date.
2. If the CFO's claim that peers "held their margins" turns out to be true and is driven by market-wide pricing discipline Kestrel can't match, the stretch-pricing lever is not available and the plan needs to lean more heavily on productivity, procurement and fixed cost — none of which closes the gap alone at the base case.
3. If the next wage agreement (date and size not in this pack) lands before or during the 2027 target window, part of the productivity-recovery gain is offset by renewed rate inflation.
4. Covenant headroom (≈€1.6m / 11% of EBITDA) is thin enough that a weak 2026 — e.g., a contentious renewal negotiation causing temporary volume loss — could breach covenant before the plan's benefits land in 2027; this should be modelled explicitly before the plan is finalised.
5. None of the actions above reduce service capability (sales coverage, on-time delivery) that the volume growth underpinning this plan depends on — worth re-confirming once the productivity and procurement actions are scoped in detail.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2026–27 variable cost per parcel holds at the 2025 level (€3.18) before actions | flat | No 2026-27 cost data in the pack | Further wage/fuel inflation would widen the gap beyond €7.4m |
| 2 | Volume holds at ~52.0m parcels through 2027 | flat | No volume forecast given | Material growth or decline changes both the revenue base and the euro-value of each margin point |
| 3 | The 60% tranche fully reprices and is at full run-rate by 2027 | full-year effect counted | Data pack states renewal is H1 2026 | A staggered or delayed renewal pushes part of the €3.9m benefit past the board date |
| 4 | Procurement savings of 2–4% on combined 2025 fuel + subcontractor spend (€72.8m) are achievable | €1.5–2.9m | Generic rebid-savings assumption — not sourced from the data pack | A real cost benchmark could show this is much larger or much smaller, or already near best-practice |
| 5 | Fixed cost can be held flat in absolute terms through 2027 despite volume growth | +€0.5–1.0m vs. a scale-with-volume counterfactual | No fixed-cost plan given | Capex or site decisions not in this pack could force fixed cost up regardless |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Are the two listed peers' margins actually holding, on a comparable (normalised) basis, and what are their contract-indexation practices? | The CFO's claim is unverified; it decides whether this is Kestrel-specific (fixable by Kestrel's own actions) or market-wide (caps how much stretch pricing is realistic) | Commercial/finance, compiling peers' annual reports | Directly changes the confidence and size of the "stretch pricing" lever (+€1.5–2.3m) |
| When does the next wage agreement fall, and at what expected increase? | Determines whether labour-rate inflation resumes before the 2027 target | HR | Could offset part of the productivity-recovery gain (+€1.0–1.9m) |
| Is the fuel cost increase driven by tariff or consumption, and the subcontractor increase by rate or volume-mix shift to subcontracted routes? | Needed to size the procurement lever with real data instead of a generic assumption | Operations / procurement | Narrows the €1.5–2.9m range to a specific, defensible figure |
| What one-off costs (discounts to retain volume, renegotiation/implementation cost) are expected at the H1 2026 renewal, and what is the risk of volume loss? | Could reduce the net EBIT effect of the largest lever (+€3.9m) | Commercial | Timing and net size of the single biggest action in the plan |
| Do all three-year contracts renew simultaneously in H1 2026, or do they stagger across the year/into 2027? | Affects how much of the €3.9m benefit is at full run-rate by the 2027 target date vs. still phasing in | Commercial | Timing of the plan's largest benefit |

## Specialists and review

No legal, tax or regulatory question is raised by this data pack. The commercial team should have contract/legal review the renewal terms (indexation clause drafting) before the H1 2026 negotiations; finance should re-run the covenant headroom check once a renewal and wage-agreement timeline is confirmed.

