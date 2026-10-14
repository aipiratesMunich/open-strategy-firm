# Profit Tree

## What it is

A logic tree that breaks profit into revenue minus cost, revenue into volume times price, and cost into fixed and variable parts, then further down to drivers that can be measured and influenced. Because every branch adds up arithmetically, it shows where a profit change came from and how large each lever is. It informs which levers to pursue in a profitability or pricing case and is the skeleton of the numbers model. It cannot tell you why a driver moved or whether a lever is achievable in the market.

## When to use

- Profit has fallen or stagnated and nobody agrees why.
- Sizing and comparing levers: price, volume, mix, variable cost, fixed cost.
- Structuring the financial model so each driver has one input cell.
- Explaining a margin bridge from one year to the next.

## When NOT to use

- **The question is strategic direction.** Where to compete is a five forces or ansoff matrix question; the tree only shows today's economics.
- **Driver data does not exist at the needed level.** A tree with estimated leaves looks precise and is not. Collect data first or stop at the level the data supports.
- **Value is in the balance sheet.** Capital-heavy businesses need a return-on-capital tree that includes assets.
- **Early-stage businesses without stable revenue.** Use [Unit Economics](unit-economics.md) per customer.

## Step by step

1. **Set the top.** Input: P&L. Output: profit (EBIT or contribution, stated) for the latest year and a comparison year.
2. **Split revenue into volume × price.** Output: units (or customers, contracts, hours) and average price per segment, so that their products sum to revenue. Separate mix if segments differ in price.
3. **Split cost into variable and fixed.** Output: variable cost per unit by main cost type; fixed cost by block. Variable plus fixed must equal total cost.
4. **Go down until each leaf is a driver someone controls.** Output: leaves such as list price, discount, units per customer, material cost per unit, headcount × cost per head.
5. **Build the bridge.** Input: both years. Output: profit change split by leaf: price, volume, mix, variable cost per unit, fixed cost. Sum must equal the total change.
6. **Size levers.** Output: profit impact of a realistic change per leaf, with the assumption and its source.
7. **Hand over to analysis.** Output: the two or three largest levers, each with the analysis that tests whether it is achievable ([Pricing Analysis](pricing-analysis.md), [Cost Benchmarking](cost-benchmarking.md)).

## Inputs needed

- P&L for at least two years, ideally three.
- Volumes and prices by segment; discount data.
- Cost split by type, with a judgement on which costs vary with volume.

## Output produced

- A profit tree where every node reconciles to the P&L.
- A profit bridge between two years.
- A sized lever list that feeds the model ([Excel Model Standards](excel-model-standards.md)) and the [Business Case](business-case.md).

## Common mistakes

- **Tree that does not add up.** If leaves do not multiply and sum to reported profit, the tree is a list of topics.
- **Revenue split by product only.** Without volume and price the main question, which one moved, stays open.
- **Fixed and variable mixed.** Labour treated as variable when headcount does not change with volume overstates savings from volume loss.
- **Stopping at accounting lines.** "Personnel cost" is not a lever. "Field engineers × cost per engineer" is.
- **Levers added naively.** A price increase lowers volume. Model the interaction instead of adding the two effects.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps: revenue EUR 180m, EBIT EUR 17.1m (9.5%), flat for three years.

- Revenue EUR 180m = new pumps 9,000 units × EUR 15,000 (EUR 135m) + spare parts and repairs EUR 45m. Three years ago: 9,600 units × about EUR 14,100. Flat revenue hides volume down about 6% and price up about 6%.
- Cost EUR 162.9m = variable EUR 126m (70% of revenue) + fixed EUR 36.9m.

Levers:
1. Price: list prices sit 6% below the two main rivals. A 4% increase across revenue is worth about EUR 7.2m revenue and, with variable cost unchanged, about EUR 7m EBIT if volume holds. Volume loss of 2% would cost about EUR 1.1m contribution (2% × EUR 54m contribution).
2. Service contracts: about EUR 12.5m revenue at 40% take-up (31,200 eligible pumps × 40% × EUR 1,000). Contribution depends on engineer cost per contract, to be modelled.
3. Fixed cost: in line with benchmark; not a priority.

The tree turns "growth is flat" into two testable questions: will price stick, and what does a service contract cost to deliver.

## Output template

```markdown
# Profit tree: <company>, <year> vs. <comparison year>

| Node | <comparison year> | <year> | Change | Reconciles to P&L? |
|---|---|---|---|---|
| Profit (<EBIT / contribution>) | | | | |
| Revenue = Σ volume × price | | | | |
| - <segment>: volume | | | | |
| - <segment>: average price | | | | |
| Variable cost = Σ volume × cost per unit | | | | |
| Fixed cost | | | | |

**Profit bridge:** price <x>, volume <y>, mix <z>, variable cost <a>, fixed cost <b> = total change <sum>

| Lever (leaf) | Realistic change | Profit impact | Assumption and source | Analysis to test it |
|---|---|---|---|---|
```

## Related

- profitability turnaround, pricing, issue tree, [MECE](mece.md), [Unit Economics](unit-economics.md), [Pricing Analysis](pricing-analysis.md), [Cost Benchmarking](cost-benchmarking.md), [Value Chain](value-chain.md)
