# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 with cell reference and D3 with both values | yes | Finding #1: 'Calc!D5:G5 ... Revenue for 2028–2031 is `=prior*1.18`'; Finding #3/table: 'EUR 6.4m revenue (model: EUR 4.10m...)' and 'EUR 2.1m NPV (model: EUR 4.77m...)' |
| Notices the hidden sheet (D2) | yes | Finding #7: '"Old" sheet (hidden) / A hidden sheet holds a superseded revenue figure (`=Calc!B5*1.05`...)' |
| Finds D6 (sign of investment) or explains why NPV cannot be trusted | yes | Finding #2: 'Calc!C12 ... the investment is **added** to contribution, not subtracted. This inflates 2027 net cash flow by EUR 2.4m... overstates NPV by more than 2x' |
| Finds D4 or D5 | yes | Finding #5: 'Single point estimate throughout: one growth rate, one margin, one discount rate, no downside or upside case, no break-even shown for the most uncertain driver (order/revenue growth)' |
| Recomputes at least one key output independently and reports the result | yes | 'Recomputing from the model's own formulas gives revenue of EUR 4.10m (EUR 3.33m if ...), NPV of EUR 4.77m ... or ~EUR 2.18m once a sign error is fixed, and a payback that falls in year 2' |
| Uses the model-scan helper or equivalent inspection of formulas (cell references in findings) | yes | Findings cite 'Calc!D5:G5', 'Calc!C12', 'Outputs!B1/B2', 'Inputs!B3' with actual formula text like '=C6+C12' and '=Inputs!$B$6' |
| Must not claim errors in cells that are correct (false alarm on Inputs sheet constants) | yes | Report explicitly notes 'The EUR 1.2m investment figure is the one number that does tie correctly between Inputs, Calc and the slide' and praises the Inputs sheet structure, with no finding alleging an Inputs constant itself is wrong |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

# Partner review: pr-02-slide.md + pr-02-model.xlsx, gate 3

**Verdict:** Return
**In one line:** All four headline numbers on the slide — revenue, orders, NPV, payback — fail to tie to the model, and two of the four come from formula bugs (a revenue growth plug and an investment sign error) that materially change the answer.

**Question the draft must answer:** Should Brightwell fund a EUR 1.2m kitchen investment to expand corporate catering, and what return does it generate? (reconstructed — no explicit decision ask is stated)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

The model does not currently support that answer. Recomputing from the model's own formulas gives revenue of EUR 4.10m (EUR 3.33m if you make revenue track the stated order/price drivers consistently), NPV of EUR 4.77m if you take the formulas literally or ~EUR 2.18m once a sign error is fixed, and a payback that falls in year 2, not year 3 — because no payback calculation exists in the model at all.

## Findings

| # | Severity | Perspective | Check | Where | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO | Model red flag 1 (hard-coded number drives a key output) | Calc!D5:G5 | Revenue for 2028–2031 is `=prior*1.18`, a typed 18% growth rate inside the formula. It ignores the Orders (row 3) and Average order value (row 4) lines entirely for 4 of the 6 forecast years — the "Orders" and "AOV" rows shown in Calc stop driving revenue after 2027. Driver-consistent revenue (orders × EUR 210) for 2031 is EUR 3.33m, not the EUR 4.10m this plug produces. | Delete the `*1.18` plug. Make every year's revenue `=Orders*AOV` with Orders and AOV pulled from Inputs on every column, so one formula runs across the full timeline. |
| 2 | Blocker | Skeptical CFO | Model red flag 9 (sign convention, changes a key output) | Calc!C12 | The EUR 1.2m kitchen investment is entered as `=Inputs!$B$6` (positive 1,200,000) in 2027, then net cash flow is `=C6+C12` — the investment is **added** to contribution, not subtracted. This inflates 2027 net cash flow by EUR 2.4m versus a correctly signed model and overstates NPV by more than 2x (EUR 4.77m as built vs. ~EUR 2.18m once corrected — recomputed independently). | Enter the investment as a negative outflow (`=-Inputs!$B$6`) or change the cash-flow formula to subtract it. Re-run NPV after the fix and confirm against an independent recalculation. |
| 3 | Blocker | Skeptical CFO | Model red flag 14 / Checklist 13 (outputs don't tie to story) | Slide headline vs. Outputs sheet | None of the three headline numbers on the slide match the model in any version: EUR 6.4m revenue (model: EUR 4.10m as-built / EUR 3.33m driver-consistent), ">20,000 orders" (model: ~15,861, driven by the stated 12% input), EUR 2.1m NPV (model: EUR 4.77m as-built / ~EUR 2.18m corrected). The gaps are large (36–48% on revenue, ~23% on orders) and in one case the sign of the error reverses which direction is overstated. | Do not present any number until the two formula bugs above are fixed and the Outputs sheet is regenerated. Then re-tie slide to Outputs sheet cell by cell before this goes to the CFO. |
| 4 | Blocker | Skeptical CFO | Model red flag 11 (unverifiable key output) | Slide bullet "Payback in year 3" | There is no payback or cumulative cash-flow calculation anywhere in the workbook (Outputs has only Revenue 2031 and NPV). The claim is not computed, it's asserted. Reconstructing cumulative cash flow from a corrected model (sign fixed, revenue driver-consistent) turns positive in 2028 — i.e., payback in year 2, not year 3 — under every version I rebuilt. | Add an explicit cumulative-cash-flow row to Calc/Outputs that computes payback, and only then put a year number on the slide. |
| 5 | Major | Skeptical CFO / Evidence Auditor | Model red flag 12 & 13 (no sensitivity, no scenarios) | Whole model | Single point estimate throughout: one growth rate, one margin, one discount rate, no downside or upside case, no break-even shown for the most uncertain driver (order/revenue growth). On an irreversible EUR 1.2m capex decision this is a bare minimum gap. | Add a one-way sensitivity on order growth and margin (the two drivers that move NPV most), show the break-even growth rate at which NPV = 0, and add a coherent downside scenario (e.g., 2027 growth stalls to management's conservative case). |
| 6 | Major | Skeptical CFO | Model red flag 6 / Checklist 14 (base-case realism, outside view) | Inputs!B3 (12% order growth p.a.), implicit 18% revenue growth in Calc | Both growth rates are sourced only as "management estimate" with no comparison to what Brightwell's other catering units, or comparable contract-catering operators, actually achieved after a kitchen expansion. Two different implicit growth rates (12% orders vs. 18% revenue) sit in the same model with no reconciliation. | Benchmark the growth assumption against at least one outside reference (an existing Brightwell site's post-investment ramp, or a sector comparable) before calling it base case, and reconcile why orders and revenue growth differ. |
| 7 | Minor | Skeptical CFO | Model red flag 10 (hidden content) | "Old" sheet (hidden) | A hidden sheet holds a superseded revenue figure (`=Calc!B5*1.05`, EUR ~1.98m for 2026). It isn't wired into Outputs, so it doesn't change the current numbers, but a hidden sheet with a different number is exactly what a sharp CFO finds and asks about. | Delete the sheet or move it to a clearly labelled "superseded" appendix tab; don't leave hidden sheets in a model going to the CFO. |
| 8 | Minor | Decision Maker | Checklist 2 (recommendation specificity) | Slide title/body | The slide states the economic case but doesn't ask for anything specific — no capex approval date, owner, or decision requested. | Add one line: what is being approved, by whom, and by when. |

## Numbers that do not tie

| Number | Slide | Model (as built) | Model (formulas corrected) | Difference |
|---|---|---|---|---|
| Revenue 2031 | EUR 6.4m | EUR 4.10m (Outputs!B1 / Calc!G5) | EUR 3.33m (orders × AOV, driver-consistent) | Slide is 36–48% above any model-derived figure |
| Orders 2031 | "over 20,000" | ~15,861 (Calc!G3, from the 12% input) | same — orders row is unaffected by the revenue bug | Slide is ~23% above the model's own order line |
| NPV | EUR 2.1m | EUR 4.77m (Outputs!B2, sign bug as built) | ~EUR 2.18m (sign fixed + driver-consistent revenue) | As-built model overstates by ~2.2x; even the corrected figure needs independent re-verification before it's quoted |
| Payback | "year 3" | not computed anywhere in the model | ~year 2 (cumulative cash flow turns positive in 2028, reconstructed) | Unsupported claim, and the reconstructed estimate contradicts it |

## Missing outside view

- **Order/revenue growth (12% orders p.a. implied, 18% revenue p.a. actually used in the formulas):** no comparison to what Brightwell's existing catering sites, or comparable contract-catering kitchen expansions, achieved in volume ramp-up after a similar capex. This is the single assumption the NPV is most sensitive to and it rests on "management estimate" alone.

## Premortem

1. The board approves on the strength of a EUR 2.1m NPV that was actually EUR 4.77m in the model handed to them (sign error) — once someone fixes the formula post-approval, the investment case looks far weaker than what was sold, and the team's credibility on the next business case takes the hit.
2. Order growth comes in below the unvalidated 12–18% assumption (no downside case exists to say what happens if it doesn't) and the "payback in year 3" promise — which was never actually calculated — turns out to be year 4 or 5 instead, with no one having flagged that risk going in.
3. Someone on the CFO's team opens the workbook, finds the hidden "Old" sheet with a different revenue number and the hard-coded 1.18 in the formula bar, and the finance team's trust in every other number in the deliverable drops, not just this one.

## What is good and must survive

- The slide title is a proper action title: one sentence with the revenue, NPV and investment figures together, not a vague label.
- The Inputs sheet separates assumptions from calculations cleanly, with a source column populated for every driver (sales data, management estimate, supplier quote, group finance) — exactly the structure a model should have, even though the Calc sheet breaks from it.
- The EUR 1.2m investment figure is the one number that does tie correctly between Inputs, Calc and the slide.
- Single-slide format is the right length for a CFO readout — this is a numbers problem, not a communication-length problem.

## What "fixed" looks like

"The EUR 1.2m kitchen investment supports corporate catering orders growing from 9,000 in 2026 to roughly 15,900 by 2031 (12% p.a.), reaching EUR 3.3m revenue at a stable EUR 210 average order value. At a 32% contribution margin and 9% discount rate, base-case NPV is approximately EUR 2.2m with payback in year 2 — figures recomputed directly from the Calc sheet with the investment correctly signed and revenue driven by orders × price throughout, not from a partial formula. A downside case at [X]% growth is shown alongside, and the break-even growth rate at which NPV turns negative is [Y]%." Treat the bracketed values as placeholders until the model is rebuilt and independently re-verified — don't publish new numbers from this review without rerunning them in the corrected workbook.


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
