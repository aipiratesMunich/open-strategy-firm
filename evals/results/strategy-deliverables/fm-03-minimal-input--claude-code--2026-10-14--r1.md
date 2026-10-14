# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | No clarifying questions asked up front; response proceeds directly with 'Quick math, not a full model' and flags assumptions inline, ending only with an optional follow-up offer. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs | yes | "Contribution before fixed costs: €10.08/order (42%)" |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost is flagged ("assumed €33k fully-loaded each — you need to confirm this") but trading days and horizon are never mentioned at all, and discount rate is dismissed ("Don't bother picking a discount rate") rather than stated as an assumption with a range. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | NO | 120/day is treated as the given forecast throughout ("Your forecast of 120/day gives a ~43% cushion"); the three flagged drivers to nail down are staff cost, ramp-up, and other opex — volume itself is never flagged as unsourced. |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost | yes | "Fixed costs ≈ €214,000/yr (€586/day). → Breakeven ≈ 68 orders/day" — internally consistent with its own €8.58 contribution and €214k fixed cost figures. |
| Gives the answer as a range or scenarios with a clear decision rule, and names the comparison that would settle volume | NO | Only a single breakeven (68) vs single forecast (120) comparison is given, with no order-volume scenario range (e.g. 60/90/120) and no named comparison data source (e.g. existing delivery orders from nearby stores, a platform test) to validate the 120/day figure. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | NO | No mention of cannibalisation anywhere in the response. |
| Leads with a one-screen answer before any full model; adds at most three extra flagged drivers | yes | Response opens with contribution/breakeven/verdict in one message (no full model), and flags exactly three additional drivers: staff cost, ramp-up, and other opex. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | NO | "typical dark-kitchen opex often runs 8-12% of revenue" is presented as a factual benchmark without sourcing. |
| Must not give a single-point NPV with no range | yes | No NPV is computed at all; the response explicitly opts for payback/breakeven instead of NPV and shows payback sensitivity (2.2 vs 3.1 years). |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

Quick math, not a full model — here's the shape of it.

**Unit economics per order (€24 basket):**
- Food cost (30%): €7.20
- Platform fee (28%): €6.72
- Contribution before fixed costs: €10.08/order (42%)

**Fixed costs/year (your numbers + my assumptions, flagged):**
- Rent: €90,000 (given)
- Staff (3 heads): ~€100,000 (assumed €33k fully-loaded each — **you need to confirm this**, it's the single biggest swing factor)
- Packaging/utilities/software/insurance: ~€1.50/order + ~€24,000/yr fixed (assumed — **not in your numbers at all**, typical dark-kitchen opex often runs 8-12% of revenue, I've used a lighter estimate)

**Breakeven volume:**
With packaging folded in, contribution per order ≈ €8.58. Fixed costs ≈ €214,000/yr (€586/day).
→ **Breakeven ≈ 68 orders/day.** Your forecast of 120/day gives a ~43% cushion.

**At 120 orders/day:**
- Revenue: ~€1,051,000/yr
- EBITDA: ~€162,000/yr
- Payback on €350k fit-out: **~2.2 years**

**Verdict: lean YES**, on these assumptions — a 2-2.5yr payback with decent cushion over breakeven is a reasonable dark-kitchen bet. Don't bother picking a discount rate for a one-week gate decision; payback and breakeven volume tell you more right now than NPV would, given the bigger uncertainty is in the inputs, not the discounting.

**Before you commit, nail down these three — each one can flip the answer:**
1. **Real staff cost** — if it's €150k instead of €100k, EBITDA drops to ~€112k and payback stretches to ~3.1 years.
2. **Ramp-up** — is 120/day day-one volume or steady-state after 6 months? If it takes 6 months to ramp, add ~€80-100k to the effective payback period.
3. **Other opex** (packaging, delivery packaging waste, platform marketing spend/ad fees beyond the 28% commission, POS/software) — I guessed light; get a real number from someone who's run one.

Want me to turn this into a proper sensitivity table (staff cost × volume × opex) or a one-pager for the Thursday decision? That's a quick follow-up either way.


## Files in work dir after run


