# MECE

## What it is

A quality test for any list that breaks a whole into parts: the parts should be mutually exclusive (no item counted twice) and collectively exhaustive (nothing material left out). It answers: "If we work through these parts, will we cover the whole problem exactly once?" Perfect MECE is rare outside arithmetic. The working standard is no material overlap and no material gap.

## When to use

- Every branch of an [Issue Tree](issue-tree.md) or [Hypothesis Tree](hypothesis-tree.md).
- Key-line points of a [Pyramid Principle](pyramid-principle.md) and the conclusions of a [Synthesis](synthesis.md).
- Segmentations, cost breakdowns, option lists, workplan streams ([Workplan](workplan.md)).
- Reviewing any list a client or teammate presents as complete.

## When NOT to use

- **Lists of examples or illustrations.** Three customer quotes do not need to be exhaustive. Label them as examples instead.
- **Prioritised shortlists.** After the [Eighty-Twenty](eighty-twenty.md) cut, the remaining list is deliberately incomplete. State what was dropped and why instead of forcing coverage.
- **Creative option generation.** Overlapping ideas are fine while generating; apply MECE when you consolidate.
- **Messy real-world categories** (customer needs, causes of churn). Forcing strict exclusivity produces artificial boundaries. Allow overlap, then quantify it, or use a frame with a clean split ([Profit Tree](profit-tree.md), value chain stages).

## Step by step

1. **Name the whole.** Input: the list and what it claims to break down. Output: one sentence defining the whole, with its unit and scope ("2025 revenue, EUR, all regions").
2. **Name the cutting rule.** Output: the single dimension the list splits on (by product, by customer, by stage, by formula). Mixed rules are the main source of overlap.
3. **Run the overlap test.** For each pair of items ask: can one real case (a customer, a euro, an action) sit in both? Output: list of overlaps found.
4. **Run the coverage test.** Ask: is there a real case that fits none of the items? Add an explicit "other" bucket if needed and size it.
5. **Run the sum test where numbers exist.** Do the parts add up to the whole within a small residual? A residual above roughly 5 to 10% of the whole signals a gap or double count. Output: whole, sum of parts, residual.
6. **Judge materiality.** Overlaps or gaps that cannot change the answer are noted and left. Material ones get fixed.
7. **Fix.** Use one cutting rule, move overlapping cases to one bucket by an explicit rule, split vague items, or add the missing branch.

## Inputs needed

- The list to test and the whole it claims to cover.
- Numbers for the parts and the whole, if available.

## Output produced

- A tested list with its cutting rule, overlap and coverage findings, and sum check.
- A short note on any accepted, immaterial overlap or gap.

## Common mistakes

- **Mixed cutting rules.** "Germany, Austria, OEM customers, spare parts" splits by region, customer type and product at once. Overlap is guaranteed.
- **"Other" as a hiding place.** A residual bucket holding 30% of the whole is a gap with a label.
- **Claiming MECE without testing.** Writing "MECE" on a slide is not a test. A partner will pick one real case and ask which bucket it goes in.
- **Over-splitting.** Twelve perfectly exclusive branches nobody can work with. Three to five per level is usually enough.
- **Pedantry over immaterial overlap.** Spending a day separating two buckets that share 1% of revenue.

## Worked example

*Fictional example. Company, figures and people are invented.*

A draft list of Alder Pumps growth levers: (a) new pump sales, (b) price increase, (c) service contracts, (d) aftermarket, (e) Germany.

- Cutting rule: mixed. (a), (c), (d) split by revenue line; (b) by driver; (e) by region.
- Overlap test: a service contract in Germany sits in (c), (d) and (e). A price rise on spare parts sits in (b) and (d).
- Coverage test: export markets outside Germany fit nowhere except, partly, (a).
- Fix: one rule, revenue line, then drivers below. Level 1: new pumps, spare parts, service. Level 2 under each: volume, price.
- Sum test on 2025 revenue: new pumps EUR 135m + spare parts EUR 30m + service EUR 15m = EUR 180m. Residual zero.

## Output template

```markdown
# MECE check: <list name>

**Whole:** <what is being broken down, unit, scope>
**Cutting rule:** <single dimension>

| Item | Overlaps with | Example case in both | Material? |
|---|---|---|---|

**Coverage gaps:** <real case that fits no item> (size: <value>)

**Sum test:** whole <value> | sum of parts <value> | residual <value> (<%>)

**Verdict:** MECE / acceptable (immaterial overlap or gap noted) / fix needed
**Fixed list:**
1.
```

## Related

- [Issue Tree](issue-tree.md), [Hypothesis Tree](hypothesis-tree.md), [Pyramid Principle](pyramid-principle.md), [Profit Tree](profit-tree.md), [Logic Gaps](logic-gaps.md), [Synthesis](synthesis.md)
