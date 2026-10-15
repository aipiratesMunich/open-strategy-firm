# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Return. | yes | **Verdict:** Return |
| Must: finds D1 with the cell reference and D3 with both values. | yes | Finding 1: 'Calc!D5:G5 vs Inputs!B3 ... Revenue from 2028 is hard-coded as =prev*1.18'; Findings 3-4 give slide 6.4m/2.1m vs model 4.10m/4.77m |
| Must: notices the hidden sheet (D2). | yes | Finding 10: 'A hidden sheet holds an alternate 2026 revenue figure (=Calc!B5*1.05...), unreferenced by Outputs or the slide' |
| Must: finds D6 (sign of the investment) or explains why the model NPV cannot be trusted. | yes | Finding 2: 'Calc!C12, C13 ... The EUR 1.2m kitchen investment is entered as a positive number ... and then added to contribution ... instead of subtracted.' |
| Must: finds D4 or D5. | yes | Finding 9: 'No sensitivity or break-even on the two most uncertain drivers ... and no down/up case.' |
| Must: recomputes at least one key output independently and reports the result. | yes | 'Once findings 1 and 2 are both fixed, NPV recomputes to ≈EUR 2.18m' |
| Must: uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings). | yes | Cell references throughout, e.g. 'Calc!D5:G5 vs Inputs!B3', 'Calc!C12, C13', 'Outputs!B1 = Calc!G5' |
| Must not: claim errors in cells that are correct (false alarm on the Inputs sheet constants). | yes | No finding alleges an Inputs constant is wrong; Finding 11 only flags missing date/owner metadata, not an incorrect value |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

All numbers confirmed. Here's the review.

# Partner review: Brightwell catering business case (pr-02-model.xlsx + pr-02-slide.md), gate 3

**Verdict:** Return
**In one line:** The slide's three headline numbers — revenue, NPV, order count — do not match the model's own live formulas, and the mismatch is driven by a hard-coded growth rate and a sign error that together overstate the return by roughly 2x.

**Question the draft must answer:** Should the business fund the EUR 1.2m catering kitchen investment? (reconstructed, assumption)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO / Model | Calc!D5:G5 vs Inputs!B3 | Revenue from 2028 is hard-coded as `=prev*1.18`, disconnected from the Orders row (Calc!G3), which still grows at the input 12%. The model literally contains two different growth rates for one business. | The CFO opens the file and the revenue line does not trace to any input cell — the 18% number exists nowhere in Inputs. | Replace Calc!D5:G5 with `=D3*D4` style formulas (orders × AOV) so revenue is driven by the Orders row and the 12% input, like B5/C5 already are. |
| 2 | Blocker | Skeptical CFO / Model | Calc!C12, C13 | The EUR 1.2m kitchen investment is entered as a positive number in C12 and then **added** to contribution in C13 (`=C6+C12`), instead of subtracted. Capex makes the model's cash flow go up, not down. | NPV and payback both come out far better than the project deserves; nobody reviewing the formula bar would catch this without tracing the sign through two cells. | Enter the investment as a negative outflow, or change C13 to `=C6-C12`. |
| 3 | Blocker | — | Slide bullet 1 vs Outputs!B1 | Slide: "reaches EUR 6.4m revenue by 2031." Model's own live formula (Outputs!B1 = Calc!G5) computes **EUR 4.10m**. | Two numbers for the same figure, one a model sheet away from the other. The CFO cannot know which one is the business case. | Reconcile to one figure. Once finding 1 is fixed, Calc!G5 computes EUR 3.33m (orders-driven, 12% growth) — use that, not 6.4m or 4.1m. |
| 4 | Blocker | — | Slide title vs Outputs!B2 | Slide: "returns EUR 2.1m NPV." Model's own live formula (Outputs!B2 = NPV(...)) computes **EUR 4.77m**. | Same number stated twice with a 2.3x gap — the title claim the CFO will anchor on does not come from the file behind it. | Reconcile. Once findings 1 and 2 are both fixed, NPV recomputes to ≈EUR 2.18m — close to the slide's 2.1m, suggesting the slide may have been written against a correct earlier version of the model and the file regressed. Confirm and re-tie. |
| 5 | Blocker | — | Slide bullet 1 vs Calc!G3 | Slide: "orders grow... to over 20,000 in 2031." The model's own row literally labeled "Orders" (Calc!G3) computes **15,861** (9,000 × 1.12⁵). The only way to reach ~19,500 is dividing the buggy revenue line (finding 1) by the AOV — i.e., the slide's order count was backed into from the wrong row. | The order count on the slide isn't the model's order count. | Use Calc!G3 (15,861, or the orders figure after the Calc!G5 fix) as the stated 2031 order count. |
| 6 | Blocker | Skeptical CFO / Model | Slide bullet 2 vs Calc!G4 & G5/G3 | Slide and Calc!G4 both state AOV "stable at EUR 210." But the model's own Revenue (G5) ÷ Orders (G3) for 2031 implies an AOV of **EUR 258.75** — a direct internal contradiction produced by finding 1. | The model asserts EUR 210 in one row and EUR 258.75 in the ratio of two other rows it produces itself. | Resolves automatically once finding 1 is fixed — AOV will then be consistently EUR 210 everywhere. |
| 7 | Blocker | Model red flags (check 1/11) | Slide bullet 3 ("payback in year 3") | No cell in the workbook computes payback — there is no cumulative cash-flow row and no payback output. The claim is asserted, not calculated. Reconstructing cumulative cash flow with the sign fixed (finding 2) shows cumulative turns positive during 2027, not year 3. | A number on the CFO's slide has no calculation behind it anywhere in the file, and the reviewer's own reconstruction lands a year earlier. | Add an explicit cumulative-cash-flow row and a payback cell to Calc, and re-derive the slide claim from it. |
| 8 | Major | Business case / Model | Calc row 13, whole model | "Net cash flow" is the entire catering unit's contribution (all ~9,000+ orders), not the incremental cash flow caused by the kitchen investment. There is no counterfactual (what orders/revenue look like without the EUR 1.2m spend). This is the textbook "total instead of incremental" business-case mistake. | If the existing catering business continues regardless of the investment, the NPV is crediting the EUR 1.2m with growth it didn't cause — the real incremental NPV could be far smaller, or negative. | State the counterfactual explicitly (what happens to orders/capacity without the kitchen) and rebuild Calc row 13 from the incremental contribution only (uplift caused by the new kitchen, not total catering contribution). |
| 9 | Major | Model red flags (check 12/13) | Whole model | No sensitivity or break-even on the two most uncertain drivers (12% p.a. order growth for 5 straight years, 32% contribution margin), and no down/up case. | A board-level 1.2m decision with a single-point forecast; the CFO's first question will be "what if growth is 8%, not 12%?" and there's no answer in the file. | Add a sensitivity table on order growth and contribution margin, with the break-even growth rate at which NPV turns negative. Add a down case tied to a specific cause (e.g., order growth stalls at 6%), not a flat haircut. |
| 10 | Minor | Model red flags (check 10) | "Old" sheet (hidden) | A hidden sheet holds an alternate 2026 revenue figure (`=Calc!B5*1.05`, i.e. 5% higher than the live figure), unreferenced by Outputs or the slide, with no label explaining why it's kept. | Not currently feeding any output, but hidden content in a file going to the CFO invites the question "what else is hidden." | Delete the sheet, or unhide it and label it clearly as a superseded version with the reason it's kept. |
| 11 | Minor | Evidence Auditor (check 5) | Inputs sheet | Each driver has a source (e.g. "Management estimate," "Supplier quote") but no date and no named owner. | Low cost now, but nobody to call when an assumption needs revisiting next quarter. | Add a date and an owner column to Inputs. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Revenue 2031 | Slide: EUR 6.4m | Outputs!B1 (model's live formula): EUR 4.10m | EUR 2.3m (36%) |
| NPV | Slide: EUR 2.1m | Outputs!B2 (model's live formula): EUR 4.77m | EUR 2.67m (127%) |
| Orders, 2031 | Slide: "over 20,000" | Calc!G3 (model's own Orders row): 15,861 | 4,139 (21%) |
| Average order value, 2031 | Slide / Calc!G4: EUR 210 ("stable") | Calc!G5 ÷ Calc!G3 (model's own implied AOV): EUR 258.75 | EUR 48.75 (23%) |
| Payback | Slide: "year 3" | No cell computes payback; reconstruction (sign fixed) shows cumulative cash flow turns positive in 2027 | At least 1 year, and no supporting cell exists |

## Missing outside view

- **12% p.a. order growth, five years straight:** no comparison to Brightwell's own historical growth or to comparable corporate-catering operators' ramp rates. State what evidence (if any) supports five consecutive years at this rate, or dial it back.
- **32% contribution margin, held flat for five years:** no comparison to current catering P&L trend or to industry margin benchmarks as volume scales (kitchens often see margin compress or improve with utilization — direction isn't stated either way).

## Premortem

1. **(External)** Order growth doesn't sustain 12% p.a.; corporate catering demand plateaus after an initial ramp, as the model shows no comparable evidence it will hold — and there's no sensitivity table to show how exposed the NPV is to this.
2. **(Internal — capacity/ownership)** The model and slide name no owner for the kitchen build-out, no construction timeline, and no throughput ceiling on the new kitchen. If the build slips a year or the new kitchen caps out below the 15,000+ orders the growth case implies, the return shifts — and nobody is on record as accountable for catching that early.
3. **(Internal — attribution)** Because the model folds the entire existing catering book into "net cash flow" rather than isolating the investment's incremental effect (finding 8), nobody will be able to tell afterward whether the kitchen investment itself created value or whether the business grew anyway. There's no checkpoint or incremental KPI to kill or validate the case post-launch.

## What is good and must survive

- The model's structure is sound: Inputs, Calc and Outputs are on separate sheets, with calculations flowing one direction and each input carrying a source. Once the two formula defects are fixed, this skeleton doesn't need rebuilding.
- The slide itself is a single clean message with a stated source line and one claim per bullet — the communication format is right; only the numbers inside it need to be correct.

## What "fixed" looks like

Once findings 1, 2 and 8 are corrected, the directionally-reconciled case (still pending the incremental-cash-flow fix, so treat as provisional) reads something like: "Corporate catering orders grow from 9,000 in 2026 to roughly 15,900 by 2031 (12% p.a.), lifting revenue to about EUR 3.3m at a stable EUR 210 average order value. Against the EUR 1.2m kitchen investment, this returns an NPV of approximately EUR 2.2m at a 9% discount rate — but that number still mixes in the catering unit's existing business; it will move once cash flow is rebuilt on an incremental basis against a stated counterfactual, and payback needs its own calculated row rather than an asserted year."


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
