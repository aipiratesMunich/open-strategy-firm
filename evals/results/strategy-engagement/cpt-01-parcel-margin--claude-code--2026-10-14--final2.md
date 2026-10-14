# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge 2023→2025 sums to -10.76 and names variable cost per parcel as largest driver | yes | Volume +2.20, Price +2.60, Variable cost per parcel -14.56, Fixed cost -1.00 ... EBIT 2025 +5.24; variable cost per parcel is the largest-magnitude driver and text says it 'accounts for most of the €10.76m EBIT decline.' |
| Splits variable cost into labour/fuel/subcontractors and labour into wage/productivity effects | yes | 'labour -9.36 ... ≈ −7.3 from the 9% wage award, ≈ −2.0 from parcels/driver-hour falling 18.0→17.6'; 'fuel -4.16'; 'subcontractors -1.04' |
| Root cause stated in one sentence first with unit cost +0.28/9.7% and price +0.05/1.25% contrast, tied to 60% unindexed fixed-price volume | NO | Opening sentence: 'This is a contract-terms problem... 60% of 2025 volume is frozen at the 2023 price of €4.00 with no cost indexation, while variable cost per parcel rose 9.7%' — omits the blended price-rise figure (€0.05/1.25%) entirely; that figure only appears later in the bridge table disconnec |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~€1.6m EBITDA) as constraint on one-off costs/timing | yes | 'Net debt/EBITDA = €44m / €14.2m = 3.10x against a 3.5x covenant: only ~11% more EBITDA decline (to €12.6m) before breach ... phase any one-off restructuring or renegotiation costs so they don't push EBITDA through the covenant during the 2026 transition.' |
| Action plan as one reconciled bridge with EBIT effect/range/one-off cost/timing/owner/confidence per action; renewal action timed to 2026 window with volume risk shown | yes | Table columns include all required fields per row (e.g. 'Reprice + index the 60% fixed book at H1 2026 renewal ... +5.6 ... +2.8 to +10.3 ... Renewal negotiation, H1 2026 ... Commercial/Sales ... Low–Medium'); risk section calls for a 'pricing/win-rate analysis on the renewal'. |
| Actions reach or show remaining gap to ~€12.6m EBIT (6%) by 2027 | yes | 'Required improvement ... ≈ +€7.4m ... Base case (+€8.6m ...) lands at ≈6.3–6.5%; the low end of the range (+€3.7m) lands at only ≈4.2% — a full miss.' |
| Treats peer margin claim as unverified and names peer figures to compile before claiming internal cause | yes | 'This is currently an unverified client claim, not evidence'; Open questions row: 'Compiled peer margins, indexation practice and cost/parcel for the two listed competitors the CFO mentioned.' |
| No euro counted twice | yes | Bridge ties exactly to reported EBIT (16.0→5.24) and action plan explicitly stated 'reconciled, no double counting — each line costed against the unchanged 2025 run-rate.' |
| Must not propose across-the-board cost cut before diagnosis or cuts to drivers/sorters without addressing productivity/service | yes | 'Targeted overhead efficiency (fixed cost grew in line with volume — do not cut broadly)'; productivity action targets recovery, not headcount cuts. |
| Must not invent peer margins or industry wage data | yes | Peer margins explicitly flagged as unverified/open question rather than invented; wage figures used (9% award) are sourced from the data pack, not invented industry data. |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

I worked this as a quick-case profitability turnaround and saved the answer page to `case-profitability-turnaround-kestrel.md`. Headline for the CFO:

**This is a contract-terms problem, not a cost or market problem.** The profit bridge ties exactly to the reported 8.0%→2.5% margin fall (€16.0m→€5.24m EBIT): a +€2.2m volume gain and +€2.6m price gain were swamped by a −€14.56m variable-cost rise (mostly labour, split ~80/20 between the 9% wage award and a 2.2% productivity loss) and −€1.0m fixed-cost growth. The root cause sits in the contract book: 60% of volume is frozen at the 2023 price of €4.00 with zero indexation, so contribution per parcel there collapsed 25% (€1.10→€0.82); even the repriced 40% book only passed through ~45% of the cost increase.

The lever is the H1 2026 renewal of that 60% book. Base-case repricing + indexation there, plus recovering lost driver productivity, delivers **+€8.6m EBIT** (range +€3.7m to +€16.1m) against a **required ~€7.4m** to hit 6% margin — base case lands at **~6.3–6.5%**, but the low end only reaches **~4.2%**. That spread is almost entirely the renewal-pricing outcome, which this data pack can't settle.

Liquidity is safe (9 months cash runway) but covenant headroom is thin (3.10x vs. 3.5x — only ~11% more EBITDA decline before breach), so any renegotiation/restructuring one-offs need careful sequencing.

Biggest open items flagged in the doc: compiled peer margins (currently just an unverified CFO claim), contract-level profitability within the 60% book, and a renewal pricing/win-rate test — that last one determines whether the plan actually clears 6% by 2027.


## Files in work dir after run

- case-profitability-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-profitability-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics, parcel division — what caused the fall from 8.0% to 2.5% EBIT margin since 2023, and which actions restore ≥6% by 2027?

**Answer:** This is a contract-terms problem, not a cost or market problem: 60% of 2025 volume is frozen at the 2023 price of €4.00 with no cost indexation, while variable cost per parcel rose 9.7% — that one bucket alone accounts for most of the €10.76m EBIT decline. Repricing and indexing that book at its H1 2026 renewal, plus recovering lost driver productivity, is a base-case +€8.6m EBIT (range +€3.7m to +€16.1m), against a required gap of ~€7.4m — base case reaches **~6.3–6.5% margin in 2027**, but the low end of the range reaches only **~4.2%**. The plan's success turns almost entirely on the price Kestrel can actually negotiate at the 2026 renewal, which this data pack cannot tell us.

**Confidence:** Medium — the profit bridge ties out exactly to the reported margins (a good sign), but the single largest lever (renewal pricing) rests on a negotiation outcome not yet tested, and the CFO's peer claim ("peers held their margins") is not yet compiled. Confidence would rise with a renewal pricing test and compiled peer data; it would fall if peers turn out to show the same decline (implying an industry-wide cost shock, not a Kestrel-specific contracting failure).

**Liquidity check:** Safe but with thin headroom — not a near-term crisis, but it constrains how the turnaround can be sequenced. Net debt/EBITDA = €44m / €14.2m = **3.10x** against a 3.5x covenant: only ~11% more EBITDA decline (to €12.6m) before breach. Cash covers ~9 months of fixed cost, which is a comfortable runway. Net: proceed with the structural plan, but phase any one-off restructuring or renegotiation costs so they don't push EBITDA through the covenant during the 2026 transition.

## Profit bridge, 2023 to 2025 (ties exactly to the reported €16.0m → €5.24m EBIT)

| Driver | Effect (€m) | How computed |
|---|---|---|
| EBIT 2023 | **+16.00** | 50.0m parcels × (€4.00 − €2.90) − €39.0m fixed = €16.0m (8.0% of €200.0m revenue) |
| Volume (+2.0m parcels at 2023 contribution) | **+2.20** | (52.0−50.0) × (4.00−2.90) |
| Price (+€0.05/parcel on 2025 volume) | **+2.60** | (4.05−4.00) × 52.0 |
| Variable cost per parcel (+€0.28 on 2025 volume) | **−14.56** | −(3.18−2.90) × 52.0, of which: |
| — labour (+€0.18/parcel) | −9.36 | ≈ −7.3 from the 9% wage award, ≈ −2.0 from parcels/driver-hour falling 18.0→17.6 (≈2.2%) |
| — fuel (+€0.08/parcel) | −4.16 | not decomposable further with this data (no tariff vs. consumption split) |
| — subcontractors (+€0.02/parcel) | −1.04 | no further detail available |
| Fixed cost (+€1.0m) | **−1.00** | roughly tracks the +4% volume growth; not the main story |
| **EBIT 2025** | **+5.24** | 52.0m × (4.05−3.18) − €40.0m = €5.24m (2.49% of €210.6m revenue, reported as 2.5%) |

Hypothesis check: *input-cost increases were not passed through in contracts without indexation* — **confirmed**, and it is the dominant driver (price+cost effects net to −€11.96m before volume and fixed cost; price recovered only €2.60m of a €14.56m cost increase). *Labour cost per unit rose faster than price* — **confirmed**, and splits roughly 80/20 between the wage award and the productivity loss. *Fixed cost grew faster than revenue* — **killed**: fixed cost (+2.6%) grew in line with volume (+4%), so it is not a primary cause; an across-the-board overhead cut would be the wrong move here.

## Where profit is lost: the two contract books behave very differently

| Book | Share of 2025 volume | Price/parcel | Var. cost/parcel | Contribution/parcel | vs. 2023 (€1.10) | Trend / renewal |
|---|---|---|---|---|---|---|
| 3-year fixed contracts, signed early 2023 | 60% (31.2m parcels) | €4.00 (unchanged since 2023) | €3.18 | **€0.82** | **−25%** | No indexation; cost increases have gone straight to the bottom line. Renews H1 2026 — the one real lever. |
| Annual contracts, repriced | 40% (20.8m parcels) | €4.125 | €3.18 | **€0.945** | −14% | Repriced, but only passed through €0.125 of the €0.28 cost increase (≈45%) — margin eroded even in the "good" book. |
| **Blended 2025** | 100% | €4.05 | €3.18 | **€0.87** | −21% | 0.6×4.00 + 0.4×4.125 = 4.05, ties to the reported average exactly. |

Hypothesis check: *a small number of contracts/sites cause most of the decline* — **not testable at this granularity**; the data pack only distinguishes two buckets, not individual contracts. This is the first follow-up analysis to run (see Open questions).

Internal vs. market: the CFO states two listed peers "held their margins" in 2024–25 — if confirmed, this **supports** the internal/contractual diagnosis (the problem is Kestrel's own indexation-free contracts, not an industry-wide cost shock everyone is absorbing). This is currently an unverified client claim, not evidence — see Open questions.

## Action plan (reconciled, no double counting — each line costed against the unchanged 2025 run-rate)

| Action | EBIT effect, base case (€m, 2027 run-rate) | Range (€m) | One-off cost / timing | Owner | Confidence |
|---|---|---|---|---|---|
| Reprice + index the 60% fixed book at H1 2026 renewal (target contribution €0.82 → €0.91–1.15/parcel, i.e. price ≈ €4.09–4.33) | **+5.6** | +2.8 to +10.3 | Renewal negotiation, H1 2026; full-year effect from 2027 | Commercial/Sales | Low–Medium — depends on customer price sensitivity and competitor pricing, neither known from this pack |
| Recover driver productivity from 17.6 back to ≈18.0 parcels/driver-hour (routing/sorting improvements) | **+2.0** | +0.9 to +2.8 | Capex/opex for the program not yet costed | Operations | Medium |
| Fuel and subcontractor cost management (surcharge/rate renegotiation) | **+0.5** (ASSUMPTION, weak evidence) | 0 to +1.5 | Not sized — no tariff/consumption or rate-card data in this pack | Procurement | Low |
| Targeted overhead efficiency (fixed cost grew in line with volume — do not cut broadly) | **+0.5** (ASSUMPTION, weak evidence) | 0 to +1.5 | No overhead benchmark available yet | Finance/Ops | Low |
| **Total, reconciled** | **+8.6** | **+3.7 to +16.1** | | | |

Required improvement to reach 6% margin at roughly flat 2025 revenue: **≈ +€7.4m** (0.06 × €210.6m − €5.24m). Base case (+€8.6m, revenue rising to ≈€216m with the repricing) lands at **≈6.3–6.5%**; the low end of the range (+€3.7m) lands at only **≈4.2%** — a full miss. The gap between base and downside cases is almost entirely the renewal-pricing lever, which is the one number in this plan that is a negotiation outcome, not an internal control.

## Risks and what would change the answer

1. If the 2026 renewal lands below the middle of the price range (€4.00–4.09), the plan misses 6% by 2027 even with every other action delivered — run a pricing/win-rate analysis on the renewal *before* the Feb 2027 board meeting, not after.
2. If compiled peer data shows competitors' margins also fell, the diagnosis shifts from "fix our contracts" toward a market-wide input-cost problem, which changes both the target and the credible timeline.
3. If contract-level data shows the 25%-margin-decline fixed book is itself concentrated in a few large accounts, the right move may be exit/renegotiate those specific accounts rather than a blanket renewal ask across the whole 60%.
4. If any one-off renegotiation or restructuring cost lands in 2026 and dents EBITDA by more than ~€1.6m in-year, the net debt/EBITDA covenant (3.5x) is at risk — sequence actions to avoid this.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Volume flat 2025→2027 | 52.0m parcels | No growth/decline guidance in the data pack | Material volume gain or loss changes both the revenue base and the achievable scale of every action |
| 2 | Labour cost/parcel is driven only by wage rate and parcels/driver-hour | Reproduces reported €1.78 almost exactly from +9% wages and 18.0→17.6 productivity | Only these two labour metrics are in the pack | Other labour-mix shifts (e.g. driver vs. sorter headcount mix) would change the 80/20 split |
| 3 | No further un-indexed wage/fuel inflation baked into the "do-nothing" 2025→2027 baseline | Flat beyond 2025 levels except where an action addresses it | Not stated in the pack | Continued 2023–25-style inflation before the 2026 indexation takes effect would widen the gap further |
| 4 | Renewal executes in H1 2026 with full-year effect by 2027 | As stated in the pack | Commercial team input | A slipped renewal timeline pushes recovery past the Feb 2027 board date |
| 5 | Fuel/subcontractor and overhead actions sized at €0.5m each, flagged weak evidence | ASSUMPTION, wide range 0–1.5m each | No tariff/consumption, rate-card, or overhead-benchmark data provided | A fuel or overhead benchmark study would replace this placeholder with a real number |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What price can Kestrel actually realize at the H1 2026 renewal (customer switching cost, competitor pricing, notice periods)? | This is the single largest and most uncertain lever (€2.8m–10.3m swing) | Commercial/sales leadership, via a pricing/win-rate analysis | Decides whether 2027 lands at ~6.3–6.5% (base) or ~4.2% (downside) |
| Compiled peer margins, indexation practice and cost/parcel for the two listed competitors the CFO mentioned | Confirms whether the cause is Kestrel-specific contracting (fixable) or industry-wide (structural) — currently just an unverified client claim | Strategy/commercial team, from competitors' annual reports | Could shift the diagnosis and the credible 2027 target |
| Contract-level profitability within the 60% fixed-price book (is the loss concentrated in a few large accounts?) | Only two buckets are visible here; individual loss-makers may warrant exit rather than blanket repricing | Finance business partner / commercial team | Changes Action 1 from a blanket renewal ask to a targeted exit/renegotiate list |
| Fuel cost breakdown: tariff vs. consumption, and whether contracts have (or could have) a fuel surcharge mechanism | Currently unsized placeholder (€0–1.5m) | Procurement / fuel desk | Replaces an assumption with a real number for Action 3 |
| Overhead/fixed-cost benchmark vs. peers or Kestrel's own best site | Fixed cost grew roughly in line with volume — avoid an across-the-board cut without evidence of real bloat | Finance/Ops | Replaces an assumption with a real number for Action 4, or kills the action |
| Capex/opex cost of the driver-productivity recovery program | Not costed in this pack | Operations | Changes Action 2's net effect and payback timing |
| Full 13-week cash forecast (only static ratios are available here) | Confirms the "safe" liquidity read under this plan's actual phasing | Treasury | Could force resequencing if a near-term dip appears that the static ratios don't show |

