# Hypothesis Tree

## What it is

An answer-driven decomposition: a proposed answer at the root, broken into the claims that must all be true for it to hold, each broken further until every leaf is a testable statement with a threshold. It answers: "What would have to be true for our answer to be right, and which of those claims is weakest?"

**Hypothesis tree or [Issue Tree](issue-tree.md)?** The issue tree asks "what do we need to know?" and covers the question space. The hypothesis tree asks "what must be true?" and covers only the logic of one answer. Use the hypothesis tree once the team can state a defensible answer: it cuts the work to the analyses that can kill that answer. Fall back to an issue tree when the problem is new to the team, when the root hypothesis is a guess with nothing behind it, or when the client needs to see the full option space.

## When to use

- After a day-one answer exists ([Hypothesis-Driven Approach](hypothesis-driven-approach.md)).
- Short projects where time allows testing only what matters.
- Familiar case types where the likely answers are known (growth strategy, pricing).
- Turning a client's preferred answer into a fair test of it.

## When NOT to use

- **No credible starting answer.** A hypothesis picked at random anchors the team on it. Use an [Issue Tree](issue-tree.md) first.
- **Diagnostic problems with many possible causes.** Committing to one cause too early hides the others. Use an issue tree on causes, then a hypothesis tree on the leading one.
- **Political settings where the answer must look open.** If stakeholders will reject a pre-formed answer, run the hypothesis tree inside the team and show the issue tree outside.
- **When nobody will write kill criteria.** Without them the tree becomes a list of things to confirm. Fix that first or use an issue tree.

## Step by step

1. **Root hypothesis.** Input: problem statement, day-one answer. Output: one sentence that answers the question and could be wrong.
2. **Ask "what must be true?"** Output: three to five supporting claims. Together they must be sufficient: if all hold, the root holds. Run the [MECE](mece.md) test on the logic, not on topics.
3. **Decompose to testable leaves.** Each leaf gets a number and a threshold: "at least 40% of the installed base is uncontracted and older than eight years".
4. **Write the kill criterion** for each leaf before seeing data: "we drop this if ...".
5. **Rank leaves** by impact on the root and current uncertainty. Test the high-impact, high-uncertainty leaves first.
6. **Attach the cheapest decisive test** to each ranked leaf: analysis, data source, owner.
7. **Update the tree after each result.** A dead leaf either kills its parent or forces a reshaped parent. Rewrite the root when needed and log why.

## Inputs needed

- Problem statement and a day-one answer with some basis.
- Enough knowledge of the business to set credible thresholds.

## Output produced

- A tree from root hypothesis to testable leaves, each with threshold, kill criterion, test and status.
- A change log of how the root moved.

## Common mistakes

- **Supporting claims that are not sufficient.** All leaves confirmed, root still not proven, because a necessary condition (capital, capability, timing) was never on the tree. A partner asks "what else would have to be true?"
- **Leaves without thresholds.** "Customers value service" cannot be killed, so it is always confirmed.
- **Kill criteria written after the data.** That is confirmation bias with paperwork.
- **Defending the root.** Leaves die, the root stays unchanged. The tree is a test, not a defence.
- **Tree as a hidden issue tree.** Leaves phrased as questions with no proposed answer. Pick one.

## Worked example

*Fictional example. Company, figures and people are invented.*

Root: "Alder Pumps can add at least EUR 19m revenue by 2030 through service contracts and a price increase, within EUR 20m capital."

- H1. Service contracts add at least EUR 12m by 2030.
  - H1a. At least 40% of the 60,000 installed pumps are older than eight years and uncontracted. Kill below 25%. Result: 52%, confirmed.
  - H1b. Customers pay at least EUR 900 per pump per year. Kill if fewer than half of plant managers accept EUR 700. Result: about EUR 1,000, confirmed.
  - H1c. Take-up reaches at least 39% by 2030 (31,200 uncontracted pumps x 39% x EUR 1,000 = EUR 12.2m). Kill if comparable offers stay below 30% after three years. Result: base case 40%, range 25% to 50%; open, highest uncertainty.
- H2. A 4% list-price increase adds about EUR 7m without volume loss. Kill if competitors are not above Alder. Result: Alder is 6% below both main competitors, confirmed.
- H3. Both levers fit the capital limit. Result: service offer needs EUR 6m, price change needs none; confirmed.

Sufficiency check: the first draft set H1 at EUR 10m. With every leaf confirmed, H1 plus H2 gave EUR 17m and the EUR 19m root was still unproven. Raising H1 to EUR 12m closed the logic and exposed H1c as the leaf that decides the answer: at the base case of 40%, service adds EUR 12.5m and the total is EUR 19.5m.

## Output template

```markdown
# Hypothesis tree: <root hypothesis, one falsifiable sentence>

**Sufficiency check:** if all supporting claims hold, does the root hold? <yes / missing: ...>

| ID | Claim (with threshold) | Parent | Kill criterion | Test / data | Impact | Uncertainty | Status |
|---|---|---|---|---|---|---|---|
| H1 | | root | | | high/med/low | high/med/low | open / confirmed / killed / reshaped |
| H1a | | H1 | | | | | |

**Decisive leaf:** <ID and why>

**Change log:**
- <date>: <leaf result> → <change to parent or root>
```

## Related

- [Issue Tree](issue-tree.md), [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [MECE](mece.md), [Problem Definition](problem-definition.md), [Weak Evidence](weak-evidence.md), [Logic Gaps](logic-gaps.md)
