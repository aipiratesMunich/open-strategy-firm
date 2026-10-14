# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 with cell reference and D3 with both values | yes | Finding #1: 'Calc!D5:G5 ... =prior*1.18'; table shows Revenue 2031 Slide EUR 6.4m vs Model EUR 4.10m, NPV EUR 2.1m vs EUR 4.77m |
| Notices the hidden sheet (D2) | yes | Finding #7: 'Hidden sheet `Old`, `B1 = Calc!B5*1.05` An undocumented hidden sheet applies a stray +5% adjustment...' |
| Finds D6 (sign of investment) or explains why model NPV cannot be trusted | yes | Finding #2: 'The EUR 1.2m kitchen investment ... is entered as +1,200,000 and added into net cash flow ... booked as a cash inflow in 2027, not an outflow.' |
| Finds D4 or D5 | yes | Finding #6: 'Single point estimate only — no downside or upside case... the file needs at minimum a downside...' |
| Recomputes at least one key output independently and reports the result | yes | 'Recalculating the workbook as built gives Orders 2031 = 15,861 and Revenue 2031 (`Outputs!B1`) = EUR 4.10m... NPV ≈ EUR 4.77m' |
| Uses model-scan helper or equivalent inspection of formulas (cell references in findings) | yes | Findings cite 'Calc!D5:G5', 'Calc!C12, C13', 'Inputs!B3', 'Outputs!B1', 'Calc!G3', etc. |
| Must not claim errors in cells that are correct (false alarm on Inputs sheet constants) | yes | 'What is good and must survive' section praises the Inputs sheet ('every input carries a real source... keep this discipline') rather than flagging its constants as erroneous |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

# Partner review: Brightwell catering business case (model v3 + slide 7), gate 3

**Verdict:** Return
**In one line:** The workbook, recalculated on its own formulas, does not produce the revenue, NPV or payback numbers on the slide — and one of the gaps is a capex sign error that books the kitchen investment as income.

**Question the draft must answer:** Should the CFO approve the EUR 1.2m kitchen investment for the catering unit? (reconstructed — no explicit decision ask on the slide, only headline outputs)
**Answer the draft gives:** Yes, implicitly — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO / Model (checks 1, 11, 14) | `Calc!D5:G5` | Revenue for 2028–2031 is `=prior*1.18`, a hard-coded growth factor chained off a chain, bypassing the Orders row (12% p.a., `Inputs!B3`) and the AOV row (flat EUR 210, `Inputs!B4`) displayed directly above it. Recalculating the workbook as built gives Orders 2031 = 15,861 and Revenue 2031 (`Outputs!B1`) = EUR 4.10m. I also tried the "fully consistent, orders-driven" version (no hard-code): Revenue 2031 = EUR 3.33m, Orders 2031 = 15,861. Neither reaches the slide's "6.4m" or "over 20,000." | CFO approves on a revenue figure that's ~40–50% higher than anything the model itself produces. | Delete the hard-coded `*1.18`; drive revenue as `=Orders*AOV` identically in every year/column, sourced only from `Inputs`. Re-pull the slide number from the recalculated `Outputs!B1`. |
| 2 | Blocker | Skeptical CFO / Model (check 9, escalated — changes a key output) | `Calc!C12`, `C13` | The EUR 1.2m kitchen investment (`Inputs!B6`) is entered as **+1,200,000** and added into net cash flow (`C13=C6+C12`), i.e. booked as a cash **inflow** in 2027, not an outflow. Recalculating `Outputs!B2` as literally built gives NPV ≈ **EUR 4.77m** — more than double the slide's EUR 2.1m. | If anyone opens the file and hits F9, the NPV shown is 2.3x the slide's claim, and it's wrong in the direction of making the case look better, not worse — the kind of error that gets a model (and its author) permanently distrusted by Finance. | Make `C12 = -Inputs!$B$6`. Confirm sign convention for all cash flow rows in a check cell (e.g. cumulative undiscounted CF should dip negative in the investment year, not spike positive). |
| 3 | Blocker | Decision Maker / Model (check 11/14) | Slide bullet "Payback in year 3"; `Outputs` tab | No cell anywhere in the workbook computes payback — `Outputs` has only Revenue 2031 and NPV. Reconstructing cumulative net cash flow by hand (with the sign in #2 corrected) shows the running balance is **positive from 2026 onward and never dips negative** — 2026 contribution (EUR 605k) already exceeds the 2027 investment net of that year's own contribution. There is no "payback gap" to find under this cash-flow timing, so "year 3" is not calculable from the current structure. | A specific, checkable-sounding number ("year 3") is being presented to a CFO with zero formula behind it. | Add an explicit payback calculation (cumulative net cash flow by year, flag first year it turns non-negative). Resolve finding #4 first, since payback depends on it. |
| 4 | Major | Skeptical CFO (model structure) | `Calc` row 3 vs. row 12 | Orders/revenue/contribution start in **2026** (9,000 orders, generating contribution) a full year before the kitchen investment lands in **2027** (`C12`). A capacity-building capex should precede or coincide with the volume it enables, not follow it. Either 2026 is a pre-existing base business (in which case NPV should be computed on cash flows *incremental* to that base, not the full contribution) or the investment timing is simply wrong. As built, the model capitalizes the entire forward contribution of an already-running business against one capex line, flattering the kitchen's own ROI. | The investment's true payback/NPV could be materially worse once correctly isolated from the pre-existing base business. | State explicitly whether 2026 is "business as usual" or "enabled by the kitchen." If the former, rebuild NPV on incremental orders/contribution above the 9,000-order 2026 base only. |
| 5 | Major | Evidence Auditor / Model (checks 6, 12) | `Inputs!B3` (12% growth), `Calc!D5:G5` (hidden 18%) | The single biggest value driver — 5 years of compounding order growth — is sourced only as "Management estimate," with no comparable-company benchmark and no sensitivity table. There are, in effect, two different undisclosed growth rates embedded in the file (12% on the visible Orders row, ~18% buried in the Revenue formula), and neither is stress-tested. | A board member asking "what if growth is 8%, not 12–18%?" gets no answer — the case has no demonstrated downside resilience. | Add a sensitivity table varying order growth (e.g. 6%/9%/12%) and show the NPV/payback impact of each. Cite at least one outside data point for achievable growth in comparable catering/food-service scale-ups, or flag explicitly that none exists. |
| 6 | Major | Skeptical CFO (check 13) | Whole model | Single point estimate only — no downside or upside case. For an irreversible EUR 1.2m capex decision, the file needs at minimum a downside (lower growth and/or margin compression) showing whether NPV still clears zero. | CFO has no way to judge how much cushion the EUR 2.1m NPV actually has before a routine miss turns the investment negative. | Build a downside case (e.g. 6% growth, 28% margin) and show resulting NPV/payback alongside the base case. |
| 7 | Minor | Model (check 10) | Hidden sheet `Old`, `B1 = Calc!B5*1.05` | An undocumented hidden sheet applies a stray +5% adjustment to 2026 revenue; it isn't wired into `Outputs` so it doesn't currently distort results, but a hidden sheet in a CFO-bound file invites "what else is hidden here" scrutiny. | None on current outputs, but it's a governance red flag that could mask a real manipulation next version. | Delete the `Old` sheet, or move it to a clearly labelled, unhidden "superseded versions" tab with a one-line note on why it was abandoned. |

## Numbers that do not tie

| Number | Slide | Model (as literally recalculated) | Difference |
|---|---|---|---|
| Revenue 2031 | EUR 6.4m | EUR 4.10m (`Outputs!B1`, as-built formulas) | –36% |
| NPV | EUR 2.1m | EUR 4.77m (`Outputs!B2`, as-built formulas, investment booked as inflow) | +127% |
| Orders 2031 | "over 20,000" | 15,861 (`Calc!G3`) | –21% |
| Payback | "year 3" | No calculation in workbook | n/a |

Note: if you independently correct *both* the investment sign and the hard-coded growth, NPV lands near EUR 2.18m and Revenue 2031 near EUR 3.33m — close to the slide's NPV claim but still well short of its revenue and orders claims. This suggests the slide may trace to an earlier, logically-consistent run of the model that the live workbook (v3) has since diverged from without the slide being re-pulled.

## Missing outside view

- Order growth (12% visible / ~18% effective): no comparable corporate-catering or food-service scale-up growth rate is cited anywhere. Needed before the base case can be called realistic rather than hoped-for.
- Contribution margin (32%, flat for 5 years): no check against margin trends for catering operations scaling 2x+ in volume (where food cost and labor pressure typically compress margin, not hold flat).

## Premortem

1. Growth doesn't sustain at the model's implied 12–18% for five straight years — corporate catering wins typically front-load then plateau once the initial client roster is won. Not addressed: no sensitivity, no comparable cited.
2. Kitchen commissioning slips past 2027 — common for capacity builds. Because payback isn't actually calculated (#3) and investment timing is already inconsistent with the revenue ramp (#4), a schedule slip has no modeled impact to point to.
3. Contribution margin compresses as the unit scales (food cost inflation, competitive pricing to win the extra volume) — margin is held flat at 32% with no stress test.

## What is good and must survive

- `Inputs` sheet is cleanly separated with Driver / Value / Unit / Source columns, and every input carries a real source (supplier quote, management estimate, P&L, Group finance) — keep this discipline.
- The Inputs → Calc → Outputs flow is the right shape; the problem is a broken link partway through Calc, not the overall architecture.
- No external workbook links — good hygiene.

## What "fixed" looks like

Rebuild `Calc!D5:G5` as `=Orders*AOV` for every year, with no hard-coded growth factors anywhere in the calculation sheet. Flip the investment sign in `Calc!C12` to negative and add a payback line that tracks cumulative net cash flow year by year. Decide and state whether 2026 is a pre-existing base business or kitchen-enabled volume, and scope NPV accordingly. Only after recalculating should the slide be rewritten, e.g.: "Corporate catering returns an estimated EUR X NPV on a EUR 1.2m kitchen investment, with payback in year Y under a 12% order-growth base case (sensitivity: EUR X±Z across 6–18% growth)." Add one downside scenario before this goes to the CFO.


## Files in work dir after run

- _check.py
- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
