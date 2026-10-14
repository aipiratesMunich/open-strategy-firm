# ra-03: Resume inside an engagement with messy client data

## Prompt

> Marlow: the till data is in. Do the next research piece.

Input folder: `ra-03-engagement/` (copy it to `engagement/marlow/` in the working directory before the run). No web access needed.

*Fictional company. All figures invented for evaluation.*

## What this case tests

Robustness. The skill must find its branch from the engagement files (H2, workplan row 2) instead of asking for a hypothesis, clean a messy export (duplicate row, a hand-typed value, inconsistent site label, a site refurbished mid-period), and write the result back into the engagement.

## Planted data issues

| # | Issue | Correct handling |
|---|---|---|
| P1 | Site A Q2 appears twice (second row marked "re-export") | Count once: site A = 48,000 visitors, EUR 74,400 |
| P2 | Site B Q1 revenue typed as "EUR 26.4k", label "site b" | Read as EUR 26,400 for site B |
| P3 | Site C was refurbished on 1 April 2026; its Q1 is a before value | Use C Q1 as a before value, C Q2 as after, not both as "refurbished" |

## Reference values

- Revenue per visitor H1 2026: A EUR 1.55 (refurbished all period); B EUR 1.10 (not refurbished, flat in Q1 and Q2); C Q1 EUR 1.25 before, C Q2 about EUR 1.34 after.
- All refurbished observations pooled (A Q1, A Q2, C Q2): EUR 98,450 / 66,000 visitors = about EUR 1.49.
- Target EUR 1.60, kill below EUR 1.35. Site A is above the kill line but below target; site C after refurbishment is just below the kill line.

## Pass criteria

- Must: reads `00-status.md`, `02-hypotheses.md` and `04-workplan.md` before analysing, and names H2 (workplan row 2) as the branch.
- Must not: ask for the hypothesis, kill criterion or problem statement again, or restart the engagement.
- Must: finds and handles P1, P2 and P3 explicitly (each mentioned in the output).
- Must: reports revenue per visitor per site in line with the reference values (rounding to two decimals accepted).
- Must: compares the result with both the EUR 1.60 target and the EUR 1.35 kill criterion and gives the verdict reshaped or open (not confirmed), with weak or medium strength.
- Must: notes that two refurbished sites and one quarter after refurbishment at site C are too few to generalise to 12 centres, and names what would settle it (e.g. more months at site C, café manager interviews, comparable refurbishments elsewhere) without inventing a benchmark.
- Must: notes a possible confounder (e.g. site A may differ from B and C in size, location or season), using site B's flat Q1 to Q2 as the control where relevant.
- Must: writes `engagement/marlow/research/h2-cafe-uplift.md` (or prints it under that heading) in the skill's output format, updates the H2 status in `02-hypotheses.md` and adds a line to `00-status.md`.
- Must: states the so-what for the EUR 4.2m decision (e.g. the all-centres answer is at risk; the business case should run at EUR 1.35 to 1.55, not EUR 1.60).
- Must not: report site A totals including the duplicate row (76,000 visitors or EUR 118,400).
