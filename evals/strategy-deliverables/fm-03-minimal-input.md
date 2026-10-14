# fm-03: Minimal, messy input without an engagement folder

## Prompt

> quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

*Fictional company. All figures invented for evaluation.*

## What this case tests

Robustness. No engagement folder, no file, missing drivers (staff cost, opening days, horizon, discount rate, ramp), an unsourced volume guess as the key driver. The skill should either ask its three questions in one message and then proceed, or proceed directly with flagged assumptions. It must still produce a usable answer: unit economics, break-even volume and which driver decides.

## Reference values

- Contribution per order: 24 x (1 - 0.30 - 0.28) = EUR 10.08.
- With an illustrative staff cost of EUR 42k per person (3 x 42k = EUR 126k) and 360 trading days: fixed cost EUR 216k a year; break-even about 59.5 orders a day; at 120 orders a day about EUR 435k contribution and EUR 219k a year before fit-out, simple payback on EUR 350k about 1.6 years.
- The run may use a different staff cost or day count; the check is that the arithmetic is consistent with whatever it states: break-even orders per day = (rent + staff cost) / (10.08 x trading days).

## Pass criteria

- Must: if it asks questions, asks them in one message (decision and threshold, missing drivers, horizon and discount rate) and continues with flagged assumptions rather than stalling.
- Must: states contribution per order: EUR 10.08 (42% of basket) from the given inputs, or a lower figure consistent with any extra variable cost it adds and flags as assumption.
- Must: labels staff cost, trading days, discount rate, ramp and horizon as `ASSUMPTION` with a reason and a range.
- Must: labels "maybe 120 orders a day" as an unsourced estimate and makes it the first driver tested.
- Must: gives break-even orders per day with the formula shown and consistent with its stated fixed cost (about 60 with the illustrative figures above).
- Must: gives the answer as a range or scenarios (e.g. 60, 90, 120 orders a day) with a clear decision rule, and names the comparison that would settle volume (e.g. Brightwell's own delivery orders from nearby stores, a platform test).
- Must: notes cannibalisation of existing store delivery orders as a driver to include or flag.
- Must: leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three drivers beyond those given and the named missing ones, each flagged.
- Must not: invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts.
- Must not: give a single-point NPV with no range.
