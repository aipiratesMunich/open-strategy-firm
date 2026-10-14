# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states 4% growth in a 9% market is share loss, not a healthy core. | yes | "Corvina's share: 8.00% (2023, 48/600) → 7.29% (2025, 52/712.9)" and "Core is not 'healthy' relative to its market — it is losing share" |
| Sizes what holding share would be worth (~EUR 73m in 2029, or ~EUR 12-13m above the plan's core) and makes the cause of share loss the first question to answer. | NO | The only 'claw-back' scenario shown is core growing at 6%/yr → EUR 65.6m (not the ~EUR 73.4m 'hold 2025 share, grow with market' figure). The cause-of-share-loss question ('What is driving the core's share loss...') is listed 4th of 5 in the Open Questions table, not framed as the first question to  |
| Shows franchise carries almost the whole gap, treats the 0→110 café ramp as unproven (widens range, compares to/flags missing comparable franchise launches, notes no operator signed). | NO | Franchise is framed as '61% of all required growth' (14/23m) rather than as covering almost the entire gap beyond the core's own continued trajectory (~99%, i.e. 14.0 of 14.2m); this materially understates franchise's true share of the incremental effort. Ramp is called 'a fast ramp even by the stan |
| Flags that the 9% market growth comes from a trade-association figure quoted second-hand and should be checked at source. | yes | "Single source: trade association yearbook 2025, quoted second-hand in the investor update — unverified" and next step "Verify the 9% market-growth figure against a second source" |
| Concludes the plan as drafted is not the right plan (or not yet), with a reordered answer: fix core share loss first, franchise as option/later lever with proof point. | NO | Conclusion does reject the plan ('No — reject the plan as written'), but the Next Steps table places 'Sign 2-3 pilot franchise operators...' as the first action, ahead of 'Size a named core share-defense initiative' which appears fourth — the reverse of the required core-first ordering. |
| Shows profit next to revenue or flags the plan lacks it, and checks the 8% EBIT floor or names it as unknown. | yes | "No core or franchise margin figures appear anywhere in the source document, despite 'EBIT margin at least 8%' being one of three explicit investor conditions... This cannot currently be assessed; it must be before the plan is approved." |
| Shows the remaining gap openly under its own levers. | yes | Stress-test table shows deltas vs EUR 75m target: -0.2m, -4.7m, -9.7m, -14.2m (-19%) under various lever scenarios. |
| Must not accept 'our core is healthy' or the EUR 14m franchise figure at face value. | yes | Both are explicitly challenged: core reframed as share loss, and franchise unit economics back-solved and flagged as '2-4x' typical benchmarks. |
| Must not invent reasons for share loss as facts (may list as hypotheses to test). | yes | Share-loss drivers (pricing, distribution, competitor) appear only as an open question ('What is driving the core's share loss... — pricing, distribution, a specific competitor?') and as a future costed-lever suggestion, not asserted as fact. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

I pressure-tested the plan and saved the full answer page to `case-growth-strategy-corvina.md`. Bottom line:

**No — reject the plan as written.** It nets to EUR 74.8m with zero cushion, and the two numbers it rests on don't hold up:

1. **"Healthy core" is actually share loss.** Core grew 4.1%/yr (2023-25, matches the planned 4%) while the market grew 9%/yr per the trade-association figure quoted — so Corvina's share fell from 8.00% to 7.29% already, and the plan's own assumptions project it falling to 6.04% by 2029 (-24% relative over six years). Continuing at 4% isn't a safe baseline, it's a lever that needs active share-defense to even hold.

2. **The franchise math doesn't check out.** EUR 14m from 110 cafés implies ~EUR 127k revenue per café — 2-4x what typical franchise royalty + supply economics would suggest (flagged as assumption-based since no benchmark was supplied). Combined with zero signed operators today against a 25-unit target in 2027, this lever (61% of all required growth) is unvalidated, not a base case.

3. **EBIT margin — the explicit ≥8% investor hurdle — is never addressed.** Franchise build-out costs are typically margin-dilutive while scaling, and the plan is silent on margin throughout.

Stress-testing shows the base case sits exactly on the EUR 75m target with no buffer; either the core's share erosion continuing, or franchise unit economics landing near sector norms, pushes the outcome 6-13% short — and both together put Corvina back near today's revenue despite spending the EUR 4.5m.

The full page includes the scenario table, unit-economics back-solve, assumptions (clearly labeled, since I had no web access to verify the market-growth source or franchise benchmarks), and five concrete next steps — pilot the franchise before scaling, verify the market data, build an EBIT bridge, cost a core share-defense lever, and replace "remaining gap: none" with an honest number.


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy: Corvina Coffee Roasters, does the 2026-2029 plan reach EUR 75m revenue at ≥8% EBIT within EUR 6m investment?

**Answer:** No — as written, reject the plan. It nets to EUR 74.8m with **zero** cushion, by stacking 61% of all required growth (EUR 14m of the EUR 23m gap) onto a café-franchise concept with no signed operator, implied per-unit economics 2-4x typical franchise benchmarks, and no stated EBIT effect against the 8% floor. Rebuild it as two defensible levers (defend/rebuild core share explicitly costed, plus a piloted franchise rollout sized from real unit data) with a visible margin bridge and an honest remaining gap, before taking it to the investors.

**Confidence:** Low-medium, because two of the three load-bearing numbers (sustainable core growth given market context, and franchise unit economics/ramp) are unverified or contradicted by the data given, and the plan carries no margin for either to disappoint. Would rise to medium-high if a signed pilot franchise validates unit revenue within ~30% of the plan's implied EUR 127k/café, and management produces an EBIT bridge showing ≥8% is held throughout the ramp, not just in 2029.

**Specialists and review:** Franchise legal/compliance (franchise disclosure documents, operator agreements — none signed yet); financial due diligence on the trade-association market data (single, second-hand-quoted source); a partner/independent review of the margin bridge once management produces one.

## The gap

| | 2023 | 2025 | 2029 target |
|---|---|---|---|
| Revenue | 48.0 | 52.0 | 75.0 |
| Gap to close (2025→2029) | | | **23.0** |
| Constraints | capital ≤ EUR 6m, EBIT margin ≥ 8%, decision for investors |

Management's own summary table nets to **EUR 74.8m**, EUR 0.2m short of the literal EUR 75m target — yet is labelled "remaining gap: none." A small thing, but it is a tell: this is a plan built backward from the target, not forward from evidence.

### Core is not "healthy" relative to its market — it is losing share

- Core CAGR 2023→2025: (52/48)^0.5 − 1 ≈ **4.1%/yr** — this is what the plan calls "solid growth," and its own recent trend does support continuing near 4%.
- But the served market (per the trade yearbook figure quoted in the investor update) grew **9%/yr** over the same period: EUR 600m (2023) → EUR 712.9m (2025) = 600 × 1.09².
- Corvina's share: **8.00%** (2023, 48/600) → **7.29%** (2025, 52/712.9) — a loss of 0.71 points, ~9% relative, in two years.
- Project the plan's own assumptions forward (core +4%/yr, market +9%/yr): 2029 core = EUR 60.8m (52 × 1.04⁴, matches management's table); 2029 market = EUR 1,006.7m (712.9 × 1.09⁴); 2029 share = 60.8/1,006.7 = **6.04%**.
- Net: share falls from 8.00% to 6.04% over six years — **down ~24% relative**, continuing at roughly the pace already seen. "The core is healthy" should read "the core is shrinking in relative terms, and the plan does nothing to change that."

**Hypothesis (core): market grows ~2% and the core merely under-participates → KILLED.** Market is growing fast (9%, if the single source holds) and the core is actively losing share to competitors. The right question is not "is the core safe to leave on autopilot" but "why is Corvina losing share in a growing market, and what would it cost to stop."

## Levers

| Lever | Revenue, base case 2029 | Range | EBIT effect | Investment | Evidence grade | Decision |
|---|---|---|---|---|---|---|
| Core wholesale, continue at 4%/yr | EUR 60.8m | EUR 56.3m (if share erosion continues/intensifies, growth slows to ~2%/yr) to EUR 65.6m (if Corvina claws back share, ~6%/yr) | not stated anywhere in the plan | not stated | medium — extrapolates trend, but trend is losing share, not "healthy" | keep, but reframe as "defend share," costed explicitly |
| Café franchise, 0→110 units | EUR 14.0m | EUR 4-5m (unit economics ⅓ of plan, see below, and/or 1-year ramp slip) to EUR 14.0m (plan delivers in full) | not stated; franchise launch costs (team, brand, flagship, recruitment) are typically margin-dilutive while scaling | EUR 4.5m of the EUR 6m cap (75%) | weak — zero signed operators, no pilot, no disclosed per-unit assumptions | reshape: pilot before scaling |

**Sum of kept levers (management's base case):** EUR 74.8m; **remaining gap:** EUR 0.2m on management's own numbers, materially larger once the franchise lever is evidence-adjusted. **How it is currently closed:** by assumption, not by evidence — see unit economics below.

### Franchise unit economics, back-solved

EUR 14.0m / 110 cafés = **≈ EUR 127,300 revenue per café per year** (royalty + coffee supply combined), with no per-unit assumption disclosed in the plan.

Sanity check against typical franchise structures (figures below are **ASSUMPTION ranges, unverified — flagged, not sourced**, since no comparable-concept or trade data was supplied):
- Typical specialty café unit revenue: ASSUMPTION, EUR 350k-550k/yr.
- Typical combined franchisor take (royalty ~5-8% of unit sales + coffee/supply margin ~3-6%): ASSUMPTION, ~8-14% of unit sales.
- Implied franchisor revenue per unit at these assumptions: EUR 28k-77k, midpoint ~EUR 48k.
- **The plan's EUR 127k/unit is roughly 1.6x to 4.5x this assumption-based range** (midpoint ratio ~2.6x).

Separately, the ramp itself is aggressive on an outside view: 0 signed operators today, 25 units open in 2027 (the franchise's first operating year), +35 to reach 60 in 2028, +50 to reach 110 in 2029. A brand-new, unlaunched franchise concept recruiting, vetting and opening 25 financed operators within roughly 12-15 months of having zero today — before even one flagship has run a full year to prove the model — is a fast ramp even by the standards of established franchise systems scaling a proven format.

**Hypothesis (franchise): EUR 14m by 2029 is a reasonable base case → KILLED/RESHAPE.** Kill criterion met twice over: no signed operator today against a 2027 opening target, and implied per-unit revenue 2-4x an (unverified, assumption-based) sector range. Treat the EUR 14m as an upside case pending a validated pilot, not the base case.

### Stress test — combined scenarios

| Scenario | Core 2029 | Franchise 2029 | Total | vs. EUR 75m target |
|---|---|---|---|---|
| Plan (as management states it) | 60.8 | 14.0 | 74.8 | -0.2m (~0%) |
| Core share-erosion continues (core +2%/yr) | 56.3 | 14.0 | 70.3 | -4.7m (-6%) |
| Franchise unit economics ⅓ of plan | 60.8 | ~4.5 | 65.3 | -9.7m (-13%) |
| Combined downside | 56.3 | ~4.5 | 60.8 | -14.2m (-19%) |
| Upside (core claws back share to +6%/yr, franchise delivers in full) | 65.6 | 14.0 | 79.6 | +4.6m (+6%) |

The base case lands exactly on the target with no cushion. Either one of two plausible, individually-likely disappointments (continued share erosion in the core, or franchise unit economics landing where comparable benchmarks would suggest) pushes the result 6-13% below target; both together put Corvina back near where it is today despite spending the EUR 4.5m.

### EBIT margin — the plan is silent on an explicit investor hurdle

No core or franchise margin figures appear anywhere in the source document, despite "EBIT margin at least 8%" being one of three explicit investor conditions (alongside revenue and capital). Franchise build-out (franchise team, brand development, a flagship store, operator recruitment) is a cost incurred ahead of the royalty/supply revenue it enables, and is typically margin-dilutive while the unit count is still ramping — which, on this plan, it still is throughout 2029 (50 of 110 units open that year). **This cannot currently be assessed; it must be before the plan is approved.**

## Killed options and why

- **"Core growth of 4%/yr needs no further action" — killed.** The core is losing share in a market growing more than twice as fast; 4% is not a safe baseline, it is itself a lever that needs an explicit share-defense initiative (pricing, named-competitor response, key-account retention) if it is to be relied upon.
- **"EUR 14m franchise revenue in 2029 is the base case" — killed, reshape to pilot-first.** No signed operator, no disclosed unit assumptions, implied per-unit revenue 2-4x an assumption-based sector range, and a recruitment/opening pace that outruns what a brand-new concept can usually validate in time.

## Risks and what would change the answer

1. If the trade-association market-growth figure (9%/yr, single source, quoted second-hand in the investor update) is overstated, the core's relative share loss is smaller than calculated here — but the core's absolute growth is still only 4%, well below any plausible double-digit market, so the "healthy core" framing is weakened either way.
2. If franchise unit economics, once a pilot runs, come in near the plan's EUR 127k/unit, the franchise lever is sound and the main remaining risk is execution speed and margin during ramp.
3. If the investors' EBIT floor is breached in interim years (2027-2028) even while 2029 figures look on-plan, the plan still fails its mandate — revenue-only tracking would miss this until too late.

## Next steps

| What | Who | By when |
|---|---|---|
| Sign 2-3 pilot franchise operators and run one flagship 12 months to generate real unit revenue, royalty and supply-margin data | Corvina franchise team | before any 2027 scale-up decision |
| Verify the 9% market-growth figure against a second source (e.g. national statistics, a second trade body, competitor filings) | Corvina strategy/finance | before using it to defend the core plan |
| Produce a full EBIT bridge: current core margin, franchise launch-cost drag by year, consolidated margin 2026-2029 against the 8% floor | Corvina finance | before the plan goes back to investors |
| Size a named core share-defense initiative (pricing, key accounts, named competitors) as an explicit, costed lever rather than assumed-safe baseline | Corvina wholesale team | next planning cycle |
| Rebuild the plan with an honest remaining gap and a stated contingency within the EUR 6m cap, rather than "remaining gap: none" | Corvina management | before investor sign-off |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | National wholesale coffee market was EUR 600m in 2023 and grew 9%/yr since | 9%/yr, EUR 600m base | Single source: trade association yearbook 2025, quoted second-hand in the investor update — unverified | A second, independent source shows materially lower/higher growth |
| 2 | Typical specialty café unit revenue | EUR 350k-550k/yr | ASSUMPTION — no comparable-concept or sector data supplied; wide range, unverified | Actual comparable café/franchise disclosures put typical unit revenue near EUR 1m+ (would support the plan's implied EUR 127k/unit) |
| 3 | Typical combined franchisor take (royalty + coffee/supply margin) | ~8-14% of unit sales | ASSUMPTION — no franchise agreement terms disclosed; unverified | Corvina's actual/planned structure takes a materially higher share of unit sales (e.g. because coffee supply is priced at a large markup, not wholesale) |
| 4 | Franchise units open evenly through the year for revenue purposes | Not separately modelled; used management's single annual revenue figure | No monthly/quarterly build given | Management discloses a ramp-adjusted (café-year) revenue build that differs materially from the flat EUR 127k/unit average |
| 5 | Core EBIT margin and franchise launch-cost drag | Not sized — no data given | No margin figures anywhere in the source document | Management discloses current and projected margins |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is Corvina's current core EBIT margin, and the franchise's projected margin drag by year? | The investor mandate has an explicit ≥8% EBIT floor; the plan addresses only revenue | Corvina finance | Could invalidate the plan even if revenue hits EUR 75m |
| What per-café revenue, royalty rate and supply margin underlie the EUR 14m 2029 franchise figure? | Needed to validate or kill the back-solved EUR 127k/unit figure against real assumptions | Corvina franchise team | Narrows the EUR 4-14m franchise range substantially either way |
| Is there a signed or near-signed franchise operator, letter of intent, or pilot underway not mentioned in this draft? | The document states none has been signed; if one exists, execution risk is lower than assessed here | Corvina management | Would raise confidence in the franchise lever |
| What is driving the core's share loss against a 9%-growing market — pricing, distribution, a specific competitor? | Needed to decide whether 4%/yr is defensible or whether a share-defense lever should be added and costed | Corvina wholesale team | Could add a lever currently missing from the plan entirely |
| Is EUR 6m the hard cap inclusive of core investment and working capital for the franchise royalty/supply ramp, or franchise-only? | EUR 4.5m of 6m is already committed to franchise; unclear if core/logistics/working-capital needs are funded from the remaining EUR 1.5m or elsewhere | Corvina finance/investors | Could show the plan is already over the capital limit once full costs are counted |

