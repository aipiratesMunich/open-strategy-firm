# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes. | yes | **Verdict:** Release with fixes |
| No Blocker findings. | yes | All 8 findings are listed as Major (7) or Minor (1); none are Blocker. |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo. | yes | Each Major row has a 'Consequence if unfixed' entry (e.g., finding 3: 'the board doesn't know whether the EUR1.2m kitchen still pays back in a time it would accept, or slips to year 5+'); recomputed figures (9,000×190≈1.71m, 62×0.03=1.86m, 1.86+0.9=2.76 vs 12.7) are internally consistent and don't m |
| Names what is good and must survive. | yes | 'What is good and must survive' section lists 6 items, e.g. 'The recommendation is concrete throughout: amount, owner, and start date for both funded moves.' |
| Must not demand a named framework, more length, or more slides. | yes | All 'Required fix' entries ask for added derivations, benchmarks, or named ownership (e.g., 'Show the actual build...', 'Name who runs sales/account management...'), none ask for a framework, more length, or more slides. |
| Must not flag the stated uncertainty or the explicit assumptions as weaknesses. | yes | Finding 3 critiques the absence of a downside payback calculation ('no downside payback shown'), not the act of stating the EUR2.5–3.3m range itself; the memo's explicit kill-switches and causal-alternative handling are praised, not penalized. |
| Must not claim numbers do not tie. | yes | '## Numbers that do not tie — None found. Every number the memo states more than once ... reconciles exactly.' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell Bakeries 2027 catering/delivery memo, gate 3

**Verdict:** Release with fixes
**In one line:** The two-move recommendation is sound and the numbers that are shown tie, but the two biggest financial claims (catering payback, gap-closing levers) rest on arithmetic the board can't check, and the memo's own justification for "revisit the target, not the floor" doesn't hold up.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and how should it resolve the resulting gap to the 2031 target? (*given*)
**Answer the draft gives:** Fund catering (EUR1.2m) and a delivery pilot (EUR0.3m); don't fund suburban stores or franchising; revisit the 2031 target rather than the margin floor. — These match; no mismatch finding.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | CFO (outside view) | "Why catering" | Delivery's 12% growth case is checked against two regional chains' actual results (10–14%). Catering — the larger investment (EUR1.2m) and larger revenue line (EUR2.9m) — has no outside comparable at all, only two internal methods (bottom-up, top-down) that triangulate with each other but not against any external benchmark. | The biggest single bet in the memo is the one with the thinnest external check; a board member who accepts the delivery benchmark will ask why catering doesn't have one. | Add at least one outside reference point (a comparable bakery/food-service catering ramp, or an industry benchmark for B2B catering growth) or state plainly that none exists and widen the stated uncertainty. |
| 2 | Major | Evidence Auditor / Model | "Why catering" | The 2027–30 revenue path (EUR1.6m/2.1m/2.5m/2.7m) that the whole kitchen payback rests on has no shown derivation. Two checks don't reconcile: (a) today's 9,000 orders × the interview median of EUR190/order ≈ EUR1.71m — above the stated *2027* figure of EUR1.6m, in year 1 of a growth investment; (b) continuing the cited 24% recent order growth for five years implies ≈26,000 orders by 2031 ≈ EUR5.0m at EUR190/order, roughly double the stated EUR2.9m 2031 base case. The path as given implies a much steeper deceleration (~31%→19%→8%→7% y/y) than anything in the memo explains. | The number the board is asked to approve a payback on can't be checked, and the one check available suggests either the growth rate or the order value quietly changes assumption partway through — nobody outside the team can tell which. | Show the actual build (orders × realized price, year by year) behind 1.6/2.1/2.5/2.7m, and state explicitly why growth decelerates from 24% to single digits (e.g., kitchen capacity cap, office density saturation) rather than letting the curve speak for itself. |
| 3 | Major | CFO (model) | "Why catering" | Only the base case (EUR2.9m by 2031) is run through the payback math. The memo's own range is EUR2.5–3.3m, but there's no downside payback shown. | If catering lands at the low end of its own stated range, the board doesn't know whether the EUR1.2m kitchen still pays back in a time it would accept, or slips to year 5+. | Rerun the payback at EUR2.5m (the low end) and state the resulting payback year alongside the base case. |
| 4 | Major | Premortem (internal) | "Why catering" | Hitting the "40% sign framework agreements in six months" threshold requires B2B account-management capability. No dedicated sales or account-management role is named; the plan hands the unit to the Head of Operations, who is already running the core retail business. | The kill-switch metric could fail for a reason the memo never considers — nobody on the team was staffed to sell — which looks to the board like a demand problem when it's a resourcing one. | Name who runs sales/account management for the catering unit (new hire, or an existing commercial role reassigned) alongside the Head of Operations' ownership of the unit. |
| 5 | Major | Premortem (internal) | "Why a delivery pilot" | Store staff are measured on in-store sales and service, not delivery throughput. Nothing in the memo reassigns labor, SLAs, or incentives for delivery fulfillment in the 8 pilot stores. | The pilot's own guardrail — "scale only if in-store transactions don't fall" — could read as a false negative: transactions could dip because staff deprioritize delivery under existing incentives, not because demand can't support both, and the board would wrongly conclude the delivery opportunity is capped. | State how delivery fulfillment is staffed/incentivized in the pilot stores so the "in-store transactions held" result is attributable to genuine capacity, not an incentive conflict. |
| 6 | Major | Logician | "What it adds up to" | The stated reason for recommending "revisit the target, not the floor" is that suburban stores and franchising "carry the weakest evidence." But the suburban figure comes from the actual 2025 P&L and the franchise figures from three real offers received — both are solid primary evidence, not obviously weaker than the catering/delivery case. The conclusion doesn't follow from the premise given. | A board member who checks this reasoning in the room will see it doesn't hold, which undercuts confidence in the memo's second (and more sensitive) recommendation — lowering the company's own growth target. | Replace the evidence-strength argument with the actual rationale (e.g., the margin floor is a financial-discipline guardrail the company doesn't want to weaken to accommodate two options that are structurally short of it, independent of how good their evidence is). |
| 7 | Major | Evidence Auditor | "What it adds up to" | The EUR1.1m (3% price increase) and EUR0.9m (longer hours, 12 stores) figures used to size how much of the gap can be closed have no shown calculation. A direct check — 3% of today's EUR62m revenue = EUR1.86m — doesn't match the stated EUR1.1m, and nothing in the memo explains the gap (elasticity, scope, competitor response). This does not flip the stated conclusion ("less than a quarter of the gap" still holds even at EUR1.86m + 0.9m = EUR2.76m against a EUR12.7m gap). | The board is asked to accept two un-derived numbers on the memo's second decision; even though the directional conclusion survives, a sharp board member will ask for the math and the team won't have it ready in the room. | Show the calculation and assumption behind both figures (e.g., volume loss assumed from the 3% increase given the two discount competitors; which stores/hours are included). |
| 8 | Minor | Outsider | "Why a delivery pilot" / "What would change our view" | The pilot's success bar is stated as "reach 60 orders per day" in the main text, but the kill-switch is "stays below 50 orders per day after month six" — two different numbers for what reads as the same metric, without labeling one as an interim checkpoint and the other as the final target. | — | Label explicitly: "month 6 interim checkpoint: ≥50/day; month 12 target: 60/day." |

## Numbers that do not tie
None found. Every number the memo states more than once (EUR5.3m = 2.9+2.4; 8.5% = 5.3/62; EUR12.7m gap = 80−67.3; the four catering contribution figures) reconciles exactly. The disagreements above are between the memo and the reviewer's own recalculation, not within the memo itself — flagged as Major per the review rules, not Blocker.

## Missing outside view
- Catering revenue growth to 2031: no comparable catering/food-service build-out cited (delivery has one; catering doesn't — see finding 1).
- 3% price increase impact: no comparable price-elasticity benchmark or prior Brightwell price move cited to sense-check the EUR1.1m (or EUR1.86m) figure.

## Premortem
1. **Internal — incentives:** Store staff are measured on in-store service, not delivery fulfillment; with no stated change to staffing or incentives in the pilot stores, delivery fulfillment degrades in-store service during peak hours, and the pilot's "transactions held" test fails for an execution reason the memo never considers (finding 5).
2. **Internal — capability:** The central kitchen's success depends on B2B sales and account management (signing framework agreements), a different skill from running retail stores, and no one is named to do it (finding 4).
3. **External — platform dependency:** The EUR3.10/order delivery contribution is net of platform fees Brightwell doesn't control. A platform fee increase (common in this market) compresses both the pilot economics and the EUR2.4m 2031 case, and the memo states no floor or mitigation (e.g., first-party ordering).

## What is good and must survive
- The recommendation is concrete throughout: amount, owner, and start date for both funded moves.
- "What would change our view" is stated up front — an explicit, falsifiable kill switch for both moves. Most memos at this stage don't do this; keep it.
- The memo directly confronts and rules out the obvious alternative causal story for catering growth (pandemic/return-to-office effect) with the Q2-over-Q2 data point, rather than ignoring it.
- Suburban stores and franchising are addressed and ruled out with sourced reasons, not silently dropped.
- The structural tension between the 2031 target and the margin floor is surfaced as an explicit second decision for the board, not buried or hidden.
- Delivery's growth assumption (12%) is benchmarked against actual outside results (two regional chains, 10–14%) — this is the standard the catering numbers should be held to as well.

**Note on verification:** I cannot check the "two regional chains" annual-report figures or the three franchise offers independently — those need the team's underlying sources on hand before the meeting, in case the CEO asks to see them.


## Files in work dir after run

- pr-03-input.md
