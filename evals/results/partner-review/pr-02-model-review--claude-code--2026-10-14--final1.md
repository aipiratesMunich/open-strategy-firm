# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is **Return**. | yes | "**Verdict:** Return" |
| Must: finds D1 with the cell reference and D3 with both values. | yes | Finding #1 cites `Calc!D5:G5` for the hardcoded `=prior*1.18`; 'Numbers that do not tie' table lists slide EUR 6.4m vs model EUR 4.10m/3.33m revenue and slide EUR 2.1m vs model EUR 4.77m NPV. |
| Must: notices the hidden sheet (D2). | yes | Finding #10: "`Old` hidden sheet ... A hidden sheet holds a stray formula from a prior version" |
| Must: finds D6 (sign of the investment) or explains why the model NPV cannot be trusted. | yes | Finding #2: "`Inputs!B6` (EUR 1,200,000 kitchen investment) is stored as a positive number and *added* into net cash flow (`C13=C6+C12`)" |
| Must: finds D4 or D5. | yes | Finding #7 'No sensitivity or break-even analysis...' and Finding #8 'Only one case is shown; no coherent downside...' |
| Must: recomputes at least one key output independently and reports the result. | yes | "a correctly-built model would show EUR 3.3m revenue, ~EUR 2.2m NPV and payback in year 2" |
| Must: uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings). | yes | Cites `Calc!D5:G5`, `Calc!C12`/`C13`, `Outputs!B1`, `Outputs!B2`, `Calc!G3`, `Inputs!B3`, `Inputs!B6`. |
| Must not: claim errors in cells that are correct (false alarm on the Inputs sheet constants). | yes | Finding #9 only flags missing sourcing/evidence for Inputs!B3 ('sourced only as Management estimate'), not that the value itself is incorrect; no Inputs constants are claimed to be wrong. |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

I checked the model line by line and recomputed every key output independently. This one has real problems — three of the four numbers on the slide don't come from the model, and the model itself has two structural bugs. Full review below.

# Partner review: Brightwell catering business case (pr-02-slide.md + pr-02-model.xlsx), gate 3

**Verdict:** Return
**In one line:** None of the slide's three headline numbers tie to the model — as built, the model would show EUR 4.1m revenue and EUR 4.8m NPV (because the EUR 1.2m investment is coded as a cash *inflow*), a correctly-built model would show EUR 3.3m revenue, ~EUR 2.2m NPV and payback in year 2, and "payback in year 3" is quoted from a calculation that doesn't exist anywhere in the workbook.

**Question the draft must answer:** Should Brightwell commit EUR 1.2m to a kitchen investment in the catering unit? (reconstructed, assumption)
**Answer the draft gives:** Yes — it pays back in year 3 and returns EUR 2.1m NPV on EUR 6.4m of 2031 revenue.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO (model red flags #1, #3) | `Calc!D5:G5` | Revenue formula hard-codes `=prior*1.18` for 2028–2031, replacing the Orders×AOV build used in 2026–2027 (`=B3*B4`, `=C3*C4`). The 18% appears nowhere as an input. | Revenue from 2028 on is driven by an invented growth rate, not by the 12% order-growth input or by the "AOV stable at EUR 210" bullet on the slide — by 2031 implied AOV is EUR 259, not EUR 210. Both headline claims misdescribe how the number was built. | Make Revenue = Orders × AOV for every year with one formula across the row; if 18% growth is actually intended, put it on the Inputs sheet and apply it to Orders, not bolt it onto Revenue. |
| 2 | Blocker | Skeptical CFO (model red flags #1, #11) | `Calc!C12`/`C13` | `Inputs!B6` (EUR 1,200,000 kitchen investment) is stored as a positive number and *added* into net cash flow (`C13=C6+C12`), so the capex is modeled as a cash inflow. | As literally built, `Outputs!B2` computes NPV ≈ EUR 4.77m — more than double the EUR 2.1m on the slide — because the cost of the investment increases cash instead of reducing it. | Enter the investment as −1,200,000 (or subtract it in the cash-flow formula) and re-run NPV. |
| 3 | Blocker | Decision Maker / Evidence Auditor (checklist #9, #13; model red flags #14) | Slide bullet "orders... over 20,000 in 2031" vs. `Calc!G3` | The model's own Orders row (the only growth input on file, 12% p.a.) reaches 15,861 by 2031, not "over 20,000." >20,000 matches an 18% CAGR that isn't an input anywhere and isn't in the Outputs sheet — it has no cell behind it at all. | A director asking to see the orders build gets a number that cannot be reproduced from the file. | Show 15,861 orders (and fix revenue to match), or add an evidenced 18% orders input and update every dependent figure. |
| 4 | Blocker | Skeptical CFO / Decision Maker (checklist #13; model red flags #14) | Slide title "EUR 6.4m revenue by 2031" vs. `Outputs!B1` | `Outputs!B1` computes EUR 4.10m as built; a corrected, internally consistent version (Orders × stable AOV at 12% growth) computes EUR 3.33m. EUR 6.4m matches neither and implies ~28% p.a. growth that is not an input anywhere. | The single number in the slide title cannot be reproduced from the model under any combination of its own assumptions. | Recompute revenue from the corrected driver chain and put that number (≈EUR 3.3m at the evidenced growth rate) on the slide. |
| 5 | Blocker | Skeptical CFO (checklist #13; model red flags #14) | Slide "Payback in year 3" | No payback calculation exists anywhere in the workbook (not on `Calc`, not on `Outputs`). Recomputing cumulative cash flow independently — investment correctly signed — shows cumulative cash turns positive in 2028, one year after the 2027 investment: payback in year 2, under both the as-built and the corrected revenue build. | The one metric with no formula behind it is also the one that's off by a year once you actually calculate it. | Add a payback line to Outputs (cumulative net cash flow by year) and quote the year it actually crosses zero. |
| 6 | Major | Logician / CFO (business case common mistake "total instead of incremental") | `Calc` rows 5–13 | Net cash flow feeding NPV is 100% of catering contribution, including the EUR 1.89m / 9,000-order base that already exists in 2026 — there is no "without the investment" counterfactual. | If the existing business continues regardless of the new kitchen, the case is overstated by the full base-case contribution, not just the increment the kitchen enables. | State what happens to the 2026-level business without the investment, and rebuild cash flow as (with) minus (without). |
| 7 | Major | Skeptical CFO (model red flags #12; business case step 6) | Workbook-wide | No sensitivity or break-even analysis on growth, AOV, margin or discount rate — despite revenue already swinging >50% between the 12% and 18% growth rates latent in this one file. | A board member asking "what if growth is 8%?" gets no answer. | Add a one-way sensitivity table on order growth, AOV and margin, with the break-even growth rate at which NPV = 0. |
| 8 | Major | Skeptical CFO (model red flags #13; business case step 5) | Workbook-wide | Only one case is shown; no coherent downside (e.g. slower ramp, competitor response) or upside. | The board can't see what has to go wrong for the investment to lose money. | Define a down case tied to a specific risk and an up case, each a coherent assumption set, not a flat haircut. |
| 9 | Major | Evidence Auditor / CFO (checklist #14; model red flags #6) | `Inputs!B3` | 12% order growth p.a. (and the buried 18%) is sourced only as "Management estimate" — no comparable catering/food-service scale-up is cited for five straight years of double-digit compounding. | A skeptical CFO will ask what comparable business sustained this; without an answer the base case reads as hoped-for. | Cite an outside comparable or industry growth benchmark, or lower the base case to what's evidenced. |
| 10 | Minor | CFO (model red flags #10) | `Old` hidden sheet | A hidden sheet holds a stray formula from a prior version (`=Calc!B5*1.05`); doesn't feed outputs, but its undisclosed presence invites doubt about which numbers are current, especially since the slide cites "model v3." | Low now, but the next analyst to open the file risks reusing stale logic. | Delete the `Old` sheet before this leaves the team. |

## Numbers that do not tie

| Number | Slide | Model | Difference |
|---|---|---|---|
| Revenue 2031 | EUR 6.4m | `Outputs!B1` as built: EUR 4.10m; corrected (consistent 12% growth): EUR 3.33m | EUR 2.3–3.1m too high |
| Orders 2031 | "over 20,000" | `Calc!G3`: 15,861 | ~4,700+ too high, and not computed in `Outputs` at all |
| NPV | EUR 2.1m | `Outputs!B2` as built (sign bug): EUR 4.77m | EUR 2.65m too high |
| Payback | Year 3 | Not calculated anywhere; independently recomputed: year 2 (2028) | 1 year off, and no formula exists |

## Missing outside view

- Order growth (12% input / 18% buried in the formula): no comparable corporate-catering or food-service scale-up cited for sustaining this for five years.
- Contribution margin (32% flat while volume grows 1.76–2.3x): no evidence margin holds as the kitchen scales — operating leverage or dilution from overtime/waste/delivery radius is untested.

## Premortem

1. Order growth comes in at a more typical food-service rate (mid-single digits) instead of 12–18%, pushing payback well past year 3 and roughly halving NPV — not addressed, since no sensitivity or down case exists.
2. The 32% contribution margin compresses as volume scales past the new kitchen's efficient capacity — not addressed; margin is a flat input for all five years.
3. The existing EUR 1.89m / 9,000-order catering base was going to continue regardless of the new kitchen, so the true incremental return is far below what's shown — not addressed; no counterfactual is modeled.

## What is good and must survive

- Inputs/Calc/Outputs separation is sound; almost every assumption lives on one clearly labeled, sourced Inputs sheet.
- Orders and AOV rows are properly driver-based (volume × price) for 2026–2027 — exactly the right pattern, just not carried through to 2031.
- The slide uses an action title stating an actual numeric conclusion, not a label, and cites a named, versioned source.
- Discount rate is sourced to Group finance, not invented.

## What "fixed" looks like

"Brightwell's corporate catering kitchen investment (EUR 1.2m) is projected to return approximately EUR 2.2m NPV at a 9% discount rate, with payback in 2028 (year 2), on revenue growing from EUR 1.9m in 2026 to approximately EUR 3.3m in 2031 as orders grow from 9,000 to roughly 15,900 at a stated 12% p.a. — a rate not yet benchmarked against comparable catering scale-ups. The base case excludes a sensitivity on growth and margin and does not yet net out what the existing catering business would do without this investment; both are needed before this goes to the CFO."


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
