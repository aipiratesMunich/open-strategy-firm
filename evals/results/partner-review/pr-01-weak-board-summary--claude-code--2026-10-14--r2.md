# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Return. | yes | **Verdict:** Return |
| Must: finds D1, D2 and D3, each rated Blocker. | yes | Finding #1 (Blocker): "'Exploring' and 'considering'... name no budget, owner or date — not an actionable fund/no-fund decision on two named moves"; plus explicit 'Question the draft must answer' / 'Answer the draft gives' noting no move named with amount; Finding #3 (Blocker): "'can add EUR 9m by 2 |
| Must: finds at least two of D4, D5, D6. | yes | Finding #8 (40 loyalty-club members survey), Finding #6/#7 and 'Missing outside view' (35%/year growth with no comparable), Finding #2 (Blocker) on franchising disappearing without explanation — all three found |
| Must: states the question the draft must answer and notes that the draft does not answer it. | yes | "Question the draft must answer: Which two growth moves should the board fund..." followed by "Answer the draft gives: ... This is a request for more study, not a funding decision" |
| Must: gives a concrete fix for every finding (not "consider improving"). | yes | e.g. "Name the two moves to fund, with euro amount, owner and 2027 start date"; "Recompute from the table; state whether the figure is incremental growth or total revenue, and match it to EUR 5.2–6.4m" |
| Must: includes a premortem with three reasons. | yes | Premortem lists three numbered items: online growth undershoot, catering investment gap, suburban stores greenlit by default |
| Must: lists at least one thing that is good and should survive (the store-level margin data is solid). | yes | "The store economics table (margin by format, sourced to the 2025 P&L, 41 stores) is exactly the right granularity — keep it" |
| Must: shows what "fixed" looks like in two to four sentences. | yes | 'What "fixed" looks like' section contains four sentences ending in "Decision requested: approve EUR [X]m..." |
| Must not: invent benchmark figures without a source; it may say which comparison is missing. | yes | "(No web search was run to source these given the dataset is explicitly fictional; the gaps above state what evidence would be needed, not invented benchmarks.)" |
| Must not: rewrite the whole document instead of reviewing it. | yes | Output is structured as findings table, premortem, and a short illustrative close, not a full rewritten executive summary |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries — Growth Strategy 2027-2031 (Executive Summary), gate 3

**Verdict:** Return
**In one line:** The summary never names the two funded moves, hides that its own numbers fall short of the EUR 18m growth target, and recommends a store format (suburban) that fails the board's own 14% margin floor — without flagging any of it.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%? (given, from problem statement)
**Answer the draft gives:** "Explore" corporate catering further and "consider" an accelerated online roadmap; next steps to be defined with management. — This is a request for more study, not a funding decision, and it does not reconcile to the EUR 18m target or the margin constraint.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | Exec summary, recommendation line | "Exploring" and "considering," with "next steps... defined with management," name no budget, owner or date — not an actionable fund/no-fund decision on two named moves | Board cannot approve anything; the document returns to the team by a different route, after the meeting | Name the two moves to fund, with euro amount, owner and 2027 start date |
| 2 | Blocker | Logician | Exec summary | Franchising (in scope) is never mentioned or ruled out; new stores is left as an open "option," neither chosen nor rejected — only catering and online get even a soft nod, and even those aren't committed to | Board approves a plan that silently narrowed its own option set; a board member who reads the problem statement will ask "what about franchising?" and get no answer | State a decision (fund / don't fund) and a one-line reason for all four in-scope options, not just two |
| 3 | Blocker | Skeptical CFO | Exec summary vs. Market overview table | "Corporate catering can add EUR 9m by 2031" does not tie to the table: offices (0.8→4.1) + events (0.4→2.3) = EUR 6.4m total 2031 potential, i.e. EUR 5.2m of incremental growth, not EUR 9m | The headline revenue number for one of the two recommended moves is unsupported by the document's own data; a sharp board member catches this in one subtraction and stops trusting every other number | Recompute from the table; state whether the figure is incremental growth or total revenue, and match it to EUR 5.2–6.4m |
| 4 | Blocker | Decision Maker / Logician | Exec summary | No figure anywhere bridges the recommended moves to the EUR 18m growth target (62→80m) or to the 14% margin floor; catering (EUR 9m, itself wrong) and online ("reach EUR 11m," a total not an increment) are never summed against the target | The board cannot tell whether approving these two moves gets Brightwell to EUR 80m, or leaves a gap — the single most important number in the document is missing | Add an explicit bridge: target +EUR 18m; catering adds X; online adds Y; remaining gap Z and how it closes |
| 5 | Major | Logician (consistency) | Store economics table vs. exec summary | "New stores remain an option in suburban locations" is floated while the same document shows suburban store margin at 13.1% — below the board's own 14% floor — with no flag | Board could greenlight further exploration of a format that already fails its own screening criterion | Either drop suburban new stores from consideration or show explicitly how margin would clear 14% (format change, pricing); connect the table to the decision, not just to the appendix |
| 6 | Major | Evidence Auditor | Market overview, sources | Catering 2031 estimate and online 35%/year growth both trace to management's own estimate/plan, returned to the board as independent findings, with no outside comparable (industry report, peer bakery/catering/delivery benchmark) | A board member asks "based on what, besides our own plan?" and the team has no second source for either headline number | Triangulate each with one outside data point; label management figures as management estimates, not as findings |
| 7 | Major | Skeptical CFO | Exec summary, online delivery | 35%/year compounded over 5 years (2.5m→11.2m) is presented as a single point estimate with no downside case; a few points of growth-rate error swings the target materially | Board approves a plan whose central number has no stated floor; if growth comes in at 20–25%, nobody flagged that this breaks the EUR 80m case | Add a base/downside range for the growth rate and state what each case does against the target |
| 8 | Major | Weak Evidence (sample) | Customer view section | Both survey stats (92% recommend, 61% would order online) come from 40 existing loyalty-club members — a small, self-selected, already-loyal sample, not representative of lapsed or non-customers the growth moves are meant to win | The 61%-online figure is used to support a growth move aimed partly at new/occasional customers, but it only measures people who already shop at Brightwell | Either widen the sample to include lapsed/non-customers or caveat explicitly that the figure describes existing loyalists only |
| 9 | Major | Unanswered So-What | Customer view; store economics table | Neither the 92%-recommend stat nor the store-margin-by-format table is linked to the recommendation by a stated so-what; they read as background facts | Reader cannot tell why these numbers are on the page, or whether they support or undercut the two recommended moves | Tie each number explicitly to the decision ("suburban margin of 13.1% is why we exclude suburban new stores") or move to appendix |
| 10 | Major | Decision Maker | Exec summary (whole) | No cost, investment or margin-impact figure is given for catering or online delivery — only revenue. The problem statement's binding constraint is margin above 14%, which this summary never addresses for either recommended move | Board could fund EUR 80m of revenue that comes with margin below 14%, which is exactly the outcome the problem statement was written to prevent | Add capex/opex and projected margin impact for each recommended move |
| 11 | Minor | Outsider / exec-summary standard | Exec summary, opening | Opens with brand background and "significant potential in several areas" filler before any answer; governing thought is not the first sentence | Costs the reader the first ten seconds; minor on its own but compounds the Blockers above | Lead with the funding recommendation and the euro amount against the EUR 18m target |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 value | "EUR 9m" — Executive summary | EUR 6.4m total (EUR 5.2m incremental) — Market overview table (0.8→4.1 + 0.4→2.3) | EUR 2.6–3.8m overstated, depending on which basis was intended |
| Combined growth vs. target | Catering + online figures in exec summary (as stated) | EUR 18m required growth (62m→80m) in problem statement | Never reconciled anywhere in the document |

## Missing outside view

- **Online delivery growth (35%/year for 5 years):** no comparable regional bakery or QSR delivery program cited. Needed: actual multi-year online/delivery growth achieved by a comparable regional food retailer, to test whether 35%/year compounded is a base case or a best case.
- **Corporate catering penetration/margin:** no comparable catering attach rate or margin for a bakery-scale catering operation. Needed: what share of revenue catering reaches at comparable regional chains, and at what margin, to sense-check the EUR 9m (or corrected EUR 5.2–6.4m) figure.
- **Franchising economics:** not evaluated at all, so there is no benchmark to compare against catering/online — the board cannot judge whether franchising was correctly screened out or just dropped.

*(No web search was run to source these given the dataset is explicitly fictional; the gaps above state what evidence would be needed, not invented benchmarks.)*

## Premortem

1. **Online delivery growth undershoots 35%/year** (third-party platforms compress margin or the 45-minute promise isn't operationally met) — the largest single number in the plan comes in well under forecast, and no downside case was shown to warn the board this was the swing factor.
2. **Catering revenue arrives without the kitchen/staffing investment to support it**, because the summary gives no cost figure — margin on the "growth" revenue turns out to be thin or negative, undermining the 14% floor the board set as a condition.
3. **Suburban new stores get greenlit by default** because the document never explicitly rules them out, dragging store-level margin below 14% even as headline revenue approaches EUR 80m — the board discovers only in year three that revenue growth and margin have decoupled.

## What is good and must survive

- The store economics table (margin by format, sourced to the 2025 P&L, 41 stores) is exactly the right granularity — keep it, but connect it to the new-stores decision explicitly instead of leaving it to stand alone.
- Splitting corporate catering into offices vs. events in the market overview is the right level of segmentation to build a credible bottom-up case — keep the split, fix the arithmetic that rolls up from it.
- Attempting a customer data point (the 45-minute delivery threshold) to ground the online growth assumption is the right instinct — it just needs a representative sample and a direct link to the 35%/year figure, which it doesn't currently support.

## What "fixed" looks like

**Fund [move 1] and [move 2] in the 2027 budget: scale corporate catering (offices + events) to EUR 6.4m by 2031, adding EUR 5.2m of incremental revenue, and invest in online delivery targeting 25–30%/year growth, adding EUR 6.5–8.7m by 2031.** Together these add an estimated EUR 12–14m against the EUR 18m target, leaving a EUR 4–6m gap that [the second funded move / a named lever] must close; new stores are excluded from suburban locations because current suburban margin (13.1%) is below the board's 14% floor. The answer changes if online growth falls below 20%/year or catering requires more than EUR [X]m of kitchen/staffing capex to deliver. **Decision requested:** approve EUR [X]m for catering capacity and EUR [Y]m for delivery logistics, owner [role], start Q1 2027.


## Files in work dir after run

- pr-01-input.md
