# pr-04: Solid deck whose numbers do not foot across slides

Regression case from community feedback (2026-10-15): a deck with numbers that did not tie across slides got "consider reconciling" and a Release verdict.

## Prompt

> CFO angle please: is this board deck ready to go out to the Harrow board on Friday?

Input file: `pr-04-input.md`

## Planted defects

The deck is otherwise well built (answer first, options compared, sources, downside case), so a lenient reviewer is tempted to release it.

| # | Defect | Expected severity |
|---|---|---|
| D1 | Annual transport saving is EUR 1.1m on slide 5 and EUR 1.3m in the slide 7 table; slide 7 title says EUR 3.4m a year while its own table sums to EUR 3.6m. Payback and NPV on slides 1, 8 and 9 cannot be traced to one savings figure. The headline capex (EUR 14.0m) ties, so the mismatch is easy to wave through as a detail | Blocker |
| D2 | Slide 7 counts the full EUR 2.3m 2025 overtime as saved, although Kassel still runs at high utilisation after Leipzig opens and the slide does not show remaining overtime | Major |
| D3 | Slide 7 nets Leipzig operating cost into "transport" without showing it, so the EUR 1.1m transport saving on slide 5 and slide 7 cannot both be gross and net | Major |

## Pass criteria

- Must: verdict is **Return**.
- Must: finds D1 and rates it Blocker.
- Must: the fix for D1 is an instruction, not a suggestion (for example "Reconcile the transport saving to one figure and rerun payback and NPV"); wording like "consider reconciling" fails this criterion.
- Must: the "Numbers that do not tie" table lists the transport saving or the slide 7 total with both locations.
- Must: finds at least one of D2, D3.
- Must: premortem has three reasons and at least one of them is internal to the client or the team (owner or sponsor, incentives, capacity or skills to execute, organisation structure, internal politics), not only market or external risks.
- Must: lists at least one thing that is good and should survive (options comparison, sourced capex quotes or the downside case).
- Must not: release the deck (Release or Release with fixes) while any number does not tie.
- Must not: invent benchmark figures without a source.
