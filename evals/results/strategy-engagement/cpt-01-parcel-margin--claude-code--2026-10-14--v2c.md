# cpt-01-parcel-margin on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Profit bridge from 2023 to 2025 by driver sums to -10.76 (within rounding) and names variable cost per parcel as the largest driver. | yes | Bridge: Volume +2.20, Price +2.60, Variable cost/parcel -14.56, Fixed cost -1.00 → EBIT 16.00→5.24; so-what states 'the EUR 10.76m EBIT decline... is a cost-per-unit story (−14.56m variable, mostly labour then fuel)'. |
| Splits variable cost into labour, fuel and subcontractors and labour into wage and productivity effects. | yes | 'labour −9.36m, fuel −4.16m, subcontractors −1.04m'; labour split '≈78% is the wage rate (≈ −EUR 7.3m), ≈22% is the productivity fall (≈ −EUR 2.0m)'. |
| Root cause in one sentence first: unit cost rose ~EUR0.28/parcel (9.7%) while price rose EUR0.05 (1.25%), mainly because 60% of volume sits on fixed-price contracts without indexation. | NO | Lead sentence: 'variable cost/parcel rose 9.7% ... while the 60% of volume on fixed, non-indexed 2023 contracts absorbed the entire increase at a flat EUR 4.00 price' — omits the overall price-rose figure (EUR0.05/1.25%), which only appears later in supporting tables ('variable cost/parcel +9.7% vs  |
| Checks liquidity separately and flags thin covenant headroom (~3.1x vs 3.5x, ~EUR1.6m EBITDA) as a constraint on one-off restructuring costs and timing. | yes | 'Liquidity check: ... net debt/EBITDA at 3.10x vs. a 3.5x covenant ... Not large, though... should trigger a recheck against the covenant, particularly if any fix carries debt-funded one-off cost'; backing file computes 'EBITDA could fall to EUR 12.57m (−11.5%) before breach' (≈EUR1.6m cushion). |
| Action plan in one reconciled bridge, each action with EBIT effect, range, one-off cost, timing, owner, confidence; repricing/indexation timed to 2026 renewal window with volume risk shown. | yes | Working file table has columns 'EBIT effect (base) / Range / One-off cost / Timing / Owner / Confidence'; renewal action timed '2026 renewal' with range '+5.0 to +7.8m (negotiation/volume-retention risk)'. |
| Actions reach or show the remaining gap to ~EUR12.6m EBIT (6%) by 2027. | yes | 'Resulting 2027 P&L (base case...) EBIT ≈ EUR 15.7m, margin ≈ 7.2% — clears the 6% target with a buffer', exceeding the ~EUR12.6m/6% threshold. |
| Treats peers 'held their margins' as unverified and names peer figures to compile (normalised margin, price indexation practice) before claiming internal cause. | yes | 'CFO's claim ... is unverified: no peer EBIT margins, cost-per-parcel, or indexation-clause terms are compiled yet. Treat as a hypothesis, not a fact.' |
| No euro counted twice (price and volume effects on same contracts shown consistently). | yes | Fixed book -8.74m (cost only) + repriced book net -3.22m (price+cost) = -11.96m, matching bridge's price(+2.60)+variable cost(-14.56)=-11.96m; fuel indexation explicitly 'bundled into the first action ... to avoid double-counting'. |
| Must not propose an across-the-board cost cut before diagnosis, or cuts to drivers/sorters without addressing productivity and service. | yes | 'No action cuts capability the recovery depends on — productivity action targets efficiency (routing/technology), not headcount or service-level cuts'. |
| Must not invent peer margins or industry wage data. | yes | Peer margins explicitly left uncompiled/unverified; wage figures (+9%, 17.6 parcels/hr) are reconstructed from the data pack's own HR detail, not invented industry data. |

## Transcript

## Turn 1

**User:** Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO. (Attached in the working directory: cpt-01-input.md.)

I saved the full working (bridge, contract-bucket analysis, action plan, trap checks) to `case-turnaround-kestrel.md`. Here's the answer page for the CFO:

---

# Profitability turnaround: Kestrel Logistics, parcel division

**Answer:** The margin fall from 8.0% to 2.5% is a pass-through failure, not a cost-control or volume problem: variable cost/parcel rose 9.7% (mostly labour, +11.25%, plus fuel +11.4%) while the 60% of volume on fixed, non-indexed 2023 contracts absorbed the entire increase at a flat EUR 4.00 price. Re-pricing and indexing that book at its H1 2026 renewal, plus restoring driver productivity, plausibly reaches a **7.2% margin by 2027** in the base case — but only a **1.8% margin** (worse than today) if the renewal lands as a partial catch-up instead of a full one.

**Confidence:** Medium — the historical diagnosis is high-confidence (the bridge reconciles exactly to both years' reported EBIT, and the EUR 4.00/EUR 4.05 blended prices tie out precisely from the two contract buckets). The 2027 projection is lower-confidence because it depends on the actual 2026 renewal outcome, which **today's date (October 2026) implies should already be known but is not in the data pack**, and on peer margins the CFO cited but hasn't compiled.

**Liquidity check:** Safe for now — net debt/EBITDA at 3.10x vs. a 3.5x covenant (EUR 5.7m of headroom), cash covers ~9 months of fixed cost. Not large, though: a downside renewal outcome would erode EBITDA and should trigger a recheck against the covenant, particularly if any fix carries debt-funded one-off cost.

## Profit bridge, 2023 to 2025
| Driver | Effect |
|---|---|
| EBIT 2023 (8.0% margin) | EUR 16.00m |
| Volume (+2.0m parcels) | +EUR 2.20m |
| Price (+EUR 0.05/parcel) | +EUR 2.60m |
| Variable cost/parcel (+EUR 0.28), of which labour −9.36m (≈78% rate/22% productivity), fuel −4.16m, subcontractors −1.04m | −EUR 14.56m |
| Fixed cost (+EUR 1.0m, but fixed cost *per parcel* fell) | −EUR 1.00m |
| **EBIT 2025 (2.5% margin)** | **EUR 5.24m** |

## Where profit is lost
| Bucket | 2025 volume | Price | Contribution/parcel | Contribution % (2023 → 2025) | Driver |
|---|---|---|---|---|---|
| Fixed, non-indexed (early-2023, 3-yr contracts) | 60% (31.2m) | EUR 4.00, unchanged since signing | EUR 0.82 | 27.5% → 20.5% | Absorbed 100% of the cost increase, zero price offset: −EUR 8.74m |
| Annual, repriced | 40% (20.8m) | EUR 4.125 | EUR 0.945 | 27.5% → 22.9% | Price rose 3.1% against 9.7% cost inflation — under-indexed too: net −EUR 3.22m |

The fixed book is 73% of the combined price-and-cost margin loss. Even the "repriced" book under-recovers cost inflation — the fix has to be an explicit wage/fuel index clause, not a return to the historical repricing pattern.

## Action plan (base case)
| Action | EBIT effect | Range | Timing | Owner | Confidence |
|---|---|---|---|---|---|
| Reprice + index the 60% fixed book at 2026 renewal (target ~EUR 4.25 + wage/fuel escalators) | +EUR 7.8m | +5.0 to +7.8m | 2026 renewal, full effect 2027 | Commercial | Medium |
| Driver productivity recovery to 18.0 parcels/driver-hour | +EUR 2.0m | +1.0 to +2.0m | 12–18 months | Operations | Medium |
| Subcontractor rate renegotiation / fleet mix | +EUR 0.6m | +0.3 to +1.0m | 2026–27 | Procurement | Low |
| **Total, reconciled** | **+EUR 10.4m → ~7.2% margin** | **+6.3 to +10.8m** | | | |

**Downside case** (partial +3% repricing, no productivity gain, one more wage round): margin falls to **~1.8%** — worse than today. The swing is ~5+ margin points, driven almost entirely by the 2026 renewal outcome, not by execution of the internal cost levers.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2027 volume flat | 52.0m parcels | 2025 actual, no growth data given | Growth or decline materially changes required price |
| 2 | 2027 variable cost flat (base case) ex. productivity/subcontractor actions | EUR 3.18/parcel baseline | 2025 actual | A further wage round (plausible, given +9% 2023-25) would need to be covered by the indexation clause, not just a one-time catch-up |
| 3 | 2027 fixed cost flat | EUR 40.0m | 2025 actual | Overhead programme or growth changes this |
| 4 | 40% annual book holds at EUR 4.125 (not re-modelled upward) | EUR 4.125 | 2025 actual | If it also gets indexed upward, less pressure falls on the 60% book |
| 5 | Labour rate vs. productivity split of the EUR 0.18/parcel rise | ~78% rate / ~22% productivity | Reconstructed from wage +9% and parcels/hour 18.0→17.6; matches reported 1.78 almost exactly | Different split changes productivity action's sizing, not the total |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What were the actual H1 2026 renewal terms (price, indexation, volume retained) for the 60% book? | This is the single swing factor between a 7.2% and a 1.8% 2027 margin; the renewal window has already passed as of today | Commercial team / contracts | Replaces the entire base/downside scenario with fact |
| Are the peers' margins actually holding, and on what cost base and indexation terms? | Confirms whether this is fixable internally or a market-wide shock | Finance (compile from peer annual reports) | Shifts confidence, not the internal diagnosis |
| Does Kestrel have (or could it add) a fuel surcharge clause separate from the base price? | Could recover part of the EUR 4.16m fuel drag without touching the base price negotiation | Commercial/Legal | Could ease the price-increase ask on the 60% book |
| What are the subcontractor contract terms and in-house cost comparison? | Determines if EUR 0.3-1.0m is realistic or optimistic | Procurement | Resizes the smallest action line |
| 2023 volume split between the two contract buckets | Would sharpen whether volume growth also shifted mix toward the lower-margin fixed book | Commercial | Refines, doesn't overturn, the bridge |

## Trap checks
- [x] Diagnosis before cost target — no across-the-board cut; fix is concentrated on one contract bucket and labour, not blanket costs.
- [x] Averages broken down — 2.5% average hides two buckets both below their 2023 contribution rate.
- [ ] Benchmarks normalised against peers — **open**, peer figures not compiled.
- [x] One reconciled bridge, no double counting — fuel indexation bundled into the single 2026 renewal action.
- [x] Renewal timing in the plan — and flagged as likely already past.
- [x] Liquidity checked separately — not at risk now, headroom moderate.
- [x] No action cuts recovery-dependent capability — productivity lever targets routing/tech, not headcount or service cuts that would jeopardize the renewal.
- [x] Model passes reconciliation — bridge and blended-price checks tie out exactly to reported figures.

**Specialists and review:** Commercial/legal review needed on contract indexation clause drafting; no tax, labour-law, or insolvency specialist implicated by the data given.


## Files in work dir after run

- case-turnaround-kestrel.md
- cpt-01-input.md

## File written by the run: case-turnaround-kestrel.md

# Quick case: Profitability turnaround — Kestrel Logistics, parcel division

*Fictional company; all figures invented for evaluation.*

## Step 1: Sharpen the question

**Sharpened question:** What explains the EBIT margin fall from 8.0% (2023) to 2.5% (2025) in the parcel division, and which actions restore at least 6% by 2027?

Answered from the pack directly:
- Last good year: 2023 (8.0% margin, EUR 16.0m EBIT on EUR 200.0m revenue).
- Target: ≥6% EBIT margin by 2027; plan due at the February 2027 board meeting.
- Cure chosen: none ("we have not picked a cure") — kept as open, not pre-decided.
- Liquidity: not the primary frame, but checked below since there is debt and a covenant.
- Peers: CFO says two listed peers "held their margins" in 2024–25 — **unverified, not compiled**. Carried as weak evidence, not fact.
- Contract timing: 60% of volume sits on 3-year fixed-price contracts signed early 2023, no wage/fuel indexation, **renewing H1 2026**.

**Flag:** today's date is October 2026. H1 2026 — the renewal window this whole turnaround thesis hinges on — has already passed or is in progress. The pack has no 2026 actuals. Everything below about 2027 is therefore a *pre-renewal planning scenario*, not a forecast grounded in known renewal outcomes. Getting the actual 2026 renewal terms is the single highest-priority data request (see Open questions).

## Step 2: Issue tree and hypotheses

| Branch | Hypothesis | Kill criterion | Verdict |
|---|---|---|---|
| Liquidity | Cash and covenant headroom are adequate to run a structural fix | Runway <13 weeks or covenant breached | **Not killed** — see liquidity check below, headroom is real but not large |
| Revenue: volume/mix | Volume/mix explain <10% of the EBIT decline | Bridge shows volume as largest driver | **Killed as a negative driver** — volume growth added +EUR 2.2m, i.e. volume helped, didn't hurt |
| Revenue: price/terms | Cost increases were not passed through in contracts without indexation | Prices tracked input costs, or indexation was in place | **Confirmed, and primary** — see bridge and contract-bucket analysis |
| Cost: variable per unit | Labour (then fuel) cost per parcel rose faster than price | Cost per unit flat after normalising | **Confirmed** — variable cost/parcel +9.7% vs price/parcel +1.25% |
| Cost: fixed | Overhead grew faster than revenue | Fixed cost per unit of output stable or falling | **Killed** — fixed cost/parcel fell from EUR 0.780 to EUR 0.769 |
| Portfolio | A few contracts (not evenly spread) cause most of the decline | Losses spread evenly | **Confirmed, reshaped** — not individual customers (not in the data) but the 60% fixed-price *bucket* causes ~73% of the combined price+cost margin loss |
| Internal vs market | Cause is internal (contract design); peers held margin | Peers show the same decline | **Open** — peer claim unverified; diagnosis doesn't depend on it, but it bounds confidence on "how much is fixable" |
| Delivery | Actions reach 6% by 2027 after one-off costs/notice periods | Reconciled plan reaches <6% in time | **Confirmed in base case, at risk in downside case** — see Step 3f |

## Step 3: Deciding analyses

### a. Profit bridge, 2023 → 2025

Check: EBIT 2023 = 50.0m × (4.00−2.90) − 39.0m = 50.0×1.10−39.0 = **EUR 16.0m** (8.0% of EUR 200.0m) ✓ matches CFO's figure.
EBIT 2025 = 52.0m × (4.05−3.18) − 40.0m = 52.0×0.87−40.0 = **EUR 5.24m** (2.49% ≈ 2.5% of EUR 210.6m) ✓ matches CFO's figure and the balance-sheet section's EBIT 5.2m.

Decomposition (volume at old margin, price/cost effects at new volume, standard bridge; sums exactly to the reported change):

| Driver | Calculation | EBIT effect |
|---|---|---|
| EBIT 2023 | | **+EUR 16.00m** |
| Volume (+2.0m parcels at 2023 contribution of EUR 1.10) | (52.0−50.0)×(4.00−2.90) | **+EUR 2.20m** |
| Price (+EUR 0.05/parcel on 2025 volume) | (4.05−4.00)×52.0 | **+EUR 2.60m** |
| Variable cost per parcel (+EUR 0.28 on 2025 volume) | −(3.18−2.90)×52.0 | **−EUR 14.56m** |
| … of which labour (+EUR 0.18/parcel) | −(1.78−1.60)×52.0 | −EUR 9.36m |
| … of which fuel (+EUR 0.08/parcel) | −(0.78−0.70)×52.0 | −EUR 4.16m |
| … of which subcontractors (+EUR 0.02/parcel) | −(0.62−0.60)×52.0 | −EUR 1.04m |
| Fixed cost (+EUR 1.0m) | −(40.0−39.0) | **−EUR 1.00m** |
| **EBIT 2025** | | **EUR 5.24m** |

Sum check: 16.00+2.20+2.60−14.56−1.00 = 5.24 ✓.

Labour split, rate vs. productivity (cross-check using the HR detail): wage agreement +9% and parcels/driver-hour 18.0→17.6 reproduce the reported 1.60→1.78 almost exactly (28.80 EUR/hr → ×1.09 = 31.39 EUR/hr; ÷17.6 = EUR 1.784/parcel, vs. reported 1.78 — consistent). Splitting the EUR 0.18/parcel rise proportionally: **≈78% is the wage rate (≈ −EUR 7.3m)**, **≈22% is the productivity fall (≈ −EUR 2.0m)**. Both are real, but the wage rate is the larger of the two.

**So-what:** volume and fixed cost are not the problem — they are mildly *helping*. The EUR 10.76m EBIT decline (16.00→5.24) is a cost-per-unit story (−14.56m variable, mostly labour then fuel) only partly offset by a small price gain (+2.60m). Fixed-cost hypothesis **killed**; volume hypothesis **killed as a negative**; variable-cost and price/terms hypotheses **confirmed**.

### b/c/e. Where profit is lost, price realisation, and unit economics by contract bucket

The pack gives two contract buckets instead of individual customers — treat this as the portfolio cut.

| Bucket | Share of 2025 volume | 2025 price | 2025 var. cost | Contribution/parcel | Contribution % | 2023 contribution/parcel* |
|---|---|---|---|---|---|---|
| Fixed, non-indexed (signed early 2023) | 60% (31.2m) | EUR 4.00 (unchanged since signing) | EUR 3.18 | EUR 0.82 | 20.5% | EUR 1.10 (27.5%) |
| Annual, repriced | 40% (20.8m) | EUR 4.125 | EUR 3.18 | EUR 0.945 | 22.9% | ~EUR 1.10 (27.5%) |

*2023 blend was EUR 4.00 flat across the division (these contracts weren't yet split), so EUR 1.10/27.5% is used as the common 2023 starting point for both.

Blend check: 0.6×4.00 + 0.4×4.125 = **4.05**, exactly the reported 2025 revenue/parcel. ✓

**Price realisation finding:** the entire +EUR 2.60m price effect in the bridge comes from the 40% repriced book; the 60% fixed book moved EUR 0.00 on price while absorbing the full EUR 0.28/parcel variable-cost increase. In EBIT terms: fixed book contributes **−EUR 8.74m** (0.28×31.2m, no price offset at all); repriced book contributes a **net −EUR 3.22m** (+EUR 2.60m price, −EUR 5.82m cost). The fixed book alone is **73%** of the combined price+cost margin loss (8.74 of 11.96). This directly confirms the playbook hypothesis: *input-cost increases were not passed through in contracts without indexation.*

**Unit-economics nuance (important for the fix):** even the "repriced" 40% book under-recovered cost inflation — price rose +3.1% (4.00→4.125) against variable cost up +9.7% (2.90→3.18), so its contribution % also fell, from 27.5% to 22.9%. The company's normal annual repricing cadence is not actually tracking cost inflation either. **Implication: the fix cannot be "treat the 60% book like the 40% book" — the 40% book is also under-indexed.** It has to be an explicit wage- and fuel-linked indexation clause, not a return to the historical repricing pattern.

### d. Cost benchmarks vs. peers

CFO's claim — two listed peers "held their margins" in 2024–25 — is **unverified**: no peer EBIT margins, cost-per-parcel, or indexation-clause terms are compiled yet. Treat as a hypothesis, not a fact, pending the data request below. It would not change the internal diagnosis (which is self-consistent from Kestrel's own numbers) but it does bound the confidence on "is 6% achievable at all industry-wide" and on how hard the 2026 renegotiation will be.

### f. Action plan value, reconciled bridge, base case vs. downside

Required price to hit 6% margin by 2027, holding 2025 variable cost (EUR 3.18/parcel) and fixed cost (EUR 40.0m) flat and volume flat at 52.0m (all three flagged as assumptions, not projections):

52p − 52×3.18 − 40.0 = 0.06×52p → p ≥ **EUR 4.20** (vs. EUR 4.05 today, +3.7%). Holding the 40% book at EUR 4.125, this requires the 60% book to reprice to about **EUR 4.25** (+6.3% vs. its current EUR 4.00) — roughly matching the cost inflation that book has already absorbed since 2023, plus a small buffer.

**Base case (plan succeeds):** 60% book repriced to EUR 4.25 with wage+fuel indexation at the 2026 renewal; driver productivity restored to 18.0 parcels/hour; modest subcontractor-rate improvement.

| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reprice + index the 60% fixed book at 2026 renewal (→ ~EUR 4.25, add wage/fuel escalators) | +EUR 7.8m | +5.0 to +7.8m (negotiation/volume-retention risk) | Low (commercial renegotiation); volume-loss risk if customers resist | Effective from 2026 renewal; full-year effect from 2027 | Commercial/Sales | Medium |
| Driver productivity recovery to 18.0 parcels/driver-hour | +EUR 2.0m | +1.0 to +2.0m | Possible routing/tech investment, not sized | 12–18 months | Operations | Medium |
| Subcontractor rate renegotiation / fleet-mix optimisation | +EUR 0.6m | +0.3 to +1.0m | Not sized — need contract terms | 2026–2027 | Procurement/Operations | Low (data-dependent) |
| **Total, reconciled, no double counting** | **+EUR 10.4m** | **+6.3 to +10.8m** | | | | |

(Fuel-specific indexation is bundled into the first action — same renewal event, same customer conversation — rather than booked as a separate line, to avoid double-counting the one 2026 renegotiation.)

Resulting 2027 P&L (base case, mid-point): Revenue = 52.0×(0.6×4.25+0.4×4.125) = **EUR 218.4m**; variable cost ≈ EUR 162.7m; fixed cost EUR 40.0m → EBIT ≈ **EUR 15.7m**, margin ≈ **7.2%** — clears the 6% target with a buffer for cost inflation the base case otherwise assumes away.

**Downside case (renewal only partially won, cost inflation continues):** 60% book repriced only +3% (to EUR 4.12, matching the weak historical pattern rather than full catch-up); no productivity or subcontractor gains realised; variable cost rises a further 3% (one more modest wage round) to EUR 3.28/parcel; fixed cost flat.

Revenue = 52.0×(0.6×4.12+0.4×4.125) ≈ EUR 214.3m; variable cost = 52.0×3.28 ≈ EUR 170.6m; fixed cost EUR 40.0m → EBIT ≈ **EUR 3.8m**, margin ≈ **1.8%** — *worse than today*, not just short of target.

**So-what:** the swing between base and downside is roughly 5+ margin points, almost entirely driven by one event — the outcome of the 2026 contract renewal on the 60% book. Internal cost actions (productivity, subcontractors) are real and worth doing but are second-order next to that negotiation. Delivery hypothesis: **confirmed in the base case, at real risk in the downside case** — this is a negotiation-outcome risk, not an execution-capability risk.

**Liquidity and covenant check:** net debt EUR 44m / EBITDA EUR 14.2m = **3.10x**, below the 3.5x covenant cap. Headroom: EBITDA could fall to EUR 12.57m (−11.5%) before breach, or net debt could rise by ~EUR 5.7m at current EBITDA. Cash covers ~9 months of fixed cost (≈EUR 30m). **Verdict: not a liquidity crisis, but headroom is moderate, not large** — the downside case above (EBITDA falling further) would eat meaningfully into that headroom, so liquidity should be rechecked once 2026 renewal outcomes are known, especially if any one-off cost (tech investment, severance) is debt-funded.

## Step 4: Trap checks

- [x] Diagnosis came before any cost target — no across-the-board cut proposed; the fix is concentrated on one contract bucket and one cost line (labour), not a blanket cost programme.
- [x] Averages broken down — the 2.5% division average hides a 20.5%-contribution fixed book and a 22.9%-contribution repriced book, both below their 2023 starting point of 27.5%.
- [ ] Benchmarks normalised against peers — **open**: peer figures not compiled; cannot yet claim or rule out a market-wide shock. Flagged as data request, confidence held at medium pending this.
- [x] All actions sit in one reconciled bridge, no euro counted twice — fuel indexation folded into the single 2026 renewal action rather than booked separately.
- [x] One-off costs and renewal timing are in the plan — 2026 renewal date is the anchor for action 1; noted that it should already have occurred given today's date.
- [x] Liquidity checked separately from profitability — done above; not at risk today, headroom moderate.
- [x] No action cuts capability the recovery depends on — productivity action targets efficiency (routing/technology), not headcount or service-level cuts that would risk the customer retention the repricing action depends on.
- [x] Model red flags — bridge reconciles exactly to reported EBIT in both years; blended price checks (EUR 4.00 and EUR 4.05) tie out from the contract-bucket split; no plug figures used.

## Step 5: Answer page

See `# Profitability turnaround: Kestrel Logistics, parcel division` below.

