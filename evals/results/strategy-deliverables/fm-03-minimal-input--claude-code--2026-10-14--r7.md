# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling. | yes | No clarifying questions were asked at all; the response proceeds directly with flagged assumptions ('Assumptions flagged' section) rather than stalling. |
| States contribution per order: EUR 10.08 (42% of basket), or a lower flagged figure. | yes | 'Basket €24 − food cost 30% (€7.20) − platform fee 28% (€6.72) = €10.08 contribution per order (42% of basket)' |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range. | NO | Only staff cost gets an explicit 'ASSUMPTION:' tag with a range (€2,200–3,500). Trading days (360) is stated with no ASSUMPTION tag and no range. Discount rate (10–12%) has a reason and sensitivity range but no explicit ASSUMPTION label. Ramp is mentioned only as 'no ramp-up period... a 3-month ramp |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested. | yes | '120 orders/day is your own estimate, unsourced — this is the whole case, treated below,' followed by dedicated analysis of the volume threshold (section 6). |
| Gives break-even orders per day with formula shown, consistent with its stated fixed cost (~60 illustrative). | yes | 'Break-even = fixed costs ÷ contribution per order ÷ 360 trading days ≈ 65–68 orders/day' — consistent with its own stated fixed cost of €231–251k. |
| Gives the answer as a range/scenarios with a clear decision rule, naming the comparison that would settle volume. | yes | 'the deal needs ~92 orders/day to clear a 10% hurdle... Below ~66/day it's cash-negative' plus decision rule: 'go if you have any real evidence (comparable site, soft-launch data, existing delivery run-rate)... run it through one aggregator in an existing kitchen (virtual brand) for a month before b |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag. | yes | 'Does Brightwell already sell to overlapping customers (dine-in or an existing delivery channel)? Cannibalisation would eat straight into the €10.08 contribution.' |
| Leads with a one-screen answer before any full model; adds at most three extra flagged drivers. | yes | 'Here's the back-of-envelope, one screen, no spreadsheet needed' followed directly by contribution, break-even, and decision rule; only one clearly extra driver (other opex ~€40–60k) is added beyond the required missing drivers, and it is flagged as an ASSUMPTION. |
| Does not invent market data on delivery demand, platform commission benchmarks, or competitor dark-kitchen results as facts. | yes | All commission/food-cost figures are taken directly from user inputs (28%, 30%); no external benchmarks or competitor data are asserted as fact. |
| Does not give a single-point NPV with no range. | yes | '5-yr NPV (flat EBITDA, no growth, no ramp) at 10–12% discount: +€370k to +€580k' |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

Here's the back-of-envelope, one screen, no spreadsheet needed.

**1. Contribution per order**
Basket €24 − food cost 30% (€7.20) − platform fee 28% (€6.72) = **€10.08 contribution per order (42% of basket)**, before rent and staff.

**2. Operating break-even volume**
Fixed costs/year = rent €90k + staff (ASSUMPTION: €2,800/month fully-loaded × 3 = €100.8k) + other opex (ASSUMPTION: packaging, utilities, POS/insurance ≈ €40–60k) ≈ **€231–251k/year**.
Break-even = fixed costs ÷ contribution per order ÷ 360 trading days ≈ **65–68 orders/day**.
Your planning case (120/day) is ~80% above break-even — decent cushion, *if* 120 is real.

**3. Base case economics (at 120 orders/day, 360 days)**
- Revenue: 120 × €24 × 360 = **€1.04m/year**
- Contribution: 43,200 orders × €10.08 = **€435k**
- EBITDA after fixed costs: **€185–245k/year** (18–24% margin) — call it **~€215k base**
- Payback on €350k fit-out: **~1.6 years**
- 5-yr NPV (flat EBITDA, no growth, no ramp) at 10–12% discount: **+€370k to +€580k** → robust to the discount-rate choice, this isn't close.

**4. Assumptions flagged**
- 120 orders/day is **your own estimate, unsourced** — this is the whole case, treated below.
- Staff cost €2,800/month/head fully loaded — wide range (€2,200–3,500) plausible, doesn't change the NPV sign.
- 360 trading days, no ramp-up period, no revenue growth — optimistic; a 3-month ramp would delay but not kill payback.
- Discount rate 10–12% assumed (SME discretionary capex) — result barely moves between 8–14%.

**5. What's not in the numbers yet — check these**
- Does Brightwell already sell to overlapping customers (dine-in or an existing delivery channel)? Cannibalisation would eat straight into the €10.08 contribution.
- One-off launch costs (platform onboarding, initial marketing push, smallware/equipment beyond fit-out).
- Any ramp period before hitting 120/day — first 2–3 months are usually 40–60% of steady state.

**6. The number that actually decides this**
Working backwards, the deal needs **~92 orders/day** to clear a 10% hurdle over 5 years (vs. your 120 estimate) — i.e., volume can miss your forecast by ~23% and still pay off. Below ~66/day it's cash-negative at the EBITDA line.

**Decision rule:** go if you have *any* real evidence (comparable site, soft-launch data, existing delivery run-rate) that ≥95–100 orders/day is achievable within the first quarter. If 120/day is a pure guess with no backing, the honest answer isn't yes/no — it's **"get a 4-week soft-launch or comparable-site number before committing €350k fit-out."** Cheapest way to settle it: run it through one aggregator in an existing kitchen (virtual brand) for a month before building anything.

If 120/day is well-grounded (your own data, not a guess): **yes**, the economics clear a hurdle with real margin even after the ramp and cannibalisation risk.

Want the full live-formula model (scenarios, tornado chart, proper ramp curve) — I can build that next if you need something to put in front of the board, but for a yes/no by next week this is the answer.


## Files in work dir after run


