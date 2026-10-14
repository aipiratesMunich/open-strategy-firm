# Business Case

## What it is

A cash-flow comparison of the world with a decision and the world without it, over a defined horizon, valued with NPV, IRR and payback, and tested in base, down and up cases. It answers "is this investment worth its money and risk, and what must be true for it to pay off?"

## When to use

- A board or investment committee must approve capital or a multi-year spend.
- Two or more options compete for the same budget.
- A recommendation has been made and needs its financial proof.

## When NOT to use

- **The drivers are unknown.** A business case on guessed take-up and guessed price is precise-looking fiction. First run market sizing, pricing analysis or a pilot, then build the case.
- **The decision is small and reversible.** A test that costs less than the analysis does not need NPV. Run it and measure.
- **The value is strategic and cannot be priced honestly.** For a defensive move, state the cost and the risk avoided in words; do not invent cash flows to reach a positive NPV.
- **Structural uncertainty dominates.** If the outcome depends on which world materialises, run scenario planning first and build the case per scenario.

## Step by step

1. **Define the decision, the options and the counterfactual.** Include "do nothing" and say what happens to the business without the investment. Output: option list and base line.
2. **Set horizon, discount rate and terminal value rule.** Ask the user for the hurdle rate or cost of capital; if missing, use a stated assumption and show the effect of plus and minus two points. Output: valuation parameters.
3. **Build incremental cash flows.** Only cash that changes because of the decision: investment, added contribution, added fixed cost, acquisition cost, cannibalised margin, working capital, tax if relevant. Exclude sunk costs and allocated overheads that do not change. Build from drivers (unit economics), never from typed totals. Output: annual cash-flow table.
4. **Compute metrics.**
   - *NPV:* sum of cash flows discounted at the hurdle rate. The decision metric.
   - *IRR:* the discount rate at which NPV is zero. Useful for comparison, misleading for flows that change sign more than once or for options of different size.
   - *Payback:* years until cumulative cash turns positive. A liquidity and risk signal, ignores value after payback.
   Output: metric table.
5. **Define base, down and up cases** as coherent sets of assumptions, each tied to evidence (interviews, comparables, pilots). The base case is the likely case, not the hoped-for case; compare it with what similar projects achieved. Output: case table.
6. **Run sensitivities and break-evens** on the three to five most uncertain drivers ([Sensitivity Analysis](sensitivity-analysis.md)). Output: break-even value per driver.
7. **Check against constraints**: capital limits, margin floors, targets. Output: constraint check.
8. **Pass [Model Red Flags](model-red-flags.md) and [Excel Model Standards](excel-model-standards.md)** before the case leaves the team.

## Inputs needed

- Decision, options, counterfactual, horizon.
- Hurdle rate or cost of capital (user-supplied, or flagged assumption).
- Driver values and evidence: volumes, prices, unit costs, take-up, investment, fixed costs.
- Board constraints and targets.

## Output produced

- Incremental cash-flow model with base, down and up cases.
- NPV, IRR, payback per case, break-even values, constraint check.

## Common mistakes

- **Total instead of incremental.** Showing all service revenue, including contracts that exist anyway, inflates the case. Only the change counts.
- **Missing cannibalisation.** Margin lost on existing products belongs in the case.
- **Hockey-stick base case.** A ramp no comparable project achieved. Partners ask for the outside view and the base collapses.
- **Down case at minus 10% on everything.** Not a coherent world. Tie the down case to a specific failure (low take-up, competitor match).
- **IRR as the headline.** High IRR on a small project can destroy less value than a lower IRR on a larger one. Lead with NPV.
- **Terminal value doing the work.** If most of the NPV sits in the terminal value, say so and show the case without it.
- **No break-even.** The board needs to know the take-up or price at which the case turns negative.

## Worked example

*Fictional example. Company, figures and people are invented.*

Decision: Alder Pumps invests EUR 6m in early 2027 in a service-contract offer. Counterfactual: no offer; existing repair business continues. Horizon 2027 to 2033, no terminal value. Discount rate 8% (assumption; the CFO to confirm). Drivers from unit economics: contribution EUR 450 per contract-year before EUR 50 lost repair margin; CAC EUR 300; renewal 90%; platform fixed cost EUR 1.0m per year. Base take-up 40% of 31,200 eligible pumps, reached in 2030 on a ramp of 10%, 25%, 35%, 40%.

| EUR m | 2027 | 2028 | 2029 | 2030 | 2031 to 2033 each |
|---|---|---|---|---|---|
| Contracts in force | 3,120 | 7,800 | 10,920 | 12,480 | 12,480 |
| Revenue | 3.12 | 7.80 | 10.92 | 12.48 | 12.48 |
| Contribution | 1.40 | 3.51 | 4.91 | 5.62 | 5.62 |
| Lost repair margin | −0.16 | −0.39 | −0.55 | −0.62 | −0.62 |
| Platform fixed cost | −1.00 | −1.00 | −1.00 | −1.00 | −1.00 |
| Acquisition cost | −0.94 | −1.50 | −1.17 | −0.80 | −0.37 |
| Net incremental cash flow | −0.69 | 0.62 | 2.20 | 3.20 | 3.62 |

Rows may not add up because of rounding. With the EUR 6m at the start: base NPV EUR 4.8m, IRR about 21%, payback in 2031. Down case (take-up 25%, same ramp shape): NPV −EUR 1.2m. Up case (50%): NPV EUR 8.9m. Break-even take-up: about 28%.

Constraint check: EUR 6m is within the EUR 20m capital limit. Service adds EUR 12.5m revenue by 2030 and the 4% price increase about EUR 7m, taking revenue to about EUR 200m, the board target, with almost no cushion. The case recommends approval, states the thin margin openly, and makes take-up in the first 18 months the go/no-go checkpoint.

## Output template

```markdown
# Business case: <decision>

**Answer:** NPV <value> at <rate>, IRR <x%>, payback <year>. Turns negative below <driver = break-even>.

## Setup
- Options: <...>
- Counterfactual: <...>
- Horizon: <years>; discount rate: <x%> (<source or ASSUMPTION>); terminal value: <rule>

## Incremental cash flows (base)
| <unit> | Year 0 | Year 1 | Year 2 | ... |
|---|---|---|---|---|
| Investment | | | | |
| Added contribution | | | | |
| Cannibalised margin | | | | |
| Added fixed cost | | | | |
| Acquisition cost | | | | |
| Working capital | | | | |
| Net incremental cash flow | | | | |

## Cases
| Case | Defining assumptions | Evidence | NPV | IRR | Payback |
|---|---|---|---|---|---|
| Down | | | | | |
| Base | | | | | |
| Up | | | | | |

## Break-even
| Driver | Base | Break-even value | Headroom |
|---|---|---|---|

## Constraint check
| Constraint | Limit | Case value | Met? |
|---|---|---|---|
```

## Related

- unit economics, [Sensitivity Analysis](sensitivity-analysis.md), scenario planning, [Model Red Flags](model-red-flags.md), [Excel Model Standards](excel-model-standards.md), market sizing, [Partner Review Checklist](partner-review-checklist.md)
