# Scenario Planning

## What it is

A set of two to four internally consistent descriptions of how the client's environment could look at the decision horizon, built from the few uncertainties that matter most. The strategy is then tested against each. It answers "does our recommendation still hold if the world turns out differently, and what would tell us early?"

Three tools are often confused:
- **Forecast:** one expected value for a driver. Useful when the future resembles the past.
- **Sensitivity:** one driver moved at a time, all else fixed ([Sensitivity Analysis](sensitivity-analysis.md)). Shows which numbers matter.
- **Scenario:** several drivers moved together in a coherent story, including changes in who holds power in the market. Shows whether the strategy survives a different world.

## When to use

- The decision is long-lived (investment, entry, capacity) and its horizon is five years or more.
- Two or more external uncertainties could each change the answer, and they interact.
- The team or board anchors on one forecast and treats it as certain.

## When NOT to use

- **One driver dominates and the rest is stable.** A sensitivity table with break-even values is faster and clearer.
- **The horizon is short and the data is good.** For next year's budget, use a forecast with a range.
- **The uncertainty is internal.** Execution risk (will the team deliver?) belongs in the plan and the premortem, not in external scenarios.
- **Scenarios would end up as optimistic, base and pessimistic.** That is a sensitivity with labels. Either find real structural uncertainties or use the [Business Case](business-case.md) up and down cases.

## Step by step

1. **State the decision and the horizon.** Output: "Should <client> do <X>; horizon <year>."
2. **List driving forces** outside the client's control: demand, technology, regulation, competitor and customer behaviour, input prices. Ask the user and check interviews. Output: list of 10 to 20 forces.
3. **Separate predetermined elements from critical uncertainties.** Predetermined: will happen in all futures (an ageing installed base). Critical uncertainty: high impact on the decision and genuinely open. Rate each on impact and uncertainty. Output: ranked list.
4. **Pick two critical uncertainties** that are independent of each other and define the two axes of a 2x2. Each axis has two end states, described concretely. Output: 2x2 frame.
5. **Write each scenario** as a short, named story: what is true in that world at the horizon, how it got there, and what it means for the client's customers and competitors. Add the predetermined elements to every scenario. Output: four scenario descriptions.
6. **Quantify where it matters.** Translate each scenario into values for the model drivers (volume, price, share). Output: driver table per scenario.
7. **Test the strategy** in each scenario. Does it still create value? What would have to change? Identify a no-regret core (works in all), options (pay off in some) and bets (need one specific world). Output: strategy test table.
8. **Define signposts.** For each scenario, two or three observable indicators with a threshold that would show it is unfolding, and the action to take when they trip. Output: signpost table with owner and review date.

## Inputs needed

- The decision and horizon.
- Interview notes and client views on external drivers.
- Market and model drivers from [Market Sizing](market-sizing.md) and the [Business Case](business-case.md).
- Any available trend data. If offline, the user supplies it or the driver is rated by judgement and flagged.

## Output produced

- Ranked driving forces, a 2x2 of critical uncertainties, four named scenarios with driver values, strategy test, signposts with triggers.

## Common mistakes

- **Optimistic, base, pessimistic.** One driver scaled up and down. Partners strike it because it tests nothing structural.
- **Most likely scenario.** Assigning probabilities invites the team to plan for one and ignore the rest.
- **Correlated axes.** Two axes that move together collapse the 2x2 into a line.
- **Scenarios with no decision.** A well-written future that never tests the recommendation is a report, not analysis.
- **No signposts.** Without triggers, the scenarios are forgotten after the board meeting.
- **Overconfident base.** Forecasts by insiders tend to be too optimistic and too narrow; scenarios exist partly to widen that view.

## Worked example

*Fictional example. Company, figures and people are invented.*

Decision: should Alder Pumps invest EUR 6m in a service-contract offer; horizon 2030. Predetermined: the installed base keeps ageing; skilled technicians stay scarce.

Critical uncertainties: (1) DACH process-industry output: shrinking versus stable. (2) Control of maintenance: pump makers keep the service relationship versus multi-brand service platforms take it.

| | Pump makers keep service | Platforms take service |
|---|---|---|
| **Output stable** | Home advantage: contracts grow as planned | Platform squeeze: Alder serves as subcontractor at lower prices |
| **Output shrinking** | Loyal but smaller: fewer pumps, high take-up among survivors | Double squeeze: base and margin both fall |

Strategy test: the contract offer creates value in Home advantage and Loyal but smaller (take-up above the 28% break-even). In Platform squeeze, it holds only if Alder adds remote monitoring that platforms cannot offer. In Double squeeze, it fails. No-regret core: launch with segment A. Option: remote-monitoring module, decided in 2028. Signposts: a multi-brand platform winning a frame contract with a top-20 Alder customer; two consecutive years of falling chemicals output in DACH; more than three customers per quarter asking for open data interfaces. Owner: head of service, reviewed each half-year.

## Output template

```markdown
# Scenarios: <decision>, horizon <year>

**Answer:** The recommendation holds in <n> of 4 scenarios. No-regret core: <...>. Options: <...>. Watch: <signposts>.

## Driving forces
| Force | Impact (H/M/L) | Uncertainty (H/M/L) | Predetermined or critical |
|---|---|---|---|

## 2x2
| | <Axis 2, end state A> | <Axis 2, end state B> |
|---|---|---|
| **<Axis 1, end state A>** | <name>: <one line> | <name>: <one line> |
| **<Axis 1, end state B>** | <name>: <one line> | <name>: <one line> |

## Driver values per scenario
| Driver | <S1> | <S2> | <S3> | <S4> |
|---|---|---|---|---|

## Strategy test
| Element of strategy | <S1> | <S2> | <S3> | <S4> | No-regret / option / bet |
|---|---|---|---|---|---|

## Signposts
| Signpost | Threshold | Points to | Action if tripped | Owner | Review |
|---|---|---|---|---|---|
```

## Related

- [Sensitivity Analysis](sensitivity-analysis.md), [Business Case](business-case.md), [Market Sizing](market-sizing.md), [Competitor Profiling](competitor-profiling.md), [Three Horizons](three-horizons.md), [Partner Review Checklist](partner-review-checklist.md)
