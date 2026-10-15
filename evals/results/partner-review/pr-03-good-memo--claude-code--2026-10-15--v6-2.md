# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings table entries are labeled Major or Minor; no Blocker row appears |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | E.g. Major #3: 'The board approves EUR 1.2m against a conversion assumption that may not hold if delivery speed isn't actually improved'; Major #4's figures (9,000 orders × EUR190 ≈ EUR1.71m vs EUR1.6m 2027 projection) match the memo's stated 9,000 orders, EUR190 median, and EUR1.6m 2027 catering re |
| Names what is good and must survive | yes | Section '## What is good and must survive' lists five specific strengths (gated metrics, named owners, triangulated demand range, named policy floor, honest hedging) |
| Does not demand a named framework, more length, or more slides | yes | All required fixes are 'add one sentence', 'rerun the four-year profit build', 'state the revenue base' — no demand for a framework or more slides/length |
| Does not flag the stated uncertainty or explicit assumptions as weaknesses | yes | The honest hedging on target-vs-floor is explicitly praised ('honestly hedged... gives the board a concrete fallback rather than forcing a false choice'); findings target missing builds/reconciliations, not the memo's disclosed ranges or caveats |
| Does not claim numbers do not tie (when they do) | yes | '## Numbers that do not tie — None found. EUR 2.9m + EUR 2.4m = EUR 5.3m; EUR 5.3m / EUR 62m = 8.5%; EUR 80m − EUR 62m − EUR 5.3m = EUR 12.7m... all check out arithmetically' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027", gate 3

**Verdict:** Release with fixes
**In one line:** The headline arithmetic ties and the asks are cheap, gated and owned — but two of the six numbers behind the EUR 5.3m growth story (the delivery revenue build and the catering demand-conversion criterion) aren't shown or don't line up with the pilot's own success bar, and the CEO will get asked about both tomorrow.

**Question the draft must answer:** Should the board fund the catering unit and delivery pilot in 2027, and what should it do about the gap to the 2031 target? (given)
**Answer the draft gives:** Fund both (EUR 1.2m catering, EUR 0.3m pilot), don't fund suburban/franchising, and revisit the 2031 target rather than the 14% margin floor. The two match.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Logician | "Why delivery pilot" | The pilot's own pass bar (38→60 orders/day within the 12-month pilot) implies order growth well above the "12% annual order growth" used to size the EUR 2.4m/3.5m 2031 figures — a store can clear the pilot threshold on growth the long-run model doesn't assume. | The board may read "pilot passed" as confirmation of the 12% growth case used to justify the later rollout, when the two aren't the same test. | Add one sentence reconciling the two: state the growth rate the 60/day target implies and explain why it's expected to revert to ~12% after the pilot's marketing push fades, or use the same rate in both places. |
| 2 | Major | Evidence Auditor | "Why delivery pilot" | EUR 3.10 contribution per order is given, but no revenue-per-order or price assumption is shown, so EUR 2.4m/3.5m by 2031 can't be recomputed from anything in the memo. | Half of the headline EUR 5.3m growth number is unverifiable by the board. | Show the build: orders/day × stores × days × average order value (or contribution, labelled as such) → 2031 total, for both the 12% and 18% cases. |
| 3 | Major | Evidence Auditor | "Why catering" | Nine of twelve office managers cite slow delivery as the main reason to switch suppliers, but nothing describes how the new central kitchen is faster than the current supplier — the solution's design isn't tied to the pain point that justifies demand. | The board approves EUR 1.2m against a conversion assumption that may not hold if delivery speed isn't actually improved. | Add one sentence on how the central kitchen's logistics beat the current supplier's (e.g., dedicated routing, closer-to-store production), or flag this as unverified. |
| 4 | Major | Skeptical CFO | "Why catering" | 9,000 orders in 2026 at the stated median EUR 190/order implies a ~EUR 1.71m current run-rate, yet the 2027 projection (year one of the EUR 1.2m investment) is EUR 1.6m — flat to down, not up. | The board sees a growth investment showing a flat/declining first year with no explanation, inviting the obvious "why pay for a kitchen to go backwards" question. | State the 2026 catering revenue baseline explicitly next to the 2027 figure, and explain the gap (mix shift, one-off bulk orders in the median, phased kitchen ramp-up, etc.). |
| 5 | Major | Skeptical CFO | "Why catering" (payback calc) | The payback-in-year-4 claim uses only the EUR 2.9m base case; no recalculation at the stated EUR 2.5m low end of the triangulated range. | If actual revenue lands at EUR 2.5m, payback likely slips past year 4 (cumulative profit at the low end would fall short of EUR 1.2m by the same point) and the board is told a looser payback claim than the range supports. | Rerun the four-year profit build at EUR 2.5m and EUR 3.3m and state the payback-year range, not a single year. |
| 6 | Major | Logician | "What would change our view" (catering) | The catering kill criterion — "40% of current office customers sign framework agreements in the first six months" — introduces a sales mechanism ("framework agreements") that appears nowhere else in the memo. The EUR 0.35m fixed cost covers only "four staff and rent" (production), not a sales/account function. | The board can't judge whether 40% is a meaningful bar, and may be approving a plan whose success test depends on a sales motion that isn't staffed or budgeted. | Either name framework agreements in the recommendation/cost section and state who runs that conversion effort, or replace the kill criterion with one the memo's own plan actually tracks (e.g., repeat-order rate). |
| 7 | Minor | Skeptical CFO | "What it adds up to" | A 3% price increase on today's EUR 62m should be ~EUR 1.86m; the memo states EUR 1.1m with no base or elasticity shown. | Doesn't change the stated "closes less than a quarter of the gap" conclusion (1.1+0.9 is still well under 25% of 12.7), so it's a transparency gap, not a decision-flipping one. | State the revenue base the 3% applies to, or note the volume loss assumed from the two discount competitors. |
| 8 | Minor | Evidence Auditor | "Why catering" | Twelve office-manager interviews is a thin sample for a EUR 190 median and a 9/12 pain-point finding, even though it's triangulated against a top-down estimate. | None that flips the recommendation — the range is corroborated independently. | Note the sample size as a caveat, or state the confidence interval if available. |
| 9 | Minor | Outsider | "Why delivery pilot" | "a rollout to all 18 high-street stores from 2028 if the pilot passes (about EUR 0.6m, a separate board decision...)" reads ambiguously — unclear whether EUR 0.6m is the rollout investment or something else. | A reader skims past it or misreads it; low stakes since it's explicitly deferred to a later board decision anyway. | Rewrite as: "a rollout to all 18 stores from 2028 if the pilot passes, at an estimated EUR 0.6m investment — a separate board decision at the end of the pilot." |

## Numbers that do not tie
None found. EUR 2.9m + EUR 2.4m = EUR 5.3m; EUR 5.3m / EUR 62m = 8.5%; EUR 80m − EUR 62m − EUR 5.3m = EUR 12.7m; the four-year catering profit build (EUR 0.16m/0.32m/0.45m/0.51m from the stated revenue × 32% − EUR 0.35m) all check out arithmetically. The headline rollup is internally consistent.

## Missing outside view
- Catering contribution margin at scale (32%): only the 2025 internal P&L is cited; no comparable catering operator's margin at a similar order volume.
- Price elasticity for the 3% increase: only "two discount competitors" named qualitatively; no comparable price-elasticity data point.
- Delivery growth (10–14% from two regional chains' annual reports) is already a genuine outside comparator — this is a strength, not a gap.

## Premortem
1. **Internal/incentive:** The central kitchen's four staff sit under the Head of Operations, who also runs core bakery production — when the two compete for oven time or management attention during retail peaks, catering loses out and the 1.6m→2.9m ramp stalls without anyone flagging it as a decision.
2. **Design/evidence:** The stated #1 reason customers would switch — slow delivery — is never shown to be fixed by the new kitchen; if speed doesn't improve, office managers don't convert and the framework-agreement target (finding 6) is missed for a reason the memo never tested.
3. **External/competitive:** Once Brightwell visibly enters catering and delivery, the incumbent supplier or a discount competitor matches on speed or price, compressing the EUR 3.10/order delivery contribution and the 32% catering margin below the levels the payback math assumes.

## What is good and must survive
- Both asks are small, time-boxed, and gated on explicit, falsifiable metrics before any bigger commitment (EUR 0.3m pilot with a 60 orders/day and no-cannibalization test, before an EUR 0.6m rollout decision later).
- Named owner and start date for each initiative (Head of Operations/April 2027; Head of Digital/March 2027) — no orphaned recommendations.
- Catering demand is triangulated two independent ways (bottom-up and top-down) landing in a consistent EUR 2.5–3.3m range, and the base case (EUR 2.9m) is a defensible pick within it.
- Suburban stores and franchising are rejected against a specific, named policy floor (14% margin) rather than vague judgment.
- The secondary ask — revisit the target, not the floor — is honestly hedged: it states what's known (margins) versus unknown (revenue) for the rejected options and gives the board a concrete fallback (size those options first) rather than forcing a false choice.

---
Six Majors, all fixable with a sentence or a rerun each — none of them make the draft's own stated numbers contradict each other or flip today's actual ask (fund the two small, gated moves). Worth tightening findings 1, 2, 4, 5, and 6 before this goes to the CEO tonight; 3, 7–9 can go either way given the deadline.


## Files in work dir after run

- pr-03-input.md
