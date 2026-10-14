# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line says diagnosis contradicts headcount cut and gives the number (labour flat at 0.42; energy/chemicals +0.11/kg, ~3.4m) | NO | Literal first line is only 'The data contradicts the CEO's diagnosis before it contradicts his cure.' The 0.42 and 0.11 figures appear in the next sentence, and the ~3.41m figure only appears later in the bridge table, not in the first line itself. |
| Profit bridge 2022→2025 sums to ~-2.55 with energy/chemicals largest driver and labour at zero | yes | Table: Volume +0.50, Hotel price +0.56, Energy/chemical -3.41, Fixed cost -0.20, 'Net (matches actual EBIT fall) -EUR2.55m'; file version also shows 'Labour cost per kg / EUR0.00m'. |
| Shows 15% headcount cut (~EUR1.95m) cannot reach 15% margin on its own, and risks capacity (94% utilisation, unchanged productivity) and 24-hour service level | NO | Capacity/productivity/SLA risk is discussed ('plants run two shifts at 94% capacity', 'output per labour-hour unchanged', '24-hour turnaround penalties'), but the ~EUR1.95m savings figure and the baseline insufficiency calculation against the ~EUR2.19m gap to 15% margin is never computed or stated a |
| Names missing price indexation as root cause, sizes indexation lever (~EUR2.4m/yr at full effect), timed to 2026/2027 renewals, shows volume risk of renegotiation | NO | Root cause and renewal timing (40% mid-2026/60% mid-2027) and volume risk ('possible short-term volume risk if a customer resists and is not renewed') are shown, but the lever is sized at '+EUR2.9m' (range 2.0–3.4m) rather than ~EUR2.4m, consistent with applying the EUR0.11/kg gap to the full 31m kg |
| Action plan in one reconciled bridge with timing, one-off cost, owner and confidence, showing whether 15% is reached by 2027 and remaining gap | NO | Action table columns are 'Action / EBIT effect by 2027 (base case) / Range / One-off cost / Timing / Confidence' — there is no Owner column anywhere in the plan. |
| Uses trade association survey with caveat (self-reported) as supporting evidence peers with indexation held margin | yes | 'Trade association data: peer EBIT margins with energy indexation ... held at 14–16% ... This is self-reported, single-source survey data, not normalised for mix or scale — weak evidence on its own, but it points the same direction.' |
| Checks or asks about liquidity separately | yes | 'Liquidity check: Not assessed — no cash, debt or covenant data provided. If liquidity is tight, secure a 13-week cash view before committing to either path.' |
| Must not design a 15% headcount cut as the main lever or confirm it restores 15% margin | yes | 'A 15% headcount cut doesn't touch the actual cause' and 'the only way the cut reaches the 15% margin target is [an] unsupported assumption' — the cut is rejected, not confirmed. |
| Must not invent energy price forecasts or peer margins beyond the survey | yes | Energy cost is held flat as an explicit stated assumption ('No forward data given; conservative/simple hold') rather than a fabricated forecast, and peer margins are only the 14-16% survey figure, not invented beyond it. |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

## Bottom line for the board note

**The data contradicts the CEO's diagnosis before it contradicts his cure.** Labour cost per kg is EUR0.42 in both 2022 and 2025 — unchanged — and output per labour-hour hasn't moved. Labour is not why margin fell. The entire 7.5pp decline is explained by one thing: energy/chemical cost rose EUR0.11/kg (+61%), and 70% of volume (hospital) is on fixed-price contracts with zero indexation, so none of that cost shock was ever recovered. The profit bridge reconciles to the euro:

| | EBIT effect |
|---|---|
| Volume growth | +EUR0.50m |
| Hotel price increases | +EUR0.56m |
| Energy/chemical cost | **-EUR3.41m** |
| Fixed cost drift | -EUR0.20m |
| **Net (matches actual EBIT fall)** | **-EUR2.55m** |

A 15% headcount cut doesn't touch the actual cause, and can't be delivered cleanly: plants run two shifts at 94% capacity with no productivity slack in evidence, so cutting heads 15% means cutting capacity ~15%, not cost at constant output. Modelled through to 2027, the "cut works" story only holds under an assumption the data doesn't support (zero output loss despite 15% fewer workers). The realistic version — losing volume, most likely from hotel first to protect hospital SLA penalties — lands around **4–5% margin, worse than today**, because fixed costs don't shrink with it.

The lever that actually closes the gap: add energy/chemical indexation to hospital contracts at their 2026/2027 renewals — exactly what peers with indexation already do to hold 14–16% margins. That alone gets Saltmarsh to roughly **15–16% margin by 2027**, with no headcount action required.

I wrote the full case (profit bridge, segment breakdown, reconciled action plan, assumptions, open questions, sensitivities) to `case-profitability-turnaround-saltmarsh.md` in the working directory. Key open items before this goes to the board: cash/liquidity position (not in the data), the split between plant-floor and overhead headcount (could support a smaller, legitimate overhead trim as a complement — not a substitute), and verification of the peer survey (self-reported, single source).


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services — what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and which actions restore at least 15% by 2027?

**Answer:** The margin collapse is not a labour problem — labour cost per kg is unchanged (EUR0.42 in both 2022 and 2025) and output per labour hour is flat. It is a contracting problem: energy and chemical costs rose EUR0.11/kg (+61%) and 70% of volume (hospital) sits on fixed-price contracts with no energy/chemical indexation, so none of that cost shock was recovered. Indexing hospital contracts at their 2026/2027 renewals — the lever peers with indexation already use to hold 14–16% margins — closes essentially all of the gap by 2027. **A 15% headcount cut does not address this cause, cannot be delivered without cutting capacity (plants run two shifts at 94% utilisation with no productivity slack), and in the realistic case where it forces volume down it makes the margin worse, not better (modelled at ~4–5% margin, not 15%).**

**Confidence:** Medium-high on the diagnosis (the bridge below reconciles to the actual EBIT change to the euro, using only Saltmarsh's own data). Medium on the 2027 forecast (depends on volume trend continuation, how much of the cost gap can be recovered at renewal, and whether energy costs keep rising — see Assumptions and Sensitivity).

**Liquidity check:** Not assessed — no cash, debt or covenant data provided. If liquidity is tight, secure a 13-week cash view before committing to either path; nothing below should be read as a liquidity plan.

## Profit bridge 2022 → 2025 (reconciles exactly to reported EBIT)

| Driver | EBIT effect | Basis |
|---|---|---|
| EBIT 2022 | EUR6.03m (16.7% margin) | 21.0m kg × EUR1.18 + 9.0m kg × EUR1.25 = EUR36.03m revenue; cost = (0.42+0.18+0.10)×30.0m kg + EUR9.0m fixed = EUR30.0m |
| Volume growth (+0.7m kg hospital, +0.3m kg hotel, at 2022 unit contribution) | +EUR0.50m | 0.7m×EUR0.48 + 0.3m×EUR0.55 |
| Hotel price increase (EUR1.25→EUR1.31/kg on 9.3m kg) | +EUR0.56m | |
| Hospital price | EUR0.00m | Price unchanged, no indexation clause |
| Energy and chemical cost (EUR0.18→EUR0.29/kg on 31.0m kg) | **-EUR3.41m** | 0.11 × 31.0m — **the dominant driver** |
| Labour cost per kg | EUR0.00m | EUR0.42/kg unchanged; output per labour-hour unchanged |
| Other variable cost | EUR0.00m | Unchanged at EUR0.10/kg |
| Fixed cost (EUR9.0m→EUR9.2m) | -EUR0.20m | |
| **EBIT 2025** | **EUR3.48m (9.2% margin)** | Ties to reported figures |

Net effect: -EUR2.55m, matching the actual EBIT fall of EUR6.03m → EUR3.48m exactly. **Energy/chemical cost accounts for 134% of the net decline (partly offset by volume and hotel pricing); labour accounts for 0%.**

## Where profit is lost: by segment

| Segment | Share of volume | Contribution margin/kg 2022 | Contribution margin/kg 2025 | Change | Why |
|---|---|---|---|---|---|
| Hospital | 70% | EUR0.48 | EUR0.37 | -23% | Fixed price, no indexation — absorbed the full EUR0.11/kg cost increase with zero offset |
| Hotel | 30% | EUR0.55 | EUR0.50 | -9% | Annual repricing recovered about half the cost increase via price |

The squeeze is concentrated in the segment with no cost pass-through mechanism, not in a segment with a labour or productivity problem.

## Is the cause internal or market-wide?

Trade association data: peer EBIT margins with energy indexation in public contracts held at 14–16% over the same period (2022–2025) — unchanged while Saltmarsh fell 7.5pp. This is **self-reported, single-source survey data, not normalised for mix or scale — weak evidence on its own**, but it points the same direction as Saltmarsh's own bridge (a contract-structure effect, not a market-wide margin collapse), which is independent triangulation. Verify before citing externally: request the survey's methodology and underlying margin distribution.

## Action plan (reconciled, no double counting)

| Action | EBIT effect by 2027 (base case) | Range | One-off cost | Timing | Confidence |
|---|---|---|---|---|---|
| Add energy/chemical indexation to hospital contracts at renewal (40% mid-2026, 60% mid-2027), recovering the EUR0.11/kg cost gap | +EUR2.9m | +EUR2.0m to +EUR3.4m depending on negotiated recovery rate (70–100%) | Negotiation cost only; possible short-term volume risk if a customer resists and is not renewed | 40% effective mid-2026, full effect from mid-2027 | Medium — depends on customer acceptance and whether only forward indexation or also a catch-up re-basing is achieved |
| Continue hotel price discipline in annual repricing (maintain trend of ~+1.5%/yr) | +EUR0.4m (already in trend, not incremental) | — | None | Annual, each January | High |
| Hold fixed cost growth to inflation rather than letting it drift as it did 2022–25 | +EUR0.1–0.2m | — | None | Ongoing | Medium |
| **15% headcount cut, undifferentiated, as proposed** | **Not recommended as sized — see below** | **-EUR3 to +EUR0.5m depending on volume impact** | Severance (not quantified — no headcount/wage data provided) | 2026 | Low — contradicted by capacity data |
| **Total (indexation + pricing + fixed cost discipline)** | **≈ +EUR3.4m, EBIT ≈ EUR6.4–6.9m, margin ≈ 15–16%** | | | By 2027 | Medium |

### Why the proposed headcount cut doesn't work

- Labour cost per kg is flat and output per labour-hour is flat since 2022 — there is no evidence of excess labour or declining productivity to cut into.
- Plants run two shifts at ~94% capacity. With no productivity slack shown in the data, a 15% cut in heads implies a roughly proportional cut in output, not a cost saving at constant output.
- Modelled through to 2027: the only way the cut reaches the 15% margin target is the assumption that output stays exactly at plan despite 15% fewer workers — unsupported by the capacity and productivity data. The realistic case, where lost capacity is taken first from hotel volume to protect hospital service levels, produces EBIT around EUR1.4m and a margin near **4–5%** — worse than today — because fixed costs don't shrink and the lost revenue outweighs the labour saving.
- Hospital contracts carry 24-hour turnaround penalties; a capacity cut that risks missing turnaround on contracted hospital volume creates a penalty cost not even included in the above, and would also undercut the leverage needed to negotiate indexation at the 2026/2027 renewals.
- The data doesn't distinguish plant-floor (direct) headcount from administrative/overhead headcount. If there is overhead headcount, a smaller, targeted reduction there could be a modest complementary lever on the fixed cost line — but nothing in the data sizes this, and it is not where the 7.5pp margin decline came from, so it should not be the primary fix.

## Trap checks

- [x] Diagnosis came before any cost target — bridge built first; the client's cure (headcount cut) was carried through as one hypothesis and killed by the data, not assumed.
- [x] Averages broken down — hospital vs. hotel contribution margin shown separately; hospital is where the squeeze is concentrated.
- [ ] Benchmarks normalised for scope/scale — not possible with the peer data given (single survey figure); flagged as weak evidence above, not used as a sized input.
- [x] All actions in one reconciled bridge, no euro counted twice.
- [x] Contract renewal timing (40%/60% in 2026/2027) built into the phasing.
- [ ] Liquidity checked — no data provided; flagged as an open question, not assumed safe.
- [x] No action cuts capability the recovery depends on — this is exactly the risk flagged against the headcount cut (it would cut the capacity and SLA performance the hospital book, and the renewal negotiations, depend on).
- [x] Reconciled totals checked against the reported EBIT change (bridge sums exactly).

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Volume grows 2025→2027 on the 2022–25 trend | Hospital 22.2m kg, hotel 9.5m kg by 2027 | Linear extrapolation of 3-year trend | Demand plateaus or declines; target gets harder on either path |
| 2 | Energy/chemical cost per kg holds flat at EUR0.29 from 2025 to 2027 | EUR0.29/kg | No forward data given; conservative/simple hold | Energy/chemicals keep rising at the 2022–25 rate (+~EUR0.037/kg/yr): the indexation case still reaches ~14% margin if indexation also covers the further rise, but the no-indexation (headcount-only) case gets markedly worse |
| 3 | Labour wage rate per hour holds flat | EUR0.42/kg equivalent | Matches 2022–25 pattern (flat despite volume growth) | Wage inflation emerges: adds a cost pressure not in either plan and strengthens the case for indexation over headcount cuts (labour becomes a real driver only then) |
| 4 | Indexation at renewal recovers 70–100% of the EUR0.11/kg cost gap on hospital volume, phased with the 40%/mid-2026, 60%/mid-2027 renewal schedule | Base case: 100% by full renewal (2027) | Matches stated peer practice (14–16% margin with indexation); recovery rate is a negotiation outcome, not observed | Customers resist and only partial indexation is achieved: still closes most of the gap (≈14% margin at 70% recovery) |
| 5 | A 15% headcount cut without indexation forces a roughly proportional capacity/volume cut, taken first from uncontracted hotel volume to protect hospital SLAs | Headcount-cut scenario range: 4–5% to 15% margin, wide because the "no volume loss" case is not supported by the capacity data | 94% capacity utilisation, flat kg/labour-hour, two-shift operation | Saltmarsh can show material indirect/overhead headcount separable from plant floor — narrows the range toward the upper end, but doesn't change the recommendation |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Cash runway and covenant headroom | Determines whether this is a profitability question or a liquidity question first | Saltmarsh CFO/finance | If liquidity is at risk, sequence a cash plan before either the indexation programme or any restructuring |
| Split of current headcount between plant floor (direct) and admin/overhead (indirect) | The data cannot currently separate a defensible overhead trim from a capacity-cutting plant-floor cut | Saltmarsh HR/finance | Could size a smaller, legitimate overhead action as a complement to indexation — not a substitute for it |
| Forward energy/chemical price outlook for 2026–2027 | Base case assumes flat cost; this is the single biggest swing factor in the forecast | Saltmarsh procurement / energy supplier contracts | A further rise without indexation widens the gap considerably; with indexation in place it matters much less |
| Actual terms achievable at the 2026/2027 hospital renewals (which customers, contract language, negotiating leverage) | Determines whether 70% or 100% of the cost gap is recoverable | Saltmarsh commercial/sales team, contract files | Sets where in the 14–16% range the 2027 outcome lands |
| Severance cost and notice periods if any headcount action proceeds | Not quantified here — no wage/headcount data provided | Saltmarsh HR, legal | Needed before costing any reduced, overhead-only action; labour law/works council input needed if Saltmarsh operates under such obligations |
| Peer survey methodology (sample, normalisation, self-reporting checks) | Currently weak evidence, used only as corroboration | Trade association | Could strengthen or weaken the external benchmark; does not change the internal bridge, which stands on its own |

## Specialists and review

Labour law/works council input is needed before any headcount reduction is finalised (consultation requirements, severance obligations) — not assessed here. Legal review of hospital contract renewal language (indexation clause drafting, SLA/penalty terms) is needed before the 2026 renewal round. This analysis has not been reviewed by a second partner; recommend one review pass before it goes to the board, given it contradicts the CEO's stated proposal.

