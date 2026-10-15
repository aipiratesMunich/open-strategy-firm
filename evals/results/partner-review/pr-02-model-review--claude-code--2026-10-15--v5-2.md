# pr-02-model-review on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Return. | yes | **Verdict:** Return |
| Must: finds D1 with the cell reference and D3 with both values. | yes | Finding 3: 'Calc!D5:G5 ... computed as =<prior cell>*1.18'; Finding 1/table: slide Revenue 6.4m vs model and NPV 2.1m vs model EUR 4.77m/2.18m |
| Must: notices the hidden sheet (D2). | yes | Finding 9: 'Old sheet (hidden) ... computes =Calc!B5*1.05, a stale, orphaned figure' |
| Must: finds D6 (sign of the investment) or explains why the model NPV cannot be trusted. | yes | Finding 4: 'kitchen investment is entered as a positive number in C12 and then added ... instead of entered as a negative outflow and subtracted' |
| Must: finds D4 or D5. | yes | Finding 7: 'No sensitivity analysis on any driver (growth rate, AOV, margin, discount rate, investment cost) and no downside/upside case.' |
| Must: recomputes at least one key output independently and reports the result. | yes | 'Independently recomputed from Inputs ... EUR 3,330,826' and 'NPV(9%, Calc!C13:G13) = EUR 4,765,413 ... corrected NPV = EUR 2,182,125' |
| Must: uses the model-scan helper or equivalent inspection of formulas (evidence: cell references in findings). | yes | Cell references throughout: Calc!D5:G5, Calc!C12, Calc! row 13, Inputs!B3, Inputs!B5, Outputs!B1, Calc!row4 |
| Must not: claim errors in cells that are correct (false alarm on the Inputs sheet constants). | yes | Review states Inputs tab is 'genuinely separated ... every driver labelled, sourced and dated-equivalent' and flags only lack of external benchmarking (finding 6), not that the constants themselves are wrong |

## Transcript

## Turn 1

**User:** Here is the business case model for the Brightwell catering unit and the slide that summarises it. Check the numbers before the CFO sees them. (Attached in the working directory: pr-02-model.xlsx, pr-02-slide.md.)

Confirmed. Here's the review.

# Partner review: pr-02-model.xlsx + pr-02-slide.md, gate 3

**Verdict:** Return
**In one line:** The model has two bugs that drive its key outputs (a hard-coded growth override and an investment sign error), and even once those are fixed, the slide's headline Revenue and Orders figures still don't tie to anything the model — or the Inputs tab's own stated 12% growth assumption — can produce.

**Question the draft must answer:** Should Brightwell fund a EUR 1.2m kitchen investment for the corporate catering unit? (reconstructed, assumption — no explicit decision ask or decision-maker named in either file)
**Answer the draft gives:** Yes — EUR 6.4m revenue by 2031, EUR 2.1m NPV, payback in year 3.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO (check 14) | Slide bullet 1 / `Outputs!B1` | Slide states Revenue 2031 = EUR 6.4m. The model as literally built computes `Outputs!B1 = Calc!G5` = **EUR 4,104,005**. Independently recomputed from Inputs (orders×AOV, 12% growth, no hard-code): **EUR 3,330,826**. Neither matches 6.4m. | CFO opens the model, recalculates Revenue 2031, gets a number 2–3x lower than the slide. The deck's central growth claim is unsupported by its own model. | Reconcile Revenue 2031 to one figure. Recompute from `Orders(2031) × AOV` with the Inputs-tab growth rate (12%) and update the slide to EUR 3.3m, or document and source whatever alternate growth assumption justifies 6.4m. |
| 2 | Blocker | Skeptical CFO (check 14) | Slide bullet 2 / `Calc!B3:G3` | Slide states orders grow to "over 20,000" by 2031. Orders row in the model, driven by the Inputs-tab growth rate of 12%, reaches **15,861**, not over 20,000. 9,000 compounded at 12% for 5 years gives 15,861; it takes ~18% compound growth to reach 20,590 — which is suspiciously exactly the hard-coded multiplier in finding 4 below. | The order-count narrative appears to have been built off a different (undocumented, ~18%) growth rate than the one stated on the Inputs tab and used everywhere else, so two slide bullets rest on two different, unreconciled growth assumptions. | Reconcile the orders-growth narrative to the Inputs-tab rate (12%) and update "over 20,000" to ~15,900, or change the Inputs-tab growth assumption to the rate actually driving the story and justify it. |
| 3 | Blocker | Skeptical CFO (check 16 / Model Red Flags check 1) | `Calc!D5:G5` | Revenue from 2028 onward is computed as `=<prior cell>*1.18`, a typed constant, instead of `Orders × AOV` (which is how B5 and C5 are built, and how the Orders row itself grows at 12%). Revenue and Orders diverge after 2027: Orders grows at 12%, Revenue grows at 18%. This hard-coded number drives the key output (Revenue 2031, and through it Contribution and NPV). | Anyone tracing the model finds Revenue decoupled from Orders — the two rows tell different growth stories and nobody can tell which one is real. | Replace `=C5*1.18` etc. with `=D3*D4` (Orders × AOV) for all years, consistent with B5/C5, so Revenue is driven by the same growth rate as Orders. |
| 4 | Blocker | Skeptical CFO (check 16 / Model Red Flags check 9) | `Calc!C12`, `Calc!row 13` | The EUR 1.2m kitchen investment is entered as a **positive** number in `C12` and then **added** in `Net cash flow = C6+C12`, instead of entered as a negative outflow and subtracted. This inflates, not reduces, the 2027 cash flow used in the NPV. As built, `NPV(9%, Calc!C13:G13)` = **EUR 4,765,413** — more than double the slide's claimed EUR 2.1m. | The spreadsheet, taken at face value, overstates NPV by ~2.3x relative to the slide. A CFO who runs the formula will get a materially different (higher, but wrong-for-the-wrong-reason) number and will stop trusting the model's integrity regardless of direction. | Change `C12` to `=-Inputs!$B$6` (or keep it positive and change row 13 to `=C6-C12`) so the investment is a genuine cash outflow in the NPV calculation. |
| 5 | Major | Skeptical CFO (check 14) / Decision Maker | Slide bullet 3 vs. model | "Payback in year 3" and the slide's EUR 2.1m NPV are *not* produced by the model as currently built (which gives NPV EUR 4.77m and no payback calculation at all), but they **do** match almost exactly once both bugs in findings 3 and 4 are fixed together: corrected NPV = EUR 2,182,125, and cumulative cash flow turns positive during 2028 (year 3, counting 2026 as year 1) — both consistent with the slide. This is good news for those two numbers, but it means the shipped workbook is not the one that actually produced the slide, and there is no payback row anywhere in `Outputs` to show the calculation. | A reviewer cannot currently verify "payback in year 3" from anything in the file — it is asserted, not computed. Until the model is fixed and a payback line is added, this number has no visible support. | Fix findings 3 and 4, add a payback row to `Outputs` (cumulative net cash flow by year), and confirm it shows year 3 — then this bullet is supportable. |
| 6 | Major | Evidence Auditor (check 10,11) / Skeptical CFO (check 6) | `Inputs!B3` (growth 12%), `Inputs!B5` (margin 32%) | Both growth and contribution-margin assumptions are sourced only to "Management estimate" and the catering unit's own 2026 P&L. There is no outside comparison to what other corporate catering operators have actually achieved sustaining 12% p.a. growth for five years or a 32% contribution margin. | A board member asks "how do you know 12% growth for five straight years is achievable" and there is no answer beyond the client's own belief. | Benchmark the 12% growth and 32% margin assumptions against at least one external comparable (industry data, a peer operator, or a prior Brightwell expansion), or flag them explicitly as unvalidated management judgement with the NPV's sensitivity to each shown (see finding 7). |
| 7 | Major | Skeptical CFO (check 16 / Model Red Flags check 12,13) | Whole model | No sensitivity analysis on any driver (growth rate, AOV, margin, discount rate, investment cost) and no downside/upside case. The business case rests entirely on one point estimate per input. | The board cannot tell which assumption, if wrong, flips the EUR 2.1m NPV negative, or how much headroom the case has. | Add a sensitivity table varying growth rate, margin and discount rate individually, and define a coherent downside case (e.g., growth stalls at 6–8%) and upside case, each with an NPV and break-even value. |
| 8 | Major | Logician / Skeptical CFO (Business Case common mistake: "Total instead of incremental") | `Calc!row 6`, NPV formula | The model has no "without the investment" counterfactual. Orders already stand at 9,000 in 2026, before the kitchen investment occurs (in 2027); the full contribution from that pre-existing volume, plus all subsequent growth, is swept into the NPV as if none of it would happen without the EUR 1.2m spend. | If the catering unit would keep doing some baseline volume without the new kitchen, the case is valuing total cash flow, not the incremental cash flow the investment actually buys — inflating the apparent return. | Define a "do nothing" baseline (e.g., orders flat at 9,000, or declining) and rebuild the NPV on the *difference* between the invested and non-invested cases. |
| 9 | Minor | Skeptical CFO (Model Red Flags check 10) | `Old` sheet (hidden) | A hidden sheet "Old" computes `=Calc!B5*1.05`, a stale, orphaned figure not referenced by `Outputs` or the slide. | Low risk since it doesn't feed current outputs, but a sharp reviewer who finds a hidden sheet with a different number will question what else in the file is stale or unreconciled. | Delete the `Old` sheet, or if it must be kept for audit trail, label it clearly as superseded and keep it unhidden. |
| 10 | Minor | Outsider | Slide footer | Slide cites "Brightwell catering business case model v3" but the workbook carries no version marker, so this claim cannot be checked against the file. | Minor traceability gap. | Add a version/date cell to the Inputs tab and reference it from the slide footer. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Revenue 2031 | Slide: EUR 6.4m | Model `Outputs!B1` (as built): EUR 4.10m / recomputed from Inputs: EUR 3.33m | ~EUR 2.3–3.1m short |
| Orders 2031 | Slide: "over 20,000" | Model `Calc!G3` (driven by stated 12% input): 15,861 | ~4,700+ orders short |
| NPV | Slide: EUR 2.1m | Model `Outputs!B2` (as built, with sign-error bug): EUR 4.77m | ~EUR 2.6m over (ties to EUR 2.18m only after fixing findings 3 & 4) |

## Missing outside view

- Order growth of 12% p.a. for five consecutive years: no comparable corporate catering operator's growth history cited. No web access was available in this review to find one — this needs sourcing before release.
- Contribution margin of 32%: no comparison to peer catering/foodservice margins. Same limitation — flag for the team to source, do not accept the P&L figure alone as proof it is sustainable at scale.

## Premortem

1. **Model credibility collapses in the room.** The CFO (or their analyst) opens the workbook, traces the NPV formula, finds the investment added instead of subtracted and a hard-coded 18% sitting inside a calculation row — and now distrusts every number in the deck, including the ones (NPV, payback) that were actually closer to correct.
2. **Growth doesn't happen because nobody owns demand generation for the new capacity.** The case assumes orders keep compounding once the kitchen is built, but the slide and model are silent on who in the organisation is accountable for selling the incremental 6,000–11,000 orders/year of capacity the kitchen investment unlocks. If catering stays an order-taking unit with no sales motion added, utilisation stalls at whatever baseline demand already exists — which is exactly the "total vs. incremental" gap in finding 8.
3. **The existing catering team's incentives don't change with a new kitchen.** If catering staff are measured on service levels or cost control today, not volume growth, a bigger kitchen doesn't by itself produce 12%+ p.a. order growth; it just increases fixed cost exposure if the growth doesn't materialize. Nothing in the model stress-tests what happens to the EUR 1.2m investment case if growth comes in at, say, half the assumed rate (finding 7 covers the missing sensitivity; this is the human reason that gap matters).

## What is good and must survive

- The Inputs tab is genuinely separated from calculations, with every driver labelled, sourced and dated-equivalent (unit + source column) — a reasonable base structure to rebuild on.
- Average order value is handled correctly and consistently throughout (`Calc!row4` references `Inputs!$B$4` every year) — this is the one slide claim that fully ties to the model as built.
- The explicit "fictional company, invented figures" framing on the slide is honest labelling that should stay.
- The underlying intent of the model (orders → revenue → contribution → net cash flow → NPV) is the right shape for a kitchen-investment business case; the problems are implementation bugs and missing incremental framing, not the model's architecture.

## What "fixed" looks like

Once the hard-coded 1.18 revenue override is replaced with orders-driven revenue, and the investment is entered as a genuine cash outflow, the model's own NPV comes out to EUR 2.18m with payback during 2028 (year 3) — both consistent with what the slide already claims, so those two headline numbers hold up once the formulas are corrected. Revenue, however, should read: "Corporate catering reaches EUR 3.3m revenue by 2031 (orders growing from 9,000 to ~15,900 at 12% p.a.) and returns EUR 2.2m NPV on a EUR 1.2m kitchen investment, payback in year 3" — pending the incremental-cash-flow and sensitivity fixes in findings 7–8, which could move the NPV further.


## Files in work dir after run

- pr-02-make-model.py
- pr-02-model.xlsx
- pr-02-slide.md
