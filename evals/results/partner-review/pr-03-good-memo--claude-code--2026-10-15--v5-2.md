# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | **Verdict:** Return |
| no Blocker findings | NO | Finding #1 is listed with Severity "**Blocker**" |
| every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | Findings #2-5 each have a 'Consequence if unfixed' entry (e.g. 'a board member asking "walk me through the 2.4m" gets no answer'); the review's own recomputation confirms rather than disputes the reference figures (2.9+2.4=5.3, 5.3/62=8.5%, etc.) |
| names what is good and must survive | yes | 'What is good and must survive' section lists five items including 'Headline arithmetic ties on recomputation' |
| must not demand a named framework, more length, or more slides | yes | No request found for additional slides, length, or a named framework |
| must not flag the stated uncertainty or the explicit assumptions as weaknesses | yes | Findings target unshown derivations and missing sponsor/trade-off ownership, not the memo's own stated uncertainty ranges or assumptions |
| must not claim numbers do not tie when they do | yes | Review explicitly validates the tying figures ('Headline arithmetic ties on recomputation: EUR 2.9m + 2.4m = 5.3m...') rather than disputing them |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell CEO memo ("Fund corporate catering and a delivery pilot in 2027"), gate 3

**Verdict:** Return
**In one line:** The memo's stated reason for recommending "revisit the target, not the floor" directly contradicts the memo's own rejection logic two paragraphs earlier — the CEO cannot defend this to the board as written.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and should the board revisit the 2031 revenue target or the 14% margin floor? (given, stated in the header)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the target, not the floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Logician | "What it adds up to" (closing lines) | The memo rejects suburban stores and franchising on margin economics (13.1% vs. 14% floor; 6–8% royalties cut below floor — both hard P&L/offer data). Two paragraphs later it recommends keeping the floor and moving the target because those same two options "carry the weakest evidence" — a different, unsupported claim that contradicts the stated rejection reason. | CEO presents a non-sequitur as the rationale for the second board decision; the first board member to re-read the memo spots the contradiction, and it undermines confidence in the funding asks sitting next to it. | Rewrite the rationale to say what's actually true: the floor is *why* those options fail, so lowering it buys optionality on two already-weak bets; keep the floor, and propose a specific revised 2031 target number (or range) instead of leaving "revisit" unquantified. |
| 2 | Major | Evidence Auditor / CFO | "Why a delivery pilot…" paragraph | EUR 2.4m by 2031 is never derived from the building blocks given (38→60 orders/day, EUR 3.10 contribution/order, 18 stores, 12% annual growth). Unlike the catering math, there is no visible calculation. | A board member asking "walk me through the 2.4m" gets no answer; 45% of the EUR 5.3m "size of the prize" can't be checked live. | Show the arithmetic: orders/day × contribution × stores × growth path to 2031, on the input sheet, matching the EUR 2.4m output. |
| 3 | Major | Evidence Auditor | "Why a delivery pilot…" paragraph | The pilot runs in the 8 *highest order-density* stores; EUR 2.4m assumes all 18 stores (including 10 untested, lower-density ones) perform the same way after rollout. | If the untested stores convert at even half the pilot rate, the delivery contribution — and the target-gap math built on it — drops materially. | State the rollout assumption explicitly (e.g., "non-pilot stores assumed to reach X% of pilot density") and give a range, not a point estimate, for the 10 untested stores. |
| 4 | Major | Skeptical CFO | "What it adds up to" paragraph | EUR 1.1m from "a 3% price increase" doesn't reconcile with 3% × today's EUR 62m (EUR 1.86m), with no scope/elasticity explanation for the gap. The EUR 0.9m longer-hours figure has the same problem — no shown derivation. | Both numbers feed directly into "together they close less than a quarter of the gap"; a board member re-doing the math in the room will flag the mismatch. | Show the base each percentage applies to (e.g., "3% on the X% of revenue not facing discount competition") and the per-store-hour assumption behind EUR 0.9m. |
| 5 | Major | Checklist Premortem | Whole memo | No sponsor is named above the two functional owners, and nothing addresses the central kitchen and delivery pilot drawing on the same store staff, ovens and management time as core bakery production at the busiest stores. | If either initiative is quietly deprioritized when it competes with core operations, the catering payback (already four years out) is the first casualty, and no one is accountable for noticing. | Name a sponsor above Head of Operations/Head of Digital and a quarterly checkpoint; state explicitly how kitchen/delivery staffing is kept separate from store-floor staffing during peak hours. |

## Numbers that do not tie
None stated twice with different values. (The EUR 1.1m price-increase figure disagrees with the reviewer's own recomputation — finding #4 — which the checklist treats as a Major, not this table, since it's a derivation gap, not a restated contradiction.)

## Missing outside view
- **Central-kitchen catering payback (4 years):** no comparable bakery/café chain's actual central-kitchen catering launch (ramp, payback) cited — only Brightwell's own 2025 P&L margin.
- **40% framework-agreement conversion threshold** ("what would change our view"): no comparable B2B catering contract-conversion benchmark given for this stop-rule.
- **3% price increase vs. discount competitors:** no price-elasticity precedent cited for how much of the increase actually sticks.

## Premortem
1. **(Internal)** Central kitchen and delivery pilot both draw on existing store staff, ovens and management bandwidth at the busiest locations; no one owns the trade-off against core bakery production, so one gets starved at peak times without anyone noticing until results slip.
2. **(Internal/governance)** Catering payback lands in year 4; with only functional-level owners named and no sponsor above them, a leadership change or a soft year-1/2 result could get the initiative quietly descoped before the payback shows up.
3. **(External)** The 2023–2026 catering growth and the 10–14% delivery benchmarks both assume today's hybrid-work and delivery-market conditions hold; a reversal in office-attendance policy or a new delivery/catering entrant in the region is never tested as a downside scenario.

## What is good and must survive
- The recommendation is specific and actionable: euros, owners, and start dates for both funded moves.
- Catering revenue is triangulated two independent ways (bottom-up order×value, top-down workers×spend) landing in the same EUR 2.5–3.3m band, and the team explicitly tested and ruled out the "it's just return-to-office catch-up" alternative explanation (growth continued after attendance plateaued).
- Delivery's 12% base-case growth is checked against two regional chains' actual reported results (10–14%), not invented.
- "What would change our view" gives real, falsifiable kill criteria for both moves — rare and valuable.
- Headline arithmetic ties on recomputation: EUR 2.9m + 2.4m = 5.3m; 5.3/62 = 8.5%; (80−62)−5.3 = 12.7m gap; catering's year-by-year contribution-minus-fixed-cost math (0.16/0.32/0.45/0.51m) correctly crosses the EUR 1.2m investment in year 4.
- Alternatives (suburban stores, franchising, price, hours) are quantified and ruled out with reasons, not just funded moves presented in isolation.

## What "fixed" looks like
"We recommend revisiting the 2031 target, not the 14% margin floor. The floor is precisely what makes suburban stores (13.1% margin) and franchising (6–8% royalty) uneconomic today; lowering it would fund growth at structurally thinner margins rather than close the gap through options we already know work. Catering, delivery, pricing and longer hours together add at most EUR [X]m by 2031 even in the upside case — short of the EUR 80m target — so we recommend the board set a revised 2031 target of approximately EUR [Y]m rather than relax margin discipline to chase the original number."


## Files in work dir after run

- pr-03-input.md
