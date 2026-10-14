# Pricing

## Typical questions

Pricing questions arrive as "what price?" and hide three different decisions: price level, price structure (what is charged for), and price execution (discounts, terms, who can deviate).

- "Can we raise prices?" → "By how much can we raise list prices in <year> without losing more than <x>% volume, and what is the EBIT effect?"
- "How should we price the new offer?" → "What price and structure capture a fair share of the value the offer creates for <segment>, against the customer's next-best alternative?"
- "Our margins erode, sales gives too many discounts." → "How much of list price is lost between list and pocket price, where, and which rules close the leak?"
- "A competitor cut prices. Do we follow?" → "What do we lose by holding price, by segment, against what we lose by matching?"

A pricing question is sharp when it names the products and segments, the decision (level, structure or execution) and the volume risk the client accepts.

## Issue tree skeleton

A MECE starting tree. Adapt, never use unchanged.

- **Where does our price sit against value?**
  - Value to the customer: what the offer saves or earns them, against the next-best alternative. *H: downtime savings exceed the price of a service contract several times over.*
  - Price position against competitors for comparable offers. *H: list prices are below the two main competitors without a quality or service reason.*
  - Willingness to pay by segment
- **How will customers and competitors react?**
  - Volume reaction by segment (switching costs, contract cycles, share of customer budget)
  - Competitor reaction: likely to follow, hold or undercut?
- **Are we capturing the price we set?** (execution)
  - List to pocket price: discounts, rebates, free services, payment terms
  - Who decides deviations, and is it controlled?
- **Is the structure right?**
  - What is charged for (product, service, usage, outcome), bundles, tiers
- **What is the profit effect and the plan?**
  - EBIT effect under volume scenarios, sequencing by segment, sales readiness

## Key analyses

- **Price benchmark.** Like-for-like comparison against competitors, adjusted for specification, service and terms ([Competitor Profiling](competitor-profiling.md)).
- **Value-to-customer analysis.** Quantify the customer's economics: cost avoided, revenue gained, against the next-best alternative ([Jobs to Be Done](jobs-to-be-done.md), [Pricing Analysis](pricing-analysis.md)).
- **Willingness to pay.** Interviews and structured price research. Weight past purchase behaviour above stated intent ([Interview Guide](interview-guide.md), [Weak Evidence](weak-evidence.md)).
- **Price waterfall.** List to pocket price per customer and deal, to find leakage ([Pricing Analysis](pricing-analysis.md)).
- **Break-even volume.** How much volume can be lost before a price increase reduces profit; depends on contribution margin ([Unit Economics](unit-economics.md)).
- **Segmentation.** [Customer Segmentation](customer-segmentation.md) by value received and price sensitivity, so increases are not applied uniformly.
- **Scenarios.** [Scenario Planning](scenario-planning.md) for competitor reaction; [Sensitivity Analysis](sensitivity-analysis.md) on volume loss.

## Traps

- **Cost-plus by habit.** Setting price from cost ignores what the offer is worth to the customer. Cost sets the floor, value sets the ceiling.
- **Trusting stated willingness to pay.** Customers in interviews name lower prices than they later accept, and sometimes higher. Anchor on what they pay today for alternatives.
- **Uniform increases.** The same percentage on every product and customer ignores differences in value and sensitivity.
- **List price only.** Raising list price while discounts grow leaves pocket price unchanged. Fix execution with the level.
- **Ignoring break-even volume.** Teams fear volume loss without knowing how much loss the increase can absorb.
- **Forgetting the sales force.** A price change that sales does not believe in will be discounted away. Plan arguments, incentives and approval rules.
- **Competition law blind spots.** Pricing work must never involve sharing or coordinating prices with competitors. Use public and customer data.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps (revenue EUR 180m) has list prices 6% below its two main competitors for comparable pumps. Interviews show customers choose on reliability and service response, not on small price gaps. Sharpened question: "Can Alder raise list prices 4% in 2027 without losing more than 2% volume, and what does it add to EBIT?"

Effect: 4% on EUR 180m is about EUR 7m if volume holds, almost all of it EBIT. Assumed contribution margin: 30% (to be confirmed with finance). Break-even volume loss for a 4% increase at 30% contribution margin is 0.04 / (0.30 + 0.04), about 12%. At 2% volume loss, EBIT still rises by about EUR 6.0m (about EUR 7.1m price gain on the retained volume, less about EUR 1.1m contribution lost on the volume that leaves). Recommendation: raise list prices 4% in 2027, cap discretionary discounts at the same time so the increase reaches pocket price, and price the new service contract separately at about EUR 1,000 per pump per year based on customers' downtime costs.

## Output template

```markdown
# Pricing: <client>, <decision question in one line>

**Answer:** <change price level / structure / execution> by <x> for <segments> from <date>; EBIT effect <range>.

## Price position
| Offer | Our price | Competitor A | Competitor B | Value difference | Gap explained? |
|---|---|---|---|---|---|

## Value to customer
| Segment | Next-best alternative | Customer value of our offer | Current price | Share of value captured |
|---|---|---|---|---|

## Price waterfall (average, <segment>)
| Step | Per unit | % of list |
|---|---|---|
| List price | | 100% |
| Discounts / rebates / terms | | |
| Pocket price | | |

## Profit effect
| Volume reaction | Revenue effect | EBIT effect |
|---|---|---|
| 0% | | |
| -<x>% | | |
| Break-even volume loss | <x>% | 0 |

## Implementation
| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|

## What would change the answer
1. If <competitor reaction / volume loss above x>, then <consequence>.
```

## Playbook

How to run this case step by step. Steps 1 to 4 are specific to this case type; the shared engagement procedure covers the rest.

### Step 1: Sharpen the question

"What price?" hides three decisions. Find out which one is on the table. Ask, in small groups:
- Is this about the price level, what you charge for (structure), or what actually reaches you after discounts (execution)?
- Which products and customer segments are in scope? Which are exempt and why?
- What contribution margin do these products earn (not gross margin)?
- How much volume loss would you accept, and over what period?
- When did prices last change, by how much, and what happened to volume?
- Who can grant discounts today, up to what level, and how are sales paid?
- For a competitor price cut: what exactly changed, for which segment, since when?

Write the decision question in this form: "By how much can we change <price level / structure / execution> for <segments> in <year> without losing more than <x>% volume, and what is the EBIT effect?" It is sharp when it names products, segments, the decision type and the accepted volume risk.

### Step 2: Instantiate the issue tree

Adapt the skeleton in the case note; set each threshold with the client.

| Branch | Hypothesis (example form) | Kill criterion |
|---|---|---|
| Value | Customer value against the next-best alternative exceeds price by a wide margin | Value gap small or unquantifiable after interviews |
| Position | List prices sit below comparable competitors without a spec or service reason | Like-for-like gap gone after adjusting for spec, service and terms |
| Willingness to pay | Segments differ in value received and price sensitivity | Revealed behaviour shows the same response everywhere |
| Volume reaction | Expected volume loss stays well below break-even loss | Expected loss near or above break-even, or contract cycles force mass renegotiation |
| Competitor reaction | Main competitors follow or hold | A competitor with spare capacity is likely to undercut in the core segment |
| Execution | A material share of list price leaks between list and pocket price | Leakage small and controlled: a list change will reach pocket price |
| Structure | Charging for <service / usage / outcome> captures more value than today's model | Customers cannot see or measure the unit; structure change adds friction only |

### Step 3: Run the deciding analyses, in order

Each analysis ends by marking its hypothesis confirmed, killed or reshaped. If your agent can run sub-tasks in parallel, run 3a to 3c in parallel; otherwise in order.

a. **Price waterfall.** List to pocket price per customer and deal ([Pricing Analysis](pricing-analysis.md)). Run it first: if leakage is large, a list change achieves little.
b. **Price benchmark.** Like-for-like comparison, adjusted for spec, service and terms ([Competitor Profiling](competitor-profiling.md)), per product line, never only as an average.
c. **Value to customer.** Customer economics against the next-best alternative ([Jobs to Be Done](jobs-to-be-done.md), [Pricing Analysis](pricing-analysis.md)).
d. **Willingness to pay.** Revealed data first (past price changes, win/loss, current spend on alternatives), then interviews ([Interview Guide](interview-guide.md)), then stated price research as a range.
e. **Break-even volume.** With price change p and contribution margin m: break-even loss for an increase is 1 - m / (m + p) ([Unit Economics](unit-economics.md)). Compare with the expected loss. For a price cut p with contribution margin m, the volume gain needed to break even is p / (m - p); show the formula and compare it with the volume the cut can realistically win back. For subscriptions, use the same formula, then translate it: the steady-state customer base scales with 1/churn, so break-even churn = current churn / (1 - break-even loss). Keep variable cost per customer fixed in euros; never apply the margin percentage to the new price.
f. **Segmentation.** [Customer Segmentation](customer-segmentation.md) by value received and sensitivity, so changes are not uniform.
g. **Reaction and stress test.** [Scenario Planning](scenario-planning.md) with three competitor reactions (follow, hold, undercut), each with its EBIT effect and the signal that would show it is happening; [Sensitivity Analysis](sensitivity-analysis.md) on volume loss and margin.

### Step 4: Run the trap checks

Answer each with yes or no and fix every no before writing:
- [ ] Cost sets the floor only; the recommended price is anchored on customer value and alternatives.
- [ ] Stated willingness to pay is treated as a range and cross-checked with revealed behaviour ([Weak Evidence](weak-evidence.md)).
- [ ] The change differs by segment where value and sensitivity differ.
- [ ] Execution is fixed with the level: discount caps or approval rules ensure the change reaches pocket price.
- [ ] Break-even volume loss is computed with contribution margin, and the expected loss is compared with it.
- [ ] Sales has arguments, incentives and approval rules for the change.
- [ ] No step involves sharing or coordinating prices with competitors; only public and customer data are used.

### Step 5: Answer page

Use the output template in [Pricing](pricing.md) for the body, wrapped in the shared format below. State which decision (level, structure, execution), for which segments, from when, and the EBIT effect as a range across volume reactions.

### Case rules

- Show the arithmetic of the break-even and the EBIT effect so finance can check it in one minute.

### Answer page format

```markdown
# Pricing: <client>, <decision question in one line>

**Answer:** <change price level / structure / execution> by <x> for <segments> from <date>; EBIT effect <range>.
**Confidence:** high / medium / low, because <one reason>

<body sections from the case note output template>

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
```

### Limits

Competition law questions (resale price rules, price signalling, dominant positions) go to legal counsel. Conjoint or large-sample price research needs a proper study; this skill can design the questions, not replace the data.

## Related

- [Profitability Turnaround](profitability-turnaround.md), [Growth Strategy](growth-strategy.md), [Pricing Analysis](pricing-analysis.md), [Unit Economics](unit-economics.md), [Customer Segmentation](customer-segmentation.md), [Jobs to Be Done](jobs-to-be-done.md), [Weak Evidence](weak-evidence.md)
