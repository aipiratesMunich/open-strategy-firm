# Unit Economics

## What it is

The profit of one unit of business: one product sold, one contract-year, one customer. It strips out fixed costs to show whether each additional unit makes money, how much it costs to win one (CAC), how long it takes to earn that back (payback), and what a customer is worth over its life (LTV). It answers "does this business make money per unit, and does growth help or hurt?"

## When to use

- A new offer or channel must prove that each sale adds profit before scaling.
- Growth is rising but profit is not, and the cause is unclear.
- A business case needs per-unit drivers instead of top-line targets.

## When NOT to use

- **Most cost is fixed and shared.** In a plant running at capacity, per-unit views hide the step costs that decide the case. Model capacity and fixed cost directly in the [Business Case](business-case.md).
- **There is no repeat relationship.** LTV makes no sense for one-off project sales. Use contribution per deal and win rate.
- **Retention data does not exist.** For a new offer, LTV built on an assumed churn rate is fiction. Lead with contribution per unit and CAC payback, and show LTV only as a scenario.
- **The question is total profit pool or market.** Use [Market Sizing](market-sizing.md) or the [Profit Tree](profit-tree.md).

## Step by step

1. **Define the unit.** One that matches how revenue is earned: per contract-year, per order, per active customer per month. Output: unit definition.
2. **Build contribution per unit.** Price realised after discounts, minus all costs that vary with the unit: materials, direct labour, travel, payment fees, and margin lost elsewhere (cannibalisation). Exclude allocated overheads. Ask the user for each line; flag assumptions. Output: contribution per unit.
3. **Compute CAC.** All sales and marketing cost to win new units in a period, divided by new units won in that period. Include sales time, commissions, trials, onboarding. Output: CAC.
4. **Compute CAC payback.** CAC / contribution per period. Short paybacks fund growth from cash; long ones need capital. Output: payback in months.
5. **Compute LTV, only if retention is known.** With contribution per period m, retention r per period and discount rate d: LTV = m × sum over t of (r / (1 + d))^t. Cap the number of periods at the realistic customer or asset life. Output: LTV and LTV / CAC, with the source of r.
6. **Check fixed-cost coverage.** Fixed cost of the business divided by contribution per unit gives the number of units needed to break even. Output: break-even units.
7. **Run sensitivities** on price, variable cost, CAC and retention ([Sensitivity Analysis](sensitivity-analysis.md)).

## Inputs needed

- Price list and realised prices, variable cost lines per unit (user-supplied).
- Sales and marketing spend and number of new units per period.
- Retention history by cohort, if any. If none, state it.
- Fixed costs of the business line.

## Output produced

- Unit P&L, CAC, payback, LTV (or the reason it is withheld), break-even units, sensitivities.

## Common mistakes

- **LTV without retention data.** An assumed churn rate drives most of the LTV number. When the offer is new, LTV is fiction and payback is the honest metric.
- **Revenue LTV.** LTV on revenue instead of contribution overstates value by the cost ratio.
- **No life cap.** Infinite-horizon LTV for customers whose equipment will be replaced in five years.
- **Blended CAC.** Mixing organic and paid customers hides that paid acquisition is unprofitable.
- **Allocated overhead in unit cost.** Makes good units look bad and leads to cutting volume that covered fixed cost.
- **Ignoring cannibalisation.** Margin lost on existing business belongs in the unit cost.

## Worked example

*Fictional example. Company, figures and people are invented.*

Unit: one Alder Pumps service contract-year.

| Line | EUR |
|---|---|
| Price | 1,000 |
| Direct delivery cost (technician time, travel, parts in scope) | −550 |
| Lost time-and-material repair margin on contracted pumps | −50 |
| Contribution per contract-year | 400 |

CAC: field technicians sell on service visits plus a commission; total EUR 300 per new contract (assumption from a pilot region, 40 contracts). Payback: 300 / 400 = 0.75 years, about 9 months.

Fixed cost of the service platform (dispatch, monitoring, contract admin): EUR 1.0m per year. Break-even: 1.0m / 400 = 2,500 contracts.

LTV: there is no renewal history. With an assumed 90% renewal and 8% discount rate, the uncapped LTV is 400 × 1.08 / (1.08 − 0.90) = EUR 2,400. Pumps older than eight years will be replaced within a few years, so the team caps life at five years: LTV = EUR 1,435, LTV / CAC about 4.8. The board pack shows payback and break-even contracts as the main metrics, and LTV as an unverified scenario until two renewal cycles are observed.

## Output template

```markdown
# Unit economics: <unit definition>

**Answer:** Contribution <value> per unit, CAC payback <months>, break-even <units>.

## Unit P&L
| Line | Value | Source / ASSUMPTION |
|---|---|---|
| Realised price | | |
| Variable cost: <item> | | |
| Cannibalised margin | | |
| Contribution per unit | | |

## Acquisition
| Metric | Value | Basis |
|---|---|---|
| CAC | | <spend / new units, period> |
| Payback (months) | | |

## Lifetime value
| Retention r | Discount d | Life cap | LTV | LTV / CAC | Retention evidence |
|---|---|---|---|---|---|

**LTV status:** measured / scenario only (<reason>)

## Fixed-cost coverage
| Fixed cost | Contribution per unit | Break-even units |
|---|---|---|

## Sensitivity
| Driver | Low | Base | High | Effect on payback |
|---|---|---|---|---|
```

## Related

- [Business Case](business-case.md), [Pricing Analysis](pricing-analysis.md), [Cost Benchmarking](cost-benchmarking.md), [Profit Tree](profit-tree.md), [Sensitivity Analysis](sensitivity-analysis.md), [Model Red Flags](model-red-flags.md)
