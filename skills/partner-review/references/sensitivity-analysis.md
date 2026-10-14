# Sensitivity Analysis

## What it is

Changing a model's inputs to see how much the output moves, so the team knows which assumptions decide the answer and how far each can move before the answer flips. It answers: "Which inputs matter most, and how wrong can they be before we would recommend something else?"

## When to use

- Every business case or model that supports a recommendation ([Business Case](business-case.md), [Excel Model Standards](excel-model-standards.md)).
- Deciding where to spend research effort: the top inputs get [Triangulation](triangulation.md), the rest do not.
- Writing the "what would change the answer" section of a [Synthesis](synthesis.md).
- Board discussions where members challenge specific assumptions.

## When NOT to use

- **Inputs that move together.** One-way sensitivity varies one input while holding the others fixed. If a competitor move would cut both price and take-up at once, one-way results understate the risk. Use scenario planning for coherent combinations.
- **Deep uncertainty about the structure itself** (a new technology, a regulatory change that rewrites the market). Varying inputs of the wrong model gives false comfort. Use scenarios or a staged decision with checkpoints.
- **Before the base case is checked.** Sensitivities on a model with errors are precise nonsense. Fix the model first ([Model Red Flags](model-red-flags.md)).
- **Formal probability questions** (what is the chance NPV falls below zero). One-way ranges do not give probabilities. Use a probabilistic simulation, if the input distributions are credible.

**Scenario or sensitivity?** Sensitivity moves one input at a time and ranks inputs by impact. A scenario moves several inputs together according to a story about the world (a competitor response, a recession) and tests the answer under that story. Use sensitivity to find the decisive inputs; use scenarios to test whether the recommendation survives plausible futures.

## Step by step

1. **Fix the output metric.** Input: the decision. Output: one metric the decision turns on (2030 revenue, NPV, payback years, margin) and the threshold that flips the decision.
2. **List the inputs** that drive the metric. Output: input list with base value and source.
3. **Set a realistic range for each input.** Low and high from evidence: interview spread, benchmark range, history. Ranges from optimism alone are too narrow; widen them where the evidence is thin.
4. **Run one-way sensitivity.** Change one input to its low, then its high, holding all others at base. Record the output each time.
5. **Rank in a tornado.** Sort inputs by output swing (high minus low), largest first. The top two or three usually explain most of the uncertainty.
6. **Compute break-even values** for the top inputs: the value at which the output hits the decision threshold. Compare each with its plausible range. A break-even inside the range is a risk to name; one outside it means that input alone cannot flip the decision.
7. **Add two or three scenarios** for inputs that move together.
8. **Write the conclusion.** Which inputs decide the answer, how far they are from break-even, and what the team did or will do to narrow them.

## Inputs needed

- A checked base-case model with inputs separated from calculations.
- Evidence-based ranges for the main inputs.
- The decision threshold.

## Output produced

- Tornado table: inputs ranked by swing.
- Break-even value for each top input against its range.
- Scenario results.
- A short statement of what would change the answer.

## Common mistakes

- **Symmetric plus or minus 10% on everything.** Ranges must come from evidence. Take-up might plausibly vary by half; a contracted price by 5%. Uniform ranges produce a meaningless ranking.
- **Sensitivity on inputs nobody doubts.** Twenty rows in a tornado, three that matter. Show the three.
- **No threshold.** Showing that NPV moves from 4 to 9 says nothing until the reader knows the decision flips at 2.
- **Treating one-way results as the worst case.** The worst case is several bad inputs at once; that is a scenario.
- **Sensitivity hidden in the appendix.** If the answer flips inside a plausible range, that belongs on the executive summary.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps service-contract offer. Metric: service revenue in 2030. Base: 31,200 uncontracted pumps (52% of 60,000) x 40% take-up x EUR 1,000 = EUR 12.5m. Investment EUR 6m. Decision rule from the board: payback within three years, so annual contribution of at least EUR 2.0m. Contribution margin on service revenue: 40% (EUR 400 per contract-year after EUR 600 delivery cost and lost repair margin, from unit economics), so revenue must reach at least EUR 5.0m.

Tornado (one-way, others at base):

| Input | Low / high | Revenue low | Revenue high | Swing |
|---|---|---|---|---|
| Take-up | 25% / 50% | EUR 7.8m | EUR 15.6m | EUR 7.8m |
| Price per pump per year | EUR 800 / 1,200 | EUR 10.0m | EUR 15.0m | EUR 5.0m |
| Uncontracted share | 45% / 55% | EUR 10.8m | EUR 13.2m | EUR 2.4m |

Break-even: take-up 16% (below the 25% low end) and price EUR 760 at base take-up (below EUR 800, since delivery cost stays at EUR 600 per contract). Both are outside the plausible range, so the payback rule holds input by input.

Scenario "competitor matches 48-hour response in 2028": take-up 25% and price EUR 900 together give EUR 7.0m revenue and EUR 2.3m contribution. Payback about two and a half years, with little margin left. Conclusion: take-up decides the answer; the team names it as the input to track in the first pilot year.

## Output template

```markdown
# Sensitivity: <output metric>, decision threshold <value>

**Base case:** <value> (<key inputs>)

| Rank | Input | Base | Low / high (evidence) | Output low | Output high | Swing | Break-even value | Break-even inside range? |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | yes / no |

**Scenarios (inputs moved together):**
| Scenario | Story | Inputs changed | Output | Decision holds? |
|---|---|---|---|---|

**What would change the answer:** <input> below <break-even> → <consequence>
```

## Related

- scenario planning, [Business Case](business-case.md), [Excel Model Standards](excel-model-standards.md), [Model Red Flags](model-red-flags.md), [Triangulation](triangulation.md), [Synthesis](synthesis.md), [Weak Evidence](weak-evidence.md)
