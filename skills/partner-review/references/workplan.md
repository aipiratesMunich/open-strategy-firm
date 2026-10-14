# Workplan

## Purpose

Translate the prioritised hypotheses into concrete analyses with owners, sources, deliverables and dates. It makes the cost of each analysis visible, so the team can cut what does not move the decision. It is also the contract with the client about what will be delivered when.

## Entry criteria

- Agreed problem statement.
- Hypothesis list with ranking and kill criteria ([Hypothesis-Driven Approach](hypothesis-driven-approach.md)).
- Ghost deck draft, so every analysis maps to a page that needs it ([Storyline and Ghost Deck](storyline.md)).

## Step by step

1. **Prune the tree.** Drop branches that cannot change the decision even if the hypothesis turns out false. Note why each was dropped.
2. **One row per analysis.** For each surviving hypothesis, list the analysis that tests it, the end product (a chart, a table, a number), the data source, the owner and the due date.
3. **Link to the ghost deck.** Every analysis names the page it feeds. An analysis without a page is a candidate for deletion; a page without an analysis is a gap.
4. **Estimate effort** in days. Sort by "impact on answer" then by effort. Use the [Eighty-Twenty](eighty-twenty.md) logic: the first few analyses usually carry most of the answer.
5. **Set checkpoints.** Fix dates for partner gates and client check-ins. Put the most decision-relevant analysis before the first client check-in.
6. **Plan data requests early.** Client data often takes the longest. Send requests on day one with a clear format and a fallback if data is missing.
7. **Mark the critical path** and the fallback when a source fails (proxy data, interviews, public benchmarks with flagged assumptions).
8. **Review weekly.** Strike finished rows, add rows only when they test a live hypothesis.

## Inputs needed

- Hypothesis list, ghost deck, available team capacity (or, for an agent, time and tool limits).
- Client data inventory: what exists, who owns it, how long it takes to get.

## Output produced

- Workplan table (template below).
- Data request list sent to the client.

## Exit criteria

- Every row tests a named hypothesis and feeds a named ghost-deck page.
- Every high-impact hypothesis has at least one analysis.
- Owners and dates are filled for every row; data requests are sent.
- Total effort fits the time available, with buffer before the final review.

## Common mistakes

- **Activity lists.** "Research the market" is an activity. "Size the service market for pumps older than eight years in Germany, Austria, Switzerland" is an analysis.
- **No end product.** An analysis without a defined output tends to run until the deadline.
- **Data requests sent late.** The team waits two weeks for a CRM export that could have been requested on day one.
- **Equal weight.** Effort spread evenly across branches instead of concentrated where the decision turns.
- **Plan never updated.** The workplan from week one still drives week four after two hypotheses died.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps workplan, week one. Row 1: "Installed base by age and contract status", tests H1, source: service ERP export plus sales records since 2005, output: one bar chart by age band, owner: analyst, 3 days, feeds ghost page 4. Row 2: "Willingness to pay for service contracts", tests H2, source: 12 plant manager interviews, output: price acceptance table, 6 days, page 5. Row 3: "Polish market share structure", tests H3, source: trade association data and three distributor calls, 2 days, page 7. Dropped: "Global pump market trends", because no finding there would change a decision limited to Central Europe. Data request for the ERP export goes out on day one with a CSV field list.

## Output template

```markdown
# Workplan: <client>, <question in one line>

| # | Analysis (specific) | Tests | End product | Data source (fallback) | Owner | Effort (days) | Due | Ghost page | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | H1 | | | | | | p. | open / done / dropped |

**Dropped branches and why:**
-

**Checkpoints:** partner gate <date>; client check-in <date>; final review <date>

**Data requests sent:** <item, owner at client, date sent, due>
```

## Related

- [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Storyline and Ghost Deck](storyline.md), [Engagement Lifecycle](engagement-lifecycle.md), [Eighty-Twenty](eighty-twenty.md)
