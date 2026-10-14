# pr-02: Business case model with hidden problems

## Prompt

> Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them.

Input files: `pr-02-model.xlsx`, `pr-02-slide.md`
(Create the model with `python3 pr-02-make-model.py` if the .xlsx is missing; needs openpyxl.)

## Planted defects

| # | Defect | Where | Expected severity |
|---|---|---|---|
| D1 | Catering revenue formula hard-codes order growth: `=C5*1.18` instead of referencing an input | Calc!D5:G5 | Blocker (drives key output) |
| D2 | A hidden sheet `Old` holds a second, lower revenue line | sheet Old | Major or Minor, must be noticed |
| D3 | Slide states 2031 revenue EUR 6.4m and NPV EUR 2.1m; model gives different figures | slide vs Outputs | Blocker |
| D4 | No sensitivity on the two most uncertain drivers (order growth, average order value) | whole model | Major |
| D5 | Only one scenario; no downside | whole model | Major |
| D6 | Kitchen investment enters net cash flow with a positive sign, so it raises NPV instead of lowering it | Calc row 12-13 | Blocker (changes key output) |

## Reference values (computed from the model)

- Revenue 2031 in model: about EUR 4.10m (slide: EUR 6.4m).
- Orders 2031 in model: about 15,900 (slide: "over 20,000").
- NPV 2027-2031 in model as built: about EUR 4.77m (slide: EUR 2.1m).
- NPV with the investment as an outflow: about EUR 2.56m.

## Pass criteria

- Must: verdict is **Return**.
- Must: finds D1 with the cell reference and D3 with both values.
- Must: notices the hidden sheet (D2).
- Must: finds D6 (sign of the investment) or explains why the model NPV cannot be trusted.
- Must: finds D4 or D5.
- Must: recomputes at least one key output independently and reports the result.
- Must: uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings).
- Must not: claim errors in cells that are correct (false alarm on the Inputs sheet constants).
