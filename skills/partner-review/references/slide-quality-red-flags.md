# Slide Quality Red Flags

## What it catches

Slides that hide their message: titles that describe instead of conclude, charts that do not prove the title, decoration that competes with data, and inconsistencies that make the reader doubt the numbers. A reader spends seconds per slide; if the message is not obvious in that time, it is lost.

## When to apply

- Every slide in a deck at gate 3, and the ghost deck titles at gate 2.

## Checks

1. **One message per slide.** Can the slide's point be said in one sentence? If there are two points, there should be two slides.
2. **Action title.** Is the title a full sentence stating the finding, at most two lines? (See [Action Titles](action-titles.md).)
3. **Body proves title.** Does the chart or table directly show what the title claims, no more and no less?
4. **Chart fits the comparison.** Does the chart type match the comparison the message makes: ranking, change over time, parts of a whole, distribution, correlation? (See chart selection.)
5. **Highlight.** Is the data point that carries the message visually emphasised, with everything else muted?
6. **Clutter.** Are there 3D effects, gridlines, legends that could be direct labels, decorative icons or colour without meaning?
7. **Honest scales.** Do bar charts start at zero? Are axes and scales consistent across comparable charts? Is any visual effect larger or smaller than the data effect?
8. **Labels and units.** Are units, currency, time period and data source on every chart?
9. **Numbers tie.** Do the same numbers match across slides, executive summary and model?
10. **Reading load.** Is text short enough to read in under a minute? No full paragraphs on a slide meant to be presented.
11. **Consistency.** Same terms, colours, number formats and abbreviations throughout.
12. **Tracker.** Can the reader see where the slide sits in the storyline (section marker or consistent structure)?

## Severity

- **Blocker:** check 9; check 7 when the distortion changes the impression of the main finding.
- **Major:** checks 1, 2, 3, 4 on key-line slides.
- **Minor:** checks 5, 6, 8, 10, 11, 12.

## False alarms

- A dense backup table in the appendix is fine; it is reference material, not a presented slide.
- A line chart for an index or growth rate may start above zero if the axis is clearly marked.
- House style elements (logo, footer) are not clutter.

## Worked example

*Fictional example. Company, figures and people are invented.*

Slide: title "Pricing benchmark". Body: 3D pie chart with Alder and six competitors' price indices, legend on the right, no source.

- Major (check 2): Title is a label. Rewrite: "Alder's list prices are 6% below the two main competitors for comparable pumps."
- Major (check 4): Pie charts show parts of a whole; prices are a ranking. Use a horizontal bar chart sorted by price index.
- Minor (check 5): Highlight Alder's bar, mute the others.
- Minor (check 6): Remove 3D and legend; label bars directly.
- Minor (check 8): Add source and date: "Distributor price lists, Q2 2026, DN50 standard pumps."

## Output template

```markdown
# Slide review: <deck>

| Slide | Severity | Check | Problem | Fix |
|---|---|---|---|---|

**Titles-only read-through tells the story:** yes / no
**Numbers checked against model:** yes / no, <mismatches>
```

## Related

- [Partner Review Checklist](partner-review-checklist.md), [Storyline and Ghost Deck](storyline.md), [Action Titles](action-titles.md), chart selection, [Slide Anatomy](slide-anatomy.md)
