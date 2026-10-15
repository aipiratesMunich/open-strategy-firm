# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Release or Release with fixes. | NO | "**Verdict:** Return" |
| Must: no Blocker findings. | NO | Finding #1 is listed as "/ 1 / **Blocker** / Skeptical CFO / ..." |
| Must: every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo. | yes | Each Major (#2-#5) has a populated 'Consequence if unfixed' cell, e.g. #2: "the recommendation on decision #2 is undefended"; figures used (2.9+2.4=5.3, 5.3/62=8.5%, 13.1%, €2.4m, €3.10/order) are internally consistent and match the memo's disclosed numbers. |
| Must: names what is good and must survive. | yes | Section "What is good and must survive" lists specific strengths: "The core recommendation is specific and actionable...", "The arithmetic ties cleanly end to end..." |
| Must not: demand a named framework, more length, or more slides. | yes | No finding asks for a named framework, additional length, or more slides; fixes requested are sentence-level rewrites and added labels. |
| Must not: flag the stated uncertainty or the explicit assumptions as weaknesses. | yes | The review uses the memo's own disclosed range (2.5-3.3m) to stress-test the payback point estimate rather than criticizing the disclosure of the range itself; the 'Numbers that do not tie' section explicitly praises the disclosed arithmetic as "a genuine strength of the draft." |
| Must not: claim numbers do not tie. | yes | "None found — the headline arithmetic is internally consistent: 2.9m + 2.4m = 5.3m; 5.3/62 = 8.5%; 80 − 62 − 5.3 = 12.7m gap..." |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Return
**In one line:** The payback claim for the €1.2m central-kitchen investment doesn't survive a recompute using the memo's own disclosed revenue range, and the board's second decision (target vs. margin floor) is resolved on one unsupported sentence.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and should the board revisit the 2031 revenue target or the margin floor? (given, stated in the "To" line)
**Answer the draft gives:** Fund catering (€1.2m) and a delivery pilot (€0.3m); don't fund suburban stores or franchising; revisit the 2031 target, not the floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Skeptical CFO | "Why catering," payback sentence | "The kitchen pays back in the fourth year" uses only the 2.9m base case. Scaling the memo's own year-by-year trajectory to the bottom of its own stated range (2.5m by 2031) gives cumulative net contribution of ~€1.06m by end-2030 — short of the €1.2m outlay. Payback likely slips to year five. | CEO tells the board a €1.2m investment pays back in four years; a board member who re-runs the memo's own numbers at the low end of its own range gets a different answer, and the memo's credibility goes with it. | State the payback range, not a point estimate: "year four in the base case, year five if 2031 catering revenue lands at the bottom of our 2.5–3.3m range." |
| 2 | Major | Logician | "What it adds up to," final two sentences | The recommendation to revisit the 2031 target rather than the margin floor rests on one assertion — "every option that needs a lower floor also carries the weakest evidence" — that isn't demonstrated and runs the wrong way: suburban margin (13.1%) comes from actual 2025 P&L and franchise royalties come from three real offers, while the catering/delivery 2031 numbers are themselves projections. | The board is explicitly asked to decide this at the meeting; a demanding board member reverses the logic in under a minute and the recommendation on decision #2 is undefended. | Quantify what a 1pp lower floor would be worth in suburban revenue, and compare evidence quality explicitly (actual P&L vs. projection), before recommending which lever to move. |
| 3 | Major | Evidence Auditor | "Why catering" | No outside view: the 2.5–3.3m 2031 catering range is built entirely from internal sales data, interviews and bottom-up/top-down math. The delivery section cites two regional chains' actual results; catering has no equivalent benchmark. | The base case could be a hoped-for case rather than a likely one, and nobody outside the room can sense-check it against what other operators actually achieved. | Add a comparable benchmark (another regional bakery/caterer's launch), or state plainly that none was found and widen the stated uncertainty accordingly. |
| 4 | Major | Evidence Auditor / Logician | "Why a delivery pilot" | The €2.4m 2031 estimate assumes the 10 non-piloted stores (of 18) perform like the 8 pilot stores — which were deliberately chosen for the *highest* order density. Lower-density stores reaching 60 orders/day is not tested. | The headline delivery number could overstate what a full rollout actually delivers, and nothing in the memo flags this as a risk even though the pilot's own selection criteria create it. | State the €2.4m as conditional on density-adjusted performance, or give a range that reflects weaker results in lower-density stores. |
| 5 | Major | Premortem | "What would change our view" | The section gives volume triggers only. It omits the three likeliest two-year failure modes: delivery-platform fee increases eroding the €3.10/order contribution, central-kitchen ramp-up/execution risk denting the 32% margin, and a competitor response in office catering compressing growth. | If any of these hits, the board has no pre-agreed trigger to revisit the investment — the memo only told it what to watch on volume. | Add at least one cost-side trigger (e.g., "if platform fees rise enough to cut contribution below €2.50/order") alongside the volume triggers already given. |
| 6 | Minor | Evidence Auditor | "Why a delivery pilot," rollout parenthetical | The "€0.6m" figure for full 18-store rollout isn't labelled — capex, incremental opex, or something else is unclear. | Low — it's explicitly deferred to a separate, later board decision. | Label the number. |
| 7 | Minor | Evidence Auditor | "What it adds up to," price-increase figure | A 3% price increase yielding "about €1.1m" is well under the naive €1.86m (3% × €62m); the gap (likely volume loss or limited pricing scope) isn't explained. | Low — this lever is already shown to be insufficient regardless. | Add one sentence on method. |
| 8 | Minor | Evidence Auditor | "What would change our view," catering threshold | The "40% of office customers sign framework agreements in six months" trigger isn't sourced or reasoned. | Low — doesn't change the recommendation. | State why 40%/six months is the right bar (e.g., minimum needed to hit the €1.6m year-one trajectory). |

## Numbers that do not tie

None found — the headline arithmetic is internally consistent: 2.9m + 2.4m = 5.3m; 5.3/62 = 8.5%; 80 − 62 − 5.3 = 12.7m gap; 1.1m + 0.9m is under a quarter of 12.7m. This is a genuine strength of the draft (see below) and should be preserved, not revisited.

## Missing outside view

- **Catering 2031 revenue (2.5–3.3m):** no comparison to what other bakeries or caterers have achieved launching a dedicated corporate-catering kitchen. The delivery section has this comparison (two regional chains); catering does not.
- **Suburban margin recovery:** no view on whether other operators have closed a ~1pp margin gap on suburban stores through format or cost changes — relevant to whether decision #2 should really favor lowering the target over the floor.

## Premortem

1. **Central-kitchen ramp-up risk.** Staffing, food-safety, and quality-control issues in the first year push the 32% contribution margin down or delay the April 2027 launch — not addressed anywhere in the memo.
2. **Delivery platform economics worsen.** Platform fees rise or terms change, cutting the €3.10/order contribution the entire delivery case depends on — not stress-tested.
3. **Rollout underperforms the pilot.** The 10 non-piloted, lower-density stores don't reach pilot-store economics, so the €2.4m 2031 figure isn't achieved even though the pilot itself "passed" — a direct consequence of finding #4 above.

## What is good and must survive

- The core recommendation is specific and actionable: named owner, budget, and start month for both funded moves, and an explicit no-fund call (with reasons) on the two alternatives.
- The catering growth story pre-empts the obvious objection — it shows quarterly growth continuing *after* office attendance stabilized, ruling out "this is just return-to-office noise."
- The delivery pilot has real kill criteria (60 orders/day *and* no cannibalization of in-store sales) and a genuine outside-view benchmark.
- The arithmetic ties cleanly end to end — unusually disciplined for a one-page memo, and worth calling out to the CEO as a sign the numbers were actually checked.
- "What would change our view" exists at all — most memos skip stating falsifiable thresholds; this one just needs cost-side and competitive triggers added to it.

## What "fixed" looks like

Keep the recommendation and its evidence exactly as is; fix the two load-bearing claims. Payback: "The central kitchen pays back in the fourth year in our base case (€2.9m catering revenue by 2031); at the bottom of our €2.5–3.3m range, payback slips into year five." Decision #2: "We recommend revisiting the 2031 target rather than the margin floor: lowering the floor by one point to clear suburban stores would need to be worth roughly €[X]m in suburban revenue — a number the team should calculate before the board votes — against a €12.7m gap and two unproven growth bets whose own evidence is still being built."


## Files in work dir after run

- pr-03-input.md
