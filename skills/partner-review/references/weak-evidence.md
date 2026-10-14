# Weak Evidence

## What it catches

Claims that rest on less than they appear to: one source, an unsourced number, the client's own belief repeated back, a survey of the wrong people, a best case presented as a base case. Weak evidence is not always wrong. It is dangerous because the team stops questioning it, and the client's sharpest critic will not.

## When to apply

- Every key claim in a document at gate 3: the governing thought, each key-line statement, and every number on the executive summary.
- Research outputs from interview guide and desk research before they enter the synthesis.

## Checks

1. **Source present.** Does each number have a source, a date, a unit and a scope (region, segment, year)?
2. **Source quality.** Is the source primary (company data, official statistics, audited reports, direct observation) or secondary (press, vendor marketing, blogs)? Key claims need primary support or two independent secondary ones.
3. **Independence.** Do the "several sources" actually trace back to one original figure?
4. **Triangulation.** Is each key claim supported by at least two kinds of evidence, for example data plus interviews, or top-down plus bottom-up? (See [Triangulation](triangulation.md).)
5. **Sample.** For interviews and surveys: who was asked, how many, how were they chosen? Are dissenters and non-customers included?
6. **Stated versus revealed.** Does the claim rest on what people say they would do, or on what they have done and paid?
7. **Circularity.** Is the client's own hypothesis or management estimate being returned to them as a finding?
8. **Outside view.** Is a forecast checked against what comparable companies or projects actually achieved, not only built bottom-up from the plan's own details?
9. **Recency and context.** Is the data current and from a comparable market, or old and from somewhere else?
10. **Counter-evidence.** Has the team looked for and shown the strongest evidence against the claim?
11. **Precision theatre.** Are numbers presented with more precision than the evidence supports (EUR 12.37m from three interviews)?
12. **Scope of a test.** Does a pilot, a single region or period, or a handful of sites carry a company-wide or multi-site conclusion? Rate it medium at best, give a range, and name what would confirm it (second region or site, longer period, matched control) without inventing a benchmark.

## Severity

- **Blocker:** check 1 or 7 on the governing thought or an executive-summary number.
- **Major:** checks 2, 3, 4, 6, 8, 10, 12 on key-line claims.
- **Minor:** checks 5, 9, 11 unless they change the conclusion, then Major.

## False alarms

- Rough estimates are fine when labelled as estimates, with the method shown and a range.
- Client data is acceptable as a source if it is labelled and has been sense-checked against at least one outside reference.
- Not every supporting detail needs triangulation; key claims do.
- A small number of interviews can be enough for a qualitative finding (why customers leave), not for a quantitative one (how many leave).

## Worked example

*Fictional example. Company, figures and people are invented.*

Draft claim: "Service contracts will add EUR 18.7m revenue by 2030." Evidence: management estimate of 60% take-up and EUR 1,000 per pump. Review:

- Blocker (check 7): 60% take-up is the client's own estimate, presented as a finding.
- Major (check 8): No outside view. What take-up rates have comparable industrial service offers reached in their first three years?
- Major (check 6): Price rests on stated willingness to pay; add what customers currently spend on unplanned repairs.
- Minor (check 11): "EUR 18.7m" suggests precision the inputs do not have. Show a range.

Fix: "Service contracts add EUR 8m to 15.6m by 2030 (take-up 25% to 50%; base case 40% based on interview intent and comparable offers), price EUR 1,000 per pump per year, supported by current repair spend of EUR 4,000 to EUR 40,000 per failure."

## Output template

```markdown
# Evidence review: <document>

| # | Severity | Claim | Where | Evidence offered | Weakness (check) | What would make it strong |
|---|---|---|---|---|---|---|

**Claims on the executive summary with primary or triangulated support:** <n> of <m>
```

## Related

- [Partner Review Checklist](partner-review-checklist.md), interview guide, [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Triangulation](triangulation.md), [Sensitivity Analysis](sensitivity-analysis.md)
