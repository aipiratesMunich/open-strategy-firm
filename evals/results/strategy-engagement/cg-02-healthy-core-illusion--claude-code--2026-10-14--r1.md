# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states 4% growth in a 9% market is share loss, not a healthy core | yes | "2023: Corvina = EUR 48m / EUR 600m market = 8.0% share... 2025: market ≈ EUR 713m; Corvina = EUR 52m / EUR 713m = 7.3% share... the core did not stall; it is losing share..." |
| Sizes what holding share would be worth (~EUR 73m in 2029, or ~EUR 12-13m above plan's core) and makes the cause of share loss the first question to answer | NO | Document sizes holding-share value ('core revenue alone would be ≈ EUR 73.5m') but never asks WHY share is being lost as a question to investigate; Next Steps/Open Questions jump straight to 'size and cost a core share-defense lever' and verifying the market-growth source, with no item diagnosing th |
| Shows franchise carries almost the whole gap and treats the 0→110 cafés ramp as unproven: widens range, compares with (or names as missing) comparable franchise launches, notes no operator signed | yes | "The plan assigns EUR 14.0m of the EUR 14.2m gap to the franchise"; "Range — EUR 0 ... to EUR 14.0m"; "No outside-view comparison is given against how comparable café-franchise systems actually ramped"; "No franchise operator has been signed." |
| Flags that the 9% market growth figure is second-hand (trade association) and should be checked at source | yes | "a single, secondary-sourced figure, not yet verified against the primary yearbook"; next step: "Verify the 9%/year market-growth figure against the primary trade-association yearbook" |
| Concludes plan as drafted is not the right plan, with reordered answer: fix core share loss first, franchise as option/later lever with proof point | yes | "Answer: No — not as drafted. Reject or send back for rework."; core lever decision: "keep, but reshape — size and fund a share-defense option"; franchise decision: "option, not 'keep' — needs a signed pilot ... before being treated as committed revenue" |
| Shows profit next to revenue or flags plan lacks it, and checks 8% EBIT floor or names as unknown | yes | "No EBIT figures anywhere, despite the investor mandate's 8% margin floor"; levers table EBIT effect column: "not disclosed" |
| Shows the remaining gap openly under its own levers | yes | "Sum of kept levers (plan's base case): EUR 74.8m... the arithmetic is actually EUR 0.2m short even on the plan's own numbers (60.8 + 14.0 = 74.8, not 75.0)" |
| Must not accept 'our core is healthy' or the EUR14m franchise figure at face value | yes | "the 'healthy core' is actually losing ground"; franchise treated as "weak" evidence grade, "not killed, but currently unverifiable" |
| Must not invent reasons for the share loss as facts (only as hypotheses) | yes | No named competitors, specific price levels, or customer quotes are asserted as facts; only generic unsized levers like 'pricing, key accounts, sales capacity' are proposed as a lever to size, not asserted causes. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

The plan's own numbers contradict its headline: using management's own cited market growth (9%/year since 2023 vs. a 48→52m core), Corvina's wholesale share fell from 8.0% to 7.3% in just two years — the "healthy core" is actually losing ground in a fast-growing market — and 61% of the growth needed to hit €75m (€14m of the €22.8m gap) is assigned to a franchise business that hasn't signed a single operator yet.

**Verdict: no, not as drafted.** Full pressure test saved to `case-growth-strategy-corvina.md`. Key findings:

1. **Core "health" claim fails its own data.** Flat 4%/year core growth is just an extrapolation of a trend set *while losing share*. If Corvina had simply held its 2025 share (7.3%) through 2029, the core alone would deliver ~€73.5m — almost the whole target, no franchise needed. Management never tested this scenario and budgets €0 to defend share.
2. **The franchise lever (€14m, 61% of the gap) is unvalidated.** Zero operators signed, no benchmark against comparable franchise rollouts, no per-unit economics disclosed, and €4.5m of the €6m investment cap is bet on it alone.
3. **No EBIT figures anywhere**, despite the investor mandate's 8% margin floor — the plan could hit €75m in revenue and still fail the mandate.
4. **Zero cushion:** the two levers sum to €74.8m against a €75m target, with no contingency if either underdelivers even slightly.

The answer page includes the full levers table, risk scenarios (e.g., franchise at half-plan → ~€67.8m, missing target by ~10%), assumptions with their basis, and an open-questions list (verify the market-growth source, build the missing margin bridge, require a signed pilot before treating franchise revenue as committed).


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy: Corvina Coffee Roasters — does the 2026-29 plan reach EUR 75m at ≥8% EBIT margin within EUR 6m capital?

**Answer:** No — not as drafted. Reject or send back for rework. The plan's own market figures show the "healthy core" is actually losing share (8.0% → 7.3% of the wholesale market in just two years), and 61% of the growth needed to close the gap to EUR 75m (EUR 14m of EUR 22.8m) is assigned to a franchise business that has not signed a single operator. The plan also contains no EBIT figures at all, even though the investor mandate has an 8% margin floor. It is an arithmetic fit to the target, not a tested plan.

**Confidence:** Low that this plan reliably delivers EUR 75m at ≥8% EBIT margin. High that it has two specific, nameable flaws — an unexamined core share loss and an unvalidated franchise lever — that must be closed before this goes back to the investors.

**Specialists and review:** Franchise legal (disclosure/registration requirements, before any operator is signed); CFO/FP&A for the missing EBIT bridge; market-research specialist to verify the single secondary-sourced market-growth figure.

## The gap

| EUR m | 2025 | 2029 |
|---|---|---|
| Revenue, momentum case (core only, 2023-25 trend continued) | 52.0 | 60.8 |
| Revenue, target | 52.0 | 75.0 |
| Gap | — | 14.2 |
| Constraints | capital ≤ EUR 6m total, EBIT margin ≥ 8%, ruled out: not stated |

The plan assigns EUR 14.0m of the EUR 14.2m gap to the franchise and claims "no remaining gap" — the arithmetic is actually EUR 0.2m short even on the plan's own numbers (60.8 + 14.0 = 74.8, not 75.0). Minor on its own, but a sign the plan wasn't checked.

## Pressure test 1: is the core really healthy?

Management's own market citation disproves its own headline. The national wholesale coffee market was EUR 600m in 2023, growing 9%/year (trade association yearbook 2025, as quoted in the investor update — a single, secondary-sourced figure, not yet verified against the primary yearbook).

- 2023: Corvina = EUR 48m / EUR 600m market = **8.0% share**.
- 2025: market ≈ 600 × 1.09² ≈ EUR 713m; Corvina = EUR 52m / EUR 713m = **7.3% share**.
- Corvina's own 2023-25 revenue CAGR is 4.1%/year — less than half the cited market growth rate. **The core did not stall; it is losing share at roughly 4-5% relative per year**, and the plan's flat "4%/year" forecast simply extrapolates that same underperformance to 2029 (projected share ≈ 6.0-6.1%).
- The road not taken: if Corvina merely *held* its 2025 share of 7.3% through 2029 (market compounding at 9%/year to ≈ EUR 1.0bn), core revenue alone would be **≈ EUR 73.5m** — almost the entire EUR 75m target, with no franchise required. Management never sized this "defend share" scenario, and budgets EUR 0 to defend or regain core share.

**Hypothesis: "core is healthy and growing" → reshaped to "core is growing in absolute terms but losing share in a fast-growing market, and the plan does nothing to address it."** This reverses the framing in the input document's own title.

## Pressure test 2: can the franchise lever carry 61% of the gap?

- No franchise operator has been signed. The lever goes from zero committed revenue today to EUR 14m and 110 cafés by 2029 — a rollout of 25 units in year one of launch, accelerating to 60 then 110.
- No outside-view comparison is given against how comparable café-franchise systems actually ramped in their first three years (sales/support team build-out, franchise agreements, site selection, training typically make a 25-unit first-year opening count aggressive for a brand-new system).
- No per-unit economics are shown: EUR 14m / 110 cafés = ~EUR 127k average per unit (royalty + coffee supply) blended across cohorts of different vintages — plausible but unverified; no royalty rate, supply margin, or comparable unit volume is disclosed.
- EUR 4.5m of the EUR 6m investment cap is committed to this single, unproven lever, leaving only EUR 1.5m for everything else, including any capacity needed to supply both the core and a fast-growing franchise network.

**Hypothesis: "franchise can deliver EUR 14m by 2029" → not killed, but currently unverifiable; evidence grade weak.** This is the single largest, least-proven number in the plan.

## Levers

| Lever | Revenue base case (2029) | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core wholesale, flat 4%/yr trend | EUR 60.8m | EUR 60.8m (trend continues, share keeps falling to ~6%) to EUR 73.5m (if 2025 share of 7.3% is simply held) | not disclosed | EUR 0 budgeted to defend/regain share | ongoing | medium (2 years of actuals; market-growth source is single/secondary) | keep, but reshape — size and fund a share-defense option before accepting the passive case |
| Café franchise | EUR 14.0m | Wide — EUR 0 (no operator signs) to EUR 14.0m (plan executes exactly); realistic base case likely well below EUR 14.0m given zero signings and a compressed ramp | not disclosed | EUR 4.5m | first revenue not before 2027, full ramp by 2029 | weak — no signed operator, no comparable-launch benchmark | option, not "keep" — needs a signed pilot and 6-12 months of actual unit economics before being treated as committed revenue |

**Sum of kept levers (plan's base case):** EUR 74.8m. **Remaining gap:** effectively the full EUR 14.0m franchise number is unproven, and EBIT is not sized at all. **How the plan closes it today:** by assumption, not evidence.

## Killed options and why

Nothing is formally killed in management's plan — which is itself a gap. The option **"invest to defend or regain core share"** was never evaluated or costed, despite being the cheapest lever on the table (it would use existing sales/pricing/key-account infrastructure rather than building a new franchise system from zero) and despite the core data showing it is needed. This should be sized before the franchise bet is treated as the only way to close the gap.

## Risks and what would change the answer

1. If the franchise delivers only half of plan (plausible for a first-time rollout with zero signed operators), 2029 revenue ≈ EUR 60.8m + EUR 7m = **EUR 67.8m**, roughly 10% short of target — and that is before any further core share loss.
2. If core share loss continues at its current relative rate rather than the flat 4%/year management modelled, the core could still hit EUR 60.8m in revenue while representing a weaker underlying position (share ≈ 6%, down from 8% in 2023) — raising risk for growth after 2029, not just this plan.
3. If franchise coffee-supply margin is similar to or below core wholesale margin (unknown — not disclosed), **hitting EUR 75m in revenue could still miss the 8% EBIT floor**, which is just as much a failure of the investor mandate as missing revenue.
4. The plan has zero cushion (74.8 vs. 75.0 target) and zero contingency lever — a single soft lever (e.g., a modest core share-defense programme) should be added as a buffer rather than relying on two levers that must both land exactly on base case.

## Next steps

| What | Who | By when |
|---|---|---|
| Verify the 9%/year market-growth figure against the primary trade-association yearbook (not just the investor-update citation) and a second source | Strategy/market intelligence | Before the plan is resubmitted |
| Build the missing EBIT bridge for core and franchise and test against the 8% floor | CFO | Before plan approval |
| Sign at least one franchise operator / run the flagship plus one pilot for 6-12 months and capture actual unit economics before committing to a 25-unit 2027 ramp | Franchise lead | Before 2027 budget is locked |
| Size and cost a core share-defense lever (pricing, key accounts, sales capacity) as an alternative or complement to the franchise bet | Core wholesale GM | In parallel with the franchise workstream |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Market grew 9%/year for exactly the same 2023-2025 window as Corvina's own figures | 9%/yr × 2 years | Literal reading of "EUR 600m in 2023 ... grown 9% a year since", matched to the core's 2023-25 reporting window | A different number of years changes the exact share-loss figure, but the direction (core growing slower than the market) holds unless true market growth was below ~4%/yr |
| 2 | Core continues its unmodified 2023-25 trend at 4%/year with no new investment or pricing action | 4%/yr flat | Management's stated plan | If management instead funds a share-defense lever, the core's base case could be materially higher (up to ~EUR 73.5m if 2025 share is simply held) |
| 3 | Franchise and core wholesale margins are unknown | n/a | Not disclosed anywhere in the plan | If franchise margin is materially below core margin, hitting EUR 75m revenue may still fail the 8% EBIT floor |
| 4 | Zero committed franchise revenue today | 0 operators signed | Stated explicitly in the plan | A signed letter of intent or a working pilot would upgrade this lever from weak to medium/strong evidence |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the 9%/year market-growth figure verified against a second, ideally primary, source? | The entire "core is losing share" finding — and the case for an unbudgeted share-defense lever — rests on one secondary-sourced number | CFO / trade association directly | If true market growth is closer to 4%/yr, the core-is-healthy framing stands and the franchise lever becomes the only open risk |
| What EBIT margin does management expect on (a) core wholesale, (b) franchise royalties, (c) franchise coffee supply? | The investor mandate requires ≥8% EBIT margin; the plan has no margin figures at all | CFO | Could kill the plan even if the EUR 75m revenue figure is hit |
| Has any franchise operator signed a letter of intent, and how did comparable café-franchise systems actually ramp in their first three years? | EUR 14m of the EUR 22.8m growth gap (61%) depends on this lever | Franchise lead / outside-view benchmark of comparable brands | A slower comparable ramp, or no signings, removes the lever that currently closes most of the gap |
| What is the EUR 1.5m of investment headroom (EUR 6m cap minus EUR 4.5m franchise) earmarked for — does the core or the franchise supply chain need capex? | The EUR 6m cap is a hard investor constraint | CFO / Operations | If core or supply-chain capex exceeds EUR 1.5m, the plan breaches the investment cap |

