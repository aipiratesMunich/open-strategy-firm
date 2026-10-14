# Eighty-Twenty

## What it is

A prioritisation heuristic: in many business distributions a small share of items (customers, products, causes, leaves of a tree) accounts for a large share of the effect. The "80/20" label is shorthand, not a law; the real split might be 60/10 or 95/40. It answers: "Where should the team spend limited time to move the answer most?" The heuristic tells you to look for concentration. Only the data tells you whether it exists.

## When to use

- Pruning an [Issue Tree](issue-tree.md) or ranking leaves of a [Hypothesis Tree](hypothesis-tree.md).
- Targeting: which customers, products, regions or cost lines deserve detailed analysis.
- Deciding when an analysis is good enough: stop refining once more precision cannot change the decision.
- Focusing a sales or operational pilot on the segment with the most at stake.

## When NOT to use

- **Flat distributions.** If the top 20% of customers hold 25% of revenue, concentration is absent. Treating the top group as special misleads. Use customer segmentation on needs or behaviour instead.
- **Tail risk.** A rare failure mode, a small customer with a liability claim, a compliance gap: low frequency, high consequence. Use a risk register or [Sensitivity Analysis](sensitivity-analysis.md) on the downside.
- **Strategic small items.** A small segment that is growing fast or that a competitor uses as a beachhead. Use three horizons or competitor profiling before cutting it.
- **As evidence in a deliverable.** "80% of value comes from 20% of customers" without the actual curve is a claim with no source. Show the measured split.

## Step by step

1. **Define the item and the effect.** Input: the question. Output: what is counted (customers, SKUs, failure causes) and what effect is measured (revenue, margin, downtime hours), with period and scope.
2. **Get the item-level data.** Output: one row per item with its effect. If item-level data is missing, say so and estimate with a stated method.
3. **Sort descending and compute the cumulative share** of items and of effect.
4. **Read the real split.** Output: the share of items that delivers 50%, 70% and 90% of the effect. Report these numbers, not "80/20".
5. **Decide the cut.** Choose the point where adding items adds little effect relative to effort. State what falls outside and its total effect.
6. **Check the excluded tail** for strategic or risk items before dropping it.
7. **Record the decision** in the workplan or analysis plan: what is in focus, what is parked, why.

## Inputs needed

- Item-level data for the effect that matters to the decision.
- The decision the prioritisation serves.

## Output produced

- A concentration curve or table with the real split.
- A focus list, a parked list, and the size of what was parked.

## Common mistakes

- **Fake precision.** Quoting "80/20" as if it were measured. A partner asks for the curve and the actual numbers.
- **Wrong effect measure.** Ranking customers by revenue when the decision is about margin or service cost. The top revenue customers can be the least profitable.
- **Dropping the tail unseen.** Parked items with a combined 30% of the effect need a reason, not a heuristic.
- **Using it to skip hard analysis.** "We focused on the 20% that matters" when the hard branch was the one that matters.
- **Static view.** Concentration measured on last year while the mix is shifting.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps wants to pilot the service-contract offer with a focused customer list. The 31,200 uncontracted pumps older than eight years sit with 4,000 customers. Sorted by number of such pumps:

- Top 400 customers (10%) hold 14,000 pumps (45%).
- Top 1,000 customers (25%) hold 21,800 pumps (70%).
- Remaining 3,000 customers (75%) hold 9,400 pumps (30%).

The real split is 25/70, not 80/20. The pilot targets the top 1,000 customers. The parked 3,000 are not dropped: they hold 30% of the opportunity and will be served through distributors with a standard contract. Tail check: 12 hospitals in the tail run pumps in critical applications and are added to the pilot because a failure there carries reputational risk.

## Output template

```markdown
# Concentration: <item> by <effect>, <period, scope>

| Share of items | Number of items | Share of effect | Effect |
|---|---|---|---|
| Top <x>% | | 50% | |
| Top <x>% | | 70% | |
| Top <x>% | | 90% | |

**Measured split:** <x>% of items deliver <y>% of <effect>
**Focus:** <items in scope>, <effect covered>
**Parked:** <items>, <effect>, handled by <approach>
**Tail exceptions (strategic or risk):** <items and reason>
**Data gaps:** <missing data and how estimated>
```

## Related

- [Issue Tree](issue-tree.md), [Hypothesis Tree](hypothesis-tree.md), [Workplan](workplan.md), customer segmentation, [Sensitivity Analysis](sensitivity-analysis.md), [Weak Evidence](weak-evidence.md)
