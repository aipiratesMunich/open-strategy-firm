# cg-02: "Our core is healthy" and an adjacency that carries the plan

## Prompt

> The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029?

Input file: `cg-02-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The trap: management reads 4% growth as a healthy core while the market grew 9% a year, so the core is losing share. The plan closes the gap with an unproven franchise ramp from zero to 110 cafés in three years. The skill must separate market growth from share change, size the core before the adjacency, and refuse to accept a plan that closes the gap only on a stretched adjacency.

## Reference values

- Corvina CAGR 2023-2025: about 4.1%. Market: EUR 600m in 2023, about EUR 712.9m in 2025 (9% a year).
- Corvina share: 8.0% in 2023, about 7.3% in 2025. On the 4% plan it falls to about 6.0% by 2029.
- Core at 4% a year: 52 x 1.04^4 = about EUR 60.8m in 2029. Gap to 75: about EUR 14.2m.
- Core holding its 2025 share (growing with the market at 9%): 52 x 1.09^4 = about EUR 73.4m in 2029, about EUR 12.6m more than the plan's core. Remaining gap would be about EUR 1.6m.
- The franchise line is 14.0 of the 14.2 gap (about 99%) and starts from zero signed operators.

## Pass criteria

- Must: computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states that 4% growth in a 9% market is share loss, not a healthy core.
- Must: sizes what holding share would be worth (about EUR 73m in 2029, or about EUR 12 to 13m above the plan's core) and makes the cause of share loss the first question to answer.
- Must: shows the franchise carries almost the whole gap and treats the 0 to 110 cafés ramp as unproven: widens the range, compares with comparable franchise launches or names that comparison as missing, and notes no operator is signed.
- Must: flags that the 9% market growth comes from a trade association figure quoted second-hand and should be checked at the source.
- Must: concludes the plan as drafted is not the right plan (or not yet), and gives a reordered answer: fix the core share loss first, franchise as an option or later lever with a proof point.
- Must: shows profit next to revenue or flags that the plan lacks it, and checks the 8% EBIT floor or names it as unknown.
- Must: shows the remaining gap openly under its own levers.
- Must not: accept "our core is healthy" or the EUR 14m franchise figure at face value.
- Must not: invent reasons for the share loss (competitor names, price levels, customer quotes) as facts; it may list them as hypotheses to test.
