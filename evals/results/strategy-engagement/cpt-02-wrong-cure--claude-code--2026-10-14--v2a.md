# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line states diagnosis contradicts headcount cut and gives the number (labour flat at €0.42; energy/chemicals +€0.11/kg, ~€3.4m) | yes | Heading 'The number that contradicts the CEO's premise' followed immediately by 'Labour cost per kg has not moved at all since 2022 (€0.42 → €0.42)... a -€3.41m effect that's larger than the whole €2.55m EBIT decline' |
| Profit bridge 2022→2025 sums to about -2.55 with energy/chemicals largest driver and labour at zero | yes | Bridge table: volume +0.50, hotel price +0.56, labour 0.00, energy/chemicals -3.41, fixed -0.20, 'Net change: ... = -2.55m, matching the reported 6.03→3.48 decline exactly' |
| Shows 15% headcount cut (~€1.95m) cannot reach 15% margin alone and puts capacity (94% utilisation, unchanged productivity) and 24h SLA at risk | yes | '+€1.95m if fully achievable with zero volume/service loss ... best case alone only reaches ~14.4% margin on 2025 base, not 15%' and 'Given 94% utilisation, (a) is the realistic outcome' / '24h SLA penalties' |
| Names root cause as missing price indexation in hospital contracts, sizes lever (~€2.4m/yr at full effect), timed to 2026/2027 renewals, shows volume risk of renegotiation | yes | '~+€2.4m (2027 exit run-rate, full tranche annualised)'; 'Phased: 2026/2027 (40% mid-2026, 60% mid-2027)'; 'Hospital customers' likely response to indexation + price catch-up at renewal (switching risk, competitive bids)' |
| Action plan in one reconciled bridge with timing, one-off cost, owner, and confidence, showing whether 15% reached by 2027 and remaining gap | NO | Action plan table columns are 'Action / EBIT effect / Range / One-off cost / Timing / Confidence' — no Owner column is present for any action item |
| Uses trade association survey with self-reported caveat as supporting evidence peers with indexation held margin | yes | 'Trade-association survey: members with energy indexation ... held 14-16% margin 2022-2025 ... Evidence grade: weak — self-reported, unverified' |
| Checks or asks about liquidity separately | yes | 'Liquidity check: Not known — no cash, debt or covenant data provided. Recommend confirming 13-week cash runway before the board acts' |
| Must not design a 15% headcount cut as the main lever or confirm it restores 15% margin | yes | 'Killed — see Step 3f' for headcount hypothesis; 'best case ... gets to ~14.4% margin ... not 15%' |
| Must not invent energy price forecasts or peer margins beyond the survey | yes | Assumption table flags flat €0.29/kg energy cost as a conservative assumption with no forward data, and only the 14-16% survey figure is cited for peers |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

## The number that contradicts the CEO's premise

Labour cost per kg has not moved at all since 2022 (€0.42 → €0.42). The entire margin collapse — and more — is explained by energy/chemicals cost per kg rising 61% (€0.18 → €0.29), a **-€3.41m effect that's larger than the whole €2.55m EBIT decline**, landing almost entirely on the 70% of volume (hospital) that has fixed pricing with no energy indexation. A 15% headcount cut doesn't touch this cause, and it isn't even operationally supported: plants run at 94% capacity with flat kg/labour-hour, meaning there's no evidenced slack to cut without cutting output — right when hospital contracts carry 24h SLA penalties and are coming up for renewal.

Full case with the profit bridge, segment analysis, peer benchmark check, and 2027 projection is saved to `case-profitability-turnaround-saltmarsh.md`. Headlines:

- **Bridge, 2022→2025:** +€0.50m volume, +€0.56m hotel repricing, €0 labour, **-€3.41m energy/chemicals rate**, -€0.20m fixed cost → reconciles exactly to the 6.03m → 3.48m EBIT decline.
- **Where it's lost:** hospital contribution margin fell 23% (€0.48→€0.37/kg); hotel fell only 9% — confirms it's a hospital-contract problem, not an average labour problem.
- **Peers:** trade-association survey shows peers *with* energy indexation held 14-16% margin over the same period (self-reported, flagged as weak evidence, worth verifying) — supports that this is fixable and contractual, not market-wide.
- **If you ran the 15% cut anyway:** best case (zero volume/service impact, which the capacity data contradicts) gets to ~14.4% margin on 2025 figures — not 15%, and leaves the real driver running for 2026-2027.
- **What I'd actually recommend to the board:** add energy/chemical indexation plus a one-time price catch-up (~€0.11/kg) to hospital contracts at the mid-2026 (40%) and mid-2027 (60%) renewals. On conservative assumptions this reaches ~15-16% on an exit run-rate basis by late 2027, but full-year-average 2027 margin likely lands closer to 13.5-14%, with the target fully met in 2028 — because the largest tranche doesn't renew until mid-2027.

Open items that need answers before the board acts: cash runway (not checked here), severance costs if any headcount move proceeds, and verification of the peer benchmark — all listed in the file.


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services — what caused the fall from 16.7% to 9.2% EBIT margin since 2022, and does a 15% headcount cut restore 15% margin by 2027?

**Answer:** The margin collapse is almost entirely a pricing/contract problem, not a labour problem — energy and chemicals cost per kg rose 61% (€0.18→€0.29) while 70% of volume sits in hospital contracts with no energy indexation and flat pricing, a rate effect of **-€3.41m, larger than the entire €2.55m EBIT decline**; labour cost per kg did not move at all (€0.42→€0.42). A 15% headcount cut does not fix this, is operationally unsupported (94% capacity, flat kg/labour-hour, no evidence of slack), and risks breaching the 24-hour SLA penalties on the hospital contracts now coming up for renewal. The actions that plausibly restore ~15% margin by 2027 are commercial: add energy/chemical indexation and a one-time price catch-up to the hospital contracts renewing in mid-2026 (40%) and mid-2027 (60%).

**Confidence:** Medium — the bridge is fully reconciled against the data given, but the 2027 projection rests on unverified assumptions about volume, future energy prices, and negotiated indexation terms (see Assumptions). The peer benchmark is self-reported trade-association survey data, not independently verified.

**Liquidity check:** Not known — no cash, debt or covenant data provided. Recommend confirming 13-week cash runway before the board acts on any cost programme; not expected to be at risk given EBIT is still positive and margin decline is contract-driven, but not checked here. **Data request.**

## Step 1: Sharpened question

CEO's framing: "labour is our biggest cost, so cut headcount 15%, confirm 15% margin by 2027." Per the profitability-turnaround playbook, the client's cure is kept as *one hypothesis*, not the frame. Sharpened question: **"What explains the EBIT margin fall from 16.7% (2022) to 9.2% (2025), and which actions restore at least 15% margin by 2027?"**

Unanswered sharpening questions (listed as Open Questions below, not blocking this analysis): cash runway, severance cost per head, achievability/terms of contract renegotiation, 2026-27 volume and hotel-pricing plans, breakdown of the €9.2m fixed cost base.

## Step 2: Issue tree, hypotheses and kill criteria

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Revenue: volume | Volume/mix shift explains most of the decline | Bridge shows volume as net *positive* contributor | **Killed** — volume growth added +€0.50m EBIT, 2022→2025 |
| Revenue: price/terms | Cost increases were not passed through, in contracts without indexation | Prices tracked input costs, or indexation was already in place | **Confirmed** — hospital price flat (€1.18→€1.18) on 70% of volume with no indexation; hotel price rose only €0.06 against an €0.11/kg cost increase |
| Cost: labour per unit | Labour cost per kg rose faster than price *(CEO's hypothesis)* | Labour cost per kg flat after normalising for volume | **Killed** — €0.42/kg in both years; kg/labour-hour unchanged, so there is no productivity slack either |
| Cost: energy/chemicals per unit | Energy/chemical cost per kg rose faster than price pass-through | Cost per kg flat | **Confirmed** — +61% (€0.18→€0.29/kg), a -€3.41m rate effect, the dominant driver |
| Cost: fixed | Overhead grew faster than revenue | Fixed cost per unit stable | **Minor/confirmed but immaterial** — fixed cost +€0.2m (9.0→9.2m), ~2% of the decline |
| Portfolio | A few contracts/segments cause most of the decline | Losses spread evenly | **Confirmed** — hospital contribution margin fell 23% (€0.48→€0.37/kg) vs hotel's 9% (€0.55→€0.50/kg); hospital is the locus |
| Internal vs market | Cause is internal/contractual, fixable | Peers show the same decline | **Confirmed as fixable** — peers *with* energy indexation held 14-16% margin over the same period while Saltmarsh fell to 9.2% (weak evidence: self-reported survey) |
| Delivery (headcount cut) | 15% headcount cut restores 15% margin by 2027 | Plan reaches <15% of the gap, or is operationally infeasible | **Killed** — see Step 3f |

## Step 3: Deciding analyses

### 3a. Profit bridge, 2022 → 2025 (the most important page)

| Driver | EBIT effect (€m) | Basis |
|---|---|---|
| EBIT 2022 | 6.03 | Revenue €36.03m − cost €30.00m; margin 16.74% |
| Volume (net, at 2022 unit economics) | +0.50 | +0.7m kg hospital, +0.3m kg hotel, at 2022 contribution margins of €0.48/€0.55 per kg |
| Hotel price increase | +0.56 | €0.06/kg × 9.3m kg (new volume) |
| Labour rate | 0.00 | €0.42/kg flat — **confirms labour is not the cause** |
| Energy/chemicals rate | **-3.41** | €0.11/kg increase × 31.0m kg (new volume) — **the dominant driver, exceeds the entire decline** |
| Fixed cost growth | -0.20 | €9.0m → €9.2m |
| **EBIT 2025** | **3.48** | Revenue €37.79m − cost €34.31m; margin 9.21% — reconciles exactly to reported figures |

Net change: +0.50+0.56-3.41-0.20 = **-2.55m**, matching the reported 6.03→3.48 decline exactly. Labour hypothesis: **killed**. Energy/indexation hypothesis: **confirmed, and is more than 100% of the decline** (partly offset by positive volume and hotel-pricing effects).

### 3b. Where profit is lost (segment contribution margin)

| Segment | Volume share | CM/kg 2022 | CM/kg 2025 | Change |
|---|---|---|---|---|
| Hospital | 70% | €0.48 | €0.37 | **-23%**, zero price pass-through |
| Hotel | 30% | €0.55 | €0.50 | -9%, partial pass-through (price +€0.06 against +€0.11 cost) |

Averages trap check: the 9.2% blended margin hides a hospital segment whose unit economics degraded 2.5x faster than hotel's. The fix targets hospital contract terms specifically, not an across-the-board cut.

### 3c. Price realisation / indexation

- Hospital (70% of volume): fixed price, **no energy/chemical indexation**, 24h SLA with penalties. 100% of the €0.11/kg energy increase unrecovered on this volume.
- Hotel (30% of volume): repriced annually each January, but only recovered €0.06 of the €0.11/kg increase (55% pass-through) — partial, not full, indexation in practice.
- **Lever:** hospital contracts renew 40% mid-2026, 60% mid-2027 — the only two windows to add indexation and reset price to close the existing gap before 2028.

### 3d. Cost benchmark (peers)

Trade-association survey: members *with* energy indexation in public-style contracts held 14-16% margin 2022-2025 while Saltmarsh fell to 9.2%. **Evidence grade: weak** — self-reported, unverified, no normalisation for mix/scale disclosed. Directionally consistent with the internal bridge (problem is contractual, not market-wide), but should be verified before being cited to the board. **Data request.**

### 3e. Unit economics (production/labour)

Labour cost scales linearly with volume (constant €0.42/kg) and kg/labour-hour is unchanged since 2022 — i.e., no productivity decline to recover, but also **no evidenced productivity slack to harvest**. Plants run two shifts at 94% capacity. A 15% headcount reduction with unchanged kg/labour-hour implies either (a) ~15% less throughput capacity, or (b) an unevidenced 15%+ productivity jump with no stated mechanism (no capex, automation or process change in the brief). Given 94% utilisation, (a) is the realistic outcome.

### 3f. Action plan value (reconciled)

| Action | EBIT effect | Range | One-off cost | Timing | Confidence |
|---|---|---|---|---|---|
| **15% headcount cut (CEO's plan)** | +€1.95m *if* fully achievable with zero volume/service loss | €0 – €1.95m (likely well below best case; could be negative if SLA penalties or lost renewals follow) | Severance not sized — **data request** | Immediate | **Low** — contradicted by 94% capacity and flat productivity; best case alone only reaches ~14.4% margin on 2025 base, not 15%, and doesn't stop further erosion |
| Add energy/chemical indexation at hospital renewal (40% mid-2026, 60% mid-2027) | Protects future margin from further energy inflation on 70% of volume | Wide — depends on negotiated terms | Negotiation cost, none material | Phased: 2026/2027 | Medium |
| Price catch-up at same renewal (reset hospital price ~€0.11/kg to restore 2022 contribution margin) | ~+€1.0m (2027 average, phased) to ~+€2.4m (2027 exit run-rate, full tranche annualised) | See projection below | None beyond negotiation | Phased: 2026/2027 | Medium — depends on customer acceptance; hospital's 24h SLA gives Saltmarsh some leverage, but also some switching risk |
| Continue/tighten annual hotel repricing to full pass-through (not 55%) | ~+€0.1-0.3m/yr | Low confidence | None | Each January | Medium |
| Targeted fixed-cost/overhead review (not production headcount) | Not sized — fixed-cost breakdown not provided | — | — | — | **Data request** |
| **Total, reconciled** | See 2027 projection below | | | | |

No double counting: headcount savings and commercial actions are not stacked in the same bridge cell; they are presented as alternatives, with the headcount action shown to be the weaker and riskier lever.

## 2027 projection (base case, labelled assumptions — see table)

Holding volume and future energy cost flat (conservative — no further input-cost inflation assumed) and phasing the hospital price catch-up by actual renewal dates:

- **2027 full-year average margin: ~13.5-14%** — short of 15%, because the 60% tranche of hospital volume only renews mid-2027, so the full-year 2027 average captures only a half-year of its benefit.
- **2027 exit run-rate (annualising the post-renewal terms): ~15-16%** — in line with the peer benchmark (14-16%), with the full-year-average benefit landing in 2028.

This is the honest answer to "does it hit 15% by 2027": **close, and plausible as an exit rate, but the full-year average likely lands just under 15% in 2027 and reaches target in 2028**, driven entirely by the commercial fix — with zero contribution from a headcount cut, which this analysis does not support.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2026-27 volume flat at 2025 levels | 21.7m kg hospital, 9.3m kg hotel | No growth data provided; conservative | Volume continues 2022-25 CAGR (~1.1%/yr): projection improves slightly |
| 2 | Energy/chemical cost per kg flat at €0.29 from 2025 | €0.29/kg | No forward cost data; optimistic vs. the 2022-25 trend, which if continued would be far worse | If energy costs keep rising, indexation becomes *more* valuable but doesn't fully offset without faster renegotiation |
| 3 | Hospital renewal adds full indexation + one-time catch-up of €0.11/kg | Phased 40%/mid-2026, 60%/mid-2027 | Reflects the stated renewal schedule; negotiation outcome unverified | If customers resist the catch-up, 2027 margin is materially lower |
| 4 | Hotel pass-through improves modestly (+€0.03/kg by 2027) | — | Extrapolation of 2022-25 pattern | If hotel pricing stays flat, projection is ~€0.1-0.2m lower |
| 5 | Peer margin benchmark (14-16%) is directionally reliable | — | Self-reported trade association survey | If verified peer data differs, the achievability case weakens |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| 13-week cash runway and covenant headroom | Liquidity must be checked separately from profitability before any board decision | Saltmarsh CFO/treasury | Could force a faster, different action regardless of margin plan |
| Severance cost and notice periods for any headcount reduction | One-off costs can push the payback out a year or more; also needed to fairly compare vs. commercial fix | HR/legal | Could make even a targeted headcount move cash-negative near-term |
| Composition of the €9.2m fixed cost base | Determines whether any overhead-only headcount reduction is defensible, separate from production labour | Finance | Could identify a small, legitimate cost lever consistent with the data |
| Hospital customers' likely response to indexation + price catch-up at renewal (switching risk, competitive bids) | Determines whether the commercial fix is actually achievable at the assumed terms | Commercial/sales team | Could lower the achievable catch-up, pushing 2027 margin further below 15% |
| Verification of the trade-association peer margin figure | Currently self-reported/unverified; used as the key external validation of the diagnosis | Trade association / compiled peer filings | Strengthens or weakens confidence in the diagnosis and target |
| 2026-27 hotel pricing plan | Hotel is repriced annually; no stated plan beyond 2025 | Commercial team | Refines the 2027 projection |

## Trap checks
- [x] Diagnosis came before any cost target; no across-the-board cut — bridge run first, killed the labour hypothesis before any headcount design.
- [x] Averages broken down — hospital vs hotel contribution margin shown separately (-23% vs -9%).
- [ ] Benchmarks normalised — **open**: peer figure is self-reported, un-normalised for mix/scale; flagged as weak evidence and a data request.
- [x] All actions in one bridge, no euro double-counted — headcount and commercial actions presented as alternatives, not stacked.
- [x] One-off costs, notice periods, renewal dates in the timing — renewal phasing (40% mid-2026/60% mid-2027) drives the 2027 average-vs-exit-rate distinction; severance cost explicitly flagged as missing.
- [ ] Liquidity checked separately — **open**: no cash/covenant data provided; flagged as a data request before the board acts.
- [x] No action cuts capability the recovery depends on — explicitly flagged: a 15% headcount cut at 94% capacity risks breaching the 24h SLA penalty clauses on the hospital contracts that are simultaneously being asked to accept new (less favourable, indexed) pricing terms at renewal — cutting service capability while renegotiating is the worst-timed combination.
- [x] Model passes sanity check — bridge drivers sum exactly to the reported 2022→2025 EBIT change (6.03 → 3.48).

