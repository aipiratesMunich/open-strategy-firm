# Growth-Share Matrix

## What it is

A portfolio chart that places business units by market growth rate and relative market share (own share divided by the largest rival's). The quadrants suggest a cash role for each unit: fund, harvest, decide, or exit. It was popularised by the Boston Consulting Group in the 1970s. It informs capital allocation across a multi-business portfolio. It cannot tell you whether a unit is profitable, whether its market is attractive, or what strategy a single unit should follow.

## When to use

- A company with several distinct business units competing for the same capital.
- A first view of a portfolio before deeper unit-level work.
- Checking whether cash generation and investment needs across units balance.

## When NOT to use

- **Single-business companies.** One dot on a chart tells nothing. Use [Profit Tree](profit-tree.md) and [Five Forces](five-forces.md).
- **Industries without scale or experience effects.** The matrix uses relative share as a proxy for cost advantage. In fragmented, service or niche businesses, small players can have the best costs. Use [Cost Benchmarking](cost-benchmarking.md).
- **When growth does not mean attractiveness.** Fast-growing markets can have low margins and heavy rivalry. Assess attractiveness with [Five Forces](five-forces.md) and actual returns.
- **For acquisition targets in isolation.** Value and fit matter more than quadrant. Use a [Business Case](business-case.md).
- **When units share costs or customers.** Exiting a "low-share, low-growth" unit can raise costs for the rest. Model the linkages before using quadrant labels.

## Step by step

1. **Define units and their markets.** Input: segment reporting. Output: list of units with a market definition each. Market definition drives share, so write it down.
2. **Calculate relative share.** Input: own revenue and largest competitor's revenue in that market. Output: ratio per unit.
3. **Estimate market growth.** Input: market data for the next three to five years. Output: real growth rate per market with its source.
4. **Plot with bubble size = unit revenue.** Output: the chart.
5. **Test the proxies.** For each unit, check whether share actually brings lower unit cost, and whether growth actually brings margin. Output: a note per unit where the proxy fails.
6. **Add cash and returns.** Input: unit cash flow, capex and return on capital. Output: cash generated or consumed per unit.
7. **Set the cash role.** Output: fund, sustain, harvest, fix or exit per unit, with reasoning that goes beyond the quadrant.

## Inputs needed

- Revenue, margin, capex and cash flow by unit.
- Market definitions, competitor revenues, market growth forecasts.
- Unit cost data for at least the largest competitors where available.

## Output produced

- A bubble chart with clear market definitions.
- A table of cash role per unit, with the proxy tests and actual returns that justify it.

## Common mistakes

- **Labels as strategy.** Calling a unit a "dog" and recommending exit without checking its cash flow or links to other units.
- **Absolute share.** Relative share against the leader is the measure. 20% share is strong if the next player has 5%.
- **Unwritten market definitions.** Narrow the market and every unit becomes a leader.
- **Nominal growth in inflationary periods.** Use real growth or say which.
- **No cash data.** A portfolio chart without cash flows cannot support an allocation decision.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps reports three product lines (revenue EUR 180m in total, each including its spare parts and repairs):

| Unit | Revenue | Market growth (real, p.a.) | Relative share | Quadrant | Proxy test |
|---|---|---|---|---|---|
| Building-services pumps | EUR 70m | 1% | 1.3 | Harvest | Holds: unit cost lowest in the market |
| Process pumps | EUR 85m | 3% | 0.8 | Low share, low growth | Fails: margin above leader thanks to custom engineering |
| Wastewater pumps | EUR 25m | 7% | 0.3 | Low share, high growth | Partly: growth driven by municipal tenders with thin margins |

The quadrant would suggest exiting process pumps. The cost data contradict it: the largest unit earns above-average margin and its customers are the target for service contracts. The team recommends sustaining process pumps, harvesting building-services pumps for cash, and making wastewater a fix-or-exit decision after one tender cycle.

## Output template

```markdown
# Portfolio view: <company>

**Market definitions:** <unit: market, geography>

| Unit | Revenue | Market growth (real, source) | Relative share (vs. <leader>) | Margin | Cash flow | Proxy holds? | Cash role |
|---|---|---|---|---|---|---|---|

**Chart:** x = relative share (log scale), y = market growth, bubble = revenue
**Allocation decision:** <where capital goes and why>
```

## Related

- [Three Horizons](three-horizons.md), [Ansoff Matrix](ansoff-matrix.md), [Five Forces](five-forces.md), [Growth Strategy](growth-strategy.md), [M&A Screening](m-and-a-screening.md), [Cost Benchmarking](cost-benchmarking.md)
