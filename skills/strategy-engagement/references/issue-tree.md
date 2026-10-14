# Issue Tree

## What it is

A question-driven decomposition: the problem statement at the root, broken into sub-questions, each broken further until every leaf can be answered by one analysis. It makes no claim about the answer. It answers: "What do we need to know to answer this question, and does that list cover it?"

**Issue tree or [Hypothesis Tree](hypothesis-tree.md)?** An issue tree splits the question; a hypothesis tree splits a proposed answer. Use an issue tree when the team has no credible answer yet, when the problem is unfamiliar, or when the client must see that every angle was covered. Switch to a hypothesis tree as soon as a defensible day-one answer exists, because it targets work at what must be true and is faster.

## When to use

- First structuring of an unfamiliar problem, before any hypothesis is credible.
- Scoping and dividing work: each branch becomes a workstream in the [Workplan](workplan.md).
- Diagnostic questions ("why did margin fall?"), where the cause is genuinely unknown.
- Showing a sceptical client that the team considered the full space before narrowing.

## When NOT to use

- **The team already has a defensible answer.** Building a full issue tree then spreads effort over branches that cannot change the answer. Use a [Hypothesis Tree](hypothesis-tree.md).
- **Pure arithmetic problems** (profit, unit cost). A formula tree is cleaner and sums by construction. Use a [Profit Tree](profit-tree.md).
- **Very small questions** answerable with one analysis. A tree adds ceremony. Write the analysis plan directly.
- **As a deliverable to the board.** A tree shows how the team thinks, not what it concluded. Present the answer in a [Pyramid Principle](pyramid-principle.md) structure.

## Step by step

1. **Root.** Input: problem statement ([Problem Definition](problem-definition.md)). Output: one question with a decision, a metric and a time frame.
2. **Choose the first cut.** Output: a single splitting logic for level 1. Prefer cuts that come from the economics (formula, value chain stage, customer, product) over generic lists.
3. **Write level 1 as questions.** Three to five sub-questions that together answer the root. Run the [MECE](mece.md) test.
4. **Decompose each branch** until each leaf is a question one analysis can answer. Usually two to four levels.
5. **Prune.** Mark each leaf by how much its answer could move the decision and how hard it is to answer. Cut or park leaves that cannot move the decision ([Eighty-Twenty](eighty-twenty.md)).
6. **Attach analyses.** For each surviving leaf: the analysis, data source, owner, and due date.
7. **Convert when ready.** When answers start to emerge, rewrite the surviving branches as hypotheses ([Hypothesis-Driven Approach](hypothesis-driven-approach.md)).

## Inputs needed

- Agreed problem statement.
- Basic understanding of how the business makes money.

## Output produced

- A tree of questions, three to five branches per level, each leaf linked to one analysis.
- A pruned list of leaves with priority, data source and owner.

## Common mistakes

- **Leaves that are topics.** "Competition" is not a question. "Will either main competitor match a 48-hour response by 2028?" is.
- **Root that is too broad.** "How can Alder improve?" produces an unprunable tree.
- **First cut from a template.** Using a generic framework as level 1 regardless of the problem. A partner asks why this cut fits this client.
- **No pruning.** Twenty-eight leaves, all "in scope". The team drowns in analysis that cannot change the answer.
- **Staying in the issue tree too long.** Week three and still no hypotheses means the team is collecting facts and hoping.

## Worked example

*Fictional example. Company, figures and people are invented.*

Root: "How can Alder Pumps grow revenue from EUR 180m to EUR 200m by 2030, organically, within EUR 20m capital?"

Level 1 (cut by revenue source): 1. Can the core pump business grow? 2. Can the installed base generate more revenue? 3. Can new markets contribute?

Level 2: 1a. Are prices below what customers would accept? 1b. Can volume grow in existing segments? 2a. How many installed pumps lack a service contract? 2b. What would customers pay for one? 2c. Is spare-part share of wallet falling? 3a. Which adjacent country has an open market? 3b. What could entry deliver by 2030?

Pruning: 1b is parked (three flat years, no sign of change). 3a and 3b are kept but scoped to one country, Poland, as the only candidate within the capital limit. Leaves 1a, 2a, 2b get the first two weeks, because they decide whether the gap can be closed.

## Output template

```markdown
# Issue tree: <root question with decision, metric, time frame>

**First cut:** <splitting logic>

1. <Sub-question>
   1.1 <Leaf question>
   1.2 <Leaf question>
2. <Sub-question>
   2.1 <Leaf question>
3. <Sub-question>
   3.1 <Leaf question>

| Leaf | Can move the decision? | Effort | Analysis | Data source | Owner | Due | Keep / park / cut |
|---|---|---|---|---|---|---|---|
| 1.1 | high/med/low | high/med/low | | | | | |

**MECE check of level 1:** <pass / issues>
```

## Related

- [Hypothesis Tree](hypothesis-tree.md), [MECE](mece.md), [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Problem Definition](problem-definition.md), [Workplan](workplan.md), [Profit Tree](profit-tree.md), [Eighty-Twenty](eighty-twenty.md)
