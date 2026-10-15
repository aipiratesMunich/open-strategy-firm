# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (2/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | NO | "Verdict:** Return" |
| No Blocker findings | NO | Finding #1 is listed with "Severity": "Blocker" ("rests on 'every option that needs a lower floor also carries the weakest evidence'") |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | NO | Finding 3 claims 'Reconstructing from 38→60 orders/day, EUR3.10 contribution/order, and 18 stores yields roughly EUR1.0m–1.7m... well under EUR2.4m', but per the reconciled figures (2.9+2.4=5.3, 5.3/62=8.5%, 80-62-5.3=12.7) the EUR2.4m figure does tie out, so the finding misstates/disputes a correct |
| Names what is good and must survive | yes | Section "What is good and must survive" lists concrete strengths: "The funding recommendation is concrete...", "Delivery's growth assumption is checked against two regional chains'...", etc. |
| Must not demand a named framework, more length, or more slides | yes | No finding asks for a specific framework, additional length, or more slides; fixes requested are reconciliations, sourcing, and clarifications. |
| Must not flag the stated uncertainty or the explicit assumptions as weaknesses | NO | Finding 3 treats the memo's explicit 12% growth assumption as a flaw: "is unclear: is '12% annual order growth' applied to orders, revenue, from what starting point?" despite the figures reconciling correctly per the calibration values. |
| Must not claim numbers do not tie (they do) | NO | Finding 2 asserts the EUR2.9m catering figure and derived EUR5.3m/EUR12.7m gap 'could be inflated by up to ~EUR1.7m' and Finding 3 says the EUR2.4m delivery figure 'yields roughly EUR1.0m–1.7m... well under EUR2.4m', contradicting the given tie-out (2.9+2.4=5.3, 5.3/62=8.5%, 80-62-5.3=12.7). |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell Bakeries 2027 growth memo, gate 3

**Verdict:** Return
**In one line:** The board's second decision — revisit the revenue target or the margin floor — is recommended on a non-sequitur, and two of the three headline revenue numbers that size the gap driving that decision don't survive a two-minute rebuild from the memo's own data.

**Question the draft must answer:** Which growth moves should the board fund in the 2027 budget, and should it revisit the 2031 revenue target or the margin floor? (given, in the "Decisions needed" line)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the target, not the floor.

The funding recommendation is specific and well-supported. The target-vs-floor recommendation — equally important, since it's the explicit second decision on the agenda — is not.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician / Decision Maker | "Why not suburban..." / "What it adds up to" (¶4–5) | The recommendation to revisit the target rather than the floor rests on "every option that needs a lower floor also carries the weakest evidence" — but the evidence shown for suburban stores and franchising (2025 P&L margin, three real franchise offers) is solid, not weak. The memo never compares what lowering the floor would actually cost against what lowering the target would cost. | The CEO carries a recommendation into the board meeting on one of only two decisions requested, with reasoning a sharp board member will dismantle in the first exchange, and the board may pick the wrong lever blind to its true cost. | Replace the "weakest evidence" line with an actual comparison: the margin/profit cost of relaxing the floor (e.g., to 13%, enough to fund suburban stores) versus the strategic cost of cutting EUR 12.7m from the 2031 target. Recommend on that basis. |
| 2 | Major | Skeptical CFO / Evidence Auditor | "Why catering" (¶2) | The catering trajectory (EUR 1.6m in 2027 → implied ~EUR 2.9m in 2031) is never reconciled against today's business. 9,000 annual orders × the memo's own EUR 190 median order value ≈ EUR 1.7m — already close to the year-1 forecast of EUR 1.6m. If 2.9m is a total rather than an incremental figure, "EUR 5.3m additional revenue" and the "EUR 12.7m gap" are overstated. ("Total instead of incremental" is a named, common business-case error for exactly this reason.) | The size of the prize used to justify the investment and to size the gap feeding decision 2 could be inflated by up to ~EUR 1.7m. | State explicitly whether the catering figures are incremental to today's run-rate or totals, and show the reconciliation against the implied current run-rate. |
| 3 | Major | Skeptical CFO | "Why a delivery pilot" (¶3) | The EUR 2.4m-by-2031 figure can't be rebuilt from the inputs given. Reconstructing from 38→60 orders/day, EUR 3.10 contribution/order, and 18 stores yields roughly EUR 1.0m–1.7m depending on timing — well under EUR 2.4m. The base is also unclear: is "12% annual order growth" applied to orders, revenue, from what starting point? | The second-largest number in the gap calculation may be materially overstated, again distorting decision 2. | Show the calculation from per-store orders/day and contribution to the EUR 2.4m headline, stating the base the 12% growth is applied to. |
| 4 | Major | Evidence Auditor | "Why catering" (¶2) | No outside-view benchmark for catering, unlike delivery (which cites two regional chains' actual 10–14% first-three-year growth). | The board has no way to judge whether near-tripling orders in three years, continuing at 24% y/y, is a credible base case or an extrapolation of an unsustainable early curve. | Add a comparable benchmark for office-catering growth, or state plainly that none is available. |
| 5 | Major | Skeptical CFO | "What it adds up to" (¶5) | The EUR 62m "today" baseline is treated as flat through 2031 with no stated assumption about the core business's own trajectory. | If the base business grows or shrinks on its own, the EUR 12.7m gap — the number driving the target-vs-floor call — is wrong. | State the assumed organic growth/decline of the EUR 62m base to 2031. |
| 6 | Major | Premortem (internal) | Whole memo | No commercial/sales owner is named for catering, even though the memo notes growth so far happened "without any sales effort." The only named owner (Head of Operations) covers kitchen production, not demand generation. | If reaching EUR 2.9m requires active account management (the "framework agreements" mentioned later need someone to go sign them), growth plateaus near today's organic rate and the payback case fails. | Name who owns commercial/sales execution for catering, or state why operations alone is sufficient. |
| 7 | Minor | Evidence Auditor | "Why catering" (¶2) | The 12 interviewed office managers' selection method and the total number of office-catering accounts aren't stated, so the EUR 190 median and "9 of 12" finding can't be judged for representativeness. | — | State how many total office-catering accounts exist and how the 12 were chosen. |
| 8 | Minor | Evidence Auditor | "Why catering" (¶2) | The EUR 0.35m central-kitchen fixed-cost figure (four staff + rent) has no stated source. | — | Add the basis (budget quote, comparable site cost). |
| 9 | Minor | Logician | "Why a delivery pilot" / "What would change our view" | Two different order-per-day thresholds appear (60 to scale, 50 to kill) with the gap between them unexplained. | — | Clarify that 50–60 is a deliberate hold zone, not an inconsistency. |
| 10 | Minor | Logician | "What would change our view" | The 40% framework-agreement threshold for catering isn't tied to any take-up rate used in the EUR 2.9m build. | — | State the take-up assumption behind the base case and how 40% relates to it. |
| 11 | Minor | Outsider | "Why catering" (¶2) | Catering growth decelerates sharply year to year (31%→19%→8%→~7%) with no stated reason. | — | State what caps growth after year two (e.g., kitchen capacity), so the board can judge whether a bigger kitchen is worth evaluating. |

## Numbers that do not tie
None found as literal restatements. Findings 2 and 3 are the reviewer's own recalculations from the memo's stated inputs, not two stated values of the same figure — flagged as Major per the calibration rule, not Blocker, since neither recalculation on its own flips the funding recommendation.

## Missing outside view
- Catering growth/take-up: no comparable company or market benchmark cited (see finding 4).
- Delivery: present and good — two regional chains' actual 10–14% first-three-year growth, cited by name of source type and date.

## Premortem
1. **Internal — no demand-generation owner:** Office catering grew "without any sales effort." Scaling to EUR 2.9m likely needs active account management, but the only named owner (Head of Operations) runs the kitchen, not sales. Growth stalls near today's organic level.
2. **Internal — capacity stretch on the named owner:** The Head of Operations already runs day-to-day store operations and now also owns a new central kitchen launch by April 2027, with no stated bandwidth or dedicated catering GM.
3. **External — platform economics:** The EUR 3.10/order delivery contribution is stated "after platform fees." A platform fee increase or algorithm change erodes the unit economics the entire rollout decision rests on, and the memo doesn't say what contribution the pilot needs to stay above.

## What is good and must survive
- The funding recommendation is concrete: amounts, owners, start dates for both moves.
- The memo states the EUR 12.7m shortfall to the 2031 target plainly instead of hiding it, and surfaces the target-vs-floor choice as a real decision rather than papering over it.
- Delivery's growth assumption is checked against two regional chains' actual results — real outside-view discipline.
- Catering's base case is triangulated two ways (bottom-up and top-down) landing in the same EUR 2.5m–3.3m range — good practice, worth extending to the other weak spots above.
- Suburban stores and franchising are rejected with sourced, falsifiable data (2025 P&L, three real franchise offers), not prose hand-waving.
- "What would change our view" gives concrete, falsifiable kill criteria — rare and valuable; keep it, just tie the numbers in it back to the model (findings 9, 10).
- The secondary levers (price, hours) are reported honestly as closing "less than a quarter of the gap" rather than oversold.

## What "fixed" looks like
"Fund the catering unit and delivery pilot as scoped below; both are reversible, and the catering orders data and delivery outside-view benchmark are the strongest evidence in this memo. Together they add an estimated EUR X–Y of incremental revenue by 2031 [reconciled against today's catering run-rate and the delivery per-store build], leaving a gap of roughly EUR Z to the EUR 80m target. We recommend closing that gap by [revisiting the target / the floor], because lowering the floor to fund suburban stores and franchising would cost EUR [A] in margin, against a strategic cost of EUR [B] from carrying a lower 2031 target — and recommend accordingly."


## Files in work dir after run

- pr-03-input.md
