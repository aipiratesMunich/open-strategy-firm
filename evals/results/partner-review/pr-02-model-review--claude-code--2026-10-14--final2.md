# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Return. | yes | **Verdict:** Return |
| Must: finds D1 with the cell reference and D3 with both values. | yes | Calc!D5:G5 ... hardcoded ×1.18'; table shows Revenue 2031 slide EUR 6.4m vs model EUR 4.10m, NPV slide EUR 2.1m vs model EUR 4.77m |
| Must: notices the hidden sheet (D2). | yes | Hidden sheet "Old" ... labelled "Revenue (v1, lower case)" still live-links to Calc!B5 |
| Must: finds D6 (sign of the investment) or explains why the model NPV cannot be trusted. | yes | Calc!C12 ... entered as `=Inputs!$B$6` (positive) instead of a negative outflow ... NPV is overstated by ~EUR 2.6m |
| Must: finds D4 or D5. | yes | Order growth (12%/yr...) and contribution margin (32%) are single-point ... estimates with no sensitivity table or downside case |
| Must: recomputes at least one key output independently and reports the result. | yes | Model (fully corrected...): Revenue 2031 EUR 3.33m; NPV EUR 2.18m |
| Must: uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings). | yes | Citations like Calc!D5:G5, Calc!C12, Outputs!B1, Outputs!B2, Calc!G3, Inputs!B3, B5 |
| Must not: claim errors in cells that are correct (false alarm on the Inputs sheet constants). | yes | "Inputs sheet is clean and auditable: every driver has value/unit/source columns — keep this structure." |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

# Partner review: pr-02-model.xlsx / pr-02-slide.md, gate 3

**Verdict:** Return
**In one line:** None of the slide's three headline numbers (EUR 6.4m revenue, >20,000 orders, EUR 2.1m NPV) can be derived from the model's own formulas — two formula bugs (a hardcoded growth override and a sign error on the investment) mean the model doesn't even agree with itself.

**Question the draft must answer:** Should Brightwell commit EUR 1.2m to expand catering kitchen capacity, and does the resulting business case justify it? (reconstructed, assumption)
**Answer the draft gives:** Yes — revenue reaches EUR 6.4m by 2031, NPV is EUR 2.1m, payback in year 3.
**Match:** No. Recomputing the model's own Calc/Outputs sheets gives different numbers under every consistent reading of the inputs.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician | Calc!D5:G5 | Revenue formulas switch from Orders×AOV (used correctly in B5:C5) to a hardcoded `×1.18` from 2028 onward — an 18% growth rate that exists nowhere in Inputs (which states 12%). | Revenue and orders decouple; neither the slide's "EUR 6.4m" nor "over 20,000 orders" can be reproduced from the model's stated drivers. | Rewrite D5:G5 as `=D3*D4`, `=E3*E4`, etc., consistent with B5:C5. Delete the 1.18 hardcode. |
| 2 | Blocker | Skeptical CFO | Calc!C12 | The EUR 1.2m kitchen investment is entered as `=Inputs!$B$6` (positive) instead of a negative outflow, so net cash flow (row 13) adds the capex instead of subtracting it. | NPV is overstated by ~EUR 2.6m (as-built NPV ≈ EUR 4.77m vs. slide's EUR 2.1m); cash flow can never go negative, so no payback year is even computable from this model. | Change C12 to `=-Inputs!$B$6` (or subtract investment in the NCF formula). Re-run Outputs. |
| 3 | Major | Decision Maker | Outputs / slide bullet 3 | "Payback in year 3" has no supporting calculation anywhere in the workbook — no cumulative cash flow row exists. | Once the sign bug is fixed, cumulative contribution turns positive in **2028 (year 2)**, not year 3 — the unsupported number is also the wrong one. | Add a cumulative-net-cash-flow row and derive payback explicitly from it. |
| 4 | Major | Skeptical CFO / Evidence Auditor | Inputs!B3, B5 | Order growth (12%/yr for 5 years) and contribution margin (32%) are single-point "management estimate" / internal-P&L figures with no sensitivity table or downside case, for a 5-year, EUR1.2m capex decision. | CFO has no visibility into how exposed NPV is to a lower-growth or margin-compression world — the first thing they'll ask for. | Add a sensitivity table (e.g. growth ±3pp, margin ±5pp) and an explicit downside scenario next to the base case. |
| 5 | Major | Outsider | Hidden sheet "Old" | A hidden sheet labelled "Revenue (v1, lower case)" still live-links to `Calc!B5`, left in the file about to go to the CFO. | Stray hidden-but-live artifacts are exactly how version drift like finding #1/#2 happens unnoticed, and risk resurfacing stale numbers on an unhide, print-all, or recalc. | Delete the Old sheet, or move it to a separately stored, values-only "superseded" file. |

## Numbers that do not tie

| Number | Slide | Model (as built) | Model (fully corrected: consistent 12% growth + investment as outflow) |
|---|---|---|---|
| Revenue 2031 | EUR 6.4m | EUR 4.10m (Outputs!B1) | EUR 3.33m |
| Orders 2031 | "over 20,000" | ~15,861 (Calc!G3) | ~15,861 |
| NPV | EUR 2.1m | EUR 4.77m (Outputs!B2) | EUR 2.18m |

The NPV coincidence (2.18m corrected vs. 2.1m claimed) is itself a red flag: it suggests the slide was built from an earlier, correctly-wired version of the model, and the Calc sheet drifted afterward without the slide being refreshed — which is consistent with finding #5 (a hidden "v1" sheet still sitting in the file).

## Missing outside view
- Order growth of 12%/yr sustained for 5 straight years: no comparable corporate-catering or food-service capacity-expansion benchmark is cited — it rests entirely on one internal "management estimate." (Note: this is a stated fictional case, so no real external benchmark should be fabricated here — but the gap would need filling with a real comparable before this went to an actual CFO.)

## Premortem
1. The kitchen investment is approved on a 6.4m revenue / 2.1m NPV story; actual results track the model's own corrected run-rate (~EUR 3.3m revenue by 2031), and the unit is read internally as having overpromised.
2. Someone recalculates the workbook post-approval, finds the capex was modeled as a cash *inflow*, and the resulting NPV correction triggers a review of every other model this team has shipped.
3. The single uncorroborated 12%/yr growth estimate doesn't hold past the first year or two of ramp-up; with no sensitivity or downside case ever built, there's no fallback story and no prior read on how exposed the NPV was.

## What is good and must survive
- Inputs sheet is clean and auditable: every driver has value/unit/source columns — keep this structure.
- The underlying causal logic (Orders × AOV × margin) is the right model for a volume-and-price catering business — it's correctly implemented in B5:C5; it just needs to be extended, not abandoned, for 2028-2031.
- The EUR 1.2m investment figure and the "AOV stable at EUR 210" claim both tie correctly between Inputs, Calc, and the slide.
- The three-bullet, single-headline-number slide format is a reasonable way to communicate this once the number is right.

## What "fixed" looks like
With both formula bugs corrected, the governing slide becomes: "Corporate catering reaches **EUR 3.3m** revenue by 2031 and returns **~EUR 2.2m** NPV on a EUR 1.2m kitchen investment, with payback in **year 2**." Orders grow from 9,000 in 2026 to **~15,900** in 2031 (not over 20,000), and average order value stays stable at EUR 210. This headline should still be shown alongside a sensitivity range on growth and margin, since both are currently single-point management estimates.


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
