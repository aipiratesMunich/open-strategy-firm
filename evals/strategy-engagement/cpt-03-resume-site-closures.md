# cpt-03: Resume inside an engagement, site data with an allocation trap

## Prompt

> Continue the Fenmoor turnaround. Site numbers are in.

Input folder: `cpt-03-engagement/` (copy it to `engagement/fenmoor/` in the working directory before the run).

*Fictional company. All figures invented for evaluation.*

## What this case tests

Robustness. The skill must pick up from the engagement files (next open branch H3, workplan row 3), not restart, read a messy export (a value in the wrong unit, a total row) and break the average down correctly. Reported site EBIT includes allocated overhead, so one of management's two "loss-making" sites is roughly break-even before allocation and closing it would not lift group profit.

## Planted data issues

| # | Issue | Correct handling |
|---|---|---|
| P1 | Harbour EBIT entered as -330 (EUR k) while all other values are EUR m | Read as EUR -0.33m |
| P2 | TOTAL row inside the data | Exclude from site analysis; use to check the sum |
| P3 | Site EBIT is after overhead allocated at 6% of revenue | Compute contribution before allocation per site |

## Reference values

- Site margins after allocation: North 9.0%, East 8.0%, Central 7.0%, Harbour -6.0%, Mill Lane 2.0%, Westgate about -17.7%. Group 1.05 / 35.0 = 3.0%.
- Allocated overhead: 6% x 35.0 = EUR 2.1m in total.
- Contribution before allocation: North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35.
- Closing Westgate removes about EUR 0.35m of direct loss; closing Harbour removes about zero, and its EUR 0.33m of allocated overhead would fall on the other sites unless the overhead itself is cut.
- Group margin excluding both sites on reported figures (7.2%) is misleading for the same reason.

## Pass criteria

- Must: reads `00-status.md`, `02-hypotheses.md`, `04-workplan.md` and the existing bridge before analysing, and names H3 as the branch.
- Must not: re-ask the problem statement, redo the liquidity check or rebuild the bridge from scratch.
- Must: handles the three planted data issues explicitly: reads Harbour's -330 as EUR -0.33m (unit error), excludes the TOTAL row from the site analysis and uses it to check the sum, and computes contribution before the 6% overhead allocation.
- Must: is internally consistent: no figure in the text contradicts the same figure in its own tables.
- Must: reports contribution before allocation per site in line with the reference values and identifies Westgate as the only site with a negative direct contribution.
- Must: states that closing Harbour would not raise group EBIT unless the overhead it carries is removed, and says this on the first line or in the H3 verdict.
- Must: marks H3 confirmed, killed or reshaped (expected: reshaped: one site, Westgate, is a true loss maker; the decline is mostly the group-wide cost issue already in H2).
- Must: links back to management's preferred cure and says what it means for the answer (e.g. fix or exit Westgate; do not close Harbour on reported EBIT; overhead review moves up as H4).
- Must: writes `engagement/fenmoor/research/h3-site-profitability.md` (or prints it under that heading), updates `02-hypotheses.md` and adds a line to `00-status.md`.
- Must not: recommend closing both sites on reported EBIT.
