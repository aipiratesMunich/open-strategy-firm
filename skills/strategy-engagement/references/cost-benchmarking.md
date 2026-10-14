# Cost Benchmarking

## What it is

A comparison of a cost line against a reference: other units of the same company, competitors, or industry data. The work is mostly normalisation, so that both sides measure the same scope, at comparable scale, under the same accounting. It answers "is this cost too high, by how much, and why?"

## When to use

- A profitability case needs to know where costs are out of line.
- Several plants, regions or business units do the same work at different cost.
- Management claims a cost gap to competitors and needs it verified before acting.

## When NOT to use

- **No like-for-like reference exists.** A unique process or business model compared with a generic average gives a false gap. Use a bottom-up should-cost model built from activities and rates.
- **The cost is a deliberate choice.** Higher service cost buying a 48-hour response is a strategy. Compare cost per unit of service level, or test the strategy with [Unit Economics](unit-economics.md).
- **The real driver is volume or mix.** If unit cost is high because volume fell, the answer is in revenue. Start with the [Profit Tree](profit-tree.md).
- **Benchmark data would require confidential competitor information.** Stop. Use published reports, industry surveys with defined scope, or internal benchmarks ([Competitor Profiling](competitor-profiling.md) sets the ethical limits).

## Step by step

1. **Define the cost object and the unit.** Example: field service cost per contract-year, cost per order line, finance FTE per EUR 100m revenue. Output: cost object, unit and the decision it informs.
2. **Choose the reference.** Internal first (best unit, best region, own history): data is comparable and owners can be asked. External second: published accounts, association surveys, benchmarking consortia. Output: benchmark set with source and year.
3. **Collect the client's figure** from the user: cost lines, volumes, headcount, allocation keys. Flag any number that is estimated. Output: client baseline.
4. **Normalise like for like.**
   - *Scope:* which activities sit inside the number (travel, overhead, outsourced work, IT).
   - *Scale:* volume, density, batch size; compare at similar scale or adjust per unit.
   - *Accounting:* allocation of overheads, capitalisation versus expense, lease treatment, currency and wage level, period.
   Record each adjustment with its value. Output: normalisation bridge from raw to like-for-like gap.
5. **Size the gap** after normalisation, as a range if adjustments are uncertain. Output: like-for-like gap.
6. **Explain the gap with drivers.** Productivity, price of inputs, design choices, complexity. Ask the people who run the process. Output: driver list with size.
7. **Decide what is addressable.** Separate gaps the client can close from gaps caused by structure it will keep. Output: addressable saving range.

## Inputs needed

- Client cost data at the right granularity, volumes, allocation keys (user-supplied).
- Benchmark data with its definition, scope and year.
- Access to process owners to explain drivers.

## Output produced

- Normalisation bridge from raw gap to like-for-like gap.
- Driver explanation and addressable saving range.

## Common mistakes

- **Raw gap on the slide.** Comparing unadjusted numbers from different scopes. The first sharp question from the CFO kills it.
- **Benchmark without a definition.** An industry average with unknown scope cannot be normalised. Discard it or mark it as indicative.
- **Best-in-class as the target.** The top performer may have a different model. Target the like-for-like median or best internal unit.
- **Allocated cost treated as addressable.** Cutting the unit does not remove group overhead allocated to it.
- **Ignoring service level.** Lower cost bought with worse response time is not a saving.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps believes its field service is 22% more expensive than a main competitor. Cost object: service delivery cost per contract-year.

Alder raw figure: EUR 575 per contract-year (service P&L). Competitor figure: EUR 470, from an association benchmarking survey in which both took part. Raw gap EUR 105, 22%.

Normalisation: the survey definition excludes travel time; Alder's figure includes EUR 60 travel per contract-year. Alder also carries EUR 25 of allocated group IT that the survey excludes. Like-for-like Alder: 575 − 60 − 25 = EUR 490. Remaining gap: EUR 20, about 4%. Scale: the competitor serves a denser customer base in southern Germany; Alder's internal benchmark shows its own densest region at EUR 470 like-for-like.

Conclusion: no structural cost problem. The addressable gap is route density in two sparse regions, worth about EUR 20 per contract-year. The 22% claim is dropped from the board story.

## Output template

```markdown
# Cost benchmark: <cost object> per <unit>

**Answer:** Like-for-like gap <value> (<x%>), addressable <range>.

## Benchmark set
| Reference | Type (internal / external) | Source, year | Definition known? |
|---|---|---|---|

## Normalisation bridge
| Step | Client | Benchmark | Gap | Note |
|---|---|---|---|---|
| Raw | | | | |
| Scope adjustment: <item> | | | | |
| Scale adjustment: <item> | | | | |
| Accounting adjustment: <item> | | | | |
| Like-for-like | | | | |

## Drivers of the remaining gap
| Driver | Size | Addressable? | Evidence |
|---|---|---|---|

**Assumptions flagged:**
-
```

## Related

- [Profit Tree](profit-tree.md), [Value Chain](value-chain.md), [Competitor Profiling](competitor-profiling.md), [Unit Economics](unit-economics.md), [Weak Evidence](weak-evidence.md), [Triangulation](triangulation.md)
