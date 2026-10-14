# Market Sizing

## What it is

An estimate of how much revenue a defined market holds, built twice: once top-down from a published aggregate, once bottom-up from countable units times value per unit. The two estimates are then reconciled. It answers "is this pool big enough to matter for the client's target, and how much of it can the client realistically win?"

## When to use

- A growth or entry decision depends on whether a market can carry a revenue target.
- The client quotes a market figure from a report and nobody knows what it includes.
- A new offer (service, product, region) needs a revenue ceiling before a business case is built.

## When NOT to use

- **The decision does not depend on market size.** If the client already holds most of a mature market, the question is share or price. Use [Pricing Analysis](pricing-analysis.md) or competitor profiling.
- **The market is obviously large relative to the target.** Sizing a EUR 40bn market for a EUR 5m entry wastes days. Size the reachable segment and the obtainable share only.
- **Countable units are not available and cannot be estimated.** A top-down figure alone is a guess with a citation. Run [Scenario Planning](scenario-planning.md) on demand drivers instead, and say the size is unknown.
- **The real question is customer behaviour.** Whether customers will switch matters more than how many exist. Start with customer segmentation and interviews (interview guide).

## Step by step

1. **Define the market in one sentence.** Product or service, customer type, geography, year, and whether the unit is revenue, volume or both. Output: market definition. Ask the user to confirm it before computing anything.
2. **Define the three layers.** TAM: total spend on this need in the geography. SAM: the part the client's offer can serve with its current model and channels. SOM: the part it can win in the time frame. Write the filter that separates each layer. Output: layer definitions.
3. **Build top-down.** Start from one published or client-held aggregate. Apply filters one at a time, each with a source or a flagged assumption. Output: top-down SAM.
4. **Build bottom-up.** Count units (customers, sites, installed machines), multiply by value per unit (price times frequency). Ask the user for unit counts and prices; if missing, state an assumption and mark it. Output: bottom-up SAM and SOM.
5. **Reconcile.** Put both SAM estimates side by side. If they differ by more than about a third, find the cause before using either: different scope, double counting, stale aggregate, wrong unit value. Adjust the definition or one estimate and record why. If a gap of 2x or more remains unexplained, report the range and do not pick a point. Output: reconciliation table with the explained gap.
6. **Set SOM from evidence.** Take-up or share must come from comparable cases, interviews or pilot data. Show a range (low, base, high). Output: SOM range.
7. **Test sensitivity** on the two or three widest assumptions and give the break-even value for the client's target ([Sensitivity Analysis](sensitivity-analysis.md)). Output: sensitivity table.
8. **Write the so-what.** One sentence: does SOM meet the target, and with which assumption at risk.

## Inputs needed

- Client target (revenue, year) the market must support.
- Unit counts: customer lists, installed base, CRM or ERP exports.
- Prices or willingness to pay per unit and purchase frequency.
- One aggregate for top-down: association data, statistical office, analyst report, with its scope definition.
- Evidence for take-up or share: interviews, pilots, comparable launches.

## Output produced

- Market definition and TAM/SAM/SOM layer definitions.
- Top-down and bottom-up estimates with each assumption sourced or flagged.
- Reconciliation table and a SOM range with sensitivities.

## Common mistakes

- **TAM theatre.** Leading with a large TAM to impress. Nobody can win a TAM; the board needs SOM and the evidence behind it. Partners strike the TAM slide or move it to the appendix.
- **One method only.** A single top-down chain of percentages looks precise and cannot be checked. Without the second method there is no test.
- **Silent reconciliation.** Averaging the two estimates hides the scope error that caused the gap.
- **Invented filters.** "Assume 10% are reachable" with no basis. Every filter needs a source or a visible assumption flag and a range.
- **Mismatched units.** Revenue in one estimate, volume in the other; one year versus cumulative.
- **SOM from ambition.** Share set to what the target requires. Derive share from evidence, then compare with the target.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps asks whether service contracts on its own installed base in DACH can add at least EUR 10m revenue by 2030. Market definition: annual service-contract revenue on Alder pumps in DACH, 2030, contracts with 48-hour response.

Bottom-up: installed base 60,000 pumps. Older than eight years without a contract: 52%, so 31,200 pumps (ERP). Willingness to pay about EUR 1,000 per pump per year (plant-manager interviews), so SAM = 31,200 × EUR 1,000 = EUR 31.2m. TAM for the same need across all 60,000 Alder pumps = EUR 60m. Take-up base 40% (range 25% to 50%): SOM = EUR 12.5m (EUR 7.8m to EUR 15.6m).

Top-down: an industry association puts DACH spend on industrial pump service contracts at EUR 500m. Alder's share of the installed pump base in DACH is about 8% (association plus Alder sales history), so the top-down SAM is EUR 40m.

Reconciliation: gap EUR 8.8m, 22% of the top-down figure. Two causes: the association figure includes contracts with spare parts, priced higher than Alder's planned offer, and pumps younger than eight years. Adjusted for scope, the estimates agree within about 10%. Conclusion: the EUR 10m target holds in the base case and fails below about 32% take-up (EUR 10m / EUR 31.2m). Take-up is the assumption to test.

## Output template

```markdown
# Market size: <market definition in one line>

**Target to test:** <revenue> by <year>
**Answer:** SOM <low> to <high>, base <value>. Target met / not met. Key risk: <assumption>.

## Layers
| Layer | Definition (filter) | Value | Source / assumption |
|---|---|---|---|
| TAM | | | |
| SAM | | | |
| SOM | | <low / base / high> | |

## Bottom-up
| Driver | Value | Unit | Source or ASSUMPTION |
|---|---|---|---|
| Units | | | |
| Share of units in scope | | % | |
| Value per unit per year | | | |
| Take-up / share | | % | |

## Top-down
| Step | Value | Source or ASSUMPTION |
|---|---|---|
| Aggregate | | |
| Filter 1 | | |

## Reconciliation
| Top-down SAM | Bottom-up SAM | Gap | Explained by | Remaining gap |
|---|---|---|---|---|

## Sensitivity
| Assumption | Low | Base | High | Break-even for target |
|---|---|---|---|---|
```

## Related

- [Triangulation](triangulation.md), [Sensitivity Analysis](sensitivity-analysis.md), customer segmentation, [Business Case](business-case.md), weak evidence, hypothesis driven approach
