# Pyramid Principle

## What it is

A way to order thinking and writing so the reader gets the answer first and the support second. One governing thought sits at the top; below it sit a few key-line points that together prove it; below each sit the facts and analyses that prove that point. It answers: "What is the one thing the reader must take away, and why should they believe it?"

## When to use

- Any document that asks a decision maker to act: executive summary, board memo, steerco deck, recommendation email.
- Testing a synthesis before slides exist. If the pyramid does not stand, the deck will not either ([Synthesis](synthesis.md)).
- Reviewing someone else's draft: rebuild its pyramid from the titles and see where it breaks.

## When NOT to use

- **Early exploration, when there is no answer yet.** Forcing a governing thought on day two produces fake certainty. Use an [Issue Tree](issue-tree.md) to structure the question instead.
- **Workshops and brainstorms.** The goal is to widen options, not to argue one. Use an open agenda or [Issue Tree](issue-tree.md) branches as prompts.
- **Bad news to a hostile audience that has not accepted the problem.** Leading with the conclusion can close the room. Open with [SCQA](scqa.md) so the audience agrees on the complication before seeing the answer; the pyramid then follows.
- **Reference material** (data books, model documentation, appendices). Readers look things up; order by topic, not by argument.

## Step by step

1. **Write the question the reader has.** Input: problem statement ([Problem Definition](problem-definition.md)). Output: one question in the reader's words.
2. **Write the governing thought.** One sentence that answers the question and could stand alone. Output: the top box.
3. **Ask "why?" or "how?" of the governing thought.** The answers become the key line: three to five points. Output: key line.
4. **Choose the logic of the key line.** Either inductive (parallel reasons of the same kind, e.g. three reasons) or deductive (a chain: situation, implication, therefore). Do not mix the two in one group.
5. **Check the group.** The key-line points must together prove the governing thought, with no material overlap and no material gap ([MECE](mece.md)). Each point must be a full sentence with a claim, never a label.
6. **Repeat one level down.** For each key-line point, ask the same question and list the supporting findings with sources.
7. **Test top-down and bottom-up.** Top-down: does each level answer the question raised by the level above? Bottom-up: does each group summarise into exactly the point above it, without adding new claims?
8. **Map to the document.** Governing thought = first paragraph or executive summary. Key line = section headings or [Action Titles](action-titles.md). Support = body and charts.

## Inputs needed

- Problem statement and the decision maker's question.
- Synthesised conclusions with evidence ([Synthesis](synthesis.md)).

## Output produced

- A pyramid in outline form: governing thought, key line, supporting points with sources.
- The skeleton of the document or deck that follows from it.

## Common mistakes

- **Topic labels instead of claims.** "Market", "Competition", "Recommendation" as key-line points. A partner strikes them because they prove nothing.
- **Governing thought that is a summary.** "There are several options for growth" answers no question. It must commit.
- **Mixed logic in one group.** Two reasons and one action in the same group. The reader cannot tell what kind of support they are reading.
- **Support that does not add up.** Three key-line points that are each true but do not together justify the top. This is the most common gap a partner finds ([Logic Gaps](logic-gaps.md)).
- **Too many key-line points.** Seven points means the team has not decided which matter.
- **Pyramid built after the slides.** Retro-fitting a pyramid onto finished slides hides the gaps it was meant to expose.

## Worked example

*Fictional example. Company, figures and people are invented.*

Question from the Alder Pumps board: "How do we grow from EUR 180m to EUR 200m revenue by 2030 without acquisitions and within EUR 20m capital?"

Governing thought: "Launch a service-contract offer on the installed base and raise list prices 4% in 2027; together they add about EUR 19.5m by 2030 within the capital limit, which reaches the target in the base case with almost no cushion, and the board should decide in March 2027 whether to fund a buffer."

Key line (inductive, three reasons):
1. Service contracts are the largest organic lever: 52% of 60,000 installed pumps are older than eight years and uncontracted, and customers would pay about EUR 1,000 per pump per year, so 40% take-up adds about EUR 12.5m (range EUR 8m to 15.6m) for EUR 6m investment.
2. Prices can rise 4% without losing volume: Alder lists 6% below its two main competitors; the increase is worth about EUR 7m.
3. Poland is not worth entering: two local players hold 78%, and entry would add less than EUR 5m by 2030.

Bottom-up check: points 1 and 2 add EUR 19.5m against a gap of EUR 20m. The governing thought states the thin margin instead of hiding it, so the pyramid holds.

## Output template

```markdown
# Pyramid: <reader's question>

**Governing thought:** <one sentence that answers the question>

**Logic of key line:** inductive / deductive

1. **<Key-line claim 1, full sentence>**
   - <Supporting finding> (<source>)
   - <Supporting finding> (<source>)
2. **<Key-line claim 2>**
   - <Supporting finding> (<source>)
3. **<Key-line claim 3>**
   - <Supporting finding> (<source>)

**Checks:**
- [ ] Each level answers the question raised by the level above
- [ ] Key-line points together prove the governing thought (no material gap)
- [ ] No two points make the same claim (no material overlap)
- [ ] Every point is a full-sentence claim, not a label
```

## Related

- [SCQA](scqa.md), [MECE](mece.md), [So-What Test](so-what-test.md), [Synthesis](synthesis.md), [Storyline and Ghost Deck](storyline.md), [Action Titles](action-titles.md), [Executive Summary](executive-summary.md), [Logic Gaps](logic-gaps.md)
