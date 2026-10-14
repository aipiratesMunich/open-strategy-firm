# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1, D2 and D3, each rated Blocker | yes | Q&A section states the funding question is never answered; Finding #1 (Blocker) says '"Exploring" and "considering" are not fundable decisions; no amounts, owners, or dates'; Finding #2 (Blocker) flags the EUR 9m vs EUR 6.4m table mismatch |
| Finds at least two of D4, D5, D6 | yes | Finding #7 (survey of 40 loyalty-club members), Finding #4/'Missing outside view' (no benchmark for 35%/year online growth), Finding #5 (franchising in scope but never mentioned) — all three covered |
| States the question the draft must answer and notes the draft does not answer it | yes | 'Question the draft must answer:' ... 'Answer the draft gives:' "Exploring"... not a funding decision, and not shown to close the EUR 18m gap |
| Gives a concrete fix for every finding | yes | Each row has a 'Required fix', e.g. 'Name the two moves explicitly with EUR budget, owner, and 2027 milestone each' |
| Includes a premortem with three reasons | yes | Premortem section lists three numbered items (online growth, catering plateau, margin drift) |
| Lists at least one thing that is good and should survive, including solid store-level margin data | yes | 'Store economics table is granular, sourced to actual P&L data, and broken out by format — the right level of detail to build a margin case on.' |
| Shows what 'fixed' looks like in two to four sentences | yes | 'What "fixed" looks like' section contains four sentences describing the funded moves, gap bridge, store/franchise decisions, and next step |
| Does not invent benchmark figures without a source | yes | 'Missing outside view' section states 'no comparable bakery/foodservice delivery platform growth rate cited' rather than fabricating one |
| Does not rewrite the whole document instead of reviewing it | yes | Output is a structured critique (findings table, premortem, bracketed template) not a full rewritten executive summary |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries — Growth Strategy 2027-2031, gate 3

**Verdict:** Return
**In one line:** The recommendation doesn't commit to two funded moves, the headline catering number doesn't match its own table, and the board's explicit 14% margin constraint is never addressed.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%? (given)
**Answer the draft gives:** "Exploring" catering further and "considering" an accelerated online roadmap, with new stores left as an open option and franchising never mentioned — not a funding decision, and not shown to close the EUR 18m gap or respect the margin floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | Exec summary, recommendation line | "Exploring" and "considering" are not fundable decisions; no amounts, owners, or dates; the board can't tell what it's being asked to approve | Board can't act — meeting stalls or approves nothing concrete | Name the two moves explicitly with EUR budget, owner, and 2027 milestone each |
| 2 | Blocker | Skeptical CFO | Exec summary vs. Market overview table | Text claims catering "can add EUR 9m by 2031"; the table beneath it sums to EUR 6.4m (0.8→4.1 + 0.4→2.3) | First number a sharp board member checks fails to tie — credibility of every other number collapses | Reconcile the figure with the table; be explicit whether EUR x is the 2031 total or the increment over 2026 |
| 3 | Blocker | Decision Maker / Logician | Whole document | The board's own margin constraint (>14%) is never tested against the recommendation. Store economics shows suburban (13.1%) and kiosk (11.4%) formats already below the floor, and no margin data exists for catering or online at all | Board could approve a plan that violates the constraint it set, without knowing it | Add projected contribution/store-level margin for catering and online under the recommended scenario, and a blended margin path to 2031 |
| 4 | Blocker | Evidence Auditor | Market overview, source notes | Both headline revenue figures (catering, online growth rate) are sourced only to "management estimate" / "management plan" — the client's own numbers returned to the board as independent analysis | No outside check on the two numbers the whole recommendation rests on; first question from a skeptical director exposes this | Triangulate: bottom-up build (accounts × contract value for catering; order volume × basket size for online) plus an outside benchmark for comparable growth rates |
| 5 | Major | Logician | Whole document | Franchising is explicitly in scope per the problem statement but is never mentioned, not even to rule it out | A board member will ask "what about franchising?" and the team has no answer on record | Add one line ruling franchising in or out with a reason |
| 6 | Major | Logician | Exec summary / store economics | New stores ("remain an option in suburban locations") is mentioned but not sized, not resolved, and contradicts the margin data two paragraphs later (suburban = 13.1%, below the 14% floor) | Looks like an unresolved option left dangling, undermining confidence the other two moves were properly screened | Either size the suburban-store option and reconcile with the margin constraint, or state why it was deprioritized |
| 7 | Major | Evidence Auditor | Customer view section | Survey is 40 loyalty-club members only (self-selected, already loyal), yet is used to support the online growth assumption (61% would order online under 45 min) that underpins the 35%/year figure | Stated intent from a biased, tiny sample is standing in for market demand evidence on the second recommended move | Label as directional; supplement with actual order/delivery data or a short pilot before using it to size the online opportunity |
| 8 | Major | Decision Maker | Exec summary, closing line | "Next steps will be defined with management" names no who/what/by when | Document ends without a decision request — exactly what should close it | State concrete next steps, e.g. who builds the business case and by when |
| 9 | Major | Logician | Exec summary (implicit) | Even on the draft's own numbers, catering + online growth (EUR 6.4m + 8.7m net, per the table) falls short of the EUR 18m gap to EUR 80m, and the summary never shows this arithmetic | Board can't see whether the recommended moves actually hit the target, or what closes the residual gap | Add an explicit bridge: EUR 62m → each lever's contribution → EUR 80m, naming what covers the residual |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 revenue | Exec summary: "EUR 9m" | Market overview table: EUR 4.1m + EUR 2.3m = EUR 6.4m | EUR 2.6m (41% overstated vs. table) |

## Missing outside view

- Online delivery growth (35%/year for five years): no comparable bakery/foodservice delivery platform growth rate cited — figure comes only from the client's own plan.
- Corporate catering (EUR 1.2m → EUR 6.4m–9m): no benchmark for what comparable regional bakery/foodservice catering programs have actually achieved from a similar base.

## Premortem

1. The 35%/year online growth assumption proves too optimistic (unsupported by any benchmark, and the <45-minute delivery promise needs infrastructure investment that's nowhere costed) — online falls well short of EUR 11m.
2. Corporate catering plateaus far below the management estimate because the starting base is tiny (EUR 1.2m) and Brightwell has no corporate sales capability — there's no bottom-up build (accounts × contract value) behind the number.
3. Blended store margin drifts below the board's 14% floor as volume shifts toward lower-margin online delivery and suburban-format stores (already at 13.1%) — because the draft never models margin impact of either recommended move, this would only surface after the budget is approved.

## What is good and must survive

- The problem statement itself is precise: a named metric, date, margin constraint, and a closed set of four options — exactly the frame a board decision needs.
- Store economics table is granular, sourced to actual P&L data, and broken out by format — the right level of detail to build a margin case on.
- The online delivery growth rate calculation is internally consistent (EUR 2.5m growing 35%/year for five years does tie to EUR 11.2m) — carry this arithmetic discipline into the rewrite.
- The survey's delivery-threshold question (<45 minutes) is a good diagnostic; it just needs a better sample.

## What "fixed" looks like

"We recommend the board fund two moves in the 2027 budget: a EUR [X]m online delivery build-out targeting sub-45-minute delivery in [N] stores, growing online revenue from EUR 2.5m to EUR [Y]m by 2031; and a EUR [X]m corporate catering sales investment growing catering revenue from EUR 1.2m to EUR [Y]m by 2031. Together these close EUR [Z]m of the EUR 18m gap to EUR 80m, with the balance from [organic high-street growth / other named source]; both are projected to hold blended store-level margin above the board's 14% floor. New stores are not recommended for 2027 because suburban-format margin (13.1%) is already below this floor; franchising is [ruled out / deferred] because [reason]. Finance to complete a full business case for both moves by Q1 2027."

(Bracketed figures are placeholders — the team needs to replace them with triangulated numbers before this goes back to the board.)


## Files in work dir after run

- pr-01-input.md
