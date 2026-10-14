# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (2/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | **Verdict:** Return |
| no Blocker findings | NO | Finding #1 is listed as Severity 'Blocker' (Logician / CFO, 'Why catering') |
| at most two Major findings, each with a concrete, defensible reason | NO | Four findings (#2, #3, #4, #5) are labeled 'Major', exceeding the two-finding cap |
| names what is good and must survive | yes | 'What is good and must survive' section lists owners/dates/budgets, kill criteria, triangulated estimates, surfaced target-vs-floor gap, and math that ties |
| does not demand a named framework, more length, or more slides | yes | No request for additional length, slides, or a named framework appears anywhere in the review |
| does not flag the stated uncertainty or explicit assumptions as weaknesses | NO | Finding #1 treats the memo's explicit non-incremental framing of catering growth as a Blocker flaw rather than an accepted stated assumption, and 'Missing outside view' flags the stated 12% extrapolation assumption as a problem to fix |
| does not claim numbers do not tie when they actually do | NO | The review includes a table titled 'Numbers that do not tie' listing the EUR 5.3m figure as an entry, even though its own text admits 'Arithmetic ties; the definition of "additional" does not' — framing a conceptual critique as a tie failure |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell Bakeries 2027 budget memo, gate 3

**Verdict:** Return
**In one line:** The memo asks the board to approve EUR 1.2m for a new central kitchen without ever showing that current capacity can't already deliver the catering growth that's happening organically — if some of that growth would occur anyway, the payback claim and the EUR 5.3m headline are both overstated.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and how should it close the gap to the 2031 target? (given)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); skip suburban stores and franchising; revisit the 2031 target rather than the margin floor. Specific, actionable, and on-point — the mismatch is in what sits underneath it, not in whether a question was answered.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician / CFO | §"Why catering" | The memo never shows why a new kitchen is *necessary*. Its own evidence (orders 3,100→9,000 "without any sales effort") says growth is happening on existing capacity. The payback calc ("pays back in the fourth year") treats the *entire* projected catering contribution as attributable to the EUR 1.2m spend, with no stated counterfactual for what catering revenue does without it. | Board approves EUR 1.2m on the assumption that none of the EUR 2.9m 2031 catering revenue would happen anyway. If even part of it would, true incremental payback is later than year four — possibly never, under the current margin floor. | State current kitchen utilization/capacity ceiling. Rebuild the P&L on incremental revenue only (projected trajectory minus the no-investment baseline), and recompute payback on that basis. |
| 2 | Major | Evidence Auditor | §"Why a delivery pilot" | The pilot runs in "the eight high-street stores with the highest order density" — the best-case sites — then uses their 38→60 orders/day result to justify a EUR 0.6m rollout to all 18 stores, including lower-density ones never tested. | The EUR 2.4m 2031 delivery estimate, and the 60-orders/day bar itself, are calibrated on an unrepresentative sample; the rollout case could look much weaker in real conditions. | Add at least one lower-density store to the pilot, or explicitly flag the EUR 2.4m as an upper bound pending a second-tier test, with a range shown instead of a point estimate. |
| 3 | Major | Evidence Auditor | §"Why catering" | The EUR 190 median order value feeding the bottom-up revenue model comes from 12 interviewed office managers. The company already has actual transaction records for all 9,000 2026 orders. | A sharp board member asks "why use a 12-person survey when you have the real number?" — undermining confidence in a figure that drives the headline EUR 2.9m. | Replace or triangulate the interview-derived EUR 190 with actual average order value from sales data; keep the interviews for the qualitative finding (delivery speed as pain point), not the price point. |
| 4 | Major | Logician | §"Why not suburban stores or franchising" | "Royalty rates of 6-8% would cut store margin below the floor" conflates two different P&Ls: a royalty is revenue to Brightwell (near-zero marginal cost), not a cost line that mechanically erodes a company-operated store's margin the way it's framed here. | Whose margin falls below 14% — the franchisee's or Brightwell's — is never stated, so the stated reason for rejecting franchising doesn't survive one follow-up question, even if the ultimate answer is right. | State explicitly: "a franchisee's store, after paying 6-8% royalty, clears only X%, below the 14% floor we require of any store format carrying our brand" (or whatever the intended comparison is). |
| 5 | Major | Logician (premortem) | §"Why catering" | The stated #1 customer pain point is slow delivery from the current supplier. The proposed fix is to *centralize* production into one kitchen — which, depending on its location relative to today's store-based prep, could lengthen rather than shorten delivery times to offices. Not addressed anywhere. | The investment could fail to fix the one problem it's funded to fix, and the memo gives the board no way to see that risk coming. | Add one line on kitchen location versus customer geography, and/or a delivery-time KPI (not just order volume) to the catering kill criteria. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Catering 2031 revenue | "Base case: EUR 2.9m" (prose) | Year-by-year table only runs 2027-2030, ending at EUR 2.7m | 2031 figure never shown; consistent with the trend but not verifiable without it |
| "EUR 5.3m additional revenue by 2031" | Headline sum (2.9 + 2.4) | Underlying catering figure may include organic growth not caused by the investment (Finding 1) | Arithmetic ties; the definition of "additional" does not |

Everything else recomputes cleanly: the 32%-contribution-minus-fixed-cost series (0.16/0.32/0.45/0.51m), the payback-in-year-four claim on the stated (non-incremental) basis, the 8.5% growth figure, and the EUR 12.7m gap to the EUR 80m target all tie correctly to their stated inputs.

## Missing outside view

- Central kitchen payback: no benchmark cited for comparable bakery/catering central-kitchen investments — only an internal P&L extrapolation.
- Franchise store economics: no data from comparable bakery/QSR franchise networks on store margins after a 6-8% royalty, to check whether the rejection threshold is realistic.
- Delivery growth comparables (10-14%) were observed only in competitors' *first three years*; the memo's base case (12%) is projected out to 2031, several years beyond that observed window — flag the extrapolation rather than treating it as like-for-like.

## Premortem

1. The central kitchen doesn't fix — or worsens — delivery speed to offices, the one factor customers named as the main pain point, because production is now farther from some customers than today's store-based prep. (Finding 5)
2. The 18-store rollout underperforms the pilot because the pilot was run only in the highest-density stores; lower-density stores don't reach the volume or cannibalization profile the pilot showed. (Finding 2)
3. Office-based demand is the shared driver behind both catering and delivery growth; a renewed shift away from office attendance would hit both moves at once, and the memo has no combined downside case for that shared risk.

## What is good and must survive

- Every move names an owner, a date, and a budget — no "explore" or "consider" language anywhere.
- Both moves carry explicit, falsifiable "what would change our view" kill criteria — genuinely rare and worth keeping.
- The catering estimate is triangulated two ways (bottom-up orders × value, top-down workers × spend) and the delivery estimate is checked against two outside comparables — real rigor, not just internal modeling.
- The memo doesn't hide the gap to the 2031 target; it surfaces a second decision (target vs. floor) and gives a reasoned basis for recommending one over the other (the options that would close it need a lower floor and have the weakest evidence).
- Where the math is shown, it ties — the contribution/payback series and the headline arithmetic all check out on recomputation.

## What "fixed" looks like

"Fund two moves in the 2027 budget: a corporate catering unit (EUR 1.2m central kitchen, Head of Operations, April 2027), justified because current store kitchens are at [X]% of capacity and cannot absorb projected volume beyond 2027 without it; net of the catering growth we'd expect to continue regardless, the investment adds an estimated EUR 1.1m-1.7m of incremental revenue by 2031 and pays back in year [N] on that basis. And a twelve-month, EUR 0.3m delivery pilot spanning both high- and low-order-density stores, to test whether the 38-to-60-orders/day uplift holds outside the strongest sites before a EUR 0.6m full rollout."


## Files in work dir after run

- pr-03-input.md
