# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (4/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Release or Release with fixes. | NO | "**Verdict:** Return" |
| Must: no Blocker findings. | NO | Findings table lists #1 and #2 as "Blocker" severity. |
| Must: every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo. | yes | Each Major row has a populated "Consequence if unfixed" cell (e.g. #6: "the payback year moves and the margin case weakens"), and figures quoted from the memo (EUR 62m, EUR 1.1m, EUR 2.4m, 1.6m→2.7m) match the memo's own stated numbers. |
| Must: names what is good and must survive. | yes | Section "What is good and must survive" lists six specific strengths (e.g. "Suburban stores are rejected on one clean, sourced number"). |
| Must not: demand a named framework, more length, or more slides. | yes | Fixes requested are all about showing existing calculations/sourcing (e.g. "Show the current online revenue base and the calculation"), not a framework, added length, or more slides. |
| Must not: flag the stated uncertainty or the explicit assumptions as weaknesses. | yes | The memo's falsifying-conditions section is explicitly praised: "The 'what would change our view' section states falsifying conditions up front — rare, and worth keeping." |
| Must not: claim numbers do not tie (they do). | NO | "Numbers that do not tie" table claims "Price-increase impact ... ~EUR 1.86m expected vs. EUR 1.1m stated — ~40% unexplained haircut" and that the delivery 2031 revenue "has no stated revenue baseline connects the growth rate to the order-count figures," asserting mismatches the grading context says |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

Apologies — that tool is for code review, not applicable here. Here's the actual partner review:

# Partner review: Brightwell catering/delivery memo, gate 3

**Verdict:** Return
**In one line:** Two of the numbers that carry the most weight — the EUR 2.4m delivery forecast and the case for revisiting the 2031 target instead of the margin floor — aren't shown well enough for the board to verify or decide on them.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and should the board revise the 2031 revenue target or the margin floor? (given)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the 2031 target, not the floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | CFO | "Why a delivery pilot" paragraph | The headline "EUR 2.4m by 2031" has no stated baseline (current online/delivery revenue) and can't be reconciled with the order-count data two sentences earlier (38→60 orders/day, 8→18 stores). The catering number shows full arithmetic (revenue × margin − fixed cost); the delivery number doesn't. | The board is asked to accept half of the EUR 5.3m total — and therefore the size of the EUR 12.7m gap — on a number nobody in the room can check. | Show the current online revenue base and the calculation that turns 12% annual order growth into EUR 2.4m, in the same format used for catering. |
| 2 | Blocker | Decision Maker / Logician | "What it adds up to" closing sentence | The second board decision ("revisit the target or the floor") is resolved in one unsupported sentence ("every option that needs a lower floor also carries the weakest evidence"), with no comparison of what each choice actually costs the company (investor commitments tied to the 80m target vs. capital-discipline implications of lowering the 14% floor). | The board approves a strategically significant choice — revising a public target vs. loosening the margin discipline that screens every other investment — without seeing the tradeoff laid out. | Add a short comparison: what changes (externally and internally) if the target moves vs. if the floor moves, then restate the recommendation against that comparison. |
| 3 | Major | Evidence Auditor / CFO | "Why catering" paragraph | The EUR 2.9m catering base case is triangulated internally (bottom-up + top-down) but has no outside-view check against what comparable catering launches or central-kitchen investments actually achieved — unlike the delivery section, which cites two regional chains' 10–14% growth. | A sharp board member will ask why delivery got a benchmark and catering, the larger and more capital-intensive bet, didn't. | Add a comparable: take-up or ramp speed for a similar corporate catering launch or central-kitchen buildout, even a rough range. |
| 4 | Major | Evidence Auditor | "Why catering" paragraph | The 12 office-manager interviews aren't described by selection method; if they were drawn from existing (growing) catering customers, the 9-of-12 "slow delivery is the main pain" finding is survivorship-biased and may overstate how representative the problem is. | The qualitative case for a EUR 1.2m kitehen (built to fix "slow delivery") may rest on the views of customers who already stayed despite the problem, not the broader market. | State how the 12 were selected; if drawn only from active accounts, add a line on churned or non-customers, or flag the gap. |
| 5 | Major | Logician | "Why catering" paragraph → recommendation | No alternative is considered for solving the stated pain point (slow delivery from the current supplier) before jumping to a EUR 1.2m central kitchen — e.g., a new supplier contract, added capacity at an existing kitchen, dedicated delivery vans. | The board can't tell whether EUR 1.2m is the cheapest way to fix the named problem, only that it is one way. | Add one sentence ruling out the cheaper alternatives, with reasons (as was done for suburban stores and franchising). |
| 6 | Major | CFO / Model | "Why catering" paragraph | The central kitchen's fixed cost (EUR 0.35m/year: four staff and rent) is held flat across 2027–2030 while revenue nearly doubles (1.6m → 2.7m). No scaling logic or downside case is shown for this cost line, which drives the stated "payback in year four." | If a kitchen built for 1.6m of throughput needs more staff or space well before reaching 2.7m, the payback year moves and the margin case weakens — a risk the memo doesn't test. | Show whether the 0.35m holds at the higher volumes, or state the staffing/capacity trigger and its cost. |
| 7 | Major | Logician | "Why not suburban stores or franchising" | The franchising rejection ("6–8% royalty would cut store margin below the floor") subtracts the royalty straight from existing store margin without accounting for costs a franchisee would absorb instead of Brightwell (labor, local management, etc.). | The argument may overstate how much franchising actually erodes margin, which matters since franchising is one of only two alternatives ruled out to justify the target/floor recommendation. | Show the store-level P&L before and after royalty, net of costs that would transfer to the franchisee. |
| 8 | Major | CFO / Evidence Auditor | "What it adds up to" paragraph | The 3% price increase is said to add "about EUR 1.1m" — a naive calculation (3% × EUR 62m) gives ~EUR 1.86m, and the gap isn't explained (elasticity? limited scope of stores/categories?). Doesn't flip the "less than a quarter of the gap" conclusion, but the derivation isn't shown. | A board member doing the arithmetic in the room will catch the mismatch and lose confidence in the surrounding numbers, even though the bottom-line conclusion survives. | Show the basis for 1.1m (e.g., volume loss assumption, which stores/SKUs it applies to). |
| 9 | Major | Outsider / Premortem | Whole memo | Premortem risk not addressed: a central kitchen built for today's volume needs more staff/space well before 2030, which is the same root cause as #6 but also a standalone risk the "what would change our view" section doesn't cover (it only has a customer-signup trigger, not a cost/capacity one). | If costs scale with volume, the catering payback claim could fail without tripping any of the stated kill criteria. | Add a cost/capacity threshold to "what would change our view" for catering, parallel to the two already given for delivery. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Price-increase impact | "3% price increase... about EUR 1.1m" | Naive calc: 3% × EUR 62m current revenue | ~EUR 1.86m expected vs. EUR 1.1m stated — ~40% unexplained haircut |
| Delivery 2031 revenue | "EUR 2.4m by 2031... 12% annual order growth" | "pilot stores average 38 delivery orders per day... 60 orders per day" across 8→18 stores | No stated revenue baseline connects the growth rate to the order-count figures in the same paragraph |

## Missing outside view

- Catering 2031 base case (EUR 2.9m): no comparable corporate-catering launch or central-kitchen investment cited, unlike delivery's two-regional-chain benchmark.
- Price-increase impact (EUR 1.1m): no comparable price-elasticity reference for the region's bakery/food-retail category.

## Premortem

1. The central kitchen's fixed cost base (four staff, rent) doesn't scale with volume as catering revenue nearly doubles 2027→2030, quietly eroding the margin the payback claim depends on — not addressed (see #6, #9).
2. The delivery pilot hits its 60-orders/day threshold through discounting or promotion rather than organic demand, so the EUR 3.10/order contribution doesn't hold at full rollout — partially addressed (cannibalization vs. comparable stores is tested) but per-order margin at scale is not.
3. Office attendance trends reverse after only one year of post-stabilization data, stalling catering growth — partially addressed (one data point on continued growth) but no demand-side kill criterion exists alongside the signup-rate one.

## What is good and must survive

- The core recommendation is specific and actionable: named owner, budget and start date for each of the two funded moves.
- The delivery pilot is properly scoped — explicit go/no-go thresholds against a matched comparison group, and the rollout decision is deliberately deferred to a future board meeting rather than smuggled into this budget ask.
- The catering forecast triangulates two independent methods (bottom-up and top-down) to the same range, and the memo correctly rules out "return-to-office recovery" as the sole explanation for growth by showing continued growth after attendance settled.
- The "what would change our view" section states falsifying conditions up front — rare, and worth keeping for every future recommendation.
- Suburban stores are rejected on one clean, sourced number (13.1% vs. 14% floor) rather than a vague judgment call.
- The memo is honest that price increases and longer hours don't close the gap, instead of overselling secondary levers.

## What "fixed" looks like

"Fund two moves in the 2027 budget: a corporate catering unit (EUR 1.2m) and a twelve-month delivery pilot (EUR 0.3m), together adding an estimated EUR 4.6m–5.3m in revenue by 2031 depending on delivery growth, versus EUR 2.4m–8.0m achieved by comparable regional operators in their first three years. Even in the upside case, a EUR [X]m gap remains to the EUR 80m 2031 target; closing it without suburban stores or franchising (both of which breach the 14% margin floor on the numbers we tested) means the board should revise [the target / the floor], because [specific, quantified tradeoff — not just 'weaker evidence']." Fill in the delivery range once its derivation is shown, and replace the last clause with an actual comparison of what each choice costs the company.


## Files in work dir after run

- pr-03-input.md
