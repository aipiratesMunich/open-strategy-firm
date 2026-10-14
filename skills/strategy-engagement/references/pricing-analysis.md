# Pricing Analysis

## What it is

A structured test of where a price should sit and what a price change does to profit. It combines three views (value to the customer, cost, competitor prices) with the price-volume trade-off. It answers "can we change price by X, and how much volume can we lose before profit falls?"

## When to use

- A list-price change, a new offer or a discount policy is on the table.
- Margin is under pressure and price has not been reviewed for years.
- Prices sit visibly above or below competitors for comparable products.

## When NOT to use

- **Realised price is the problem, not list price.** If discounts, rebates and free extras leak most of the list price, a list increase changes little. Run a price waterfall per customer first and fix discount governance.
- **The product is a commodity priced off an index.** Price is set by the market; work on cost ([Cost Benchmarking](cost-benchmarking.md)) or mix.
- **The client has no idea what the customer gains.** Value-based pricing needs a quantified customer benefit. Without it, start with interviews ([Interview Guide](interview-guide.md)) and [Customer Segmentation](customer-segmentation.md), then come back.
- **Regulated or tendered prices.** Bid strategy and tender rules decide, not willingness to pay.

## Step by step

1. **Fix the scope.** Products, customers, region, and whether the question is list price, realised price or structure (bundles, tiers, service add-ons). Output: scope statement.
2. **Get the price facts.** Ask the user for list prices, realised prices after all discounts, volumes and contribution margin per product line. Output: price and margin table, with assumptions flagged.
3. **Run the three views.**
   - *Cost-plus:* cost per unit plus target margin. A floor, never the answer.
   - *Competitive:* price position against the two or three alternatives the customer actually compares, like for like on spec and service.
   - *Value-based:* the customer's economic gain from the product (avoided downtime, saved labour) compared with the next-best alternative. The gap between that gain and the alternative's price is the room to price in.
   Output: one row per view with the price it implies.
4. **Estimate willingness to pay.** Pick the method the evidence allows:
   - *Interviews* on value and current alternatives (cheap, qualitative, small samples).
   - *Price sensitivity survey (Van Westendorp type):* four questions on too cheap, cheap, expensive, too expensive; the curves give an acceptable range. Stated, not revealed, preference.
   - *Conjoint:* respondents choose between product profiles that vary price and features; the model estimates what each feature is worth. Needs a proper sample and design.
   - *Revealed data:* past price changes, win/loss records, test markets. Best evidence when it exists.
   Output: WTP range with method and sample size.
5. **Compute the price-volume trade-off.** For a price increase p and a contribution margin m (both as a share of the old price), profit is unchanged if volume retention equals m / (m + p). So the break-even volume loss is 1 − m / (m + p). For a price cut, retention needed is m / (m − p). Output: break-even table.
6. **Compare expected volume loss with break-even.** Use win/loss data, competitor gap and interviews to judge the likely loss. Output: verdict with margin of safety.
7. **Check competitor response** ([Competitor Profiling](competitor-profiling.md)). Would they follow, hold or attack?
8. **Recommend** price, timing, which segments are exempt, and how sales will hold the line on discounts.

## Inputs needed

- List and realised prices, volumes, contribution margins per product line (user-supplied).
- Competitor prices for comparable products, with spec differences.
- Customer value evidence: interviews, downtime or labour data.
- Win/loss records and history of past price changes, if available.

## Output produced

- Three-view price table, WTP range with method, break-even volume table, recommendation with risks.

## Common mistakes

- **Cost-plus as the answer.** Cost says what the client needs, not what the customer will pay.
- **Using gross margin instead of contribution margin** in the break-even formula. Fixed costs do not move with volume; using the wrong margin understates the allowed loss.
- **Average price gap.** "6% below competitors" averaged across all products hides lines where the client is already above.
- **Stated WTP taken as fact.** Survey answers overstate what customers pay. Treat them as a range and cross-check with revealed data.
- **Ignoring the price waterfall.** A list increase that sales gives back as discount.
- **No segment cut.** One price move for all customers when the strategic accounts react differently.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps, revenue EUR 180m. List prices are 6% below the two main competitors for comparable pumps (price benchmark). Proposal: raise list prices 4% in 2027. Gross effect at constant volume: 4% × EUR 180m = EUR 7.2m, about EUR 7m.

Contribution margin: the CFO gives an average of 30% (assumption until confirmed per product line). Break-even retention = 0.30 / (0.30 + 0.04) = 88.2%. Alder can lose up to 11.8% of volume before contribution falls below today.

Expected loss: after the increase Alder is still about 2% below competitors (0.94 × 1.04 = 0.978). Win/loss records show price named in a minority of lost deals; interviews name response time first. Expected volume loss is put at 0% to 3%, far below 11.8%. Risk: realised prices on the 20 largest accounts already carry special discounts; the increase applies there only if sales holds it. Recommendation: 4% in 2027, key accounts reviewed one by one, discount approval moved to the sales director.

## Output template

```markdown
# Pricing analysis: <scope>

**Answer:** <price move> is / is not justified. Break-even volume loss <x%>, expected loss <y%>.

## Price facts
| Product line | List price | Realised price | Volume | Contribution margin | Source / ASSUMPTION |
|---|---|---|---|---|---|

## Three views
| View | Implied price or room | Basis |
|---|---|---|
| Cost-plus (floor) | | |
| Competitive | | |
| Value-based | | |

## Willingness to pay
| Method | Sample | Range | Limits |
|---|---|---|---|

## Break-even
| Price change | Contribution margin | Required retention = m / (m + p) | Break-even volume loss | Expected loss | Margin of safety |
|---|---|---|---|---|---|

## Competitor response
- <competitor>: <likely response, evidence>

## Recommendation
- Price, timing, exempt segments, discount control.
```

## Related

- [Pricing](pricing.md), [Customer Segmentation](customer-segmentation.md), [Competitor Profiling](competitor-profiling.md), [Unit Economics](unit-economics.md), [Sensitivity Analysis](sensitivity-analysis.md), [Profit Tree](profit-tree.md), [Weak Evidence](weak-evidence.md)
