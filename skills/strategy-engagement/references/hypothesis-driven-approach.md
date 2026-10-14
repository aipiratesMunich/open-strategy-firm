# Hypothesis-Driven Approach

## Purpose

Start with a best-guess answer and spend the project proving or killing it, instead of collecting facts and hoping an answer emerges. It focuses effort on the few analyses that can change the answer. Its known risk is confirmation bias, so the approach only works with explicit kill criteria.

## Entry criteria

- An agreed problem statement ([Problem Definition](problem-definition.md)).
- Enough context to make an informed guess: the briefing, a short look at the business, or a first conversation with the client.

## Step by step

1. **Write a day-one answer.** One sentence that would answer the problem statement if the project ended today. It is allowed to be wrong; it is not allowed to be vague.
2. **Break it into supporting hypotheses** using an [Issue Tree](issue-tree.md) or [Hypothesis Tree](hypothesis-tree.md). Each hypothesis is a claim that must be true for the answer to hold. Keep the branches [MECE](mece.md).
3. **Make every hypothesis testable.** Rewrite each as a statement with a threshold: "Service contracts can add at least EUR 20m revenue by 2030", not "Service is attractive".
4. **Define kill criteria before looking at data.** For each hypothesis write: "We drop this if we find ...". This is the main guard against confirmation bias.
5. **Name the analysis that tests it** and the cheapest data that would do. Prefer an analysis that can be done in days over one that takes weeks, if both could kill the hypothesis.
6. **Rank hypotheses** by (a) how much the answer depends on them and (b) how uncertain they are. Test the high-impact, high-uncertainty ones first.
7. **Test, then update.** After each result, mark the hypothesis confirmed, killed or reshaped. Rewrite the day-one answer when a key hypothesis dies. Record what changed and why.
8. **Seek the disconfirming case.** For every confirmed hypothesis, look once for the strongest evidence against it ([Triangulation](triangulation.md)).

## Inputs needed

- Problem statement.
- Initial context: client documents, a first interview, public information.

## Output produced

- Day-one answer and its revision history.
- Hypothesis list with test, data source, kill criterion, status.

## Exit criteria

- Every hypothesis is testable, has a kill criterion and maps to one analysis.
- The top-ranked hypotheses have been tested with data, not opinion.
- The current answer is consistent with every surviving hypothesis.

## Common mistakes

- **Hypothesis as a topic.** "Pricing" is not a hypothesis. "We can raise list prices 4% without losing more than 2% volume" is.
- **No kill criteria.** Without them, every result gets read as support.
- **Falling in love with day one.** Defending the first answer after the data turned. Partners respect a killed hypothesis; they punish a defended dead one.
- **Testing the easy ones first.** Low-impact hypotheses get tested because data is at hand, while the one that decides the case waits.
- **Asking the client to confirm.** A manager agreeing with a hypothesis is an opinion, not a test.

## Worked example

*Fictional example. Company, figures and people are invented.*

Day-one answer for Alder Pumps: "Grow through service contracts on the installed base and entry into Poland." Hypotheses: H1 "At least 40% of the installed base of roughly 60,000 pumps is older than eight years and not under a service contract." H2 "Customers will pay at least EUR 900 per pump per year for a contract." H3 "Poland can deliver at least EUR 15m revenue by 2030." Kill criteria: H1 dies below 25%, H2 dies if fewer than half of interviewed plant managers accept EUR 700, H3 dies if the two leading local competitors hold more than 70% share. Installed-base data confirms H1 at 52%. Interviews put willingness to pay around EUR 1,000, confirming H2. Market data shows local competitors at 78%, killing H3. The answer is rewritten: "Service contracts plus a pricing reset; no Poland entry before 2029."

## Output template

```markdown
# Hypotheses: <problem statement in one line>

**Current answer (v<n>, <date>):**

| # | Hypothesis (testable, with threshold) | Impact on answer | Uncertainty | Test / analysis | Data source | Kill criterion | Status |
|---|---|---|---|---|---|---|---|
| H1 | | high/med/low | high/med/low | | | We drop this if ... | open / confirmed / killed / reshaped |

**Change log:**
- v1 → v2: <what changed, which result caused it>
```

## Related

- [Problem Definition](problem-definition.md), [Workplan](workplan.md), [Issue Tree](issue-tree.md), [Hypothesis Tree](hypothesis-tree.md), [Weak Evidence](weak-evidence.md), [Logic Gaps](logic-gaps.md)
