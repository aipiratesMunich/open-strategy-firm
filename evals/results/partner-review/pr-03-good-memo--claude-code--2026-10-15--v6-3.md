# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings are rated Major or Minor; no 'Blocker' severity appears in the table |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | Finding 1: 'The gate for the EUR 0.6m rollout isn't tied to the model that justifies it'; Finding 3: 'this conclusion is weaker than presented' tied to the board's revisit-target decision; figures (2.9, 2.4, 5.3, 8.5%, 12.7, 1.1+0.9) match the reference arithmetic given |
| Names what is good and must survive | yes | 'What is good and must survive' section lists actionable ownership, triangulated catering data, fully-shown payback build, and evidence-based rule-outs |
| Must not demand a named framework, more length, or more slides | yes | All required fixes ask for sourcing, calculations, or stated assumptions (e.g. 'Name the source, date and scope...', 'Show the calculation behind each figure in one line') — none ask for a framework, more length, or more slides |
| Must not flag the stated uncertainty or the explicit assumptions as weaknesses | yes | Findings target missing sourcing/linkage (e.g. unnamed 'spend per head' source, unlinked 40% threshold) rather than penalizing any uncertainty or assumption the memo explicitly disclosed |
| Must not claim numbers do not tie | yes | 'Numbers that do not tie: None found — every headline figure ... recomputes cleanly from the inputs given' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Release with fixes
**In one line:** The pilot's pass bar for delivery (60 orders/day in 12 months, up from 38) implies ~58% growth — nearly five times the 12% annual rate the memo uses to value the EUR 2.4m rollout — and nothing reconciles the two, which undercuts the gap analysis that drives the board's second decision.

**Question the draft must answer:** Which two moves should the board fund in the 2027 budget, and should the board revisit the 2031 revenue target or the margin floor? (Given, in the memo's own header.)
**Answer the draft gives:** Fund the catering unit (EUR 1.2m) and the delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the revenue target, not the floor. Match: yes.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | CFO / Logician | "Why a delivery pilot" | Pilot passes if stores reach 60 orders/day in 12 months (from 38 today, ~58% growth), but the EUR 2.4m/2031 valuation and the EUR 0.6m rollout decision rest on 12% annual growth — a rate nearly 5x lower for the same metric. | The board can't tell whether passing the pilot proves the base case or far exceeds it (understating the prize), nor whether a near-miss that still beats 12%/year would wrongly be read as failure. The gate for the EUR 0.6m rollout isn't tied to the model that justifies it. | Show the orders/day path implied by 12% annual growth from 38/day, and state explicitly why the pass bar sits above (or below) that path — e.g. year-one launch push vs. steady-state rate from 2028. |
| 2 | Major | Evidence Auditor | "Why catering" | The top-down estimate (office workers within 5km × catering spend per head) has no sourced "spend per head" figure, so it isn't shown to be independent of the bottom-up estimate it's used to corroborate. | The memo's main support for treating EUR 2.9m as credible is "two independent methods converge on EUR 2.5–3.3m." If the top-down multiplier was fitted to match the bottom-up number, that's one estimate presented as two. | Name the source, date and scope of the catering-spend-per-head figure. |
| 3 | Major | Evidence Auditor | "What it adds up to" | The EUR 1.1m price-increase and EUR 0.9m extended-hours estimates have no stated method, unlike every other figure in the memo. | These two numbers support "closes less than a quarter of the gap," which is the premise for recommending the board revisit the target rather than the floor. If either is materially off, that conclusion is weaker than presented. | Show the calculation behind each figure in one line (stores/products affected, uplift basis, extra hours × average sales/hour). |
| 4 | Major | Logician / Evidence Auditor | "What would change our view" | The 40%-framework-agreement threshold for catering appears for the first time in the closing section; the base case built earlier never mentions framework agreements or a take-up assumption. | The board is handed an early-warning trip-wire it cannot evaluate — no way to tell if 40% is the rate the model needs, a buffer, or arbitrary. | State what take-up rate (if any) the EUR 2.9m base case assumes, and show that 40% in six months is the level below which that assumption breaks. |
| 5 | Minor | Evidence Auditor | "Why a delivery pilot" | "Two regional chains" comparable is unnamed, undated. | — | Name the chains and the years their 10–14% growth covers. |
| 6 | Minor | Evidence Auditor | "Why not suburban stores or franchising" | "Royalty would cut margin below the floor" has no arithmetic shown. | — | State the pre-royalty store margin so the conclusion can be checked in one line. |
| 7 | Minor | Outsider | "What it adds up to" | "Today's EUR 62m" has no fiscal year. | — | Add the year (e.g. "2026E revenue"). |
| 8 | Minor | Logician | "Why catering" | Contribution table runs 2027–2030 only; 2031 (EUR 2.9m, used in the roll-up) isn't shown in the same table. | — | Add the 2031 line. |
| 9 | Minor | Evidence Auditor | "Why catering" | EUR 190 median order value — a quantitative model input — comes from only 12 interviews. | — | Note as a small-sample input; mitigated once Finding 2 is fixed. |

## Numbers that do not tie
None found — every headline figure (EUR 2.9m catering, EUR 2.4m delivery, EUR 5.3m total, 8.5% growth, EUR 12.7m gap, the four-year payback build) recomputes cleanly from the inputs given.

## Missing outside view
- Delivery growth rate: the 12% base case is checked against two regional chains' first three years — name them (Finding 5) so the comparison can be verified.
- Catering spend-per-head: no outside benchmark or source at all (Finding 2) — this is the gap, not just a citation nicety.

## Premortem
1. **Market:** A national delivery platform or a competing bakery chain reacts to the visible 9,000-order catering growth with its own corporate offer or undercuts on courier fees, compressing the EUR 3.10 per-order contribution before volume scales — the memo has no stated sensitivity to platform-fee or competitive-price erosion.
2. **Internal — incentives:** Store staff at the 8 (then 18) high-street stores are not given revised targets for delivery fulfillment. If their existing KPIs reward counter sales and queue times, packing delivery orders during peak hours gets deprioritized, capping daily volume regardless of demand — the memo names a budget owner (Head of Digital) but not who resets store-level incentives.
3. **Internal — capacity:** The Head of Operations who owns the EUR 1.2m kitchen also runs existing bakery production. If the April 2027 launch collides with a production peak, the new unit loses capacity to the core business and ramps slower than the EUR 1.6m year-one plan assumes, with no named escalation point above the Head of Operations if that happens.

## What is good and must survive
- The recommendation is fully actionable: named owner, budget and start date for both moves (Head of Operations / EUR 1.2m / April 2027; Head of Digital / EUR 0.3m / March 2027).
- Catering triangulates sales data, 12 customer interviews and two sizing methods, and sources the contribution margin from the actual 2025 P&L rather than an assumption.
- The payback build is fully shown and recomputes exactly: EUR 0.16m/0.32m/0.45m/0.51m from the stated revenue path and the EUR 0.35m kitchen fixed cost, landing payback correctly in year four.
- Suburban stores and franchising are ruled out with real data (actual 2025 margins, actual franchise offers), not asserted.
- The memo states concrete leading indicators that would change the recommendation (take-up rate, orders/day, cannibalization), not just generic risks.
- One page, no padding, every section ties back to one of the two decisions the board must take.


## Files in work dir after run

- pr-03-input.md
