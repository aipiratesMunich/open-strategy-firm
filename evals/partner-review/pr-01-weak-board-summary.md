# pr-01: Weak board summary

## Prompt

> Review this executive summary before it goes to the Brightwell board next week. Is it ready?

Input file: `pr-01-input.md`

## Planted defects

| # | Defect | Expected severity |
|---|---|---|
| D1 | The question in the problem statement (which two moves to fund in the 2027 budget) is never answered; no move is named with an amount | Blocker |
| D2 | Recommendation uses "explore" and "consider"; no owner, budget or date | Blocker |
| D3 | Summary says catering adds EUR 9m; the table on the same page sums to EUR 6.4m | Blocker |
| D4 | "Customers love the brand" rests on a survey of 40 loyalty-club members only | Major |
| D5 | Online growth assumes 35% annual growth for five years with no comparison to what similar bakery chains achieved | Major |
| D6 | Franchise option was in scope but disappears without explanation | Major |
| D7 | Title "Market overview" is a label, not a finding | Minor or Major |

## Pass criteria

- Must: verdict is **Return**.
- Must: finds D1, D2 and D3, each rated Blocker.
- Must: finds at least two of D4, D5, D6.
- Must: states the question the draft must answer and notes that the draft does not answer it.
- Must: gives a concrete fix for every finding (not "consider improving").
- Must: includes a premortem with three reasons.
- Must: lists at least one thing that is good and should survive (the store-level margin data is solid).
- Must: shows what "fixed" looks like in two to four sentences.
- Must not: invent benchmark figures (e.g. "bakery chains typically grow online 12%") without a source; it may say which comparison is missing.
- Must not: rewrite the whole document instead of reviewing it.
