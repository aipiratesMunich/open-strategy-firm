# Logic Gaps

## What it catches

Arguments that look complete but do not prove what they claim: conclusions that leap past their support, groups of points that overlap or leave holes, causal claims built on correlation, and recommendations that answer a different question from the one asked. Logic gaps are what a sharp board member finds in the first five minutes.

## When to apply

- Every storyline, executive summary and memo at gates 2 and 3.
- Every issue tree and hypothesis tree at gate 2.

## Checks

1. **Question match.** Does the top message answer the question in the problem statement, using its terms (decision, metric, date)? Or does it answer an easier neighbour question?
2. **Vertical logic.** For each point, ask "why?" or "how do we know?". Do the points directly below answer that question, and only that one?
3. **Sufficiency.** If all supporting points were true, would the conclusion have to be true? If not, which missing point is needed?
4. **Overlap.** Do any two supporting points say the same thing in different words, or count the same euros twice?
5. **Gaps in coverage.** For a list that claims to be complete (all segments, all cost lines, all options), what is missing? Do the parts add to the whole?
6. **Grouping type.** Is each group either a chain of reasoning (A, therefore B, therefore C) or a set of like items (three reasons, three segments)? Mixed groups hide gaps.
7. **Causality.** Is any "because" really just "at the same time as"? Is reverse causation or a third factor ruled out?
8. **Alternatives.** Is the recommended option compared with the realistic alternatives, including doing nothing?
9. **Scope drift.** Does the recommendation stay within the agreed scope, or does it smuggle in topics that were ruled out?
10. **Internal consistency.** Do any two pages contradict each other in fact or in direction?

## Severity

- **Blocker:** checks 1, 3 on the governing thought, 10.
- **Major:** checks 2, 3 on section level, 4, 5, 7, 8.
- **Minor:** checks 6, 9 unless the drift changes the decision, then Major.

## False alarms

- A deliberate simplification stated as such ("we ignore the export business, which is below 3% of revenue") is not a coverage gap.
- Not every list must be exhaustive. Three reasons can be the three most important ones if labelled that way.
- A judgement call is allowed if it is marked as judgement and the evidence for it is shown.

## Worked example

*Fictional example. Company, figures and people are invented.*

Draft storyline: "Alder should grow through services (title). 1. The installed base is large. 2. Competitors are growing their service business. 3. Service has higher margins than new pumps." Review:

- Major (check 3): All three points could be true and services could still fail for Alder. Missing: evidence that Alder's customers will buy from Alder, at a price that works. Add the willingness-to-pay finding.
- Major (check 7): "Competitors are growing service" does not show that service causes their growth. Remove or reframe as market evidence.
- Major (check 8): No comparison with the alternatives considered (pricing, Poland, doing nothing).
- Blocker (check 1): The title answers "should we grow through services?" but the question was "which two moves should the board fund?" The second move is missing.

## Output template

```markdown
# Logic review: <document>

| # | Severity | Check | Where | The claim | The gap | Fix (missing point / regroup / cut) |
|---|---|---|---|---|---|---|

**Governing thought proven by its key line:** yes / no, because <reason>
```

## Related

- [Partner Review Checklist](partner-review-checklist.md), [Synthesis](synthesis.md), [Storyline and Ghost Deck](storyline.md), [Pyramid Principle](pyramid-principle.md), [MECE](mece.md)
