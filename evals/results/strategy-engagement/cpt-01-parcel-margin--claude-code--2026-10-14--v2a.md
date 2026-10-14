# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge from 2023 to 2025 by driver sums to -10.76 and names variable cost per parcel as largest driver | yes | Bridge rows +2.20+2.60-7.34-2.02-4.16-1.04-1.00 = -10.76; so-what states 'The decline is almost entirely variable-cost inflation (−14.56m, of which labour is −9.36m)' |
| Splits variable cost into labour, fuel, subcontractors; labour into wage and productivity effects | yes | Table rows: 'labour, wage rate (+9% wage agreement) −7.34', 'labour, productivity (18.0→17.6) −2.02', 'fuel −4.16', 'subcontractors −1.04' |
| Root cause stated in one sentence first with unit cost rise (EUR0.28/9.7%) AND price rise (EUR0.05/1.25%) and 60% fixed-price/no-indexation cause | NO | Headline/answer sentence only states: 'they absorbed the full EUR 0.28/parcel (9.7%) rise in variable cost with no price offset' — the EUR0.05/1.25% price-rise figure is never paired with the unit-cost figure in the lead root-cause sentence, only appearing later buried in a Step 2 table row ('+1.25% |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~EUR1.6m EBITDA) as constraint on one-off costs/timing | yes | 'net debt/EBITDA is 3.10x (44m/14.2m) against a 3.5x cap, an EBITDA buffer of only ~EUR 1.6m... Any one-off renegotiation, severance or restructuring cost in the 2026 plan should be stress-tested against this buffer' |
| Action plan in one reconciled bridge with EBIT effect, range, one-off cost, timing, owner, confidence per action; indexation timed to 2026 renewal with volume risk shown | yes | Action table has all six columns filled for each action; indexation row 'H1 2026; run-rate from FY2027' with 'volume-loss risk, unquantified' and Risk #1 on customer resistance |
| Actions reach or show remaining gap to ~EUR12.6m EBIT (6%) by 2027 | yes | '6% margin on 2025 revenue... requires EBIT of EUR 12.64m... gap of EUR 7.40m' and total actions '+10.2m (range +6.2m to +15.2m)' shown against the gap |
| Treats peers 'held margins' as unverified and names peer figures to compile before claiming internal cause | yes | 'CFO's claim, not compiled' and Open questions row: 'Compiled peer EBIT margins (2023–2025) and their contract indexation practice' |
| No euro counted twice | yes | Trap check: 'All actions sit in one bridge, no euro counted twice — each action maps to a distinct cost/price driver from 3a.' |
| Must not propose across-the-board cost cut, or cuts to drivers/sorters without addressing productivity/service | yes | 'No action cuts capability the recovery depends on — fixed cost/overhead is explicitly not cut... no sales-coverage or service-quality cuts proposed' |
| Must not invent peer margins or industry wage data | yes | Peer margins explicitly flagged unverified/not compiled; wage figure (+9%) sourced from stated wage agreement, not fabricated peer/industry data |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

Saved the full quick-case workup (steps 1–4 plus the CFO answer page) to `case-turnaround-kestrel.md`. Headline:

**Root cause isn't volume or overhead** — both moved in Kestrel's favor. It's the 60% of volume locked into non-indexed 3-year contracts (EUR 4.00 flat, no wage/fuel escalator) that absorbed the full 9.7% rise in variable cost with zero price offset. The bridge from EBIT 16.0m (8.0%) in 2023 to 5.24m (2.5%) in 2025 ties out exactly: +2.2m volume, +2.6m price, −7.34m wage rate, −2.02m labour productivity, −4.16m fuel, −1.04m subcontractors, −1.0m fixed cost.

**Action plan** (reconciled, one bridge): re-index the 60% book at the H1 2026 renewal (+6.1m, range 4.4–8.7m), driver-productivity program (+1.9m), fuel surcharge/hedge (+1.5m, data gap), subcontractor mix (+0.7m) — totaling **+10.2m (range 6.2–15.2m)** against a **required +7.4m** to hit 6% margin. Base case clears it; pessimistic case doesn't — the plan leans heavily on one lever (customer acceptance of indexation).

**Liquidity:** safe for now (9-month cash runway, 3.10x vs 3.5x covenant), but covenant headroom is thin (~11.5% EBITDA buffer) — worth stress-testing against the plan's one-off renegotiation/severance costs.

Biggest open gaps flagged in the doc: peer margins are unverified (CFO's claim, not compiled), no customer-level profitability within the two contract buckets, no fuel tariff/consumption split, and labour-law/contract-counsel/treasury review needed before this goes to the board.


## Files in work dir after run

- case-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-turnaround-kestrel.md

# Profitability turnaround: Kestrel Logistics, parcel division — quick case

*Fictional company; all figures invented for this exercise.*

## Step 1: Sharpen the question

**Sharpened question:** What explains the fall from 8.0% to 2.5% parcel-division EBIT margin from 2023 to 2025, and which actions restore at least 6% EBIT margin by 2027?

- **Cash at risk in 13 weeks?** No. Cash covers ~9 months of fixed cost (~EUR 30m), well above a 13-week (~3-month) need. Checked separately in the liquidity line below.
- **Last good year / target:** 2023 (8.0% margin) → target 6.0% by 2027 (board meeting February 2027).
- **Cure already chosen?** None — CFO states "we have not picked a cure." Kept open; not pre-framed as a cost programme.
- **Do peers suffer the same?** CFO says two listed peers "held their margins" in 2024–2025, but figures are **not compiled** — unverified claim, treated as a hypothesis, not a fact.
- **Contracts and indexation:** 60% of 2025 volume sits on 3-year contracts signed early 2023 at a flat EUR 4.00/parcel with **no fuel or wage indexation**, renewing H1 2026. 40% is on annual contracts, repriced to ~EUR 4.125 by 2025.
- **Loss-making unit fix/sell/close?** Not applicable — this is a single division, not a sell/close decision.

## Step 2: Issue tree

| Branch | Hypothesis | Status after data pack |
|---|---|---|
| Liquidity | Cash covers ≥13 weeks without new measures | **Confirmed** — ~9 months runway; see liquidity check |
| Revenue: volume and mix | Volume/mix explain <10% of the decline | **Confirmed, and reversed sign** — volume growth (+2.0m parcels) is a +EUR 2.2m tailwind, not a cause |
| Revenue: price and terms | Cost increases were not passed through in contracts without indexation | **Confirmed** — 60% of volume had zero price indexation for 2 years while unit cost rose 9.7% |
| Cost: variable per unit | Labour (and other variable) cost per unit rose faster than price | **Confirmed** — variable cost/parcel +9.7% (2.90→3.18) vs price +1.25% (4.00→4.05) |
| Cost: fixed | Overhead grew faster than revenue | **Killed** — fixed cost +2.6% (39.0m→40.0m) vs revenue +5.3%; fixed cost per parcel fell (0.78→0.769) |
| Portfolio | A few contracts cause most of the decline | **Reshaped** — only two contract buckets in the data (60%/40%); the non-indexed 60% bucket causes the bulk of the decline (see Step 3b). True customer/site-level concentration not testable with data given |
| Internal vs market | Cause is internal; peers held margin | **Open** — CFO claim unverified; peer figures not compiled |
| Delivery | Actions reach 6% by 2027 after one-off costs and notice periods | **Open / provisional** — see Step 3f; depends on 2026 renewal outcome |

## Step 3: Deciding analyses

### 3a. Profit bridge, 2023 → 2025

Checked against reported change: EBIT 2023 = 50.0m × (4.00 − 2.90) − 39.0m = **EUR 16.00m** (8.0% of EUR 200.0m revenue). EBIT 2025 = 52.0m × (4.05 − 3.18) − 40.0m = **EUR 5.24m** (2.5% of EUR 210.6m revenue). Reported decline: **−EUR 10.76m**. Labour is split into wage-rate and productivity (usage) effects per the +9% wage agreement and the drop from 18.0 to 17.6 parcels per driver-hour; the split sums to the full EUR 0.18/parcel labour increase, so the bridge below ties out exactly.

| Driver | Effect (EUR m) |
|---|---|
| EBIT 2023 | +16.00 |
| Volume (+2.0m parcels × 2023 contribution of EUR 1.10) | +2.20 |
| Price and terms (price rise on the 40% repriced book only) | +2.60 |
| Variable cost per unit — labour, wage rate (+9% wage agreement) | −7.34 |
| Variable cost per unit — labour, productivity (18.0→17.6 parcels/driver-hour) | −2.02 |
| Variable cost per unit — fuel | −4.16 |
| Variable cost per unit — subcontractors | −1.04 |
| Fixed cost | −1.00 |
| **EBIT 2025** | **+5.24** |

**So-what:** Volume is not the problem — it is a small tailwind. Fixed cost is not the problem — it fell slightly per parcel. The decline is almost entirely variable-cost inflation (−14.56m, of which labour is −9.36m) that was priced into contracts covering only 40% of volume. Hypothesis "cost increases not passed through" → **confirmed**; hypothesis "fixed cost grew faster than revenue" → **killed**.

### 3b. Where profit is lost (by contract type — the only segmentation the data supports)

| Bucket | Share of 2025 volume | Price/parcel | Contribution/parcel (price − 3.18) | Contribution margin % | Change in contribution/parcel vs 2023 blended (1.10) |
|---|---|---|---|---|---|
| 3-year fixed, no indexation, signed early 2023 | 60% (31.2m) | EUR 4.00 | EUR 0.82 | 20.5% | **−0.28 (−25%)** — absorbed 100% of the cost increase |
| Annual, repriced | 40% (20.8m) | EUR 4.125 | EUR 0.945 | 22.9% | −0.155 (−14%) — partial pass-through |

**So-what:** Both buckets eroded, but the non-indexed 60% bucket eroded nearly twice as much per parcel. This is the single largest identifiable lever. (Note: variable cost per parcel is reported company-wide, not split by contract type; the table assumes the same unit cost applies to both buckets — flagged in Assumptions.)

### 3c. Price realisation

No list-to-pocket discount data exists for this B2B parcel book, so price realisation collapses to indexation coverage: the 60% fixed book realised **0% of the EUR 0.28/parcel cost increase**; the 40% annual book realised price growth of +3.1% (4.00→4.125) against variable cost growth of +9.7% over the same period — even the "repriced" book under-recovered cost inflation, by roughly two-thirds. Hypothesis reshaped: indexation gap is the dominant driver, but even annual repricing has not been keeping pace with cost.

### 3d. Cost benchmarks

**Provisional only.** No peer cost-per-parcel or normalized margin data is compiled. The CFO's "peers held margin" claim is unverified and must not be used to call this a market-wide (unfixable) problem or a Kestrel-specific (fully fixable) one. Internally, the division's own two buckets show identical unit cost (by data-pack construction), so there is no internal cost-benchmark gap to find with the data given — the gap is commercial (pricing/terms), not an operating-cost outlier, as far as current data shows.

### 3e. Unit economics

2025 blended contribution per parcel = 4.05 − 3.18 = EUR 0.87. Fixed cost per parcel = 40.0m / 52.0m = EUR 0.769. EBIT per parcel = EUR 0.10 (≈2.5% margin, ties to the P&L). **So-what:** the core per-parcel model is still positive but has almost no buffer — a further EUR 0.10/parcel cost shock or volume dip would push the division to breakeven or loss. This is a thin-margin business, not a broken one.

### 3f. Action plan value (reconciled, one bridge, no double counting)

Target sizing: 6% margin on 2025 revenue (EUR 210.6m) requires EBIT of **EUR 12.64m**; current EBIT is EUR 5.24m → **gap of EUR 7.40m**. (2027 revenue will differ with volume/price — this gap should be re-cut once a 2026–2027 volume/price forecast exists; see Open questions.)

| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Add wage + fuel indexation clauses to the 60% fixed-price book at H1 2026 renewal | +6.1m | +4.4m to +8.7m | Negotiation cost; risk of volume loss if customers push back — not quantified | Effective H1 2026; full run-rate from FY2027 | Commercial/Sales Director | Medium |
| Driver productivity programme (routing/scheduling) to restore 18.0 parcels/driver-hour | +1.9m | +1.5m to +2.5m | ASSUMPTION: EUR 1–2m capex/IT, needs ops sizing | 12–18 months | COO/Operations | Medium |
| Fuel surcharge clause or hedge, aligned to contract renewals | +1.5m (placeholder) | +0 to +3.0m | Unknown — no tariff/consumption data | Tied to 2026 renewal | Procurement/Commercial | Low (data gap) |
| Subcontractor cost / in-house mix review | +0.7m (placeholder) | +0.3m to +1.0m | Minimal | 6–12 months | Operations | Low |
| **Total, reconciled, no double counting** | **+10.2m** | **+6.2m to +15.2m** | | | | |
| **vs required gap** | **+7.4m** | | | | | |

**So-what:** The base case clears the gap (10.2m vs 7.4m required), but the low end of the range (6.2m) falls short. The plan should not rely on the indexation lever alone — it is necessary but, on its own at the pessimistic end (4.4m), insufficient.

## Step 4: Trap checks

- [x] Diagnosis came before any cost target; no across-the-board cut proposed.
- [x] Averages broken down — split into price/volume/cost-per-unit/fixed, and into the two contract buckets. Customer- or site-level breakdown within each bucket is **not possible with the data given** — carried to Open questions.
- [ ] Benchmarks normalised before claiming a gap — **not done**: peer figures are not compiled. Fix: do not state "internal cost problem" or "industry-wide problem" until peer data arrives; both labels are currently unverified.
- [x] All actions sit in one bridge, no euro counted twice — each action maps to a distinct cost/price driver from 3a.
- [~] One-off costs, notice periods, renewal dates in timing — renewal date (H1 2026) is in; exact notice periods and one-off severance/negotiation costs are not known. Flagged as Open question.
- [x] Liquidity checked separately from profitability — see below.
- [x] No action cuts capability the recovery depends on — fixed cost/overhead is explicitly *not* cut, since it is already efficient per parcel; no sales-coverage or service-quality cuts proposed.
- [x] Bridge sums exactly to the reported EBIT change (16.00 → 5.24); no unexplained plug.

---

# Profitability turnaround: Kestrel Logistics, parcel division — answer page for the CFO

**Answer:** The 8.0%→2.5% margin fall is not a volume or overhead problem — it is a commercial one: 60% of 2025 volume sits on 3-year contracts (signed early 2023, renewing H1 2026) with **zero wage or fuel indexation**, so they absorbed the full EUR 0.28/parcel (9.7%) rise in variable cost with no price offset, while fixed cost and volume both moved in Kestrel's favour. Re-indexing that book at the 2026 renewal, plus a driver-productivity programme and smaller fuel/subcontractor fixes, is sized at **+EUR 10.2m EBIT (range +6.2m to +15.2m)** against a **required +EUR 7.4m to reach 6% margin by 2027** — plausible, but concentrated in one lever and not yet proven out with customers.

**Confidence:** Medium — the profit bridge ties out exactly and the contract-indexation finding is solid, but (a) the single largest lever (indexation at 2026 renewal) depends on a customer negotiation outcome with no evidence yet on achievable pass-through, and (b) the "is this internal or market-wide" question is still open because peer margin and indexation data have not been compiled.

**Liquidity check:** Safe for the next 13 weeks — cash covers ~9 months of fixed cost. Covenant headroom is thinner than it looks: net debt/EBITDA is 3.10x (44m/14.2m) against a 3.5x cap, an EBITDA buffer of only ~EUR 1.6m (≈11.5%). Any one-off renegotiation, severance or restructuring cost in the 2026 plan should be stress-tested against this buffer before the plan is finalised — not at risk today, but not a lot of slack either.

## Profit bridge 2023 to 2025

| Driver | Effect |
|---|---|
| EBIT 2023 (8.0% of EUR 200.0m) | +EUR 16.00m |
| Volume (+2.0m parcels) | +EUR 2.20m |
| Price and terms (40% repriced book only) | +EUR 2.60m |
| Variable cost per unit — labour wage rate (+9% wage agreement) | −EUR 7.34m |
| Variable cost per unit — labour productivity (18.0→17.6 parcels/driver-hour) | −EUR 2.02m |
| Variable cost per unit — fuel | −EUR 4.16m |
| Variable cost per unit — subcontractors | −EUR 1.04m |
| Fixed cost | −EUR 1.00m |
| EBIT 2025 (2.5% of EUR 210.6m) | +EUR 5.24m |

## Where profit is lost

| Contract bucket | Revenue (2025) | Contribution margin | Trend vs 2023 | Action |
|---|---|---|---|---|
| 3-year fixed, no indexation (60% of volume) | EUR 124.8m | 20.5% | −0.28/parcel, 100% of cost rise unrecovered | Re-index at H1 2026 renewal |
| Annual, repriced (40% of volume) | EUR 85.8m | 22.9% | −0.155/parcel, partial pass-through | Tighten repricing formula at next renewal |

## Action plan

| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Wage + fuel indexation on the 60% fixed-price book, H1 2026 renewal | +6.1m | +4.4m to +8.7m | Negotiation cost; volume-loss risk, unquantified | H1 2026; run-rate from FY2027 | Commercial/Sales Director | Medium |
| Driver productivity programme (restore 18.0 parcels/driver-hour) | +1.9m | +1.5m to +2.5m | EUR 1–2m capex/IT (ASSUMPTION) | 12–18 months | COO/Operations | Medium |
| Fuel surcharge clause or hedge | +1.5m | +0 to +3.0m | Unknown | Tied to 2026 renewal | Procurement/Commercial | Low (data gap) |
| Subcontractor / in-house mix review | +0.7m | +0.3m to +1.0m | Minimal | 6–12 months | Operations | Low |
| **Total, reconciled, no double counting** | **+10.2m** | **+6.2m to +15.2m** | | | | |

Required to reach 6% margin on 2025 revenue base: **+EUR 7.4m**. Re-cut against actual 2026–2027 revenue once a volume/price forecast exists.

## Risks and what would change the answer

1. If customers resist indexation and ≥20% of the 60% book is lost or re-priced down at renewal, the lead action falls toward the low end (4.4m) and the plan misses the target without a second major lever.
2. If compiled peer data shows competitors' margins also fell, the cause is partly structural (industry-wide cost inflation) and the target or timeline may need revisiting with the board.
3. If one-off renegotiation or severance costs exceed ~EUR 1.6m in a single year, the EBITDA covenant (3.5x net debt/EBITDA) could be breached — sequence the plan to avoid this.
4. If productivity decline is structural (e.g., denser last-mile stops, smaller average parcel) rather than fixable by routing, the productivity lever shrinks or disappears.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2027 volume extrapolated from 2023–2025 trend | ~54.0m parcels | Linear extrapolation of +2.0m/2yr | Commercial forecast shows materially different volume |
| 2 | Indexation pass-through achieved at 2026 renewal | 70% base case | Typical negotiation outcome (not evidenced) | Actual renewal outcome known |
| 3 | Variable cost per parcel identical across both contract buckets | EUR 3.18 both | Data pack reports cost company-wide, not by contract type | Contract-type cost data becomes available |
| 4 | Productivity recoverable to 18.0 parcels/driver-hour via routing/scheduling investment | Base case, range 1.5–2.5m EBIT | No root-cause data on the productivity drop | Ops confirms the drop is structural (route density, parcel size mix) |
| 5 | Fuel lever sized at EUR 0–3m with no tariff/consumption data | Placeholder | No fuel rate or liters-per-parcel data in pack | Fuel tariff/consumption split is provided |
| 6 | Wage-rate vs productivity split of the labour increase | ~78% rate / 22% productivity | Back-solved from +9% wage agreement and 18.0→17.6 parcels/driver-hour, scaled to tie the reported 0.18/parcel increase exactly | More precise payroll data is provided |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Compiled peer EBIT margins (2023–2025) and their contract indexation practice | Determines if the cause is Kestrel-specific (fixable) or market-wide (structural) | CFO / competitive intelligence | Could lower or raise target feasibility and change the headline framing |
| Customer- or contract-level profitability within the 60%/40% buckets | The data pack only gives two aggregate buckets; true 80/20 concentration (a few bad contracts) is not visible | Commercial/finance | Could reveal the action should target specific accounts, not the whole 60% book uniformly |
| Fuel tariff vs consumption detail | Needed to size the fuel lever and judge whether a surcharge clause is viable | Operations/procurement | Changes the EUR 0–3m fuel estimate to a real number |
| Notice periods and expected one-off renegotiation/severance costs for the 2026 plan | Needed to confirm the plan doesn't breach the 3.5x covenant during execution | Treasury/legal | Could force resequencing of actions |
| Wage agreement terms and any union/works-council constraints on productivity changes | Collective bargaining agreement referenced; labour-law specialist needed before committing to workforce actions | HR/labour law counsel | Could cap or delay the productivity lever |
| Confirmed 13-week cash position (beyond the "about nine months" estimate) | Firms up the liquidity-safe call with precision | Treasury | Would not likely change the safe/at-risk verdict but should be confirmed before the board paper |
| 2026–2027 volume and price plan for the renewal negotiation | Needed to re-size the EBIT gap in euros against actual future revenue, not the 2025 proxy | Commercial team | Could raise or lower the required EUR 7.4m gap |

**Specialists and review needed:** labour/industrial-relations counsel (wage agreement, any productivity-driven workforce change); commercial contract counsel (drafting and negotiating indexation clauses at the 2026 renewal); treasury (covenant stress test of one-off costs). None of these are covered by this analysis and should review before the plan goes to the board.

