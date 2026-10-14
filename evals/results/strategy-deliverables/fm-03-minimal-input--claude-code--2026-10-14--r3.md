# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (1/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | Response asks no blocking questions; it proceeds directly with a full model using stated assumptions (e.g., 'assumed €3k/mo loaded each') and only invites a follow-up refinement at the end. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs, or a lower figure consistent with any extra variable cost it adds and flagged as assumption | NO | The response never states a per-order contribution figure or percentage anywhere; it only presents annual revenue/cost totals and EBITDA, never isolating 'contribution per order' (€10.08 or any flagged-lower variant). |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost is marked 'assumed €3k/mo loaded each' with no reason/range; trading days (360) is stated with no assumption label at all; discount rate '10%' is given a one-line reason but no range; ramp and horizon are not labeled as assumptions with reason+range at all. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | NO | Volume is ranked '#1' and tested at 80/day ('At 80/day instead of 120, payback stretches to ~9.5 years'), but the 120/day figure is never explicitly flagged as an unsourced/user guess. |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost (about 60 with the illustrative figures above) | NO | 'Break-even volume: ~67 orders/day.' is stated with no formula shown anywhere in the response. |
| Gives the answer as a range or scenarios with a clear decision rule, and names the comparison that would settle volume | NO | Only a single alternate scenario (80/day) is tested and no named comparison (e.g. existing store delivery data, a platform pilot) is mentioned; the ask is only for 'a rough ramp curve' from the user, not an external benchmark to settle volume. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | NO | No mention of cannibalisation of existing store delivery/orders anywhere in the response. |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three drivers beyond those given and named missing ones, each flagged | NO | The response leads with one line ('Conditional yes...') then immediately presents the full EBITDA table/model before any concise contribution-per-order/break-even summary. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | NO | 'Platform commission — these go up over time... worth knowing your contract has no escalation clause' presents a market trend about commissions as fact without sourcing. |
| Must not give a single-point NPV with no range | NO | 'NPV over 5 yrs @ 10% discount rate ... +€236k — comfortably positive' is a single-point NPV with no stated range. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

**Conditional yes — but don't sign anything until you pin down 3 numbers.**

**Base case (360 operating days/year, EUR):**

| | |
|---|---|
| Revenue (120 ord/day × €24) | €1,036,800 |
| − Food cost (30%) | €311,040 |
| − Platform fee (28%) | €290,304 |
| − Rent | €90,000 |
| − Staff (3 FTE, **assumed** €3k/mo loaded each) | €108,000 |
| − Other opex (packaging/utilities/POS — **assumed** 8% of rev) | €82,944 |
| **EBITDA** | **€154,500** (15% margin) |

- **Payback on €350k fit-out:** ~2.3 years
- **NPV over 5 yrs @ 10% discount rate** (reasonable hurdle for this risk level, no rate given): **+€236k** — comfortably positive
- **Break-even volume:** ~67 orders/day. Your 120/day plan is 1.8x that, so there's real cushion.

**What moves the answer (ranked):**
1. **Order volume** — biggest lever. At 80/day instead of 120, payback stretches to ~9.5 years. If 120/day is a steady-state target rather than a day-1 number, you need a ramp assumption — that's the single most important missing input.
2. **Other opex (my 8% is a guess, not a number you gave me)** — if it's really 15%, payback moves to ~4.3 years. Still works, but tighter.
3. **Platform commission** — these go up over time. At 32% instead of 28%, payback is ~3.1 years. Fine, but worth knowing your contract has no escalation clause.
4. **Staff cost** — I assumed €108k/year total; get the real number, it's a pure fixed-cost assumption.

**Bottom line:** the math clears a 10% hurdle rate with margin to spare even under a moderately bad case (worse opex, higher commission, or slower staff ramp). It only breaks if volume is well below 120/day for an extended period — that's the one assumption worth stress-testing before you commit €350k. If you can get even a rough ramp curve (e.g., "60/day month 1, 120/day by month 4") I can redo this in 5 minutes with that built in instead of flat volume.


## Files in work dir after run


