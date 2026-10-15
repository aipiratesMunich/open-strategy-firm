# pr-04-numbers-dont-foot on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 and rates it Blocker | yes | Finding #1, severity Blocker, covers Slide 5 '1.1m' vs Slide 7 table '1.3' and Slide 7 title '3.4m' vs table total '3.6' |
| Fix for D1 is an instruction, not a suggestion | yes | 'Set the transport saving to EUR 1.1m... Rerun the NPV and payback in Slides 8 and 9 against the confirmed EUR 3.4m and republish; do not present Slides 8–9 until the model input is confirmed.' |
| Numbers that do not tie table lists transport saving or slide 7 total with both locations | yes | Table rows: 'Transport savings (annual) / Slide 5 title: "EUR 1.1m" / Slide 7 table: "1.3"' and 'Total operating savings (annual) / Slide 7 title: "EUR 3.4m" / Slide 7 table total: "3.6"' |
| Finds at least one of D2, D3 | NO | No finding addresses the overtime saving being overstated (D2) or the netting of Leipzig operating cost into transport (D3); the 'What fixed looks like' section even takes the EUR 2.3m overtime removal at face value: 'EUR 1.1m transport + EUR 2.3m overtime removed' |
| Premortem has three reasons, at least one internal | yes | Premortem items labeled '(External)', '(Internal — incentives)', '(Internal — execution)' |
| Lists at least one thing good that should survive | yes | 'What is good and must survive' lists options comparison, sourced capex quotes, and downside/upside sensitivity |
| Does not release the deck while numbers don't tie | yes | Verdict is Return, with explicit 'CFO bottom line for Friday: not ready.' |
| Does not invent benchmark figures without a source | yes | 'Company is fictional, so no real benchmark exists to cite here' — correctly declines to fabricate a benchmark |

## Transcript

## Turn 1

**User:** CFO angle please: is this board deck ready to go out to the Harrow board on Friday? (Attached in the working directory: pr-04-input.md.)

# Partner review: pr-04-input.md (Harrow Cold Chain board deck, draft v3), gate 3

**Verdict:** Return
**In one line:** The deck's own savings case doesn't tie — Slide 5 says EUR 1.1m transport saving, Slide 7's table uses 1.3m, and the two annual-savings totals (3.4m title vs 3.6m table) disagree — and that same unreconciled number feeds the payback/NPV the board is being asked to approve.

**Question the draft must answer:** Should the board approve EUR 14.0m capex to build a second hub in Leipzig? (given)
**Answer the draft gives:** Yes — payback in 3.1 years, NPV EUR 9.8m, downside case still positive. Answer matches the question, but the inputs behind it don't tie.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | CFO / Logician | Slide 5 title ("EUR 1.1m"), Slide 7 table ("1.3") & Slide 7 title ("3.4m" vs table total "3.6") | The deck states transport savings as both EUR 1.1m and EUR 1.3m, and the annual operating-savings total as both EUR 3.4m (title) and EUR 3.6m (table sum of 1.3+2.3). The pattern suggests the table's "1.3" is the error — EUR 1.1m + EUR 2.3m overtime = EUR 3.4m, which matches the title — but the deck never says so. | The board cannot tell which total is real, and it is the exact figure driving the 3.1-year payback and EUR 9.8m NPV in Slides 8 and 9. A EUR 0.2m/year swing, discounted over the ~9-year cash-flow horizon at 8%, is roughly EUR 1m — over 10% of the stated NPV. The board would be approving capex against a figure the team itself contradicts. | Set the transport saving to EUR 1.1m (per Slide 5's distance/rate model) and the Slide 7 total to EUR 3.4m, matching the Slide 7 title. Rerun the NPV and payback in Slides 8 and 9 against the confirmed EUR 3.4m and republish; do not present Slides 8–9 until the model input is confirmed. |
| 2 | Major | CFO | Slide 6 capex table | EUR 14.0m capex has no contingency line. Building (60% of capex) rests on two contractor quotes; cold-storage equipment (22%) rests on a single quote (Frigotec), with no competitive second bid. | A construction cost overrun of even 5-10% — common for this type of build — moves the payback and NPV in Slides 8-9 adversely, and the board sees no exposure to this in the sensitivity table (which only flexes volume). | Add an explicit, justified contingency line to the Slide 6 capex table, and add a capex-overrun scenario to Slide 9 alongside the volume downside/upside cases. |
| 3 | Major | CFO / Decision Maker | Slide 8 | "Payback 3.1 years" is stated next to "NPV EUR 9.8m at 8% discount rate" without saying whether the 3.1-year figure is simple or discounted payback. These are materially different claims. | The board may read 3.1 years as the stronger (discounted) claim when it is the weaker (simple) one, or vice versa — directly affecting how attractive the project looks relative to other capital asks. | State explicitly on Slide 8 whether the payback figure is simple or discounted; if simple, show the discounted payback alongside it. |
| 4 | Major | Logician / Evidence Auditor | Slide 4 (GDP clause 7.2) vs Slide 9 (70% volume floor tied to losing two anchor customers) | The deck rejects the Halle third-party option because it lacks GDP certification required by two of the five largest customers, and pins the sensitivity break-even to losing those same two customers — but never confirms that the new Leipzig hub will itself hold GDP certification by the Q3 2028 go-live, or what that costs/takes. | If Leipzig's own GDP certification slips past go-live, the two anchor customers the whole volume case depends on may not ship there — which is exactly the scenario Slide 9 says flips the answer. The deck doesn't show this risk is covered. | Add a line (Slide 6 or 10) confirming Leipzig's GDP-certification scope, cost, and timeline relative to the Q3 2028 start. |
| 5 | Minor | CFO | Slide 10 | 38-staff hiring plan lands Q4 2027, ~3 quarters before Q3 2028 operations — plausible for training/ramp but not explained. | Implementation detail; doesn't change the board's decision. | Add one line on Slide 10 noting the hiring lead time is for training/certification ramp. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Transport savings (annual) | Slide 5 title: "EUR 1.1m" | Slide 7 table: "1.3" (EUR m/year) | 0.2m |
| Total operating savings (annual) | Slide 7 title: "EUR 3.4m" | Slide 7 table total: "3.6" (EUR m/year) | 0.2m |

## Missing outside view
- Payback/NPV comparables: no benchmark is offered for what comparable cold-chain second-hub builds have actually achieved on payback period or capex-per-pallet-capacity. (Company is fictional, so no real benchmark exists to cite here — but in a live deck this would be the first thing a CFO on the board asks for.)
- Transport rate assumption: the EUR 1.62/pallet-km bracket (Slide 5) is sourced to "2025 carrier rates" with no indication of how it tracks against current/forward rates for the 2029+ savings period.

## Premortem
1. **(External)** The eastward growth trend (62% of new volume since 2023) that justifies a 10-year capacity runway reverses or plateaus — Slide 9's sensitivity tests overall volume decline but not a geographic mix shift back toward Kassel-proximate customers, which would leave Leipzig oversized while Kassel stays constrained.
2. **(Internal — incentives)** Kassel site management, whose overtime budget and visible capacity pressure disappear under this plan, has no stated incentive to actively move volume to Leipzig; the deck names a project owner (COO) but not who is accountable for the Kassel-to-Leipzig handover or how Kassel's metrics change once overtime is "saved away."
3. **(Internal — execution)** Hiring and GDP-certifying the Leipzig site in time for Q3 2028 go-live slips, delaying the two anchor customers the business case depends on (see finding #4) and pushing the payback clock without anyone owning that specific risk.

## What is good and must survive
- Single-page recommendation with capex, payback, NPV, and owner stated upfront (Slide 1) — the right structure for a board deck.
- Historical trend data on Slide 2 is sourced and dated (Harrow WMS/payroll, extracted 2026-08-14) — not an unsupported assertion.
- Real options comparison (Slide 4) with a concrete, contractual reason for rejecting the cheaper alternative (GDP clause 7.2) rather than a hand-wave.
- Downside/upside sensitivity (Slide 9) with a break-even condition tied to a specific, checkable business event (losing two named-tier customers), not just a generic volume haircut.
- Capex table (Slide 6) sums correctly and is sourced to named, dated contractor and equipment quotes.

## What "fixed" looks like
Once reconciled, Slide 1/7 should read: Leipzig removes the Kassel capacity constraint and cuts annual operating cost by EUR 3.4m (EUR 1.1m transport + EUR 2.3m overtime removed) from year two of operations. The EUR 14.0m capex payback and EUR 9.8m NPV in Slides 8-9 must be recomputed against this confirmed EUR 3.4m figure — not the EUR 3.6m currently sitting in the Slide 7 table — before those numbers go in front of the board.

---

**CFO bottom line for Friday: not ready.** The two unreconciled savings figures are the kind of thing a board member finds in thirty seconds by comparing Slide 5 to Slide 7, and once found, it undermines confidence in every number downstream (Slides 8 and 9) even though the deck's structure and sourcing are otherwise solid. Fix the reconciliation and rerun the NPV/payback, add a capex contingency line, and confirm Leipzig's own GDP certification timeline — those are the three things I'd want closed before this goes out.


## Files in work dir after run

- pr-04-input.md
