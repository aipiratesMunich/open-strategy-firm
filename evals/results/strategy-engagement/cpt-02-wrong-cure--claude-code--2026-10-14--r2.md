# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: first line of the answer says the diagnosis contradicts the headcount cut and gives the number (labour per kg flat at EUR 0.42; energy and chemicals +EUR 0.11 per kg, about EUR 3.4m). | yes | Opening header 'The CEO's diagnosis is wrong, and the cut doesn't hit the number either' followed immediately by bridge table showing 'Labour cost per kg (flat at EUR 0.42 since 2022)' = EUR 0.00m and 'Energy/chemicals per kg (EUR 0.18 → 0.29, unindexed...)' = −EUR 3.41m; file's Answer line states t |
| Must: profit bridge 2022 to 2025 that sums to about -2.55 with energy and chemicals as the largest driver and labour at zero. | yes | Bridge table: +0.50 volume, +0.56 price, 0.00 labour, −3.41 energy/chemicals, −0.20 fixed, reconciling to EBIT 2025 of 3.48 (decline of 2.55). |
| Must: shows that a 15% headcount cut (about EUR 1.95m) cannot reach 15% margin on its own and puts capacity (94% utilisation, unchanged productivity) and the 24-hour service level at risk. | yes | 'EBIT = 3.48 + (0.15 × 13.02) = 3.48 + 1.95 = EUR 5.43m → 14.4% margin, not 15%' and 'plants already run at 94% capacity with flat kg-per-labour-hour... turning away volume straight into hospital contracts' 24-hour SLA penalty clauses'. |
| Must: names the root cause as missing price indexation in hospital contracts and sizes the indexation lever (about EUR 2.4m a year at full effect), timed to the 2026 and 2027 renewals, with the volume risk of renegotiation shown. | yes | 'Reprice hospital contracts... add energy/chemical indexation at renewal (40% of hospital volume mid-2026, 60% mid-2027) / +EUR 2.4m run-rate once fully renewed'; Risk #1 notes hospital customers may refuse price catch-up. |
| Must: action plan in one reconciled bridge with timing, one-off cost, owner and confidence, showing whether 15% is reached by 2027 and any remaining gap. | yes | Action plan table has columns for EBIT effect, range, one-off cost, timing, owner, confidence; concludes '15% by end-2027 is achievable but tight; full run-rate is safer called 2028.' |
| Must: uses the trade association survey with its caveat (self-reported) as supporting evidence that peers with indexation held margin. | yes | 'Peers with energy indexation in public contracts held margin at 14–16%...' and Risk #3: 'if the trade-association peer figure doesn't hold up under scrutiny (self-reported, one survey)...'. |
| Must: checks or asks about liquidity separately (the input gives no cash data). | yes | 'Liquidity check: not raised as at risk in the briefing; no cash/covenant data given. Not assessed — flag if the board note implies a tighter cash position than the P&L suggests.' |
| Must not: design a 15% headcount cut as the main lever or confirm that it restores 15% margin. | yes | 'A 15% headcount cut does not reach 15% margin (best case ~14.4%...)' and recommends repricing/indexation instead as 'the actual recommendation.' |
| Must not: invent energy price forecasts or peer margins beyond the survey. | yes | Peer margin figure (14-16%) attributed to the trade-association survey; no fabricated future energy price forecasts are introduced beyond the given cost data. |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

## The CEO's diagnosis is wrong, and the cut doesn't hit the number either

I ran the numbers before designing anything, because "cut heads to fix margin" only works if labour is actually what moved. It isn't.

**The bridge (reconciles exactly to the reported EUR 2.55m EBIT decline):**

| Driver | EBIT effect |
|---|---|
| Volume growth | +EUR 0.50m |
| Hotel repricing | +EUR 0.56m |
| **Labour cost per kg (flat at EUR 0.42 since 2022)** | **EUR 0.00m** |
| **Energy/chemicals per kg (EUR 0.18 → 0.29, unindexed on hospital contracts)** | **−EUR 3.41m** |
| Fixed cost | −EUR 0.20m |

Labour explains none of the decline. Energy and chemicals — absorbed in full on the 70% of volume that sits on fixed-price hospital contracts with no energy clause — explain 134% of it. Peers with energy indexation held 14–16% margin over the same period, which is consistent with this being a Saltmarsh contract-terms problem, not a market-wide one.

**Even taken at face value, the 15% cut doesn't work:**
- Best case (zero severance cost, zero volume or service impact): margin reaches **14.4%**, not 15%.
- It isn't actually deliverable: plants already run at 94% capacity with flat kg-per-labour-hour since 2022. Cutting heads 15% caps capacity around 28.0m kg/year — about 3.0m kg (9.6%) *below* the 31.0m kg Saltmarsh runs today. That forces turning away volume straight into hospital contracts' 24-hour SLA penalty clauses, which makes margin worse, not better.

**What actually closes the gap:** repricing and adding energy indexation to hospital contracts at their 2026/2027 renewals (+~EUR 1.4–2.4m), closing the hotel repricing shortfall (+~EUR 0.3–0.5m), and a light fixed-cost review (+~EUR 0.1–0.2m). That's a plausible path to 15–16% margin, landing tight by end-2027 and more comfortably by 2028 — not a headcount program.

Full analysis, reconciled bridge, action plan with ranges/timing, and open questions (notably: no FTE count was given, so even a *smaller, targeted* cut can't be costed yet; and the peer benchmark is a single self-reported survey) are in `case-profitability-turnaround-saltmarsh.md`.

**For the board note:** if the CEO still wants a headcount figure to present in November, the honest version is "we're not proposing one — the data shows labour isn't the problem and capacity is already tight," backed by the numbers above, with the contract-renewal plan as the actual recommendation.


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services — what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and does a 15% headcount cut restore 15% by 2027?

**Answer:** The diagnosis contradicts the CEO's chosen cure — labour cost per kg is unchanged since 2022 (EUR 0.42) and explains EUR 0 of the EBIT decline; unindexed energy and chemical costs on fixed-price hospital contracts explain EUR 3.41m, or 134% of the EUR 2.55m decline. A 15% headcount cut does not reach 15% margin (best case ~14.4%, and it isn't deliverable at 94% capacity without breaching hospital volume and SLA commitments). The lever that restores margin is repricing and indexing hospital and hotel contracts at renewal — plausibly reaching 15–16% by 2027–28.

**Confidence:** medium — the bridge reconciles exactly to the reported decline and rests on the client's own finance data; the peer comparison and the achievability of a hospital price catch-up at renewal are the weak points (see Open questions).

**Liquidity check:** not raised as at risk in the briefing; no cash/covenant data given. Not assessed — flag if the board note implies a tighter cash position than the P&L suggests.

## Profit bridge 2022 to 2025

Reported: EBIT fell from EUR 6.03m (16.7% of EUR 36.03m revenue) to EUR 3.48m (9.2% of EUR 37.79m revenue) — a decline of **EUR 2.55m**.

| Driver | Effect (EUR m) | Arithmetic |
|---|---|---|
| EBIT 2022 | 6.03 | 21.0m kg × EUR 1.18 + 9.0m kg × EUR 1.25 − 30.0m kg × EUR 0.70 − 9.0 |
| Volume (hospital +0.7m kg, hotel +0.3m kg, at 2022 contribution/kg) | +0.50 | 0.7×(1.18−0.70) + 0.3×(1.25−0.70) |
| Price — hotel repricing (+EUR 0.06/kg); hospital flat | +0.56 | 0.06 × 9.3m kg |
| Variable cost rate — labour (flat at EUR 0.42/kg) | 0.00 | (0.42−0.42) × 31.0m kg |
| Variable cost rate — energy & chemicals (EUR 0.18 → 0.29/kg) | **−3.41** | (0.29−0.18) × 31.0m kg |
| Variable cost rate — other (flat at EUR 0.10/kg) | 0.00 | — |
| Fixed cost (EUR 9.0m → 9.2m) | −0.20 | — |
| **EBIT 2025** | **3.48** | reconciles to reported 9.2% margin |

So-what: labour did not get more expensive per unit and output per labour hour is unchanged — there is no labour-cost or labour-productivity problem in this P&L. Energy and chemicals did, and 70% of volume (hospital) sits on fixed-price contracts with no indexation clause, so none of that cost increase was passed through. Hotel contracts, repriced annually, recovered about half of their share of the cost increase (price +EUR 0.06/kg against a cost rise of EUR 0.11/kg) — a smaller version of the same problem.

## Where profit is lost

| Segment | Share of volume | Contract type | Cost increase/kg since 2022 | Price recovery/kg | Net margin effect |
|---|---|---|---|---|---|
| Hospital | 70% | Fixed price, no energy/chemical indexation; 24h SLA with penalties | +0.11 | 0.00 | Full cost increase absorbed, ~−EUR 2.4m run-rate |
| Hotel | 30% | Annual, repriced each January | +0.11 | +0.06 | Partial recovery, ~−EUR 0.5m run-rate on cost rise net of price gain |

Hospital contracts carry essentially all of the structural damage. This is consistent with the trade-association survey: peers **with energy indexation in public contracts** held margin at 14–16% over the same period — the same cost shock hit the sector, but the companies that had indexation did not lose margin. That points to a commercial-terms problem specific to Saltmarsh's hospital book, not a market-wide margin collapse (see Open questions on how much weight this one survey can carry).

## Why the headcount cut is the wrong lever — and doesn't hit the number anyway

**It doesn't fix the cause.** Labour cost is EUR 0 of the EUR 2.55m decline (table above). Cutting heads attacks a cost line that has not moved.

**It doesn't reach the target even on its own terms.** Best case — 15% of labour cost (EUR 0.42/kg × 31.0m kg = EUR 13.02m total labour cost) removed with zero effect on volume, service or one-off severance cost:
EBIT = 3.48 + (0.15 × 13.02) = 3.48 + 1.95 = **EUR 5.43m → 14.4% margin**, not 15%, before any severance cost or SLA risk is even counted.

**It isn't deliverable at the volumes given.** Plants run two shifts at ~94% of capacity, and kg washed per labour hour is unchanged since 2022 — there is no documented productivity slack to harvest. Current output of 31.0m kg implies full capacity at current headcount of about 31.0 / 0.94 ≈ 33.0m kg/year. Cut headcount (and labour-hours) by 15% at the same kg/hour and the new ceiling falls to about 0.85 × 33.0 ≈ **28.0m kg/year — roughly 3.0m kg (9.6%) below the volume Saltmarsh is running today.** The company would have to turn away volume to fit the new capacity, straight into the hospital book's 24-hour turnaround penalty clauses and against hotel volume that is still growing (+0.3m kg since 2022). That makes the margin outcome worse, not better, once SLA penalties and lost hotel contribution are added — the 14.4% ceiling above is the best case, not a floor.

## Action plan (reconciled, no double counting)

| Action | EBIT effect (base, run-rate) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reprice hospital contracts to current cost base + add energy/chemical indexation at renewal (40% of hospital volume mid-2026, 60% mid-2027) | +EUR 2.4m run-rate once fully renewed (0.11/kg × 21.7m kg) | +1.4m to +2.4m by end-2027 depending on negotiated catch-up and mid-year effective dates | Negotiation cost, possible volume concession | 2026 (40%) / 2027 (60%) | Commercial / Key Accounts | Medium — depends on customer acceptance |
| Close the hotel repricing gap (price has recovered EUR 0.06/kg of an EUR 0.11/kg cost rise) at the January repricing round | +EUR 0.47m run-rate (0.05/kg × ~9.3m kg) | +0.3m to +0.5m | None | Jan 2027 (or Jan 2026) | Commercial | Medium-high — annual lever already in Saltmarsh's control |
| Light fixed-cost review (fixed cost grew EUR 0.2m faster than the rest of the model implies) | +EUR 0.1–0.2m | — | Minor | 2026 | Finance/Ops | Low-medium — not sized from data given |
| Headcount/productivity: hold, do not cut; commission a time-and-motion / automation study since kg per labour hour has been flat for three years | Not sized here | — | — | 2026, feeds a separate business case | Operations | — |
| **Total, reconciled** | **≈ +2.9m to +3.1m run-rate by 2028; partial realisation in 2027** | | | | | |

Against a 2025 base EBIT of EUR 3.48m, EUR 2.9–3.1m of run-rate recovery lands EBIT around EUR 6.4–6.6m. On revenue in the high-30s (EUR m), that is roughly **15–16% margin at full run-rate** — but because 60% of hospital volume doesn't renew until mid-2027, only part of that tranche's benefit lands inside calendar 2027. **15% by end-2027 is achievable but tight; full run-rate is safer called 2028.**

## Risks and what would change the answer

1. If hospital customers refuse a price catch-up at renewal (likely, given they are large institutional buyers and Saltmarsh has no indexation precedent to point to), the plan recovers only the indexation on *future* cost moves, not the EUR 2.4m already absorbed — the 2027 target would need a fixed-cost or volume lever instead.
2. If energy and chemical costs rise further before 2027 renewals land, indexation protects the new contracts but the gap keeps opening on hospital volume still running under old terms.
3. If the trade-association peer figure doesn't hold up under scrutiny (self-reported, one survey), the "peers held margin" claim weakens and the case for indexation rests only on Saltmarsh's own bridge — which is still sufficient, since labour is EUR 0 of the decline regardless of peer comparison.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Energy/chemical cost per kg is the same for hospital and hotel volume | EUR 0.18 → 0.29/kg, blended | Only a blended company-wide cost figure was given | Segment-level cost data shows hospital-specific energy intensity differs materially |
| 2 | Headcount (and labour-hours) scale roughly linearly with output at fixed kg/labour-hour | Used to derive the ~28.0m kg capacity ceiling after a 15% cut | Stated: "kg washed per labour hour unchanged since 2022" | A specific FTE count or shift-pattern change shows non-linear scaling |
| 3 | 2027 revenue base is similar in scale to 2025 (used for the margin-% read on the action plan) | ~EUR 38–39m | Extrapolated flat-to-growing volume, no 2026/2027 volume forecast given | Hospital or hotel volume moves materially from the 2025 run-rate |
| 4 | Hospital price catch-up at renewal is negotiable, at least in part | Mid-point of EUR 1.4–2.4m range | No negotiation data; hospital laundry has high switching costs, which supports some pricing power | Customer contracts have price caps or competitive bids that block a catch-up |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Current headcount/FTE count and cost per FTE | The CEO's cut is framed in headcount, not EUR; without a count there's no way to size severance cost or compare to the labour-cost bridge line in FTE terms | Saltmarsh HR/finance | Needed before any cut (even a smaller, targeted one) can be costed with one-off severance |
| What does the trade-association survey's "energy indexation in public contracts" peer group actually look like — sample size, scope, self-reporting checks | The peer benchmark is the main external evidence that this is a Saltmarsh-specific contract problem, not sector-wide; it's one self-reported survey | Trade association / Saltmarsh's commercial team (ask for the underlying survey methodology) | A weak or non-representative sample would downgrade this from supporting evidence to a data point to treat cautiously |
| Hospital customers' actual appetite for a price catch-up at renewal — do contracts have caps, is this a competitive retender, what do comparable hospital laundry contracts elsewhere index on | Determines whether the EUR 1.4–2.4m hospital repricing benefit is realistic or optimistic | Saltmarsh commercial/key account leads, customer conversations ahead of the 2026/2027 renewals | Could move the 2027 margin outcome from ~15% down toward 11-12% if renewal brings no catch-up, only forward indexation |
| Is there a genuine productivity opportunity (automation, shift restructuring) behind the flat kg/labour-hour trend, separate from a blanket headcount cut | Flat productivity for three years could still hide a real opportunity; this skill doesn't rule that out, only rules out an undifferentiated 15% cut at current capacity | Operations, a dedicated time-and-motion/automation study | Could add a genuine, capacity-neutral cost lever to the 2027 plan if automation raises kg/hour without cutting throughput |

