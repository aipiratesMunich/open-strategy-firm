# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | No clarifying questions were asked; the response proceeds directly with assumptions labeled ASSUMPTION (e.g., staff cost, trading days, discount rate) rather than stalling. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs, or a lower figure consistent with any extra variable cost | yes | "Revenue €24.00 − food cost (30%) €7.20 − platform commission (28%) €6.72 = **€10.08 contribution/order** (42% of basket)." |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost and discount rate get reason+range ("range €85k–€115k"; "range 8–12%"), but trading days ("ASSUMPTION 350 days" with no reason/range), horizon ("5-year horizon" bullet with no ASSUMPTION tag, reason, or range), and ramp (discussed only as an unflagged risk: "Ramp-up — 120/day is presumabl |
| Labels "maybe 120 orders a day" as an unsourced estimate and makes it the first driver tested | yes | "this is your own unsourced "maybe 120" — the deciding variable, tested first" |
| Gives break-even orders per day with the formula shown, consistent with its stated fixed cost | yes | "Break-even orders/day = fixed costs ÷ (contribution × trading days/year...) = 186,000 ÷ (10.08 × 350) = ~53 orders/day" — consistent with its own stated €186k fixed cost (90k rent + 96k staff). |
| Gives the answer as a range or scenarios with a clear decision rule and names the comparison that would settle volume | yes | Low/base/high scenario table (70/120/160 orders/day) plus "Decision rule: go if an 8–12 week pilot/ramp shows sustained volume ≥80/day..." and "asking the delivery platform for catchment-area demand data" / an 8-week soft launch to get real order data. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | yes | "Cannibalization — if any of these 120 orders/day would've come through an existing channel (current restaurant, existing delivery listing), they're not incremental. This is the biggest unstated risk." |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three drivers beyond those given and named missing ones, each flagged | NO | The decision rule only appears in section 3 after the full scenario/NPV table (with payback and NPV by scenario) has already been presented, so the one-screen summary (contribution, break-even, decision rule) is not completed before the detailed model is shown. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | yes | No external market/competitor data or demand benchmarks are asserted as fact; reasoning like "typical loaded cost for kitchen crew in a European urban market" is offered only as justification for a labeled ASSUMPTION, not as a sourced fact. |
| Must not give a single-point NPV with no range | yes | NPV is given across three scenarios (−€119k, +€550k, +€1,085k) plus a sensitivity check at 15% discount rate, not as a single point. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

## Quick read: Brightwell dark kitchen — provisional yes, but one number needs checking before you sign anything

**1. Contribution per order**
Revenue €24.00 − food cost (30%) €7.20 − platform commission (28%) €6.72 = **€10.08 contribution/order** (42% of basket).

**2. Operating break-even volume**
Fixed costs/year = rent €90k + staff `ASSUMPTION` ≈ €96k (3 staff × ~€32k fully loaded — no cost given, reason: typical loaded cost for kitchen crew in a European urban market; range €85k–€115k) = **€186k/year** (range €175k–€205k).

Break-even orders/day = fixed costs ÷ (contribution × trading days/year, `ASSUMPTION` 350 days)
= 186,000 ÷ (10.08 × 350) = **~53 orders/day** (range 50–58).

Your 120/day estimate is ~2.2x break-even operationally — comfortable cushion.

**3. Low / base / high on orders/day** (this is your own unsourced "maybe 120" — the deciding variable, tested first)

| Case | Orders/day | Annual EBITDA* | Simple payback on €350k fit-out | 5yr NPV @10%** |
|---|---|---|---|---|
| Low | 70 | €61k | 5.7 yrs | **−€119k** |
| Base | 120 | €237k | 1.5 yrs | +€550k |
| High | 160 | €378k | 0.9 yrs | +€1,085k |

*EBITDA ≈ cash flow here (no tax/maintenance capex — fine for a quick check, not for a signed decision).
**Discount rate `ASSUMPTION`: 10% (typical hurdle for mid-size F&B growth capex; range 8–12%). Doesn't flip the answer — even at 15% base-case NPV is still +€446k. **Volume, not discount rate, is what decides this.**

NPV-positive threshold (5yr, 10%) works out to **~79 orders/day** — higher than operating break-even because it also has to earn a return on the €350k, not just cover costs.

**Decision rule:** go if an 8–12 week pilot/ramp shows sustained volume ≥80/day; treat anything sustained below ~60/day as a stop-and-reassess signal.

**4. Assumptions I added (flag before you act on this):**
- Staff cost €96k/yr — unsourced, ±20% swing possible
- 350 trading days/yr
- 10% discount rate
- 5-year horizon
- Cash flow ≈ EBITDA (no tax, no maintenance capex, no working capital)

**5. Things you didn't mention that could flip this:**
- **Cannibalization** — if any of these 120 orders/day would've come through an existing channel (current restaurant, existing delivery listing), they're not incremental. This is the biggest unstated risk.
- Is packaging/consumables inside the 30% food cost, or on top?
- Platform fixed fees or required ad spend beyond the 28% take rate?
- Ramp-up — 120/day is presumably steady-state; month 1–3 is typically 40–60% of that, pushing payback out a few months.
- Lease/exit terms if volume disappoints — the €350k fit-out is sunk once built.

**6. Cheapest evidence before you commit €350k:** an 8-week soft launch (shared/cloud kitchen slot, or spare capacity if you have an existing site) to get a real orders/day number, plus asking the delivery platform for catchment-area demand data. Both are cheap and directly settle the one number this decision hinges on.

**Bottom line for next week:** directionally yes — base case pays back in ~18 months and the discount rate doesn't change that. But don't sign the lease off a "maybe 120" — get even 4 weeks of real order data first, since the downside case (70/day) is NPV-negative.

Want the full model (CSV/Excel with live formulas, tornado chart, scenario tabs) instead of this back-of-envelope version?


## Files in work dir after run


