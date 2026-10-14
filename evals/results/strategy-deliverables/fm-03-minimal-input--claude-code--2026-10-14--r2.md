# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (4/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks questions in one message and continues with flagged assumptions rather than stalling | yes | Proceeds with a provisional yes and assumed staff cost, then lists missing items ('Actual staff cost — I guessed...') instead of stalling for answers. |
| States contribution per order: EUR 10.08 (42% of basket) from given inputs | yes | 'Contribution per order = €24 × (1 − 30% food − 28% platform) = €10.08' |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with reason and range | NO | Staff cost is given as a single guess ('assuming ~€32k fully loaded per head') with no range or 'ASSUMPTION' label; discount rate is dismissed ('Don't burn time picking one') rather than assumed with a range; trading days (365) and ramp are mentioned in passing, not formally flagged as ASSUMPTION wi |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | NO | The 120/day figure is treated as a fixed input throughout ('Your plan is 120/day → ~2.4x cushion') with no flag that it is an unsourced guess, and it is not tested as a sensitivity driver. |
| Gives break-even orders per day with formula shown, consistent with stated fixed cost | yes | 'Breakeven volume = €186k ÷ €10.08 ≈ 50 orders/day' is internally consistent with its own €186k fixed-cost assumption. |
| Gives answer as range/scenarios with decision rule and names a comparison to settle volume | NO | Only a single-point 120/day scenario with a cushion multiple is given; no 60/90/120-style scenario set, no decision rule, and no named comparison (e.g., existing store delivery volumes or a platform test) to validate the 120/day figure. |
| Notes cannibalisation of existing store delivery orders as a driver | NO | No mention of cannibalisation of existing store delivery orders anywhere in the response. |
| Leads with one-screen answer before full model; adds at most three extra drivers beyond given/named missing ones | NO | The 'What would change my answer' section lists four added drivers (staff cost, packaging/delivery supplies, ramp-up, platform dependency), exceeding the three-driver cap. |
| Does not invent market data on delivery demand, platform commissions, or competitor dark-kitchen results as facts | NO | States as fact 'packaging... typically 3-5% of revenue for delivery-only' and 'normal hurdle periods for F&B capex (typically 3 years)' without sourcing, presenting invented benchmarks as established facts. |
| Does not give a single-point NPV with no range | yes | No NPV calculation is performed at all; only payback period is computed, with two scenario figures (1.4 years and 1.8 years at a reduced day count). |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

**Provisional yes** — but confirm two missing numbers before you commit.

**Breakeven (doesn't need a discount rate)**
- Contribution per order = €24 × (1 − 30% food − 28% platform) = **€10.08**
- Need to cover rent + staff. Staff cost wasn't given — assuming ~€32k fully loaded per head (3 staff = €96k), fixed costs = €90k rent + €96k staff = **€186k/year**
- Breakeven volume = €186k ÷ €10.08 ≈ **50 orders/day**
- Your plan is 120/day → **~2.4x cushion** above breakeven. That's a comfortable margin even if volume undershoots for months.

**Payback on the €350k fit-out**
- Annual revenue (120 × €24 × 365 days) ≈ **€1.05m**
- After food cost + platform cut + staff + rent: **~€255k/year contribution**
- Payback ≈ **350k ÷ 255k ≈ 1.4 years**

Even at a conservative 6-day week (312 days) instead of 365, payback only stretches to ~1.8 years. Either way it's well inside normal hurdle periods for F&B capex (typically 3 years) — this is why the discount rate barely matters here: at this payback speed, 8% vs 15% WACC won't flip the decision. Don't burn time picking one.

**What would change my answer**
1. **Actual staff cost** — I guessed €32k/head. If it's meaningfully higher (e.g. night/weekend premiums), rerun the breakeven line.
2. **Packaging/delivery supplies** — not in your numbers, typically 3-5% of revenue for delivery-only. Add it to food cost line.
3. **Ramp-up** — 120 orders/day on day one is unlikely; realistic payback probably lands closer to 2 years once you factor a 3-6 month ramp.
4. **Single-platform dependency** — 28% take rate is steep; worth knowing if that's locked in or renegotiable at volume.

Get real staff cost + packaging cost from finance/ops this week — plug them into the same two formulas above and you'll have your answer confirmed. If you want this turned into a one-page board memo with sensitivities (volume, take-rate, staff cost) before the meeting, say so and I'll build it.


## Files in work dir after run


