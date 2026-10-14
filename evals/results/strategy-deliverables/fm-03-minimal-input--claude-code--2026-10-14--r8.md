# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (1/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling. | yes | The response asks no clarifying questions and proceeds directly with assumptions (e.g. 'Assume a realistic €30k/head'), so it does not stall. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs, or a lower figure consistent with any extra variable cost it adds and flagged as assumption. | NO | The response only gives annualized figures (revenue €1,051,200, contribution €441,504) and never states a per-order contribution figure or the 42% margin explicitly. |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range. | NO | Uses '365 operating days' with no flag at all, says 'Assume a realistic €30k/head' with no range, and '10% is a fine default' — none use an ASSUMPTION label with reason and range. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested. | NO | 120 orders/day is used as a fixed hard input throughout ('Revenue: 120 orders × €24 × 365') with no flag that it is unsourced, and it is never sensitivity-tested. |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost (about 60 with the illustrative figures above). | NO | Only a break-even euro cost is given ('Break-even staff+rent cost ... is €351,504/year'); no break-even orders-per-day figure or formula is shown. |
| Gives the answer as a range or scenarios with a clear decision rule, and names the comparison that would settle volume. | NO | The answer is a single verdict 'Yes — open it.' with no scenario table (e.g. 60/90/120 orders) and no named data source (like existing delivery orders) to validate the 120/day figure. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag. | NO | Cannibalisation of existing store delivery is never mentioned anywhere in the response. |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three extra flagged drivers. | NO | Leads with 'Yes — open it' plus a margin table, but omits contribution per order, operating break-even, and any explicit decision rule in the lead. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts. | NO | 'many platforms also charge payment processing (~2-3%) and sometimes a fixed fee per order' is an unsourced platform-commission claim presented as fact. |
| Must not give a single-point NPV with no range. | NO | 'NPV over 5 years at 10% discount rate ≈ +€640k. Even stress-testing at 20% discount, it's still strongly positive' gives one point estimate and only a vague qualitative note, not a quantified range. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

**Yes — open it.** The margin per order is wide enough that this clears the bar even under conservative assumptions, and discount rate barely moves the answer.

**Quick math** (annualized, 365 operating days):

| | |
|---|---|
| Revenue: 120 orders × €24 × 365 | €1,051,200 |
| – Food cost (30%) | –€315,360 |
| – Platform fee (28%) | –€294,336 |
| **= Contribution before rent/staff** | **€441,504** |
| – Rent | –€90,000 |
| – Staff (3 people) | — *you didn't give me this, see below* |

**The missing number that actually matters:** you gave me rent and fit-out but not staff cost. Good news — it doesn't matter much. Break-even staff+rent cost (where annual cash flow hits zero) is **€351,504/year**. That's ~€117k per head for 3 staff, which is absurdly high for a dark-kitchen crew. So unless you're planning to pay way above market, staff cost is not the swing factor here.

Assume a realistic €30k/head (€90k total staff):
- **Annual EBITDA ≈ €261,500**
- **Payback on the €350k fit-out ≈ 1.3 years**
- NPV over 5 years at 10% discount rate ≈ **+€640k**. Even stress-testing at 20% discount, it's still strongly positive. **Discount rate choice doesn't change the decision** — don't lose time picking one, 10% is a fine default for a cash-generative, low-residual-value asset like a kitchen fit-out.

**What actually could kill this** — not covered in your numbers, and the real risk:
1. **Volume ramp-up**: is 120 orders/day day-one steady-state, or the target after ramping? If it takes 6-9 months to get there, payback stretches but still stays under 2 years — model holds.
2. **Order economics on top of the 28%**: many platforms also charge payment processing (~2-3%) and sometimes a fixed fee per order — check your contract, as that eats into the 28% figure.
3. Food cost could drift above 30% early on (waste during ramp-up) — worth a margin buffer for month 1-3.

**Bottom line for the yes/no:** the deal is profitable even in a pessimistic case; the volume ramp-up timeline is the only thing worth double-checking before you commit, not the discount rate or staff cost.


## Files in work dir after run


