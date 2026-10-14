# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is **Return**. | yes | "**Verdict: Return**" |
| Must: finds D1, D2 and D3, each rated Blocker. | yes | Finding #1 (Blocker): '"Explore further" / "considering" / "next steps TBD" is a hedge, not a funding recommendation'; Finding #2 (Blocker): 'Catering "+9m by 2031" vs. table delta of 1.2m→6.4m = 5.2m'; both D1 (no funding decision) and D2 (hedge language, no budget) are covered by #1, D3 by #2. |
| Must: finds at least two of D4, D5, D6. | yes | Finding #6 (D4): '92% and 61% figures both come from 40 loyalty-club members'; Finding #7/Missing outside view (D5): 'no comparable regional food-delivery or bakery growth rate cited'; Finding #5 (D6): 'New stores and franchising — half the in-scope options — get no real evaluation'. All three found |
| Must: states the question the draft must answer and notes that the draft does not answer it. | yes | 'Question the draft must answer: Which two growth moves should the board fund...' / 'Answer the draft gives: ... This is not a funding decision, so it does not match the question.' |
| Must: gives a concrete fix for every finding (not "consider improving"). | yes | e.g. 'State the two moves to fund, 2027 budget ask, and 2031 revenue/margin impact for each'; 'Add margin/contribution-margin estimates for catering and online; flag suburban format as below threshold today'. |
| Must: includes a premortem with three reasons. | yes | Premortem section lists three numbered scenarios (catering overstatement, online growth assumption failure, suburban margin breach). |
| Must: lists at least one thing that is good and should survive (the store-level margin data is solid). | yes | 'The Store economics table is genuinely useful, granular, sourced, and is what exposes the margin problem — keep it front and center' |
| Must: shows what "fixed" looks like in two to four sentences. | yes | 'What "fixed" looks like' section gives a 3-sentence example recommendation. |
| Must not: invent benchmark figures without a source; it may say which comparison is missing. | yes | 'no comparable regional food-delivery or bakery growth rate cited' — flags the missing comparison without inventing a figure. |
| Must not: rewrite the whole document instead of reviewing it. | yes | Response is a structured critique with findings tables and a short illustrative 'what fixed looks like' paragraph, not a full rewrite of the executive summary. |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

## Partner review: pr-01-input.md, gate 3

**Verdict: Return**
**In one line:** It doesn't actually recommend which two moves to fund, and the one number it does commit to (catering +9m) doesn't match its own supporting table.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to go from EUR 62m to EUR 80m by 2031, keeping store margin above 14%? (given)
**Answer the draft gives:** "Explore" catering further and "consider" an accelerated online roadmap — next steps TBD with management. This is not a funding decision, so it does not match the question.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | Exec summary, recommendation line | "Explore further" / "considering" / "next steps TBD" is a hedge, not a funding recommendation | Board gets no fundable decision — the document's entire purpose | State the two moves to fund, 2027 budget ask, and 2031 revenue/margin impact for each |
| 2 | Blocker | Evidence Auditor | Exec summary vs. Market overview table | Catering "+9m by 2031" vs. table delta of 1.2m→6.4m = **5.2m** | Board sizes a catering bet ~70% larger than the data supports | Correct the headline to match the table, or correct the table and reconcile |
| 3 | Blocker | Logician | Exec summary + Store economics table | Suburban stores (13.1%) and kiosks (11.4%) are already below the board's 14% margin floor, yet suburban is floated as an option; catering/online have **no margin figures at all** | Board can fund moves without ever checking against its own hard constraint | Add margin/contribution-margin estimates for catering and online; flag suburban format as below threshold today |
| 4 | Major | Logician | Cross-reference, table vs. target | Even using the table's own numbers, catering (+5.2m) + online (+8.7m) = 13.9m, EUR 4.1m short of the 18m needed | Board believes the plan hits 80m when the arithmetic doesn't support it | Show the gap explicitly and name a third lever (or revise the target) |
| 5 | Major | Decision Maker | Whole doc | New stores and franchising — half the in-scope options — get no real evaluation | Board can't tell if catering/online were chosen on merit or by default | Add a short comparison of why new stores and franchising were deprioritized |
| 6 | Major | Evidence Auditor | Lines 11, 39 | 92% and 61% figures both come from 40 loyalty-club members — a small, self-selected, already-loyal sample — yet drive the 35%/year online growth assumption | Online growth target may be unreachable with no warning given | Broaden sample or caveat as directional; stress-test growth at a lower take-up rate |
| 7 | Major | Outsider | Line 25 | Both 2031 figures trace only to internal "management estimate/plan," no external benchmark | No independent check on whether targets are achievable | Cite a comparable bakery/catering or food-delivery growth benchmark, or flag the gap explicitly |
| 8 | Minor | Skeptical CFO | Whole doc | No investment cost/capex/payback shown for either move | Board can't actually size a budget line from revenue alone | Add 2027 investment ask and payback per option |

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 contribution | "EUR 9m" (exec summary, line 13) | EUR 5.2m delta per table (lines 19–23) | ~3.8m overstated (+73%) |

## Missing outside view
- Online delivery 35%/year growth: no comparable regional food-delivery or bakery growth rate cited.
- Corporate catering ramp: no comparable company's catering build-out cited.

## Premortem
1. The catering target is already overstated by 3.8m before anyone spends a euro; actual results track the table's 5.2m, and the board later asks why the funded number was never achievable.
2. The 35%/year online growth assumption, built on a 40-person loyalty-survey stated preference, doesn't convert to real orders; last-mile costs to meet the 45-minute SLA also erode margin that was never modeled, silently breaching the 14% floor.
3. Suburban store expansion proceeds as "an option" even though it already runs at 13.1% margin, mechanically dragging group margin below the board's mandate — because nobody flagged the conflict.

## What is good and must survive
- The problem statement itself is sharp and well-scoped (specific revenue target, margin constraint, named options, CEO sign-off date).
- The Store economics table is genuinely useful, granular, sourced, and is what exposes the margin problem — keep it front and center rather than burying it below the fold.
- The Market overview table separates catering into offices vs. events with current and 2031 figures and named sources, which is exactly the right structure — the exec summary just needs to be forced to agree with it.

## What "fixed" looks like
"We recommend the board fund two moves in the 2027 budget: corporate catering (EUR [X] investment, growing from EUR 1.2m to EUR 6.4m revenue by 2031 at [Y]% contribution margin) and online delivery (EUR [X] investment, growing from EUR 2.5m to EUR 11.2m at 35%/year, at [Y]% contribution margin). Together these close EUR 13.9m of the EUR 18m revenue gap; closing the remaining EUR 4.1m requires [a named third lever or a revised 2031 target]. We do not recommend suburban new-store expansion in this cycle: at 13.1% store margin it already sits below the board's 14% floor."

---

**Bottom line: not ready.** Fix the three blockers — make an actual funding call, correct the catering number, and address the margin constraint against the draft's own data — before this goes to the board.


## Files in work dir after run

- pr-01-input.md
