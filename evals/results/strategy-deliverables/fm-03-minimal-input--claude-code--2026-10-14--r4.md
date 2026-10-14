# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | No clarifying questions were asked; model proceeded directly with assumptions marked 'ASSUMPTION' (e.g. '–€114k *(ASSUMPTION: ~€38k/head fully loaded — not given, confirm)*') rather than stalling. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs | yes | 'Contribution per order = €24 × (1 − 30% − 28%) = €10.08' |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Only staff cost is explicitly flagged ('ASSUMPTION: ~€38k/head... confirm') and without a range; 360 trading days, the 5-year horizon, and discount rate are used/tested but never labeled ASSUMPTION with reason+range, and no ramp-up period is mentioned or flagged at all. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | yes | 'the case isn't fragile to cost creep — it's fragile to one thing: whether 120 orders/day is real, validated demand, not a hopeful target' and recommends 'Get a real demand number for 120 orders/day... before signing the lease — that's the only lever that flips this.' |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost (about 60 with the illustrative figures) | yes | 'Fixed costs (rent + labor) = €204k/yr → breakeven ≈ 56 orders/day (≈70/day if you include the opex buffer)' — consistent with its own stated €204k fixed cost and €10.08 contribution. |
| Gives the answer as a range/scenarios with a clear decision rule, and names the comparison that would settle volume | NO | Decision rule given ('If sustained volume comes in below ~60-70/day, the project loses money; above that, it's comfortably profitable') but no explicit order-volume scenario set (e.g. 60/90/120) is modeled, and the suggested validation ('pre-orders, platform category data, a comparable site') does n |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | NO | No mention of cannibalisation of existing store delivery orders anywhere in the response. |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three extra flagged drivers | NO | Response opens with 'Short answer: yes' then immediately presents a full annual P&L table (revenue, costs, EBITDA) before stating contribution per order or break-even, which appear later under separate headers rather than in an upfront one-screen summary. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | yes | No competitor benchmarks, market demand data, or dark-kitchen comparables are asserted as facts; only the user-given 28% commission and 30% food cost are used. |
| Must not give a single-point NPV with no range | yes | 'NPV over 5 years: positive at any sane discount rate — €297k at 12%, €252k at 15%, €187k at 20%.' |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

**Short answer: yes — the numbers clear the bar with real margin for error, but two assumptions I had to invent need checking before you commit.**

## The math (annual, 360 trading days)

| | |
|---|---|
| Revenue | 120 orders/day × €24 × 360 days = **€1,037k** |
| – Food cost (30%) | –€311k |
| – Platform commission (28%) | –€290k |
| **Contribution** | **€435k** (i.e. €10.08 contribution per order) |
| – Rent | –€90k |
| – Labor, 3 staff | –€114k *(ASSUMPTION: ~€38k/head fully loaded — not given, confirm)* |
| – Other opex (packaging/utilities/software, ~5% rev) | –€52k *(ASSUMPTION — not given)* |
| **EBITDA** | **~€180k/yr** |

Capex: €350k fit-out, year 0.

## Headline outputs
- **Payback: ~1.9 years** (sooner, ~1.5 yrs, if you strip the €52k opex buffer — it's a guess either way)
- **NPV over 5 years: positive at any sane discount rate** — €297k at 12%, €252k at 15%, €187k at 20%. You'd need a discount rate well north of 40% to kill it.
- **IRR: ~45-50%**

## What actually decides this: breakeven volume
Contribution per order = €24 × (1 − 30% − 28%) = **€10.08**
Fixed costs (rent + labor) = €204k/yr → **breakeven ≈ 56 orders/day** (≈70/day if you include the opex buffer).

Your plan is 120/day — that's a **40-55% volume cushion**. Stress-tested:
- Platform commission up to 32%: breakeven still only ~62/day
- Food cost up to 35%: breakeven still only ~64/day

So the case isn't fragile to cost creep — it's fragile to one thing: **whether 120 orders/day is real, validated demand**, not a hopeful target. If sustained volume comes in below ~60-70/day, the project loses money; above that, it's comfortably profitable.

## Recommendation
**Go**, conditional on:
1. Confirm labor cost (€114k is my estimate, not yours) and discount rate — neither changes the yes/no here, NPV stays positive even if labor runs 20% hotter.
2. Get a real demand number for 120 orders/day (pre-orders, platform category data, a comparable site) before signing the lease — that's the only lever that flips this.

No model file built — this was back-of-envelope per your "fast, plain text" ask. Say the word if you want it turned into a proper versioned model with scenarios before it goes to whoever signs off.


## Files in work dir after run


