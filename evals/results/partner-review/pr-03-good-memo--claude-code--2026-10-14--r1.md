# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings table severities are Major, Major, Minor, Minor, Minor, Minor, Minor — no Blocker listed |
| At most two Major findings, each with a concrete, defensible reason | yes | Exactly two Major findings (#1 decision #2 trade-off unquantified; #2 catering lacks outside-view check), each with a stated consequence and required fix |
| Names what is good and must survive | yes | Section 'What is good and must survive' lists specific recommendation, honest gap disclosure, triangulation, kill criteria, alternatives considered, and tight length |
| Must not demand a named framework, more length, or more slides | yes | All required fixes ask for one added line/clause each; memo's one-page length is praised as a strength ('Tight, one-page length with no padding') |
| Must not flag the stated uncertainty or explicit assumptions as weaknesses | yes | Findings target missing outside-view checks and unstated methodology (e.g., interviewee selection), not the memo's own disclosed uncertainty or assumptions |
| Must not claim numbers do not tie | NO | The memo asserts a 'Numbers that do not tie' section and Finding #4 claiming the EUR 1.1m 3% price increase figure doesn't match 3% x EUR 62m (~EUR 1.86m, a ~0.76m 'unexplained gap'), contradicting the reference that all cited figures (including the 1.1m used in '1.1 + 0.9 = 2.0 < 12.7/4') actually  |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027" memo, gate 3

**Verdict:** Release with fixes
**In one line:** The ask and numbers hold up on inspection, but the board is handed decision #2 (revisit the target or the floor) with no sense of what's on the other side of that trade-off, and catering — the bigger of the two bets — gets no outside-view check that delivery got.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and how do they address the 2031 revenue target and margin floor? (given, stated at top of memo)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; these close EUR 5.3m of a EUR 12.7m gap to the EUR 80m target, so the board must also decide whether to revisit the target or the margin floor.

These match — a rare, genuine strength for a one-pager going out the night before a board meeting.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Decision Maker / Unanswered So-What | "What it adds up to" | Decision #2 asks the board to "revisit the 2031 target or the margin floor" but never quantifies the other side of that trade-off — e.g. what relaxing the 14% floor would actually unlock from suburban stores. | A board member asked to loosen the floor has no basis to judge the upside against the risk; they may defer the decision entirely or anchor on the wrong number. | Add one line: "Relaxing the floor to X% would clear the suburban margin test and could add ~EUR Ym by 2031," even as a rough range. |
| 2 | Major | Skeptical CFO / Weak Evidence (check 14) | "Why catering" | Catering is the larger investment (EUR 1.2m vs. EUR 0.3m) but, unlike delivery (benchmarked against two regional chains at 10–14% growth), has no comparable-company check on the EUR 2.5–3.3m range or the 32% contribution margin. | A sharp board member will ask why one bet got an outside check and the other didn't, and may discount the catering case as internally generated. | Add one outside reference point for catering growth or margin (an industry report, a comparable operator's catering unit economics) or state explicitly that none was found and why that's acceptable here. |
| 3 | Minor | Evidence Auditor (check 5) | "Why catering," ¶1 | The EUR 190 median order value — a direct input to the bottom-up revenue estimate — comes from 12 interviewees with no description of how they were selected or how representative they are of the ~9,000-order base. | Mitigated by top-down convergence on the same range, so unlikely to flip the conclusion, but it's the kind of detail a careful reader probes first. | Add one line on how the 12 were selected (e.g. "stratified across our ten largest accounts"). |
| 4 | Minor | Skeptical CFO (numbers tie) | "What it adds up to" | "A 3% price increase (about EUR 1.1m)" doesn't tie to 3% of the stated EUR 62m base (~EUR 1.86m); no scope is given for why it's smaller. | Doesn't change the gap-to-target conclusion even if corrected, but an unexplained arithmetic mismatch on page one undercuts trust in every other number. | Either state the narrower base the increase applies to, or correct the figure. |
| 5 | Minor | Logician (vertical logic) | "Why catering," ¶1 | The pain point driving the investment ("nine named slow delivery from their current supplier") is never explicitly tied to why a central kitchen fixes it. | Minor — the inference is reasonable and obvious, but currently implicit. | Add a clause: "...a dedicated kitchen cuts fulfillment time from X to Y hours." |
| 6 | Minor | Premortem | "What would change our view" | Kill criteria for the delivery pilot cover order volume and in-store cannibalization only; a platform fee increase could erode the already-thin EUR 3.10/order contribution without tripping either trigger. | Relevant to the later scale decision, not to funding this reversible pilot now — so it doesn't block tomorrow's ask, but should be added before any national rollout decision. | Add a margin/fee floor to the criteria the pilot gets judged against before scaling. |
| 7 | Minor | Logic Gaps (check 5, coverage) | "Why catering" / "What would change our view" | Catering has no stated cannibalization check against in-store counter sales from the same office customers, though the delivery pilot has one. | Low — catering displacement of walk-in sales is plausible but likely small relative to net new office revenue. | Add a one-line check, e.g. tracking in-store transactions at stores near large catering accounts. |

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| 3% price increase revenue | Stated: "about EUR 1.1m" | Implied by 3% × EUR 62m base | ~EUR 0.76m gap, unexplained |

All other headline figures check out: catering contribution-minus-fixed-cost math (0.16/0.32/0.45/0.51m from 1.6/2.1/2.5/2.7m at 32% less EUR 0.35m) ties exactly; EUR 5.3m = 2.9m + 2.4m; 5.3/62 = 8.5%; 80 − 67.3 = 12.7m all tie correctly.

## Missing outside view
- Catering revenue (EUR 2.5–3.3m by 2031) and 32% contribution margin: no comparable catering/food-service launch cited, unlike delivery's two-regional-chain benchmark.
- 3% price increase: no comparable evidence on price elasticity against discount competitors beyond the qualitative mention.

## Premortem
1. Office catering demand is concentrated in a handful of large accounts (or tied to office-attendance trends that could still reverse); the kitchen's fixed costs (EUR 0.35m/year, 4 staff) go underutilized and payback slips past year four. Partly caught by the 40%-framework-agreement test, but that's a six-month signal, not an ongoing concentration safeguard.
2. Delivery platform commission rates rise, compressing the EUR 3.10/order contribution toward zero even if the 60-orders/day volume target is hit — the pilot "passes" on the stated criteria while the unit economics quietly fail.
3. Catering cannibalizes in-store counter sales from the same office workers once the business actively courts their employer — untested, unlike the equivalent check built into the delivery pilot.

## What is good and must survive
- Specific, actionable recommendation: amounts, owners, start dates for both moves, and an explicit no on suburban stores and franchising.
- Honest disclosure of the EUR 12.7m gap to target instead of stretching the base case to paper over it — and framing the target/floor tension as the board's decision rather than quietly answering it themselves.
- Real triangulation: delivery growth checked against two regional chains' actual results; catering's bottom-up and top-down estimates independently converge on the same range.
- Explicit, falsifiable kill criteria for both moves ("what would change our view") — this is good practice that most memos skip entirely.
- Alternatives (suburban stores, franchising, price increase, longer hours) are named, sized, and rejected with sourced reasons rather than ignored.
- Tight, one-page length with no padding.


## Files in work dir after run

- pr-03-input.md
