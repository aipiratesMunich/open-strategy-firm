# Growth Strategy

## Typical questions

The client usually names an ambition, rarely a decision. Sharpen it into a gap, a deadline and the constraints the answer must respect.

- "We need to grow." → "Which combination of levers closes the gap from EUR <x> to EUR <y> revenue by <year>, within <capital limit> and without margin falling below <floor>?"
- "Our core has stalled. Where next?" → "Is the core really saturated, or are we losing share or leaving value in the installed base? Which adjacent move earns more than its cost of capital?"
- "Should we go digital / international / into services?" → Treat the named option as one hypothesis among several. The question becomes "Does <option> close more of the gap per euro and per unit of risk than the alternatives?"
- "The board wants a growth plan." → Ask what the board will decide, when, and what it has already ruled out (acquisitions, new plants, dilution). Those rule-outs are part of the question.

A growth question is sharp when it states the gap in money, the year, the hard constraints and the decision maker.

## Issue tree skeleton

A MECE starting tree. Adapt, never use unchanged. Start from the gap, then split by where growth can come from.

- **How large is the gap, honestly?**
  - Base-case trajectory of the core without new action (momentum case)
  - Gap to target in revenue and profit, by year
- **Can the core grow faster?** (existing products, existing customers and markets)
  - Market growth: is the served market growing, flat or shrinking? *H: market grows about 2% a year; the core is losing share, not stalling with the market.*
  - Share: are we winning or losing against named competitors, and why?
  - Wallet share and installed base: what do existing customers buy elsewhere? *H: service and spare parts are bought from third parties for most of the installed base.*
  - Price: is the price position below value delivered? *H: list prices sit below competitors without a volume reason.*
- **Can adjacent moves add growth?**
  - New offers to existing customers (services, software, consumables)
  - Existing offers to new segments or geographies
  - New business models (subscription, as-a-service, outcome pricing)
- **Can inorganic moves add growth?** (only if not ruled out)
  - Acquisitions, partnerships, licensing
- **Which portfolio of moves is best?**
  - Size, timing and certainty of each lever against the gap
  - Capital and capability required, against the limits
  - Risk: what happens to the plan if the largest lever under-delivers?

The [Ansoff Matrix](ansoff-matrix.md) is a useful check that no quadrant was skipped. It is not the tree itself: the tree is built around the gap and the constraints.

## Key analyses

- **Gap and momentum case.** Project the core without new action, then size the gap. A simple [Business Case](business-case.md) baseline. Without it, every lever looks necessary.
- **Market and share decomposition.** [Market Sizing](market-sizing.md) for each served segment, split into market growth versus share change. Tells you whether the core problem is the market or the company.
- **Installed-base and wallet analysis.** [Customer Segmentation](customer-segmentation.md) of existing customers by what they buy, from whom, and what they would buy. Usually the cheapest growth.
- **Lever sizing.** Each lever sized with a range, its drivers and an evidence grade. Use [Unit Economics](unit-economics.md) for new offers and [Pricing Analysis](pricing-analysis.md) for price levers.
- **Adjacency attractiveness.** For each adjacency: market size, structure ([Five Forces](five-forces.md)), right to win ([Competitor Profiling](competitor-profiling.md), [Value Chain](value-chain.md)).
- **Portfolio and timing.** Map levers on [Three Horizons](three-horizons.md) so the plan does not rest on far-out bets alone. [Growth-Share Matrix](growth-share-matrix.md) for multi-business clients.
- **Stress test.** [Scenario Planning](scenario-planning.md) and [Sensitivity Analysis](sensitivity-analysis.md) on the two or three largest levers.

## Traps

- **Adding up hope.** Summing the upside case of every lever until the gap closes. Size each lever on its base case, show the range, and state the remaining gap openly.
- **Skipping the core.** Teams jump to adjacencies because they are more exciting. The core and the installed base usually hold the fastest and cheapest growth.
- **Inside view on new moves.** Forecasting a new market or offer from the plan's own logic. Check ramp-up against what comparable launches achieved ([Weak Evidence](weak-evidence.md), outside view).
- **Market growth confused with share growth.** "Revenue flat" can mean a flat market or a growing market with share loss. The two need opposite answers.
- **Ignoring the constraints.** A plan that needs acquisitions the board has ruled out, or more capital than allowed, is not an answer.
- **Too many initiatives.** Eight levers of EUR 2m each is an organisation problem, not a strategy. Two or three large levers plus small ones as options.
- **Revenue without margin.** Growth that dilutes margin below the floor fails the brief. Show profit next to revenue for every lever.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps: revenue EUR 180m, flat for three years, EBIT margin about 9.5%. Board target: EUR 200m by 2030, EBIT margin not below 9%, capital limit EUR 20m, no acquisitions; decision in March 2027. Sharpened question: "Which organic levers close the EUR 20m revenue gap by 2030 within EUR 20m capital and a 9% margin floor?"

Momentum case: flat at EUR 180m. Levers sized:

| Lever | Base case 2030 | Range | Investment | Status |
|---|---|---|---|---|
| Service contracts on the uncontracted installed base | EUR 12.5m | EUR 8m to 15.6m | EUR 6m | keep |
| List price reset (+4%, prices 6% below the two main competitors) | about EUR 7m | depends on volume reaction | low | keep |
| Poland entry | under EUR 5m | | | killed (two local players hold 78%) |

Service: 52% of 60,000 pumps are older than eight years and have no contract, about 31,200 pumps. At 40% take-up and about EUR 1,000 per pump per year this gives about EUR 12.5m. The two kept levers sum to about EUR 19.5m, which reaches the EUR 200m target in the base case with almost no cushion. The team states the thin margin openly and names two options for it (spare-parts attach on new contracts as a buffer; target reset with the board if take-up lags) rather than stretching the service take-up assumption to create one.

## Output template

```markdown
# Growth strategy: <client>, <decision question in one line>

**Answer:** <which levers, how much, by when, at what investment>

## The gap
| | <year 0> | <target year> |
|---|---|---|
| Revenue, momentum case | | |
| Revenue, target | | |
| Gap | | |
| Constraints | capital <x>, margin floor <y>, ruled out: <...> |

## Levers
| Lever | Revenue base case | Range | EBIT effect (EUR) | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| | | | | | | strong / medium / weak | keep / option / killed |

**Sum of kept levers (base case):** <x>; **remaining gap:** <y>; **how we close or accept it:** <...>

## Killed options and why
- <option>: <fact that killed it>

## Risks and what would change the answer
1. If <largest lever> delivers only <low case>, then <consequence>.

## Next steps
| What | Who | By when |
|---|---|---|
```

## Playbook

How to run this case step by step. Steps 1 to 4 are specific to this case type; the shared engagement procedure covers the rest.

### Step 1: Sharpen the question

The client names an ambition, rarely a decision. Ask, in small groups:
- What revenue and profit by which year? Where does the target come from (board, investors, plan)?
- What is ruled out: acquisitions, new plants, dilution, specific countries?
- How much capital may the plan use, and what margin floor must it hold?
- Who decides, at which meeting, and what will they approve (budget, plan, first moves)?
- Has revenue been flat because the market is flat or because share is lost? What do you believe, and on what basis?

Write the decision question in this form: "Which combination of levers closes the gap from <x> to <y> revenue by <year>, within <capital> and without margin below <floor>?" It is sharp when it states the gap in money, the year, the hard constraints and the decision maker. If the client named one option ("go international"), keep it as one hypothesis among several.

### Step 2: Instantiate the issue tree

Start from the gap, never from a list of ideas. Adapt the skeleton in the case note; set each threshold with the client. Keep every branch; mark one already settled by the data as settled instead of dropping it.

| Branch | Hypothesis (example form) | Kill criterion |
|---|---|---|
| Gap and momentum | Momentum case misses the target by <x> in <year> | Gap under <x>: question becomes defend the core, not growth |
| Core: market vs share | Served market grows; the core is losing share | Share stable or rising for three years: the market is the limit, shift weight to adjacencies |
| Core: installed base | Most of the installed base buys service or parts elsewhere | Third-party share small or already contracted: lever below <x> |
| Core: price | List prices sit below comparable competitors without a volume reason | Like-for-like gap explained by spec or service |
| Adjacencies | At least one adjacency can add <x> with a right to win | Addressable segment too small or held by entrenched players |
| Inorganic | Only if not ruled out: a buy closes more gap per euro than organic | Ruled out by the board, or switch to the M&A screening playbook ([M&A Screening](m-and-a-screening.md)) |
| Portfolio | Two or three levers on base case close at least <x>% of the gap | Base-case sum below half the gap: reopen the target with the board |

Check with the Ansoff grid that no quadrant was skipped by habit; the tree itself stays built around the gap.

### Step 3: Run the deciding analyses, in order

Each analysis ends by marking its hypothesis confirmed, killed or reshaped. If your agent can run sub-tasks in parallel, run 3b to 3d in parallel; otherwise in order.

a. **Gap and momentum case.** Project the core without new action, then size the gap per year ([Business Case](business-case.md) baseline). Without it every lever looks necessary.
b. **Market and share split.** [Market Sizing](market-sizing.md) per served segment, separated into market growth and share change.
c. **Installed base and wallet.** [Customer Segmentation](customer-segmentation.md) of existing customers by what they buy and from whom; [Jobs to Be Done](jobs-to-be-done.md) where the offer is new.
d. **Lever sizing.** Base case, range, drivers, evidence grade per lever. [Unit Economics](unit-economics.md) for new offers, [Pricing Analysis](pricing-analysis.md) for price.
e. **Adjacency attractiveness.** Size, structure ([Five Forces](five-forces.md)), right to win ([Competitor Profiling](competitor-profiling.md), [Value Chain](value-chain.md)).
f. **Portfolio and timing.** Place levers on [Three Horizons](three-horizons.md); use [Growth-Share Matrix](growth-share-matrix.md) only for multi-business clients.
g. **Stress test.** [Scenario Planning](scenario-planning.md) and [Sensitivity Analysis](sensitivity-analysis.md) on the two or three largest levers.

### Step 4: Run the trap checks

Answer each with yes or no and fix every no before writing:
- [ ] Each lever is sized on its base case, and the remaining gap is shown openly, not closed by stretching assumptions. Where evidence is thin, the base case comes from a labelled assumption with a weak grade and a wide range.
- [ ] The core and installed base were sized before any adjacency.
- [ ] Ramp-up of new moves is compared with what comparable launches achieved, or the range is widened and the missing comparison named.
- [ ] Market growth and share change are separated.
- [ ] No lever needs a move the board ruled out or capital above the limit.
- [ ] Two or three large levers carry the plan; small ones are options.
- [ ] Every lever shows its EBIT effect in euros next to its revenue, and the page states group EBIT margin after the kept levers against the floor.

### Step 5: Answer page

Use the output template in [Growth Strategy](growth-strategy.md) for the body, wrapped in the shared format below. Kept levers, killed options with the fact that killed each, remaining gap and how it is closed or accepted.

### Case rules

- Decide. A short answer with stated uncertainty beats a hedged list of options; with little data, the Answer is a provisional day-one answer labelled as hypothesis (most likely levers and rough split of the gap).

### Answer page format

```markdown
# Growth strategy: <client>, <decision question in one line>

**Answer:** <which levers, how much, by when, at what investment>
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

Sizing is only as good as the client's data; say where it is thin. Legal, tax and financing questions are flagged, not answered.

## Related

- [Market Entry](market-entry.md), [Pricing](pricing.md), [M&A Screening](m-and-a-screening.md), [Operating Model](operating-model.md), [Problem Definition](problem-definition.md), [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Synthesis](synthesis.md), [Ansoff Matrix](ansoff-matrix.md), [Three Horizons](three-horizons.md)
