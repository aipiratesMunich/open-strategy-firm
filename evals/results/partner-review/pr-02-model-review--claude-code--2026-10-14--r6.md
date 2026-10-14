# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 with cell reference and D3 with both values | yes | Finding #2: 'Calc!D5:G5 ... Revenue for 2028-2031 is hardcoded as `=prev*1.18`'; Numbers table lists both 2031 revenue (slide 6.4m vs model) and NPV (slide 2.1m vs model) |
| Notices the hidden sheet (D2) | yes | Finding #9: "Sheet 'Old' (hidden) ... A hidden sheet with a stale formula" |
| Finds D6 or explains why NPV cannot be trusted | yes | Finding #3: 'the EUR 1.2m kitchen investment is stored positive and `C13 = C6+C12` adds it ... instead of subtracting it as an outflow' |
| Finds D4 or D5 | yes | Finding #6: 'Only one case is modeled. Order growth and discount rate ... are never flexed; no break-even growth rate or order volume is shown.' |
| Recomputes at least one key output independently and reports result | yes | 'Recalculating Outputs!B2 exactly as written gives NPV ≈ EUR 4.77m' |
| Uses model-scan helper or equivalent inspection of formulas (cell references in findings) | yes | Cites Calc!D5:G5, Inputs!B6, Calc!C12-C13, Calc!G3, Outputs!B2 throughout findings |
| Must not claim errors in correct cells (false alarm on Inputs sheet constants) | yes | 'The Inputs sheet is clean: one driver per row ... no hardcoded numbers in formulas — this is the right structure and should stay.' |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

Leaving that empty folder — not worth another prompt. Here's the full review:

# Partner review: Brightwell catering business case (model + slide), gate 3

**Verdict:** Return
**In one line:** The model's own formulas, recalculated independently, produce a 2031 revenue of ~EUR 4.1m and an NPV of ~EUR 4.8m (or ~EUR 2.6m once a sign error is fixed) — none of which is EUR 6.4m or EUR 2.1m, the two headline numbers on the slide.

**Question the draft must answer:** Should Brightwell invest EUR 1.2m in the catering kitchen? (reconstructed, assumption — no explicit decision question stated)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

## Findings

| # | Severity | Perspective | Check | Where | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO | 16 (Model Red Flags: business-case incremental logic) | Calc rows 5-6, 13 | The model counts 100% of catering contribution margin as the return on the EUR 1.2m kitchen spend. Orders 2026 (9,000) is sourced to actual 2026 sales data — the unit already operates before this investment — so there is no counterfactual isolating what the kitchen itself adds. | Define "without the investment" (e.g. catering capped at current capacity) and count only the incremental contribution the kitchen enables, per business-case.md's "total vs incremental" rule. |
| 2 | Blocker | Skeptical CFO | 16 (Model Red Flags #1, #7) | Calc!D5:G5 | Revenue for 2028-2031 is hardcoded as `=prev*1.18`, not `Orders*AOV` as rows B5:C5 compute it. This silently decouples the headline revenue number from the stated 12% order-growth input. Recomputed consistently as Orders×AOV, 2031 revenue is ~EUR 3.33m; the model's own current (still buggy) output is ~EUR 4.10m. Neither is EUR 6.4m. | Replace D5:G5 with `=D3*D4` style formulas so revenue is driven by Orders×AOV in every year, then re-tie the slide's headline number to the recalculated output. |
| 3 | Blocker | Skeptical CFO | 13 / Model Red Flags #9, #11 | Inputs!B6, Calc!C12-C13 | The EUR 1.2m kitchen investment is stored positive and `C13 = C6+C12` **adds** it to contribution instead of subtracting it as an outflow. Recalculating Outputs!B2 exactly as written gives NPV ≈ EUR 4.77m — more than double the slide's EUR 2.1m, and still not EUR 2.1m even after the sign is corrected (≈ EUR 2.56m) or fully reconciled with fix #2 (≈ EUR 2.18m). | Store the investment as a negative value, or change the formula to `C6-C12`. Recompute NPV from the corrected model and re-tie it to the slide. |
| 4 | Blocker | Evidence Auditor | 9 | Slide bullet 3 ("Payback in year 3") | No cell anywhere in the model computes payback — Outputs only has Revenue 2031 and NPV. Reconstructing cumulative cash flow under any version of the model tested (as-built, sign-corrected, fully corrected) does not land on year 3. | Add a cumulative cash-flow row and an explicit payback formula to Outputs before stating a payback year anywhere. |
| 5 | Blocker | Skeptical CFO | 13 | Slide bullet 1 ("over 20,000" orders) | The model's own Orders row (Calc!G3, grown at the stated 12%) reaches only ~15,861 by 2031. Even the inflated 2031 revenue divided by the stable AOV implies ~19,543 orders — still under 20,000. No cell in the model reaches "over 20,000." | Trace the 20,000 figure to its source, or correct it to whatever the fixed model actually outputs for 2031 orders. |
| 6 | Major | Skeptical CFO | 15 / Model Red Flags #12, #13 | Model-wide | Only one case is modeled. Order growth and discount rate — the two most uncertain drivers — are never flexed; no break-even growth rate or order volume is shown. | Add a down case (e.g., half the base growth rate) and an up case, and show the break-even order growth at which NPV turns negative. |
| 7 | Major | Skeptical CFO | 14 | Inputs!A3 ("Management estimate") | 12% p.a. order growth for five straight years (and the undocumented ~18% embedded in the revenue formula) has no comparison to Brightwell's own prior order history or a comparable catering operator's actual multi-year growth. | Benchmark the growth assumption against Brightwell's historical order trend or a named comparable; state the base case relative to that evidence. |
| 8 | Major | Skeptical CFO | 16 (Model Red Flags #8) | Model-wide | No check cells exist anywhere (e.g., nothing flags when Revenue ≠ Orders×AOV), which is exactly the tripwire that would have caught finding #2 automatically. | Add a check row that flags any year where Revenue diverges from Orders×AOV, and surface it prominently (e.g., conditional formatting or an Outputs-sheet flag). |
| 9 | Minor | Skeptical CFO | 16 (Model Red Flags #10) | Sheet 'Old' (hidden) | A hidden sheet with a stale formula (`Revenue v1 = Calc!B5*1.05`) sits unused in the live file. Doesn't change the current result, but invites "which version is this" questions. | Delete the Old sheet, or move prior versions to a separate file with clear version labels. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| 2031 revenue | Slide: EUR 6.4m | Model (Outputs!B1 = Calc!G5, recalculated): EUR 4.10m | EUR 2.3m overstated on slide (+56%); also doesn't match the orders-driven figure (EUR 3.33m) |
| 2031 orders | Slide: "over 20,000" | Model (Calc!G3, 12% growth): ~15,861 | Slide ~30% above the model's own Orders row |
| NPV | Slide: EUR 2.1m | Model (Outputs!B2, recalculated as currently formulated): EUR 4.77m | EUR 2.7m apart; even a sign-corrected EUR 2.56m or fully-reconciled EUR 2.18m doesn't match the slide's rounded EUR 2.1m |
| Payback | Slide: "year 3" | Model: no payback calculation exists | Not reproducible from the cited source under any version tested |

## Missing outside view

- **Order growth (12% p.a., five years, plus an undocumented ~18% effectively baked into the revenue formula):** needs comparison against Brightwell's own catering order history prior to 2026, or a named comparable corporate-catering operator's sustained multi-year growth. Nothing in the model supplies this; "Management estimate" is the only source given.

## Premortem

1. The business case credits the whole catering P&L to a single kitchen purchase; the kitchen's real capacity-driven uplift turns out to be a fraction of that, and finance can't trace where the claimed contribution came from — directly caused by finding #1.
2. Order growth doesn't sustain 12%+ for five straight years (no downside case exists to show how much cushion there was) — finding #6/#7.
3. Someone reopens the model, recalculates, and gets EUR 4.1-4.8m where the slide said EUR 6.4m revenue / EUR 2.1m NPV — the team's credibility on this case (and the next one) takes the hit, not just this slide — findings #2-#5.

## What is good and must survive

- The Inputs sheet is clean: one driver per row with value, unit and source columns, no hardcoded numbers in formulas — this is the right structure and should stay.
- The discount rate and contribution margin are both sourced to specific internal references (Group finance, Catering P&L 2026) rather than asserted.
- The slide title is a genuine action title stating a finding, not a label — keep that discipline once the numbers behind it are fixed.
- The slide is appropriately short with one message — don't let the fix add clutter.

## What "fixed" looks like

Brightwell's catering kitchen investment is likely still worth doing, but on a smaller scale than currently claimed: once the model counts only the incremental contribution the new kitchen enables (not the entire catering P&L), fixes the revenue formula to stay driven by Orders×AOV throughout, and treats the EUR 1.2m spend as an outflow rather than an inflow, the 2031 revenue figure is closer to EUR 3.3m and NPV in the region of EUR 2-2.5m — before any downside case or break-even has been run. State that range with its uncertainty, add the break-even order growth, and only then put a payback year on the slide once the model actually calculates one.


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
