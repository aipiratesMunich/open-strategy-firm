# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (3/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | NO | **Verdict:** Return |
| No Blocker findings | NO | Finding #1 is listed as severity **Blocker** |
| At most two Major findings, each with a concrete, defensible reason | NO | Four findings (#2, #3, #4, #5) are marked Major |
| Names what is good and must survive | yes | 'What is good and must survive' section lists funded moves, payback math, triangulated revenue range, benchmarked delivery assumption, falsifiable kill-criteria, and no gap-hiding |
| Does not demand a named framework, more length, or more slides | yes | No fix requests a named framework, additional length, or more slides; fixes ask for clarifying language/sensitivity, not volume |
| Does not flag the stated uncertainty or explicit assumptions as weaknesses | NO | Finding #5 criticizes the memo for leaving the target-vs-floor choice open ('offers no point of view on which... missed opportunity to lead the decision'), which is an explicit, disclosed open question in the memo, not a hidden flaw |
| Does not claim numbers do not tie | yes | 'Numbers that do not tie: None found mismatched across the memo... all tie' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Return
**In one line:** The EUR 2.4m delivery benefit driving the headline EUR 5.3m / EUR 12.7m-gap numbers requires a chain-wide rollout that is neither funded, costed, nor disclosed as a future ask — only an 8-store pilot is in this budget.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and does it need to revisit the 2031 revenue target or margin floor? (given, memo header)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; base case still leaves a EUR 12.7m gap to the EUR 80m 2031 target, so the board must revisit the target or the floor — no view offered on which.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | CFO / Logician | "Why a delivery pilot" + "What it adds up to" | The EUR 2.4m delivery contribution to 2031 (and hence the EUR 5.3m total, 8.5% growth, and EUR 12.7m gap) requires rolling delivery out beyond the 8 pilot stores. Only the EUR 0.3m, 8-store, 12-month pilot is funded here; no rollout decision, timeline, or cost is in the memo. At the pilot's current 38 orders/day × EUR 3.10 contribution, the 8 stores generate roughly EUR 0.34m/year — nowhere near EUR 2.4m. | The board approves the pilot believing EUR 12.7m is *the* gap to the 2031 target. In fact, realizing EUR 2.4m needs a second, unbudgeted investment decision that hasn't been asked for. If that decision is delayed or declined, the real gap is larger than stated — and the board's choice on whether to revisit the target or the floor is made on an understated number. | Separate "pilot" from "full rollout" explicitly: state what chain-wide delivery would cost to build out (kitchens/packaging/staffing beyond the 8 stores) and reframe EUR 2.4m as contingent on a rollout decision not yet requested. Show the base case with only the pilot's realistic 2027–2031 contribution if rollout isn't approved. |
| 2 | Major | CFO | "Why catering" | No outside-view benchmark for the catering growth trajectory (EUR 1.6m → 2.9m by 2031, ~16%/yr). Delivery gets one (two regional chains, 10–14% actual growth); catering doesn't. | A board member asks "compared to what?" and there's no answer — the catering base case could be a hoped-for case dressed as a base case, and nothing in the memo would catch it. | Add at least one comparable: how fast did another bakery/foodservice central-kitchen catering operation actually grow after launch, or what take-up rate did similar office-catering offers reach in year 1–2. |
| 3 | Major | CFO / Model | "Why catering," the 1.6/2.1/2.5/2.7 figures | These four annual revenue figures aren't traced to a stated growth or take-up driver (unlike delivery's explicit "12% annual order growth"). They look like they were set to land the curve at ~EUR 2.9m by 2031, not built up from an assumption. | No one outside the team can stress-test the payback-in-year-4 claim — if the real growth rate undershoots, there's no way to say by how much payback slips, because the driver was never named. | State the assumed annual order/take-up growth rate (e.g., "orders grow X%/year off the current 9,000, framework-agreement take-up ramps to Y% by year N") and derive the four revenue figures from it. |
| 4 | Major | CFO / Model | "Why catering," central kitchen fixed costs | The EUR 0.35m/year fixed cost (four staff + rent) is held flat across all four years even as catering revenue nearly doubles (EUR 1.6m → 2.7m). No sensitivity shown on whether the kitchen needs more staff/capacity to serve that growth. | The single most load-bearing number in the memo — "payback in the fourth year" — could be wrong in the optimistic direction if fixed costs must step up with volume, and the board has no way to know. | Show whether the kitchen's rated capacity covers the 2030 volume without added headcount/rent; if it doesn't, add a step-up and re-run payback. |
| 5 | Major | Decision Maker / So-What | "What it adds up to," final sentence | The memo surfaces "revisit the 2031 target or the margin floor" as a board decision but offers no point of view on which, despite having just shown that relaxing the margin floor is exactly what sank suburban stores and franchising. | The board is handed a harder, less-structured choice than the team's own analysis supports — this is explicitly allowed to be the board's call (so Major, not Blocker), but it's a missed opportunity to lead the decision. | Add one sentence of team recommendation, e.g., which lever (target vs. floor) the team would lean toward and why, given what the rest of the memo already shows about floor economics. |
| 6 | Minor | Evidence Auditor | "What it adds up to," price increase | "3% price increase (about EUR 1.1m)" — 3% of EUR 62m is EUR 1.86m, not EUR 1.1m; the gap presumably reflects an assumed volume/competitive offset, but it isn't shown. | Low — doesn't change the qualitative conclusion ("doesn't close the gap"), but a sharp reader will flag the unreconciled arithmetic. | One clause: "after an assumed X% volume loss to the two discount competitors." |
| 7 | Minor | Logician | "Why not suburban stores" | Rejection rests on existing suburban stores' average margin (13.1%) as a proxy for new-store economics, with no view on whether better site selection could clear the 14% floor. | Low on its own, but it's the only evidence offered against a move a board member will likely ask about directly. | One line on whether site selection could plausibly close the 0.9-point gap, or why not. |
| 8 | Minor | Outsider | "What would change our view" | "Framework agreements" appears only in the kill-criterion sentence, never introduced or explained in the catering rationale above it. | Low — a board member can infer it, but it reads as a term dropped in from an earlier draft. | Introduce the concept once in the catering paragraph (what a framework agreement is, why 40% take-up is the right bar). |
| 9 | Minor | Evidence Auditor | Catering revenue figures | Figures carry one-decimal precision (EUR 2.9m, EUR 0.51m) despite resting on a 12-person interview sample and a bottom-up/top-down range that's itself EUR 0.8m wide. | Low — doesn't change the decision, but invites "how precise is this really?" | Present the base case as a range (e.g., EUR 2.5m–3.3m, base case ~2.9m) rather than single-point figures carried to two decimals downstream. |

## Numbers that do not tie
None found mismatched across the memo — the catering payback arithmetic (1.6/2.1/2.5/2.7 × 32% − 0.35 = 0.16/0.32/0.45/0.51) recomputes correctly, and 2.9 + 2.4 = 5.3, 5.3/62 = 8.5%, 62 + 5.3 = 67.3, 80 − 67.3 = 12.7 all tie. The problem is not arithmetic — it's an undisclosed dependency behind the EUR 2.4m delivery figure (Finding 1).

## Missing outside view
- **Catering growth to 2031:** no comparable company's actual central-kitchen catering ramp cited, unlike delivery's two-regional-chain benchmark.
- **Central kitchen fixed-cost scaling:** no reference point for whether four staff can serve both EUR 1.6m and EUR 2.7m of throughput without added cost.

## Premortem
1. The EUR 2.4m delivery benefit never materializes because chain-wide rollout turns out to need meaningful capex/opex that was never budgeted or approved — the board finds out the "EUR 12.7m gap" was really closer to EUR 15m all along.
2. Office catering demand cools (further hybrid-work reversion, a recession hitting corporate T&E/catering budgets) while the central kitchen's EUR 0.35m fixed cost doesn't flex down, pushing payback past year 4 into a loss position with no downside case to show how bad it gets.
3. A delivery-platform fee increase or a new discount entrant compresses the EUR 3.10 per-order contribution before the pilot has run long enough to prove the 60-orders/day target — the pilot's economics move the goalposts mid-test, and the memo has no plan for that.

## What is good and must survive
- Two sharply specific funded moves — amount, owner, start date — plus two explicitly rejected moves with stated reasons (margin floor breach). This is exactly the level of actionability check 2 asks for.
- The catering payback math is genuinely recomputable and checks out by hand.
- Catering revenue range is triangulated two independent ways (bottom-up orders × value, top-down worker density × spend) and converges — good evidence discipline.
- Delivery's growth assumption is benchmarked against two real comparable companies' actual multi-year results, not just built bottom-up from hope.
- Pre-registered, falsifiable kill-criteria for both moves ("what would change our view") — this is rare and should be kept in any rewrite.
- The memo doesn't hide the gap to the 2031 target or inflate secondary levers to paper over it; it explicitly shows price increase + longer hours closing less than a quarter of the gap.

## What "fixed" looks like
"Fund the EUR 1.2m catering kitchen and the EUR 0.3m, 8-store delivery pilot in 2027. Catering's base case (EUR 2.9m by 2031) is fully funded by this ask. Delivery's EUR 0.3m buys proof of concept only; scaling delivery chain-wide to capture the full EUR 2.4m opportunity is a separate decision we are not asking the board to make today, and we don't yet know what it costs — we'll bring that back after the pilot reports in Q1 2028. On that basis, the board should treat the gap to the 2031 target as at least EUR 12.7m today, with more clarity once delivery rollout economics are costed; we recommend [the team's actual view] on whether to revisit the target or the floor rather than leaving that open."


## Files in work dir after run

- pr-03-input.md
