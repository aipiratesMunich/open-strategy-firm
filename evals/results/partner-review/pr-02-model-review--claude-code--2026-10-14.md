# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 with cell reference and D3 with both values | yes | Finding #2: 'Calc!D5:G5 vs. Outputs!B1 vs. slide ... hard-coded to grow at 18% (`=prev*1.18`)'; Numbers table lists slide Revenue 2031 EUR 6.4m and NPV EUR 2.1m vs model figures |
| Notices the hidden sheet (D2) | yes | Finding #7: '"Old" sheet (hidden) — A hidden sheet holds a prior revenue calc ... not referenced by any output.' |
| Finds D6 (sign of investment) or explains why NPV can't be trusted | yes | Finding #1: 'Kitchen investment (EUR 1.2m) is entered as a positive number and then added to contribution in the net cash flow row, instead of subtracted.' |
| Finds D4 or D5 | NO | The 'Missing outside view' section flags a missing benchmark for the 12% order-growth assumption and missing margin-compression sensitivity, but never states that the two most uncertain drivers (order growth, AOV) lack sensitivity testing (D4), nor that the model has only one scenario with no downsi |
| Recomputes at least one key output independently and reports result | yes | 'orders reach 15,861 by 2031' and 'If revenue is properly driven by orders × AOV at the stated 12%, it is EUR 3.33m' and NPV recomputed to '~EUR 2.56m' / '~EUR 2.69m' |
| Uses model-scan/formula inspection (cell references in findings) | yes | References like 'Calc!C12', 'Calc!D5:G5', 'Outputs!B1', 'Outputs!B2', 'NPV(...,C13:G13)' |
| Must not claim errors in correct Inputs-sheet constants | yes | 'most of the model genuinely is input-driven (orders, AOV, margin, discount rate all flow from the Inputs sheet correctly for most periods)' — no false alarms raised against Inputs constants |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them.

# Partner review: Brightwell catering business case (pr-02-model.xlsx + pr-02-slide.md), gate 3

**Verdict:** Return
**In one line:** Every headline number on the slide — orders, revenue, NPV — fails to tie to the model, and the model itself has a sign error that makes the investment look like a cash inflow.

**Question the draft must answer:** Should Brightwell invest EUR 1.2m in a corporate catering kitchen? (reconstructed from slide)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO / Model check 1 | Calc!C12 | Kitchen investment (EUR 1.2m) is entered as a **positive** number and then *added* to contribution in the net cash flow row, instead of subtracted. The model literally computes a higher return because of the capex than without it. | A CFO who traces the formula chain finds the investment is treated as income. Anyone who audits this loses confidence in the whole case instantly; it's a one-line smoking gun. | Enter investment as a negative outflow in Calc!C12 (or SUM it as `-Inputs!$B$6`), and place it in the year the cash actually leaves (see #4). |
| 2 | Blocker | Logician / Model check 14 | Calc!D5:G5 vs. Outputs!B1 vs. slide | Revenue for 2028–2031 is hard-coded to grow at **18%** (`=prev*1.18`) instead of being driven by orders × AOV, even though orders (row 3) keep growing at the input-driven 12%. The model's own live output for Revenue 2031 is **EUR 4.10m**, not the EUR 6.4m on the slide. If revenue is properly driven by orders × AOV at the stated 12%, it is **EUR 3.33m**. Under neither interpretation does the model support 6.4m. | CFO opens Outputs!B1, sees 4.1m, and the deck's headline number is unexplained and wrong by 36–92%. | Remove the hard-coded 1.18 factor; drive revenue as `=orders*AOV` in every period. Decide whether 12% (input) or some other rate is the intended growth assumption, and re-source it. Re-tie the slide to the recalculated Outputs!B1. |
| 3 | Blocker | Decision Maker | Outputs!B2 vs. slide | Live NPV formula, run as built (with bug #1 intact), returns **EUR 4.77m** — more than double the EUR 2.1m quoted on the slide. Fixing only the sign error brings it to ~EUR 2.56m; fixing both the sign error and the revenue bug and placing capex at t0 (2026) gives ~EUR 2.69m. None of these routes land on 2.1m. There is no traceable path from the model to the slide's number. | The CFO cannot verify the 2.1m from the file at all — it doesn't correspond to the model as built, nor to any obvious "corrected" version of it. The investment case rests on a number nobody can reproduce. | Recompute NPV after fixing #1 and #2, state which cash-flow timing convention is used (see #4), and show the calculation path from Outputs!B2 to the slide. |
| 4 | Major | Logician / Model check 4 | Calc!C12 | Investment is booked in **2027**, not 2026, while 2026 cash flow is excluded from the NPV range (`NPV(...,C13:G13)` starts at 2027). This means the "first" year of the model (2026) carries neither the capex nor is counted as a benefit period — an undocumented timing convention that materially affects both NPV and any payback calculation. | Payback and NPV both shift depending on when the capex actually hits, and currently nobody has decided or disclosed this. | State explicitly when the kitchen spend occurs (presumably before or at the start of 2026 ramp-up) and build the cash-flow timeline, discounting, and NPV range consistently around that date. |
| 5 | Major | Evidence Auditor | Slide bullet "Orders grow from 9,000 in 2026 to over 20,000 in 2031" | At the model's own input growth rate (12% p.a.), orders reach **15,861** by 2031, not "over 20,000." Reaching ~20,000 requires ~17.3% p.a. growth — suspiciously close to the hard-coded 18% used (wrongly) on the *revenue* row, suggesting the order count on the slide was derived from the same buggy growth rate rather than the 12% input. | The single most-quoted growth stat on the slide overstates the model's own assumption by ~30%, and appears to come from the same planted error as finding #2. | Recompute orders for 2031 from the 12% input (15,861) or get the business owner to confirm and re-source an 18% growth case explicitly, in the Inputs sheet — not hard-coded in a calc cell. |
| 6 | Major | Evidence Auditor / Model check 7 | Slide bullet "Payback in year 3" | No payback calculation exists anywhere in the model. Calc and Outputs have only a revenue row and an NPV output — no cumulative cash-flow or payback row. | A specific, confident-sounding claim ("year 3") has zero support in the file; if asked to show it, the team cannot. | Add a cumulative net cash flow row to Calc and derive payback period from it explicitly, using the corrected (non-buggy) cash flows. |
| 7 | Minor | Evidence Auditor / Model check 10 | "Old" sheet (hidden) | A hidden sheet holds a prior revenue calc (`=Calc!B5*1.05`, labeled "v1, lower case") not referenced by any output. Not functionally wrong, but it's exactly the kind of stale hidden content that confuses a later auditor or gets accidentally re-linked. | Low risk today, but a governance/hygiene flag for a model about to be handed to Finance. | Delete the hidden sheet or move it to a clearly labeled version-history file outside the live workbook. |

## Numbers that do not tie

| Number | Location A (slide) | Location B (model) | Difference |
|---|---|---|---|
| Orders, 2031 | "over 20,000" | 15,861 (at stated 12% input growth) | ~+26% overstated |
| Revenue, 2031 | EUR 6.4m | EUR 4.10m (model as built, buggy) / EUR 3.33m (orders × AOV, corrected) | +56% / +92% overstated |
| NPV | EUR 2.1m | EUR 4.77m (model as built, buggy) | Model's live output is more than double the slide; neither a "sign-fix only" (~2.56m) nor "fully corrected" (~2.69m) recomputation reproduces 2.1m exactly |
| Payback | "year 3" | Not computed anywhere in the model | No basis found |

## Missing outside view

- Order growth of 12% p.a. (input) — and the ~17–18% implied by the slide/hard-coded formula — has no comparable-company or market benchmark attached in the Inputs sheet ("Management estimate" only). Before this goes to the CFO, get a reference point (prior years' actual growth, a comparable corporate-catering rollout) to show which growth case is realistic.
- Contribution margin of 32% is sourced to "Catering P&L 2026" — fine as a base, but there's no sensitivity shown for margin compression as volume scales (kitchen utilization, staffing ramp).

## Premortem

1. The business case was approved on a 6.4m/2.1m story; actual results track the 12%-growth, orders×AOV reality (~3.3m revenue by 2031). Two years in, the unit is "underperforming the plan" by 40%+ even though nothing changed — the plan was just never achievable as modeled.
2. The kitchen capex hits as a real cash outflow in year 1, but because the model treated it as an inflow, nobody budgeted for the liquidity gap. Payback, never actually computed, turns out to be materially later than "year 3," straining working capital.
3. Kitchen capacity (a 1.2m build) was never checked against the ~16,000–20,000 order volumes being planned for — if the kitchen can't physically produce at that scale, growth stalls on operational grounds regardless of demand, and nobody flagged this because the model has no capacity/utilization check.

## What is good and must survive

- The model's structure (Inputs / Calc / Outputs separation) is sound in principle, and most of the model genuinely is input-driven (orders, AOV, margin, discount rate all flow from the Inputs sheet correctly for most periods).
- The slide itself is commendably compact and quotes its source version ("Brightwell catering business case model v3") — that sourcing discipline should stay.

## What "fixed" looks like

Corporate catering is expected to reach approximately EUR 3.3m revenue by 2031 (9,000 orders in 2026 growing at a management-estimated 12% p.a. to ~15,900 orders, average order value stable at EUR 210), returning an NPV of roughly EUR 2.6–2.7m against a EUR 1.2m kitchen investment once that investment is correctly modeled as a cash outflow at the start of the project. [Team to re-run the corrected model and confirm the exact NPV and payback year — the figures above are an independent recomputation for illustration, not a substitute for the team's own corrected file.] If the business intends a more aggressive ~18% growth case, that assumption needs its own line in the Inputs sheet with a stated source, not a hard-coded multiplier buried in the revenue row.


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
