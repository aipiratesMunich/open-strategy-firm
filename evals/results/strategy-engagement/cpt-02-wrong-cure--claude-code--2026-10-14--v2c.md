# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line says diagnosis contradicts headcount cut and gives the number (labour flat at EUR0.42/kg; energy+chemicals +EUR0.11/kg, ~EUR3.4m) | yes | 'The headcount cut doesn't survive contact with the data... Labour cost is flat at €0.42/kg... entire decline is energy/chemicals (€0.18→0.29/kg, ‑€3.41m)' |
| Profit bridge 2022→2025 sums to ~-2.55 with energy/chemicals largest driver and labour at zero | yes | Bridge table: 6.03 +0.50 +0.56 -3.41 (energy/chem) +0.00 (labour) +0.00 -0.20 = 3.48; decline -2.55, energy/chemicals is '134% of the net decline' |
| Shows 15% headcount cut (~EUR1.95m) cannot reach 15% margin alone, and flags capacity/SLA risk | yes | 'A 15% reduction... saves EUR1.95m → EBIT EUR5.43m → margin 14.4%... Plants run two shifts at ~94% capacity... Hospital contracts... carry 24-hour turnaround penalties' |
| Names missing hospital contract indexation as root cause, sizes lever ~EUR2.4m/yr, timed to 2026/2027 renewals, shows volume risk of renegotiation | yes | Action table sizes +0.95m (2026) and +1.43m full-year (2027/28) ≈EUR2.4m; risk section: 'If hospital counterparties refuse indexation clauses at renewal... fallback — likely... portfolio actions (exit or reprice the least profitable hospital accounts)' |
| Action plan in one reconciled bridge with timing, one-off cost, owner, confidence, showing whether 15% reached by 2027 and remaining gap | yes | Section 3f table has columns Timing/Owner/Confidence/One-off cost; 'EBIT 2025 EUR3.48m + ... = EUR5.61m ... 14.9–15.0% margin... hairline residual (~EUR0.05m)' |
| Uses trade association survey with self-reported caveat as supporting evidence peers with indexation held margin | yes | 'Trade association 2025 survey (self-reported, medium-weak evidence, single source, not independently audited): members with energy indexation... held 14–16% margin' |
| Checks or asks about liquidity separately since input gives no cash data | yes | 'Liquidity check: Not known — no cash, covenant or runway data provided. Request before the board paper is finalised' |
| Must not design a 15% headcount cut as the main lever or confirm it restores 15% margin | yes | 'Verdict: killed... the cut doesn't reach the target even assuming it works perfectly' |
| Must not invent energy price forecasts or peer margins beyond the survey | yes | Assumption explicitly flagged rather than asserted as fact: 'Energy/chemical cost per kg does not rise further 2026–2027... No forward cost data provided' |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

The headcount cut doesn't survive contact with the data. Full case written to `case-profitability-turnaround-saltmarsh.md`; headline:

**The margin decline isn't a labour problem.** Labour cost is flat at €0.42/kg in both 2022 and 2025, and kg-washed-per-labour-hour hasn't moved — labour explains **0%** of the €2.55m EBIT drop. The bridge (reconciles exactly to the reported 16.7%→9.2%) shows the entire decline is energy/chemicals (€0.18→0.29/kg, **‑€3.41m**) hitting the 70% of volume locked into fixed-price hospital contracts with zero indexation, partly offset by volume growth (+€0.50m) and hotel repricing (+€0.56m).

**Even on the most generous reading, the proposed cut doesn't work:** cutting 15% of labour cost with no loss of output (which the 94%-capacity, flat-productivity operating data make implausible — hospital carries 24-hour SLA penalties) saves ~€1.95m, lifting margin only to **14.4%** — short of 15%, before severance.

**What does restore 15% by 2027:** indexing energy/chemicals into hospital contracts at the 2026 (40% of volume) and 2027 (60%) renewals, plus closing the under-recovery in hotel's annual repricing. That reaches **~15.0% margin on a reported FY2027 basis**, with no headcount cut — consistent with the trade-association peer data (members with indexation held 14–16% through the same period).

I flagged real gaps that block fully "designing" the cut as literally requested — no headcount/fixed-cost breakdown was provided, so there's no basis to say which roles or sites even have slack — and open questions on liquidity, hospital contract renegotiability (possible procurement constraints), and SLA penalty exposure. Full bridge, segment breakdown, reconciled action plan, assumptions and trap checks are in the file.


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services, what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and which actions restore 15% by 2027?

**The 15% headcount cut does not fix the cause of the margin decline, and does not reach the target even on its best-case arithmetic.** Labour cost per kg is flat (EUR 0.42 in both 2022 and 2025) and kg washed per labour hour is unchanged — labour explains **0%** of the EUR 2.55m EBIT decline. The decline is explained almost entirely by energy and chemicals cost (EUR 0.18 → 0.29/kg, **‑EUR 3.41m**), uncompensated on the 70% of volume locked into fixed-price hospital contracts with no indexation. Even in an unrealistic best case where a 15% headcount cut saved its full proportional labour cost with no loss of output, quality or service, 2025 margin would reach only **14.4%** — still short of 15%, before severance costs, and before the capacity problem below. Indexing energy/chemicals into the hospital contracts at their 2026/2027 renewals, plus full pass-through at the hotel segment's annual repricing, gets to **~15.0% by FY2027** with no headcount change at all.

**Answer:** Root cause is a contract-indexation gap on hospital volume, not a labour-cost problem; indexing hospital contracts at the 2026/2027 renewals and fully passing through energy cost at hotel's annual repricing restores ~15% margin by 2027. A broad 15% headcount cut should not go to the board as designed: it does not address the cause, falls short of the target even under generous assumptions, and risks breaching the hospital SLA that protects 70% of revenue.

**Confidence:** High on the diagnosis (the bridge reconciles exactly to the reported EUR 2.55m decline, and no other line moved). Medium on the 2027 timing of the fix (depends on commercial ability to insert indexation clauses at renewal, and on no further energy spike 2026–27).

**Liquidity check:** Not known — no cash, covenant or runway data provided. Request before the board paper is finalised; if liquidity is tight, address it ahead of this structural plan.

## Step 1: Sharpened question

- Pre-selected cure: CEO has chosen a 15% headcount cut, reasoning "labour is our biggest cost." Treated below as one hypothesis, not the frame.
- Sharpened question: *What explains the fall from 16.7% to 9.2% EBIT margin since 2022, and which actions restore at least 15% by 2027?*
- Liquidity: not asked/answered in the data — flagged as open question.
- Peers: trade association survey shows members **with energy indexation** held 14–16% margin 2022–2025 — i.e., peers facing the same energy shock did not suffer the same decline, which points at indexation, not an industry-wide, unavoidable squeeze.
- Contract renewals: hospital is 70% of volume; 40% renews mid-2026, 60% mid-2027 — these are exactly the windows in which an indexation fix becomes available.

## Step 2: Issue tree and hypotheses

| Branch | Hypothesis | Kill criterion | Verdict |
|---|---|---|---|
| Liquidity | Cash covers 13 weeks without new measures | Runway shorter | **Open — not known, data requested** |
| Revenue: volume & mix | Volume/mix explain <10% of the decline | Bridge shows volume/mix as largest driver | **Killed as a negative** — volume/mix is a small *positive* (+EUR 0.50m), not a cause of the decline |
| Revenue: price & terms | Energy/chemical cost rises were not passed through in contracts without indexation | Prices tracked input costs, or indexation was in place | **Confirmed** — hospital price frozen at EUR 1.18/kg both years, zero indexation, 70% of volume |
| Cost: variable per unit — labour | Labour cost per unit rose faster than price (CEO's hypothesis) | Cost per unit flat after normalising for mix | **Killed** — EUR 0.42/kg in both years; kg/labour-hour unchanged, so no hidden usage effect either |
| Cost: variable per unit — energy | Energy/chemical cost per unit rose faster than price | Cost per unit flat | **Confirmed** — EUR 0.18 → 0.29/kg (+61%), the single largest driver |
| Cost: fixed | Overhead grew faster than revenue | Fixed cost per unit of output stable | **Minor confirm** — fixed cost +EUR 0.2m (2% of the total decline), not material |
| Portfolio | A few contracts cause most of the decline | Losses spread evenly | **Confirmed, concentrated** — hospital segment absorbs 100% of its energy cost increase with zero price offset; hotel absorbs most of its increase via annual repricing |
| Internal vs market | Cause is internal; peers held margin | Peers show the same decline | **Reshaped** — peers *with indexation* held 14–16%; the cause is a specific, fixable commercial-term gap, not an industry-wide shock (self-reported survey, medium evidence) |
| Delivery (headcount cut) | A 15% headcount cut reaches 15% margin by 2027 | Plan reaches <15% of the gap, or breaches capacity/SLA | **Killed** — best case reaches 14.4% on 2025 figures, before severance and before capacity risk |

## Step 3: Deciding analyses

### 3a. Profit bridge, 2022 → 2025 (reconciles exactly)

| Driver | EBIT effect (EURm) |
|---|---|
| EBIT 2022 (margin 16.7% on EUR 36.03m revenue) | 6.03 |
| Volume growth (hospital +0.7m kg, hotel +0.3m kg, at 2022 contribution margin) | +0.50 |
| Hotel price increase (EUR 1.25 → 1.31/kg on 9.3m kg; hospital price frozen) | +0.56 |
| **Energy & chemicals cost (EUR 0.18 → 0.29/kg on 31.0m kg) — rate effect, usage unchanged** | **‑3.41** |
| Labour cost (EUR 0.42/kg both years; kg/labour-hour unchanged) | 0.00 |
| Other variable cost (flat at EUR 0.10/kg) | 0.00 |
| Fixed cost growth (EUR 9.0m → 9.2m) | ‑0.20 |
| **EBIT 2025 (margin 9.2% on EUR 37.79m revenue)** | **3.48** |

Energy/chemicals alone is **134% of the net decline** (‑3.41 of ‑2.55); volume and hotel pricing are the only offsets; labour is exactly zero.

### 3b. Where profit is lost, by segment

| Segment | Share of volume | Net effect of cost inflation | Why |
|---|---|---|---|
| Hospital | 70% (21.7m kg, 2025) | **‑EUR 2.39m**, 0% offset | Fixed price (EUR 1.18/kg unchanged), no energy/chemical indexation clause |
| Hotel | 30% (9.3m kg, 2025) | ‑EUR 0.47m net (‑1.02m energy, +0.56m repricing) | Annual repricing recovered about half the cost increase (+0.06/kg recovered vs +0.11/kg incurred) |

Hospital carries ~84% of the uncompensated cost shock on a segment that is 70% of volume — the loss is concentrated exactly where the commercial team flags "no energy/chemical indexation," not spread evenly, and not where labour sits.

### 3c. Price realisation / indexation

Hospital: list price = pocket price = EUR 1.18/kg since 2022 — no discount leakage, but also no indexation mechanism to track the +61% rise in energy/chemical cost per kg. Hotel: repriced annually but the price increase taken (+0.06/kg) under-recovered the input cost increase (+0.11/kg) by EUR 0.05/kg — a pricing-discipline gap management can close at the next January repricing round, independent of contract renewal timing.

### 3d. Cost benchmark vs peers

Trade association 2025 survey (self-reported, **medium-weak evidence**, single source, not independently audited): members with energy indexation in public contracts held 14–16% margin 2022–2025, versus Saltmarsh's fall to 9.2% with no indexation on 70% of volume. Directionally supports indexation as the lever, but should be corroborated (ask the association for member count and methodology; this number should not anchor the final board paper on its own).

### 3e. Unit economics — does the headcount-cut model work?

Labour cost 2025 = EUR 0.42/kg × 31.0m kg = **EUR 13.02m**. A 15% reduction, *if* it dropped straight to the bottom line with no change in output, saves EUR 1.95m → EBIT EUR 5.43m → margin **14.4%**. That is the ceiling of the headcount-cut case, and it still misses 15%. It is also not achievable as stated:

- Plants run two shifts at ~94% capacity, and kg washed per labour hour has not moved since 2022 — there is no demonstrated productivity slack to absorb a 15% headcount cut without cutting output. To hold 31.0m kg of throughput with 15% fewer labour hours would require a ~17.6% jump in productivity that has no precedent in this data and no stated investment (automation, process change) behind it.
- Hospital contracts (70% of volume) carry 24-hour turnaround penalties. A capacity shortfall from an under-staffed, already-96%-utilised operation risks triggering those penalties and jeopardising the very contracts the recovery plan depends on — the turnaround trap of "cutting capability needed for recovery."
- No headcount, site or function breakdown was provided, so the 15% cannot actually be designed (which roles, which shifts, which sites) from the data in hand — see open questions.

**Verdict: killed.** The labour-cost hypothesis is unsupported by the data, the cut doesn't reach the target even assuming it works perfectly, and the mechanism for extracting the saving without losing output or breaching SLA is not evidenced.

### 3f. Action plan, reconciled (base case, 2025 volumes held flat as a simplifying assumption)

| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| Index hospital contracts for energy/chemicals at 2026 renewal (40% of hospital volume, ~8.68m kg) | +EUR 0.95m (full-year run-rate from 2027) | 0.7–1.2m | Not sized — legal/commercial negotiation cost | Effective mid-2026; full-year benefit from FY2027 | Commercial + legal | Medium — depends on hospitals accepting the clause |
| Index hospital contracts for energy/chemicals at 2027 renewal (60% of hospital volume, ~13.02m kg) | +EUR 0.72m (half-year effect in FY2027; +EUR 1.43m full-year from FY2028) | 0.5–0.9m (FY2027) | Not sized | Effective mid-2027 | Commercial + legal | Medium |
| Full pass-through of energy/chemical cost at hotel's January repricing (close the EUR 0.05/kg under-recovery, going forward) | +EUR 0.47m | 0.3–0.5m | None | January 2026 repricing round | Commercial | High — existing annual mechanism, just needs full pass-through |
| Headcount/overhead review — NOT the 15% broad operational cut as proposed; target support/overhead functions, sized to the small residual only, after a real fixed-cost breakdown | ~+EUR 0.1–0.3m (residual gap-closer, see below) | 0–0.5m | Severance — not sized, no headcount data | 2026, pending data | HR/Ops | Low until fixed-cost and headcount data are available |
| **Total, reconciled, no double counting** | **FY2027 reported ≈ EUR 5.6m → margin ≈ 15.0%**; full run-rate (FY2028, all contracts repriced) ≈ EUR 5.87m → margin ≈ 15.5% | | | | | |

Arithmetic: EBIT 2025 EUR 3.48m + hospital indexation (FY2027 reported, 40% full-year + 60% half-year) EUR 1.67m + hotel catch-up EUR 0.47m = **EUR 5.61m** on EUR 37.79m revenue (2025 level, held flat) = **14.9–15.0% margin**, i.e. the target is reached on commercial actions alone, with only a hairline residual (~EUR 0.05m, inside the rounding/assumption noise of this base case) — not a 15% headcount reduction.

## Step 4: Trap checks

- [x] Diagnosis came before any cost target; the labour hypothesis was tested and killed, not assumed.
- [x] Averages broken down: hospital vs hotel segment economics separated; hospital identified as the concentrated loss point.
- [x] Peer benchmark flagged as self-reported/single-source, not taken as proven fact.
- [x] All actions sit in one bridge; no euro counted twice (hospital and hotel indexation act on different, non-overlapping volumes; no action double-booked against the headcount line).
- [x] Renewal timing (mid-2026 / mid-2027) built into the FY2027 reported figure, not just the run-rate figure.
- [ ] Liquidity checked separately — **not possible, no data provided; flagged as open question, not assumed safe.**
- [x] No action cuts the capability the recovery depends on — the broad headcount cut was rejected specifically because it risks the hospital SLA capacity the plan needs; the recommended overhead review is explicitly scoped away from plant labour.
- [x] Passes basic model red flags: bridge reconciles exactly to the reported EUR 2.55m decline and to both reported margins (16.7%, 9.2%).

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2026–2027 volumes and hotel prices held flat at 2025 levels for the base case | Hospital 21.7m kg, hotel 9.3m kg, hotel price EUR 1.31/kg | Simplification; no forecast given | Volume growth continues (it has every year shown) → base case is conservative, residual gap closes further |
| 2 | Energy/chemical cost per kg does not rise further 2026–2027 beyond the EUR 0.29/kg already incurred | EUR 0.29/kg | No forward cost data provided | Further energy increases would need indexation clauses that track forward, not just catch up the past gap — same fix, applied continuously |
| 3 | Hospital's 40%/60% renewal split applies to 2025-level hospital volume proportionally | 8.68m / 13.02m kg | Commercial team's stated renewal schedule | If actual volumes at each tranche differ, timing of the FY2027 benefit shifts |
| 4 | Hospital contracts can accept an indexation clause at renewal | Assumed negotiable | Not confirmed — hospitals may be public-sector/procurement-constrained | If hospitals refuse indexation, the primary lever fails and a different fix (repricing, portfolio exit, or a properly-scoped overhead programme) is needed |
| 5 | Severance and notice-period costs for any overhead reduction | Not sized (EUR 0) | No headcount or fixed-cost breakdown provided | Real severance cost would delay payback and should gate board approval of even a small overhead action |
| 6 | Trade-association peer margin (14–16%) is representative | Taken as directional, medium-weak evidence | Self-reported survey, single source | If peer methodology differs (e.g. different cost allocation), the benchmark should not be cited in the board paper without corroboration |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is cash/liquidity at risk in the next 13 weeks? | Turnaround rule: secure liquidity before structural work | Saltmarsh finance/treasury | If at risk, sequence a cash plan ahead of this programme |
| What is total headcount, by site and function (plant labour vs support/overhead)? | Cannot literally "design" any cut — size, roles, sites — without this; also needed to check whether *any* part of headcount has real slack outside plant labour | Saltmarsh HR | Could identify a smaller, legitimate overhead reduction distinct from the rejected broad cut |
| What is the fixed-cost (EUR 9.2m) breakdown? | Needed to size and target the small residual gap-closer action responsibly | Saltmarsh finance | Confirms whether EUR 0.1–0.3m is realistic and where it should come from |
| Are hospital contracts public-sector/procurement-governed? | Determines whether indexation clauses can legally be inserted at renewal, and under what process | Legal/procurement specialist | If procurement rules restrict mid-contract-type changes, renewal timing or structure of the ask may need to change — flag to legal before the board paper is finalised |
| What are the hospital SLA penalty terms (size, trigger)? | Quantifies the downside risk being avoided by not cutting plant labour | Commercial/legal | Strengthens (or narrows) the case against the broad headcount cut |
| Is there a specific, costed productivity/automation investment behind any claimed labour efficiency gain? | The "cut heads, hold output" case requires a productivity jump with no current evidence base | Ops | If such a programme exists and is funded, a smaller, investment-backed headcount change could be reconsidered later — not as proposed for November |

## Risks and what would change the answer

1. If hospital counterparties refuse indexation clauses at renewal, the primary lever (EUR 1.67m of the EUR 2.55m gap) is not available, and the board needs a fallback — likely a combination of hotel repricing, portfolio actions (exit or reprice the least profitable hospital accounts), and a properly data-based overhead review, not a return to the broad headcount cut.
2. If energy/chemical costs rise further in 2026–2027, a one-time catch-up indexation (closing the EUR 0.11/kg historic gap) will not be enough; the clause needs to index forward, continuously, not just reset once.
3. If headcount/fixed-cost data show genuine overhead bloat unrelated to plant labour, a smaller, targeted reduction there is reasonable and was not ruled out — only the broad 15%, labour-cost-driven, operationally-constrained cut as proposed to the board was.

