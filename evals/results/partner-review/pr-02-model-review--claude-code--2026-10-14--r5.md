# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 with the cell reference and D3 with both values | yes | Finding #2: 'Calc!D5:G5 ... uses =prev*1.18 (hard-coded) ... instead of orders(row3) × AOV(row4)'; Finding #1 and #3 show slide revenue 6.4m vs model 4.10m/3.33m and slide NPV 2.1m vs model 4.77m/2.69m |
| Notices the hidden sheet (D2) | yes | Finding #6: 'Hidden sheet "Old" (Calc!B5*1.05) ... A hidden, stale "v1" revenue calc is still sitting in the workbook' |
| Finds D6 (sign of the investment) or explains why the model NPV cannot be trusted | yes | Finding #3: 'The EUR 1.2m kitchen investment is entered as positive and then added to contribution ... instead of subtracted — it's modeled as a cash inflow. This pushes Outputs!B2 NPV to ≈EUR 4.77m' |
| Finds D4 or D5 | yes | Finding #5: 'Single scenario only. No sensitivity on the 12% p.a. order-growth input ... or the 9% discount rate, and no downside case.' |
| Recomputes at least one key output independently and reports the result | yes | 'The model's own revenue formula produces EUR 4.10m for 2031' and 'Outputs!B2 NPV to ≈EUR 4.77m as the file actually computes' and 'Calc!G3 = ~15,861' |
| Uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings) | yes | Specific cell references throughout: 'Calc!G5 / Outputs!B1', 'Calc!D5:G5', 'Calc!C12, Calc!row13', 'Inputs!row3' |
| Must not claim errors in cells that are correct (false alarm on the Inputs sheet constants) | yes | 'Inputs sheet cleanly separates each driver with value, unit, and source — the hard-coded constants belong there, and that discipline should stay' — Inputs sheet is praised, not flagged as erroneous |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

All confirmed against the actual workbook formulas. Here's the review.

# Partner review: Brightwell catering business case (pr-02-model.xlsx + pr-02-slide.md), gate 3

**Verdict:** Return
**In one line:** None of the three headline numbers on the slide (EUR 6.4m revenue, EUR 2.1m NPV, >20,000 orders) actually come out of the model when you recompute its own formulas — there's a revenue-formula override that silently breaks mid-forecast, an investment sign error that inflates NPV, and a "payback in year 3" claim with no calculation anywhere behind it.

**Question the draft must answer:** Should Brightwell spend EUR 1.2m on a catering kitchen, and what return (revenue, NPV, payback) does that generate by 2031? (reconstructed from the slide's headline, not stated explicitly)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, orders more than double to 20,000+, payback in year 3.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Evidence Auditor | Calc!G5 / Outputs!B1 vs. slide title | The model's own revenue formula produces EUR 4.10m for 2031, not EUR 6.4m. No version of the model (buggy or corrected) ties to 6.4m. | CFO signs off on a revenue number ~2.3–3.1m higher than anything the workbook computes. | Trace the headline number back to a model cell; update the slide to whatever Outputs!B1 actually says once the model is fixed. |
| 2 | Blocker | Evidence Auditor | Calc!D5:G5 | Revenue formula uses `=prev*1.18` (hard-coded) from 2028 onward instead of `orders(row3) × AOV(row4)` as used in B5/C5. This silently decouples revenue growth (18%) from the 12% order-growth input. The slide's ">20,000 orders" figure only reconciles if you back-solve the broken 18%-revenue line ÷ EUR 210 (≈19,543) — the model's actual Orders row (Calc!row3) only reaches ~15,861 by 2031. Two headline figures were pulled from two different, contradictory growth assumptions in the same file. | Order and revenue figures on the slide don't even agree with each other, let alone with the model. | Delete the `*1.18` override; drive every year of revenue off row3 × row4, as B5/C5 already do. Regenerate both the orders and revenue slide figures from that single consistent line. |
| 3 | Blocker | Skeptical CFO | Calc!C12, Calc!row13 | The EUR 1.2m kitchen investment is entered as **positive** and then **added** to contribution (`=C6+C12`) instead of subtracted — it's modeled as a cash inflow. This pushes Outputs!B2 NPV to ≈EUR 4.77m as the file actually computes, not EUR 2.1m. A guessed correction (subtract it, move it to 2026 pre-ramp) lands near EUR 2.69m — closer to the slide, but still not an exact tie and only reached by assuming what was intended. | CFO approves a return figure built on an investment that was added to cash flow instead of subtracted — the real economics are unknown until this is fixed and re-tied. | Fix the sign, decide the correct timing (likely 2026, before order ramp-up), rebuild Outputs!B2 from the corrected cash flow, and confirm the slide matches the new output — don't just restate 2.1m. |
| 4 | Blocker | Evidence Auditor | Slide bullet "Payback in year 3" | No cumulative cash flow or payback calculation exists anywhere in Calc or Outputs. The claim is asserted, not computed. Under a sign/timing-corrected cash flow, cumulative CF turns positive in **2027 (year 2)**, not year 3. | A specific, checkable-sounding number is presented to the CFO with zero model support; if challenged, there's nothing to show. | Add an explicit cumulative-cash-flow/payback row to the workbook and set the slide claim to whatever that row actually computes. |
| 5 | Major | Model red flags | Inputs sheet / whole model | Single scenario only. No sensitivity on the 12% p.a. order-growth input (an unbenchmarked "management estimate" compounded over 5 years) or the 9% discount rate, and no downside case. | CFO has no visibility into how fragile the NPV is to the one driver that's pure judgment. | Add a sensitivity table (e.g. ±3pp growth, ±1–2pp discount rate) and a downside scenario before this goes up. |
| 6 | Major | Outsider | Hidden sheet "Old" (`Calc!B5*1.05`) | A hidden, stale "v1" revenue calc is still sitting in the workbook that's about to go to the CFO. Not wired into live outputs, but exactly the kind of thing that surfaces in diligence and erodes trust in the rest of the file. | Reviewer/CFO who unhides sheets finds a leftover, unexplained alternate number and questions the whole model's hygiene. | Delete the Old sheet (or keep version history outside the live model) before sending. |
| 7 | Minor | Evidence Auditor | Inputs!row3 ("Order growth p.a.", source: "Management estimate") | 12% p.a. compounding for 5 years has no external comparable (contract/B2B catering market growth) cited to sanity-check it. | Minor — doesn't make a stated number wrong, but it's the single biggest judgment call in the model and it's unvalidated. | Add one comparable data point, or explicitly flag this as unvalidated management judgment. |

## Numbers that do not tie

| Number | Slide | Model | Difference |
|---|---|---|---|
| Revenue 2031 | EUR 6.4m | Outputs!B1 = EUR 4.10m (as modeled, with bug); EUR 3.33m if orders-driven formula is used consistently throughout | off by EUR 2.3–3.1m |
| NPV | EUR 2.1m | Outputs!B2 = EUR 4.77m (as modeled, sign bug); ≈EUR 2.69m under a guessed sign/timing fix | off by EUR 2.7m (as modeled) / ~0.6m (best-guess fix) |
| Orders 2031 | "over 20,000" | Calc!G3 = ~15,861 | off by 4,100+ |
| Payback | "year 3" | not computed anywhere; ≈year 2 under corrected cash flows | unsupported claim |

## Missing outside view
- **12% p.a. order growth**: no comparable B2B/contract-catering growth rate cited to validate 5 years of sustained compounding — currently pure management judgment.
- **32% contribution margin held flat at ~1.76x order volume**: no benchmark or capacity check on whether one kitchen sustains that margin at near-double throughput.

## Premortem
1. The 12% growth assumption (unbenchmarked) undershoots. Even the best-guess *corrected* NPV (~2.7m) isn't a large cushion over a 1.2m investment — a modest growth miss could flip the case negative, and nobody will have seen that because there's no sensitivity table.
2. Contribution margin is modeled as flat at 32% regardless of volume, but pushing a single kitchen to ~1.8x order volume plausibly requires extra shifts/labor/equipment that compress margin — there's no capacity or opex-scaling check anywhere in the model.
3. The capex line has a sign error and no clear timing logic in the version the CFO was about to see — if the same lack of scrutiny extends to the actual kitchen build (delivery delay, cost overrun, common for build-outs), payback slips further right exactly when the real NPV cushion is thin.

## What is good and must survive
- The slide headline is a genuine assertion with a number and a "so what," not a label — keep that format once the numbers are fixed.
- Inputs sheet cleanly separates each driver with value, unit, and source — the hard-coded constants belong there, and that discipline should stay.
- Average order value (EUR 210) is correctly held flat and consistently referenced everywhere — this is the one headline figure that actually ties between slide and model.
- The discount rate is pulled from Inputs into the NPV formula rather than hard-coded elsewhere — correct practice, don't regress it when fixing the other bugs.

## What "fixed" looks like
"Corporate catering revenue grows from EUR 1.9m in 2026 to EUR 3.3m in 2031, as order volume rises from 9,000 to ~15,900 at a stable EUR 210 average order value, on a 12% p.a. growth assumption we have not yet benchmarked against comparable contract-catering growth. After correcting the kitchen investment's sign and timing (EUR 1.2m spent upfront in 2026), the business case returns approximately EUR 2.7m NPV at a 9% discount rate, with payback in year 2 — pending a sensitivity check on the growth rate and a capacity check on whether a single kitchen sustains margin at nearly double current volume." (Treat the 2.7m/year-2 figures as an illustrative reconstruction, not a finished number — the team still needs to decide and rebuild the actual correct formula logic.)


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
