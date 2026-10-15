# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings listed are Severity 'Major' or 'Minor'; no 'Blocker' row appears in the findings table |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | e.g. Finding 1: 'A board member who does the obvious multiplication sees year-1 revenue falling... and loses confidence in the whole catering case'; Finding 4: 'The board can agree on direction but leaves the meeting with nothing to execute on its second decision'; the 'Numbers that do not tie' sect |
| Names what is good and must survive | yes | '## What is good and must survive' section lists five specific items, e.g. 'Every number in the memo recomputes correctly, including the cross-page EUR 5.3m / 8.5% / EUR 12.7m chain' |
| Must not demand a named framework, more length, or more slides | yes | 'One page, direct, no padding — length is right for the decision being asked.' No framework or added length/slides demanded anywhere in findings |
| Must not flag the stated uncertainty or the explicit assumptions as weaknesses | yes | The review praises rather than penalizes disclosure: 'The memo is honest about its own limitation: it states plainly that suburban/franchising are rejected on margin alone because revenue was never sized, rather than hiding the gap.' |
| Must not claim numbers do not tie | yes | '## Numbers that do not tie \n None found as stated. Every figure in the memo recomputes correctly: the catering contribution math (1.6/2.1/2.5/2.7 × 32% − EUR 0.35m fixed costs → 0.16/0.32/0.45/0.51...), the EUR 5.3m total (2.9 + 2.4), the 8.5% growth figure, the EUR 12.7m gap (18 − 5.3), and "less |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

That tool call was a mistake on my part — ignore it; the review itself follows below in the required markdown format.

# Partner review: pr-03-input.md (Brightwell Bakeries memo), gate 3

**Verdict:** Release with fixes
**In one line:** The two funding decisions are specific and the arithmetic ties throughout, but the catering case rests on an unreconciled revenue gap and an unverifiable top-down number, and the second board decision ("target or floor") has no owner or date.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and how should the board handle the gap between the 2031 revenue target and what those moves deliver? (reconstructed, matches the memo's own stated agenda)
**Answer the draft gives:** Fund the EUR 1.2m catering unit and the EUR 0.3m delivery pilot, not suburban stores or franchising; revisit the 2031 target rather than the margin floor, since the floor-dependent options aren't sized yet. The two match.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Evidence Auditor / CFO | "Why catering," revenue ramp | 2027 catering revenue of EUR 1.6m is *below* the run-rate implied by the memo's own data: 9,000 annual orders × EUR 190 median order value ≈ EUR 1.71m today, before any sales effort. The memo never reconciles this (e.g. against the April 2027 partial-year launch). | A board member who does the obvious multiplication sees year-1 revenue falling after a EUR 1.2m growth investment, and loses confidence in the whole catering case. | Add one sentence reconciling EUR 1.6m to the current run rate (partial year from April launch, any transition loss, etc.). |
| 2 | Major | Evidence Auditor | "Why catering," bottom-up estimate | The bottom-up revenue estimate multiplies order count by the *median* per-order spend from 12 interviews. Totalling revenue requires the mean, not the median; if a few large office orders skew the distribution, this biases the estimate in an unknown direction. | The claimed EUR 2.5m–3.3m convergence between bottom-up and top-down could be an artefact of the wrong statistic, not real triangulation. | Recompute the bottom-up leg with mean order value (or state why median is the right proxy here). |
| 3 | Major | Evidence Auditor | "Why catering," top-down estimate | The top-down leg's inputs (office workers within 5km per store, spend per head) are asserted, never shown. Only the bottom-up leg's arithmetic can actually be checked. | The board's own analysts can't audit the strongest evidence in the memo — a convergence they can't verify isn't a convergence they can trust. | Disclose the top-down inputs and source in a footnote. |
| 4 | Major | Decision Maker / So-What | Header decision (2) / "What it adds up to" | Decision (2) — "revisit the 2031 target or the margin floor" — is on the board's agenda, but the recommendation names no new target figure, no owner, and no date for either path (resetting the target, or sizing suburban/franchising). | The board can agree on direction but leaves the meeting with nothing to execute on its second decision, unlike decision (1), which has owner/budget/date for both moves. | Name an owner and date, e.g. "Finance brings a revised 2031 target to the Q1 2027 board meeting" or "Head of Operations sizes suburban/franchising revenue by Q2 2027." |
| 5 | Major | Logician / Premortem | "Why catering" | No mention of how the incumbent catering suppliers — whose slow delivery is cited as the reason 9 of 12 office managers are dissatisfied — might respond once Brightwell enters with a faster offer. | If a competitor fixes delivery speed or cuts price before April 2027, the ramp assumption is exposed and nothing in the memo would have flagged it in advance. | Add one sentence on expected competitor response, and confirm whether the "40% framework agreements in six months" trigger would catch it. |
| 6 | Major | Premortem (internal) | Recommendation / owner | No capacity or program-management plan is stated for building a new central kitchen (facility, four staff, supply chain) in ~5 months (Nov 2026 approval to Apr 2027 launch) on top of the Head of Operations' existing job. | If the build slips, the already-tight year-1 revenue (finding 1) slips further and payback moves past year four. | State the Head of Operations' capacity/backfill plan or name a dedicated build lead. |
| 7 | Minor | Outsider | "Why a delivery pilot," rollout sentence | "(about EUR 0.6m, a separate board decision...)" is unlabelled — unclear if it's rollout capex, revenue, or something else. | A reader could misattribute the figure. | Label it explicitly, e.g. "(rollout capex of about EUR 0.6m)". |
| 8 | Minor | Evidence Auditor | "Why catering," interviews | The 12 office-manager interviews aren't described (existing customers vs. broader market, how selected), yet feed a market-sizing calc meant to cover the wider 5km universe. | Minor — doesn't change the decision but weakens the input if challenged. | Add one line on sample composition. |
| 9 | Minor | CFO | "Why catering" | Only a single base case (EUR 2.9m) plus a triangulation range is given; unlike delivery, there's no named downside combination (e.g., lower conversion + lower margin together) and its effect on the payback year. | Minor given the 40% trigger provides an early warning. | Add a downside case and state its effect on the year-4 payback. |

## Numbers that do not tie
None found as stated. Every figure in the memo recomputes correctly: the catering contribution math (1.6/2.1/2.5/2.7 × 32% − EUR 0.35m fixed costs → 0.16/0.32/0.45/0.51, cumulative crossing EUR 1.2m in year 4), the EUR 5.3m total (2.9 + 2.4), the 8.5% growth figure, the EUR 12.7m gap (18 − 5.3), and "less than a quarter of the gap" (2.0/12.7 ≈ 16%) all check out. Finding 1 is a derived inconsistency (implied run-rate vs. stated forecast), not two stated values in conflict, so it is rated Major rather than listed here.

## Missing outside view
- Catering revenue ramp and unit economics: no external comparable for how another bakery/food-service catering unit scaled from a standing start — the memo only triangulates internally (bottom-up vs. top-down using Brightwell's own data).
- 3% price increase → EUR 1.1m: no comparable on realized price pass-through at similar chains facing discount competitors.
(Delivery growth is the exception — it is already benchmarked against two regional chains' reported 10–14% growth, which is good practice.)

## Premortem
1. **External:** The incumbent catering suppliers fix their slow-delivery problem or cut price once Brightwell announces the central kitchen, eroding the differentiation the whole case rests on — not addressed (finding 5).
2. **Internal — no owner:** The "revisit the target or floor" decision has no named owner or date, so it stalls after the meeting while the two funded moves proceed without the broader 2031 recalibration ever happening (finding 4).
3. **Internal — capacity:** The Head of Operations is asked to stand up a new central kitchen in about five months on top of running existing operations, with no stated backfill or program lead — if the April 2027 launch slips, the already-tight year-1 number slips further (finding 6).

## What is good and must survive
- The recommendation is specific where it matters most: owner, budget and start date for both of the two funded moves.
- Every number in the memo recomputes correctly, including the cross-page EUR 5.3m / 8.5% / EUR 12.7m chain — most one-pagers don't survive this check.
- Catering revenue is triangulated two independent ways (bottom-up and top-down) and delivery growth is benchmarked against named outside comparables — real triangulation and outside view, not just asserted.
- The delivery pilot has genuine go/no-go thresholds (60 orders/day, no in-store cannibalization) tied to a comparable-store control, not a vague "if it goes well."
- The memo is honest about its own limitation: it states plainly that suburban/franchising are rejected on margin alone because revenue was never sized, rather than hiding the gap.
- One page, direct, no padding — length is right for the decision being asked.


## Files in work dir after run

- pr-03-input.md
