# Model Red Flags

## What it catches

Financial models that produce wrong numbers, or right numbers nobody can verify. Field audits of real spreadsheets regularly find errors in most models of any size, and authors rarely catch their own. A model that decides an investment must be checkable by someone who did not build it.

## When to apply

- Every model, business case or numeric table that supports a recommendation, at gate 3.
- A lighter pass (checks 1 to 6) when the model structure is first set up.

## Checks

**Structure**
1. **Inputs separated.** Are all assumptions in one clearly marked place, with no hard-coded numbers inside formulas?
2. **Flow.** Do calculations run in one direction: inputs, then calculations, then outputs? No circular references unless documented and necessary.
3. **One formula per row.** Is each row calculated with the same formula across all periods?
4. **Timeline.** Is there one consistent timeline, with period labels and units on every row?

**Assumptions**
5. **Documented.** Does each assumption have a source or a reason, a date and an owner?
6. **Base case realism.** Are growth, take-up, margin and timing assumptions compared with what comparable companies or projects achieved? Is the base case a likely case, not a hoped-for case?
7. **Drivers, not plugs.** Are key outputs built from drivers (volume × price, customers × churn) rather than typed in as targets?

**Integrity**
8. **Checks built in.** Are there check cells: balance sheet balances, totals add up, segments sum to total, cash ties?
9. **Units and signs.** Are units (thousands, millions), currencies and sign conventions consistent?
10. **Hidden content.** Are there hidden rows, sheets or links to external files that change results?
11. **Spot test.** Recalculate two or three key outputs by hand or independently. Do they match?

**Use**
12. **Sensitivity.** Are the three to five most uncertain drivers tested with ranges, and is the break-even value of each shown? (See [Sensitivity Analysis](sensitivity-analysis.md).)
13. **Scenarios.** Are downside and upside cases defined by coherent combinations of assumptions, not by adding 10% to everything?
14. **Outputs tie to the story.** Do the numbers in the deck and executive summary match the model's current version?

## Severity

- **Blocker:** checks 11 (mismatch on a key output), 14, and 1 when hard-coded numbers drive a key output.
- **Major:** checks 2, 3, 5, 6, 7, 8, 12, 13.
- **Minor:** checks 4, 9, 10 unless they change a key output, then Blocker.

## False alarms

- A small one-sheet model can combine inputs and calculations on one sheet if inputs are visibly marked.
- Not every assumption needs external evidence; low-impact ones can be marked as judgement.
- A circular reference for interest on average cash can be acceptable when documented and switchable.

## Worked example

*Fictional example. Company, figures and people are invented.*

Service business case for Alder Pumps. Findings:

- Blocker (check 1): Revenue row for 2028 contains "=B12*0.6*1000", with take-up 60% and price EUR 1,000 typed into the formula.
- Major (check 6): 60% take-up in year two has no outside reference; interviews and comparable offers support a base case of about 40% by 2030.
- Major (check 12): No sensitivity. Break-even take-up for the EUR 6m investment is not shown.
- Blocker (check 14): Executive summary shows EUR 18.0m service revenue in 2030; the current model version shows EUR 18.7m.
- Minor (check 9): Costs are in EUR thousands on one sheet and EUR on another.

Verdict: Return. Move take-up and price to the input sheet, set base case to 40% with a 25% to 50% range, add break-even take-up, re-tie the executive summary.

## Output template

```markdown
# Model review: <model file>, version <v>, <date>

| # | Severity | Check | Sheet / cell / row | Problem | Fix |
|---|---|---|---|---|---|

**Key outputs recomputed independently:** <output: model value vs. check value>
**Most sensitive drivers and break-even values:**
**Verdict:** Return / Release with fixes / Release
```

## Related

- [Partner Review Checklist](partner-review-checklist.md), [Excel Model Standards](excel-model-standards.md), [Sensitivity Analysis](sensitivity-analysis.md), [Business Case](business-case.md), [Weak Evidence](weak-evidence.md)
