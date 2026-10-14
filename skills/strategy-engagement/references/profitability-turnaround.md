# Profitability Turnaround

## Typical questions

Clients describe a symptom and often a pre-selected cure ("we need to cut costs"). Sharpen the question to a target, a time frame and the root cause.

- "Our margins are collapsing." → "What explains the fall from <x>% to <y>% EBIT margin since <year>, and which actions restore at least <z>% by <year>?"
- "We need a cost-cutting programme." → "Is the profit gap caused by costs at all? If so, which costs, compared with what benchmark?"
- "Business unit <B> loses money. Fix or sell?" → "Can <B> reach <threshold> margin within <time> at acceptable cost, and is it worth more fixed, sold or closed?"
- "Cash is running out." → A liquidity question first. Secure 13-week cash before working on structural profit.

A turnaround question is sharp when it states the profit target, the date, and whether liquidity is at risk.

## Issue tree skeleton

A MECE starting tree. Adapt, never use unchanged. Decompose profit before forming opinions.

- **Where did the profit go?** (bridge from the last good year to today)
  - Revenue side
    - Volume: market, share, mix of customers and products
    - Price: list price, discounts, contract terms, cost pass-through. *H: input-cost increases were not passed through in contracts without indexation.*
  - Cost side
    - Variable costs per unit: materials, labour, energy, logistics. *H: labour cost per unit rose faster than prices.*
    - Fixed costs: overhead, sites, IT
  - Portfolio: which customers, products, contracts or sites lose money? *H: a small number of contracts cause most of the decline.*
- **Is the cause internal or market-wide?**
  - Compare with competitors and the industry: are peers suffering the same?
- **Which actions close the gap?**
  - Price and commercial terms
  - Portfolio pruning: exit or reprice loss-making parts
  - Cost: variable cost per unit, then fixed cost
  - Capital and cash: working capital, capex discipline
- **Can the organisation deliver it, and how fast?**
  - Timing, one-off costs, risks, owners

Use the [Profit Tree](profit-tree.md) for the first branch. Split every number into price times volume and cost per unit times volume before comparing years.

## Key analyses

- **Profit bridge.** Year-by-year walk from the last good year to today, by driver ([Profit Tree](profit-tree.md)). The single most important page of a turnaround.
- **Profitability by customer, product, contract, site.** Find the loss makers; profit is rarely lost evenly ([Eighty-Twenty](eighty-twenty.md), [Customer Segmentation](customer-segmentation.md)).
- **Price realisation.** List price to pocket price, discount leakage, indexation clauses ([Pricing Analysis](pricing-analysis.md)).
- **Cost benchmarks.** [Cost Benchmarking](cost-benchmarking.md) against peers and internal best sites, per unit of output.
- **Unit economics.** [Unit Economics](unit-economics.md) for the core offer or contract type, to see whether the model works at all.
- **Action plan value.** [Business Case](business-case.md) per action with timing, one-off cost and confidence; [Sensitivity Analysis](sensitivity-analysis.md) on the largest actions.

## Traps

- **Cutting before diagnosing.** Across-the-board cost targets hit healthy and sick parts alike and miss price or portfolio causes.
- **Averages hide the problem.** An average margin of 1% can be a healthy core plus a few deeply loss-making contracts.
- **Benchmarking without normalising.** Comparing cost ratios across companies with different mix, scale or outsourcing produces false gaps.
- **Counting the same euro twice.** Price and volume actions on the same customers, or headcount savings also booked in a process programme. Reconcile all actions in one bridge.
- **Ignoring one-off costs and timing.** Severance, exit fees and contract notice periods move the profit effect by a year or more.
- **Confusing liquidity with profitability.** A company can be profitable and run out of cash. Check cash first if there is any doubt.
- **Cutting capability needed for recovery.** Sales coverage, service quality or maintenance cuts that drive away the revenue the plan depends on.

## Worked example

*Fictional example. Company, figures and people are invented.*

Kestrel Logistics, a contract logistics firm, saw EBIT fall from EUR 13.8m (6% of EUR 230m revenue) in 2022 to EUR 2.4m (1% of EUR 240m) in 2025. Management asked for a cost-cutting programme. Sharpened question: "What caused the EUR 11.4m EBIT decline, and which actions restore a 5% margin by 2028?"

Profit bridge 2022 to 2025:

| Driver | EBIT effect |
|---|---|
| EBIT 2022 | EUR 13.8m |
| Volume growth (+EUR 10m revenue at 16% contribution) | +EUR 1.6m |
| Wage increases not passed through to customers | -EUR 7.0m |
| Energy and fuel | -EUR 2.0m |
| Three contracts renewed at worse terms | -EUR 3.2m |
| Overhead growth | -EUR 0.8m |
| EBIT 2025 | EUR 2.4m |

Most of the decline is commercial: contracts without wage and energy indexation. Cost benchmarks show warehouse productivity in line with peers. Actions: add indexation clauses at renewal (60% of revenue renews within 24 months), reprice or exit the three loss-making contracts, and a targeted overhead programme. An overhead-led cost programme, as first requested, would have addressed less than a tenth of the decline.

## Output template

```markdown
# Profitability turnaround: <client>, <decision question in one line>

**Answer:** <root cause in one sentence>; <actions> restore <x>% margin by <year>.

**Liquidity check:** <cash runway, covenant headroom; safe / at risk>

## Profit bridge <last good year> to <today>
| Driver | Effect |
|---|---|
| EBIT <year> | |
| Volume | |
| Price and terms | |
| Variable cost per unit | |
| Fixed cost | |
| Portfolio and mix | |
| EBIT <year> | |

## Where profit is lost
| Segment / contract / site | Revenue | Margin | Trend | Action |
|---|---|---|---|---|

## Action plan
| Action | EBIT effect (base) | Range | One-off cost | Timing | Owner | Confidence |
|---|---|---|---|---|---|---|
| **Total, reconciled, no double counting** | | | | | | |

## Risks and what would change the answer
1. If <fact>, then <consequence>.
```

## Playbook

How to run this case step by step. Steps 1 to 4 are specific to this case type; the shared engagement procedure covers the rest.

### Step 1: Sharpen the question

Clients describe a symptom and often a pre-selected cure. Ask, in small groups:
- Is cash at risk in the next 13 weeks? What is the runway and covenant headroom? If at risk, secure liquidity first and say so on the answer page.
- Which was the last good year, and what margin is the target by which year?
- What cure has management already chosen, and why?
- Do peers suffer the same, or is it only you?
- Which contracts renew when, and do they carry price indexation?
- For a loss-making unit: what are the options on the table (fix, sell, close) and who decides?

Write the decision question in this form: "What explains the fall from <x>% to <y>% EBIT margin since <year>, and which actions restore at least <z>% by <year>?" It is sharp when it states the profit target, the date and whether liquidity is at risk. Keep the client's cure as one hypothesis, not as the frame.

### Step 2: Instantiate the issue tree

Decompose profit before forming opinions. Adapt the skeleton in the case note; set each threshold with the client.

| Branch | Hypothesis (example form) | Kill criterion |
|---|---|---|
| Liquidity | Cash covers at least 13 weeks without new measures | Runway shorter: switch to a cash plan before structural work |
| Revenue: volume and mix | Volume and mix explain less than <x>% of the decline | Bridge shows volume or mix as the largest driver |
| Revenue: price and terms | Cost increases were not passed through in contracts without indexation | Prices tracked input costs, or indexation was in place |
| Cost: variable per unit | One cost per unit (labour, material, energy) rose faster than price | Cost per unit flat after normalising for mix |
| Cost: fixed | Overhead grew faster than revenue | Fixed cost per unit of output stable |
| Portfolio | A few customers, contracts or sites cause most of the decline | Losses spread evenly across the portfolio |
| Internal vs market | The cause is internal; peers held margin | Peers show the same decline: the answer is structural, not a fix |
| Delivery | Actions reach the target by <year> after one-off costs and notice periods | Reconciled plan reaches less than <x>% of the gap in time |

Split every number into price times volume and cost per unit times volume before comparing years.

### Step 3: Run the deciding analyses, in order

Each analysis ends by marking its hypothesis confirmed, killed or reshaped. If your agent can run sub-tasks in parallel, run 3b to 3d in parallel after the bridge; otherwise in order.

a. **Profit bridge.** Year by year from the last good year to today by driver ([Profit Tree](profit-tree.md)). The bridge must sum to the reported change. It is the most important page of the case. Split each variable cost per unit into input-rate and usage effects in euros where the data allow (labour: wage rate vs output per hour; energy: tariff vs consumption).
b. **Where profit is lost.** Profitability by customer, contract, product, site ([Eighty-Twenty](eighty-twenty.md), [Customer Segmentation](customer-segmentation.md)).
c. **Price realisation.** List to pocket price, discount leakage, indexation clauses ([Pricing Analysis](pricing-analysis.md)).
d. **Cost benchmarks.** [Cost Benchmarking](cost-benchmarking.md) against peers and internal best units, normalised per unit of output; [Value Chain](value-chain.md) to locate the cost by activity. Treat client statements about peers ("they held margin") as unverified until compiled; name the peer figures needed (reported and normalised margin, price indexation practice, cost per unit).
e. **Unit economics.** [Unit Economics](unit-economics.md) for the core offer or contract type: does the model work at all?
f. **Action plan value.** One reconciled bridge of all actions, each with EBIT effect, range, one-off cost, timing, owner and confidence ([Business Case](business-case.md)); [Sensitivity Analysis](sensitivity-analysis.md) on the largest actions. Test the plan's one-off costs and any temporary EBITDA dip against cash runway and covenant headroom; resequence actions that would breach it.

### Step 4: Run the trap checks

Answer each with yes or no and fix every no before writing:
- [ ] The diagnosis came before any cost target; no across-the-board cut.
- [ ] Averages were broken down; loss makers are named, not hidden in a mean margin.
- [ ] Benchmarks are normalised for scope, scale and accounting before any gap is claimed.
- [ ] All actions sit in one bridge with no euro counted twice (price and volume on the same customers, savings booked in two programmes).
- [ ] One-off costs, notice periods and contract renewal dates are in the timing.
- [ ] Liquidity was checked separately from profitability.
- [ ] No action cuts capability the recovery depends on (sales coverage, service quality, maintenance).
- [ ] The model passes [Model Red Flags](model-red-flags.md).

### Step 5: Answer page

Use the output template in [Profitability Turnaround](profitability-turnaround.md) for the body, wrapped in the shared format below. Root cause in one sentence first, then the bridge, the loss makers and the reconciled action plan.

### Case rules

- If the diagnosis contradicts the client's chosen cure, say so on the first line with the number that shows it.

### Answer page format

```markdown
# Profitability turnaround: <client>, <decision question in one line>

**Answer:** <root cause in one sentence>; <actions> restore <x>% margin by <year>.
**Confidence:** high / medium / low, because <one reason>
**Liquidity check:** <runway and covenant headroom: safe / at risk / not known, and the data requested>

<body sections from the case note output template>

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
```

### Limits

Insolvency, restructuring law, labour law and financing negotiations need specialists; flag them. A 13-week cash plan is outside this skill beyond the check in step 1.

## Related

- [Pricing](pricing.md), [Operating Model](operating-model.md), [Profit Tree](profit-tree.md), [Cost Benchmarking](cost-benchmarking.md), [Unit Economics](unit-economics.md), [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Model Red Flags](model-red-flags.md)
