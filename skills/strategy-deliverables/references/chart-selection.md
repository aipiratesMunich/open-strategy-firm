# Chart Selection

## What it is

Choosing the chart from the message, not from the data. Every action title makes one kind of comparison; each comparison has one or two chart types that show it fastest and most honestly. The deck builder uses this mapping for every exhibit; the analyst uses it to decide which cut of the data to pull.

## When NOT to use

- **Two or three numbers.** Write them in the title or as large figures on the page. A chart for "EUR 12.5m versus EUR 7m" is decoration.
- **Exact lookup.** When the reader needs to find a specific value (price per pump type, account list), use a table.
- **Qualitative findings.** Interview themes, process steps or options with criteria belong in a table or simple diagram, not a chart.
- **Exploratory analysis.** While the team is still searching for the message, use whatever chart helps thinking. This mapping applies once the message is known.

## Standard

**Map the message to the comparison, then to the chart.**

| Message type | Typical title words | Use | Avoid |
|---|---|---|---|
| Ranking (items compared) | larger, smaller, ranks, below, above | Horizontal bar, sorted | Pie, unsorted bars |
| Time series (change over time) | grew, fell, since, trend | Vertical bars (few periods) or line (many periods) | Horizontal bars for time |
| Part-to-whole (share) | share, makes up, accounts for | Single stacked bar or 100% bar; pie only with two or three slices | Pie with many slices, donut sets |
| Distribution (frequency) | most, range, concentrated, spread | Histogram (column bars by range band) | Line through categories |
| Correlation (two variables) | related to, rises with, does not depend on | Scatter plot, optionally with a trend line | Paired bars, dual-axis lines |
| Deviation (versus a reference) | above plan, gap, versus target | Bars diverging from zero or a target line | Two lines the reader must subtract |
| Flow and bridge (how A becomes B) | bridge, adds up to, closes the gap | Waterfall | Stacked bars for additions and subtractions |

**Never:**
- Pie or donut with more than three slices, or several pies side by side for comparison. Angles are hard to compare; use bars.
- 3D effects of any kind. They distort size and add nothing ([Slide Quality Red Flags](slide-quality-red-flags.md)).
- Dual axes without care. Two scales let the author make any two lines look related. Use them only when units differ, both axes are labelled in the series colour, and the title does not depend on the visual crossing; otherwise use two small charts stacked with a shared time axis.
- Bar charts not starting at zero. Bar length must represent the value.
- Area charts for comparing several series. Only the bottom series has a flat baseline.

**Always:** one highlight colour for the message, units and period in the header, source at the bottom, direct labels over legends.

## Step by step

1. Write the action title first ([Action Titles](action-titles.md)).
2. Name the comparison it makes from the table above. If it makes two, split the slide.
3. Pick the chart. Prefer the simplest type that shows the comparison.
4. Sort and order: rankings largest to smallest (or the highlighted item first), time left to right.
5. Set honest scales: zero baseline for bars, same scale across charts that will be compared.
6. Highlight the data that proves the title; mute everything else.
7. Label directly, add unit, period and source ([Slide Anatomy](slide-anatomy.md)).
8. Test: show the chart without the title to someone for five seconds. Do they say what the title says?

## Common mistakes

- **Chart chosen from the software's default.** The default rarely matches the message. Struck because the reader has to work out the point.
- **Pie for a ranking.** Prices, margins or growth rates of competitors are not parts of a whole.
- **Line chart across unrelated categories.** A line implies continuity; regions or products have none.
- **Waterfall without a start and end total.** The reader cannot check that the steps add up.
- **Everything on one chart.** Eight series, two axes, three annotations. Split into small multiples or pick the series the title needs.
- **Truncated bar axis to dramatise a small gap.** A 2% difference drawn as a doubling. Credibility is lost once someone notices.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps exhibits for the board:

| Title (message) | Comparison | Chart |
|---|---|---|
| List prices are 6% below the two main competitors | Ranking | Horizontal bars of price index, sorted, Alder highlighted |
| Revenue has been flat at EUR 180m for three years | Time series | Three vertical bars, same value, target line at EUR 200m for 2030 |
| 52% of the installed base is older than eight years without a contract | Part-to-whole | One 100% bar split by age and contract status |
| Downtime costs per failure range from EUR 4,000 to EUR 40,000 | Distribution | Histogram of reported cost per failure by cost band |
| Service and pricing just reach the 2030 target, with almost no cushion | Flow | Waterfall: EUR 180m, plus about EUR 12.5m service, plus about EUR 7m price, equals about EUR 200m, target line at EUR 200m |

Weak version of the last one: a pie of "growth sources" with service, price and "other". It hides how thin the margin to the target is, which is the board's most important question.

## Output template

```markdown
| Slide | Action title | Comparison (ranking / time / part-to-whole / distribution / correlation / deviation / flow) | Chart type | Highlight | Scale note | Source |
|---|---|---|---|---|---|---|
| | | | | | zero baseline / same scale as slide <n> | |
```

## Related

- [Slide Anatomy](slide-anatomy.md), [Action Titles](action-titles.md), [Slide Quality Red Flags](slide-quality-red-flags.md), [Deck Structure](deck-structure.md)
